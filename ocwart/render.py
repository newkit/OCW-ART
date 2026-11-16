"""The day video and the diary video (ART-PROJECT §3, §4): contact sheets,
shots, time-lapse, chapters, features roll, end card."""

from __future__ import annotations

import datetime as dt
import hashlib
import random
import re
import shutil
import tomllib
from pathlib import Path

from . import core as C
from . import features as F
from .core import ART, DAYS, ffmpeg, FONTS, FPS, H, log, LOGO, now_meta, PINK, probe_duration, RATE, VIDEO, VIOLET, W
from .journal import incident_text, journal, media_of
from .mask import mask
from .music import Music
from .sfx import sfx_bell, sfx_ding, sfx_pop, sfx_tick, sfx_whoosh, write_wav
from .subtitles import esc, num_fmt, prompt_lines, Subs

# ------------------------------------------------------------------ frames


def norm_still(src: Path, day: str) -> Path:
    """The image (or a video's middle frame) as a 1920x1080 JPEG: fitted over
    a blurred, darkened copy of itself (no black bars)."""
    out = C.WORK / day / "norm" / (src.name + ".jpg")
    if out.exists():
        return out
    out.parent.mkdir(parents=True, exist_ok=True)
    pre = []
    if src.suffix.lower() in VIDEO:
        pre = ["-ss", f"{max(0.0, probe_duration(src) / 2):.2f}"]
    ffmpeg(*pre, "-i", src, "-frames:v", "1", "-filter_complex", FIT, "-q:v", "3", out)
    return out


FIT = (
    f"[0:v]split[a][b];"
    f"[a]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},"
    f"boxblur=24:2,eq=brightness=-0.18:saturation=1.2[bg];"
    f"[b]scale={W}:{H}:force_original_aspect_ratio=decrease[fg];"
    f"[bg][fg]overlay=(W-w)/2:(H-h)/2,setsar=1,format=yuv420p"
)


def sheet(day: str):
    media = [m for m in media_of(day) if m["kind"] != "audio"]
    out = C.WORK / day / "sheets"
    out.mkdir(parents=True, exist_ok=True)
    per = 20
    for i in range(0, len(media), per):
        chunk = media[i : i + per]
        inputs, filt = [], []
        for k, m in enumerate(chunk):
            inputs += ["-i", norm_still(C.HIST / day / m["file"], day)]
            label = m["file"].replace(":", r"\:")[:44]
            filt.append(
                f"[{k}:v]scale=480:270,drawbox=y=240:h=30:color=black@0.7:t=fill,"
                f"drawtext=fontfile={FONTS / 'FiraMono-Regular.ttf'}:text='{label}':"
                f"x=4:y=246:fontsize=15:fontcolor=white[t{k}]"
            )
        for k in range(len(chunk), per):
            filt.append(f"color=black:s=480x270:d=1[t{k}]")
        filt.append("".join(f"[t{k}]" for k in range(per)) + "xstack=inputs=20:layout=" + "|".join(
            f"{(k % 4) * 480}_{(k // 4) * 270}" for k in range(per)
        ) + "[v]")
        target = out / f"sheet-{i // per + 1:02d}.jpg"
        ffmpeg(*inputs, "-filter_complex", ";".join(filt), "-map", "[v]", "-frames:v", "1",
               "-q:v", "4", target)
        log(target)




# ------------------------------------------------------------------- shots

XF = 0.5  # cross-transition between segments, s
ROLL_PAGE_S = 3.6  # a page of the features roll, s
TRANSITIONS = ["pixelize", "slideleft", "circleopen", "wipeup", "smoothleft",
               "radial", "hblur", "squeezeh", "diagtl", "slideup"]
ENC = ["-c:v", "libx264", "-preset", "veryfast", "-crf", "16", "-pix_fmt", "yuv420p",
       "-r", str(FPS)]


