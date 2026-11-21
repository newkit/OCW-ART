"""Settings, paths, the archive lock and small helpers shared by every part of the tool."""

from __future__ import annotations

import contextlib
import datetime as dt
import fcntl
import hashlib
import os
import subprocess
import sys
import time
import tomllib
from pathlib import Path

# This checkout (OCW-ART, https://github.com/newkit/OCW-ART): the tool, the
# day scripts and the archive. OCW itself (its git log, SPECIFICATION.md,
# test-output/, config/machines.toml and scripts/remote.sh) is read from the
# OCW checkout named by OCW_REPO, else `ocw_repo` in ocw-art.toml, else
# ../OCW next to this checkout (ART-PROJECT §5).
ART = Path(__file__).resolve().parent.parent
DAYS = ART / "days"
ASSETS = ART / "assets"
CONFIG = ART / "ocw-art.toml"


def ocw_repo() -> Path:
    """The OCW checkout the tool reads (OCW_REPO, ocw-art.toml, ../OCW)."""
    env = os.environ.get("OCW_REPO")
    if env:
        return Path(env).expanduser().resolve()
    if CONFIG.is_file():
        try:
            v = tomllib.loads(CONFIG.read_text()).get("ocw_repo")
        except tomllib.TOMLDecodeError as e:
            raise SystemExit(f"{CONFIG.name}: {e}") from None
        if v:
            return (ART / Path(v).expanduser()).resolve()
    return (ART.parent / "OCW").resolve()


ROOT = ocw_repo()


def check_ocw():
    """Stops with a clear message when OCW_REPO is not an OCW checkout."""
    if not (ROOT / "SPECIFICATION.md").is_file() or not (ROOT / ".git").exists():
        raise SystemExit(f"no OCW checkout at {ROOT}: clone https://github.com/newkit/OCW next to this "
                         f"checkout (../OCW), or set OCW_REPO / `ocw_repo` in {CONFIG.name} (ART-PROJECT §5)")


# The archive (ART-PROJECT §2): media git-ignored (or in Git LFS, §2.8),
# masked text tracked. OCW_ART_HISTORY moves it (tests).
HIST = Path(os.environ.get("OCW_ART_HISTORY") or ART / "build-history")
OUT = HIST / "diary"
WORK = HIST / ".work"
TEST_OUTPUT = Path(os.environ.get("OCW_TEST_OUTPUT") or ROOT / "test-output")
# The agent worktrees, whose test-output/ gather collects too. With
# OCW_TEST_OUTPUT (tests) only that folder is a source, unless
# OCW_ART_WORKTREES names a worktrees folder ("" = none).
_wt = os.environ.get("OCW_ART_WORKTREES")
WORKTREES = (Path(_wt) if _wt else None) if _wt is not None else (
    None if os.environ.get("OCW_TEST_OUTPUT") else ROOT / ".claude" / "worktrees")
# Fira Mono (the app's UI font) and the logo, copied from OCW (assets/README.md).
FONTS = ASSETS / "fonts"
LOGO = ASSETS / "logos" / "ocw-512.png"
# GitHub: the art project's release (videos, day zips, SHA256SUMS) is on
# OCW-ART; OCW's own release `build-history` holds days 1-4 too (fetch falls
# back to it) and the README's product images. OCW's releases are listed in
# the journal (features, §2.7).
ART_GH = os.environ.get("OCW_ART_GH_REPO", "newkit/OCW-ART")
OCW_GH = "newkit/OCW"
RELEASE = "build-history"

IMAGE = {".png", ".jpg", ".jpeg", ".gif", ".webp"}
VIDEO = {".mp4", ".webm", ".mkv", ".mov"}
AUDIO = {".wav", ".ogg", ".mp3", ".flac"}
TEXT = {".txt", ".md"}
LOGS = {".log", ".json", ".jsonl", ".args", ".route", ".toml", ".csv"}

# The collector's status file and its own files in OCW's test-output/build-log/DAY/
# (written every run: gather does not count them as new files).
STATUS_NAME = "art.json"
COLLECTOR_FILES = {STATUS_NAME, "art-runs.jsonl", "art.log", STATUS_NAME + ".tmp", "incidents.jsonl"}

