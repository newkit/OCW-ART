<!-- The README is generated: `make readme` (diary.py readme) fills this
     template (docs/readme/README.template.md) with the hero, the totals, the
     evolution strip (docs/readme/evolution.toml) and one section per build
     day from the day scripts and journals. Edit the template, not README.md. -->
# OCW Build Diary

**The art project of [Open Cycling World](https://github.com/newkit/OCW).**
OCW is built by a human and a crowd of AI agents, day and night.
The OCW Build Diary keeps *everything* that was made on the way: every
screenshot, video, sound, log, commit, merge and test. From it, each build
day becomes a short video (title, a time-lapse of the whole day, the story in
chapters, today's features, the numbers), and the days are joined into one
growing diary video.

{{hero}}

**▶ [Watch the whole diary](https://github.com/newkit/OCW-ART/releases/download/build-history/ocw-build-diary.mp4)** ·
**[Browse the gallery](https://newkit.github.io/OCW-ART/)** (every picture and video, day by day) ·
[Day zips and videos](https://github.com/newkit/OCW-ART/releases/tag/build-history) ·
[The brief and the rules](docs/ART-PROJECT.md)

{{totals}}

## How the game grew

{{evolution}}

## The build days

{{days}}

## How it is made

```mermaid
flowchart LR
  A[OCW test runs: screenshots, videos, sounds] --> C[hourly collector: gather and journal]
  B[git log, spec, build log, prompts, tokens] --> C
  C --> D[build-history day folders]
  D --> E[day script]
  E --> F[render: ffmpeg and synthesised music]
  F --> G[release: day video, diary, day zip]
  D --> H[gallery: thumbnails, web copies]
  H --> I[GitHub Pages]
  D --> J[Git LFS: pictures and videos]
```

1. **Collect** (every hour, a systemd timer): every picture, video, sound and
   log of OCW's test runs is gathered into `build-history/DAY/`, with its
   capture time; the journal adds commits, merges, spec versions, builds,
   prompts, token usage, incidents and the day's features. All text is
   masked (no hosts, users, home paths, e-mail or private addresses).
2. **Write** the day's story: `days/DAY.toml` picks the chapters, shots, captions
   and jokes from the journal and the contact sheets – facts only.
3. **Render** the day video with ffmpeg: Ken Burns stills, clips, splits,
   sticker notes, a time-lapse with a running clock and the commit log, the
   features roll and the end card; music and sound effects are synthesised
   by the tool (a style per day). Then the diary is rebuilt.
4. **Publish**: the day zip and the videos go to the release, the gallery to
   GitHub Pages, the pictures and videos into Git LFS, and this README is
   regenerated.

## Layout

```
OCW-ART/
├── diary.py               # the command line (diary.py --help)
├── ocwart/                # the Python package: core, mask, archive, prompts, incidents,
│                          # agents, features, journal, render, subtitles, music, sfx,
│                          # publish, gallery, lfs, readme, collect, cli
├── bin/collect.sh         # the hourly collector (run by the systemd user timer)
├── systemd/               # ocw-art-collect.service / .timer
├── site/                  # the gallery's templates (page, CSS, lightbox script)
├── .github/workflows/     # gallery.yml: deploys the gallery to GitHub Pages
├── days/YYYY-MM-DD.toml   # the day scripts (story, shots, jokes)
├── assets/                # the OCW logo and Fira Mono (copies from OCW)
├── docs/ART-PROJECT.md    # the specification; docs/readme/ this README's template
├── tests/                 # unit tests (hermetic: fixture archives and repositories)
└── build-history/         # the archive (masked text tracked, media in LFS or local)
```

## Where the media live

| Where | What |
|---|---|
| `build-history/` on the dev machine | the archive: everything, full size |
| Git LFS of this repository | the day folders' pictures and videos, one commit per day, within a 9 GiB budget of the free plan's 10 GiB ([§2.8](docs/ART-PROJECT.md#28-pictures-and-videos-in-git-lfs-decided-by-the-user-2026-11-15)) |
| the release [`build-history`](https://github.com/newkit/OCW-ART/releases/tag/build-history) | one zip per finished day (full size, text masked), the day videos, the diary, the gallery's zips |
| [GitHub Pages](https://newkit.github.io/OCW-ART/) | the gallery: thumbnails, web copies and poster frames, under 900 MB ([§6](docs/ART-PROJECT.md#6-the-gallery-decided-by-the-user-2026-11-15)) |

Git tracks the archive's masked text (`index.md`, `SHA256SUMS`, per day
`journal.md`, `journal.json`, `tokens.json`, `incidents.md`); the media go
only into LFS. Never in git or LFS: the day zips, the diary videos and the
work files (`.work/`).

**Clone without the media** (the code, the day scripts, the journals) – this
saves the free LFS bandwidth of 10 GiB a month:

```bash
GIT_LFS_SKIP_SMUDGE=1 git clone https://github.com/newkit/OCW-ART.git
# or once per machine: git lfs install --skip-smudge
git lfs pull --include "build-history/2026-11-14/*"   # later: one day's media
```

## Setup and commands

Needs Python 3.11+, ffmpeg with libass, git-lfs, `zip`, the Lato font and
`gh` (logged in). `make deps` checks them, installs ffmpeg, git-lfs and zip
(apt or dnf; on macOS it prints the `brew` line) and runs `git lfs install`.
The tool reads OCW from a checkout next to this one (`../OCW`; `OCW_REPO` or
`ocw_repo` in a git-ignored `ocw-art.toml` point elsewhere).

```bash
git clone https://github.com/newkit/OCW.git OCW
GIT_LFS_SKIP_SMUDGE=1 git clone https://github.com/newkit/OCW-ART.git OCW-ART
cd OCW-ART && make deps && make help

make gather DAY=2026-11-13    # collect the day's media and logs, write the journal
make sheets DAY=2026-11-13    # contact sheets for writing days/DAY.toml
make render DAY=2026-11-13    # the day video
make diary                    # the diary video
make publish DAY=2026-11-13   # day zip + videos → release, the gallery, this README
make gallery                  # the gallery locally (make gallery-preview)
make readme                   # regenerate this README
make lfs-check                # the LFS total, the budget, the days left
make lfs-commit DAY=2026-11-13 && make lfs-push   # the day's media → Git LFS
make check                    # tracked text, README and media names masked?
make test                     # unit tests
make install-timer            # the hourly collector (systemd user timer)
```

The art project lived in OCW until 2026-11-15
([docs/ART-PROJECT.md §5.2](docs/ART-PROJECT.md#52-history-from-ocw-to-ocw-art-2026-11-15)).

## Licences and credits

- **Code** (`diary.py`, `ocwart/`, `bin/`, `site/`, the tests, the Makefile,
  the units and the workflow): MIT OR Apache-2.0, like OCW
  ([LICENSE-MIT](LICENSE-MIT), [LICENSE-APACHE](LICENSE-APACHE)).
- **Fonts:** Fira Mono (SIL Open Font License 1.1, `assets/fonts/OFL.txt`;
  © 2012-2015 The Mozilla Foundation and Telefonica S.A.); Lato (SIL OFL 1.1,
  from the system).
- **Map data:** the world renders contain OpenStreetMap-derived data,
  **© [OpenStreetMap contributors](https://www.openstreetmap.org/copyright)**
  (ODbL). The attribution rules of OCW and of each of its assets apply
  (OCW's spec §4.6).
- **Music and sound effects:** synthesised by the tool itself – no samples.
- **The pictures and videos** are renders of Open Cycling World, made while
  building it.
