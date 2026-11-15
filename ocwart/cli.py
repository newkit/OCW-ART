#!/usr/bin/env python3
"""OCW Build Diary: the art project's tool (docs/ART-PROJECT.md).

    diary.py fetch   [DAY...]   download and unpack the day zips from the
                                GitHub release `build-history` (OCW-ART,
                                else OCW's for days 1-4)
    diary.py gather  [DAY...]   collect every image, video, sound, text and
                                log of the day into build-history/DAY/
    diary.py stamp   [DAY...]   write the ISO 8601 capture time into every
                                archived PNG/MP4 that has none (gather does it)
    diary.py prompts [DAY...]   the user's prompts of the day (from the Claude
                                Code transcripts, masked) – journal runs it
    diary.py journal [DAY...]   write DAY/journal.md + journal.json (commits,
                                merges, spec versions, tests, media; masked)
    diary.py sheet   DAY        contact sheets of the day's media (for
                                writing the day's script)
    diary.py render  [DAY...]   render the day video(s) from days/DAY.toml
    diary.py diary              chain all day videos into the diary video
    diary.py publish [DAY...]   zip the day folders and upload zips and
                                videos to the release `build-history` of
                                newkit/OCW-ART (--videos: only the videos
                                and SHA256SUMS)
    diary.py all     [DAY...]   gather + journal + render + diary
    diary.py collect [--sheets|--no-sheets] [--no-gallery] [--lfs|--no-lfs] [DAY...]
                                the hourly collector (bin/collect.sh):
                                gather + journal of yesterday and today,
                                the mask check, the local gallery; in the
                                23:xx run the contact sheets and the LFS
                                commit of the finished days; status in
                                OCW's test-output/build-log/DAY/art.json
                                (the build dashboard reads it)
    diary.py gallery build|publish|deploy|serve [--max-mb N] [--jobs N]
                 [--wait] [--port P]
                                the web gallery (§6): build it locally
                                (build-history/.work/gallery/site/), upload
                                its zips to the release and deploy it to
                                GitHub Pages, deploy only, or preview it
    diary.py lfs-budget         the Git LFS total, the budget and the days
                                left (§2.8)
    diary.py lfs-commit [--dry-run] [--trailer T] [DAY...]
                                commit the days' media to Git LFS, one
                                commit per day, within the budget (default:
                                every finished day with new media)
    diary.py lfs-push           push the archive commits (LFS objects
                                first) and verify the LFS file list
    diary.py agent-event --task T --branch B --event E [--agent ID]
                 [--commits C] [--note N] [--time ISO] [--day DAY]
                                append an agent job event (E: started,
                                reported, interrupted, resumed, merged,
                                abandoned) to OCW's test-output/build-log/
                                DAY/agents.jsonl, masked (the coordinator)
    diary.py agent-backfill DAY the day's agent jobs from git (merged agent
                                branches) and the incident log
    diary.py check-masked [--fix]
                                fail if a tracked text file of the archive
                                (index.md, SHA256SUMS, DAY/journal.*,
                                DAY/tokens.json, DAY/incidents.md) or a
                                media file name holds a private pattern;
                                --fix masks the text files in place
    diary.py ocw-repo           print the OCW checkout the tool reads

DAY is YYYY-MM-DD; without DAY: every day that has a script in days/.
The OCW checkout (git log, SPECIFICATION.md, test-output/, config/
machines.toml for the mask): OCW_REPO, else `ocw_repo` in ocw-art.toml,
else ../OCW next to this checkout.
Needs Python 3.11+ (tomllib), ffmpeg/ffprobe with libass, git-lfs, and
`gh` for fetch/publish (make deps). The media land in build-history/; only
its masked text files and, through Git LFS within the budget, the day
folders' pictures and videos are committed (§2.5, §2.8).
Runs never overlap: every command but check-masked, lfs-budget, lfs-push
and gallery serve takes the lock build-history/.lock (bin/collect.sh takes
the same one).
"""


from __future__ import annotations

import argparse
import contextlib
import datetime as dt
import json
import os
import re
import sys

from . import core as C
from . import features as F
from . import gallery, lfs
from .agents import agent_backfill, agent_event
from .archive import fetch, gather, stamp
from .collect import collect, iso_now, write_status
from .core import all_days, art_lock, check_ocw, days_with_scripts, log
from .journal import journal
from .mask import check_masked, tracked_files
from .prompts import prompts, tokens
from .publish import publish
from .render import diary, render, sheet