def media_path(day: str, name: str) -> Path:
    """A shot's file: the day folder, else a path in this checkout (e.g.
    assets/logos/ocw-512.png), else one in the OCW checkout."""
    p = C.HIST / day / name
    if p.exists():
        return p
    for root in (ART, C.ROOT):
        p = root / name
        if p.exists():
            return p
    raise SystemExit(f"{day}: shot file not found: {name}")


def seeded(name: str) -> random.Random:
    return random.Random(int(hashlib.md5(name.encode()).hexdigest()[:8], 16))


def kenburns(src: Path, seconds: float, out: Path, day: str):
    """A still with a slow zoom and drift (direction from the file name)."""
    still = norm_still(src, day)
    n = max(1, round(seconds * FPS))
    r = seeded(src.name)
    z0, z1 = (1.0, 1.14) if r.random() < 0.6 else (1.14, 1.0)
    dx, dy = r.choice([-1, 1]) * r.uniform(0.2, 0.5), r.uniform(-0.3, 0.3)
    z = f"{z0}+({z1 - z0})*on/{n}"
    x = f"(iw-iw/zoom)/2*(1+{dx:.3f}*(on/{n}-0.5)*2)"
    y = f"(ih-ih/zoom)/2*(1+{dy:.3f}*(on/{n}-0.5)*2)"
    ffmpeg("-i", still, "-filter_complex",
           f"[0:v]scale=3840:2160,zoompan=z='{z}':x='{x}':y='{y}':d={n}:s={W}x{H}:fps={FPS},"
           f"setsar=1,format=yuv420p[v]",
           "-map", "[v]", "-frames:v", str(n), *ENC, out)


def clip(src: Path, start: float, seconds: float, speed: float, out: Path):
    """A video shot: from `start`, `speed` times faster, fitted to 16:9."""
    n = max(1, round(seconds * FPS))
    dur = probe_duration(src)
    loop = ["-stream_loop", "-1"] if dur and start + seconds * speed > dur else []
    ffmpeg(*loop, "-ss", f"{start:.2f}", "-i", src, "-filter_complex",
           f"[0:v]setpts=PTS/{speed},fps={FPS},{FIT.removeprefix('[0:v]')}[v]",
           "-map", "[v]", "-an", "-frames:v", str(n), *ENC, out)


def split(a: Path, b: Path, seconds: float, out: Path, day: str):
    """Before | after: the left half of one still next to the right half of
    the other, with a bright seam."""
    n = max(1, round(seconds * FPS))
    sa, sb = norm_still(a, day), norm_still(b, day)
    ffmpeg("-loop", "1", "-i", sa, "-loop", "1", "-i", sb, "-filter_complex",
           f"[0:v]crop={W // 2}:{H}:{W // 4}:0[l];[1:v]crop={W // 2}:{H}:{W // 4}:0[r];"
           f"[l][r]hstack,drawbox=x={W // 2 - 4}:y=0:w=8:h={H}:color=0x{PINK}:t=fill,"
           f"zoompan=z='1+0.06*on/{n}':x='(iw-iw/zoom)/2':y='(ih-ih/zoom)/2':d=1:s={W}x{H}:fps={FPS},"
           f"setsar=1,format=yuv420p[v]",
           "-map", "[v]", "-frames:v", str(n), *ENC, out)


def card(seconds: float, out: Path, color: str = VIOLET):
    n = max(1, round(seconds * FPS))
    ffmpeg("-f", "lavfi", "-i", f"color=c=0x{color}:s={W}x{H}:r={FPS}", "-vf",
           "vignette=PI/4,format=yuv420p", "-frames:v", str(n), *ENC, out)


def concat(parts: list[Path], out: Path):
    lst = out.with_suffix(".txt")
    lst.write_text("".join(f"file '{p}'\n" for p in parts))
    ffmpeg("-f", "concat", "-safe", "0", "-i", lst, "-vf",
           f"scale=out_range=tv,format=yuv420p,setsar=1,fps={FPS}", *ENC, out)


