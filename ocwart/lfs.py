"""The archive's pictures and videos in Git LFS (ART-PROJECT §2.8), within the
free GitHub plan: 10 GiB of LFS storage, 10 GiB of download bandwidth a month.

    lfs-budget            the LFS total (tracked + about to be added), the
                          budget (default 9 GiB) and the days left at the
                          current rate
    lfs-commit [DAY...]   one commit per day of the day's media (the policy:
                          `all` = pictures and videos, `pictures` = pictures
                          only), refused beyond the budget; the media left
                          out stay local and git-ignored
    lfs-push              git lfs push + git push of main, only when every
                          unpushed commit touches nothing but build-history/
                          and .gitignore; then the check that the LFS file
                          list matches the committed media

Never in LFS or git: the day zips, the diary videos (build-history/diary/),
.work/ (contact sheets, the gallery) - they are on the release. The
.gitignore allow-list grows by one block per committed day (managed
between the `>>> lfs-days` / `<<< lfs-days` markers)."""

from __future__ import annotations

import datetime as dt
import json
import os
import re
import shutil
import subprocess
import tomllib
from pathlib import Path

from . import core as C
from .core import ART, CONFIG, log
from .mask import private_findings

GIB = 1 << 30
DEFAULT_BUDGET_GIB = 9.0
QUOTA_GIB = 10.0  # the free plan's LFS storage and monthly bandwidth
PICTURES = (".jpg", ".jpeg", ".png", ".webp")
VIDEOS = (".mp4", ".webm", ".mkv")
POLICIES = {"all": PICTURES + VIDEOS, "pictures": PICTURES}
BEGIN, END = "# >>> lfs-days", "# <<< lfs-days"
INSTALL_HINT = "install git-lfs (make deps), then run `git lfs install` once"


def setting(key: str, env: str, default):
    v = os.environ.get(env)
    if v:
        return v
    if CONFIG.is_file():
        try:
            return tomllib.loads(CONFIG.read_text()).get(key, default)
        except tomllib.TOMLDecodeError as e:
            raise SystemExit(f"{CONFIG.name}: {e}") from None
    return default


def budget_bytes() -> int:
    """lfs_budget_gib in ocw-art.toml or OCW_ART_LFS_BUDGET_GIB (default 9)."""
    gib = float(setting("lfs_budget_gib", "OCW_ART_LFS_BUDGET_GIB", DEFAULT_BUDGET_GIB))
    if not 0 < gib <= QUOTA_GIB:
        raise SystemExit(f"LFS budget {gib} GiB: must be above 0 and at most the {QUOTA_GIB:.0f} GiB quota")
    return int(gib * GIB)


def policy() -> str:
    """lfs_policy in ocw-art.toml or OCW_ART_LFS_POLICY: `all` (default) or `pictures`."""
    p = str(setting("lfs_policy", "OCW_ART_LFS_POLICY", "all"))
    if p not in POLICIES:
        raise SystemExit(f"lfs_policy {p!r}: one of {', '.join(POLICIES)}")
    return p


# ----------------------------------------------------------------- git


def repo() -> Path:
    """The git checkout that holds the archive (this one, unless
    OCW_ART_HISTORY points elsewhere)."""
    r = subprocess.run(["git", "-C", str(C.HIST), "rev-parse", "--show-toplevel"], capture_output=True, text=True)
    return Path(r.stdout.strip()) if r.returncode == 0 and r.stdout.strip() else ART


def git(*args, check=True, input=None) -> str:
    r = subprocess.run(["git", "-C", str(repo()), *args], capture_output=True, text=True, input=input)
    if check and r.returncode != 0:
        raise RuntimeError(f"git {' '.join(args[:2])}: {(r.stderr or r.stdout).strip()[-300:]}")
    return r.stdout


def lfs_available() -> str | None:
    """None when git-lfs is installed and set up, else what is missing."""
    if subprocess.run(["git", "lfs", "version"], capture_output=True).returncode != 0:
        return "git-lfs is not installed: " + INSTALL_HINT
    if not git("config", "--get", "filter.lfs.clean", check=False).strip():
        return "git-lfs is not set up (no filter.lfs.clean): run `git lfs install` (make deps)"
    return None


def require_lfs():
    why = lfs_available()
    if why:
        raise SystemExit(why)


def rel(p: Path) -> str:
    return p.resolve().relative_to(repo().resolve()).as_posix()


