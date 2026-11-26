"""Unit tests of the art project's tool (docs/ART-PROJECT.md): masking of the
tracked text files, check-masked, the collector's days, the lock, the status
file, the OCW checkout setting, GitHub targets and collect.sh. A small
fixture archive in a temporary directory; no real archive, no network, no
ffmpeg. The OCW checkout (OCW_REPO, else ../OCW) is only read (git log).

    /usr/bin/python3 -m unittest discover -s tests -p 'test_*.py'   (make test)
"""

from __future__ import annotations

import datetime as dt
import json
import os
import subprocess
import sys
import tempfile
import time
import unittest
from pathlib import Path
from unittest import mock

HERE = Path(__file__).resolve().parent
REPO = HERE.parent  # the OCW-ART checkout: diary.py, bin/collect.sh, ocwart/
sys.path.insert(0, str(REPO))

from ocwart import agents, archive, collect, core, incidents, journal, mask, prompts, publish  # noqa: E402

# Fake build machines: (value, replacement) as mask._secrets() returns them.
SECRETS = [("buildhost.example.lan", "marge"), ("10.20.30.40", "leela"), ("builder", "user"),
           ("/home/devuser", "~")]
PRIVATE = ["buildhost.example.lan", "10.20.30.40", "builder@", "/home/devuser", "/home/builder",
           "dev@mail.example.org", "192.168.7.9"]
DAY = "2026-11-14"


def tree_state(root: Path) -> dict:
    """{relative path: (size, mtime_ns)} of every file and folder below root."""
    if not root.exists():
        return {}
    out = {}
    for p in [root, *root.rglob("*")]:
        st = p.lstat()
        out[p.relative_to(root).as_posix()] = (st.st_size if p.is_file() else None, st.st_mtime_ns)
    return out


# The real archive at the default place (this checkout's build-history/):
# the tests must never touch it. They hold its lock meanwhile (the hourly
# collector waits), and compare every file's size and mtime before and after.
REAL_HISTS = [core.ART / "build-history"]
_real: dict[Path, dict] = {}


def setUpModule():
    import fcntl
    for hist in REAL_HISTS:
        if not hist.is_dir():
            continue
        entry = {"lock": None, "state": None}
        lock = hist / ".lock"
        if lock.exists():  # (no lock file: creating one would touch the archive)
            f = open(lock, "r")
            try:
                fcntl.flock(f, fcntl.LOCK_SH | fcntl.LOCK_NB)
            except BlockingIOError:
                f.close()
                continue  # a collector or diary run is busy: no stable state to compare
            entry["lock"] = f
        entry["state"] = tree_state(hist)
        _real[hist] = entry


def tearDownModule():
    errors = []
    for hist, entry in _real.items():
        try:
            after = tree_state(hist)
            changed = sorted(k for k in set(after) | set(entry["state"]) if after.get(k) != entry["state"].get(k))
            if changed:
                errors.append(f"the tests changed the real archive {hist}: {changed[:10]}")
        finally:
            if entry["lock"] is not None:
                entry["lock"].close()
    if errors:
        raise AssertionError("; ".join(errors))


class Fixture(unittest.TestCase):
    """A temporary archive and test-output, the fake secrets."""

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="ocw-art-test-"))
        self.hist = self.tmp / "build-history"
        self.out = self.tmp / "test-output"
        self.hist.mkdir()
        self.out.mkdir()
        self._saved = (core.HIST, core.TEST_OUTPUT, mask._SECRETS, prompts.TRANSCRIPTS, core.WORKTREES)
        core.set_history(self.hist)
        core.TEST_OUTPUT = self.out
        prompts.TRANSCRIPTS = str(self.tmp / "no-transcripts")
        core.WORKTREES = None  # never the real agent worktrees' test-output
        mask._SECRETS = sorted(SECRETS, key=lambda kv: -len(kv[0]))
        self.env = mock.patch.dict(os.environ, {"OCW_TRANSCRIPTS": str(self.tmp / "no-transcripts"),
                                                  "OCW_ART_JOURNAL": "0",  # never the live journal
                                                  "OCW_ART_NO_MACHINES": "1", "OCW_ART_GH": "0",
                                                  # the gallery and LFS have their own tests
                                                  "OCW_ART_GALLERY": "0", "OCW_ART_LFS": "0"})
        self.env.start()
        os.environ.pop("OCW_ART_LOCK_HELD", None)

    def tearDown(self):
        self.env.stop()
        core.set_history(self._saved[0])
        core.TEST_OUTPUT, mask._SECRETS, prompts.TRANSCRIPTS, core.WORKTREES = self._saved[1:]
        subprocess.run(["rm", "-rf", "--", str(self.tmp)], check=False)

    def assert_clean(self, text: str):
        for p in PRIVATE:
            self.assertNotIn(p, text)


