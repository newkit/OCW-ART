"""Unit tests of the Build Diary's music (music.py, ART-PROJECT §3.2):
determinism, a different style per day, variation within a video, no
clipping and a sane loudness. Nobody can listen here, so the tests (and
`music.stats`) look at the waveform.

    /usr/bin/python3 -m unittest discover -s tests -p 'test_*.py'   (make test)
"""

from __future__ import annotations

import subprocess
import sys
import unittest
import zlib
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
sys.path.insert(0, str(REPO))

from ocwart import music as M  # noqa: E402


def timeline(chapters=6, chapter_s=7.0):
    """Segments like a day video: title, time-lapse, chapters, end card."""
    segs, t = [(0.0, "intro"), (6.0, "drive")], 20.0
    for _ in range(chapters):
        segs.append((t, "groove"))
        t += chapter_s
    segs.append((t, "outro"))
    return segs, t + 9.0


def crc(samples) -> int:
    return zlib.crc32(bytes(memoryview(samples).cast("B")))


SEGS, SECONDS = timeline()
_cache = {}


def render(day, bpm=116, key="C", **kw):
    k = (day, bpm, key, tuple(sorted(kw.items())))
    if k not in _cache:
        _cache[k] = M.Music(bpm, key, seed=day, **kw).render(SECONDS, SEGS)
    return _cache[k]


class DeterminismTest(unittest.TestCase):
    def test_same_seed_same_samples(self):
        a = M.Music(120, "G", seed=4).render(SECONDS, SEGS)
        b = M.Music(120, "G", seed=4).render(SECONDS, SEGS)
        self.assertEqual(crc(a), crc(b))

    def test_same_samples_in_another_process(self):
        """No hash() randomisation (PYTHONHASHSEED) in the music."""
        code = ("import sys, zlib; sys.path.insert(0, %r); from ocwart import music as M; "
                "a = M.Music(120, 'G', seed=4).render(30, [(0, 'intro'), (5, 'drive'), (15, 'groove'), "
                "(24, 'outro')]); print(zlib.crc32(bytes(memoryview(a).cast('B'))))" % str(REPO))
        outs = {subprocess.run([sys.executable, "-c", code], capture_output=True, text=True, check=True,
                               env={"PYTHONHASHSEED": str(h)}).stdout.strip() for h in (1, 2)}
        self.assertEqual(len(outs), 1)
        a = M.Music(120, "G", seed=4).render(30, [(0, "intro"), (5, "drive"), (15, "groove"), (24, "outro")])
        self.assertEqual(outs.pop(), str(crc(a)))

    def test_other_seed_other_music(self):
        self.assertNotEqual(crc(render(4)), crc(render(9)))  # 9 is chiptune too, other material


class StyleTest(unittest.TestCase):
    def test_days_1_to_4_get_different_styles(self):
        styles = [M.style_for(d) for d in (1, 2, 3, 4)]
        self.assertEqual(len(set(styles)), 4, styles)
        self.assertEqual(M.style_for(4), "chiptune")  # the band days 1–4 had, now varied
        self.assertEqual(M.style_for(6), M.style_for(1))

    def test_days_sound_different(self):
        """Brightness, zero-crossing rate and onset rate tell the days apart."""
        feats = {}
        for d in (1, 2, 3, 4):
            s = M.stats(render(d))
            feats[d] = (s["brightness"], s["zcr"] / 5000, s["onsets_per_s"] / 4)
        for a in feats:
            for b in feats:
                if a < b:
                    dist = sum((x - y) ** 2 for x, y in zip(feats[a], feats[b])) ** 0.5
                    self.assertGreater(dist, 0.05, (a, b, feats[a], feats[b]))

    def test_script_overrides_style_and_mode(self):
        m = M.Music(110, "D", seed=1, style="house", mode="dorian")
        self.assertEqual(m.describe(), "house in D dorian, 110 bpm")
        self.assertEqual(m.scale, M.MODES["dorian"])
        with self.assertRaises(SystemExit):
            M.Music(110, "D", seed=1, style="polka")
        with self.assertRaises(SystemExit):
            M.Music(110, "D", seed=1, mode="locrian-ish")

    def test_every_style_renders(self):
        for name in M.STYLES:
            a = M.Music(118, "F", seed=3, style=name).render(16, [(0, "intro"), (4, "drive"), (9, "groove"),
                                                                  (13, "outro")])
            st = M.stats(a)
            self.assertLess(st["peak_db"], -1.0, name)
            self.assertGreater(st["rms_db"], -30, name)


class LevelTest(unittest.TestCase):
    def test_no_clipping_and_sane_loudness(self):
        for d in (1, 2, 3, 4, 5):
            s = M.stats(render(d))
            self.assertLess(s["peak_db"], -1.0, (d, s))  # headroom for the effects
            self.assertGreater(s["rms_db"], -26.0, (d, s))
            self.assertLess(s["rms_db"], -14.0, (d, s))

    def test_no_silent_holes_in_the_middle(self):
        a = render(2)
        w = M.RATE // 2
        quiet = [i for i in range(M.RATE * 2, len(a) - M.RATE * 2, w)
                 if max(abs(x) for x in a[i:i + w]) < 0.01]
        self.assertEqual(quiet, [])


