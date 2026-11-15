"""The ASS subtitle layer of the videos (titles, captions, counters, bubbles)."""

from __future__ import annotations

import re
from pathlib import Path

from .core import GOLD, H, PINK, VIOLET, W

# --------------------------------------------------------------- subtitles


def col(hexrgb: str, alpha: int = 0) -> str:
    r, g, b = hexrgb[0:2], hexrgb[2:4], hexrgb[4:6]
    return f"&H{alpha:02X}{b}{g}{r}".upper()


def num_fmt(v: int) -> str:
    """12345 -> "12 345" (thin space groups)."""
    return f"{v:,}".replace(",", "\u2009")


def ts(t: float) -> str:
    t = max(0.0, t)
    h, rem = divmod(t, 3600)
    m, s = divmod(rem, 60)
    return f"{int(h)}:{int(m):02d}:{s:05.2f}"


def esc(text: str) -> str:
    return text.replace("\\", "\\\\").replace("{", "(").replace("}", ")").replace("\n", "\\N")


def prompt_lines(text: str, width: int = 52, lines: int = 3) -> str:
    """A prompt wrapped for a chat bubble (≤ `lines` lines, ellipsis)."""
    words, out, cur = " ".join(text.split()).split(" "), [], ""
    for w in words:
        if len(cur) + len(w) + 1 > width:
            out.append(cur)
            cur = w
            if len(out) == lines:
                break
        else:
            cur = (cur + " " + w).strip()
    else:
        out.append(cur)
    body = "\\N".join(esc(x) for x in out[:lines])
    return body + ("…" if len(out) >= lines and len(" ".join(out)) < len(" ".join(words)) else "")


def ass_header() -> str:
    def style(name, font, size, fg, bold=0, italic=0, border=1, outline=0.0, shadow=0.0,
              back="000000", back_a=255, outline_c="000000", align=7, spacing=0.0, ml=0, mr=0, mv=0):
        return (f"Style: {name},{font},{size},{col(fg)},{col(fg, 255)},{col(outline_c)},"
                f"{col(back, back_a)},{-1 if bold else 0},{-1 if italic else 0},0,0,100,100,"
                f"{spacing},0,{border},{outline},{shadow},{align},{ml},{mr},{mv},1")

    styles = [
        style("Kicker", "Fira Mono", 32, "FFFFFF", bold=1, spacing=6, border=3, outline=10,
              back=PINK, back_a=0, outline_c=PINK, align=5),
        style("Title", "Lato Black", 168, "FFFFFF", shadow=7, back=VIOLET, back_a=0, align=5),
        style("Date", "Fira Mono", 40, "FFFFFF", spacing=4, align=5),
        style("Tag", "Lato Medium", 54, "FFFFFF", italic=1, shadow=3, back="000000", back_a=96,
              align=5),
        style("ChTime", "Fira Mono", 40, "1A1A1A", bold=1, border=3, outline=10, back=GOLD,
              back_a=0, outline_c=GOLD, align=1),
        style("ChTitle", "Lato Black", 82, "FFFFFF", border=3, outline=16, back=VIOLET,
              back_a=40, outline_c=VIOLET, align=1),
        style("Caption", "Lato Semibold", 50, "FFFFFF", border=3, outline=14, back="101018",
              back_a=70, outline_c="101018", align=2, ml=140, mr=140),
        style("Note", "Lato Heavy", 46, "1A1A1A", border=3, outline=12, back="FFE45C",
              back_a=0, outline_c="FFE45C", align=9),
        style("Badge", "Fira Mono", 38, "FFFFFF", bold=1, border=3, outline=10, back=PINK,
              back_a=0, outline_c=PINK, align=3),
        style("Ticker", "Fira Mono", 26, "C8FFD8", border=3, outline=12, back="0B0B12",
              back_a=60, outline_c="0B0B12", align=3),
        style("TickerHi", "Fira Mono", 26, "FFFFFF", bold=1, border=3, outline=12, back=PINK,
              back_a=0, outline_c=PINK, align=3),
        style("Clock", "Fira Mono", 110, "FFFFFF", bold=1, shadow=5, back="000000", back_a=60,
              align=7),
        style("Counter", "Fira Mono", 36, "FFFFFF", border=3, outline=10, back="0B0B12",
              back_a=60, outline_c="0B0B12", align=7),
        style("StatNum", "Lato Black", 124, PINK, shadow=4, back="000000", back_a=80, align=5),
        style("StatLabel", "Fira Mono", 30, "FFFFFF", spacing=3, align=5),
        style("Outro", "Lato Heavy", 64, "FFFFFF", shadow=4, back="000000", back_a=80, align=5),
        style("Teaser", "Fira Mono", 38, "FFE45C", spacing=2, align=5),
        style("Prompt", "Lato Semibold", 38, "1A1A2E", border=3, outline=16, back="FFFFFF",
              back_a=10, outline_c="FFFFFF", align=7),
        style("PromptWho", "Fira Mono", 28, "FFFFFF", bold=1, border=3, outline=8, back=PINK,
              back_a=0, outline_c=PINK, align=7),
    ]
    return "\n".join([
        "[Script Info]", "ScriptType: v4.00+", f"PlayResX: {W}", f"PlayResY: {H}",
        "WrapStyle: 0", "ScaledBorderAndShadow: yes", "",
        "[V4+ Styles]",
        "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, "
        "BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, "
        "BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding",
        *styles, "",
        "[Events]",
        "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text",
    ])


class Subs:
    def __init__(self):
        self.lines = []

    def add(self, start, end, style, text, layer=1):
        if end > start:
            self.lines.append(f"Dialogue: {layer},{ts(start)},{ts(end)},{style},,0,0,0,,{text}")

    def typed(self, start, end, style, text, pre="", cps=40):
        """Typewriter: the text appears a few characters at a time; the rest
        is already laid out but fully transparent (so nothing jumps)."""
        chars = list(text)
        # Keep escapes (\\N, \\h) as single units.
        units, k = [], 0
        while k < len(chars):
            if chars[k] == "\\" and k + 1 < len(chars):
                units.append(chars[k] + chars[k + 1])
                k += 2
            else:
                units.append(chars[k])
                k += 1
        step = 2
        dt_ = step / cps
        t = start
        for n in range(step, len(units) + step, step):
            shown, rest = "".join(units[:n]), "".join(units[n:])
            t_end = end if n >= len(units) else min(end, t + dt_)
            body = shown + (f"{{\\alpha&HFF&}}{rest}" if rest else "")
            # Fades only on the last step (it holds until `end`).
            p = pre if t_end >= end else re.sub(r"\\fad\([^)]*\)", "", pre)
            self.add(t, t_end, style, p + body)
            t = t_end
            if t >= end:
                break

    def write(self, path: Path):
        path.write_text(ass_header() + "\n" + "\n".join(self.lines) + "\n")