def stills_of(day: str, skip=()) -> list[dict]:
    """The day's pictures for the time-lapse: in time order, without review
    sheets and before/after crops, a video only without its own still, and
    without the day script's `timelapse_skip` files (§4)."""
    media = media_of(day)
    names = {m["file"] for m in media}
    skip = set(skip)
    out = []
    for m in media:
        f = m["file"]
        if f in skip or m["kind"] == "audio" or re.search(r"sheet|before|after|crop|cmp|-first", f):
            continue
        stem = f.rsplit(".", 1)[0]
        if m["kind"] == "video" and ({f"{stem}.png", f"{stem}.jpg"} & names):
            continue
        out.append(m)
    return out


def timelapse(day: str, out: Path, skip=()) -> tuple[float, list[tuple[float, float, dict]]]:
    """Every picture of the day, fast, in time order. Returns the duration
    and (start, end, picture) for the overlay."""
    pics = stills_of(day, skip)
    total = min(26.0, max(10.0, len(pics) * 0.11))
    per = total / max(1, len(pics))
    frames = max(2, round(per * FPS))
    lst = out.with_suffix(".txt")
    rows, t, lines = [], 0.0, []
    for m in pics:
        p = norm_still(C.HIST / day / m["file"], day)
        d = frames / FPS
        lines.append(f"file '{p}'\nduration {d:.4f}\n")
        rows.append((t, t + d, m))
        t += d
    lines.append(f"file '{norm_still(C.HIST / day / pics[-1]['file'], day)}'\n")
    lst.write_text("".join(lines))
    ffmpeg("-f", "concat", "-safe", "0", "-i", lst, "-vf",
           f"fps={FPS},eq=saturation=1.15:contrast=1.05,vignette=PI/5,format=yuv420p",
           "-frames:v", str(round(t * FPS)), *ENC, out)
    return t, rows


def mosaic(day: str, seconds: float, out: Path, skip=()):
    """The end card's background: 24 of the day's pictures, dimmed."""
    pics = stills_of(day, skip)
    pick = [pics[round(i * (len(pics) - 1) / 23)] for i in range(24)]
    inputs, filt = [], []
    for k, m in enumerate(pick):
        inputs += ["-i", norm_still(C.HIST / day / m["file"], day)]
        filt.append(f"[{k}:v]scale=320:180[t{k}]")
    filt.append("".join(f"[t{k}]" for k in range(24)) + "xstack=inputs=24:layout=" + "|".join(
        f"{(k % 6) * 320}_{(k // 6) * 180}" for k in range(24)) + ",scale=1920:720[m]")
    n = max(1, round(seconds * FPS))
    tile = C.WORK / day / "mosaic.jpg"
    ffmpeg(*inputs, "-filter_complex", ";".join(filt), "-map", "[m]", "-frames:v", "1", tile)
    ffmpeg("-loop", "1", "-i", tile, "-filter_complex",
           f"[0:v]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},"
           f"eq=brightness=-0.32:saturation=0.7,boxblur=3:1,"
           f"zoompan=z='1.12-0.1*on/{n}':x='(iw-iw/zoom)/2':y='(ih-ih/zoom)/2':d=1:s={W}x{H}:fps={FPS},"
           f"vignette=PI/4,format=yuv420p[v]",
           "-map", "[v]", "-frames:v", str(n), *ENC, out)


# ------------------------------------------------------------------ render


