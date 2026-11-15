"""The gallery (ART-PROJECT §6): a static web site of the archive's pictures
and videos, published on GitHub Pages of newkit/OCW-ART.

    build    thumbnails (320 px), web copies (1280 px) and video poster frames
             of every day, incremental (keyed on each source's size and
             mtime), in build-history/.work/gallery/; the pages from site/
    publish  per day a small gallery-DAY.zip of its thumbnails and web copies
             (only when it changed) and gallery-pages.zip (the pages) to the
             release build-history; then the workflow .github/workflows/
             gallery.yml unpacks them and deploys them to Pages
    serve    a local preview of the built site

The size guard keeps the site under --max-mb (default 900; Pages allows
1 GB): when the budget is reached, the oldest days get smaller web copies
first (960 px), then thumbnails only, the newest day last (§6.3).
Media never go into git for the gallery: the site is built here and travels
through the release; the raw MP4s stay in the day zips."""

from __future__ import annotations

import datetime as dt
import hashlib
import html
import json
import os
import re
import shutil
import subprocess
import tomllib
import urllib.parse
import zipfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from string import Template

from . import core as C
from .core import ART, ART_GH, ASSETS, DAYS, IMAGE, RELEASE, VIDEO, log, run
from .mask import mask, private_findings

SITE_SRC = ART / "site"  # the templates: page.html, gallery.css, gallery.js
PAGES_URL = "https://newkit.github.io/OCW-ART/"
REPO_URL = f"https://github.com/{ART_GH}"
RELEASE_PAGE = f"{REPO_URL}/releases/tag/{RELEASE}"
DOWNLOAD = f"{REPO_URL}/releases/download/{RELEASE}/"
WORKFLOW = "gallery.yml"

THUMB_W, THUMB_Q = 320, 4  # JPEG -q:v (2 best … 31): about 10-15 KB at 320 px
# Web copies per tier (§6.3): (width, -q:v); "thumbs" has none.
TIERS = {"full": (1280, 3), "reduced": (960, 6), "thumbs": None}
TIER_ORDER = ["full", "reduced", "thumbs"]
DEFAULT_MAX_MB = 900
MAX_JOBS = 4  # deb: at most 4 ffmpeg processes, niced
DEFAULT_JOBS = 3
PAGE_ALLOWANCE = 200_000  # bytes kept free for the pages when planning tiers


def gallery_dir() -> Path:
    return C.WORK / "gallery"


def site_dir() -> Path:
    return gallery_dir() / "site"


def cache_dir() -> Path:
    return gallery_dir() / "cache"


# ------------------------------------------------------------------ items


def caption_of(name: str) -> str:
    """A file name as a caption: no HHMMSS- prefix, no extension, words."""
    stem = re.sub(r"^\d{6}-", "", Path(name).stem)
    return re.sub(r"\s+", " ", stem.replace("-", " ").replace("_", " ")).strip() or name


def script_of(day: str) -> dict:
    p = DAYS / f"{day}.toml"
    try:
        return tomllib.loads(p.read_text()) if p.is_file() else {}
    except tomllib.TOMLDecodeError:
        return {}


def script_notes(sc: dict) -> dict[str, str]:
    """{file: "In the video: chapter – note"} for the shots the day script uses."""
    out = {}
    if sc.get("hero"):
        out[sc["hero"]] = "In the video: the title picture"
    for ch in sc.get("chapter", []):
        for shot in ch.get("shots", []):
            files = shot.get("split") or ([shot["file"]] if shot.get("file") else [])
            for f in files:
                if "/" in f:
                    continue
                note = f"In the video: {ch.get('title', '')}".rstrip(": ")
                if shot.get("note"):
                    note += f" – “{shot['note']}”"
                out.setdefault(f, note)
    return out


def gallery_days() -> list[str]:
    return sorted(d.name for d in C.HIST.glob("????-??-??") if d.is_dir()
                  and re.fullmatch(r"\d{4}-\d{2}-\d{2}", d.name))


