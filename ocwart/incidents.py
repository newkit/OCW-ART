"""Incidents (ART-PROJECT §2.6): the dev machine's journal and the build log."""

from __future__ import annotations

import datetime as dt
import json
import os
import re
import subprocess
from pathlib import Path

from . import core as C
from .core import log, run
from .mask import _secrets, mask

# --------------------------------------------------------------- incidents
#
# The incident log (ART-PROJECT §2.6): what went wrong on the build
# infrastructure, collected every hour into test-output/build-log/DAY/
# incidents.jsonl (time, kind, source, machine, text; masked) from the
# journal of this machine (OOM kills, failed and restarted units, read-only)
# and from the build log (machines offline / online, disks over 90 %,
# janitor deletions, failed remote.sh runs); plus the coordinator's
# root-cause notes in build-history/DAY/incidents.md (tracked, masked).

INCIDENTS_NAME = "incidents.jsonl"
DISK_FULL_PCT = 90.0
JOURNAL_RE = re.compile(r"^(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})\S*\s+(\S+)\s+([^:]+):\s+(.*)$")
JOURNAL_GREP = r"OOM killer|Killed process|Out of memory|Failed with result|Scheduled restart job"


def _unit_label(unit: str) -> str:
    """A unit's name for the log: tmux-spawn-<uuid>.scope → tmux scope."""
    if unit.startswith("tmux-spawn-"):
        return "tmux scope (a terminal session)"
    return unit


def parse_journal(lines, host="deb") -> list[dict]:
    """Incidents from `journalctl -o short-iso` lines: OOM kills, failed and
    restarted units. Each OOM kill of a unit is listed once per minute."""
    out, seen = [], set()
    for line in lines:
        m = JOURNAL_RE.match(line.strip())
        if not m:
            continue
        ts, _host, ident, msg = m.groups()
        time_ = ts[11:19]
        k = re.search(r"(?:Out of memory: )?Killed process (\d+) \(([^)]*)\)", msg)
        if k and ident.startswith("kernel"):
            kind, text = "oom-kill", f"kernel OOM killer killed {k.group(2)} (pid {k.group(1)})"
        else:
            u = re.match(r"(\S+\.(?:service|scope|timer)): (.*)$", msg)
            if not u:
                continue
            unit, rest = u.groups()
            label = _unit_label(unit)
            if "killed by the OOM killer" in rest:
                kind, text = "oom-kill", f"OOM killer stopped {label}"
            elif rest.startswith("Failed with result"):
                res = re.search(r"'([^']+)'", rest)
                res = res.group(1) if res else "?"
                if res == "oom-kill" or not unit.startswith("ocw-"):
                    continue  # an OOM kill is already listed; only our own units fail loudly
                kind, text = "unit-failed", f"{label} failed ({res})"
            elif rest.startswith("Scheduled restart job"):
                n = re.search(r"counter is at (\d+)", rest)
                kind, text = "unit-restart", f"{label} restarted" + (f" (restart {n.group(1)})" if n else "")
            else:
                continue
        key = (kind, text, time_[:5])
        if key in seen:
            continue
        seen.add(key)
        out.append({"time": time_, "kind": kind, "source": "journal", "machine": host, "text": text})
    return out


def journal_lines(day: str) -> list[str]:
    """This machine's journal of the day (user and system, read-only),
    filtered to the incident messages. Empty where journalctl is missing
    or OCW_ART_JOURNAL=0 (tests)."""
    if os.environ.get("OCW_ART_JOURNAL") == "0":
        return []
    nxt =(dt.date.fromisoformat(day) + dt.timedelta(days=1)).isoformat()
    lines = []
    for scope in (["--user"], []):
        try:
            r = run(["journalctl", *scope, "--since", f"{day} 00:00:00", "--until", f"{nxt} 00:00:00",
                     "-o", "short-iso", "--no-pager", "-q", "--grep", JOURNAL_GREP],
                    capture_output=True, text=True, check=False, timeout=60)
        except (OSError, subprocess.TimeoutExpired):
            continue
        lines += r.stdout.splitlines()
    return lines


