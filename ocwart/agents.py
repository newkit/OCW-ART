"""Agent jobs (ART-PROJECT §2.7): the coordinator's agents.jsonl and the backfill
from git."""

from __future__ import annotations

import datetime as dt
import json
import re
from pathlib import Path

from . import core as C
from . import features as F
from .core import _next_day, git_out, log
from .incidents import _jsonl, INCIDENTS_NAME
from .mask import _secrets, mask

_BRANCHES: dict = {}


def branch_of(sha: str) -> str | None:
    """The agent branch (worktree-agent-…) holding a merge's second parent."""
    if sha in _BRANCHES:
        return _BRANCHES[sha]
    names = [b.strip() for b in git_out("branch", "--format=%(refname:short)", "--contains", sha).splitlines()
             if b.strip().startswith("worktree-agent-")]
    full = git_out("rev-parse", sha).strip()
    tips = [b for b in names if git_out("rev-parse", b).strip() == full]
    # Every branch made from main later contains the commit too; the owner
    # has it on its own first-parent chain.
    own = tips or [b for b in names if full in git_out("rev-list", "--first-parent", b).split()]
    _BRANCHES[sha] = (own or [None])[0]
    return _BRANCHES[sha]


def agents_path(day: str) -> Path:
    return C.TEST_OUTPUT / "build-log" / day / "agents.jsonl"


def agent_event(day: str, task: str, branch: str, event: str, agent: str | None = None, commits: str = "",
                note: str = "", time_: str | None = None) -> dict:
    """Appends one agent event to the day's agents.jsonl (masked)."""
    if event not in F.EVENTS:
        raise SystemExit(f"event: one of {', '.join(F.EVENTS)}")
    e = {"time": time_ or dt.datetime.now().astimezone().isoformat(timespec="seconds"),
         "agent_id_short": F.agent_id(branch, agent), "task": task, "branch": branch, "event": event,
         "commits": commits, "note": note}
    path = agents_path(day)
    path.parent.mkdir(parents=True, exist_ok=True)
    line = mask(json.dumps(e, ensure_ascii=False))
    with open(path, "a") as f:
        f.write(line + "\n")
    return json.loads(line)


def agent_backfill(day: str) -> list[dict]:
    """The day's agent jobs from git (merged agent branches: first and last
    commit, the merge) and the incident log (an OOM kill of the coordinator's
    session interrupts the jobs running then); replaces earlier backfilled
    lines of agents.jsonl."""
    nxt = _next_day(day)
    c0 = git_out("rev-list", "-1", "--first-parent", f"--before={day} 00:00:00", "HEAD").strip()
    c1 = git_out("rev-list", "-1", "--first-parent", f"--before={nxt} 00:00:00", "HEAD").strip()
    rng = f"{c0}..{c1}" if c0 else c1
    kills = [e for e in _jsonl(C.TEST_OUTPUT / "build-log" / day / INCIDENTS_NAME)
             if e.get("kind") == "oom-kill" and "tmux" in str(e.get("text"))]
    note = "backfilled from git"
    out = []
    for line in git_out("log", "--first-parent", "--merges", "--reverse", "--format=%H%x1f%h%x1f%aI%x1f%P%x1f%s",
                        rng).splitlines():
        full, short, iso, parents, subject = line.split("\x1f")
        p1, p2 = parents.split()[:2]
        # A branch that moved on (fast-forwarded to main) owns nothing any more:
        # the job is still listed, under its merge.
        branch = branch_of(p2) or f"merge-{short}"
        times = sorted(git_out("log", "--format=%aI", f"{p1}..{p2}").split())
        if not times:
            continue
        task = re.sub(r"^Merge (branch '[^']*' into \S+|)", "", subject).strip(" :") or branch
        task = task[:100]
        ev = [("started", times[0], ""), ("reported", times[-1], "")]
        for k in kills:
            kt = f"{day}T{k['time']}"
            if times[0][:19] < kt < iso[:19]:
                after = [t for t in times if t[:19] > kt]
                ev.append(("interrupted", kt, "OOM kill of the coordinator session (incidents.md)"))
                if after:
                    ev.append(("resumed", after[0], ""))
        ev.append(("merged", iso, ""))
        for event, t, n in sorted(ev, key=lambda x: x[1][:19]):
            out.append({"time": t, "agent_id_short": F.agent_id(branch), "task": task, "branch": branch,
                        "event": event, "commits": short if event == "merged" else "",
                        "note": "; ".join(x for x in (note, n) if x)})
    # Agent branches not merged (yet) with commits of the day: still running,
    # reported, or left; interrupted when they span the OOM kill.
    done = {e["branch"] for e in out}
    for b in git_out("for-each-ref", "--format=%(refname:short)", "refs/heads/worktree-agent-*").split():
        if b in done:
            continue
        times = sorted(t for t in git_out("log", "--format=%aI", f"HEAD..{b}").split() if t[:10] == day)
        if not times:
            continue
        subj = git_out("log", "-1", "--no-merges", "--format=%s", f"HEAD..{b}").strip()[:100] or b
        ev = [("started", times[0], ""), ("reported", times[-1], "")]
        for k in kills:
            kt = f"{day}T{k['time']}"
            if times[0][:19] < kt:
                after = [t for t in times if t[:19] > kt]
                ev.append(("interrupted", kt, "OOM kill of the coordinator session (incidents.md)"))
                if after:
                    ev.append(("resumed", after[0], ""))
        for event, t, n in sorted(ev, key=lambda x: x[1][:19]):
            out.append({"time": t, "agent_id_short": F.agent_id(b), "task": subj, "branch": b, "event": event,
                        "commits": git_out("rev-parse", "--short", b).strip() if event == "reported" else "",
                        "note": "; ".join(x for x in (note, "not merged yet", n) if x)})
    path = agents_path(day)
    keep = [e for e in _jsonl(path) if not str(e.get("note", "")).startswith(note)]
    path.parent.mkdir(parents=True, exist_ok=True)
    secrets = _secrets()
    path.write_text("".join(mask(json.dumps(e, ensure_ascii=False), secrets) + "\n" for e in keep + out))
    log(f"{day}: {len(out)} backfilled agent events ({len(set(e['branch'] for e in out))} jobs)")
    return out
