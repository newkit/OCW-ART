"""Unit tests of the Git LFS part (ocwart/lfs.py, ART-PROJECT §2.8): the
managed .gitignore block, the budget guard, the policy, one commit per day,
private file names, the push rule and the verification. Each test makes its
own git repository (with this checkout's .gitattributes and .gitignore) and
a local bare remote in a temporary directory; no network, no GitHub.

    /usr/bin/python3 -m unittest discover -s tests -p 'test_*.py'   (make test)
"""

from __future__ import annotations

import datetime as dt
import json
import os
import shutil
import subprocess
import sys
import unittest
from pathlib import Path
from unittest import mock

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))

from ocwart import collect, lfs  # noqa: E402
from test_diary import Fixture  # noqa: E402

REPO = HERE.parent
D1, D2, D3 = "2026-10-01", "2026-10-02", "2026-10-03"
TODAY = "2026-10-04"
HAVE_LFS = subprocess.run(["git", "lfs", "version"], capture_output=True).returncode == 0
GIT_ENV = {"GIT_AUTHOR_NAME": "Test Rider", "GIT_AUTHOR_EMAIL": "rider@example.org",
           "GIT_COMMITTER_NAME": "Test Rider", "GIT_COMMITTER_EMAIL": "rider@example.org"}


class BlockTest(unittest.TestCase):
    def test_managed_allow_list(self):
        base = "/build-history/**\n!/build-history/????-??-??/\n"
        t = lfs.with_allowed(base, D2, {".png", ".mp4"})
        t = lfs.with_allowed(t, D1, {".jpg"})
        t2 = lfs.with_allowed(t, D1, {".jpg"})
        self.assertEqual(t, t2)  # idempotent
        self.assertTrue(t.startswith(base))
        self.assertEqual(lfs.ignore_block(t), {D1: {".jpg"}, D2: {".png", ".mp4"}})
        lines = t.split(lfs.BEGIN)[1].split(lfs.END)[0].splitlines()
        self.assertIn(f"!/build-history/{D1}/*.jpg", lines)
        self.assertLess(lines.index(f"!/build-history/{D1}/*.jpg"), lines.index(f"!/build-history/{D2}/*.mp4"))
        self.assertEqual(t.count(lfs.BEGIN), 1)

    def test_settings(self):
        with mock.patch.dict(os.environ, {"OCW_ART_LFS_BUDGET_GIB": "2.5", "OCW_ART_LFS_POLICY": "pictures"}):
            self.assertEqual(lfs.budget_bytes(), int(2.5 * lfs.GIB))
            self.assertEqual(lfs.policy(), "pictures")
        with mock.patch.dict(os.environ, {"OCW_ART_LFS_BUDGET_GIB": "11"}), self.assertRaises(SystemExit):
            lfs.budget_bytes()  # over the free quota
        with mock.patch.dict(os.environ, {"OCW_ART_LFS_POLICY": "everything"}), self.assertRaises(SystemExit):
            lfs.policy()

    def test_this_checkout_routes_only_day_media_to_lfs(self):
        for rel, want in ((f"build-history/{D1}/x.jpg", "lfs"), (f"build-history/{D1}/x.mp4", "lfs"),
                          (f"build-history/{D1}/x.webm", "lfs"), ("build-history/diary/d.mp4", "unspecified"),
                          ("build-history/ocw-build-history-2026-10-01.zip", "unspecified"),
                          (f"build-history/.work/{D1}/sheets/s.jpg", "unspecified"),
                          (f"build-history/{D1}/logs/x.png", "unspecified"), ("assets/logos/ocw-512.png", "unspecified")):
            out = subprocess.run(["git", "-C", str(REPO), "check-attr", "filter", "--", rel],
                                 capture_output=True, text=True).stdout
            self.assertTrue(out.strip().endswith(": " + want), (rel, out))


