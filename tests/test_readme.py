"""Unit tests of the generated README (ocwart/readme.py, ART-PROJECT §5.3):
the day sections from fake day scripts, journals and a fake built gallery,
release links, the evolution strip, the spec range, the mask guard. All in a
temporary directory; no network, no ffmpeg.

    /usr/bin/python3 -m unittest discover -s tests -p 'test_*.py'   (make test)
"""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path
from unittest import mock

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))

from ocwart import gallery, readme  # noqa: E402
from test_diary import Fixture  # noqa: E402

D1, D2 = "2026-10-01", "2026-10-02"
PAGES = gallery.PAGES_URL
DL = gallery.DOWNLOAD


class SpecRangeTest(unittest.TestCase):
    def test_features_first_then_trimmed_subjects(self):
        self.assertEqual(readme.spec_range({"features": [{"version": "3.36"}, {"version": "3.4"},
                                                         {"version": "3.10"}]}), "spec 3.4 → 3.36")
        self.assertEqual(readme.spec_range({"spec_versions": ["2.30", "2.31", "2.64", "4.7"]}), "spec 2.30 → 2.64")
        self.assertEqual(readme.spec_range({"spec_versions": ["2.6", "2.65", "2.66"]}), "spec 2.65 → 2.66")
        self.assertEqual(readme.spec_range({"spec_versions": ["1.0"]}), "spec 1.0")
        self.assertEqual(readme.spec_range({}), "")