def main():
    if len(sys.argv) < 2 or sys.argv[1] in {"-h", "--help", "help"}:
        print(__doc__)
        return
    cmd, args = sys.argv[1], sys.argv[2:]
    if cmd == "ocw-repo":  # for collect.sh and the Makefile
        print(C.ROOT)
        return
    try:
        check_ocw()
    except SystemExit as e:
        if cmd == "collect":  # the dashboard shows why the collector stopped
            now = iso_now()
            write_status({"start": now, "end": now, "status": "failed", "run_day": now[:10], "days": {},
                          "new_files": 0, "media": None, "mask_check": None, "sheets": False,
                          "errors": [str(e).splitlines()[0]], "log": os.environ.get("OCW_ART_LOG", "")},
                         final=True)
        raise
    if cmd == "agent-event":
        ap = argparse.ArgumentParser(prog="diary.py agent-event")
        ap.add_argument("--task", required=True)
        ap.add_argument("--branch", required=True)
        ap.add_argument("--event", required=True, choices=F.EVENTS)
        ap.add_argument("--agent", help="agent id (default: from the branch name)")
        ap.add_argument("--commits", default="")
        ap.add_argument("--note", default="")
        ap.add_argument("--time", help="ISO 8601 time (default: now)")
        ap.add_argument("--day", help="YYYY-MM-DD (default: the time's day)")
        a = ap.parse_args(args)
        t = a.time or dt.datetime.now().astimezone().isoformat(timespec="seconds")
        e = agent_event(a.day or t[:10], a.task, a.branch, a.event, a.agent, a.commits, a.note, t)
        print(json.dumps(e, ensure_ascii=False))
        return
    if cmd == "gallery":
        gallery_command(args)
        return
    if cmd in ("lfs-budget", "lfs-commit", "lfs-push"):
        lfs_command(cmd, args)
        return
    flags = {a for a in args if a.startswith("--")}
    days = [a for a in args if not a.startswith("--")]
    if cmd == "check-masked":
        fix = "--fix" in flags
        with art_lock(cmd) if fix else contextlib.nullcontext():
            found = check_masked(fix=fix)
        for f in found:
            print(f)
        n = len(tracked_files())
        if found:
            raise SystemExit(f"check-masked: {len(found)} private pattern(s) in the tracked text files or media "
                             f"names (values not shown); `diary.py check-masked --fix` masks the text files")
        log(f"check-masked: {n} tracked text files and the media names, no private patterns")
        return
    check_days(days)
    with art_lock(" ".join(sys.argv[1:])):
        run_command(cmd, days, flags)


def check_days(days):
    for d in days:
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", d):
            raise SystemExit(f"not a day: {d}")


def gallery_command(args):
    ap = argparse.ArgumentParser(prog="diary.py gallery")
    ap.add_argument("action", choices=["build", "publish", "deploy", "serve"])
    ap.add_argument("--max-mb", type=float, default=gallery.DEFAULT_MAX_MB,
                    help=f"size budget of the site (default {gallery.DEFAULT_MAX_MB}; Pages allows 1000)")
    ap.add_argument("--jobs", type=int, default=gallery.DEFAULT_JOBS,
                    help=f"ffmpeg processes at once (1-{gallery.MAX_JOBS})")
    ap.add_argument("--wait", action="store_true", help="publish/deploy: wait for the Pages deployment")
    ap.add_argument("--port", type=int, default=8000, help="serve: the local port")
    a = ap.parse_args(args)
    if not 0 < a.max_mb < 1000:
        raise SystemExit("--max-mb: above 0 and below 1000 (GitHub Pages allows 1 GB per site)")
    if a.action == "serve":
        gallery.serve(a.port)
    elif a.action == "deploy":
        gallery.deploy(a.wait)
    else:
        with art_lock(f"gallery {a.action}"):
            if a.action == "build":
                gallery.build(a.max_mb, a.jobs)
            else:
                gallery.publish(a.max_mb, a.jobs, a.wait)


def lfs_command(cmd, args):
    if cmd == "lfs-budget":
        why = lfs.lfs_available()
        if why:
            raise SystemExit(why)
        print(lfs.report(lfs.status()))
        return
    if cmd == "lfs-push":
        r = lfs.push()
        if not r["ok"]:
            raise SystemExit(f"lfs-push: {r['lfs_files']} LFS files but {r['committed_media']} committed media")
        return
    ap = argparse.ArgumentParser(prog="diary.py lfs-commit")
    ap.add_argument("days", nargs="*")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--trailer", action="append", default=[], help="a line appended to each commit message")
    a = ap.parse_args(args)
    check_days(a.days)
    with art_lock("lfs-commit"):
        r = lfs.commit_days(a.days or None, a.dry_run, trailers=a.trailer)
    for c in r["committed"]:
        log(f"{'would commit' if c.get('dry_run') else 'committed'} {c['day']}: {c['files']} files, "
            f"{c['bytes'] / lfs.GIB:.2f} GiB" + (f" ({c['commit']})" if c.get("commit") else ""))
    if not r["committed"] and not r["refused"]:
        log("lfs-commit: nothing new to commit")
    if r["refused"]:
        raise SystemExit("lfs-commit: the budget is reached; " + lfs.budget_advice())


def run_command(cmd: str, days: list[str], flags: set[str] = frozenset()):
    if cmd == "diary":
        diary()
        return
    if cmd == "collect":
        sheets = True if "--sheets" in flags else False if "--no-sheets" in flags else None
        lfs_ = True if "--lfs" in flags else False if "--no-lfs" in flags else None
        st = collect(days or None, sheets, gallery_=("--no-gallery" not in flags), lfs_=lfs_)
        if st["status"] != "ok":
            raise SystemExit("collect failed: " + "; ".join(st["errors"]))
        return
    if cmd == "publish" and "--videos" in flags:  # only the videos (+ SHA256SUMS), no day zips
        publish([])
        return
    if not days:
        days = all_days() if cmd in {"fetch", "gather", "journal", "publish", "stamp", "prompts", "tokens"} \
            else days_with_scripts()
    if cmd == "all":
        for d in days:
            gather(d)
            journal(d)
            render(d)
        diary()
        return
    fn = {"fetch": fetch, "gather": gather, "journal": journal, "sheet": sheet,
          "render": render, "stamp": stamp, "prompts": prompts,
          "tokens": tokens, "agent-backfill": agent_backfill}.get(cmd)
    if cmd == "publish":
        publish(days)
    elif fn:
        for d in days:
            fn(d)
    else:
        raise SystemExit(f"unknown command {cmd}; see diary.py --help")


if __name__ == "__main__":
    main()
