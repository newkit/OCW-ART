"""The archive (ART-PROJECT §2): fetch a day from the release, gather the day's
files from OCW's test-output, stamp capture times into PNG/MP4."""

from __future__ import annotations

import datetime as dt
import json
import os
import re
import shutil
import struct
from pathlib import Path

from . import core as C
from .core import ART_GH, AUDIO, COLLECTOR_FILES, ffmpeg, IMAGE, log, LOGS, OCW_GH, RELEASE, run, sha, TEXT, VIDEO

# ------------------------------------------------------------------ gather


def fetch(day: str):
    C.HIST.mkdir(parents=True, exist_ok=True)
    z = C.HIST / f"ocw-build-history-{day}.zip"
    if not z.exists():
        r = run(
            ["gh", "release", "download", RELEASE, "-R", ART_GH, "-D", C.HIST, "-p", z.name],
            check=False,
        )
        if r.returncode:  # days 1-4 are on OCW's release too
            r = run(["gh", "release", "download", RELEASE, "-R", OCW_GH, "-D", C.HIST, "-p", z.name],
                    check=False)
        if r.returncode:
            log(f"{day}: no zip on the release")
            return
    if not (C.HIST / day).exists():
        run(["unzip", "-q", "-n", z, "-d", C.HIST])
    log(f"{day}: unpacked {z.name}")


TIME_RE = re.compile(r"^(\d{6})-")
DIR_TIME_RE = re.compile(r"(\d{4}-?\d{2}-?\d{2})[-_T]?(\d{6})")


def file_time(path: Path) -> tuple[str, str]:
    """(YYYY-MM-DD, HHMMSS) of a file: name, folder name, else mtime."""
    for part in [path.name, *[p.name for p in path.parents][:3]]:
        m = DIR_TIME_RE.search(part)
        if m:
            d = m.group(1).replace("-", "")
            return f"{d[:4]}-{d[4:6]}-{d[6:]}", m.group(2)
    t = dt.datetime.fromtimestamp(path.stat().st_mtime)
    m = TIME_RE.match(path.name)
    hms = m.group(1) if m else t.strftime("%H%M%S")
    # A date folder (test-output/YYYY-MM-DD/...) is the day.
    for p in path.parents:
        if re.fullmatch(r"\d{4}-\d{2}-\d{2}", p.name):
            return p.name, hms
    return t.strftime("%Y-%m-%d"), hms


def slug(s: str) -> str:
    s = re.sub(r"[^A-Za-z0-9.,+-]+", "-", s).strip("-")
    return re.sub(r"-{2,}", "-", s)


def sources() -> list[Path]:
    """Every checkout's test-output (main + agent worktrees)."""
    out = [C.TEST_OUTPUT]
    if C.WORKTREES is not None:
        out += sorted(C.WORKTREES.glob("*/test-output"))
    return [p for p in out if p.is_dir()]


def withheld() -> set[str]:
    """`DAY/name` of the media withheld from the archive (ART-PROJECT §2.5):
    `build-history/withheld.txt`, one per line, `#` starts a comment. They
    are never gathered again; the files themselves wait, local only, in
    `build-history/.withheld/DAY/`."""
    p = C.HIST / "withheld.txt"
    if not p.exists():
        return set()
    return {ln.split("#", 1)[0].strip() for ln in p.read_text().splitlines()} - {""}


