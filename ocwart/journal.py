"""The day's journal (ART-PROJECT §2): commits, merges, spec rows, builds,
media, prompts, tokens, incidents, features and agent jobs; journal.md + journal.json."""

from __future__ import annotations

import json
import os
import re
import subprocess

from . import core as C
from . import features as F
from .agents import agents_path, branch_of
from .archive import TIME_RE
from .core import _next_day, AUDIO, day_number, git_lines, git_out, IMAGE, log, OCW_GH, run, VIDEO
from .incidents import _jsonl, incidents_of
from .mask import write_tracked
from .prompts import fmt_tokens, prompts, tokens

# ----------------------------------------------------------------- journal


def commits_of(day: str) -> list[dict]:
    out = []
    fmt = "%H%x1f%h%x1f%ad%x1f%P%x1f%s"
    for line in git_lines(
        "log", "--reverse", f"--format={fmt}", "--date=format-local:%Y-%m-%d %H:%M:%S"
    ):
        full, short, when, parents, subject = line.split("\x1f")
        if not when.startswith(day):
            continue
        out.append(
            {
                "sha": short,
                "time": when[11:],
                "merge": len(parents.split()) > 1,
                "subject": subject,
            }
        )
    # Lines changed (non-merge commits).
    stats = {}
    cur = None
    for line in git_lines(
        "log", "--no-merges", "--format=@%h", "--shortstat",
        "--date=format-local:%Y-%m-%d",
    ):
        if line.startswith("@"):
            cur = line[1:]
        elif cur and "changed" in line:
            ins = re.search(r"(\d+) insertion", line)
            dels = re.search(r"(\d+) deletion", line)
            stats[cur] = (int(ins.group(1)) if ins else 0, int(dels.group(1)) if dels else 0)
    for c in out:
        c["added"], c["removed"] = stats.get(c["sha"], (0, 0))
    out.sort(key=lambda c: c["time"])
    return out


def media_of(day: str) -> list[dict]:
    d = C.HIST / day
    out = []
    for f in sorted(d.iterdir()) if d.exists() else []:
        ext = f.suffix.lower()
        if ext not in IMAGE | VIDEO | AUDIO or f.stat().st_size == 0:
            continue  # empty files (an aborted capture) are kept but not shown
        m = TIME_RE.match(f.name)
        hms = m.group(1) if m else "000000"
        kind = "image" if ext in IMAGE else "video" if ext in VIDEO else "audio"
        out.append({"file": f.name, "time": f"{hms[:2]}:{hms[2:4]}:{hms[4:]}", "kind": kind})
    out.sort(key=lambda m: (m["time"], m["file"]))
    return out


def tests_of(commits: list[dict]) -> int | None:
    """The highest test count a commit message of the day mentions."""
    best = None
    for c in commits:
        for m in re.finditer(r"(\d{3,4}) tests", c["subject"]):
            best = max(best or 0, int(m.group(1)))
    return best


def builds_of(day: str) -> dict:
    """Summary of the day's build log: remote.sh runs and build-server samples."""
    d = C.HIST / day / "logs" / "build-log"
    runs, samples = [], []
    for name, out in (("runs.jsonl", runs), ("servers.jsonl", samples)):
        p = d / name
        if p.exists():
            for line in p.read_text(errors="replace").splitlines():
                try:
                    out.append(json.loads(line))
                except ValueError:
                    pass
    machines = {}
    for r in runs:
        m = machines.setdefault(r.get("machine", "?"), {"runs": 0, "seconds": 0.0, "failed": 0,
                                                         "cargo_s": 0.0, "compiled": 0, "wait_s": 0.0})
        m["runs"] += 1
        m["seconds"] += float(r.get("seconds") or 0)
        m["failed"] += int(r.get("exit", 0) != 0)
        # Cargo's own times, crates compiled and build-slot waits (spec
        # §11.2; runs logged since 2026-11-13, null where cargo was quiet).
        m["cargo_s"] += float(r.get("cargo_s") or 0)
        m["compiled"] += int(r.get("compiled") or 0)
        m["wait_s"] += float(r.get("wait_s") or 0)
    online = {}
    for s_ in samples:
        for m in (s_.get("status") or {}).get("machines", []) or []:
            o = online.setdefault(m.get("name", "?"), [0, 0])
            o[0] += 1 if m.get("online") else 0
            o[1] += 1
    return {
        "runs": len(runs),
        "seconds": sum(float(r.get("seconds") or 0) for r in runs),
        "cargo_s": sum(float(r.get("cargo_s") or 0) for r in runs),
        "compiled": sum(int(r.get("compiled") or 0) for r in runs),
        "wait_s": sum(float(r.get("wait_s") or 0) for r in runs),
        "failed": [r for r in runs if r.get("exit", 0) != 0],
        "longest": sorted(runs, key=lambda r: -float(r.get("seconds") or 0))[:5],
        "machines": machines,
        "online": {k: (v[0] / v[1] if v[1] else 0.0) for k, v in online.items()},
        "samples": len(samples),
    }