def tracked() -> dict[str, int]:
    """{path: size} of the media of the archive committed at HEAD (LFS pointers)."""
    out = {}
    if not git("rev-parse", "--verify", "-q", "HEAD", check=False).strip():
        return out
    prefix = rel(C.HIST) + "/"
    try:
        data = json.loads(git("lfs", "ls-files", "--json") or "{}")
    except (RuntimeError, ValueError):
        return out
    for f in data.get("files") or []:
        if f["name"].startswith(prefix):
            out[f["name"]] = int(f["size"])
    return out


def stored_bytes() -> tuple[int, int]:
    """(bytes, objects) of every LFS object in the history (all refs): what
    counts against the storage quota once pushed (each version once)."""
    if not git("rev-parse", "--verify", "-q", "HEAD", check=False).strip():
        return 0, 0
    try:
        data = json.loads(git("lfs", "ls-files", "--all", "--json") or "{}")
    except (RuntimeError, ValueError):
        return 0, 0
    objs = {f["oid"]: int(f["size"]) for f in data.get("files") or []}
    return sum(objs.values()), len(objs)


# ------------------------------------------------------------- the media


def media_days() -> list[str]:
    return sorted(d.name for d in C.HIST.glob("????-??-??") if d.is_dir()
                  and re.fullmatch(r"\d{4}-\d{2}-\d{2}", d.name))


def day_media(day: str, kinds=PICTURES + VIDEOS) -> list[Path]:
    d = C.HIST / day
    return sorted(f for f in d.iterdir() if f.is_file() and f.suffix in kinds and f.stat().st_size > 0) \
        if d.is_dir() else []


def pending(day: str, have: dict[str, int], pol: str, secrets=None) -> dict:
    """The day's media not yet committed (new or changed) under the policy,
    and those held back: a private pattern in the name (never committed),
    or a kind the policy leaves out."""
    new, private, left_out = [], [], []
    for f in day_media(day):
        r = rel(f)
        if r in have and have[r] == f.stat().st_size:
            continue  # committed (a changed file of the same size is caught by git status)
        if private_findings(f.name, secrets):
            private.append(f)
        elif f.suffix not in POLICIES[pol]:
            left_out.append(f)
        else:
            new.append(f)
    return {"files": new, "bytes": sum(f.stat().st_size for f in new), "private": private,
            "left_out": left_out, "left_out_bytes": sum(f.stat().st_size for f in left_out)}


def status(secrets=None, today: str | None = None) -> dict:
    """The budget report (lfs-budget, the collector)."""
    today = today or dt.date.today().isoformat()
    pol, budget = policy(), budget_bytes()
    have = tracked()
    stored, objects = stored_bytes()
    days = {}
    for d in media_days():
        p = pending(d, have, pol, secrets)
        local = day_media(d, POLICIES[pol])
        days[d] = {"local_files": len(local), "local_bytes": sum(f.stat().st_size for f in local),
                   "committed_files": sum(1 for f in local if rel(f) in have),
                   "pending_files": len(p["files"]), "pending_bytes": p["bytes"],
                   "private_names": [f.name for f in p["private"]],
                   "left_out_files": len(p["left_out"]), "left_out_bytes": p["left_out_bytes"]}
    finished = [d for d in days if d < today and days[d]["local_bytes"]]
    rate = sum(days[d]["local_bytes"] for d in finished) / len(finished) if finished else 0
    pend = sum(v["pending_bytes"] for v in days.values())
    free = budget - stored - pend
    return {"policy": pol, "budget": budget, "quota": int(QUOTA_GIB * GIB), "stored_bytes": stored,
            "stored_objects": objects, "tracked_files": len(have), "pending_bytes": pend,
            "pending_files": sum(v["pending_files"] for v in days.values()),
            "rate_per_day": int(rate), "days_left": (free / rate) if rate else None,
            "over_budget": stored + pend > budget, "days": days}


def report(st: dict) -> str:
    g = lambda n: f"{n / GIB:.2f} GiB"  # noqa: E731
    lines = [f"Git LFS (policy {st['policy']}): {g(st['stored_bytes'])} stored in {st['stored_objects']} objects "
             f"({st['tracked_files']} files at HEAD), {g(st['pending_bytes'])} about to be added "
             f"({st['pending_files']} files); budget {g(st['budget'])} of the {g(st['quota'])} quota"]
    for d, v in st["days"].items():
        extra = []
        if v["left_out_files"]:
            extra.append(f"{v['left_out_files']} left out by the policy ({g(v['left_out_bytes'])})")
        if v["private_names"]:
            extra.append(f"{len(v['private_names'])} with a private pattern in the name (never committed)")
        lines.append(f"  {d}: {v['local_files']} files, {g(v['local_bytes'])}; committed {v['committed_files']}, "
                     f"pending {v['pending_files']} ({g(v['pending_bytes'])})" + (f"; {', '.join(extra)}" if extra
                                                                                   else ""))
    if st["rate_per_day"]:
        left = st["days_left"]
        lines.append(f"Rate: {g(st['rate_per_day'])} per build day; "
                     + (f"{left:.1f} days left in the budget" if left > 0 else
                        "the budget is reached: " + budget_advice()))
    if st["over_budget"]:
        lines.append("WARNING: the pending media do not all fit the budget; lfs-commit adds whole days while "
                     "they fit and leaves the rest local (git-ignored).")
    return "\n".join(lines)


