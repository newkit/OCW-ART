"""The README (ART-PROJECT §5.3): a visual overview of the project, generated
from docs/readme/README.template.md, docs/readme/evolution.toml, the day
scripts and the journals by `diary.py readme` (make readme; make publish runs
it after the gallery).

Pictures are the gallery's thumbnails on GitHub Pages (320 px; the hero one
web copy), each linking to its place in the gallery; videos are poster
thumbnails linking to the release assets (GitHub does not play embedded
release videos). Only pictures the built gallery holds are used, so every
link works once the gallery is published. The text passes the mask check
before it is written."""

from __future__ import annotations

import json
import re
import tomllib
from pathlib import Path

from . import core as C
from . import gallery as G
from .core import ART, ART_GH, DAYS, RELEASE, log, run
from .mask import mask, private_findings
from .music import style_for

TEMPLATE = ART / "docs" / "readme" / "README.template.md"
EVOLUTION = ART / "docs" / "readme" / "evolution.toml"
README = ART / "README.md"
THUMBS_PER_DAY = 4
THUMB_W = 200


def release_sizes() -> dict[str, int] | None:
    """{asset: bytes} of the release build-history (None: unknown)."""
    import os
    if os.environ.get("OCW_ART_GH") == "0":
        return None
    r = run(["gh", "release", "view", RELEASE, "-R", ART_GH, "--json", "assets"],
            capture_output=True, text=True, check=False)
    if r.returncode != 0:
        return None
    try:
        return {a["name"]: int(a["size"]) for a in json.loads(r.stdout)["assets"]}
    except (ValueError, KeyError, TypeError):
        return None


def local_sizes(days: list[str]) -> dict[str, int]:
    out = {}
    for p in [*(C.HIST / f"ocw-build-history-{d}.zip" for d in days), *C.OUT.glob("*.mp4")]:
        if p.is_file():
            out[p.name] = p.stat().st_size
    return out


def human(n: float, unit: str = "B") -> str:
    for f, s in ((1e9, "G"), (1e6, "M"), (1e3, "k")):
        if n >= f:
            return f"{n / f:.1f} {s}{unit}".replace(".0 ", " ")
    return f"{n:.0f} {unit}"


def tokens_human(n: int) -> str:
    return f"{n / 1e9:.2f} billion" if n >= 1e9 else f"{n / 1e6:.0f} million"


class Site:
    """What the built gallery holds (so every README picture exists on Pages)."""

    def __init__(self, root: Path | None = None):
        self.root = root or G.site_dir()
        self.index: dict[str, list[str]] = {}

    def items(self, day: str) -> list[str]:
        """The day's files in gallery order (from its page's item list)."""
        if day not in self.index:
            names = []
            p = self.root / "days" / day / "index.html"
            if p.is_file():
                m = re.search(r'type="application/json">(.*?)</script>', p.read_text(), re.S)
                if m:
                    names = [i["f"] for i in json.loads(m.group(1).replace("<\\/", "</"))["items"]]
            self.index[day] = names
        return self.index[day]

    def has(self, day: str, name: str, kind: str = "t") -> bool:
        return (self.root / "days" / day / kind / (name + ".jpg")).is_file()

    def thumb(self, day: str, name: str, kind: str = "t") -> str:
        return f"{G.PAGES_URL}days/{day}/{kind}/{G.q(name)}.jpg"

    def link(self, day: str, name: str) -> str:
        """The picture in the gallery's lightbox (#N), else the day page."""
        names = self.items(day)
        n = names.index(name) + 1 if name in names else 0
        return f"{G.PAGES_URL}days/{day}/" + (f"#{n}" if n else "")


def img(src: str, alt: str, width: int = THUMB_W) -> str:
    return f'<img src="{src}" width="{width}" alt="{G.esc(alt)}">'


def best_pictures(day: str, sc: dict, site: Site, n: int = THUMBS_PER_DAY) -> list[str]:
    """The hero, then one still per chapter of the day script spread over the
    day, else pictures spread evenly over the day (all in the gallery)."""
    out = []

    def add(name):
        if name and name not in out and Path(name).suffix.lower() in G.IMAGE and site.has(day, name):
            out.append(name)
    add(sc.get("hero"))
    stills = []  # one still per chapter of the day script, in story order
    for ch in sc.get("chapter", []):
        for shot in ch.get("shots", []):
            f = shot.get("file") or (shot.get("split") or [None, None])[1]
            if f and "/" not in f and f not in out and Path(f).suffix.lower() in G.IMAGE and site.has(day, f):
                stills.append(f)
                break
    pics = [x for x in site.items(day) if Path(x).suffix.lower() in G.IMAGE and site.has(day, x)]
    for pool in (stills, pics):  # spread evenly over the story, else over the day
        want = n - len(out)
        if want <= 0 or not pool:
            continue
        idx = sorted({round(i * (len(pool) - 1) / max(1, want - 1)) for i in range(want)}) \
            if len(pool) > want else range(len(pool))
        for i in idx:
            add(pool[i])
    return out[:n]


