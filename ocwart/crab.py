"""A day without tokens (ART-PROJECT §4.1): an ASCII crab turns its pockets
out. 2026-11-20 had no build at all – the account's weekly token limit was
reached on the evening before ("You've hit your weekly limit · resets Nov
21, 9am") – so the day has no pictures of the game. The diary tells it with
its own: a terminal-orange ASCII crab on a dark terminal, in the spirit of
the Claude Code CLI's mascot (drawn here, not copied), pulls its trouser
pockets inside out; a moth and some dust fly out, the token counter runs
down to 0.

    diary.py crab DAY   →  build-history/DAY/120000-no-tokens-crab-pockets.mp4
                           the terminal alone (…-0-terminal.jpg, the title's
                           background) and three stills of the clip (…-1-limit.jpg,
                           …-2-pockets.jpg, …-3-moth.jpg), for the day script

Everything is text: each animation frame is one block of Fira Mono in the
ASS layer the day videos use (subtitles.py), drawn by ffmpeg/libass over a
dark background, ten ASCII frames a second. Deterministic; no Pillow.
"""

from __future__ import annotations

import math
import random
from pathlib import Path

from . import core as C
from .core import ffmpeg, FONTS, FPS, H, log, now_meta, W
from .subtitles import ass_header, col, num_fmt, Subs, ts

ORANGE = "D97757"  # the terminal's orange
LINING = "F4EFE6"  # the pockets' white lining
DUST = "8C8577"
MOTH = "CDBFA4"
DIM = "6E6A63"
GREY = "B8B2A7"
RED = "FF5A4F"
BG = "16141A"

SECONDS = 22.0
TICK = 0.1  # one ASCII frame
NAME = "120000-no-tokens-crab-pockets"
LIMIT = "You've hit your weekly limit · resets Nov 21, 9am"
CAPTION = "2026-11-20 – no tokens left · weekly limit · resets Nov 21, 9:00"

# The crab, 30 columns wide: E the eyes (on stalks), MM the mouth; [ … ]
# marks the pockets' lining (white), the brackets themselves are not drawn.
# Every pose has the same 11 rows and the body at the same columns.
_UP = [
    r"  (\/)                  (\/)  ",
    r"   \ \     E      E     / /   ",
    r"    \ \    |      |    / /    ",
    r"     \ \.-''''''''''-./ /     ",
    r"      \_/            \_/      ",
    r"        |     MM     |        ",
    r"        |============|        ",
    r"        |     ||     |        ",
    r"        |     ||     |        ",
    r"        |_____||_____|        ",
    r"       (_____)  (_____)       ",
]
_DOWN = [  # the claws go down into the pockets
    r"                              ",
    r"           E      E           ",
    r"           |      |           ",
    r"        .-''''''''''-.        ",
    r"       /              \       ",
    r"      / |     MM     | \      ",
    r"     / /|============|\ \     ",
    r"    (\/)|     ||     |(\/)    ",
    r"        |     ||     |        ",
    r"        |_____||_____|        ",
    r"       (_____)  (_____)       ",
]
_OUT = [  # the pockets inside out, the claws holding them
    r"                              ",
    r"           E      E           ",
    r"           |      |           ",
    r"        .-''''''''''-.        ",
    r"       /              \       ",
    r"      / |     MM     | \      ",
    r"     /  |============|  \     ",
    r" (\/)[.-.]|     ||     |[.-.](\/) ",
    r"     [| |]|     ||     |[| |]     ",
    r"     [\_/]|_____||_____|[\_/]     ",
    r"       (_____)  (_____)       ",
]
_SHRUG = [  # the claws up beside the head, the pockets left hanging out
    r"  (\/)                  (\/)  ",
    r"   \ \     E      E     / /   ",
    r"    \ \    |      |    / /    ",
    r"     \ \.-''''''''''-./ /     ",
    r"      \_/            \_/      ",
    r"        |     MM     |        ",
    r"        |============|        ",
    r"     [.-.]|     ||     |[.-.]     ",
    r"     [| |]|     ||     |[| |]     ",
    r"     [\_/]|_____||_____|[\_/]     ",
    r"       (_____)  (_____)       ",
]
ROWS, COLS = 16, 44  # the scene: the crab at rows 4–14, room above for the moth
CRAB_AT = (4, 7)
FS = 46  # the scene's font size
POS = (600, 205)  # the scene's top left (the chapter title's lower third stays clear)


def pose(art: list[str], eyes: str = "o", mouth: str = "__") -> list[list[tuple[str, str]]]:
    """A pose as rows of (char, colour)."""
    out = []
    for line in art:
        line = line.replace("E", eyes).replace("MM", mouth)
        row, colour = [], ORANGE
        for ch in line:
            if ch == "[":
                colour = LINING
            elif ch == "]":
                colour = ORANGE
            else:
                row.append((ch, colour))
        out.append(row)
    return out