def budget_advice() -> str:
    return ("nothing new goes into LFS; options: lfs_policy = \"pictures\" in ocw-art.toml (videos stay local "
            "and on the release), or more LFS storage (a paid data pack) and a higher lfs_budget_gib "
            "(ART-PROJECT §2.8)")


# ------------------------------------------------------------ .gitignore


def ignore_block(text: str) -> dict[str, set[str]]:
    """{day: {extensions}} of the managed allow-list block."""
    out: dict[str, set[str]] = {}
    if BEGIN not in text:
        return out
    block = text.split(BEGIN, 1)[1].split(END, 1)[0]
    for m in re.finditer(r"^!/build-history/(\d{4}-\d{2}-\d{2})/\*(\.\w+)$", block, re.M):
        out.setdefault(m.group(1), set()).add(m.group(2))
    return out


def with_allowed(text: str, day: str, exts) -> str:
    """The .gitignore text with the day's media extensions in the managed block."""
    days = ignore_block(text)
    days.setdefault(day, set()).update(exts)
    body = "\n".join(f"!/build-history/{d}/*{e}" for d in sorted(days) for e in sorted(days[d]))
    block = (f"{BEGIN}\n# The days whose pictures/videos are in Git LFS (ART-PROJECT §2.8), written by\n"
             f"# `diary.py lfs-commit`: do not edit by hand.\n{body}\n{END}")
    if BEGIN in text:
        pre, rest = text.split(BEGIN, 1)
        post = rest.split(END, 1)[1] if END in rest else ""
        return pre + block + post
    return text.rstrip("\n") + "\n\n" + block + "\n"


# ---------------------------------------------------------------- commit


def busy() -> str | None:
    """Why the checkout cannot take an automatic commit now, or None."""
    gd = Path(git("rev-parse", "--absolute-git-dir").strip())
    for n in ("MERGE_HEAD", "rebase-merge", "rebase-apply", "CHERRY_PICK_HEAD", "REVERT_HEAD"):
        if (gd / n).exists():
            return f"a {n.lower().replace('_', ' ')} is in progress"
    b = git("rev-parse", "--abbrev-ref", "HEAD").strip()
    if b != "main":
        return f"the checkout is on {b}, not main"
    return None