W, H, FPS = 1920, 1080, 30
RATE = 44100

# Brand colours (assets/logos/ocw.svg): rider pink, deep violet, gold.
PINK, VIOLET, GOLD, INK = "FF1472", "3A2F55", "C98A00", "2B2B3A"


def log(*a):
    print(*a, file=sys.stderr, flush=True)


def set_history(path: Path):
    """Points the tool at another archive (tests, OCW_ART_HISTORY)."""
    global HIST, OUT, WORK
    HIST = Path(path)
    OUT = HIST / "diary"
    WORK = HIST / ".work"


# ------------------------------------------------------------------- lock
#
# Runs never overlap (ART-PROJECT §5.1): every writing command takes an
# exclusive flock on build-history/.lock. collect.sh takes
# the same lock itself and sets OCW_ART_LOCK_HELD=1 for the diary.py it runs.

LOCK_NAME = ".lock"


def lock_path() -> Path:
    return HIST / LOCK_NAME


@contextlib.contextmanager
def art_lock(what: str = "", wait: float | None = None):
    """Holds the archive's lock. `wait`: seconds to wait for it (None:
    OCW_ART_LOCK_WAIT, else forever); raises TimeoutError when it runs out."""
    if os.environ.get("OCW_ART_LOCK_HELD") == "1":
        yield
        return
    if wait is None and os.environ.get("OCW_ART_LOCK_WAIT"):
        wait = float(os.environ["OCW_ART_LOCK_WAIT"])
    path = lock_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "a+") as f:
        try:
            fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            f.seek(0)
            holder = f.read().strip() or "another run"
            log(f"waiting for the build-history lock ({holder})")
            t0 = time.monotonic()
            while True:
                try:
                    fcntl.flock(f, fcntl.LOCK_EX | (fcntl.LOCK_NB if wait is not None else 0))
                    break
                except BlockingIOError:
                    if time.monotonic() - t0 >= wait:
                        raise TimeoutError(f"build-history lock held by {holder}") from None
                    time.sleep(0.2)
        f.seek(0)
        f.truncate()
        f.write(f"pid {os.getpid()}: diary.py {what}".strip() + "\n")
        f.flush()
        try:
            yield
        finally:
            f.seek(0)
            f.truncate()
            fcntl.flock(f, fcntl.LOCK_UN)


def run(cmd, **kw):
    kw.setdefault("check", True)
    return subprocess.run([str(c) for c in cmd], **kw)


def ffmpeg(*args):
    run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", *args])


def probe_duration(path: Path) -> float:
    out = run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path],
        capture_output=True,
        text=True,
    ).stdout.strip()
    try:
        return float(out)
    except ValueError:
        return 0.0


def sha(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def days_with_scripts() -> list[str]:
    return sorted(p.stem for p in DAYS.glob("????-??-??.toml"))


def all_days() -> list[str]:
    """Days with commits (local time)."""
    out = run(
        ["git", "-C", ROOT, "log", "--format=%ad", "--date=format-local:%Y-%m-%d"],
        capture_output=True,
        text=True,
    ).stdout.split()
    return sorted(set(out))


def day_number(day: str) -> int:
    """The day's number in the build (1 = the first day with commits); a day
    without commits yet (just after midnight) counts as the next one. A day
    the diary tells without commits (a day script, e.g. 2026-11-20, when the
    weekly token limit was reached) counts too, so the days after it keep
    their own numbers."""
    first = min(all_days(), default=day)
    told = {d for d in days_with_scripts() if first <= d}
    return len({d for d in set(all_days()) | told if d < day}) + 1


# Text files of the archive that are tracked in git (ART-PROJECT §2): always
# written masked; everything else in the archive is git-ignored.
def now_meta() -> list[str]:
    t = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.000000Z")
    return ["-metadata", f"creation_time={t}"]


def git_lines(*args) -> list[str]:
    return run(["git", "-C", ROOT, *args], capture_output=True, text=True).stdout.splitlines()


def git_out(*args) -> str:
    r = run(["git", "-C", ROOT, *args], capture_output=True, text=True, check=False)
    return r.stdout if r.returncode == 0 else ""


def _next_day(day: str) -> str:
    return (dt.date.fromisoformat(day) + dt.timedelta(days=1)).isoformat()
