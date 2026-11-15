"""Unit tests of the gallery (ocwart/gallery.py, ART-PROJECT §6): captions,
the tier plan under the size budget, the pages, incremental builds, the mask
guard and the release zips. A fixture archive in a temporary directory; the
encoder is a fake (no ffmpeg) except in FfmpegTest, which makes real
thumbnails from generated test patterns. No network.

    /usr/bin/python3 -m unittest discover -s tests -p 'test_*.py'   (make test)
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import time
import unittest
import zipfile
from pathlib import Path
from unittest import mock

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))

from ocwart import gallery  # noqa: E402
from test_diary import Fixture  # noqa: E402

DAY1, DAY2 = "2026-10-01", "2026-10-02"
SIZES = {"t": 1000, "w1280": 10_000, "w960": 4000}


class FakeEncoder:
    """Writes a file of a fixed size per variant instead of running ffmpeg."""

    def __init__(self):
        self.calls = []

    def __call__(self, item, variants, seconds=None):
        self.calls.append((item["day"], item["file"], tuple(variants)))
        for v in variants:
            p = gallery.out_path(item, v)
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_bytes(b"\xff\xd8" + b"x" * (SIZES[v] - 2))


class GalleryFixture(Fixture):
    def setUp(self):
        super().setUp()
        self.days = self.tmp / "days"
        self.days.mkdir()
        self.p_days = mock.patch.object(gallery, "DAYS", self.days)
        self.p_days.start()
        self.enc = FakeEncoder()

    def tearDown(self):
        self.p_days.stop()
        super().tearDown()

    def media(self, day, *names):
        d = self.hist / day
        d.mkdir(parents=True, exist_ok=True)
        for n in names:
            (d / n).write_bytes(b"media " + n.encode())
        return d

    def build(self, **kw):
        kw.setdefault("assets", None)
        return gallery.build(encoder=self.enc, **kw)

    def site(self, rel):
        return (gallery.site_dir() / rel).read_text()


class CaptionTest(unittest.TestCase):
    def test_caption_from_the_file_name(self):
        self.assertEqual(gallery.caption_of("000101-shot-wayland-a26-foot-down.jpg"), "shot wayland a26 foot down")
        self.assertEqual(gallery.caption_of("plain_name.png"), "plain name")

    def test_script_notes(self):
        sc = {"hero": "a.png", "chapter": [{"title": "Trees", "shots": [
            {"file": "b.png", "note": "a rider inside a tree"}, {"split": ["c.png", "d.png"]},
            {"card": True}, {"file": "../2026-10-01/e.png"}]}]}
        notes = gallery.script_notes(sc)
        self.assertEqual(notes["a.png"], "In the video: the title picture")
        self.assertEqual(notes["b.png"], "In the video: Trees – “a rider inside a tree”")
        self.assertEqual(notes["d.png"], "In the video: Trees")
        self.assertNotIn("../2026-10-01/e.png", notes)


class PlanTest(unittest.TestCase):
    SIZE = {"full": 100, "reduced": 40, "thumbs": 10}

    def plan(self, budget, days=("d1", "d2", "d3")):
        return gallery.plan_tiers(list(days), lambda d, t: self.SIZE[t], budget)

    def test_all_full_when_it_fits(self):
        self.assertEqual(set(self.plan(300).values()), {"full"})

    def test_oldest_days_step_down_first(self):
        self.assertEqual(self.plan(240), {"d1": "reduced", "d2": "full", "d3": "full"})
        self.assertEqual(self.plan(180), {"d1": "reduced", "d2": "reduced", "d3": "full"})
        # all reduced (120) still too big: thumbnails for the oldest first, the newest keeps the most
        self.assertEqual(self.plan(100), {"d1": "thumbs", "d2": "reduced", "d3": "reduced"})
        self.assertEqual(self.plan(65), {"d1": "thumbs", "d2": "thumbs", "d3": "reduced"})

    def test_fixed_bytes_count(self):
        self.assertEqual(gallery.plan_tiers(["d1"], lambda d, t: self.SIZE[t], 120, fixed=30), {"d1": "reduced"})

    def test_refuses_when_even_thumbnails_do_not_fit(self):
        with self.assertRaises(SystemExit) as e:
            self.plan(20)
        self.assertIn("--max-mb", str(e.exception))


class BuildTest(GalleryFixture):
    def test_pages_in_time_order_with_posters_and_links(self):
        self.media(DAY1, "120000-shot-hills.png", "090000-first-light.jpg", "100000-video-ride.mp4",
                   "110000-empty.jpg")
        (self.hist / DAY1 / "110000-empty.jpg").write_bytes(b"")  # an aborted capture: not shown
        (self.hist / DAY1 / "130000-verdict.txt").write_text("not media")
        self.media(DAY2, "080000-next-day.png")
        (self.days / f"{DAY1}.toml").write_text('title = "First light"\nhero = "120000-shot-hills.png"\n')
        (self.hist / DAY1 / "journal.json").write_text(json.dumps({"number": 7, "commits": [{}, {}], "merges": 1}))
        assets = {f"ocw-build-history-{DAY1}.zip", f"ocw-diary-day-07-{DAY1}.mp4", "ocw-build-diary.mp4"}
        s = self.build(assets=assets)
        self.assertEqual((s["days"], s["items"]), (2, 4))
        page = self.site(f"days/{DAY1}/index.html")
        order = [page.index(n) for n in ("090000-first-light.jpg", "100000-video-ride.mp4", "120000-shot-hills.png")]
        self.assertEqual(order, sorted(order))
        self.assertNotIn("110000-empty.jpg", page)
        self.assertNotIn("verdict", page)
        self.assertIn('class="play"', page)  # the video's play mark
        self.assertIn(f"{gallery.DOWNLOAD}ocw-build-history-{DAY1}.zip", page)
        self.assertIn(f"{gallery.DOWNLOAD}ocw-diary-day-07-{DAY1}.mp4", page)
        self.assertIn(f'href="../{DAY2}/" rel="next"', page)
        self.assertIn("Day 7", page)
        self.assertIn("In the video: the title picture", page)
        data = json.loads(page.split('type="application/json">')[1].split("</script>")[0])
        self.assertEqual([i["k"] for i in data["items"]], ["image", "video", "image"])
        self.assertTrue(data["items"][0]["w"].startswith("w/"))
        for rel in ("t/090000-first-light.jpg.jpg", "w/090000-first-light.jpg.jpg", "t/100000-video-ride.mp4.jpg"):
            self.assertTrue((gallery.site_dir() / "days" / DAY1 / rel).is_file(), rel)
        # DAY2 is not published yet: no links, the buttons are off
        page2 = self.site(f"days/{DAY2}/index.html")
        self.assertIn('class="btn off"', page2)
        self.assertNotIn("ocw-build-history-2026-10-02.zip\"", page2)
        index = self.site("index.html")
        self.assertLess(index.index(DAY2), index.index(DAY1))  # newest first
        self.assertIn(f"days/{DAY1}/t/120000-shot-hills.png.jpg", index)  # the script's hero
        self.assertIn("3 pictures · 1 videos", index)
        self.assertIn("OpenStreetMap contributors", index)
        self.assertIn("MIT OR Apache-2.0", index)
        self.assertTrue((gallery.site_dir() / "assets" / "gallery.js").is_file())
        self.assertTrue((gallery.site_dir() / ".nojekyll").is_file())

    def test_incremental(self):
        d = self.media(DAY1, "090000-a.png", "091000-b.png")
        self.build()
        self.assertEqual(len(self.enc.calls), 2)
        self.enc.calls.clear()
        s = self.build()
        self.assertEqual((self.enc.calls, s["ffmpeg_runs"]), ([], 0))
        time.sleep(0.01)
        (d / "091000-b.png").write_bytes(b"changed")  # new size and mtime: made again
        self.media(DAY1, "092000-c.png")
        self.build()
        self.assertEqual(sorted(c[1] for c in self.enc.calls), ["091000-b.png", "092000-c.png"])
        # a deleted cache file is made again
        self.enc.calls.clear()
        gallery.out_path({"day": DAY1, "file": "090000-a.png"}, "t").unlink()
        self.build()
        self.assertEqual(self.enc.calls, [(DAY1, "090000-a.png", ("t",))])

    def test_budget_steps_the_oldest_day_down(self):
        self.media(DAY1, *[f"09000{i}-a.png" for i in range(5)])
        self.media(DAY2, *[f"09000{i}-b.png" for i in range(5)])
        full = self.build()["bytes"]
        media = 2 * 5 * (SIZES["t"] + SIZES["w1280"])  # 110 KB; day 1 reduced: 25 + 55 = 80 KB
        static = sum(p.stat().st_size for p in gallery.SITE_SRC.glob("*") if p.suffix in (".css", ".js")) + \
            (gallery.ASSETS / "logos" / "ocw.svg").stat().st_size
        pages = full - media - static  # the HTML, as the planner's allowance
        with mock.patch.object(gallery, "PAGE_ALLOWANCE", pages + 2000):
            s = self.build(max_mb=(full - 20_000) / 1e6)
            self.assertEqual(s["tiers"], {DAY1: "reduced", DAY2: "full"})
            self.assertEqual({p.stat().st_size for p in (gallery.site_dir() / "days" / DAY1 / "w").iterdir()}, {4000})
            self.assertIn("smaller web copies", self.site(f"days/{DAY1}/index.html"))
            s = self.build(max_mb=(full - 50_000) / 1e6)  # every day smaller before any loses its copies
            self.assertEqual(s["tiers"], {DAY1: "reduced", DAY2: "reduced"})
            s = self.build(max_mb=(full - 78_000) / 1e6)
            self.assertEqual(s["tiers"], {DAY1: "thumbs", DAY2: "reduced"})
            self.assertFalse((gallery.site_dir() / "days" / DAY1 / "w").exists())
            self.assertIn("thumbnails only", self.site(f"days/{DAY1}/index.html"))
            self.assertLessEqual(s["bytes"], full - 78_000)
        with self.assertRaises(SystemExit):
            self.build(max_mb=0.001)

    def test_private_names_skipped_and_text_masked(self):
        self.media(DAY1, "090000-shot-buildhost.example.lan.png", "091000-ok.png")
        (self.days / f"{DAY1}.toml").write_text(
            'title = "Ran in /home/builder/src"\n[[chapter]]\ntitle = "On 10.20.30.40"\n'
            'shots = [{ file = "091000-ok.png", note = "mail dev@mail.example.org" }]\n')
        s = self.build()
        self.assertEqual(s["skipped"], [f"{DAY1}/090000-shot-buildhost.example.lan.png"])
        for p in gallery.site_dir().rglob("*.html"):
            self.assert_clean(p.read_text())
        self.assertFalse(any("buildhost" in p.name for p in gallery.site_dir().rglob("*")))

    def test_the_mask_guard_stops_a_leak(self):
        self.media(DAY1, "091000-ok.png")
        (self.days / f"{DAY1}.toml").write_text('title = "Ran in /home/builder/src"\n')
        self.build()
        before = self.site("index.html")
        with mock.patch.object(gallery, "mask", side_effect=lambda t, s=None: t):  # a broken mask
            with self.assertRaises(SystemExit) as e:
                self.build()
        self.assertIn("home directory", str(e.exception))
        self.assertNotIn("/home/builder", str(e.exception))
        self.assertEqual(self.site("index.html"), before)  # the old site stays

    def test_release_zips_only_when_changed(self):
        self.media(DAY1, "090000-a.png")
        self.media(DAY2, "090000-b.png")
        self.build()
        files = gallery.release_files(None)
        self.assertEqual(sorted(f.name for f in files), sorted([f"gallery-{DAY1}.zip", f"gallery-{DAY2}.zip",
                                                                 "gallery-pages.zip"]))
        with zipfile.ZipFile(files[0]) as z:
            names = z.namelist()
        self.assertIn(f"days/{DAY1}/t/090000-a.png.jpg", names)
        self.assertFalse(any(n.endswith(".html") for n in names))
        with zipfile.ZipFile(gallery.gallery_dir() / "release" / "gallery-pages.zip") as z:
            pages = z.namelist()
        self.assertIn("index.html", pages)
        self.assertIn(f"days/{DAY2}/index.html", pages)
        self.assertIn("assets/gallery.css", pages)
        self.assertFalse(any("/t/" in n for n in pages))
        # unchanged: only the pages; a new picture on day 2: its zip again
        self.build()
        self.assertEqual([f.name for f in gallery.release_files(None)], ["gallery-pages.zip"])
        self.media(DAY2, "100000-c.png")
        self.build()
        self.assertEqual([f.name for f in gallery.release_files(None)], [f"gallery-{DAY2}.zip", "gallery-pages.zip"])
        # missing on the release: uploaded again
        self.assertEqual(len(gallery.release_files({"gallery-pages.zip"})), 3)

    def test_publish_uploads_and_deploys(self):
        self.media(DAY1, "090000-a.png")
        calls = []

        def fake_run(cmd, **kw):
            calls.append([str(c) for c in cmd])
            return subprocess.CompletedProcess(cmd, 0, '{"assets": []}', "")
        with mock.patch.object(gallery, "run", side_effect=fake_run), \
                mock.patch.object(gallery, "encode", self.enc), mock.patch.dict(os.environ, {"OCW_ART_GH": "1"}):
            gallery.publish()
        up = next(c for c in calls if c[:3] == ["gh", "release", "upload"])
        self.assertEqual(up[up.index("-R") + 1], "newkit/OCW-ART")
        self.assertTrue(any(x.endswith("gallery-pages.zip") for x in up))
        self.assertTrue(any(c[:3] == ["gh", "workflow", "run"] and "gallery.yml" in c for c in calls))

    def test_cli_rejects_a_budget_over_pages_limit(self):
        env = {**os.environ, "OCW_ART_HISTORY": str(self.hist)}
        r = subprocess.run([sys.executable, str(HERE.parent / "diary.py"), "gallery", "build", "--max-mb", "1200"],
                           env=env, capture_output=True, text=True)
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("below 1000", r.stderr)


@unittest.skipUnless(shutil.which("ffmpeg") and shutil.which("ffprobe"), "needs ffmpeg")
class FfmpegTest(GalleryFixture):
    """Real thumbnails, web copies and a poster frame from generated test patterns."""

    def probe(self, p: Path) -> tuple[int, int]:
        r = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                            "stream=width,height", "-of", "csv=p=0", str(p)], capture_output=True, text=True)
        w, h = r.stdout.strip().split(",")
        return int(w), int(h)

    def test_thumbnails_web_copies_and_posters(self):
        d = self.hist / DAY1
        d.mkdir(parents=True)
        for args, name in ((["testsrc=size=1920x1080:rate=1", "-frames:v", "1"], "090000-big.png"),
                           (["testsrc=size=640x360:rate=1", "-frames:v", "1"], "091000-small.jpg"),
                           (["testsrc2=size=1280x720:rate=10", "-t", "2", "-pix_fmt", "yuv420p"], "092000-clip.mp4")):
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", *args, str(d / name)], check=True)
        s = gallery.build(assets=None, jobs=2)
        self.assertEqual((s["items"], s["failed"]), (3, []))
        site = gallery.site_dir() / "days" / DAY1
        self.assertEqual(self.probe(site / "t" / "090000-big.png.jpg"), (320, 180))
        self.assertEqual(self.probe(site / "w" / "090000-big.png.jpg"), (1280, 720))
        self.assertEqual(self.probe(site / "w" / "091000-small.jpg.jpg"), (640, 360))  # never scaled up
        self.assertEqual(self.probe(site / "t" / "092000-clip.mp4.jpg"), (320, 180))  # the poster
        man = json.loads((gallery.cache_dir() / "manifest.json").read_text())
        self.assertAlmostEqual(man[f"{DAY1}/092000-clip.mp4"]["seconds"], 2.0, delta=0.2)
        self.assertEqual(gallery.build(assets=None)["ffmpeg_runs"], 0)

    def test_a_broken_file_gets_no_preview(self):
        self.media(DAY1, "090000-broken.png")
        s = gallery.build(assets=None, jobs=1)
        self.assertEqual(s["failed"], [f"{DAY1}/090000-broken.png"])
        self.assertIn("no preview", self.site(f"days/{DAY1}/index.html"))


if __name__ == "__main__":
    unittest.main()