class VariationTest(unittest.TestCase):
    def plan(self, day=4, seconds=None, segs=None):
        m = M.Music(120, "G", seed=day)
        return m, m.plan(seconds or SECONDS, segs or SEGS)

    def test_patterns_progressions_fills_and_lead_vary(self):
        for day in (1, 2, 3, 4, 5):
            m, specs = self.plan(day)
            grooves = [s for s in specs if s[-1] == "groove"]
            self.assertGreaterEqual(len({s[1] for s in grooves}), 2, day)  # drum patterns
            self.assertGreaterEqual(len({s[0] for s in grooves}), 3, day)  # chords
            self.assertGreaterEqual(len({s[8] for s in grooves}), 2, day)  # arp / stab patterns
            self.assertTrue(any(s[2] for s in specs), day)  # fills, build-ups or stops
            self.assertTrue(any(s[3] for s in specs), day)  # crashes on new sections
            leads = {s[11] for s in grooves if s[11]}
            self.assertGreaterEqual(len(leads), 4, day)  # the melody develops
            self.assertTrue(any(s[1] is None for s in specs if s[-1] == "intro"), day)  # no drums in the intro

    def test_call_and_response(self):
        m = M.Music(120, "G", seed=4)
        import random
        call = m.motif(random.Random(1))
        ans = m.answer(call)
        self.assertEqual([n for n in ans if n[0] < 16], [n for n in call if n[0] < 16])
        self.assertEqual(ans[-1][2], 0)  # the answer ends on the root
        self.assertEqual(ans[-1][0] + ans[-1][1], 32)  # held to the end
        for op in ("seq", "inv", "rhythm", "orn", "thin"):
            v = m.vary(call, op, random.Random(2))
            self.assertTrue(v)
            self.assertTrue(all(0 <= s < 32 for s, _, _ in v))

    def test_key_lift_and_bridge_in_long_videos(self):
        segs, seconds = timeline(chapters=9, chapter_s=9.0)
        self.assertGreater(seconds, 90)
        m, specs = self.plan(4, seconds, segs)
        shifts = [s[-2] for s in specs if s[-1] == "groove"]
        self.assertEqual(shifts[0], 0)
        self.assertIn(shifts[-1], m.st["lift"])  # the last third lifts the key
        self.assertEqual(sorted(set(shifts)), [0, shifts[-1]])
        self.assertIn(shifts[-1], {s[-2] for s in specs if s[-1] == "outro"})
        bridge = m.chord(m.st["bridge"][0], 0)
        first_lifted = shifts.index(shifts[-1])
        self.assertIn(bridge, {s[0] for s in [s for s in specs if s[-1] == "groove"][:first_lifted]})
        short_segs, short_s = timeline(chapters=3)
        _, specs = self.plan(4, short_s, short_segs)
        self.assertEqual({s[-2] for s in specs}, {0})  # short videos keep their key

    def test_stop_bar_breaks_off(self):
        m = M.Music(120, "G", seed=4)
        chord = m.chord(0, 0)
        base = (chord, "four", None, False, False, 16, "oct8", 1.0, "up", 1.0, 0, (), 1.0, 0.04, 1.0, 0, "groove")
        stop = (chord, "four", "stop", False, True, 8, "oct8", 1.0, "up", 1.0, 0, (), 1.0, 0.04, 1.0, 0, "groove")
        half, n = m.bar_n // 2, m.bar_n

        def energy(x, a, b):
            return sum(v * v for v in x[a:b]) / (b - a)
        a, b = m.bar(base), m.bar(stop)
        self.assertLess(energy(b, half + 800, n - m.bar_n // 8), 0.5 * energy(a, half + 800, n - m.bar_n // 8))


if __name__ == "__main__":
    unittest.main()


class DarkchipTest(unittest.TestCase):
    """Day 6's redo (user 2026-11-17: "less squeeky and less happy … different drums styles")."""
    SEGS = [(0, "intro"), (6, "drive"), (20, "groove"), (28, "groove"), (36, "groove"), (44, "groove"),
            (52, "groove"), (60, "outro")]

    def test_darker_than_chiptune(self):
        dark = M.stats(M.Music(140, "D", seed=6, style="darkchip").render(68, self.SEGS))
        chip = M.stats(M.Music(140, "D", seed=6, style="chiptune", mode="minor").render(68, self.SEGS))
        self.assertLess(dark["brightness"], chip["brightness"] * 0.7, (dark, chip))
        self.assertLess(dark["zcr"], chip["zcr"], (dark, chip))

    def test_a_drum_style_per_chapter_in_turn(self):
        m = M.Music(140, "D", seed=6, style="darkchip")
        specs = m.plan(68, self.SEGS)
        grooves = [s[1] for s in specs if s[-1] == "groove" and s[1]]
        self.assertGreaterEqual(len(set(grooves) & set(M.STYLES["darkchip"]["grooves"])), 3, grooves)


def beat_bpm(samples, lo=90, hi=150, rate=M.RATE) -> float:
    """The tempo of the low end: the 10 ms envelope of the low-passed track,
    its autocorrelation's strongest lag between `lo` and `hi` bpm."""
    low = M._lowpass(M._lowpass(samples, 0.02), 0.02)
    w = rate // 100
    env = [sum(abs(x) for x in low[i:i + w]) for i in range(0, len(low) - w, w)]
    d = [max(0.0, env[i] - env[i - 1]) for i in range(1, len(env))]  # onsets
    best, lag_best = -1.0, 0
    for lag in range(round(6000 / hi), round(6000 / lo) + 1):
        c = sum(d[i] * d[i - lag] for i in range(lag, len(d)))
        if c > best:
            best, lag_best = c, lag
    return 6000 / lag_best


class MelodicDeepHouseTest(unittest.TestCase):
    """Day 7 (user 2026-11-18: "use music style: melodic deep house")."""
    SEGS = [(0, "intro"), (6, "drive"), (20, "groove"), (28, "groove"), (36, "groove"), (44, "groove"),
            (52, "groove"), (60, "outro")]

    def test_minor_ninth_chords(self):
        m = M.Music(122, "F", seed=7, style="melodic-deep-house")
        self.assertEqual(m.mode_name, "minor")
        root = m.chord(0, 0)
        self.assertEqual([s - root[0] for s in root], [0, 3, 7, 10, 14])  # Fm9

    def test_four_on_the_floor_with_off_beat_hats_and_claps_on_2_and_4(self):
        for g in M.STYLES["melodic-deep-house"]["grooves"][:3]:
            pat = M.DRUMS[g]
            self.assertEqual(pat["k"], "x...x...x...x...", g)
            self.assertEqual(pat["o"], "..x...x...x...x.", g)
            back = pat.get("s") or pat.get("m")
            self.assertTrue(back[4] != "." and back[12] != ".", g)

    def test_warm_tempo_and_loudness(self):
        segs = [(0, "groove"), (16, "groove")]
        deep = M.Music(122, "F", seed=7, style="melodic-deep-house").render(32, segs)
        house = M.Music(122, "F", seed=7, style="house").render(32, segs)
        sd, sh = M.stats(deep), M.stats(house)
        self.assertLess(sd["brightness"], sh["brightness"] * 0.8, (sd, sh))  # warmer, rounder
        self.assertLess(sd["peak_db"], -2.4)
        self.assertAlmostEqual(sd["rms_db"], -19, delta=1.5)
        self.assertAlmostEqual(beat_bpm(deep), 122, delta=3)

    def test_the_filter_opens_over_a_phrase(self):
        m = M.Music(122, "F", seed=7, style="melodic-deep-house")
        alphas = [s[13] for s in m.plan(68, self.SEGS) if s[-1] == "groove"]
        self.assertGreater(len(set(alphas)), 2, alphas)


class LiquidDnbTest(unittest.TestCase):
    """Day 8 (2026-11-18): liquid drum & bass, a style unlike days 6 and 7."""
    SEGS = [(0, "intro"), (6, "drive"), (20, "groove"), (28, "groove"), (36, "groove"), (44, "groove"),
            (52, "groove"), (60, "outro")]

    def test_dorian_ninth_chords(self):
        m = M.Music(172, "G", seed=8, style="liquid-dnb")
        self.assertEqual(m.mode_name, "dorian")
        root = m.chord(0, 0)
        self.assertEqual([s - root[0] for s in root], [0, 3, 7, 10, 14])  # Gm9
        four = m.chord(3, 0)
        self.assertEqual([s - four[0] for s in four], [0, 4, 7, 10, 14])  # C9: dorian's major IV

    def test_two_step_with_the_snare_on_2_and_4(self):
        for g in M.STYLES["liquid-dnb"]["grooves"][:3]:
            pat = M.DRUMS[g]
            self.assertEqual(pat["k"][0], "x", g)
            self.assertEqual(pat["k"][10], "x", g)
            self.assertEqual(pat["k"][4] + pat["k"][12], "..", g)  # no four on the floor
            self.assertEqual(pat["s"][4] + pat["s"][12], "XX", g)

    def test_a_drum_style_per_chapter(self):
        m = M.Music(172, "G", seed=8, style="liquid-dnb")
        grooves = [s[1] for s in m.plan(68, self.SEGS) if s[-1] == "groove" and s[1]]
        self.assertGreaterEqual(len(set(grooves) & set(M.STYLES["liquid-dnb"]["grooves"])), 3, grooves)

    def test_fast_and_loud_enough(self):
        segs = [(0, "groove"), (16, "groove")]
        dnb = M.Music(172, "G", seed=8, style="liquid-dnb").render(32, segs)
        deep = M.Music(122, "G", seed=8, style="melodic-deep-house").render(32, segs)
        sd, sh = M.stats(dnb), M.stats(deep)
        self.assertGreater(sd["onsets_per_s"], sh["onsets_per_s"], (sd, sh))  # busier drums
        self.assertLess(sd["peak_db"], -2.4)
        self.assertAlmostEqual(sd["rms_db"], -19, delta=1.5)