class MaskTest(Fixture):
    def test_mask_hosts_users_homes_mails_ips(self):
        t = ("ssh builder@buildhost.example.lan; ping 10.20.30.40; cd /home/devuser/src; "
             "ls /home/builder/src/OCW; mail dev@mail.example.org; 192.168.7.9; C:\\Users\\builder\\x")
        m = mask.mask(t)
        self.assert_clean(m)
        self.assertIn("user@marge", m)
        self.assertIn("~/src/OCW", m)
        self.assertIn("<e-mail>", m)
        self.assertIn("<ip>", m)

    def test_mask_keeps_public_names(self):
        t = "~/.builder/worktrees builder.ai icon@2x.png react@18.3.1 https://x.org/home/page"
        self.assertEqual(mask.mask(t), t)
        self.assertEqual(mask.private_findings(t), [])

    def test_mask_is_idempotent(self):
        t = "builder@buildhost.example.lan /home/devuser/x 10.20.30.40"
        self.assertEqual(mask.mask(mask.mask(t)), mask.mask(t))
        self.assertEqual(mask.private_findings(mask.mask(t)), [])

    def test_tracked_files_written_masked(self):
        """journal.md, journal.json and tokens.json land masked on disk."""
        commits = [{"sha": "abc1234", "time": "10:00:00", "merge": False, "added": 3, "removed": 1,
                    "subject": "Run on buildhost.example.lan in /home/builder/src/OCW (dev@mail.example.org)"}]
        tokens = {"day": DAY, "total": {"total": 10, "messages": 1, "input": 1, "cache_write": 2,
                                        "cache_read": 3, "output": 4},
                  "tasks": {"agent: fix /home/devuser/x on 10.20.30.40": {"feature": "Other", "total": 10,
                                                                          "output": 4, "messages": 1}},
                  "features": {"Other": {"total": 10, "output": 4, "messages": 1}}, "models": {}}
        with mock.patch.object(journal, "commits_of", return_value=commits), \
                mock.patch.object(prompts, "tokens_of", return_value=tokens), \
                mock.patch.object(core, "all_days", return_value=["2026-11-11", DAY]), \
                mock.patch.object(core, "days_with_scripts", return_value=[]):
            j = journal.journal(DAY)
        self.assertEqual(j["number"], 2)
        for name in mask.TRACKED_DAY[:3]:  # (incidents.md is written by the coordinator)
            text = (self.hist / DAY / name).read_text()
            self.assert_clean(text)
        self.assertIn("~/src/OCW", (self.hist / DAY / "journal.md").read_text())
        json.loads((self.hist / DAY / "journal.json").read_text())  # still valid JSON
        self.assertEqual(mask.check_masked(), [])

    def test_day_number_without_commits_yet(self):
        with mock.patch.object(core, "all_days", return_value=["2026-11-11", "2026-11-12"]), \
                mock.patch.object(core, "days_with_scripts", return_value=[]):
            self.assertEqual(core.day_number("2026-11-12"), 2)
            self.assertEqual(core.day_number("2026-11-13"), 3)

    def test_day_number_counts_a_told_day_without_commits(self):
        """2026-11-20: no commits (the weekly token limit), but a day script –
        it is day 10, and the next day with commits is day 11."""
        days = ["2026-11-18", "2026-11-19", "2026-11-21"]
        with mock.patch.object(core, "all_days", return_value=days), \
                mock.patch.object(core, "days_with_scripts", return_value=["2026-11-19", "2026-11-20"]):
            self.assertEqual(core.day_number("2026-11-19"), 2)
            self.assertEqual(core.day_number("2026-11-20"), 3)
            self.assertEqual(core.day_number("2026-11-21"), 4)