class ReadmeTest(Fixture):
    def setUp(self):
        super().setUp()
        self.days = self.tmp / "days"
        self.days.mkdir()
        self.site = self.tmp / "site"
        (self.tmp / "docs").mkdir()
        self.template = self.tmp / "docs" / "README.template.md"
        self.template.write_text("# Title\n\n{{hero}}\n\n{{totals}}\n\n## Evolution\n\n{{evolution}}\n\n## Days\n\n"
                                 "{{days}}\n\nFooter: © OpenStreetMap contributors\n")
        self.evolution = self.tmp / "docs" / "evolution.toml"
        self.evolution.write_text(f'[[pic]]\nday = "{D1}"\nfile = "090000-first.png"\ncaption = "The first road"\n'
                                  f'[[pic]]\nday = "{D2}"\nfile = "999999-missing.png"\ncaption = "Not built"\n')
        self.readme = self.tmp / "README.md"
        self.patches = [mock.patch.object(readme, "DAYS", self.days),
                        mock.patch.object(readme, "TEMPLATE", self.template),
                        mock.patch.object(readme, "EVOLUTION", self.evolution),
                        mock.patch.object(readme, "README", self.readme)]
        for p in self.patches:
            p.start()
        self.day(D1, number=1, files=["090000-first.png", "100000-clip.mp4", "110000-second.jpg", "120000-third.png",
                                      "130000-fourth.png", "140000-fifth.png"], web=["120000-third.png"],
                 journal={"commits": [{}] * 12, "merges": 3, "spec_versions": ["1.1", "1.4"], "images": 5,
                          "videos": 1, "tokens": {"total": {"total": 2_500_000_000}}})
        (self.days / f"{D1}.toml").write_text(
            'title = "The first day"\ntagline = "In which a road appears."\nhero = "120000-third.png"\n'
            '[[chapter]]\ntitle = "A"\nshots = [{ file = "100000-clip.mp4" }, { file = "090000-first.png" }]\n'
            '[[chapter]]\ntitle = "B"\nshots = [{ split = ["110000-second.jpg", "140000-fifth.png"] }]\n')
        self.day(D2, number=2, files=["080000-today.png"], web=[],
                 journal={"commits": [{}] * 4, "merges": 1, "features": [{"version": "1.5"}], "images": 1,
                          "videos": 0, "tokens": {"total": {"total": 40_000_000}}})

    def tearDown(self):
        for p in self.patches:
            p.stop()
        super().tearDown()

    def day(self, day, number, files, web, journal):
        (self.hist / day).mkdir(parents=True)
        (self.hist / day / "journal.json").write_text(json.dumps({"number": number, **journal}))
        d = self.site / "days" / day
        (d / "t").mkdir(parents=True)
        (d / "w").mkdir()
        for f in files:
            (d / "t" / (f + ".jpg")).write_bytes(b"jpg")
        for f in web:
            (d / "w" / (f + ".jpg")).write_bytes(b"jpg")
        items = json.dumps({"items": [{"f": f} for f in files]})
        (d / "index.html").write_text(f'<script id="items" type="application/json">{items}</script>')

    def build(self, sizes):
        return readme.build(sizes=sizes, site=readme.Site(self.site))

    def test_days_evolution_hero_and_links(self):
        sizes = {f"ocw-build-history-{D1}.zip": 1_300_000_000, f"ocw-diary-day-01-{D1}.mp4": 33_000_000,
                 "ocw-build-diary.mp4": 280_000_000}
        text = self.build(sizes)
        self.assertEqual(self.readme.read_text(), text)
        self.assertNotIn("{{", text)
        # newest day first
        self.assertLess(text.index(f"— (the day's story"), text.index("Day 1 · 2026-10-01 — The first day"))
        self.assertIn("*In which a road appears.*", text)
        # the day video: a poster (the hero's thumbnail) linking to the release asset
        self.assertIn(f'<a href="{DL}ocw-diary-day-01-{D1}.mp4"><img src="{PAGES}days/{D1}/t/120000-third.png.jpg"',
                      text)
        self.assertIn(f"[⇩ Day zip]({DL}ocw-build-history-{D1}.zip) (1.3 GB)", text)
        # thumbnails: hero + one still per chapter (no video), linking into the gallery's lightbox
        self.assertIn(f'href="{PAGES}days/{D1}/#1"><img src="{PAGES}days/{D1}/t/090000-first.png.jpg"', text)
        self.assertIn(f"{PAGES}days/{D1}/t/140000-fifth.png.jpg", text)  # the split's after picture
        self.assertNotIn("100000-clip.mp4.jpg", text.split("## Days")[1].split("### Day 1")[1].split("[Gallery]")[0])
        self.assertIn("**12** commits · **3** merges · spec 1.1 → 1.4 · **5** pictures · **1** videos · "
                      "**2.50 billion** tokens · music: synthwave", text)
        # day 2: not published yet
        self.assertIn("day zip and video: at the end of the day", text)
        self.assertIn("spec 1.5", text)
        self.assertIn("music: funk", text)
        # evolution: the built picture with its caption; the missing one left out
        self.assertIn("<sub>The first road</sub>", text)
        self.assertNotIn("Not built", text)
        # hero: the newest day with a web copy of its hero, linking to the diary video
        self.assertIn(f'<a href="{DL}ocw-build-diary.mp4"><img src="{PAGES}days/{D1}/w/120000-third.png.jpg" '
                      f'width="860"', text)
        self.assertIn("**2 build days** · **16** commits · **6** pictures · **1** videos", text)
        self.assertIn("OpenStreetMap contributors", text)

    def test_without_release_assets_no_dead_links(self):
        text = self.build({})
        self.assertNotIn(DL, text.split("## Days")[1])
        self.assertNotIn("Day video", text)

    def test_mask(self):
        (self.days / f"{D2}.toml").write_text('title = "Ran on buildhost.example.lan"\n')
        text = self.build({})
        self.assertIn("Ran on marge", text)
        self.assert_clean(text)
        self.template.write_text(self.template.read_text() + "\nmail dev@mail.example.org\n")
        with self.assertRaises(SystemExit) as e:
            self.build({})
        self.assertIn("e-mail address", str(e.exception))
        self.assertNotIn("dev@mail", str(e.exception))


class TemplateTest(unittest.TestCase):
    def test_the_real_template_and_evolution(self):
        t = readme.TEMPLATE.read_text()
        for k in ("{{hero}}", "{{totals}}", "{{evolution}}", "{{days}}"):
            self.assertIn(k, t)
        self.assertIn("OpenStreetMap contributors", t)
        import tomllib
        pics = tomllib.loads(readme.EVOLUTION.read_text())["pic"]
        self.assertGreaterEqual(len(pics), 6)
        for p in pics:
            self.assertTrue(p["caption"] and p["file"] and p["day"])


if __name__ == "__main__":
    unittest.main()