def items_of(day: str, secrets=None) -> tuple[list[dict], list[str]]:
    """The day's pictures and videos in time order, and the names skipped
    because the file name itself holds a private pattern (never published)."""
    d = C.HIST / day
    notes = script_notes(script_of(day))
    out, skipped = [], []
    for f in sorted(d.iterdir()) if d.is_dir() else []:
        ext = f.suffix.lower()
        if not f.is_file() or ext not in IMAGE | VIDEO:
            continue
        st = f.stat()
        if st.st_size == 0:
            continue  # an aborted capture: kept, not shown
        if private_findings(f.name, secrets):
            skipped.append(f.name)
            continue
        m = re.match(r"^(\d{2})(\d{2})(\d{2})-", f.name)
        out.append({"day": day, "file": f.name, "src": f, "kind": "video" if ext in VIDEO else "image",
                    "time": f"{m.group(1)}:{m.group(2)}:{m.group(3)}" if m else "",
                    "key": f"{st.st_size}-{st.st_mtime_ns}", "bytes": st.st_size,
                    "caption": mask(caption_of(f.name), secrets),
                    "note": mask(notes.get(f.name, ""), secrets)})
    out.sort(key=lambda i: (i["time"], i["file"]))
    return out, skipped


# ------------------------------------------------------------- the images


def variant_name(tier: str) -> str | None:
    spec = TIERS[tier]
    return f"w{spec[0]}" if spec else None


def out_path(item: dict, variant: str) -> Path:
    return cache_dir() / item["day"] / variant / (item["file"] + ".jpg")


def scale(width: int) -> str:
    return f"scale='min({width},iw)':-2:flags=lanczos"


def probe_seconds(src: Path) -> float:
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of",
                        "default=nw=1:nk=1", str(src)], capture_output=True, text=True)
    try:
        return float(r.stdout.strip())
    except ValueError:
        return 0.0


def nice_prefix() -> list[str]:
    pre = ["nice", "-n", "10"]
    if shutil.which("ionice"):
        pre = ["ionice", "-c", "3", *pre]
    return pre


