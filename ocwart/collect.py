"""The hourly collector (ART-PROJECT §5.1), run by bin/collect.sh."""

from __future__ import annotations

import datetime as dt
import json
import os
from pathlib import Path

from . import core as C
from . import gallery, lfs
from .archive import gather
from .core import log, STATUS_NAME
from .incidents import incidents
from .journal import journal, media_of
from .mask import check_masked, mask
from .render import sheet

# ----------------------------------------------------------------- collect
#
# The hourly collector (ART-PROJECT §5.1; bin/collect.sh, the
# systemd user timer ocw-art-collect.timer on the dev machine): gather +
# journal of yesterday and today (the last hour before midnight is not
# lost; gather is idempotent), the mask check of the tracked text files,
# the local gallery (incremental, not published), and in the 23:xx run the
# contact sheets of today and the Git LFS commit of the finished days
# (§2.8; bin/collect.sh pushes it after the lock is released). No render,
# no publish.
# Status: test-output/build-log/DAY/art.json (the latest run of DAY) and
# art-runs.jsonl (every run); the output goes to art.log next to them.



def default_collect_days(now: dt.datetime | None = None) -> list[str]:
    now = now or dt.datetime.now()
    return [(now - dt.timedelta(days=1)).strftime("%Y-%m-%d"), now.strftime("%Y-%m-%d")]


def status_dir(day: str) -> Path:
    return C.TEST_OUTPUT / "build-log" / day


def iso_now() -> str:
    return dt.datetime.now().astimezone().isoformat(timespec="seconds")


def write_status(st: dict, final: bool = False):
    d = status_dir(st["run_day"])
    d.mkdir(parents=True, exist_ok=True)
    tmp = d / (STATUS_NAME + ".tmp")
    tmp.write_text(json.dumps(st, indent=1, ensure_ascii=False) + "\n")
    tmp.replace(d / STATUS_NAME)
    if final:
        with open(d / "art-runs.jsonl", "a") as f:
            f.write(json.dumps(st, ensure_ascii=False) + "\n")


def collect(days: list[str] | None = None, sheets: bool | None = None,
            now: dt.datetime | None = None, gallery_: bool = True, lfs_: bool | None = None) -> dict:
    """One collector run; returns its status (status "ok" or "failed").
    gallery_: refresh the local gallery (OCW_ART_GALLERY=0 turns it off);
    lfs_: the LFS commit of the finished days (None: in the 23:xx run;
    OCW_ART_LFS=0 turns LFS off, e.g. on a machine without git-lfs)."""
    now = now or dt.datetime.now()
    days = days or default_collect_days(now)
    if sheets is None:
        sheets = now.hour == 23
    lfs_on = os.environ.get("OCW_ART_LFS") != "0"
    if lfs_ is None:
        lfs_ = now.hour == 23
    gallery_ = gallery_ and os.environ.get("OCW_ART_GALLERY") != "0"
    st = {"start": iso_now(), "end": None, "status": "running", "run_day": now.strftime("%Y-%m-%d"),
          "days": {}, "new_files": 0, "media": 0, "mask_check": None, "sheets": bool(sheets),
          "gallery": None, "lfs": None, "lfs_push": False,
          "errors": [], "warnings": [], "log": os.environ.get("OCW_ART_LOG", "")}
    if lfs_on:
        why = lfs.lfs_available()
        if why:  # gather and journal still run: nothing of the day is lost
            st["errors"].append(why)
            lfs_on = False
    write_status(st)
    for day in days:
        r = st["days"][day] = {"new_files": 0, "media": 0}
        try:
            r["new_files"] = gather(day) or 0
            r["incidents"] = len(incidents(day))
            journal(day)
        except Exception as e:  # one day failing must not hide the other
            st["errors"].append(f"{day}: {type(e).__name__}: {mask(str(e))[:300]}")
        r["media"] = len(media_of(day))
        st["new_files"] += r["new_files"]
    st["media"] = st["days"][days[-1]]["media"]
    try:
        found = check_masked()
        st["mask_check"] = "ok" if not found else f"failed: {len(found)} finding(s)"
        for f in found:
            log("private pattern: " + f)
        if found:
            st["errors"].append(f"mask check: {len(found)} finding(s) (diary.py check-masked)")
    except Exception as e:
        st["mask_check"] = "error"
        st["errors"].append(f"mask check: {type(e).__name__}: {mask(str(e))[:300]}")
    if sheets:
        try:
            sheet(days[-1])
        except Exception as e:
            st["errors"].append(f"sheets {days[-1]}: {type(e).__name__}: {mask(str(e))[:300]}")
    if gallery_:
        try:
            g = gallery.build(jobs=2, assets=None)
            st["gallery"] = f"ok: {g['items']} items, {g['bytes'] / 1e6:.0f} MB, {g['ffmpeg_runs']} new"
        except (Exception, SystemExit) as e:
            st["gallery"] = "failed"
            st["errors"].append(f"gallery: {type(e).__name__}: {mask(str(e))[:300]}")
    if lfs_on:
        try:
            if lfs_:
                r = lfs.commit_days(today=now.strftime("%Y-%m-%d"))
                st["lfs_push"] = bool(r["committed"])
                st["warnings"] += r["warnings"]
            b = lfs.status(today=now.strftime("%Y-%m-%d"))
            st["lfs"] = {"policy": b["policy"], "stored_gib": round(b["stored_bytes"] / lfs.GIB, 2),
                         "pending_gib": round(b["pending_bytes"] / lfs.GIB, 2),
                         "budget_gib": round(b["budget"] / lfs.GIB, 2),
                         "days_left": None if b["days_left"] is None else round(b["days_left"], 1),
                         "days_left_largest": None if b.get("days_left_largest") is None
                         else round(b["days_left_largest"], 1)}
            if b["days_left"] is not None and b["days_left"] < 1:
                st["warnings"].append("LFS budget (nearly) reached: " + lfs.budget_advice())
        except (Exception, SystemExit) as e:
            st["errors"].append(f"lfs: {type(e).__name__}: {mask(str(e))[:300]}")
    for w in st["warnings"]:
        log("WARNING: " + w)
    st["end"] = iso_now()
    st["status"] = "failed" if st["errors"] else "ok"
    write_status(st, final=True)
    log(f"collect: {st['status']}, {st['new_files']} new files, {st['media']} media today, "
        f"mask check {st['mask_check']}")
    return st