@unittest.skipUnless(HAVE_LFS, "needs git-lfs")
class LfsRepoTest(Fixture):
    def setUp(self):
        super().setUp()
        self.env2 = mock.patch.dict(os.environ, {**GIT_ENV, "OCW_ART_LFS_POLICY": "all",
                                                 "OCW_ART_LFS_BUDGET_GIB": str(5000 / lfs.GIB)})
        self.env2.start()
        r = self.tmp
        self.remote = self.tmp.parent / (self.tmp.name + "-remote.git")
        self.git("init", "-q", "--bare", "-b", "main", str(self.remote), cwd=self.tmp.parent)
        self.git("init", "-q", "-b", "main")
        self.git("lfs", "install", "--local")
        shutil.copy(REPO / ".gitattributes", r / ".gitattributes")
        gi = (REPO / ".gitignore").read_text()  # without the real days' block
        if lfs.BEGIN in gi:
            gi = gi.split(lfs.BEGIN)[0].rstrip("\n") + "\n" + gi.split(lfs.END, 1)[1].lstrip("\n")
        (r / ".gitignore").write_text(gi)
        (self.hist / "index.md").write_text("# Build history\n")
        self.git("add", ".gitattributes", ".gitignore", "build-history/index.md")
        self.git("commit", "-q", "-m", "fixture")
        self.git("remote", "add", "origin", str(self.remote))
        self.git("push", "-q", "origin", "main")

    def tearDown(self):
        self.env2.stop()
        subprocess.run(["rm", "-rf", "--", str(self.remote)], check=False)
        super().tearDown()

    def git(self, *args, cwd=None):
        return subprocess.run(["git", "-C", str(cwd or self.tmp), *args], check=True, capture_output=True,
                              text=True).stdout

    def media(self, day, name, size):
        d = self.hist / day
        d.mkdir(parents=True, exist_ok=True)
        (d / name).write_bytes(os.urandom(size))

    def test_budget_status_commit_and_push(self):
        self.media(D1, "090000-a.png", 1000)
        self.media(D1, "091000-b.mp4", 1000)
        self.media(D2, "090000-c.jpg", 2500)
        self.media(D3, "090000-d.jpg", 3000)  # would cross the 5000-byte budget
        (self.hist / D1 / "notes.txt").write_text("not media\n")
        self.media(D1, "092000-aborted.jpg", 0)  # an aborted capture: committed empty, no LFS object
        st = lfs.status(today=TODAY)
        self.assertEqual((st["stored_bytes"], st["pending_bytes"], st["pending_files"]), (0, 7500, 5))
        self.assertTrue(st["over_budget"])
        self.assertEqual(st["rate_per_day"], 2500)  # (2000 + 2500 + 3000) / 3 finished days
        self.assertEqual(st["largest_day"], 3000)
        self.assertLess(st["days_left"], 0)
        self.assertLess(st["days_left_largest"], 0)
        self.assertIn("budget", lfs.report(st))

        r = lfs.commit_days(today=TODAY, trailers=["Co-Authored-By: Test Rider <rider@example.org>"])
        self.assertEqual([c["day"] for c in r["committed"]], [D1, D2])
        self.assertEqual([x["day"] for x in r["refused"]], [D3])
        self.assertTrue(any("LFS budget reached" in w for w in r["warnings"]))
        log = self.git("log", "--format=%s", "-n", "2").splitlines()
        self.assertEqual(log, [f"Build history {D2}: 1 pictures and 0 videos in Git LFS (0 MB; ART-PROJECT §2.8)",
                               f"Build history {D1}: 2 pictures and 1 videos in Git LFS (0 MB; ART-PROJECT §2.8)"])
        self.assertIn("Co-Authored-By: Test Rider", self.git("log", "-1", "--format=%B"))
        # the media are LFS pointers, the text file and day 3 are not committed
        self.assertTrue(self.git("show", f"HEAD:build-history/{D1}/091000-b.mp4").startswith(
            "version https://git-lfs.github.com/spec/v1"))
        files = self.git("ls-files").split()
        self.assertNotIn(f"build-history/{D1}/notes.txt", files)
        self.assertNotIn(f"build-history/{D3}/090000-d.jpg", files)
        ignored = subprocess.run(["git", "-C", str(self.tmp), "check-ignore", "-q",
                                  f"build-history/{D3}/090000-d.jpg"]).returncode == 0
        self.assertTrue(ignored)  # left local and ignored
        gi = (self.tmp / ".gitignore").read_text()
        self.assertEqual(lfs.ignore_block(gi), {D1: {".png", ".mp4", ".jpg"}, D2: {".jpg"}})
        self.assertIn(".gitignore", self.git("show", "--name-only", "--format=", f"HEAD~1"))
        self.assertEqual(self.git("status", "--porcelain", "--", ".gitignore"), "")

        self.assertIn(f"build-history/{D1}/092000-aborted.jpg", files)
        self.assertEqual(self.git("status", "--porcelain", "--", "build-history"), "")
        v = lfs.verify()
        self.assertEqual((v["lfs_files"], v["committed_media"], v["empty_files"], v["ok"]), (3, 3, 1, True))
        self.assertEqual(lfs.stored_bytes(), (4500, 3))
        st = lfs.status(today=TODAY)
        self.assertEqual((st["stored_bytes"], st["pending_files"]), (4500, 1))
        self.assertEqual(st["days"][D1]["pending_files"], 0)

        p = lfs.push()
        self.assertEqual((p["pushed"], p["ok"]), (2, True))
        self.assertEqual(self.git("rev-parse", "HEAD"), self.git("rev-parse", "main", cwd=self.remote))
        objects = [x for x in (self.remote / "lfs" / "objects").rglob("*") if x.is_file()]
        self.assertEqual(len(objects), 3)
        self.assertEqual(lfs.commit_days(today=TODAY)["committed"], [])  # nothing new fits

    def test_policy_pictures_keeps_videos_local(self):
        self.media(D1, "090000-a.png", 100)
        self.media(D1, "091000-b.mp4", 100)
        with mock.patch.dict(os.environ, {"OCW_ART_LFS_POLICY": "pictures"}):
            r = lfs.commit_days(today=TODAY)
            st = lfs.status(today=TODAY)
        self.assertEqual(r["committed"][0]["files"], 1)
        self.assertNotIn(f"build-history/{D1}/091000-b.mp4", self.git("ls-files").split())
        self.assertEqual(st["days"][D1]["left_out_files"], 1)

    def test_private_names_never_committed_and_today_waits(self):
        self.media(D1, "090000-shot-buildhost.example.lan.png", 100)
        self.media(D1, "091000-ok.png", 100)
        self.media(TODAY, "090000-today.png", 100)
        r = lfs.commit_days(today=TODAY)
        files = self.git("ls-files").split()
        self.assertIn(f"build-history/{D1}/091000-ok.png", files)
        self.assertFalse(any("buildhost" in f for f in files))
        self.assertFalse(any(TODAY in f for f in files))  # not finished yet
        self.assertTrue(any("private pattern" in w for w in r["warnings"]))
        self.assertTrue(lfs.commit_days([TODAY], today=TODAY)["committed"])  # explicitly: the end-of-day step

    def test_dry_run_changes_nothing(self):
        self.media(D1, "090000-a.png", 100)
        head = self.git("rev-parse", "HEAD")
        r = lfs.commit_days(dry_run=True, today=TODAY)
        self.assertTrue(r["committed"][0]["dry_run"])
        self.assertEqual(self.git("rev-parse", "HEAD"), head)
        self.assertNotIn(lfs.BEGIN, (self.tmp / ".gitignore").read_text())

    def test_refuses_off_main_and_foreign_unpushed_commits(self):
        self.media(D1, "090000-a.png", 100)
        self.git("checkout", "-q", "-b", "other")
        with self.assertRaises(SystemExit) as e:
            lfs.commit_days(today=TODAY)
        self.assertIn("not main", str(e.exception))
        self.git("checkout", "-q", "main")
        (self.tmp / "README.md").write_text("code\n")
        self.git("add", "README.md")
        self.git("commit", "-q", "-m", "code change")
        lfs.commit_days(today=TODAY)
        with self.assertRaises(SystemExit) as e:
            lfs.push()
        self.assertIn("push by hand", str(e.exception))

    def test_without_git_lfs(self):
        with mock.patch.object(lfs, "lfs_available", return_value="git-lfs is not installed: " + lfs.INSTALL_HINT):
            with self.assertRaises(SystemExit) as e:
                lfs.commit_days(today=TODAY)
        self.assertIn("make deps", str(e.exception))