def commit_days(days: list[str] | None = None, dry_run: bool = False, secrets=None,
                today: str | None = None, trailers: list[str] = ()) -> dict:
    """One LFS commit per day (oldest first) while the budget holds. Days
    default to every finished day (before today) with pending media.
    Returns {"committed": [...], "refused": [...], "warnings": [...]}."""
    require_lfs()
    today = today or dt.date.today().isoformat()
    pol, budget = policy(), budget_bytes()
    why = busy()
    if why:
        raise SystemExit(f"lfs-commit: {why}")
    have = tracked()
    stored, _ = stored_bytes()
    days = days or [d for d in media_days() if d < today]
    res = {"committed": [], "refused": [], "warnings": [], "policy": pol}
    gi = repo() / ".gitignore"
    for d in sorted(days):
        p = pending(d, have, pol, secrets)
        if p["private"]:
            res["warnings"].append(f"{d}: {len(p['private'])} file name(s) with a private pattern stay local")
        if not p["files"]:
            continue
        if stored + p["bytes"] > budget:
            res["refused"].append({"day": d, "files": len(p["files"]), "bytes": p["bytes"]})
            res["warnings"].append(
                f"LFS budget reached: {d} ({len(p['files'])} files, {p['bytes'] / GIB:.2f} GiB) would bring the "
                f"total to {(stored + p['bytes']) / GIB:.2f} GiB of {budget / GIB:.2f} GiB; it stays local. "
                + budget_advice())
            break  # later days wait too: the history stays in day order
        paths = [rel(f) for f in p["files"]]
        n_pic = sum(f.suffix in PICTURES for f in p["files"])
        n_vid = len(paths) - n_pic
        msg = (f"Build history {d}: {n_pic} pictures and {n_vid} videos in Git LFS "
               f"({p['bytes'] / 1e6:.0f} MB; ART-PROJECT §2.8)")
        if dry_run:
            res["committed"].append({"day": d, "files": len(paths), "bytes": p["bytes"], "dry_run": True})
            stored += p["bytes"]
            continue
        gi.write_text(with_allowed(gi.read_text() if gi.is_file() else "", d,
                                   {f.suffix for f in p["files"]}))
        listing = "\0".join([".gitignore", *paths]) + "\0"
        git("add", "--pathspec-from-file=-", "--pathspec-file-nul", input=listing)
        # Every staged media file must be an LFS pointer (never a raw blob in git).
        attrs = git("check-attr", "filter", "--stdin", "-z", input="\0".join(paths) + "\0").split("\0")
        bad = [attrs[i] for i in range(0, len(attrs) - 2, 3) if attrs[i + 2] != "lfs"]
        staged_raw = [x for x in paths[:50] if not git("cat-file", "-p", f":{x}").startswith(
            "version https://git-lfs.github.com/spec/v1")]
        if bad or staged_raw:
            git("reset", "-q", "--", *(bad or staged_raw)[:50], check=False)
            raise SystemExit(f"lfs-commit: {len(bad or staged_raw)} file(s) would go into git without LFS "
                             f"(check .gitattributes); nothing committed")
        body = msg + ("\n\n" + "\n".join(trailers) if trailers else "")
        git("commit", "-q", "-m", body, "--pathspec-from-file=-", "--pathspec-file-nul", input=listing)
        stored += p["bytes"]
        for x, f in zip(paths, p["files"]):
            have[x] = f.stat().st_size
        res["committed"].append({"day": d, "files": len(paths), "bytes": p["bytes"],
                                 "commit": git("rev-parse", "--short", "HEAD").strip()})
        log(f"lfs-commit: {msg}")
    for w in res["warnings"]:
        log("WARNING: " + w)
    return res


# ------------------------------------------------------------------ push


def push(remote: str = "origin") -> dict:
    """Pushes main when every unpushed commit only touches build-history/
    and .gitignore (the collector's and the coordinator's archive commits);
    then compares the LFS file list with the committed media."""
    require_lfs()
    why = busy()
    if why:
        raise SystemExit(f"lfs-push: {why}")
    git("fetch", "-q", remote, "main")
    ahead = git("rev-list", f"{remote}/main..HEAD").split()
    behind = git("rev-list", f"HEAD..{remote}/main").split()
    if behind:
        raise SystemExit(f"lfs-push: main is {len(behind)} commit(s) behind {remote}/main; pull first")
    if ahead:
        files = set(git("diff", "--name-only", f"{remote}/main..HEAD").split("\n")) - {""}
        other = sorted(f for f in files if not (f.startswith("build-history/") or f == ".gitignore"))
        if other:
            raise SystemExit(f"lfs-push: unpushed commits touch more than the archive ({len(other)} file(s), "
                             f"e.g. {other[0]}); push by hand")
        subprocess.run(["git", "-C", str(repo()), "lfs", "push", remote, "main"], check=True)
        subprocess.run(["git", "-C", str(repo()), "push", "-q", remote, "main"], check=True)
    v = verify()
    log(f"lfs-push: {len(ahead)} commit(s) pushed; {v['lfs_files']} LFS files, {v['committed_media']} media "
        f"committed, {v['stored_bytes'] / GIB:.2f} GiB" + ("" if v["ok"] else " - MISMATCH"))
    return {"pushed": len(ahead), **v}


def verify() -> dict:
    """`git lfs ls-files` against the media committed at HEAD, and the storage."""
    lfs_n = len([x for x in git("lfs", "ls-files", "-n").splitlines() if x.strip()])
    prefix = rel(C.HIST) + "/"
    committed = [x for x in git("ls-files", "-z", "--", prefix).split("\0")
                 if x and Path(x).suffix in PICTURES + VIDEOS and re.match(re.escape(prefix) + r"\d{4}-\d{2}-\d{2}/",
                                                                            x)]
    stored, objects = stored_bytes()
    return {"lfs_files": lfs_n, "committed_media": len(committed), "ok": lfs_n == len(committed),
            "stored_bytes": stored, "stored_objects": objects}


def disk_free() -> int:
    return shutil.disk_usage(repo()).free