def _jsonl(path: Path) -> list[dict]:
    out = []
    if path.exists():
        for line in path.read_text(errors="replace").splitlines():
            try:
                out.append(json.loads(line))
            except ValueError:
                pass
    return out


def build_log_incidents(day: str, build_log: Path) -> list[dict]:
    """Incidents from the day's build log: machines going offline / online,
    disks over 90 %, janitor deletions, failed remote.sh runs (a count)."""
    out, online, full = [], {}, set()
    for s_ in _jsonl(build_log / "servers.jsonl"):
        t = str(s_.get("time", ""))[11:19]
        for m in (s_.get("status") or {}).get("machines", []) or []:
            name, on = m.get("name", "?"), bool(m.get("online"))
            if online.get(name, True) != on:
                out.append({"time": t, "kind": "machine-offline" if not on else "machine-online",
                            "source": "dashboard", "machine": name,
                            "text": f"{name} {'unreachable' if not on else 'back online'}"
                                    + (f" ({mask(str(m.get('error')))[:60]})" if not on and m.get("error") else "")})
            online[name] = on
            for d in m.get("disks") or []:
                key, pct = (name, d.get("name")), d.get("pct")
                if pct is None:
                    continue
                if pct >= DISK_FULL_PCT and key not in full:
                    full.add(key)
                    out.append({"time": t, "kind": "disk-full", "source": "dashboard", "machine": name,
                                "text": f"disk {d.get('name')} on {name} at {pct:.0f} %"})
                elif pct < DISK_FULL_PCT - 5:
                    full.discard(key)
    for e in _jsonl(build_log / "janitor.jsonl"):
        size = e.get("bytes") or 0
        out.append({"time": str(e.get("time", ""))[11:19], "kind": "janitor-delete", "source": "janitor",
                    "machine": e.get("machine", "?"),
                    "text": f"janitor {e.get('action', 'deleted')} {e.get('path', '')} ({size / 1e9:.1f} GB)"})
    failed = [r for r in _jsonl(build_log / "runs.jsonl") if r.get("exit", 0) != 0]
    if failed:
        per = {}
        for r in failed:
            per[r.get("machine", "?")] = per.get(r.get("machine", "?"), 0) + 1
        out.append({"time": str(failed[-1].get("start", ""))[11:19], "kind": "runs-failed", "source": "remote.sh",
                    "machine": ", ".join(sorted(per)),
                    "text": f"{len(failed)} failed remote.sh runs ("
                            + ", ".join(f"{k} {v}" for k, v in sorted(per.items())) + ")"})
    return out


def incidents(day: str, journal_text: list[str] | None = None) -> list[dict]:
    """Collects the day's incidents into test-output/build-log/DAY/incidents.jsonl
    (rewritten, masked) and returns them."""
    build_log = C.TEST_OUTPUT / "build-log" / day
    lines = journal_lines(day) if journal_text is None else journal_text
    out = parse_journal(lines) + build_log_incidents(day, build_log)
    out.sort(key=lambda e: e["time"])
    secrets = _secrets()
    text = "".join(mask(json.dumps(e, ensure_ascii=False), secrets) + "\n" for e in out)
    build_log.mkdir(parents=True, exist_ok=True)
    (build_log / INCIDENTS_NAME).write_text(text)
    log(f"{day}: {len(out)} incidents")
    return [json.loads(x) for x in text.splitlines()]


def incidents_of(day: str) -> dict:
    """The day's incidents for the journal: the collected ones (test-output,
    else the archive's copy) and the coordinator's notes (incidents.md)."""
    auto = _jsonl(C.TEST_OUTPUT / "build-log" / day / INCIDENTS_NAME)
    if not auto:
        auto = _jsonl(C.HIST / day / "logs" / "build-log" / INCIDENTS_NAME)
    notes_p = C.HIST / day / "incidents.md"
    notes = mask(notes_p.read_text(errors="replace")) if notes_p.exists() else ""
    heads = [h.strip("# ").strip() for h in notes.splitlines() if h.startswith("## ")]
    return {"auto": auto, "notes": notes, "noted": heads}