def blank() -> list[list[tuple[str, str]]]:
    return [[(" ", ORANGE) for _ in range(COLS)] for _ in range(ROWS)]


def stamp(grid, rows, at):
    r0, c0 = at
    for r, row in enumerate(rows):
        for c, (ch, colour) in enumerate(row):
            if ch != " " and 0 <= r0 + r < ROWS and 0 <= c0 + c < COLS:
                grid[r0 + r][c0 + c] = (ch, colour)


def put(grid, r, c, text, colour, behind=False):
    """Text into the grid at (row, column); `behind`: only into empty cells."""
    for k, ch in enumerate(text):
        rr, cc = round(r), round(c) + k
        if 0 <= rr < ROWS and 0 <= cc < COLS and not (behind and grid[rr][cc][0] != " "):
            grid[rr][cc] = (ch, colour)


def ass_layers(grid, alpha: dict | None = None) -> list[tuple[str, str]]:
    """The grid as one ASS text per colour, (colour tags, text): the other
    colours' characters are hard spaces, so the monospace layers line up
    (no colour tag inside a line, where a backslash before it would escape
    its brace)."""
    out = []
    for colour in sorted({c for row in grid for ch, c in row if ch != " "}):
        lines = []
        for row in grid:
            lines.append("".join(
                "\\h" if ch == " " or c != colour else ch.replace("{", "(").replace("}", ")")
                for ch, c in row))
        a = (alpha or {}).get(colour, 0)
        out.append((f"\\c{col(colour)}\\alpha&H{a:02X}&", "\\N".join(lines)))
    return out


def scene(t: float, seed: int = 20) -> tuple[list, dict]:
    """The crab scene at time t (s): the grid and the alpha per colour."""
    g = blank()
    blink = int(t * 10) % 37 in (0, 1)
    # 0–5.5 s idle, then looking at the counter running down; 5.5–8 reaching
    # into the pockets; 8–10.5 pockets out; 10.5–16 the shrug while the moth
    # flies off; then asleep.
    if t < 5.5:
        stamp(g, pose(_UP, "-" if blink else ("o" if t < 2.0 else "°"), "__"), CRAB_AT)
    elif t < 8.0:
        k = int((t - 5.5) / 0.4) % 2  # rummaging
        stamp(g, pose(_DOWN, "o", "~~" if k else "__"), (CRAB_AT[0], CRAB_AT[1] + k))
    elif t < 10.5:
        stamp(g, pose(_OUT, "O", "o "), CRAB_AT)
    elif t < 16.0:
        stamp(g, pose(_SHRUG, "-" if blink else "o", "~~" if t < 13 else "__"), CRAB_AT)
    else:
        stamp(g, pose(_SHRUG, "-", "__"), CRAB_AT)
        for k, (d, txt) in enumerate(((0.0, "z"), (0.9, "z"), (1.8, "Z"))):
            age = (t - 16.0 - d) % 2.7
            if t - 16.0 >= d and age < 2.2:
                put(g, CRAB_AT[0] + 1 - age * 1.2, CRAB_AT[1] + 24 + k * 2 + age, txt, DIM)
    alpha = {}
    # The moth: out of the left pocket at 9.0 s, fluttering up and away.
    if 9.0 <= t < 16.5:
        a = t - 9.0
        wings = ("\\o/", "-o-", "/o\\", "-o-")[int(t * 8) % 4]
        r = CRAB_AT[0] + 7 - a * 1.6 + 0.5 * (int(t * 4) % 2)
        c = CRAB_AT[1] + 4 + a * 3.0 + 1.5 * math.sin(a * 2.3)
        put(g, r, c, wings, MOTH)
    # Dust: specks puffing out of both pockets when they turn (8.0 s), sinking and fading.
    if 8.0 <= t < 14.0:
        rng = random.Random(seed)
        a = t - 8.0
        for i in range(16):
            side = -1 if i % 2 == 0 else 1
            vx = side * rng.uniform(0.8, 3.0)
            vy = -rng.uniform(0.8, 2.4)
            ch = rng.choice("·.˙'`,*")
            r = CRAB_AT[0] + 8 + vy * a + 0.5 * a * a
            c = CRAB_AT[1] + (6 if side < 0 else 23) + vx * a
            if r < CRAB_AT[0] + 11:
                put(g, r, c, ch, DUST, behind=True)
        alpha[DUST] = min(255, int(a / 6.0 * 255))
    return g, alpha