def journal_of(day: str) -> dict:
    p = C.HIST / day / "journal.json"
    try:
        return json.loads(p.read_text()) if p.is_file() else {}
    except ValueError:
        return {}


def script_of(day: str) -> dict:
    p = DAYS / f"{day}.toml"
    try:
        return tomllib.loads(p.read_text()) if p.is_file() else {}
    except tomllib.TOMLDecodeError:
        return {}


def spec_range(j: dict) -> str:
    """The spec versions of the day: from the features log (the rows added),
    else from the version numbers in the commit subjects, without stray
    outliers at the ends (a subject naming another number)."""
    key = lambda v: tuple(int(x) for x in v.split("."))  # noqa: E731
    vs = sorted({f["version"] for f in j.get("features") or [] if re.fullmatch(r"\d+\.\d+", f.get("version", ""))},
                key=key)
    if not vs:
        vs = sorted({v for v in j.get("spec_versions") or [] if re.fullmatch(r"\d+\.\d+", v)}, key=key)
        num = lambda v: key(v)[0] * 1000 + key(v)[1]  # noqa: E731
        while len(vs) > 2 and num(vs[-1]) - num(vs[-2]) > 50:
            vs.pop()
        while len(vs) > 2 and num(vs[1]) - num(vs[0]) > 50:
            vs.pop(0)
    if not vs:
        return ""
    return f"spec {vs[0]} → {vs[-1]}" if vs[0] != vs[-1] else f"spec {vs[0]}"


def release_link(name: str | None, sizes: dict[str, int]) -> str | None:
    return f"{G.DOWNLOAD}{G.q(name)}" if name and name in sizes else None


# The day's data the README links (ART-PROJECT §5.3): the masked text git tracks in the day folder.
DAY_DATA = (("journal.md", "journal"), ("journal.json", "journal (JSON)"), ("tokens.json", "tokens"),
            ("incidents.md", "incidents"), ("index.md", "index"), ("SHA256SUMS", "checksums"))


def tracked(path: Path) -> bool:
    """True when git tracks the file (so a link in the README works on GitHub)."""
    try:
        # Ask the repository that holds the file (the archive may live in another checkout than the code).
        return bool(run(["git", "-C", str(path.parent), "ls-files", "--error-unmatch", path.name],
                        check=False, capture_output=True).returncode == 0)
    except Exception:
        return path.is_file()


def data_links(day: str, sizes: dict[str, int]) -> list[str]:
    """Every piece of the day's data: the day script, the tracked journal files, the media folder
    (Git LFS) and the gallery zip of the release."""
    out = []
    script = DAYS / f"{day}.toml"
    if script.is_file() and tracked(script):
        out.append(f"[day script](days/{day}.toml)")
    folder = C.HIST / day
    for name, label in DAY_DATA:
        if (folder / name).is_file() and tracked(folder / name):
            out.append(f"[{label}](build-history/{day}/{name})")
    if folder.is_dir() and tracked(folder / "journal.json"):
        out.append(f"[pictures and videos](build-history/{day}/) (Git LFS)")
    gz = f"gallery-{day}.zip"
    if gz in sizes:
        out.append(f"[⇩ gallery zip]({G.DOWNLOAD}{G.q(gz)}) ({human(sizes[gz])})")
    return out