def end_stats(j: dict, sc: dict) -> list[tuple[int, str]]:
    """The end card's numbers of the day: (value, label), in order."""
    stats = [
        (j["commits"].__len__(), "COMMITS"),
        (j["merges"], "MERGES"),
        (j["lines_added"], "LINES WRITTEN"),
        (j["images"] + j["videos"], "PICTURES & VIDEOS"),
    ]
    if sc.get("tests") or j["tests"]:
        stats.append((int(sc.get("tests") or j["tests"]), "TESTS PASSING"))
    if j.get("prompts"):
        stats.append((len(j["prompts"]), "PROMPTS"))
    if (j.get("tokens") or {}).get("total", {}).get("total"):
        stats.append((round(j["tokens"]["total"]["total"] / 1e6), "MILLION TOKENS"))
    b = j.get("builds") or {}
    if b.get("runs"):
        stats.append((b["runs"], "BUILD RUNS"))
        stats.append((round(b["seconds"] / 3600), "BUILD HOURS"))
    if b.get("cargo_s"):
        # The compile time (cargo) of the day's runs (user 2026-11-16: "record
        # also compile time"), in minutes: a day compiles a few hours.
        stats.append((round(b["cargo_s"] / 60), "COMPILE MINUTES"))
    return stats


def load_script(day: str) -> dict:
    p = DAYS / f"{day}.toml"
    if not p.exists():
        raise SystemExit(f"no script for {day}: write days/{day}.toml (see docs/ART-PROJECT.md §4)")
    return tomllib.loads(p.read_text())


