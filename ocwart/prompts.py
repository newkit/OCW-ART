"""The user's prompts (ART-PROJECT §2.3) and the token usage (§2.4), both from
the Claude Code session transcripts."""

from __future__ import annotations

import datetime as dt
import json
import os
import re
from pathlib import Path

from . import core as C
from .core import log
from .mask import _secrets, mask, write_tracked

# ----------------------------------------------------------------- prompts
#
# The user's prompts to Claude Code are part of the story (ART-PROJECT §2.3):
# taken from the session transcripts (~/.claude/projects/*OCW*/*.jsonl, the
# main sessions only, not the agents'), with host names, user names, e-mail
# addresses and keys masked, into DAY/prompts.jsonl and DAY/prompts.md.

TRANSCRIPTS = os.environ.get("OCW_TRANSCRIPTS", str(Path.home() / ".claude" / "projects"))


def transcript_files(root: Path) -> list[Path]:
    """The main sessions' transcripts: projects named *OCW* (the checkout, its
    worktrees, the old user's checkout), plus the folder holding the OCW
    checkout (on deb since 2026-11-16 the coordinator runs in ~/src, project
    `-home-claude-src`, next to OCW and OCW-ART)."""
    dirs = set(root.glob("*OCW*"))
    parent = root / re.sub(r"[^A-Za-z0-9]", "-", str(C.ROOT.resolve().parent))
    if parent.is_dir():
        dirs.add(parent)
    return sorted(f for d in dirs for f in d.glob("*.jsonl"))
REMINDER_RE = re.compile(r"<system-reminder>.*?</system-reminder>", re.S)
def prompt_text(raw: str) -> str | None:
    """The user's words from a transcript message, or None for anything that
    is not a human prompt (tool output, notifications, agent messages)."""
    t = REMINDER_RE.sub("", raw).strip()
    if not t:
        return None
    m = re.match(r"<command-name>(/?[^<]+)</command-name>.*?(?:<command-args>(.*?)</command-args>)?", t, re.S)
    if m:
        return (("/" + m.group(1).lstrip("/")) + (" " + m.group(2).strip() if m.group(2) else "")).strip()
    bad = ("<task-notification", "<agent-message", "[SYSTEM NOTIFICATION", "Another Claude session",
           "<local-command", "[Request interrupted", "Caveat:", "<command-message", "This session is being continued")
    if any(t.startswith(b) or b in t[:200] for b in bad):
        return None
    return t


def prompts_of(day: str) -> list[dict]:
    seen, out = set(), []
    files = transcript_files(Path(TRANSCRIPTS))
    for f in files:
        for line in f.read_text(errors="replace").splitlines():
            if '"user"' not in line and "queued_command" not in line:
                continue
            try:
                d = json.loads(line)
            except ValueError:
                continue
            text, ts = None, d.get("timestamp", "")
            if d.get("type") == "user" and not d.get("isMeta") and d.get("userType", "external") == "external":
                c = (d.get("message") or {}).get("content")
                if isinstance(c, str):
                    text = prompt_text(c)
            elif d.get("type") == "attachment":
                a = d.get("attachment") or {}
                if a.get("type") == "queued_command" and (a.get("origin") or {}).get("kind") == "human":
                    text = prompt_text(str(a.get("prompt", "")))
            if not text or not ts:
                continue
            local = dt.datetime.fromisoformat(ts.replace("Z", "+00:00")).astimezone()
            if local.strftime("%Y-%m-%d") != day:
                continue
            key = (text, local.strftime("%H:%M"))
            if key in seen:
                continue
            seen.add(key)
            out.append({"time": local.strftime("%H:%M:%S"), "iso": local.isoformat(timespec="seconds"),
                        "text": text})
    secrets = _secrets()
    for p_ in out:
        p_["text"] = mask(p_["text"], secrets)
    out.sort(key=lambda p_: p_["time"])
    return out


def prompts(day: str) -> list[dict]:
    ps = prompts_of(day)
    d = C.HIST / day
    d.mkdir(parents=True, exist_ok=True)
    (d / "prompts.jsonl").write_text("".join(json.dumps(p_, ensure_ascii=False) + "\n" for p_ in ps))
    md = [f"# Prompts – {day}", "", f"{len(ps)} prompts to Claude Code (main session; masked).", ""]
    for p_ in ps:
        md += [f"**{p_['time']}**", "", "> " + p_["text"].replace("\n", "\n> "), ""]
    (d / "prompts.md").write_text("\n".join(md))
    log(f"{day}: {len(ps)} prompts")
    return ps


# ------------------------------------------------------------------ tokens
#
# Token usage of the build (ART-PROJECT §2.4): every assistant message of the
# Claude Code sessions of this project – the main session and every agent
# (subagents/agent-*.jsonl with their meta.json) – counted once per message
# (de-duplicated by message id), by the local day of its timestamp.
#   task:    an agent's task description; for the main session the user
#            prompt the message answered ("coordination: <prompt>")
#   feature: a coarse group from keywords in the task (FEATURES below)
# Totals: input (uncached), cache writes, cache reads, output.

