"""Masking (ART-PROJECT §2.3, §2.5): build machines' hosts and users, home
directories, e-mail and private IP addresses; the tracked text files and check-masked."""

from __future__ import annotations

import os
import re
from pathlib import Path

from . import core as C
from .core import log, run

TRACKED_TOP = ("index.md", "SHA256SUMS")
TRACKED_DAY = ("journal.md", "journal.json", "tokens.json", "incidents.md")


def tracked_files() -> list[Path]:
    out = [C.HIST / n for n in TRACKED_TOP]
    for d in sorted(C.HIST.glob("????-??-??")):
        if d.is_dir() and re.fullmatch(r"\d{4}-\d{2}-\d{2}", d.name):
            out += [d / n for n in TRACKED_DAY]
    return [f for f in out if f.is_file()]


def write_tracked(path: Path, text: str, secrets=None):
    """Writes a tracked text file of the archive, masked (§2.3)."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(mask(text, secrets))


MEDIA_NAMES = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".mp4", ".webm", ".mkv", ".mov", ".wav"}


def check_masked(fix: bool = False, secrets=None) -> list[str]:
    """Findings ("path:line: kind") in the tracked text files and in the
    names of the day folders' media; with `fix` the text files are masked in
    place first (a file name is never renamed). Never prints a private value."""
    secrets = secrets if secrets is not None else _secrets()
    out = []
    for f in tracked_files():
        text = f.read_text(errors="replace")
        if fix:
            masked = mask(text, secrets)
            if masked != text:
                f.write_text(masked)
                log(f"masked {f.relative_to(C.HIST)}")
                text = masked
        for n, kind in private_findings(text, secrets):
            out.append(f"{f.relative_to(C.HIST)}:{n}: {kind}")
    # The media's file names: public in Git LFS, the gallery and the day zips
    # (§2.8). Reported masked, so the value is never shown.
    for d in sorted(C.HIST.glob("????-??-??")):
        if not d.is_dir():
            continue
        for f in sorted(d.iterdir()):
            if f.is_file() and f.suffix.lower() in MEDIA_NAMES:
                for _, kind in private_findings(f.name, secrets):
                    out.append(f"{d.name}/{mask(f.name, secrets)}: {kind} in the file name")
    return out


# user@domain.tld (not `icon@2x.png`, not `react@18.3.1`).
EMAIL_RE = re.compile(r"[\w.+-]+@(?!\d+x\.)[\w-]+(?:\.[\w-]+)*\.[A-Za-z]{2,}\b")
# Private network addresses (10/8, 172.16/12, 192.168/16, 100.64/10).
PRIVATE_IP_RE = re.compile(
    r"\b(?:10\.\d{1,3}|172\.(?:1[6-9]|2\d|3[01])|192\.168|100\.(?:6[4-9]|[7-9]\d|1[01]\d|12[0-7]))"
    r"\.\d{1,3}\.\d{1,3}\b")


_SECRETS: list[tuple[str, str]] | None = None


def machines_conf() -> Path | None:
    """config/machines.toml of this checkout, else of the main checkout (an
    agent worktree has none; scripts/remote.sh looks there too). Running in
    a worktree without this fallback once wrote journals without the users
    masked (2026-11-15)."""
    for root in (C.ROOT, main_checkout()):
        if root is not None and (root / "config" / "machines.toml").is_file():
            return root / "config" / "machines.toml"
    return None


def main_checkout() -> Path | None:
    r = run(["git", "-C", C.ROOT, "rev-parse", "--path-format=absolute", "--git-common-dir"],
            capture_output=True, text=True, check=False)
    common = r.stdout.strip()
    return Path(common).parent if r.returncode == 0 and common else None


def _secrets() -> list[tuple[str, str]]:
    """(text, replacement) pairs: every build machine's host (replaced by the
    machine's name) and user ("user"; asked from scripts/remote.sh, which
    reads config/machines.toml) and the home directory ("~"). Asked once per
    run. Never printed."""
    global _SECRETS
    if _SECRETS is not None:
        return _SECRETS
    out = []
    conf = machines_conf()
    if conf is None:
        if os.environ.get("OCW_ART_NO_MACHINES") != "1":
            raise SystemExit("config/machines.toml not found (here or in the main checkout): without it the "
                             "build machines' hosts and users cannot be masked (ART-PROJECT §2.5). "
                             "OCW_ART_NO_MACHINES=1 masks without them (tests only).")
        names = []
    else:
        names = re.findall(r'^\s*name\s*=\s*"([^"]+)"', conf.read_text(), re.M)
    for name in names:
        for k in ("host", "user"):
            v = run([C.ROOT / "scripts" / "remote.sh", name, "field", k], capture_output=True,
                    text=True, check=False).stdout.strip()
            if len(v) >= 3:
                out.append((v, name if k == "host" else "user"))
    out.append((str(Path.home()), "~"))
    # A value that is part of a replacement (a host named like its machine)
    # is public and would never mask away.
    reps = {r for _, r in out}
    out = [(v, r) for v, r in out if not any(v in r_ for r_ in reps)]
    _SECRETS = sorted(set(out), key=lambda kv: -len(kv[0]))
    return _SECRETS


# Any home directory (Linux, macOS, Windows; also JSON-escaped backslashes).
HOME_RE = re.compile(r"(?<![\w.-])(?:/home|/Users)/[A-Za-z0-9._-]+"
                     r"|\b[A-Za-z]:(?:\\\\|\\|/)Users(?:\\\\|\\|/)[A-Za-z0-9._-]+")


def _user_re(user: str) -> re.Pattern:
    """A build machine's user name as a word of its own (`claude@host`,
    `"claude"`, `user claude`), not inside a path or name such as
    `~/.claude/` or `claude.ai`."""
    return re.compile(r"(?<![\w./\\])" + re.escape(user) + r"(?![\w/]|\.\w)")


def _mask_steps(secrets):
    """(kind, function) of every masking step, in order: hosts and home
    directories first (a user name is part of both), then the users, then
    the generic patterns."""
    hosts = [("build-machine host", lambda t, v=v, r=r: t.replace(v, r))
             for v, r in secrets if r not in ("user", "~")]
    homes = [("home directory", lambda t, v=v: t.replace(v, "~")) for v, r in secrets if r == "~"]
    homes.append(("home directory", lambda t: HOME_RE.sub("~", t)))
    users = [("build-machine user", lambda t, rx=_user_re(v): rx.sub("user", t))
             for v, r in secrets if r == "user"]
    return [*hosts, *homes, *users,
            ("e-mail address", lambda t: EMAIL_RE.sub("<e-mail>", t)),
            ("private IP address", lambda t: PRIVATE_IP_RE.sub("<ip>", t))]


def mask(text: str, secrets=None) -> str:
    for _, f in _mask_steps(secrets if secrets is not None else _secrets()):
        text = f(text)
    return text


def private_findings(text: str, secrets=None) -> list[tuple[int, str]]:
    """(line number, kind) of every private pattern in the text: what mask()
    would change. The values themselves are never reported."""
    steps = _mask_steps(secrets if secrets is not None else _secrets())
    out = []
    for n, line in enumerate(text.splitlines(), 1):
        for kind, f in steps:
            if f(line) != line and (n, kind) not in out:
                out.append((n, kind))
    return out