class MachinesConfTest(Fixture):
    """The mask list comes from config/machines.toml – in an agent worktree
    from the main checkout's (regression: on 2026-11-15 a worktree run wrote
    journals with the build users unmasked)."""

    def test_falls_back_to_the_main_checkout(self):
        here, main = self.tmp / "wt", self.tmp / "main"
        (main / "config").mkdir(parents=True)
        (main / "config" / "machines.toml").write_text('[[machine]]\nname = "marge"\n')
        here.mkdir()
        with mock.patch.object(core, "ROOT", here), mock.patch.object(mask, "main_checkout", return_value=main):
            self.assertEqual(mask.machines_conf(), main / "config" / "machines.toml")
            (here / "config").mkdir()
            (here / "config" / "machines.toml").write_text("")
            self.assertEqual(mask.machines_conf(), here / "config" / "machines.toml")

    def test_refuses_to_mask_without_a_machine_list(self):
        with mock.patch.object(mask, "machines_conf", return_value=None), mock.patch.object(mask, "_SECRETS", None), \
                mock.patch.object(core, "CONFIG", self.tmp / "none.toml"), mock.patch.dict(os.environ):
            os.environ.pop("OCW_ART_NO_MACHINES", None)
            with self.assertRaises(SystemExit) as e:
                mask._secrets()
            self.assertIn("machines.toml", str(e.exception))
            os.environ["OCW_ART_NO_MACHINES"] = "1"
            self.assertEqual([r for _, r in mask._secrets()], ["~"])

    def test_private_words_from_the_config(self):
        """mask_users and mask_names of ocw-art.toml: a former user name as a
        word, a real person's name in any case (a prompt on 2026-11-16)."""
        conf = self.tmp / "ocw-art.toml"
        conf.write_text('mask_users = ["olduser"]\nmask_names = ["Ada Realname"]\n')
        with mock.patch.object(mask, "machines_conf", return_value=None), mock.patch.object(mask, "_SECRETS", None), \
                mock.patch.object(core, "CONFIG", conf), mock.patch.dict(os.environ, {"OCW_ART_NO_MACHINES": "1"}):
            secrets = mask._secrets()
            self.assertEqual(mask.mask("which are olduser files? ADA REALNAME rode", secrets),
                             "which are user files? <name> rode")
            self.assertEqual(mask.mask("~/olduser-notes", secrets), "~/olduser-notes")
            self.assertEqual([k for _, k in mask.private_findings("Ada Realname", secrets)], ["a real person's name"])

    def test_tokens_and_keys(self):
        """API tokens pasted into a prompt (a Vercel and a Fly.io token,
        2026-11-26) and mask_secrets (a hex key in any spelling); commit and
        certificate hashes stay."""
        t = ("key vck_3fmKxLSg1TLSOWDBycZ4rY2A5BRr2bdClOIDXjtD, fly FlyV1 fm2_lJPECAAAAAAAGk6N+xBD/ISq==,fm2_abcdefABCDEF0123 "
             "gh ghp_abcdefghijklmnopqrstuvwxyz0123456789 commit 5e482567 cert 0ae1fb51a5eacb8fb1beb577b107b5fa5")
        self.assertEqual(mask.mask(t), "key <token>, fly <token> gh <token> commit 5e482567 "
                         "cert 0ae1fb51a5eacb8fb1beb577b107b5fa5")
        conf = self.tmp / "ocw-art.toml"
        conf.write_text('mask_secrets = ["0011AABBCCDDEEFF"]\n')
        with mock.patch.object(mask, "machines_conf", return_value=None), mock.patch.object(mask, "_SECRETS", None), \
                mock.patch.object(core, "CONFIG", conf), mock.patch.dict(os.environ, {"OCW_ART_NO_MACHINES": "1"}):
            secrets = mask._secrets()
            for k in ("0011aabbccddeeff", "00 11 AA BB CC DD EE FF", "0x00, 0x11, 0xAA, 0xBB, 0xCC, 0xDD, 0xEE, 0xFF"):
                self.assertEqual(mask.mask(f"the key {k}.", secrets), "the key <secret>.")
            self.assertEqual(mask.mask("ab0011aabbccddeeff00", secrets), "ab0011aabbccddeeff00")
            self.assertEqual([k for _, k in mask.private_findings("vck_abcdefghijklmnopqrstu", secrets)], ["a token or key"])


class CheckMaskedTest(Fixture):
    def write(self, rel, text):
        p = self.hist / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text)
        return p

    def test_finds_private_patterns_in_tracked_files_only(self):
        self.write("index.md", "# Build history\n\nfrom /home/builder/src/OCW\n")
        self.write(f"{DAY}/journal.json", '{"x": "ssh builder@buildhost.example.lan"}\n')
        self.write(f"{DAY}/tokens.json", "{}\n")
        self.write("SHA256SUMS", "00  ocw-build-history-2026-11-14.zip\n")
        # Untracked text keeps the originals: not checked.
        self.write(f"{DAY}/logs/run.log", "10.20.30.40 /home/devuser\n")
        self.write(f"{DAY}/prompts.md", "dev@mail.example.org\n")
        found = mask.check_masked()
        self.assertIn("index.md:3: home directory", found)
        self.assertTrue(any(f.startswith(f"{DAY}/journal.json:1: ") for f in found))
        self.assertFalse(any("logs" in f or "prompts" in f for f in found))
        for f in found:  # the values are never reported
            self.assert_clean(f)

    def test_media_file_names_are_checked_masked(self):
        """File names go public (Git LFS, gallery, day zips): a private
        pattern in one is a finding, reported masked."""
        (self.hist / DAY).mkdir(parents=True)
        (self.hist / DAY / "090000-shot-buildhost.example.lan.png").write_bytes(b"x")
        (self.hist / DAY / "091000-shot-ok.png").write_bytes(b"x")
        (self.hist / DAY / "092000-notes-buildhost.example.lan.txt").write_text("x")  # not media: zip text is masked
        found = mask.check_masked()
        self.assertEqual(found, [f"{DAY}/090000-shot-marge.png: build-machine host in the file name"])
        self.assertEqual(mask.check_masked(fix=True), found)  # never renamed

    def test_fix_masks_in_place(self):
        p = self.write("index.md", "from /home/builder/src/OCW on 10.20.30.40\n")
        log_ = self.write(f"{DAY}/logs/run.log", "10.20.30.40\n")
        self.assertTrue(mask.check_masked())
        self.assertEqual(mask.check_masked(fix=True), [])
        self.assertEqual(p.read_text(), "from ~/src/OCW on leela\n")
        self.assertEqual(log_.read_text(), "10.20.30.40\n")  # originals stay
        self.assertEqual(mask.check_masked(), [])

    def test_cli_exit_code(self):
        self.write("index.md", "cd /home/someone/x\n")
        env = {**os.environ, "OCW_ART_HISTORY": str(self.hist)}
        r = subprocess.run([sys.executable, str(REPO / "diary.py"), "check-masked"], env=env,
                           capture_output=True, text=True)
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("index.md:1: home directory", r.stdout)
        self.assertNotIn("/home/someone", r.stdout + r.stderr)
        r = subprocess.run([sys.executable, str(REPO / "diary.py"), "check-masked", "--fix"], env=env,
                           capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stderr)