FEATURES = [  # first match wins: specific features before broad ones
    ("Art project", r"art project|diary|build.?history|readme|logo|prompts? (in|of)|token"),
    ("Materials & look", r"material|texture|shadow|tunnel|marking|wheel|graphic"),
    ("UI & menus", r"menu|hud|timestamp|screenshot|capture|kiosk|dashboard"),
    ("Sky, time & weather", r"\bsun\b|sky|time machine|weather|season|night|day/night"),
    ("Audio & voice", r"audio|sound|freehub|voice|noise"),
    ("Riders & bikes", r"rider|bike|model|animation|\blegs?\b"),
    ("Multiplayer & server", r"multiplayer|server|quic|\bbots?\b"),
    ("Worlds & terrain", r"world|terrain|black ?forest|liechtenstein|tenerif|osm|\bdem\b|bridge|clean|package|route|mummelsee"),
    ("Build, release & infra", r"build|release|deploy|\bci\b|windows|\bmac|clang|version|machine|coordinator"),
    ("Planning & spec", r"plan|spec|phase|\bvr\b|browser|question"),
]


def feature_of(task: str) -> str:
    t = (task or "").lower()
    for name, rx in FEATURES:
        if re.search(rx, t):
            return name
    return "Other"


def _usage(u: dict) -> dict:
    return {"input": int(u.get("input_tokens") or 0),
            "cache_write": int(u.get("cache_creation_input_tokens") or 0),
            "cache_read": int(u.get("cache_read_input_tokens") or 0),
            "output": int(u.get("output_tokens") or 0)}


def _add(acc: dict, u: dict):
    for k, v in u.items():
        acc[k] = acc.get(k, 0) + v
    acc["total"] = acc.get("total", 0) + sum(u.values())
    acc["messages"] = acc.get("messages", 0) + 1


def tokens_of(day: str) -> dict:
    root = Path(TRANSCRIPTS)
    seen = set()
    total, per_task, per_feature, per_model = {}, {}, {}, {}
    sources = []
    for f in transcript_files(root):
        sources.append((f, None))
        for a in (f.parent / f.stem / "subagents").glob("agent-*.jsonl"):
            meta = a.with_suffix(".meta.json")
            desc = ""
            if meta.exists():
                try:
                    desc = json.loads(meta.read_text()).get("description", "")
                except ValueError:
                    pass
            sources.append((a, desc or a.stem))
    secrets = _secrets()
    for f, agent in sources:
        last_prompt = None
        for line in f.read_text(errors="replace").splitlines():
            if agent is None and ('"user"' in line or "queued_command" in line):
                try:
                    d = json.loads(line)
                except ValueError:
                    continue
                text = None
                if d.get("type") == "user" and isinstance((d.get("message") or {}).get("content"), str):
                    text = prompt_text(d["message"]["content"])
                elif d.get("type") == "attachment":
                    a_ = d.get("attachment") or {}
                    if a_.get("type") == "queued_command" and (a_.get("origin") or {}).get("kind") == "human":
                        text = prompt_text(str(a_.get("prompt", "")))
                if text:
                    last_prompt = text
                continue
            if '"usage"' not in line or '"assistant"' not in line:
                continue
            try:
                d = json.loads(line)
            except ValueError:
                continue
            if d.get("type") != "assistant":
                continue
            m = d.get("message") or {}
            key = (m.get("id"), d.get("requestId"))
            if key in seen or not m.get("usage"):
                continue
            seen.add(key)
            ts = d.get("timestamp", "")
            try:
                local = dt.datetime.fromisoformat(ts.replace("Z", "+00:00")).astimezone()
            except ValueError:
                continue
            if local.strftime("%Y-%m-%d") != day:
                continue
            u = _usage(m["usage"])
            if agent is not None:
                task = "agent: " + agent
            else:
                p = " ".join((last_prompt or "(session start)").split())
                task = "coordination: " + mask(p[:80] + ("…" if len(p) > 80 else ""), secrets)
            feat = feature_of(agent if agent is not None else (last_prompt or ""))
            _add(total, u)
            _add(per_task.setdefault(task, {"feature": feat}), u)
            _add(per_feature.setdefault(feat, {}), u)
            _add(per_model.setdefault(m.get("model", "?"), {}), u)
    return {"day": day, "total": total, "tasks": per_task, "features": per_feature, "models": per_model}


def tokens(day: str) -> dict:
    t = tokens_of(day)
    d = C.HIST / day
    d.mkdir(parents=True, exist_ok=True)
    write_tracked(d / "tokens.json", json.dumps(t, indent=1, ensure_ascii=False))
    log(f"{day}: {t['total'].get('total', 0):,} tokens in {t['total'].get('messages', 0)} messages")
    return t


def fmt_tokens(n: int) -> str:
    return f"{n / 1e9:.2f} B" if n >= 1e9 else f"{n / 1e6:.1f} M" if n >= 1e6 else f"{n / 1e3:.0f} k"
