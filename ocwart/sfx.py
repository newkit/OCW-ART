"""Synthesised sound effects (ART-PROJECT §3.2): bell, whooshes, pops, ticks, ding."""

from __future__ import annotations

import math
import wave
from array import array
from pathlib import Path

from .core import RATE

# ------------------------------------------------------------------- audio


# The music (ART-PROJECT §3.2): a style per day, varied within the video;
def sfx_whoosh(rng):
    n = round(0.7 * RATE)
    out, lp = [], 0.0
    for i in range(n):
        t = i / n
        a = 0.02 + 0.5 * math.sin(math.pi * t) ** 2
        lp += a * (rng.uniform(-1, 1) - lp)
        out.append(lp * math.sin(math.pi * t) * 0.9)
    return out


def sfx_bell():
    """A bicycle bell: two strikes of an inharmonic, decaying ring."""
    n = round(1.6 * RATE)
    parts = [(2300, 1.0, 1.4), (2300 * 2.76, 0.4, 0.7), (2300 * 5.4, 0.2, 0.35), (2310, 0.6, 1.4)]
    one = [sum(a * math.sin(2 * math.pi * f * i / RATE) * math.exp(-i / (d * RATE / 3))
               for f, a, d in parts) * 0.2 for i in range(n)]
    out = [0.0] * (n + round(0.18 * RATE))
    for start in (0, round(0.18 * RATE)):
        for i, v in enumerate(one):
            out[start + i] += v
    return out


def sfx_pop():
    n = round(0.12 * RATE)
    return [math.sin(2 * math.pi * (900 - 500 * i / n) * i / RATE) * (1 - i / n) * 0.35
            for i in range(n)]


def sfx_tick():
    n = round(0.025 * RATE)
    return [math.sin(2 * math.pi * 1800 * i / RATE) * (1 - i / n) * 0.18 for i in range(n)]


def sfx_ding():
    n = round(1.2 * RATE)
    return [(math.sin(2 * math.pi * 1318.5 * i / RATE) + 0.5 * math.sin(2 * math.pi * 1975.5 * i / RATE))
            * math.exp(-i / (0.35 * RATE)) * 0.25 for i in range(n)]


def write_wav(path: Path, data):
    peak = max(1e-9, max(abs(x) for x in data))
    g = min(1.0, 0.89 / peak)
    pcm = array("h", (int(max(-1, min(1, x * g)) * 32767) for x in data))
    with wave.open(str(path), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(RATE)
        w.writeframes(pcm.tobytes())
