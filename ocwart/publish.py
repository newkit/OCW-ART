"""Publishing to the GitHub release build-history (ART-PROJECT §2): masked day
zips, videos, SHA256SUMS."""

from __future__ import annotations

import os
import shutil
from pathlib import Path

from . import core as C
from .core import ART_GH, log, LOGS, RELEASE, run, sha, TEXT
from .mask import _secrets, mask, write_tracked

def masked_copy(day: str) -> Path:
    """A copy of the day folder for the public zip: text files (logs, build
    log, journal, prompts) masked like the prompts (§2.3: build machines'
    hosts and users, the home directory, e-mail addresses); media are
    hard-linked. The archive itself is left as it was."""
    secrets = _secrets()
    src = C.HIST / day
    stage = C.WORK / "publish"
    dest = stage / day
    if dest.exists():
        shutil.rmtree(dest)
    for f in sorted(src.rglob("*")):
        if not f.is_file():
            continue
        t = dest / f.relative_to(src)
        t.parent.mkdir(parents=True, exist_ok=True)
        if f.suffix.lower() in TEXT | LOGS:
            t.write_text(mask(f.read_text(errors="replace"), secrets))
            shutil.copystat(f, t)
        else:
            try:
                os.link(f, t)
            except OSError:
                shutil.copy2(f, t)
    return stage


def publish(days: list[str]):
    files = []
    for d in days:
        folder = C.HIST / d
        if not folder.exists():
            continue
        z = C.HIST / f"ocw-build-history-{d}.zip"
        if z.exists():
            z.unlink()
        stage = masked_copy(d)
        run(["zip", "-q", "-r", z, d], cwd=stage)
        shutil.rmtree(stage / d)
        files.append(z)
    files += sorted(C.OUT.glob("*.mp4"))
    # Checksums of every zip and video known locally (all days, not only these).
    sums = C.HIST / "SHA256SUMS"
    write_tracked(sums, "".join(f"{sha(f)}  {f.name}\n" for f in
                                [*sorted(C.HIST.glob("ocw-build-history-*.zip")), *sorted(C.OUT.glob("*.mp4"))]))
    files.append(sums)
    for f in files:
        log(f"upload {f.name} ({f.stat().st_size / 1e6:.1f} MB)")
    ensure_release()
    run(["gh", "release", "upload", RELEASE, "-R", ART_GH, "--clobber", *files])


RELEASE_NOTES = (
    "The OCW Build Diary (https://github.com/newkit/OCW-ART): a video per build day of Open Cycling World "
    "(`ocw-diary-day-NN-YYYY-MM-DD.mp4`), the growing diary (`ocw-build-diary.mp4`), and the day's archive, "
    "one zip per day (`ocw-build-history-YYYY-MM-DD.zip`: screenshots, videos, sounds, logs, journal; text "
    "masked). `SHA256SUMS` lists the zips and videos; `index.md` describes the test-output files. "
    "`gallery-pages.zip` and `gallery-YYYY-MM-DD.zip` are the web gallery (thumbnails, web copies, pages), "
    "deployed to https://newkit.github.io/OCW-ART/.\n\n"
    "Not a software release. Map renders contain OpenStreetMap-derived data: © OpenStreetMap contributors "
    "(ODbL).\n")


def ensure_release():
    """Creates the release `build-history` on OCW-ART when it is missing."""
    if run(["gh", "release", "view", RELEASE, "-R", ART_GH], capture_output=True, check=False).returncode == 0:
        return
    log(f"creating the release {RELEASE} on {ART_GH}")
    run(["gh", "release", "create", RELEASE, "-R", ART_GH, "--prerelease",
         "--title", "OCW Build Diary (videos and day archives)", "--notes", RELEASE_NOTES])