def gather(day: str):
    held = withheld()
    dest = C.HIST / day
    dest.mkdir(parents=True, exist_ok=True)
    (dest / "logs").mkdir(exist_ok=True)
    # Checksums of the gathered originals: the copies here get metadata
    # (stamp), so their own checksums differ from the sources'.
    manifest = dest / "logs" / ".sources.json"
    known = json.loads(manifest.read_text()) if manifest.exists() else {}
    for f in dest.rglob("*"):
        if f.is_file() and f.name != manifest.name:
            known.setdefault(sha(f), f.name)
    added = 0
    for src in sources():
        for f in sorted(src.rglob("*")):
            if not f.is_file() or C.HIST in f.parents:
                continue
            ext = f.suffix.lower()
            if ext not in IMAGE | VIDEO | AUDIO | TEXT | LOGS or f.name == "index.md":
                continue
            d, hms = file_time(f)
            if d != day:
                continue
            if "build-log" in f.parts:
                # The build log (remote.sh runs, dashboard samples) grows
                # during the day: keep one copy per file, updated in place.
                target = dest / "logs" / "build-log" / f.name
                if not target.exists() or target.stat().st_size != f.stat().st_size:
                    target.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(f, target)
                    # The collector's own status and log change every run.
                    added += f.name not in COLLECTOR_FILES
                continue
            h = sha(f)
            if h in known:
                continue
            rel = f.relative_to(src).with_suffix("").as_posix()
            stem = re.sub(r"^\d{4}-\d{2}-\d{2}/", "", rel)
            stem = DIR_TIME_RE.sub("", stem)
            stem = re.sub(r"(^|/)\d{6}-", r"\1", stem)
            stem = re.sub(r"(^|[-/])(nogit|[0-9a-f]{7}(-dirty)?)-", r"\1", stem)
            stem = re.sub(r"agent-[0-9a-f]{17}", "agent", stem)
            name = f"{hms}-{slug(stem)[:90] or 'file'}{ext}"
            if f"{day}/{name}" in held:
                known[h] = name
                continue
            target = (dest / "logs" if ext in LOGS else dest) / name
            n = 2
            while target.exists():
                target = target.with_name(f"{hms}-{slug(stem)[:90]}-{n}{ext}")
                n += 1
            shutil.copy2(f, target)
            known[h] = target.name
            added += 1
    manifest.write_text(json.dumps(known, indent=0))
    stamp(day)
    media = [f for f in dest.iterdir() if f.suffix.lower() in IMAGE | VIDEO | AUDIO]
    log(f"{day}: {added} new files; {len(media)} images/videos/sounds in {dest}")
    return added


# ------------------------------------------------------------------- stamp
#
# Every photo and video carries its ISO 8601 date and time in the file
# (ART-PROJECT.md §2): PNG `tEXt` "Creation Time", MP4 `creation_time`.
# The app writes them itself (spec 2.24+); for older files the archive copy
# gets them from the capture time (file name / folder / mtime).


def capture_time(day: str, name: str) -> dt.datetime:
    m = TIME_RE.match(name)
    hms = m.group(1) if m else "000000"
    t = dt.datetime.strptime(f"{day} {hms}", "%Y-%m-%d %H%M%S")
    return t.astimezone()  # local time zone of this machine (the build's)


def png_text(path: Path) -> dict[str, str]:
    data = path.read_bytes()
    out, i = {}, 8
    while i + 8 <= len(data):
        n, kind = struct.unpack(">I4s", data[i:i + 8])
        if kind == b"tEXt":
            k, _, v = data[i + 8:i + 8 + n].partition(b"\0")
            out[k.decode("latin-1")] = v.decode("latin-1")
        if kind == b"IEND":
            break
        i += 12 + n
    return out


def png_add_text(path: Path, items: dict[str, str]):
    """Insert tEXt chunks before the first IDAT."""
    import zlib

    data = path.read_bytes()
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        return
    i = 8
    while i + 8 <= len(data):
        n, kind = struct.unpack(">I4s", data[i:i + 8])
        if kind == b"IDAT":
            break
        i += 12 + n
    chunks = b""
    for k, v in items.items():
        body = k.encode("latin-1") + b"\0" + v.encode("latin-1")
        chunks += struct.pack(">I", len(body)) + b"tEXt" + body + struct.pack(
            ">I", zlib.crc32(b"tEXt" + body) & 0xFFFFFFFF)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_bytes(data[:i] + chunks + data[i:])
    os.utime(tmp, (path.stat().st_atime, path.stat().st_mtime))
    tmp.replace(path)


def mp4_creation_time(path: Path) -> str:
    return run(["ffprobe", "-v", "error", "-show_entries", "format_tags=creation_time",
                "-of", "csv=p=0", path], capture_output=True, text=True,
               check=False).stdout.strip()


def stamp(day: str):
    """Writes the capture time into every archived PNG and MP4 that has none."""
    n = 0
    for f in sorted((C.HIST / day).iterdir()):
        ext = f.suffix.lower()
        if ext not in {".png", ".mp4"}:
            continue
        t = capture_time(day, f.name)
        if ext == ".png":
            if "Creation Time" in png_text(f):
                continue
            png_add_text(f, {"Creation Time": t.isoformat(timespec="seconds"),
                             "Comment": "OCW build history (time from the capture's file name)"})
        else:
            if mp4_creation_time(f):
                continue
            tmp = f.with_name(f.stem + ".stamp.mp4")
            ffmpeg("-i", f, "-map", "0", "-c", "copy", "-metadata",
                   f"creation_time={t.astimezone(dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.000000Z')}",
                   "-metadata", "comment=OCW build history (time from the capture's file name)", tmp)
            os.utime(tmp, (f.stat().st_atime, f.stat().st_mtime))
            tmp.replace(f)
        n += 1
    log(f"{day}: stamped {n} files with their ISO 8601 capture time")