def counter_value(t: float, start: int) -> int:
    """The tokens left: the day before's total running down to 0 (2–5 s)."""
    if t < 2.0:
        return start
    if t >= 5.0:
        return 0
    return round(start * (1 - (t - 2.0) / 3.0) ** 3)


def _header() -> str:
    """The day videos' ASS header plus a plain style (no box, no outline)."""
    plain = (f"Style: Plain,Fira Mono,40,{col('FFFFFF')},{col('FFFFFF', 255)},{col('000000')},"
             f"{col('000000', 255)},0,0,0,0,100,100,0,0,1,0,0,7,0,0,0,1")
    head = ass_header()
    return head.replace("\n\n[Events]", f"\n{plain}\n\n[Events]")


def render_crab(day: str, start_tokens: int) -> list[Path]:
    """The animation and three stills into the day folder; returns the paths."""
    dest = C.HIST / day
    dest.mkdir(parents=True, exist_ok=True)
    work = C.WORK / day / "crab"
    work.mkdir(parents=True, exist_ok=True)
    sub = Subs()
    n = round(SECONDS / TICK)
    for i in range(n):  # the scene, ten ASCII frames a second
        t = i * TICK
        g, alpha = scene(t)
        for tags, text in ass_layers(g, alpha):
            sub.add(t, t + TICK, "Plain", f"{{\\an7\\pos{POS}\\fs{FS}{tags}}}" + text, layer=2)
    # The terminal: the last answer of the evening before, typed.
    sub.add(0.2, SECONDS, "Plain", f"{{\\pos(90,64)\\fs34\\c{col(GREY)}}}> keep building Open Cycling World")
    sub.typed(0.9, SECONDS, "Plain", "  └  " + LIMIT, pre=f"{{\\pos(90,112)\\fs34\\c{col(ORANGE)}}}", cps=36)
    # The counter, top right.
    sub.add(0.4, SECONDS, "Plain", f"{{\\an9\\pos(1840,64)\\fs30\\fsp4\\c{col(GREY)}}}TOKENS LEFT")
    for i in range(n):
        t = i * TICK
        v = counter_value(t, start_tokens)
        sub.add(max(0.4, t), t + TICK, "Plain",
                f"{{\\an9\\pos(1840,104)\\fnLato Black\\fs104\\c{col(ORANGE if v else RED)}}}{num_fmt(v)}")
    # The caption: the day, the limit, the reset.
    sub.typed(11.0, SECONDS, "Plain", CAPTION,
              pre=f"{{\\an2\\pos(960,1050)\\fs40\\c{col(LINING)}}}", cps=30)
    ass = work / "crab.ass"
    ass.write_text(_header() + "\n" + "\n".join(sub.lines) + "\n")
    out = dest / f"{NAME}.mp4"
    ffmpeg("-f", "lavfi", "-i", f"color=c=0x{BG}:s={W}x{H}:r={FPS}", "-f", "lavfi", "-i",
           "anullsrc=r=48000:cl=stereo", "-filter_complex",
           f"[0:v]vignette=PI/5,ass={ass}:fontsdir={FONTS},format=yuv420p[v]",
           "-map", "[v]", "-map", "1:a", "-t", f"{SECONDS}", "-c:v", "libx264", "-preset", "medium",
           "-crf", "18", "-pix_fmt", "yuv420p", "-r", str(FPS), "-c:a", "aac", "-b:a", "128k",
           *now_meta(), "-metadata", f"title=OCW Build Diary – {day}: no tokens left",
           "-movflags", "+faststart", out)
    made = [out]
    # The terminal alone (no crab), the counter at 0: the title's background.
    bare = work / "terminal.ass"
    bare.write_text(_header() + "\n" + "\n".join(x for x in sub.lines if not x.startswith("Dialogue: 2,")) + "\n")
    still = dest / f"{NAME}-0-terminal.jpg"
    ffmpeg("-f", "lavfi", "-i", f"color=c=0x{BG}:s={W}x{H}:r={FPS}", "-filter_complex",
           f"[0:v]vignette=PI/5,ass={bare}:fontsdir={FONTS},trim=start=8,setpts=PTS-STARTPTS[v]",
           "-map", "[v]", "-frames:v", "1", "-q:v", "2", still)
    made.append(still)
    for k, (at, label) in enumerate(((4.0, "limit"), (9.6, "pockets"), (12.6, "moth")), 1):
        still = dest / f"{NAME}-{k}-{label}.jpg"
        ffmpeg("-ss", f"{at:.2f}", "-i", out, "-frames:v", "1", "-q:v", "2", still)
        made.append(still)
    for p in made:
        log(p)
    return made