def encode(item: dict, variants: list[str], seconds: float | None = None) -> None:
    """One ffmpeg run: the thumbnail and/or a web copy of a picture, or of a
    video's poster frame (at 40 % of its length). Writes atomically."""
    outs = []
    for v in variants:
        w, q = (THUMB_W, THUMB_Q) if v == "t" else next(s for s in TIERS.values() if s and f"w{s[0]}" == v)
        dest = out_path(item, v)
        dest.parent.mkdir(parents=True, exist_ok=True)
        outs.append((v, w, q, dest, dest.with_name(dest.name + ".tmp.jpg")))
    pre = []
    if item["kind"] == "video" and seconds:
        pre = ["-ss", f"{seconds * 0.4:.2f}"]
    n = len(outs)
    graph = f"[0:v]split={n}" + "".join(f"[s{i}]" for i in range(n)) + ";" + ";".join(
        f"[s{i}]{scale(w)}[o{i}]" for i, (_, w, *_r) in enumerate(outs))
    cmd = [*nice_prefix(), "ffmpeg", "-v", "error", "-nostdin", "-y", "-threads", "1", *pre, "-i", str(item["src"]),
           "-filter_complex", graph]
    for i, (_, _, q, _, tmp) in enumerate(outs):
        cmd += ["-map", f"[o{i}]", "-frames:v", "1", "-q:v", str(q), str(tmp)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0 or not all(o[4].is_file() and o[4].stat().st_size for o in outs):
        for o in outs:
            o[4].unlink(missing_ok=True)
        raise RuntimeError((r.stderr or "no output").strip().splitlines()[-1][:200])
    for _, _, _, dest, tmp in outs:
        tmp.replace(dest)


class Cache:
    """manifest.json: per "DAY/file" the source key, the variants built
    (bytes), the video length and the last error."""

    def __init__(self):
        self.path = cache_dir() / "manifest.json"
        try:
            self.data = json.loads(self.path.read_text())
        except (OSError, ValueError):
            self.data = {}

    def entry(self, item: dict) -> dict:
        k = f"{item['day']}/{item['file']}"
        e = self.data.get(k)
        if not e or e.get("key") != item["key"]:
            e = self.data[k] = {"key": item["key"], "variants": {}}
        return e

    def missing(self, item: dict, variants: list[str]) -> list[str]:
        e = self.entry(item)
        return [v for v in variants if v not in e["variants"] or not out_path(item, v).is_file()]

    def save(self):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        tmp = self.path.with_suffix(".tmp")
        tmp.write_text(json.dumps(self.data, indent=0, sort_keys=True))
        tmp.replace(self.path)


def ensure(cache: Cache, items: list[dict], variants_of, jobs: int = DEFAULT_JOBS, encoder=None) -> int:
    """Builds the missing variants of every item (variants_of(item) -> list),
    at most `jobs` (≤ 4) ffmpeg processes at once. Returns the number of
    ffmpeg runs; failures are recorded in the manifest, not raised."""
    encoder = encoder or encode
    todo = []
    for it in items:
        need = cache.missing(it, variants_of(it))
        if need:
            todo.append((it, need))
    if not todo:
        return 0
    log(f"gallery: {len(todo)} pictures/posters to make ({min(jobs, MAX_JOBS)} at once)")

    def one(job):
        it, need = job
        e = cache.entry(it)
        try:
            if it["kind"] == "video" and "seconds" not in e:
                e["seconds"] = round(probe_seconds(it["src"]), 2)
            encoder(it, need, e.get("seconds"))
            for v in need:
                e["variants"][v] = out_path(it, v).stat().st_size
            e.pop("error", None)
        except Exception as ex:  # one broken file must not stop the gallery
            e["error"] = mask(str(ex))[:200]
            log(f"gallery: {it['day']}/{it['file']}: {e['error']}")
    done = 0
    with ThreadPoolExecutor(max_workers=max(1, min(jobs, MAX_JOBS))) as pool:
        for _ in pool.map(one, todo):
            done += 1
            if done % 200 == 0:
                cache.save()
                log(f"gallery: {done}/{len(todo)}")
    cache.save()
    return len(todo)


# --------------------------------------------------------------- the budget


def plan_tiers(days: list[str], size, budget: int, fixed: int = 0) -> dict[str, str]:
    """The tier of each day (§6.3): every day "full" while the site fits the
    budget; else the oldest days step down to "reduced" one by one, then to
    "thumbs", the newest day last. size(day, tier) is the bytes of the
    day's media in that tier (thumbnails included). Raises SystemExit when
    even thumbnails only do not fit."""
    tiers = {d: "full" for d in days}

    def total():
        return fixed + sum(size(d, tiers[d]) for d in days)
    for tier in TIER_ORDER[1:]:
        for d in days:  # oldest first
            if total() <= budget:
                return tiers
            tiers[d] = tier
    if total() > budget:
        raise SystemExit(f"gallery: {total() / 1e6:.0f} MB with thumbnails only is over the budget of "
                         f"{budget / 1e6:.0f} MB (--max-mb); raise it below 1000 or thin out the thumbnails "
                         f"(ART-PROJECT §6.3)")
    return tiers


# ------------------------------------------------------------- the release


def release_assets() -> set[str] | None:
    """Names of the assets on the release build-history (None: unknown,
    OCW_ART_GH=0 or gh failed)."""
    if os.environ.get("OCW_ART_GH") == "0":
        return None
    r = run(["gh", "release", "view", RELEASE, "-R", ART_GH, "--json", "assets"],
            capture_output=True, text=True, check=False)
    if r.returncode != 0:
        return None
    try:
        return {a["name"] for a in json.loads(r.stdout)["assets"]}
    except (ValueError, KeyError, TypeError):
        return None


def day_links(day: str, assets: set[str] | None) -> dict:
    """The day's zip and video on the release, or None while not published
    (without the release's list: the local files that publish uploads)."""
    zip_name = f"ocw-build-history-{day}.zip"
    if assets is None:
        names = {p.name for p in C.HIST.glob(zip_name)} | {p.name for p in C.OUT.glob(f"ocw-diary-day-*-{day}.mp4")}
    else:
        names = assets
    video = next((n for n in sorted(names) if re.fullmatch(rf"ocw-diary-day-\d+-{day}\.mp4", n)), None)
    return {"zip": zip_name if zip_name in names else None, "video": video,
            "diary": "ocw-build-diary.mp4" if assets is None or "ocw-build-diary.mp4" in assets else None}


# --------------------------------------------------------------- the pages


def esc(s) -> str:
    return html.escape(str(s), quote=True)


def q(name: str) -> str:
    return urllib.parse.quote(name)


def page(title: str, body: str, root: str, description: str = "") -> str:
    tpl = Template((SITE_SRC / "page.html").read_text())
    return tpl.substitute(title=esc(title), description=esc(description), root=root, body=body,
                          footer=footer(root))


def footer(root: str) -> str:
    return (f'<p>The <a href="{REPO_URL}">OCW Build Diary</a> is the art project of '
            f'<a href="https://github.com/newkit/OCW">Open Cycling World</a>: every picture and video made '
            f'while building it, day by day. Full-size files: the day zips and videos on the release '
            f'<a href="{RELEASE_PAGE}">build-history</a>.</p>'
            f'<p>Code: MIT OR Apache-2.0 (<a href="{REPO_URL}/blob/main/LICENSE-MIT">MIT</a>, '
            f'<a href="{REPO_URL}/blob/main/LICENSE-APACHE">Apache-2.0</a>). The pictures are OCW renders; '
            f'map and world renders contain OpenStreetMap-derived data: © '
            f'<a href="https://www.openstreetmap.org/copyright">OpenStreetMap contributors</a> (ODbL).</p>'
            f'<p class="gen">Built {dt.datetime.now().astimezone().strftime("%Y-%m-%d %H:%M %z")}.</p>')


def fmt_mb(n: int) -> str:
    return f"{n / 1e6:.0f} MB" if n >= 10e6 else f"{n / 1e6:.1f} MB"


def day_info(day: str) -> dict:
    sc = script_of(day)
    j = {}
    p = C.HIST / day / "journal.json"
    if p.is_file():
        try:
            j = json.loads(p.read_text())
        except ValueError:
            j = {}
    return {"title": sc.get("title", ""), "tagline": sc.get("tagline", ""), "hero": sc.get("hero"),
            "number": j.get("number"), "commits": len(j.get("commits") or []), "merges": j.get("merges")}


def hero_of(items: list[dict], hero: str | None, have) -> dict | None:
    pics = [i for i in items if have(i, "t")]
    for i in pics:
        if i["file"] == hero:
            return i
    imgs = [i for i in pics if i["kind"] == "image"] or pics
    return imgs[len(imgs) // 2] if imgs else None


def release_link(name: str | None, label: str, missing: str) -> str:
    if name:
        return f'<a class="btn" href="{DOWNLOAD}{q(name)}">{esc(label)}</a>'
    return f'<span class="btn off" title="{esc(missing)}">{esc(label)}</span>'


def day_page(day: str, info: dict, items: list[dict], tier: str, links: dict, prev_day, next_day,
             have) -> str:
    web = variant_name(tier)
    rows, data = [], []
    for n, it in enumerate(items):
        t_ok = have(it, "t")
        w_ok = bool(web) and have(it, web)
        thumb = f"t/{q(it['file'])}.jpg" if t_ok else None
        big = f"w/{q(it['file'])}.jpg" if w_ok else thumb
        data.append({"t": thumb, "w": big, "f": it["file"], "k": it["kind"], "time": it["time"],
                     "c": it["caption"], "n": it["note"], "s": it.get("seconds")})
        cls = "item video" if it["kind"] == "video" else "item"
        img = (f'<img loading="lazy" src="{thumb}" alt="{esc(it["caption"])}">' if thumb
               else '<span class="noimg">no preview</span>')
        play = '<span class="play" aria-hidden="true"></span>' if it["kind"] == "video" else ""
        dur = f' · {it["seconds"]:.0f} s' if it.get("seconds") else ""
        rows.append(f'<figure class="{cls}" id="i{n}"><a href="{big or "#"}" data-i="{n}">{img}{play}</a>'
                    f'<figcaption><time>{esc(it["time"][:5])}</time> {esc(it["caption"])}{dur}</figcaption>'
                    f'</figure>')
    n_img = sum(i["kind"] == "image" for i in items)
    n_vid = len(items) - n_img
    title = f"Day {info['number']} · {day}" if info.get("number") else day
    nav = ['<a href="../../">All days</a>']
    if prev_day:
        nav.append(f'<a href="../{prev_day}/" rel="prev">← {prev_day}</a>')
    if next_day:
        nav.append(f'<a href="../{next_day}/" rel="next">{next_day} →</a>')
    payload = json.dumps({"day": day, "zip": links["zip"], "video": links["video"], "download": DOWNLOAD,
                          "release": RELEASE_PAGE, "items": data}, ensure_ascii=False).replace("</", "<\\/")
    tier_note = ""
    if tier != "full":
        tier_note = (f'<p class="note">To keep the gallery under its size budget this day shows '
                     f'{"smaller web copies" if tier == "reduced" else "thumbnails only"}; every file is '
                     f'full size in the day zip.</p>')
    body = (f'<header class="day"><nav>{" ".join(nav)}</nav>'
            f'<h1>{esc(title)}</h1>'
            + (f'<p class="lead">{esc(mask(info["title"]))}</p>' if info.get("title") else "")
            + f'<p class="meta">{n_img} pictures · {n_vid} videos'
            + (f' · {info["commits"]} commits' if info.get("commits") else "") + '</p>'
            f'<p class="links">{release_link(links["video"], "▶ Day video", "rendered at the end of the day")} '
            f'{release_link(links["zip"], "⇩ Day zip (full size)", "published at the end of the day")}</p>'
            f'{tier_note}</header>'
            f'<main class="grid">{"".join(rows)}</main>'
            f'<script id="items" type="application/json">{payload}</script>')
    return page(f"{title} – OCW Build Diary", body, "../../",
                f"{n_img} pictures and {n_vid} videos of {day}, building Open Cycling World")


def index_page(cards: list[dict], total: dict, links: dict) -> str:
    rows = []
    for c in reversed(cards):  # newest first
        img = (f'<img loading="lazy" src="days/{c["day"]}/t/{q(c["hero"]["file"])}.jpg" alt="">'
               if c["hero"] else '<span class="noimg"></span>')
        title = f"Day {c['number']}" if c.get("number") else c["day"]
        vid = (f' <a class="btn" href="{DOWNLOAD}{q(c["links"]["video"])}">▶ Day video</a>'
               if c["links"]["video"] else "")
        rows.append(f'<article class="card"><a class="hero" href="days/{c["day"]}/">{img}</a>'
                    f'<div class="txt"><h2><a href="days/{c["day"]}/">{esc(title)} · {c["day"]}</a></h2>'
                    + (f'<p class="lead">{esc(mask(c["title"]))}</p>' if c.get("title") else "")
                    + f'<p class="meta">{c["images"]} pictures · {c["videos"]} videos'
                    + (f' · {c["commits"]} commits' if c.get("commits") else "")
                    + f'</p><p class="links"><a class="btn" href="days/{c["day"]}/">Gallery</a>{vid}</p>'
                    f'</div></article>')
    diary = (f'<a class="btn" href="{DOWNLOAD}{links["diary"]}">▶ The whole diary</a> ' if links.get("diary")
             else "")
    body = (f'<header class="top"><img class="logo" src="assets/ocw.svg" alt="">'
            f'<h1>OCW Build Diary</h1><p class="lead">How Open Cycling World was built, one day at a time: '
            f'every screenshot and video of the build, in the order they were made.</p>'
            f'<p class="meta">{len(cards)} days · {total["images"]} pictures · {total["videos"]} videos</p>'
            f'<p class="links">{diary}<a class="btn" href="{RELEASE_PAGE}">Day zips and videos</a></p></header>'
            f'<main class="days">{"".join(rows)}</main>')
    return page("OCW Build Diary", body, "./",
                "Every picture and video made while building Open Cycling World, day by day")


# ---------------------------------------------------------------- the build


def link_or_copy(src: Path, dest: Path):
    dest.parent.mkdir(parents=True, exist_ok=True)
    try:
        os.link(src, dest)
    except OSError:
        shutil.copy2(src, dest)


def build(max_mb: float = DEFAULT_MAX_MB, jobs: int = DEFAULT_JOBS, assets: set[str] | None | bool = False,
          secrets=None, encoder=None, days: list[str] | None = None) -> dict:
    """Builds the site into build-history/.work/gallery/site/ (atomically
    replaced). Returns a summary: days, items, bytes, tiers, ffmpeg runs,
    failures, skipped names."""
    if assets is False:
        assets = release_assets()
    days = days or gallery_days()
    cache = Cache()
    per_day, skipped = {}, []
    for d in days:
        its, sk = items_of(d, secrets)
        per_day[d] = its
        skipped += [f"{d}/{n}" for n in sk]
    days = [d for d in days if per_day[d]]
    all_items = [i for d in days for i in per_day[d]]
    runs = ensure(cache, all_items, lambda it: ["t", variant_name("full")], jobs, encoder)

    def have(it, v):
        e = cache.data.get(f"{it['day']}/{it['file']}", {})
        return e.get("key") == it["key"] and v in e.get("variants", {}) and out_path(it, v).is_file()
    for it in all_items:
        it["seconds"] = cache.data.get(f"{it['day']}/{it['file']}", {}).get("seconds")

    def size(d, tier):
        v = variant_name(tier)
        if v:
            nonlocal runs
            runs += ensure(cache, per_day[d], lambda it: [v], jobs, encoder)
        return sum(cache.data[f"{d}/{i['file']}"]["variants"].get(x, 0)
                   for i in per_day[d] for x in ("t", v) if x and have(i, x))
    static = sum(p.stat().st_size for p in SITE_SRC.glob("*") if p.suffix in (".css", ".js")) + \
        (ASSETS / "logos" / "ocw.svg").stat().st_size
    budget = int(max_mb * 1e6)
    tiers = plan_tiers(days, size, budget, static + PAGE_ALLOWANCE)

    out = site_dir()
    new = out.with_name("site.new")
    if new.exists():
        shutil.rmtree(new)
    (new / "assets").mkdir(parents=True)
    for p in SITE_SRC.glob("*"):
        if p.suffix in (".css", ".js"):
            shutil.copy2(p, new / "assets" / p.name)
    shutil.copy2(ASSETS / "logos" / "ocw.svg", new / "assets" / "ocw.svg")
    (new / ".nojekyll").write_text("")
    cards, total = [], {"images": 0, "videos": 0}
    for n, d in enumerate(days):
        its = per_day[d]
        web = variant_name(tiers[d])
        for it in its:
            if have(it, "t"):
                link_or_copy(out_path(it, "t"), new / "days" / d / "t" / (it["file"] + ".jpg"))
            if web and have(it, web):
                link_or_copy(out_path(it, web), new / "days" / d / "w" / (it["file"] + ".jpg"))
        info = day_info(d)
        links = day_links(d, assets)
        (new / "days" / d).mkdir(parents=True, exist_ok=True)
        (new / "days" / d / "index.html").write_text(
            day_page(d, info, its, tiers[d], links, days[n - 1] if n else None,
                     days[n + 1] if n + 1 < len(days) else None, have))
        imgs = sum(i["kind"] == "image" for i in its)
        total["images"] += imgs
        total["videos"] += len(its) - imgs
        cards.append({"day": d, "number": info["number"], "title": info["title"], "commits": info["commits"],
                      "images": imgs, "videos": len(its) - imgs, "links": links,
                      "hero": hero_of(its, info["hero"], have)})
    (new / "index.html").write_text(index_page(cards, total, day_links("", assets)))
    # Every text on the pages passes the mask rules (§2.5): fail before anything is replaced.
    found = []
    for p in sorted(new.rglob("*.html")):
        for line, kind in private_findings(p.read_text(), secrets):
            found.append(f"{p.relative_to(new)}:{line}: {kind}")
    if found:
        shutil.rmtree(new)
        raise SystemExit("gallery: private patterns on the pages (values not shown):\n  " + "\n  ".join(found))
    size_b = sum(p.stat().st_size for p in new.rglob("*") if p.is_file())
    if size_b > budget:
        shutil.rmtree(new)
        raise SystemExit(f"gallery: {size_b / 1e6:.0f} MB is over the budget of {max_mb:.0f} MB")
    if out.exists():
        shutil.rmtree(out)
    new.rename(out)
    failed = sorted(k for k, e in cache.data.items() if e.get("error"))
    summary = {"days": len(days), "items": len(all_items), "bytes": size_b, "tiers": tiers, "ffmpeg_runs": runs,
               "failed": failed, "skipped": skipped, "site": str(out)}
    (gallery_dir() / "summary.json").write_text(json.dumps(summary, indent=1) + "\n")
    degraded = {d: t for d, t in tiers.items() if t != "full"}
    log(f"gallery: {len(all_items)} items of {len(days)} days, {fmt_mb(size_b)} of {max_mb:.0f} MB, "
        f"{runs} ffmpeg runs" + (f", smaller: {degraded}" if degraded else "")
        + (f", {len(failed)} without preview" if failed else "")
        + (f", {len(skipped)} skipped (private name)" if skipped else "") + f" → {out}")
    return summary


# -------------------------------------------------------------- publishing


def digest(folder: Path) -> str:
    h = hashlib.sha256()
    for p in sorted(folder.rglob("*")):
        if p.is_file():
            st = p.stat()
            h.update(f"{p.relative_to(folder).as_posix()} {st.st_size} {st.st_mtime_ns}\n".encode())
    return h.hexdigest()


def zip_folder(dest: Path, root: Path, members: list[Path]):
    tmp = dest.with_suffix(".tmp")
    with zipfile.ZipFile(tmp, "w", zipfile.ZIP_STORED) as z:  # JPEGs do not compress
        for m in members:
            for p in sorted([m] if m.is_file() else m.rglob("*")):
                if p.is_file():
                    z.write(p, p.relative_to(root).as_posix(),
                            compress_type=zipfile.ZIP_DEFLATED if p.suffix in (".html", ".css", ".js", ".svg")
                            else zipfile.ZIP_STORED)
    tmp.replace(dest)


def release_files(assets: set[str] | None) -> list[Path]:
    """The zips to upload: gallery-pages.zip always, gallery-DAY.zip of the
    days whose media changed since the last publish or are missing on the
    release."""
    site, rel = site_dir(), gallery_dir() / "release"
    rel.mkdir(parents=True, exist_ok=True)
    state_p = gallery_dir() / "published.json"
    try:
        state = json.loads(state_p.read_text())
    except (OSError, ValueError):
        state = {}
    out = []
    for dd in sorted((site / "days").iterdir()) if (site / "days").is_dir() else []:
        media = [p for p in (dd / "t", dd / "w") if p.is_dir()]
        name = f"gallery-{dd.name}.zip"
        dg = hashlib.sha256("".join(digest(m) for m in media).encode()).hexdigest()
        if state.get(name) == dg and (rel / name).is_file() and (assets is None or name in assets):
            continue
        zip_folder(rel / name, site, media)
        state[name] = dg
        out.append(rel / name)
    pages = [site / "index.html", site / ".nojekyll", site / "assets", *sorted((site / "days").glob("*/index.html"))]
    zip_folder(rel / "gallery-pages.zip", site, pages)
    out.append(rel / "gallery-pages.zip")
    state_p.write_text(json.dumps(state, indent=1, sort_keys=True) + "\n")
    return out


def publish(max_mb: float = DEFAULT_MAX_MB, jobs: int = DEFAULT_JOBS, wait: bool = False, build_first=True):
    """Build, upload the changed gallery zips to the release, start the Pages workflow."""
    assets = release_assets()
    if build_first:
        build(max_mb, jobs, assets)
    files = release_files(assets)
    for f in files:
        log(f"upload {f.name} ({fmt_mb(f.stat().st_size)})")
    run(["gh", "release", "upload", RELEASE, "-R", ART_GH, "--clobber", *files])
    deploy(wait)


def deploy(wait: bool = False):
    """Starts the workflow that deploys the release's gallery zips to Pages."""
    t0 = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    run(["gh", "workflow", "run", WORKFLOW, "-R", ART_GH, "--ref", "main"])
    log(f"gallery: deploy started ({REPO_URL}/actions/workflows/{WORKFLOW}) → {PAGES_URL}")
    if not wait:
        return
    import time
    for _ in range(30):
        r = run(["gh", "run", "list", "-R", ART_GH, "--workflow", WORKFLOW, "--json", "databaseId,createdAt",
                 "-L", "5"], capture_output=True, text=True, check=False)
        ids = [x["databaseId"] for x in json.loads(r.stdout or "[]") if x["createdAt"] >= t0]
        if ids:
            run(["gh", "run", "watch", str(ids[0]), "-R", ART_GH, "--exit-status"])
            return
        time.sleep(2)
    log("gallery: the workflow run did not show up; check the Actions page")


def serve(port: int = 8000):
    import functools
    import http.server
    d = site_dir()
    if not (d / "index.html").is_file():
        raise SystemExit("no gallery built yet: make gallery")
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(d))
    log(f"gallery preview: http://127.0.0.1:{port}/ (Ctrl-C stops)")
    http.server.ThreadingHTTPServer(("127.0.0.1", port), handler).serve_forever()