# ---------------------------------------------------------------- features
#
# The features log (ART-PROJECT §2.7): the spec rows added on the day, the
# merge that landed each, its check run on marge (build log), the deploys
# (deploys.jsonl, scripts/deploy-test.sh) and releases (gh, skipped when it
# fails or OCW_ART_GH=0); the agent jobs from the coordinator's
# test-output/build-log/DAY/agents.jsonl. Pure parts in features.py.
def releases_of(day: str) -> list[dict]:
    if os.environ.get("OCW_ART_GH") == "0":
        return []
    try:
        r = run(["gh", "release", "list", "-R", OCW_GH, "--limit", "50", "--json",
                 "tagName,name,publishedAt,isPrerelease"], capture_output=True, text=True, check=False, timeout=30)
        rel = json.loads(r.stdout) if r.returncode == 0 else []
    except (OSError, ValueError, subprocess.TimeoutExpired):
        return []
    out = []
    for x in rel:
        t = F.when(x.get("publishedAt") or "")
        if t and t.astimezone().strftime("%Y-%m-%d") == day:
            out.append({"tag": x.get("tagName"), "name": x.get("name"), "time": t.astimezone().isoformat(),
                        "prerelease": x.get("isPrerelease")})
    return out


def features_for(day: str) -> dict:
    """The day's features (spec rows with their merges and checks), deploys
    and releases. Empty parts where git or the build log have nothing."""
    nxt = _next_day(day)
    c0 = git_out("rev-list", "-1", "--first-parent", f"--before={day} 00:00:00", "HEAD").strip()
    c1 = git_out("rev-list", "-1", "--first-parent", f"--before={nxt} 00:00:00", "HEAD").strip()
    if not c1 or c1 == c0:
        feats, merges = [], []
    else:
        rng = f"{c0}..{c1}" if c0 else c1
        start = F.spec_rows(git_out("show", f"{c0}:SPECIFICATION.md")) if c0 else {}
        end = F.spec_rows(git_out("show", f"{c1}:SPECIFICATION.md"))
        log = git_out("log", "--first-parent", "--reverse", "-p", "--diff-merges=first-parent",
                      f"--format={F.COMMIT_MARK}%x1f%H%x1f%h%x1f%aI%x1f%P%x1f%s", rng, "--", "SPECIFICATION.md")
        feats = F.features_of(F.parse_spec_log(log), start, end)
        merges = sorted(git_out("log", "--first-parent", "--merges", "--format=%aI", rng).split())
    bl = C.TEST_OUTPUT / "build-log" / day
    runs = _jsonl(bl / "runs.jsonl")
    for f in feats:
        if not f["merge"]:
            continue
        p2 = f["parents"][1]
        f["branch"] = branch_of(p2)
        until = next((m for m in merges if m > f["time"]), None)
        chk = F.find_check(runs, f["time"], f["branch"], [f["sha"], p2], until)
        if chk and chk.get("log") and (bl / chk["log"]).exists():
            chk.update(F.parse_test_results((bl / chk["log"]).read_text(errors="replace")))
        f["check"] = chk
    for f in feats:
        f.pop("parents", None)
    return {"features": feats, "deploys": _jsonl(bl / "deploys.jsonl"), "releases": releases_of(day)}


def incident_text(j: dict, at: str, text: str | None = None) -> str:
    """The text of an incident card: `text`, else the root-cause note whose
    heading starts with the time `at`, else the first collected incident at
    that time."""
    if text:
        return text
    inc = j.get("incidents") or {}
    for h in inc.get("noted") or []:
        if h.startswith(at):
            return h[len(at):].strip(" –-:")
    for e in inc.get("auto") or []:
        if str(e.get("time", "")).startswith(at):
            return e["text"]
    return "something went wrong"