class DaysTest(unittest.TestCase):
    def test_today_and_yesterday(self):
        self.assertEqual(collect.default_collect_days(dt.datetime(2026, 11, 14, 9, 5)),
                         ["2026-11-13", "2026-11-14"])

    def test_month_and_year_boundary(self):
        self.assertEqual(collect.default_collect_days(dt.datetime(2026, 12, 1, 0, 3)),
                         ["2026-11-30", "2026-12-01"])
        self.assertEqual(collect.default_collect_days(dt.datetime(2027, 1, 1, 0, 1)),
                         ["2026-12-31", "2027-01-01"])


class LockTest(Fixture):
    def test_second_run_waits_and_times_out(self):
        with core.art_lock("first"):
            self.assertIn("diary.py first", core.lock_path().read_text())
            t0 = time.monotonic()
            with self.assertRaises(TimeoutError):
                with core.art_lock("second", wait=0.3):
                    pass
            self.assertGreaterEqual(time.monotonic() - t0, 0.3)
        with core.art_lock("third", wait=0.3):  # free again
            pass

    def test_lock_held_by_the_collector_script(self):
        with core.art_lock("collector"):
            with mock.patch.dict(os.environ, {"OCW_ART_LOCK_HELD": "1"}):
                with core.art_lock("child", wait=0.1):  # no deadlock
                    pass

    def test_lock_excludes_another_process(self):
        holder = subprocess.Popen(["flock", str(core.lock_path()), "sleep", "5"])
        try:
            deadline = time.monotonic() + 3
            while not core.lock_path().exists() and time.monotonic() < deadline:
                time.sleep(0.05)
            time.sleep(0.2)
            with self.assertRaises(TimeoutError):
                with core.art_lock("x", wait=0.3):
                    pass
        finally:
            holder.kill()
            holder.wait()


