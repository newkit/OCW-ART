# OCW-ART – the OCW Build Diary

The art project of [Open Cycling World](https://github.com/newkit/OCW) (OCW):
it documents the whole build of OCW – every screenshot, video, sound, log,
commit, merge and test – and turns each build day into a short video, joined
into a growing diary video. The full brief and every rule are in
[ART-PROJECT.md](ART-PROJECT.md).

**Watch:** the videos and the day archives are on the release
[`build-history`](https://github.com/newkit/OCW-ART/releases/tag/build-history)
(`ocw-build-diary.mp4`, `ocw-diary-day-NN-YYYY-MM-DD.mp4`,
`ocw-build-history-YYYY-MM-DD.zip`, `SHA256SUMS`).

## What is here

| Path | What |
|---|---|
| `diary.py` | the tool: gather, journal, contact sheets, render, diary, publish, the hourly collector, the mask check |
| `music.py`, `features.py` | the synthesised music; the features log of the journal |
| `test_*.py` | unit tests (hermetic: a fixture archive, no network, no ffmpeg) |
| `collect.sh`, `systemd/` | the hourly collector and its systemd user timer |
| `days/YYYY-MM-DD.toml` | the day scripts (story, shots, jokes) |
| `build-history/` | the archive: media git-ignored, masked text tracked (`index.md`, `SHA256SUMS`, per day `journal.md`, `journal.json`, `tokens.json`, `incidents.md`) |
| `assets/` | the OCW logo and Fira Mono, copied from OCW |

## Setup

Needs Python 3.11+ (`/usr/bin/python3` on Debian 13), ffmpeg with libass,
`zip`, the Lato font and `gh` (logged in) for fetching and publishing. No Rust
build is involved.

The tool reads OCW from an OCW checkout: by default `../OCW` next to this
checkout. Point elsewhere with `OCW_REPO=/path/to/OCW` or with `ocw_repo` in a
git-ignored `ocw-art.toml` (copy `ocw-art.example.toml`). From OCW it reads
the git log, `SPECIFICATION.md`, `test-output/` (and the agent worktrees'),
and `config/machines.toml` through OCW's `scripts/remote.sh` for the mask
list; without a machine list it refuses to mask. The collector's status goes
to OCW's `test-output/build-log/DAY/art.json`, where OCW's build dashboard
reads it.

```bash
git clone git@github.com:newkit/OCW.git OCW
git clone git@github.com:newkit/OCW-ART.git OCW-ART
cd OCW-ART && make help
```

## Use

```bash
make fetch DAY=2026-11-13     # restore a day's archive from the release (OCW-ART, else OCW's)
make gather DAY=2026-11-13    # collect the day's media and logs, write the journal
make sheets DAY=2026-11-13    # contact sheets for writing days/DAY.toml
make render DAY=2026-11-13    # the day video
make diary                    # the diary video
make publish DAY=2026-11-13   # day zip + videos + SHA256SUMS → release build-history
make check                    # tracked text masked? (FIX=1 masks)
make test                     # unit tests
make install-timer            # the hourly collector (systemd user timer, this checkout)
make timer-status
```

Moving from OCW (where the art project lived until 2026-11-15) is described
in [ART-PROJECT.md §5.2](ART-PROJECT.md#52-moving-to-ocw-art-2026-11-15).

## Licence

The code (`diary.py`, `music.py`, `features.py`, the tests, `collect.sh`, the
Makefile, the units) is dual-licensed under MIT OR Apache-2.0, like OCW
([LICENSE-MIT](LICENSE-MIT), [LICENSE-APACHE](LICENSE-APACHE)). Fira Mono
keeps its own licence (OFL 1.1, `assets/fonts/OFL.txt`).

The generated media (the videos and the day archives) show OCW renders: map
renders contain OpenStreetMap-derived data, **© OpenStreetMap contributors**
(ODbL), and the attribution rules of OCW and of each asset apply
(ART-PROJECT.md §2, OCW's spec §4.6).