def journal(day: str) -> dict:
    commits = commits_of(day)
    builds = builds_of(day)
    ps = prompts(day)
    tk = tokens(day)
    media = media_of(day)
    inc = incidents_of(day)
    try:
        feat = features_for(day)
    except Exception as e:  # the journal never fails on the features log
        log(f"{day}: features log skipped ({type(e).__name__}: {e})")
        feat = {"features": [], "deploys": [], "releases": []}
    jobs = F.agent_jobs(_jsonl(agents_path(day)))
    spec = [
        m.group(1)
        for c in commits
        for m in [re.search(r"[Ss]pec (?:v)?(\d+\.\d+)", c["subject"])]
        if m
    ]
    j = {
        "day": day,
        "number": day_number(day),
        "commits": commits,
        "merges": sum(c["merge"] for c in commits),
        "lines_added": sum(c["added"] for c in commits),
        "lines_removed": sum(c["removed"] for c in commits),
        "spec_versions": spec,
        "tests": tests_of(commits),
        "media": media,
        "images": sum(m["kind"] == "image" for m in media),
        "videos": sum(m["kind"] == "video" for m in media),
        "sounds": sum(m["kind"] == "audio" for m in media),
        "builds": {k: v for k, v in builds.items() if k not in ("longest",)},
        "prompts": ps,
        "tokens": {"total": tk["total"], "features": tk["features"]},
        "incidents": inc,
        "features": feat["features"],
        "deploys": feat["deploys"],
        "releases": feat["releases"],
        "agent_jobs": jobs,
    }
    d = C.HIST / day
    d.mkdir(parents=True, exist_ok=True)
    write_tracked(d / "journal.json", json.dumps(j, indent=1, ensure_ascii=False))
    md = [
        f"# OCW build diary – day {j['number']}, {day}",
        "",
        f"{len(commits)} commits ({j['merges']} merges), +{j['lines_added']} / "
        f"−{j['lines_removed']} lines, {j['images']} images, {j['videos']} videos, "
        f"{j['sounds']} sounds" + (f", {j['tests']} tests" if j["tests"] else "") + ".",
        "",
        "## Commits",
        "",
        "| Time | Commit | |",
        "|---|---|---|",
    ]
    for c in commits:
        md.append(
            f"| {c['time'][:5]} | `{c['sha']}`{' (merge)' if c['merge'] else ''} | "
            f"{c['subject'].replace('|', '/')} |"
        )
    if builds["runs"] or builds["samples"]:
        md += ["", "## Builds and build servers", "",
               f"{builds['runs']} build/test runs on the build machines, "
               f"{builds['seconds'] / 3600:.1f} h in total, {len(builds['failed'])} failed; "
               f"{builds['samples']} server samples; cargo compiled {builds['compiled']} crates "
               f"in {builds['cargo_s'] / 3600:.1f} h, {builds['wait_s'] / 3600:.1f} h waiting for build slots.", "",
               "| Machine | Runs | Hours | Cargo h | Crates | Waited h | Failed | Online |",
               "|---|---|---|---|---|---|---|---|"]
        for name in sorted(set(builds["machines"]) | set(builds["online"])):
            m = builds["machines"].get(name, {"runs": 0, "seconds": 0, "failed": 0})
            on = builds["online"].get(name)
            md.append(f"| {name} | {m['runs']} | {m['seconds'] / 3600:.1f} | "
                      f"{m.get('cargo_s', 0) / 3600:.1f} | {m.get('compiled', 0)} | "
                      f"{m.get('wait_s', 0) / 3600:.1f} | {m['failed']} | "
                      + (f"{on:.0%}" if on is not None else "–") + " |")
        if builds["failed"]:
            md += ["", "Failed runs:", ""]
            md += [f"- {r.get('start', '')[11:16]} {r.get('machine')}: `{r.get('command', '')[:80]}` "
                   f"(exit {r.get('exit')}, log `build-log/{r.get('log')}`)" for r in builds["failed"]]
        if builds["longest"]:
            md += ["", "Longest runs:", ""]
            md += [f"- {float(r.get('seconds') or 0) / 60:.0f} min on {r.get('machine')}: "
                   f"`{r.get('command', '')[:80]}`" for r in builds["longest"]]
    if tk["total"].get("total"):
        tt = tk["total"]
        md += ["", "## Token usage", "",
               f"{fmt_tokens(tt['total'])} tokens in {tt['messages']:,} model messages "
               f"(output {fmt_tokens(tt['output'])}, cache reads {fmt_tokens(tt['cache_read'])}, "
               f"cache writes {fmt_tokens(tt['cache_write'])}, uncached input {fmt_tokens(tt['input'])}). "
               "Full breakdown: [tokens.json](tokens.json).", "",
               "| Feature | Tokens | Output | Messages |", "|---|---|---|---|"]
        for name, v in sorted(tk["features"].items(), key=lambda kv: -kv[1]["total"]):
            md.append(f"| {name} | {fmt_tokens(v['total'])} | {fmt_tokens(v['output'])} | {v['messages']:,} |")
        md += ["", "| Task | Feature | Tokens | Output |", "|---|---|---|---|"]
        for name, v in sorted(tk["tasks"].items(), key=lambda kv: -kv[1]["total"])[:40]:
            md.append(f"| {name.replace('|', '/')} | {v['feature']} | {fmt_tokens(v['total'])} | {fmt_tokens(v['output'])} |")
    if ps:
        md += ["", "## Prompts", "", f"{len(ps)} prompts (full text: [prompts.md](prompts.md)).", "",
               "| Time | Prompt |", "|---|---|"]
        md += [f"| {p_['time'][:5]} | {p_['text'][:140].replace('|', '/').replace(chr(10), ' ')} |" for p_ in ps]
    if feat["features"] or feat["deploys"] or feat["releases"]:
        md += ["", "## Features", "",
               f"{len(feat['features'])} spec versions added, {sum(f['merge'] for f in feat['features'])} "
               f"landed by a merge; {len(feat['deploys'])} deploys, {len(feat['releases'])} releases.", ""]
        if feat["features"]:
            md += ["| Spec | Feature | Landed | Check (marge) |", "|---|---|---|---|"]
            for f in feat["features"]:
                landed = (f"{str(f['time'])[11:16]} `{f['commit']}`" + (" (merge)" if f["merge"] else "")
                          if f["commit"] else "–")
                c = f.get("check")
                chk = "–" if not c else (
                    f"{'ok' if c['exit'] == 0 else 'exit ' + str(c['exit'])} at {str(c['time'])[11:16]}"
                    + (f", {c['suites']} suites, {c['passed']} passed, {c['failed']} failed" if c.get("suites") else "")
                    + f" ({c['how']})")
                md.append(f"| {f['version']} | {f['title'].replace('|', '/')} | {landed} | {chk} |")
        if feat["deploys"]:
            md += ["", "Deploys:", ""]
            md += [f"- {str(d_.get('start', ''))[11:16]} {d_.get('machine')}: `{d_.get('commit')}` "
                   f"({'ok' if d_.get('exit') == 0 else 'exit ' + str(d_.get('exit'))})" for d_ in feat["deploys"]]
        if feat["releases"]:
            md += ["", "Releases:", ""]
            md += [f"- {r_['time'][11:16]} {r_['tag']}" + (" (pre-release)" if r_.get("prerelease") else "")
                   for r_ in feat["releases"]]
    if jobs:
        md += ["", "## Agent jobs", "", f"{len(jobs)} jobs (coordinator log agents.jsonl).", "",
               "| Task | Branch | Start | End | Status | Interrupted | Merged |", "|---|---|---|---|---|---|---|"]
        for a in jobs:
            md.append(f"| {str(a['task'])[:90].replace('|', '/')} | {a['agent']} | {str(a['start'] or '')[11:16]} | "
                      f"{str(a['end'] or '')[11:16]} | {a['status']} | {a['interruptions'] or ''} | "
                      f"{('`' + a['merged'] + '`') if a['merged'] else ''} |")
    if inc["auto"] or inc["notes"]:
        kinds = {}
        for e in inc["auto"]:
            kinds[e["kind"]] = kinds.get(e["kind"], 0) + 1
        md += ["", "## Incidents", "",
               f"{len(inc['auto'])} collected ("
               + (", ".join(f"{k} {v}" for k, v in sorted(kinds.items())) or "none")
               + f"), {len(inc['noted'])} with root-cause notes ([incidents.md](incidents.md)).", ""]
        if inc["auto"]:
            md += ["| Time | Kind | Machine | What |", "|---|---|---|---|"]
            md += [f"| {e['time'][:5]} | {e['kind']} | {e.get('machine', '')} | {str(e['text']).replace('|', '/')} |"
                   for e in inc["auto"][:60]]
        if inc["notes"]:
            body = [ln for ln in inc["notes"].splitlines() if not ln.startswith("# ")]
            md += ["", "### Root-cause notes", ""] + [("#" + ln) if ln.startswith("## ") else ln for ln in body]
    md += ["", "## Media", "", "| Time | File |", "|---|---|"]
    md += [f"| {m['time']} | [{m['file']}]({m['file']}) |" for m in media]
    write_tracked(d / "journal.md", "\n".join(md) + "\n")
    log(f"{day}: journal – {len(commits)} commits, {len(media)} media")
    return j