class CollectLfsTest(Fixture):
    """The collector's LFS step, with lfs.* mocked."""

    def run_collect(self, hour, **env):
        with mock.patch.dict(os.environ, {"OCW_ART_LFS": "1", **env}), \
                mock.patch.object(collect, "gather", return_value=0), mock.patch.object(collect, "journal"), \
                mock.patch.object(collect, "sheet"), \
                mock.patch.object(lfs, "lfs_available", return_value=None), \
                mock.patch.object(lfs, "commit_days", return_value={"committed": [{"day": D1}], "refused": [],
                                                                     "warnings": ["LFS budget reached: x"]}) as c, \
                mock.patch.object(lfs, "status", return_value={"policy": "all", "stored_bytes": 3 * lfs.GIB,
                                                               "pending_bytes": 0, "budget": 9 * lfs.GIB,
                                                               "days_left": 4.2}):
            st = collect.collect(now=dt.datetime(2026, 10, 4, hour, 5))
        return st, c

    def test_commit_in_the_23h_run_only(self):
        st, c = self.run_collect(14)
        c.assert_not_called()
        self.assertFalse(st["lfs_push"])
        self.assertEqual(st["lfs"]["days_left"], 4.2)
        st, c = self.run_collect(23)
        c.assert_called_once()
        self.assertTrue(st["lfs_push"])
        self.assertEqual(st["warnings"], ["LFS budget reached: x"])
        self.assertEqual(st["status"], "ok")  # a warning, not a failure
        status = json.loads((self.out / "build-log" / "2026-10-04" / "art.json").read_text())
        self.assertIs(status["lfs_push"], True)

    def test_missing_git_lfs_fails_with_the_hint(self):
        with mock.patch.dict(os.environ, {"OCW_ART_LFS": "1"}), \
                mock.patch.object(collect, "gather", return_value=0), mock.patch.object(collect, "journal"), \
                mock.patch.object(lfs, "lfs_available", return_value="git-lfs is not installed: " + lfs.INSTALL_HINT):
            st = collect.collect(now=dt.datetime(2026, 10, 4, 23, 5))
        self.assertEqual(st["status"], "failed")
        self.assertTrue(any("make deps" in e for e in st["errors"]))


if __name__ == "__main__":
    unittest.main()