class OcwRepoTest(Fixture):
    """The OCW checkout the tool reads: OCW_REPO, else ocw-art.toml, else ../OCW."""

    def test_env_then_config_then_sibling(self):
        art = self.tmp / "OCW-ART"
        art.mkdir()
        conf = art / "ocw-art.toml"
        with mock.patch.object(core, "ART", art), mock.patch.object(core, "CONFIG", conf), \
                mock.patch.dict(os.environ):
            os.environ.pop("OCW_REPO", None)
            self.assertEqual(core.ocw_repo(), (self.tmp / "OCW").resolve())
            conf.write_text('ocw_repo = "../src/OCW-main"\n')
            self.assertEqual(core.ocw_repo(), (self.tmp / "src" / "OCW-main").resolve())
            os.environ["OCW_REPO"] = str(self.tmp / "elsewhere")
            self.assertEqual(core.ocw_repo(), (self.tmp / "elsewhere").resolve())
            conf.write_text("ocw_repo = [\n")
            os.environ.pop("OCW_REPO")
            with self.assertRaises(SystemExit):
                core.ocw_repo()

    def test_check_ocw_needs_a_checkout(self):
        with mock.patch.object(core, "ROOT", self.tmp / "nothing"):
            with self.assertRaises(SystemExit) as e:
                core.check_ocw()
            self.assertIn("OCW_REPO", str(e.exception))
        core.check_ocw()  # the checkout the tests run against

    def test_cli_prints_the_checkout(self):
        r = subprocess.run([sys.executable, str(REPO / "diary.py"), "ocw-repo"],
                           env={**os.environ, "OCW_REPO": str(self.tmp)}, capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(r.stdout.strip(), str(self.tmp.resolve()))

    def test_cli_refuses_without_an_ocw_checkout(self):
        r = subprocess.run([sys.executable, str(REPO / "diary.py"), "check-masked"],
                           env={**os.environ, "OCW_REPO": str(self.tmp / "nothing"),
                                "OCW_ART_HISTORY": str(self.hist)}, capture_output=True, text=True)
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("no OCW checkout", r.stderr)


class GitHubTest(Fixture):
    """publish uploads to newkit/OCW-ART; fetch falls back to OCW's release."""

    def test_publish_goes_to_ocw_art(self):
        (self.hist / "diary").mkdir()
        (self.hist / "diary" / "ocw-build-diary.mp4").write_bytes(b"video")
        calls = []

        def fake_run(cmd, **kw):
            calls.append([str(c) for c in cmd])
            return subprocess.CompletedProcess(cmd, 0, "", "")
        with mock.patch.object(publish, "run", side_effect=fake_run):
            publish.publish([])
        gh = [c for c in calls if c[:1] == ["gh"]]
        self.assertTrue(gh)
        for c in gh:
            self.assertEqual(c[c.index("-R") + 1], "newkit/OCW-ART")
        self.assertEqual(gh[-1][:3], ["gh", "release", "upload"])
        self.assertTrue((self.hist / "SHA256SUMS").read_text().rstrip().endswith("  ocw-build-diary.mp4"))

    def test_fetch_falls_back_to_the_ocw_release(self):
        repos = []

        def fake_run(cmd, **kw):
            cmd = [str(c) for c in cmd]
            if cmd[:3] == ["gh", "release", "download"]:
                repos.append(cmd[cmd.index("-R") + 1])
            return subprocess.CompletedProcess(cmd, 1, "", "")
        with mock.patch.object(archive, "run", side_effect=fake_run):
            archive.fetch(DAY)
        self.assertEqual(repos, ["newkit/OCW-ART", "newkit/OCW"])


class CollectTest(Fixture):
    def fake_gather(self, day):
        if day == "2026-11-13":
            raise RuntimeError("disk full at /home/builder/x")
        (self.hist / day).mkdir(parents=True, exist_ok=True)
        (self.hist / day / "120000-shot.png").write_bytes(b"x")
        (self.hist / day / "120100-clip.mp4").write_bytes(b"x")
        return 2

    def test_status_file(self):
        now = dt.datetime(2026, 11, 14, 15, 2)
        with mock.patch.object(collect, "gather", side_effect=self.fake_gather), \
                mock.patch.object(collect, "journal") as journal, \
                mock.patch.object(collect, "sheet") as sheet:
            st = collect.collect(now=now)
        self.assertEqual([c.args[0] for c in journal.call_args_list], [DAY])  # the failed day: no journal
        sheet.assert_not_called()  # not the 23:xx run
        status = json.loads((self.out / "build-log" / DAY / "art.json").read_text())
        self.assertEqual(status, st)
        self.assertEqual(status["status"], "failed")
        self.assertEqual(status["days"][DAY], {"new_files": 2, "media": 2, "incidents": 0})
        self.assertEqual(status["new_files"], 2)
        self.assertEqual(status["media"], 2)
        self.assertEqual(status["mask_check"], "ok")
        self.assertTrue(status["start"] and status["end"])
        self.assertEqual(len(status["errors"]), 1)
        self.assertIn("2026-11-13", status["errors"][0])
        self.assert_clean(json.dumps(status))  # errors are masked too
        runs = (self.out / "build-log" / DAY / "art-runs.jsonl").read_text().splitlines()
        self.assertEqual(json.loads(runs[-1])["status"], "failed")

    def test_sheets_in_the_23h_run_and_mask_failure(self):
        (self.hist / "index.md").write_text("ssh builder@buildhost.example.lan\n")
        with mock.patch.object(collect, "gather", return_value=0), \
                mock.patch.object(collect, "journal"), mock.patch.object(collect, "sheet") as sheet:
            st = collect.collect(now=dt.datetime(2026, 11, 14, 23, 3))
        sheet.assert_called_once_with(DAY)
        self.assertTrue(st["sheets"])
        self.assertEqual(st["status"], "failed")
        self.assertTrue(st["mask_check"].startswith("failed: "))


class CollectScriptTest(Fixture):
    """collect.sh on the fixture (OCW_ART_HISTORY, OCW_TEST_OUTPUT)."""

    SCRIPT = REPO / "bin" / "collect.sh"

    def script_env(self, **kw):
        return {**os.environ, "OCW_REPO": str(core.ROOT), "OCW_ART_HISTORY": str(self.hist),
                "OCW_TEST_OUTPUT": str(self.out),
                "OCW_TRANSCRIPTS": str(self.tmp / "no-transcripts"), "OCW_ART_PYTHON": sys.executable, **kw}

    def test_locked_run_gives_up(self):
        today = dt.date.today().isoformat()
        lock = self.hist / ".lock"
        holder = subprocess.Popen(["flock", str(lock), "sleep", "10"])
        try:
            time.sleep(0.3)
            r = subprocess.run([str(self.SCRIPT), "--no-sheets"], env=self.script_env(OCW_ART_LOCK_WAIT="1"),
                               capture_output=True, text=True, timeout=60)
        finally:
            holder.kill()
            holder.wait()
        self.assertEqual(r.returncode, 75, r.stderr)
        st = json.loads((self.out / "build-log" / today / "art.json").read_text())
        self.assertEqual(st["status"], "locked")

    def test_full_run(self):
        """gather + journal of a fixture day: status ok, media counted, log."""
        day = "2026-11-14"
        src = self.out / day
        src.mkdir(parents=True)
        (src / "101500-shot.jpg").write_bytes(b"\xff\xd8 fixture")
        (src / "101600-verdict.txt").write_text("ran on /home/builder/src/OCW\n")
        r = subprocess.run([str(self.SCRIPT), "--no-sheets", day], env=self.script_env(),
                           capture_output=True, text=True, timeout=300)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        today = dt.date.today().isoformat()
        st = json.loads((self.out / "build-log" / today / "art.json").read_text())
        self.assertEqual(st["status"], "ok")
        self.assertEqual(st["days"][day]["media"], 1)
        self.assertGreaterEqual(st["new_files"], 2)
        self.assertEqual(st["mask_check"], "ok")
        self.assertIn("art-collect", (self.out / "build-log" / today / "art.log").read_text())
        self.assertTrue((self.hist / day / "101500-shot.jpg").exists())
        self.assertTrue((self.hist / day / "journal.json").exists())
        # A second run finds nothing new (sources deduplicated by SHA-256).
        r = subprocess.run([str(self.SCRIPT), "--no-sheets", day], env=self.script_env(),
                           capture_output=True, text=True, timeout=300)
        self.assertEqual(r.returncode, 0, r.stderr)
        st = json.loads((self.out / "build-log" / today / "art.json").read_text())
        self.assertEqual(st["days"][day]["new_files"], 0)
        self.assertEqual(st["days"][day]["media"], 1)


JOURNAL_SAMPLE = [  # recorded `journalctl -o short-iso` lines (the 2026-11-15 OOM incident and others)
    "2026-11-15T00:39:18+01:00 deb systemd[5805]: ocw-build-dashboard.service: A process of this unit has been "
    "killed by the OOM killer.",
    "2026-11-15T00:39:18+01:00 deb systemd[5805]: ocw-build-dashboard.service: Main process exited, code=killed, "
    "status=9/KILL",
    "2026-11-15T00:39:18+01:00 deb systemd[5805]: ocw-build-dashboard.service: Failed with result 'oom-kill'.",
    "2026-11-15T00:39:29+01:00 deb systemd[5805]: ocw-build-dashboard.service: Scheduled restart job, restart "
    "counter is at 1.",
    "2026-11-15T00:39:47+01:00 deb systemd[5805]: tmux-spawn-75bb77d1-0461-4850-87c0-3f340ccdf0f3.scope: A process "
    "of this unit has been killed by the OOM killer.",
    "2026-11-15T00:39:56+01:00 deb systemd[5805]: tmux-spawn-75bb77d1-0461-4850-87c0-3f340ccdf0f3.scope: Failed "
    "with result 'oom-kill'.",
    "2026-11-15T00:39:50+01:00 deb kernel: Out of memory: Killed process 4242 (ffmpeg) total-vm:1234kB",
    "2026-11-15T03:00:05+01:00 deb systemd[5805]: ocw-art-collect.service: Failed with result 'exit-code'.",
    "2026-11-15T03:10:00+01:00 deb systemd[1]: some-other.service: Failed with result 'exit-code'.",
    "-- Boot 1234 --",
    "2026-11-15T04:00:00+01:00 deb systemd[5805]: Started ocw-art-collect.service.",
]


class IncidentTest(Fixture):
    DAY2 = "2026-11-15"

    def test_parse_journal(self):
        got = incidents.parse_journal(JOURNAL_SAMPLE)
        self.assertEqual([(e["time"], e["kind"]) for e in got], [
            ("00:39:18", "oom-kill"), ("00:39:29", "unit-restart"), ("00:39:47", "oom-kill"),
            ("00:39:50", "oom-kill"), ("03:00:05", "unit-failed")])
        self.assertEqual(got[0]["text"], "OOM killer stopped ocw-build-dashboard.service")
        self.assertIn("tmux scope", got[2]["text"])
        self.assertIn("ffmpeg", got[3]["text"])
        self.assertEqual(got[4]["text"], "ocw-art-collect.service failed (exit-code)")
        self.assertTrue(all(e["source"] == "journal" and e["machine"] == "deb" for e in got))

    def test_build_log_incidents_and_masking(self):
        bl = self.out / "build-log" / self.DAY2
        bl.mkdir(parents=True)

        def sample(t, online, pct, err=None):
            m = {"name": "marge", "online": online, "disks": [{"name": "home", "pct": pct}]}
            if err:
                m["error"] = err
            return json.dumps({"time": f"{self.DAY2}T{t}+01:00", "status": {"machines": [m]}})
        (bl / "servers.jsonl").write_text("\n".join([
            sample("01:00:00", True, 80), sample("01:01:00", False, 80, "ssh to buildhost.example.lan timed out"),
            sample("01:05:00", True, 91), sample("01:06:00", True, 93), sample("01:07:00", True, 80)]) + "\n")
        (bl / "janitor.jsonl").write_text(json.dumps(
            {"time": f"{self.DAY2}T02:00:00+01:00", "machine": "marge", "action": "deleted",
             "path": "/home/builder/src/OCW-worktree-agent-x/target", "bytes": 12e9}) + "\n")
        (bl / "runs.jsonl").write_text("\n".join(json.dumps(r) for r in [
            {"start": f"{self.DAY2}T05:00:00+01:00", "machine": "marge", "exit": 0},
            {"start": f"{self.DAY2}T05:10:00+01:00", "machine": "marge", "exit": 101},
            {"start": f"{self.DAY2}T05:20:00+01:00", "machine": "macos", "exit": 1}]) + "\n")
        got = incidents.incidents(self.DAY2, JOURNAL_SAMPLE[:1])
        kinds = [e["kind"] for e in got]
        self.assertEqual(kinds, ["oom-kill", "machine-offline", "machine-online", "disk-full", "janitor-delete",
                                 "runs-failed"])
        self.assertIn("2 failed remote.sh runs (macos 1, marge 1)", got[-1]["text"])
        text = (bl / "incidents.jsonl").read_text()
        self.assert_clean(text)
        self.assertIn("marge", text)

    def test_journal_merges_collected_and_notes(self):
        bl = self.out / "build-log" / self.DAY2
        bl.mkdir(parents=True)
        incidents.incidents(self.DAY2, JOURNAL_SAMPLE)
        (self.hist / self.DAY2).mkdir(parents=True)
        (self.hist / self.DAY2 / "incidents.md").write_text(
            "# Incidents – 2026-11-15\n\n## 00:39 – OOM on deb\n\n- **Cause:** VMs on 10.20.30.40\n")
        with mock.patch.object(journal, "commits_of", return_value=[]), \
                mock.patch.object(prompts, "tokens_of", return_value={"total": {}, "tasks": {}, "features": {},
                                                                    "models": {}}), \
                mock.patch.object(core, "all_days", return_value=[DAY]):
            j = journal.journal(self.DAY2)
        self.assertEqual(len(j["incidents"]["auto"]), 5)
        self.assertEqual(j["incidents"]["noted"], ["00:39 – OOM on deb"])
        md = (self.hist / self.DAY2 / "journal.md").read_text()
        self.assertIn("## Incidents", md)
        self.assertIn("### 00:39 – OOM on deb", md)
        self.assert_clean(md)
        self.assertEqual(journal.incident_text(j, "00:39"), "OOM on deb")
        self.assertEqual(journal.incident_text(j, "03:00"), "ocw-art-collect.service failed (exit-code)")
        self.assertEqual(journal.incident_text(j, "00:39", "custom"), "custom")

    def test_incidents_md_is_tracked_and_checked(self):
        self.assertIn("incidents.md", mask.TRACKED_DAY)
        (self.hist / self.DAY2).mkdir(parents=True)
        (self.hist / self.DAY2 / "incidents.md").write_text("## 00:39\n\nssh builder@buildhost.example.lan\n")
        self.assertTrue(any(f.startswith(f"{self.DAY2}/incidents.md:3:") for f in mask.check_masked()))
        root = core.ART
        for rel, ignored in ((f"build-history/{self.DAY2}/incidents.md", False),
                             (f"build-history/{self.DAY2}/journal.md", False),
                             (f"build-history/{self.DAY2}/logs/build-log/incidents.jsonl", True),
                             (f"build-history/{self.DAY2}/prompts.md", True)):
            r = subprocess.run(["git", "-C", str(root), "check-ignore", "-q", "--no-index", rel])
            self.assertEqual(r.returncode == 0, ignored, rel)


class DefaultArchiveUntouchedTest(Fixture):
    """The collector run with OCW_ART_HISTORY / OCW_TEST_OUTPUT, from a copy
    of this checkout that has a real-looking archive at the default place
    (build-history/), next to a fake OCW checkout (OCW_REPO) with its own
    test-output/ and an agent worktree with media of the day: none of these
    may be read into or written by the run."""

    ENV = {"GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@example.org",
           "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@example.org",
           "GIT_AUTHOR_DATE": f"{DAY}T10:00:00", "GIT_COMMITTER_DATE": f"{DAY}T10:00:00"}

    def git_repo(self, repo: Path, files: list[str]):
        env = {**os.environ, **self.ENV}
        for cmd in (["init", "-q"], ["add", *files], ["commit", "-q", "-m", "fixture"]):
            subprocess.run(["git", "-C", str(repo), *cmd], env=env, check=True, capture_output=True)

    def real_looking_archive(self, real: Path):
        (real / DAY / "logs" / "build-log").mkdir(parents=True)
        for name, data in (("index.md", "# Build history\n"), (".lock", ""), ("SENTINEL", "do not touch\n"),
                           (f"{DAY}/090000-real-shot.jpg", "jpeg"), (f"{DAY}/journal.json", "{}\n"),
                           (f"{DAY}/logs/build-log/runs.jsonl", "{}\n")):
            (real / name).write_text(data)

    def make_repos(self) -> tuple[Path, Path]:
        art, ocw = self.tmp / "OCW-ART", self.tmp / "OCW"
        art.mkdir()
        files = ["diary.py", "bin/collect.sh", *(p.relative_to(REPO).as_posix() for p in (REPO / "ocwart").glob("*.py"))]
        for rel in files:
            (art / rel).parent.mkdir(parents=True, exist_ok=True)
            (art / rel).write_bytes((REPO / rel).read_bytes())
            (art / rel).chmod(0o755)
        self.git_repo(art, files)
        (ocw / "scripts").mkdir(parents=True)
        (ocw / "SPECIFICATION.md").write_text("# Open Cycling World\n")
        self.git_repo(ocw, ["SPECIFICATION.md"])
        self.real_looking_archive(art / "build-history")
        # Media of the day in OCW's own test-output and in a worktree.
        for leak in (ocw / "test-output" / DAY, ocw / ".claude" / "worktrees" / "agent-x" / "test-output" / DAY):
            leak.mkdir(parents=True)
            (leak / "110000-leak.jpg").write_bytes(b"\xff\xd8 must not be gathered")
        return art, ocw

    def test_overrides_keep_the_default_archive_untouched(self):
        art, ocw = self.make_repos()
        watched = {p: tree_state(p) for p in (art / "build-history", ocw / "test-output", ocw / ".claude")}
        (self.out / DAY).mkdir(parents=True)
        (self.out / DAY / "101500-shot.jpg").write_bytes(b"\xff\xd8 fixture")
        env = {**os.environ, "OCW_REPO": str(ocw), "OCW_ART_HISTORY": str(self.hist),
               "OCW_TEST_OUTPUT": str(self.out), "OCW_TRANSCRIPTS": str(self.tmp / "no-transcripts"),
               "OCW_ART_PYTHON": sys.executable}
        env.pop("OCW_ART_WORKTREES", None)
        time.sleep(0.05)  # an mtime change would be visible
        r = subprocess.run([str(art / "bin" / "collect.sh"), "--no-sheets", DAY], env=env,
                           capture_output=True, text=True, timeout=300)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        for p, before in watched.items():
            self.assertEqual(tree_state(p), before, f"{p} was changed")
        self.assertEqual((art / "build-history" / "SENTINEL").read_text(), "do not touch\n")
        # Only the fixture's own media were gathered (no leak, no real files).
        self.assertEqual(sorted(f.name for f in (self.hist / DAY).iterdir() if f.suffix == ".jpg"),
                         ["101500-shot.jpg"])
        st = json.loads((self.out / "build-log" / dt.date.today().isoformat() / "art.json").read_text())
        self.assertEqual(st["days"][DAY]["media"], 1)

    def test_sources_honour_the_overrides(self):
        """In-process: with WORKTREES off only TEST_OUTPUT is a source."""
        self.assertEqual(archive.sources(), [self.out])
        wt = self.tmp / "wt" / "agent-y" / "test-output"
        wt.mkdir(parents=True)
        core.WORKTREES = self.tmp / "wt"
        self.assertEqual(archive.sources(), [self.out, wt])


if __name__ == "__main__":
    unittest.main()


class StillsSkipTest(unittest.TestCase):
    """The day script's `timelapse_skip` keeps pictures out of the time-lapse
    and the end card's mosaic (ART-PROJECT §4); the other filters stay."""

    def test_skip(self):
        from ocwart import render
        media = [{"file": f, "kind": k} for f, k in [
            ("100000-a.jpg", "image"), ("100100-account-signed-in.jpg", "image"),
            ("100200-sheet-1.jpg", "image"), ("100300-clip.mp4", "video"),
            ("100300-clip.jpg", "image"), ("100400-b.png", "image")]]
        with mock.patch.object(render, "media_of", return_value=media):
            self.assertEqual([m["file"] for m in render.stills_of(DAY)],
                             ["100000-a.jpg", "100100-account-signed-in.jpg", "100300-clip.jpg", "100400-b.png"])
            self.assertEqual([m["file"] for m in render.stills_of(DAY, ["100100-account-signed-in.jpg"])],
                             ["100000-a.jpg", "100300-clip.jpg", "100400-b.png"])


class WithheldTest(Fixture):
    """Media listed in build-history/withheld.txt are never gathered (ART-PROJECT §2.5)."""

    def test_withheld_media_are_not_gathered(self):
        src = self.out / DAY
        src.mkdir()
        (src / "120000-account-signed-in.png").write_bytes(b"real name")
        (src / "120100-ok.png").write_bytes(b"fictional name")
        (self.hist / "withheld.txt").write_text(
            "# a test account with a real person's name\n"
            f"{DAY}/120000-account-signed-in.png  # withheld\n")
        with mock.patch.object(archive, "stamp"):
            archive.gather(DAY)
            archive.gather(DAY)  # a second run brings nothing back either
        names = sorted(f.name for f in (self.hist / DAY).iterdir() if f.is_file())
        self.assertEqual(names, ["120100-ok.png"])


class EndStatsTest(unittest.TestCase):
    """The day video's end card numbers (ART-PROJECT §2.2): compile time in
    minutes next to the build runs and hours (user 2026-11-16)."""

    def test_compile_minutes(self):
        from ocwart import render
        j = {"commits": [1, 2, 3], "merges": 1, "lines_added": 10, "images": 4, "videos": 1,
             "tests": 0, "builds": {"runs": 5, "seconds": 7200, "cargo_s": 12240}}
        stats = render.end_stats(j, {})
        self.assertIn((5, "BUILD RUNS"), stats)
        self.assertIn((2, "BUILD HOURS"), stats)
        self.assertIn((204, "COMPILE MINUTES"), stats)
        j["builds"]["cargo_s"] = 0
        self.assertNotIn("COMPILE MINUTES", [label for _, label in render.end_stats(j, {})])