def render(day: str) -> Path:
    sc = load_script(day)
    j = journal(day)
    work = C.WORK / day / "render"
    if work.exists():
        shutil.rmtree(work)
    work.mkdir(parents=True)
    num = j["number"]
    date = dt.date.fromisoformat(day)
    segs: list[tuple[Path, float, str]] = []  # (file, seconds, music section)

    # 1. Title.
    title_s = float(sc.get("title_seconds", 6.5))
    t1 = work / "00-title.mp4"
    kenburns(media_path(day, sc["hero"]), title_s, t1, day)
    segs.append((t1, title_s, "intro"))

    # 2. Time-lapse of the whole day.
    t2 = work / "01-timelapse.mp4"
    tl_s, tl_rows = timelapse(day, t2, sc.get("timelapse_skip", []))
    segs.append((t2, tl_s, "drive"))

    # 3. Chapters.
    chapters = sc.get("chapter", [])
    ch_shots = []
    for ci, ch in enumerate(chapters):
        parts, shots = [], []
        for si, shot in enumerate(ch["shots"]):
            out = work / f"ch{ci:02d}-{si:02d}.mp4"
            secs = float(shot.get("seconds", 3.5))
            if "split" in shot:
                a, b = shot["split"]
                split(media_path(day, a), media_path(day, b), secs, out, day)
            elif "card" in shot:
                card(secs, out, shot.get("color", VIOLET))
            else:
                src = media_path(day, shot["file"])
                if src.suffix.lower() in VIDEO:
                    clip(src, float(shot.get("start", 0)), secs, float(shot.get("speed", 1)), out)
                else:
                    kenburns(src, secs, out, day)
            parts.append(out)
            shots.append((secs, shot))
        seg = work / f"ch{ci:02d}.mp4"
        concat(parts, seg)
        segs.append((seg, sum(s for s, _ in shots), "groove"))
        ch_shots.append(shots)

    # 3b. "Today's features": a paged roll of the merged spec rows (§4 features_roll).
    roll = F.roll_pages(j.get("features") or []) if sc.get("features_roll", True) else []
    roll_s = ROLL_PAGE_S * len(roll)
    if roll:
        t3 = work / "98-features.mp4"
        card(roll_s, t3)
        segs.append((t3, roll_s, "groove"))

    # 4. End card.
    end_s = float(sc.get("end_seconds", 9))
    t4 = work / "99-end.mp4"
    mosaic(day, end_s, t4, sc.get("timelapse_skip", []))
    segs.append((t4, end_s, "outro"))

    # Timeline: segment i starts at start[i]; xfades overlap by XF.
    starts, t = [], 0.0
    for _, d, _ in segs:
        starts.append(t)
        t += d - XF
    total = t + XF

    # ---- overlay text
    sub = Subs()
    # Title.
    sub.add(0.4, title_s - 0.3, "Kicker",
            "{\\fad(300,300)\\pos(960,300)}OCW BUILD DIARY")
    sub.add(0.7, title_s - 0.3, "Title",
            f"{{\\fad(150,300)\\pos(960,450)\\fscx150\\fscy150\\t(0,450,\\fscx100\\fscy100)}}DAY {num}")
    sub.add(1.2, title_s - 0.3, "Date",
            f"{{\\fad(300,300)\\pos(960,590)}}{date.strftime('%A, %d %B %Y').upper()}")
    sub.typed(1.9, title_s - 0.2, "Tag", esc(sc["tagline"]), pre="{\\pos(960,720)\\fad(0,300)}")
    if sc.get("title"):
        sub.add(1.5, title_s - 0.3, "Caption",
                f"{{\\fad(300,300)\\pos(960,880)}}{esc(sc['title'])}")

    # Time-lapse: clock, counters and the commit ticker.
    t0 = starts[1]
    commits = j["commits"]
    sub.add(t0 + 0.2, t0 + tl_s - 0.2, "Kicker",
            "{\\an9\\pos(1860,40)\\fad(200,200)}THE DAY IN " + f"{round(tl_s)}" + " SECONDS")
    for k, (a, b, m) in enumerate(tl_rows):
        hhmm = m["time"][:5]
        done = [c for c in commits if c["time"] <= m["time"]]
        sub.add(t0 + a, t0 + b, "Clock", f"{{\\an9\\pos(1860,84)}}{hhmm}")
        sub.add(t0 + a, t0 + b, "Counter",
                f"{{\\an9\\pos(1856,222)}}commits {len(done):3d}  ·  merges "
                f"{sum(c['merge'] for c in done):2d}  ·  pictures {k + 1:3d}")
        last = done[-6:]
        y = 1040
        for i, c in enumerate(reversed(last)):
            txt = esc(f"{c['time'][:5]} {c['sha']} {c['subject'][:64]}")
            style = "TickerHi" if i == 0 and c is done[-1] and (
                k == 0 or c["time"] > tl_rows[k - 1][2]["time"]) else "Ticker"
            alpha = min(200, i * 34)
            sub.add(t0 + a, t0 + b, style, f"{{\\pos(1880,{y})\\alpha&H{alpha:02X}&}}{txt}")
            y -= 46

    # Prompts in the time-lapse: each one as a chat bubble when its time comes.
    ps = j.get("prompts") or []
    shown, bubbles = set(), []
    for k, (a, b, m) in enumerate(tl_rows):
        due = [p_ for p_ in ps if p_["time"] <= m["time"] and p_["time"] not in shown]
        if not due or (bubbles and a - bubbles[-1] < 1.2):
            continue  # at most one new bubble per 1.2 s; the newest prompt wins
        p_ = due[-1]
        shown.update(x["time"] for x in due)
        bubbles.append(a)
        nxt = next((r[0] for r in tl_rows[k + 1:] if r[0] - a >= 1.2), tl_s)
        end = min(t0 + tl_s - 0.2, t0 + a + 2.2, t0 + nxt)
        txt = prompt_lines(p_["text"])
        sub.add(t0 + a, end, "PromptWho", f"{{\\pos(60,330)\\fad(80,150)}}YOU · {p_['time'][:5]}")
        sub.add(t0 + a, end, "Prompt", f"{{\\pos(60,380)\\fad(80,150)}}{txt}")

    # Chapters.
    sfx_events = [(0.25, "bell")]
    duck = []
    for ci, ch in enumerate(chapters):
        cs = starts[2 + ci]
        cd = segs[2 + ci][1]
        sub.add(cs + 0.25, cs + min(cd, 3.6), "ChTime",
                f"{{\\move(-300,700,80,700,0,260)\\fad(0,250)}}{esc(ch.get('time', ''))}")
        sub.add(cs + 0.35, cs + min(cd, 3.6), "ChTitle",
                f"{{\\move(-1400,830,80,830,40,330)\\fad(0,250)}}{esc(ch['title'])}")
        if ch.get("prompt"):
            ptxt = prompt_lines(mask(ch["prompt"]))
            sub.add(cs + 0.4, cs + min(cd, 4.5), "PromptWho", "{\\pos(60,300)\\fad(150,200)}YOU ASKED")
            sub.add(cs + 0.4, cs + min(cd, 4.5), "Prompt", f"{{\\pos(60,350)\\fad(150,200)}}{ptxt}")
        if ch.get("caption"):
            sub.typed(cs + min(cd - 1.0, 2.4), cs + cd - 0.25, "Caption", esc(ch["caption"]),
                      pre="{\\fad(0,200)}")
        tt = cs
        for secs, shot in ch_shots[ci]:
            if shot.get("incident"):  # an incident card: "HH:MM" of the incident, its text centred
                inc_txt = incident_text(j, str(shot["incident"]), shot.get("text"))
                sub.add(tt + 0.2, tt + secs - 0.15, "Kicker",
                        f"{{\\pos(960,380)\\fad(150,150)}}INCIDENT · {esc(str(shot['incident']))}")
                sub.typed(tt + 0.5, tt + secs - 0.15, "Outro", esc(inc_txt), pre="{\\pos(960,560)\\fad(0,150)}")
            if shot.get("note"):
                sub.add(tt + 0.5, tt + secs - 0.15, "Note",
                        f"{{\\pos(1860,70)\\frz{seeded(shot['note']).uniform(-5, 5):.1f}"
                        f"\\fscx40\\fscy40\\t(0,180,\\fscx112\\fscy112)\\t(180,280,\\fscx100\\fscy100)"
                        f"\\fad(0,150)}}{esc(shot['note'])}")
                sfx_events.append((tt + 0.5, "pop"))
            spd = float(shot.get("speed", 1))
            if spd > 1:
                sub.add(tt + 0.2, tt + secs - 0.1, "Badge",
                        f"{{\\pos(1880,1040)}}▶▶ TIME-LAPSE ×{spd:g}")
            tt += secs
        if ch.get("sound"):
            duck.append((cs, cs + cd, 0.35))
        sfx_events.append((cs - XF / 2, "whoosh"))
    sfx_events.append((starts[1] - XF / 2, "whoosh"))
    sfx_events.append((starts[-1] - XF / 2, "whoosh"))

    # The features roll: a kicker, then one page of lines after the other.
    if roll:
        rs = starts[-2]
        sub.add(rs + 0.2, rs + roll_s - 0.2, "Kicker", "{\\pos(960,150)\\fad(200,200)}TODAY'S FEATURES")
        for pi, page in enumerate(roll):
            a = rs + pi * ROLL_PAGE_S
            for li, line in enumerate(page):
                sub.add(a + 0.15 + li * 0.12, a + ROLL_PAGE_S - 0.1, "Counter",
                        f"{{\\an4\\pos(260,{300 + li * 100})\\fad(180,180)}}{esc(line)}")
        sfx_events.append((rs - XF / 2, "whoosh"))

    # End card: count-up stats.
    es = starts[-1]
    stats = end_stats(j, sc)
    # One row for up to five numbers, else two rows with smaller numbers.
    rows = [stats] if len(stats) <= 5 else [stats[: (len(stats) + 1) // 2],
                                            stats[(len(stats) + 1) // 2 :]]
    pos = []  # (x, y of the number, y of the label, scale %)
    for r, row in enumerate(rows):
        step = min(360, 1760 / max(1, len(row)))
        y, sc_ = (380, 100) if len(rows) == 1 else (300 + r * 190, 78)
        pos += [(960 + (i - (len(row) - 1) / 2) * step, y, y + 72 * sc_ / 100 + 18, sc_)
                for i in range(len(row))]
    outro_y = 650 if len(rows) == 1 else 700
    for i, (val, label) in enumerate(stats):
        x, y, ly, scl = pos[i]
        fs = f"\\fscx{scl}\\fscy{scl}"
        a = es + 0.5 + i * 0.25
        steps = 24
        for k in range(steps):
            v = round(val * ((k + 1) / steps) ** 0.6)
            sub.add(a + k / FPS * 1.4, a + (k + 1) / FPS * 1.4, "StatNum",
                    f"{{\\pos({x:.0f},{y}){fs}}}{num_fmt(v)}")
            if k % 3 == 0:
                sfx_events.append((a + k / FPS * 1.4, "tick"))
        sub.add(a + steps / FPS * 1.4, es + end_s - 0.2, "StatNum",
                f"{{\\pos({x:.0f},{y}){fs}\\t(0,120,\\fscx{scl * 1.15:.0f}\\fscy{scl * 1.15:.0f})"
                f"\\t(120,260,\\fscx{scl}\\fscy{scl})\\fad(0,300)}}"
                f"{num_fmt(val)}")
        sub.add(a, es + end_s - 0.2, "StatLabel",
                f"{{\\pos({x:.0f},{ly:.0f})\\fad(200,300)}}{label}")
    sfx_events.append((es + 0.5 + len(stats) * 0.25 + 1.4, "ding"))
    sub.typed(es + 3.2, es + end_s - 0.2, "Outro", esc(sc["outro"]), pre=f"{{\\pos(960,{outro_y})\\fad(0,300)}}")
    if sc.get("teaser"):
        sub.add(es + 5.2, es + end_s - 0.1, "Teaser",
                f"{{\\pos(960,800)\\fad(400,300)}}{esc(sc['teaser'])}")
    sub.add(es + 0.3, es + end_s - 0.1, "Kicker",
            f"{{\\pos(960,170)\\fad(300,300)}}DAY {num}  ·  {date.strftime('%d.%m.%Y')}  ·  "
            "OPEN CYCLING WORLD")
    ass = work / "overlay.ass"
    sub.write(ass)

    # ---- soundtrack
    band = Music(bpm=int(sc.get("bpm", 108)), key=sc.get("key", "C"), seed=num,
                 style=sc.get("style"), mode=sc.get("mode"))
    log(f"{day}: music {band.describe()}")
    music = band.render(total, [(starts[i], segs[i][2]) for i in range(len(segs))], duck)
    rng = random.Random(num)
    fx = {"bell": sfx_bell(), "pop": sfx_pop(), "tick": sfx_tick(), "ding": sfx_ding()}
    for at, kind in sfx_events:
        data = sfx_whoosh(rng) if kind == "whoosh" else fx[kind]
        s = round(max(0.0, at) * RATE)
        for i, v in enumerate(data):
            if s + i < len(music):
                music[s + i] += v * (0.5 if kind == "whoosh" else 1.0)
    track = work / "soundtrack.wav"
    write_wav(track, music)

    # ---- assemble: xfade chain + overlay + audio, one encode
    inputs, filt = [], []
    for p, _, _ in segs:
        inputs += ["-i", p]
    for i in range(len(segs)):
        filt.append(f"[{i}:v]scale=out_range=tv,format=yuv420p,setsar=1,fps={FPS},"
                    f"settb=1/{FPS * 512}[n{i}]")
    prev = "[n0]"
    for i in range(1, len(segs)):
        off = starts[i]
        tr = TRANSITIONS[(i + num) % len(TRANSITIONS)]
        filt.append(f"{prev}[n{i}]xfade=transition={tr}:duration={XF}:offset={off:.3f}[x{i}]")
        prev = f"[x{i}]"
    filt.append(f"{prev}ass={ass}:fontsdir={FONTS},format=yuv420p[v]")
    audio_in = len(segs)
    inputs += ["-i", track]
    amix = [f"[{audio_in}:a]volume=1.0[m]"]
    mix_labels = ["[m]"]
    k = audio_in + 1
    for ci, ch in enumerate(chapters):
        if ch.get("sound"):
            src = media_path(day, ch["sound"])
            cd = segs[2 + ci][1]
            inputs += ["-i", src]
            ms = round(starts[2 + ci] * 1000)
            amix.append(f"[{k}:a]aresample={RATE},atrim=0:{cd:.2f},afade=t=in:d=0.3,"
                        f"afade=t=out:st={max(0, cd - 0.6):.2f}:d=0.6,"
                        f"volume={float(ch.get('sound_gain', 1.0))},adelay={ms}|{ms}[s{ci}]")
            mix_labels.append(f"[s{ci}]")
            k += 1
    amix.append("".join(mix_labels) + f"amix=inputs={len(mix_labels)}:normalize=0,"
                "alimiter=limit=0.95[a]")
    C.OUT.mkdir(parents=True, exist_ok=True)
    out = C.OUT / f"ocw-diary-day-{num:02d}-{day}.mp4"
    ffmpeg(*inputs, "-filter_complex", ";".join(filt + amix), "-map", "[v]", "-map", "[a]",
           "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p",
           "-r", str(FPS), "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
           "-t", f"{total:.3f}", *now_meta(), "-metadata",
           f"title=OCW Build Diary – day {num} ({day})", "-movflags", "+faststart", out)
    log(f"{day}: {out} ({total:.1f} s)")
    return out


def diary() -> Path:
    """The diary: a short opener, then every day video in order."""
    days = [p for p in sorted(C.OUT.glob("ocw-diary-day-*.mp4"))]
    if not days:
        raise SystemExit("no day videos yet: diary.py render")
    work = C.WORK / "diary"
    work.mkdir(parents=True, exist_ok=True)
    opener = work / "opener.mp4"
    sec = 5.0
    sub = Subs()
    sub.add(0.3, sec - 0.2, "Kicker", "{\\pos(960,330)\\fad(300,300)}AN ART PROJECT")
    sub.add(0.6, sec - 0.2, "Title",
            "{\\pos(960,480)\\fad(200,300)\\fscx120\\fscy120\\t(0,500,\\fscx100\\fscy100)}"
            "The Build Diary")
    sub.typed(1.4, sec - 0.2, "Tag",
              esc(f"How Open Cycling World was built, one day at a time · {len(days)} "
                  f"day{'s' if len(days) != 1 else ''} so far"), pre="{\\pos(960,640)\\fad(0,300)}")
    ass = work / "opener.ass"
    sub.write(ass)
    logo = LOGO
    ffmpeg("-f", "lavfi", "-i", f"color=c=0x{VIOLET}:s={W}x{H}:r={FPS}", "-loop", "1", "-i", logo,
           "-f", "lavfi", "-i", f"anullsrc=r=48000:cl=stereo",
           "-filter_complex",
           f"[1:v]scale=230:-1[l];[0:v][l]overlay=(W-w)/2:40,vignette=PI/4,"
           f"ass={ass}:fontsdir={FONTS},format=yuv420p[v]",
           "-map", "[v]", "-map", "2:a", "-t", f"{sec}", "-c:v", "libx264", "-preset", "medium",
           "-crf", "20", "-pix_fmt", "yuv420p", "-r", str(FPS), "-c:a", "aac", "-b:a", "192k",
           "-ar", "48000", "-ac", "2", opener)
    bell = work / "bell.wav"
    write_wav(bell, [0.0] * round(0.3 * RATE) + sfx_bell())
    opener2 = work / "opener-bell.mp4"
    ffmpeg("-i", opener, "-i", bell, "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac",
           "-b:a", "192k", "-ar", "48000", "-ac", "2", "-af", "apad", "-t", f"{sec}", opener2)
    out = C.OUT / "ocw-build-diary.mp4"
    lst = work / "diary.txt"
    lst.write_text("".join(f"file '{p}'\n" for p in [opener2, *days]))
    ffmpeg("-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", *now_meta(),
           "-metadata", "title=OCW Build Diary", "-movflags", "+faststart", out)
    log(f"diary: {out} ({probe_duration(out):.1f} s, {len(days)} days)")
    return out
