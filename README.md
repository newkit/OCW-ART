# OCW-ART – the OCW Build Diary

The art project of [Open Cycling World](https://github.com/newkit/OCW) (OCW):
it documents the whole build of OCW – every screenshot, video, sound, log,
commit, merge and test – and turns each build day into a short video, joined
into a growing diary video. The full brief and every rule are in
[docs/ART-PROJECT.md](docs/ART-PROJECT.md).

**See it:**

- **Gallery:** <https://newkit.github.io/OCW-ART/> – every picture and a
  poster frame of every video, day by day, with a lightbox.
- **Videos and day archives:** the release
  [`build-history`](https://github.com/newkit/OCW-ART/releases/tag/build-history)
  (`ocw-build-diary.mp4`, `ocw-diary-day-NN-YYYY-MM-DD.mp4`,
  `ocw-build-history-YYYY-MM-DD.zip`, `SHA256SUMS`, and the gallery's
  `gallery-*.zip`).

## Where the media live

| Where | What |
|---|---|
| `build-history/` on the dev machine | the archive: everything, full size (about 3 GB of media, growing by up to 1.4 GB per build day) |
| Git LFS of this repository | the day folders' pictures and videos, one commit per day, within a 9 GiB budget of the free plan's 10 GiB ([§2.8](docs/ART-PROJECT.md#28-pictures-and-videos-in-git-lfs-decided-by-the-user-2026-11-15)) |
| the release `build-history` | one zip per finished day (full size, text masked), the day videos, the diary, the gallery zips |
| GitHub Pages | the gallery: thumbnails, web copies and poster frames, under 900 MB ([§6](docs/ART-PROJECT.md#6-the-gallery-decided-by-the-user-2026-11-15)) |

Git tracks the masked text of the archive (`index.md`, `SHA256SUMS`, per day
`journal.md`, `journal.json`, `tokens.json`, `incidents.md`); the media go
only into LFS. Never in git or LFS: the day zips, the diary videos and the
work files (`.work/`: renders, contact sheets, the gallery).

**Clone without the media** (most clones: the code, the day scripts, the
journals) – this saves the free LFS bandwidth of 10 GiB a month:

```bash
GIT_LFS_SKIP_SMUDGE=1 git clone git@github.com:newkit/OCW-ART.git
# or once per machine: git lfs install --skip-smudge
git lfs pull --include "build-history/2026-11-14/*"   # later: one day's media
```

## Layout

```
OCW-ART/
├── diary.py               # the command line (diary.py --help)
├── ocwart/                # the Python package: core, mask, archive, prompts, incidents,
│                          # agents, features, journal, render, subtitles, music, sfx,
│                          # publish, gallery, lfs, collect, cli
├── bin/collect.sh         # the hourly collector (run by the systemd user timer)
├── systemd/               # ocw-art-collect.service / .timer
├── site/                  # the gallery's templates (page, CSS, lightbox script)
├── .github/workflows/     # gallery.yml: deploys the gallery to GitHub Pages
├── days/YYYY-MM-DD.toml   # the day scripts (story, shots, jokes)
├── assets/                # the OCW logo and Fira Mono (copies from OCW)
├── docs/ART-PROJECT.md    # the specification
├── tests/                 # unit tests (hermetic: fixture archives and repositories)
└── build-history/         # the archive (masked text tracked, media in LFS or local)
```

## Setup

Needs Python 3.11+ (`/usr/bin/python3` on Debian 13), ffmpeg with libass,
git-lfs, `zip`, the Lato font and `gh` (logged in) for fetching and
publishing. `make deps` checks them, installs ffmpeg, git-lfs and zip (apt
or dnf; on macOS it prints the `brew` line) and runs `git lfs install`. No
Rust build is involved.

The tool reads OCW from an OCW checkout: by default `../OCW` next to this
checkout. Point elsewhere with `OCW_REPO=/path/to/OCW` or with `ocw_repo` in a
git-ignored `ocw-art.toml` (copy `ocw-art.example.toml`; it also holds the
LFS settings `lfs_policy` and `lfs_budget_gib`). From OCW it reads the git
log, `SPECIFICATION.md`, `test-output/` (and the agent worktrees'), and
`config/machines.toml` through OCW's `scripts/remote.sh` for the mask list;
without a machine list it refuses to mask. The collector's status goes to
OCW's `test-output/build-log/DAY/art.json`, where OCW's build dashboard reads
it.

```bash
git clone git@github.com:newkit/OCW.git OCW
GIT_LFS_SKIP_SMUDGE=1 git clone git@github.com:newkit/OCW-ART.git OCW-ART
cd OCW-ART && make deps && make help
```

## Commands

```bash
make fetch DAY=2026-11-13     # restore a day's archive from the release (OCW-ART, else OCW's)
make gather DAY=2026-11-13    # collect the day's media and logs, write the journal
make sheets DAY=2026-11-13    # contact sheets for writing days/DAY.toml
make render DAY=2026-11-13    # the day video
make diary                    # the diary video
make publish DAY=2026-11-13   # day zip + videos + SHA256SUMS → release, then the gallery
make gallery                  # build the gallery locally (incremental); make gallery-preview
make gallery-publish          # gallery zips → release, deploy to GitHub Pages
make lfs-check                # the LFS total, the budget, the days left
make lfs-commit DAY=2026-11-13 && make lfs-push   # the day's media → Git LFS
make check                    # tracked text and media names masked? (FIX=1 masks the text)
make test                     # unit tests
make install-timer            # the hourly collector (systemd user timer, this checkout)
make timer-status
```

The art project lived in OCW until 2026-11-15
([docs/ART-PROJECT.md §5.2](docs/ART-PROJECT.md#52-history-from-ocw-to-ocw-art-2026-11-15)).

## Licence

The code (`diary.py`, `ocwart/`, `bin/`, `site/`, the tests, the Makefile, the
units and the workflow) is dual-licensed under MIT OR Apache-2.0, like OCW
([LICENSE-MIT](LICENSE-MIT), [LICENSE-APACHE](LICENSE-APACHE)). Fira Mono
keeps its own licence (OFL 1.1, `assets/fonts/OFL.txt`).

The generated media (the videos, the day archives, the gallery and the media
in LFS) show OCW renders: map renders contain OpenStreetMap-derived data,
**© OpenStreetMap contributors** (ODbL), and the attribution rules of OCW and
of each asset apply (docs/ART-PROJECT.md §2, OCW's spec §4.6).