def day_section(day: str, site: Site, sizes: dict[str, int]) -> str:
    sc, j = script_of(day), journal_of(day)
    num = j.get("number")
    title = sc.get("title") or "(the day's story is written at the end of the day)"
    head = f"### Day {num} · {day} — {title}" if num else f"### {day} — {title}"
    lines = [head, ""]
    if sc.get("tagline"):
        lines += [f"*{sc['tagline']}*", ""]
    video = next((n for n in sorted(sizes) if re.fullmatch(rf"ocw-diary-day-\d+-{day}\.mp4", n)), None)
    zip_name = f"ocw-build-history-{day}.zip"
    pics = best_pictures(day, sc, site)
    cells = []
    for i, f in enumerate(pics):
        if i == 0 and video:
            cells.append(f'<a href="{G.DOWNLOAD}{G.q(video)}">{img(site.thumb(day, f), "the day video")}</a><br>'
                         f'▶ <a href="{G.DOWNLOAD}{G.q(video)}">day video</a> ({human(sizes[video])})')
        else:
            cells.append(f'<a href="{site.link(day, f)}">{img(site.thumb(day, f), G.caption_of(f))}</a>')
    if cells:
        lines += ["<table><tr>" + "".join(f'<td align="center" valign="top">{c}</td>' for c in cells)
                  + "</tr></table>", ""]
    links = [f"[Gallery]({G.PAGES_URL}days/{day}/)"]
    if video:
        links.append(f"[▶ Day video]({G.DOWNLOAD}{G.q(video)})")
    if zip_name in sizes:
        links.append(f"[⇩ Day zip]({G.DOWNLOAD}{G.q(zip_name)}) ({human(sizes[zip_name])})")
    else:
        links.append("day zip and video: at the end of the day")
    lines += [" · ".join(links), ""]
    data = data_links(day, sizes)
    if data:
        lines += ["Data: " + " · ".join(data), ""]
    nums = []
    if j.get("commits") is not None:
        nums.append(f"**{len(j['commits'])}** commits")
    if j.get("merges") is not None:
        nums.append(f"**{j['merges']}** merges")
    sr = spec_range(j)
    if sr:
        nums.append(sr)
    nums.append(f"**{j.get('images', len([x for x in site.items(day) if Path(x).suffix.lower() in G.IMAGE]))}**"
                f" pictures")
    if j.get("videos") is not None:
        nums.append(f"**{j['videos']}** videos")
    tok = ((j.get("tokens") or {}).get("total") or {}).get("total")
    if tok:
        nums.append(f"**{tokens_human(tok)}** tokens")
    if num:
        nums.append(f"music: {style_for(num, sc.get('style'))}")
    lines += [" · ".join(nums), ""]
    return "\n".join(lines)


def evolution(site: Site, path: Path | None = None) -> str:
    p = path or EVOLUTION
    pics = tomllib.loads(p.read_text()).get("pic", []) if p.is_file() else []
    cells = []
    for x in pics:
        if not site.has(x["day"], x["file"]):
            log(f"readme: evolution picture {x['day']}/{x['file']} is not in the gallery; left out")
            continue
        cells.append(f'<a href="{site.link(x["day"], x["file"])}">{img(site.thumb(x["day"], x["file"]), x["caption"])}'
                     f'</a><br><sub>{G.esc(x["caption"])}</sub>')
    rows = [cells[i:i + 4] for i in range(0, len(cells), 4)]
    return "\n".join("<table><tr>" + "".join(f'<td align="center" valign="top" width="25%">{c}</td>' for c in r)
                     + "</tr></table>" for r in rows)


def hero(site: Site, sizes: dict[str, int], days: list[str]) -> str:
    """The newest finished day's hero as a wide web copy, linking to the diary video."""
    diary = "ocw-build-diary.mp4"
    for d in reversed(days):
        h = script_of(d).get("hero")
        if h and site.has(d, h, "w"):
            target = f"{G.DOWNLOAD}{diary}" if diary in sizes else f"{G.PAGES_URL}days/{d}/"
            return (f'<p align="center"><a href="{target}">{img(site.thumb(d, h, "w"), "The OCW Build Diary", 860)}'
                    f'</a></p>')
    return ""


def totals(days: list[str], sizes: dict[str, int]) -> str:
    js = [journal_of(d) for d in days]
    commits = sum(len(j.get("commits") or []) for j in js)
    pics = sum(j.get("images") or 0 for j in js)
    vids = sum(j.get("videos") or 0 for j in js)
    tok = sum(((j.get("tokens") or {}).get("total") or {}).get("total") or 0 for j in js)
    diary = sizes.get("ocw-build-diary.mp4")
    return (f"**{len(days)} build days** · **{commits}** commits · **{pics}** pictures · **{vids}** videos · "
            f"**{tokens_human(tok)}** tokens" + (f" · the diary video: {human(diary)}" if diary else ""))


def build(sizes: dict[str, int] | None | bool = False, site: Site | None = None, secrets=None,
          write: bool = True) -> str:
    """Generates README.md; raises SystemExit when a private pattern would leak."""
    days = [d for d in G.gallery_days() if (C.HIST / d / "journal.json").is_file()]
    if sizes is False:
        sizes = release_sizes()
    if sizes is None:
        sizes = local_sizes(days)
    site = site or Site()
    text = TEMPLATE.read_text()
    parts = {"hero": hero(site, sizes, days), "totals": totals(days, sizes), "evolution": evolution(site),
             "days": "\n".join(day_section(d, site, sizes) for d in reversed(days)).rstrip("\n")}
    for k, v in parts.items():
        text = text.replace("{{" + k + "}}", mask(v, secrets))
    found = private_findings(text, secrets)
    if found:
        raise SystemExit("readme: private patterns (values not shown): "
                         + ", ".join(f"line {n}: {k}" for n, k in found))
    if write:
        README.write_text(text)
        log(f"readme: {README} ({len(text) / 1e3:.0f} kB, {len(days)} days)")
    return text
