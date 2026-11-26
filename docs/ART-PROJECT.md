# OCW Build Diary – Art Project Specification

Version 3.3 – 25 November 2026

| Version | Change |
|---|---|
| 1.0 | The brief, the diary format, the media archive, the tool (`art/diary.py`), day scripts for 11 and 12 November 2026 |
| 1.1 | Every photo and video carries its ISO 8601 date and time, in the file and in the picture (§2.1) |
| 1.2 | The build process itself is documented: every build/test run on the build machines and the build servers' state (§2.2) |
| 1.3 | The user's prompts are part of the archive and the videos (§2.3) |
| 1.4 | Token usage of the build: in total, per task and per feature (§2.4) |
| 1.5 | The archive moved to `art/build-history/`; its text files (index, checksums, journals, token usage) are tracked in git, masked, while media stay out of git (§2, §2.5). An hourly collector on the dev machine, a systemd user timer: gather + journal of yesterday and today, the mask check, the contact sheets at 23:xx, a lock, a status file, a dashboard line (§5.1). Day videos: images stay on screen about 1.4× longer (3–5 s), and shots run in capture order within a chapter (§3, §4). All decided by the user 2026-11-14 |
| 1.6 | Music with more variety and a style per day (user 2026-11-14): synthwave, funk, lofi, chiptune, house (`style` and `mode` in the day script, else picked by the day number). It varies within the video: a progression, drum pattern, bass line and arpeggio per chapter; fills, build-ups and stops at chapter changes; crashes, a breakdown, a bridge and a key lift in long videos; a developing lead (motif, variations, call and response); and swells. Deterministic, loudness-normalised, tested (`art/music.py`, §3.2, §4) |
| 1.7 | Incident log (user 2026-11-15, §2.6): the hourly collector gathers OOM kills, failed and restarted units (journalctl), machines offline / online, full disks, janitor deletions and failed runs into `test-output/build-log/DAY/incidents.jsonl` (masked). The coordinator writes root-cause notes to `DAY/incidents.md` (tracked, masked). The journal merges both under "Incidents", and a day script can show an incident as a card (`incident = "HH:MM"`, §4). First entry: the 2026-11-15 00:39 OOM on deb |
| 1.8 | Features and agent jobs (user 2026-11-15, §2.7): the journal lists the day's spec rows with the merge that landed each, its marge check (suites, passed, failed), deploys (`deploys.jsonl` from `deploy-test.sh`) and releases. Agent jobs come from the coordinator's `agents.jsonl` (`diary.py agent-event`, `agent-backfill`). The day video closes with a "Today's features" roll (`features_roll`, §4). `remote.sh` logs each run's commit |
| 1.9 | **Own repository** (user 2026-11-15: "Use this repository for everything ART related", "also move the build-history to the new art project location"): the art project moved out of OCW into [newkit/OCW-ART](https://github.com/newkit/OCW-ART), with the history of OCW's `art/`. The former `art/` is its root; `scripts/art-collect.sh` is `collect.sh`; the `make art-*` targets are `make gather`, `render`, … in OCW-ART. The tool reads OCW from outside (`OCW_REPO`, else `ocw_repo` in `ocw-art.toml`, else `../OCW`): git log, `SPECIFICATION.md`, `test-output/`, `config/machines.toml` (§5). The archive is OCW-ART's `build-history/` (§2, §5.2: how it moves). New videos and day zips go to the release `build-history` of OCW-ART, where days 1–4 were copied; OCW's release keeps the README images. Logo and Fira Mono are copied into `assets/`. The status file stays in OCW's `test-output/build-log/DAY/art.json`, so the build dashboard is unchanged. The regional reference boards (`reference/`) serve OCW's world look and stay in OCW, now `docs/reference/` |
| 2.0 | **Restructure, gallery, Git LFS** (user 2026-11-15: "looks a bit unstructured. Re-structure and cleanup"; "I miss seeing the actual photos and videos"; "add the fotos and videos into the free git LFS"; git-lfs "to the build dependencies where it fits"). Layout (§5): the code is the package `ocwart/` (the former 2,400-line `diary.py` split into `core`, `mask`, `archive`, `prompts`, `incidents`, `agents`, `journal`, `subtitles`, `sfx`, `render`, `publish`, `collect`, `cli`, plus `music`, `features` and the new `gallery`, `lfs`); `diary.py` stays the command; `collect.sh` is `bin/collect.sh` (the timer was reinstalled); tests in `tests/`, this document in `docs/`, the gallery's templates in `site/`. The check for the archive at its old place in OCW is gone (the move is done). **Gallery** (§6): a static site of every picture and video poster, day by day, on GitHub Pages of OCW-ART, built on the dev machine and deployed by a workflow from small gallery zips on the release, under a size budget (900 MB; the oldest days get smaller web copies first, then thumbnails only); `make publish` refreshes it. **Git LFS** (§2.8): the day folders' pictures and videos, one commit per day, within a 9 GiB budget of the free plan's 10 GiB, policy `all` or `pictures`; day zips, diary videos and `.work/` stay out. `make deps` installs ffmpeg and git-lfs; `check-masked` also checks the media file names. **README** (§5.3, user: "a nice overview (visually) over the project, the evolution and the build days"): generated by `diary.py readme` from a template, the evolution strip and the journals; `make publish` refreshes it |
| 2.1 | `timelapse_skip` in the day script (§4): pictures left out of the time-lapse and the end card's mosaic – first used on day 5 for three early sign-in screenshots that showed a real cyclist's name as the test account |
| 2.2 | **Withheld media** (§2.5, user 2026-11-16): `build-history/withheld.txt` keeps listed pictures out of gather, journal, day zip, gallery and Git LFS; day 5's three sign-in screenshots with a real cyclist's name are withheld and removed from the published gallery. **Decision titles** (§2.7): decision rows show what was decided, not "Decision by the user" |
| 2.3 | **Compile time on the end card** (§2.2, user 2026-11-16: "record also compile time"): COMPILE MINUTES – cargo's time of the day's build runs – next to BUILD RUNS and BUILD HOURS; the journal already lists it per machine |
| 2.4 | **Day 6 fixes** (2026-11-17): the transcripts also come from the project folder of the directory holding the OCW checkout (on deb since the move: `~/src`, where the coordinator runs; day 6 had 22 of its 63 prompts without it, §2.3); private words in the git-ignored `ocw-art.toml` (`mask_users`: the coordinator's former user, `mask_names`: a real person's name in a prompt) are masked too, and the day-5 journal's former user was masked (§2.5); `timelapse_skip` takes shell patterns and a plain card its own `text` (§4); the collector's unit sets `TMPDIR=%h/tmp` (§5.1) |
| 2.5 | **`darkchip`, a cooler 8-bit style** (user 2026-11-17 on day 6: "less squeeky and less happy. make something cooler with different drums styles"): dorian or phrygian, a rounded low-passed pulse lead in the middle register, slow triangle arpeggios, a solid square/triangle bass with a sine sub, a darker soft kit with a rim click, and a drum style per chapter in turn (half-time, four-on-the-floor with an open hat, 2-step, half-time break; kick and rim in the breakdown) with tom fills into the chapters (§3.2). A still can push in on a detail (`focus = [x, y, zoom]`, §4) |
| 2.6 | **`melodic-deep-house`** (user 2026-11-18 for day 7: "use music style: melodic deep house"): minor with 7th and 9th chords (e.g. F minor), 120–124 bpm, a four-on-the-floor kit with soft off-beat open hats, the clap (or a rim) on 2 and 4 and shaker ghosts, a warm sine-sub bass with a little low-passed saw, lush detuned pads whose filter opens over every 4-bar phrase, a mellow plucked arpeggio and an FM lead, both with a dotted-8th delay; build-ups into the chapters, a kick-less breakdown, no key lift (§3.2). Withheld on day 7 (§2.5): a whole-desktop capture of Weela and the build dashboard's battery screenshots, which show a user name |
| 2.7 | **CO2 footprint of the tokens (planned, not built)** (user 2026-11-18: "estimate also the co2 footprint for the token usage and log that and show it in the video"; §2.4.1): an estimate with a range from the token counts of §2.4 × energy per token kind (output, input, cache writes, cache reads) × data-centre overhead × grid carbon intensity, cited factors in `co2.toml`; logged in `tokens.json` and the journal, shown on the end card with a plain comparison; open Q1 (which figures), Q2 (also the build machines?), Q3 (which comparison) |
| 2.8 | **`liquid-dnb`** (day 8, 2026-11-19; the end-of-day video's style is picked to differ from the days before: day 6 darkchip, day 7 melodic deep house): liquid drum & bass, dorian with 7th and 9th chords (e.g. G dorian), 170–174 bpm, the two-step breakbeat (kick on 1 and the "and" of 3, the snare on 2 and 4) with ghost snares and shuffled 16th hats, a drum style per chapter in turn (two-step, rolling, ride, half-time; hats and rim in the breakdown), a reese bass (two detuned low-passed saws) over a sine sub in long rolling notes, FM-Rhodes chords, an airy detuned pad whose filter opens over each phrase, a sparse FM lead with a dotted-8th delay (§3.2). Withheld on day 8 (§2.5): the build dashboard's two battery screenshots of 00:00, which show the coordinator's user name |
| 2.9 | **`electro`** (day 9, 2026-11-19, the busiest day yet; a style unlike days 6–8): 808 electro-funk, phrygian (e.g. E phrygian, the bII chord), 124–128 bpm, the broken 808 beat (kick on 1, the "a" of 2 and the "and" of 3, never four on the floor; the clap on 2 and 4; 16th hats, a rim like a cowbell), a drum style per chapter in turn, a booming 808 bass (a sine dropping into its pitch, a little drive) in syncopated 16ths, a sequenced saw arpeggio, a pulse lead with a delay (§3.2). Nothing withheld on day 9 (1,380 pictures checked). **A day without tokens** (day 10, 2026-11-20: the weekly token limit was reached the evening before; no commits, no prompts, no pictures; §4.1): `diary.py crab DAY` draws the diary's own pictures – an ASCII crab in the terminal's orange turning its trouser pockets inside out, a moth and dust flying out, the token counter running down to 0 – as a clip and stills in the day folder; **`ambient`**, a quiet bed without drums (lydian 7th/9th chords, a sine drone, a music-box arpeggio and lead, a slow pad); the day script can drop the time-lapse (`timelapse = false`) and set the end card's numbers (`stats`); a day with a day script but no commits keeps its day number (§4) |
| 3.0 | **`trance`** (day 11, 2026-11-21, the day the tokens came back; a style unlike days 6–10): uplifting trance, aeolian (e.g. A minor, i–VI–III–VII), 136–140 bpm, four on the floor with the open hat on every off-beat and the clap on 2 and 4, a drum style per chapter in turn (trance, driving 16ths, rim and shaker, half-time lift), a rolling bass – three saw 16ths after every kick, never on the beat –, a gated detuned supersaw pad whose filter opens over each phrase, a plucked 16th arpeggio with an echo and a saw lead with vibrato (§3.2). Day 11 withholds one picture: Host a ride's join link showing the build machine's private network address (§2.5) |
| 3.1 | **`dub`** (day 12, 2026-11-22, the day of smooth junctions and smooth riders; a style unlike days 6–11): roots dub, dorian (e.g. D dorian, i–IV), 72–76 bpm with swung 16ths, the one-drop beat (kick and rim together on the third beat, nothing on the one), a drum style per chapter in turn (one drop, rockers, steppers, a half-drop with the open hat), a round melodic sub bass that leaves the downbeat to the drop, the skank – short plucked chord chops on 2 and 4 – with a dotted-8th echo (chord stabs can now have an echo), a sustained organ, a reedy melodica-like pulse lead with a long delay, dub stops at chapter changes; rim and hats alone in the breakdown (§3.2) |
| 3.2 | **`garage`** (day 13, 2026-11-23, the day the riders left the road; a style unlike days 6–12): UK garage, 2-step, minor with 7th and 9th chords (e.g. C minor), 130–134 bpm with heavily swung 16ths, the 2-step beat (the kick on the one and skipping past the third beat, the snare on 2 and 4, shuffled hats with ghosts), a drum style per chapter in turn (2-step, 2-step with a rim, speed garage – four on the floor with the open hat off the beat –, half-time), a bouncing sub bass that skips with the kick and leaves gaps, chopped Rhodes-like chord stabs, a plucked lead with an echo like a cut-up vocal; hats and rim in the breakdown (§3.2). Feature titles of "Built: …" / "Fixed: …" rows keep an acronym's case ("Built: OCW Studio edits model files", not "oCW") |
| 3.3 | **`acid`** (day 14, 2026-11-24, the day of smooth road sides and the first WebXR build for a headset; a style unlike days 6–13): acid house / acid techno, minor with 7th chords (e.g. F minor), 126–130 bpm, a squelching 303-like bass – a saw through a resonant low-pass whose cutoff snaps open on every note and closes again – in 16ths with octave jumps, a 909-like kit with a drum style per chapter in turn (four on the floor with the open hat off the beat, a jacking variant with a 16th ride and an extra kick, a broken break, a half-time stomp), dry minor stabs off the beat, a hollow square lead with an echo; open hats and hats in the breakdown (§3.2). **Decision rows that start with the decision** (OCW's rule since 2026-11-16: "**The browser app is built with WebAssembly SIMD …** (decision by the user, 2026-11-24; Phase 10 Q10 (a); …)") get "Decided: Phase 10 Q10 – the browser app is built with …" too (§2.7); the question is the one named after the parenthesis' first ";", none when it names only sections. A name with inner capitals keeps its case ("WebXR", not "webXR") |

## 1. The brief

The art project documents the **entire build process of Open Cycling World**:
every step, with images, videos, text and audio. Every commit, merge and test
is part of the story. From this material a video is made for **every build day**,
and the days are joined into a growing **diary**: each new day is added after the
day before, so the diary video tells the whole story from the first commit to today.
Each day's video is also kept on its own.

Tone and style:

- **Cool and stylish**: a clear visual identity (the app's colours and fonts),
  confident typography, motion that serves the story.
- **Funny**: dry, affectionate humour about the build, the bugs, the riders and the
  agents who never sleep. It never mocks real people, and it doesn't invent facts:
  every joke is about something that really happened that day (commits, tests,
  pictures).
- **Appealing to the viewer**: short (about 1.5–3 minutes per day), fast
  but readable, music and sound, a story arc per day.
- **Time-lapse elements**: the whole day is compressed into a time-lapse
  (every picture in order, the clock running, the commits scrolling by),
  and video shots can be sped up (with a "TIME-LAPSE ×N" badge).

The source text of this brief (the user's own words, 12 November 2026):

> I want to create an Art Project on the entire Build Process of this OCW App.
> Therefore it is super important to document every step we do with images,
> videos, text and audio. Every merge, commit and test is interesting as well.
> […] create a video which documents the evolution of the world, the riders,
> the images, the landscapes and such. […] for every build day, adding each new
> day to the previous video from the day before, so that it becomes like a diary.
> Also keep the per day video separately as well. Use a cool and stylish way of
> story telling and make it funny too. Make it appealing to the viewer. Use some
> time lapse elements.

## 2. What is documented (the archive)

**Everything** made while building OCW is kept; nothing is curated away. The
selection happens only in the video.

| Kind | Source | Kept as |
|---|---|---|
| Screenshots (single pictures; comparisons only as `-compare-` images) | test runs (`test-output/`, agent worktrees), scene harness | `YYYY-MM-DD/HHMMSS-label.png` |
| Videos | `--capture` recordings, scenes, multiplayer kiosk/camera | `YYYY-MM-DD/HHMMSS-label.mp4` |
| Audio | game-audio demos (`.wav`) | `YYYY-MM-DD/HHMMSS-label.wav` |
| Text | test verdicts and summaries (`.txt`) | `YYYY-MM-DD/HHMMSS-label.txt` |
| Logs | app/server/bot logs, run args, route files | `YYYY-MM-DD/logs/…` |
| Commits, merges, spec versions, tests | git history | `YYYY-MM-DD/journal.md` + `journal.json` |

- **Pictures stand alone (decided by the user 2026-11-14, spec §11.4 v3.25):** every
  screenshot and frame is kept (and sent to the user) as its own file, exactly as
  rendered with its timestamp – no grids or contact sheets made of several shots.
  A joined image is made only to show a comparison (before / after, two settings,
  two dates or places side by side); it is kept as well, next to the single pictures,
  labelled `…-compare-….jpg`.
- **Where:** `build-history/YYYY-MM-DD/` of the OCW-ART checkout on the dev
  machine (until 2026-11-15: `art/build-history/` of the OCW checkout, until
  2026-11-14 `artwork/build-history/`). Its text files are tracked, masked
  (§2.5). Since v2.0 the day folders' pictures and videos go into **Git LFS**
  of OCW-ART, one commit per day, within a budget (§2.8). They never go into
  plain git, and never into OCW (OCW spec §11.3; OCW's history was
  rewritten on 2026-11-12 to remove them).
- **Seen:** in the gallery on GitHub Pages, <https://newkit.github.io/OCW-ART/>
  (§6): every picture and a poster frame of every video, day by day.
- **Published:** one zip per day, `ocw-build-history-YYYY-MM-DD.zip`, on the GitHub
  release [`build-history`](https://github.com/newkit/OCW-ART/releases/tag/build-history) of OCW-ART,
  next to the videos. `diary.py fetch` (`make fetch DAY=…`) restores a day on
  another machine. It looks on OCW-ART's release first, then on OCW's
  [`build-history`](https://github.com/newkit/OCW/releases/tag/build-history),
  which still has days 1–4 (and OCW's README images, which stay there).
  The zip's text files (logs, build log, journal, prompts) are masked like the
  prompts (§2.3: build machines' hosts and users, the home directory, e-mail
  addresses, private IP addresses); the local archive keeps the originals.
- **Time** of a file: the `HHMMSS-` prefix (local time of the run), else the time
  in its folder name, else its modification time. Commits use local time as well.
- Identical files (same SHA-256) are kept once.

### 2.1 Date and time on every photo and video

Every photo and video carries its **ISO 8601 date and time** (local time with
UTC offset, e.g. `2026-11-12T22:14:05+01:00`) twice:

- **In the picture:** the app draws it in the in-game HUD's **top-right corner**
  on every screenshot and every video frame, also when the HUD is otherwise
  off (spec §3.2). In frame-exact `--capture` videos it is the capture start
  plus the video time.
- **In the file:** PNG `tEXt` chunk `Creation Time` (plus `Software`); MP4
  `creation_time` (UTC, the start of the recording). The diary videos carry
  their render time.
- **Older material** (made before this rule): `diary.py stamp` (run by
  `gather`) writes the capture time from the file name into the archive copy's
  metadata; the picture itself is left as it was taken.

### 2.2 The build process: runs, build times, errors, build servers

The build infrastructure is part of the story, so it is recorded continuously,
in `test-output/build-log/YYYY-MM-DD/` of the OCW main checkout (git-ignored;
gathered into the day folder's `logs/build-log/`):

| File | Written by | Content |
|---|---|---|
| `runs.jsonl` | `scripts/remote.sh run` (every build / test run on a build machine, by people and agents) | one JSON line per run: start (ISO 8601), seconds (including any wait for a build slot), machine, OS, checkout, branch, command, exit code, log file |
| `HHMMSS-MACHINE-PID.log` | `scripts/remote.sh run` | the run's full output (stdout + stderr): build times, warnings, test results, **errors** |
| `servers.jsonl` | the build dashboard (`make dashboard-install`; every 60 s) | the build servers' state: online / offline, CPU, memory, disk, running and queued tasks, build slots |

- **Privacy:** host names, addresses, user names and key paths are replaced by
  the machine's name before anything is written (the dashboard masks too).
- **Journal:** `diary.py journal` adds "Builds and build servers" to the day's
  `journal.md`: runs, build hours, failures with their commands and logs, the
  longest runs, each server's online share and the **compile time** (cargo's
  time and the crates compiled, per machine and in total). The day video's end
  card shows BUILD RUNS, BUILD HOURS and COMPILE MINUTES (user 2026-11-16:
  "record also compile time").
- `OCW_BUILD_LOG=0` turns the run log off for a single command.

### 2.3 The prompts

The user's prompts to Claude Code (the conversation that builds OCW) are part
of the story.

- **Source:** the Claude Code session transcripts of the project
  (`~/.claude/projects/*OCW*/*.jsonl`, and the project of the directory that
  holds the OCW checkout, on deb `-home-claude-src` since the move;
  `OCW_TRANSCRIPTS` overrides the root): the
  user's own messages, including those sent while Claude was working; not the
  agents' messages, tool output or notifications; slash commands as `/name args`.
- **Kept as:** `DAY/prompts.jsonl` (time, ISO 8601, text) and `DAY/prompts.md`;
  the journal lists them. `diary.py prompts DAY` (run by `journal`).
- **Masked** before they are written: every build machine's host and user name,
  e-mail addresses, private IP addresses and the home directory. The day zips are public.
- **In the video:** during the time-lapse each prompt pops up as a chat bubble
  ("YOU · 08:58") when its time comes (at most one new bubble per 1.2 s; the
  newest wins); a chapter can quote the prompt that started it (`prompt = "…"`
  in the day script, shown as "YOU ASKED"); the end card counts PROMPTS.

### 2.4 Token usage

How much model work went into the build is part of the record too.

- **Source:** every assistant message in the project's Claude Code
  transcripts: the main session and every agent
  (`subagents/agent-*.jsonl` with its `meta.json`). Each message is counted
  once (de-duplicated by message id), on the local day of its timestamp.
- **Counted:** uncached input, cache writes, cache reads and output tokens,
  their sum ("tokens"), and the number of model messages; per model too.
- **Per task:** an agent's task description (e.g. "agent: Fix wheels sinking
  into road"); the main session's work under the user prompt it answered
  ("coordination: <prompt>", masked like the prompts, §2.3).
- **Per feature:** tasks are grouped by keywords (`FEATURES` in `diary.py`:
  art project, materials & look, menus, sky & time, audio, multiplayer,
  riders, worlds & terrain, build & infra, planning; the first match wins).
- **Kept as:** `DAY/tokens.json`; the journal has a "Token usage" section
  (per feature, the 40 biggest tasks); the day video's end card shows
  MILLION TOKENS. `diary.py tokens DAY` (run by `journal`).
- Most of the total is cache reads (the conversation re-read from the cache
  on every step); output tokens are about 0.2 % of it.

#### 2.4.1 The CO2 footprint of the tokens (planned, user 2026-11-18; not built)

The user (2026-11-18): "estimate also the CO2 footprint for the token usage and
log that and show it in the video".

- **What is estimated:** the greenhouse-gas emissions (kg CO2e) of the model
  work counted in §2.4 – per day, per task and feature, and in total. It is an
  **estimate with a range**, never shown as an exact number: the provider does
  not publish energy per token, so the result comes from published estimates
  and assumptions, all of them written down.
- **The model (proposal):** energy = Σ tokens of each kind × energy per million
  tokens of that kind, per model; × the data centre's overhead (PUE); ×
  the grid's carbon intensity (g CO2e per kWh) = CO2e.
  - The token kinds of §2.4 cost very differently: output tokens (generated
    one by one) far more than uncached input (processed in parallel), cache
    writes about like input, **cache reads much less** (most of our total
    is cache reads, so this factor decides most of the result).
  - Each factor gets a **low / central / high** value with its source
    (published measurements and estimates of inference energy per token or
    per prompt for large models, e.g. papers and reports on LLM inference
    energy, the providers' own disclosures where they exist; PUE and grid
    intensity from the data-centre regions' public figures). The values are
    researched and cited when this is built, kept in a small config file
    (`co2.toml`, with the sources as comments), and the journal says which
    version of the factors a day used, so later better figures can recompute
    old days.
- **Logged:** `DAY/tokens.json` gains the estimate (central, low, high; per
  model, per task and feature, and the factors' version); the journal's
  *Token usage* section shows it next to the tokens; `diary.py tokens DAY`
  computes it; the README's totals line and the day's README section show
  the day's and the project's total.
- **In the video:** the end card shows it next to MILLION TOKENS, e.g. "≈ 12 kg
  CO2e (5–30)" and a plain comparison (e.g. "≈ 80 km by car" or "≈ N hours
  of a laptop", with the comparison's source); the diary video's end card
  the running total.
- **Tests:** the arithmetic per token kind and model, the range, a day without
  transcripts, the recompute with new factors, the end card's text.
- **Open questions:**
  - **Q1 (open) – Which figures:** which published sources to use for energy
    per token and for the data centres (to be researched and proposed with
    citations before building), and whether to show only the range or a
    central value with it.
  - **Q2 (open) – Only the tokens, or the build too:** also estimate the
    electricity of the build machines and the coordinator (compile hours of
    §2.2 × each machine's typical power, the local grid's intensity), shown
    separately?
  - **Q3 (open) – The comparison:** car kilometres, laptop hours, kettle
    boils, or none?

### 2.5 Text in git (decided by the user 2026-11-14)

The archive's text record is versioned with the code; its media are not in
plain git (since v2.0 the day folders' pictures and videos are in Git LFS, §2.8).

| In `build-history/` | Git |
|---|---|
| `index.md`, `SHA256SUMS` | **tracked** |
| `withheld.txt` | **tracked**: media withheld from the archive (below) |
| per day `journal.md`, `journal.json`, `tokens.json` | **tracked** |
| the day folders' pictures and videos (jpg, jpeg, png, webp, mp4, webm, mkv) | **Git LFS**, per day within the budget (§2.8); the rest ignored |
| other media (wav, gif …), the day zips, `diary/*.mp4` | ignored (GitHub release `build-history`) |
| per day `logs/` (unmasked originals), `prompts.*` (published masked in the zip), `.txt` verdicts | ignored |
| `.work/` (render, contact-sheet and gallery files), `.lock` | ignored |

- `.gitignore` ignores `/build-history/**` and re-includes exactly the
  tracked files above, plus the media of the days in Git LFS (the managed
  `lfs-days` block, §2.8).
- **Masked:** the tracked files are written masked by `diary.py`
  (`journal`, `tokens`, `publish`'s `SHA256SUMS`), with the same mask as the
  zip's text (§2.3). The mask replaces each build machine's host with the
  machine's name and its user with `user`. The host and user list comes from
  `config/machines.toml`, read through `scripts/remote.sh … field`; its
  values are never printed. The mask also replaces any home directory
  (`/home/NAME`, `/Users/NAME`, `C:\Users\NAME`) with `~`, the private
  words of the git-ignored `ocw-art.toml` (`mask_users` → `user`, e.g. the
  coordinator's former user on deb; `mask_names` → `<name>`, a real person's
  name that reached a prompt; `mask_secrets` → `<secret>`, a key that may
  never be published, such as the ANT+ network key, a hex key also written
  byte by byte), API tokens (Vercel `vck_…`, Fly.io `FlyV1 fm2_…`, GitHub,
  `sk-…`, Slack, AWS key ids) with `<token>` (2026-11-27: two tokens had
  reached day 16's prompts), e-mail addresses
  with `<e-mail>` and private IP addresses with `<ip>`. A user name is masked
  as a word of its own (`claude@host`, `"claude"`). It is not masked inside a
  path or a name such as `~/.claude/` or `claude.ai`.
- **`diary.py check-masked`** (`make check`; the hourly collector runs
  it too) fails if a tracked file still holds a private pattern, or a media
  file name of a day folder does (names go public through LFS, the gallery
  and the zips; the binaries themselves are not checked). It prints
  `file:line: kind` (a file name masked), never the value. `check-masked --fix` (`make check
  FIX=1`) masks the files in place, for files written before this rule
  (`index.md`, old journals). The untracked originals are left as they are.

**Withheld media** (user 2026-11-16: "leave out the images where that name is
visible"): a picture or video that must not be published – e.g. a test
account that showed a real person's name – is listed as `DAY/name` in
`build-history/withheld.txt` (with a comment why) and moved, local only, to
`build-history/.withheld/DAY/`. `gather` never copies it back, so it is in
no journal, day zip, gallery or Git LFS commit. A gallery already published
with it is rebuilt by the next `make publish DAY=…`. Test data in OCW uses
only made-up names (OCW's CLAUDE.md).

### 2.6 Incidents (decided by the user 2026-11-15)

What went wrong on the build infrastructure is part of the story too: crashes,
machines dropping out, full disks.

- **Collected every hour** by the collector (§5.1), per day into
  `test-output/build-log/DAY/incidents.jsonl`, which is rewritten on each run
  and gathered into the day's `logs/build-log/`. Each line holds `time`,
  `kind`, `source`, `machine` and `text`, masked like the journals (§2.5).
  - *From the journal of the dev machine* (`journalctl`, user and system,
    read-only; `OCW_ART_JOURNAL=0` turns it off):
    - OOM kills (`oom-kill`: "killed by the OOM killer", the kernel's
      "Killed process");
    - failed OCW user units (`unit-failed`: `ocw-build-dashboard`,
      `ocw-art-collect`, …);
    - restarts (`unit-restart`).

    A tmux scope is listed as "tmux scope (a terminal session)".
  - *From the build log* (§2.2):
    - a machine going offline or back online (`machine-offline`,
      `machine-online`, from the dashboard samples);
    - a disk over 90 % (`disk-full`, once per crossing);
    - janitor deletions (`janitor-delete`);
    - the failed `remote.sh` runs of the day, as a count per machine
      (`runs-failed`).
- **Root-cause notes** by the coordinator: `build-history/DAY/incidents.md`,
  tracked in git, masked and checked by `check-masked`. It has one `## HH:MM –
  title` section per incident, with **What happened**, **Cause**, **Effect**,
  **Fix** and **Follow-up**. The first entry is 2026-11-15, 00:39, when deb
  ran out of memory.
- **Journal:** `journal.md` gets an "Incidents" section. It shows counts per
  kind, the table of collected incidents and the root-cause notes, merged.
  `journal.json` has `incidents`, with `auto` (the collected list), `notes`
  (the Markdown) and `noted` (the headings).
- **In the video:** a chapter can be about an incident: a card shot with
  `incident = "HH:MM"` (§4) shows "INCIDENT · HH:MM" and the incident's text:
  the shot's `text` if it has one, else the heading of its root-cause note,
  else the collected entry.

### 2.7 Features and agent jobs (decided by the user 2026-11-15)

What got built each day, and by which agent job, is part of the record.

- **Features** (`journal.md` "Features", `journal.json` `features`, `deploys`,
  `releases`), built automatically by `journal` (`features.py`):
  - *Spec rows:* the `SPECIFICATION.md` version rows that are in the
    end-of-day spec but were not in the start-of-day spec. Each gets its
    number and a title: the first clause, without parentheses and bold.
    A decision row ("Decision by the user / from the build dashboard: Phase
    10 Q8 – …") gets what was decided instead: "Decided: Phase 10 Q8 – the
    first clause of the answer" (user 2026-11-16: "use a description of
    what the user actually decided"). OCW's own rule since then: the row
    starts with the decision itself, followed by "(decision by the user,
    DATE; Phase 10 Q10 (a); …)"; such a row gets "Decided: Phase 10 Q10 –
    its first clause" (v3.3).
    These come from `git log --first-parent -p` of the spec over the day.
  - *Landed by:* the first-parent commit whose diff added the final row
    (usually the merge; a direct "Spec X.Y" commit otherwise), with its time.
    If several commits added it, a merge naming "spec X.Y" in its subject
    wins. That subject alone counts only when no diff shows the row.
  - *Check:* the latest marge test run (`cargo test`, `make check|test`)
    from the build log, found by one of three rules, best first: the merge
    or its branch tip as the run's `commit` (`scripts/remote.sh` logs it
    since 2026-11-15); the merged agent branch before the merge; or `main`
    between this merge and the next. It reports the exit code and, from
    the run's log, the test suites, passed and failed ("test result:" lines).
  - *Deploys:* `scripts/deploy-test.sh` appends one line per deploy (start,
    end, machine, commit, exit) to `test-output/build-log/DAY/deploys.jsonl`.
  - *Releases:* from `gh release list`, the ones published that day. They are
    skipped when gh fails (offline) or with `OCW_ART_GH=0`.
- **Agent jobs** (`journal.md` "Agent jobs", `journal.json` `agent_jobs`): a
  log the coordinator writes, `test-output/build-log/DAY/agents.jsonl`
  (git-ignored, masked). It has one line per event: `time`,
  `agent_id_short`, `task`, `branch`, `event` (`started`, `reported`,
  `interrupted`, `resumed`, `merged` or `abandoned`), `commits` and `note`.
  - Appending: `diary.py agent-event --task … --branch … --event …
    [--commits …] [--note …]`. The agent id comes from the branch name
    (`worktree-agent-<id>`).
  - The journal shows one row per job: task, start, end, status (the last
    event), interruptions and the merged commit.
  - `diary.py agent-backfill DAY` derives a day's merged jobs from git
    (first and last branch commit, the merge) and the incident log (an OOM
    kill of the coordinator's session interrupts the jobs running then). It
    replaces only its own earlier lines ("backfilled from git"). 2026-11-15
    was backfilled this way.
- **In the video:** a closing **"Today's features"** roll after the chapters,
  before the end card: the merged spec rows, six per page, 3.6 s per page,
  on a violet card under "TODAY'S FEATURES". `features_roll = false` in the
  day script turns it off (§4).
- Everything in these sections is masked like the journals (§2.5). The
  journal is tracked in git; `agents.jsonl` and `deploys.jsonl` stay in the
  git-ignored `test-output/`.

### 2.8 Pictures and videos in Git LFS (decided by the user 2026-11-15)

"Add the fotos and videos into the free git LFS": the day folders' media are
versioned in OCW-ART through [Git LFS](https://git-lfs.com/), within the
free GitHub plan's quota, which nothing may exceed:

| Free plan | Quota | What counts |
|---|---|---|
| LFS storage | 10 GiB | every pushed object, each version once, also of files changed or deleted later |
| LFS bandwidth | 10 GiB a month | every download of LFS objects: clones, fetches, CI checkouts |

- **What:** `build-history/YYYY-MM-DD/*.{jpg,jpeg,png,webp,mp4,webm,mkv}`
  (`.gitattributes`). Never in LFS or git: the day zips (they duplicate the
  media; on the release), the diary videos `build-history/diary/*.mp4` (on
  the release), `.work/` (contact sheets, renders, the gallery). A media
  file whose name holds a private pattern (§2.5) is never committed.
- **One commit per day:** `diary.py lfs-commit [DAY…]` (`make lfs-commit`)
  commits a day's media in one commit, "Build history DAY: N pictures and M
  videos in Git LFS (X MB)", together with the day's lines in the managed
  `lfs-days` block of `.gitignore` (between `# >>> lfs-days` and
  `# <<< lfs-days`; one `!/build-history/DAY/*.ext` per committed kind).
  Without days it takes every finished day (before today) with new media,
  oldest first. Late additions to a committed day get a small commit of
  their own. Empty files (aborted captures) are committed as plain empty
  files: LFS keeps no object for them. It refuses to run without git-lfs ("install git-lfs (make
  deps)"), off `main`, or during a merge or rebase. It checks that every
  staged file is an LFS pointer, never a raw blob. `--dry-run` shows what it
  would do.
- **Budget guard:** `diary.py lfs-budget` (`make lfs-check`) sums the LFS
  objects of the history (`git lfs ls-files --all`, each object once) and
  the media about to be added, against the budget: **9 GiB** by default
  (`lfs_budget_gib` in `ocw-art.toml` or `OCW_ART_LFS_BUDGET_GIB`; at most
  the 10 GiB quota). It reports the total, the files, the rate (the average
  media of a finished day, and the largest day) and the days left at both. `lfs-commit` adds whole days
  while they fit. The first day that does not fit, and every later day,
  stays local and ignored, with the warning "LFS budget reached".
- **Policy** (`lfs_policy` in `ocw-art.toml` or `OCW_ART_LFS_POLICY`): `all`
  (default: pictures and videos) or `pictures` (videos stay local and in
  the day zips). One setting switches it; days already committed keep what
  they have.
- **When the budget is reached** (open, for the user to decide): the guard
  stops adding (nothing new). The choices:
  - `lfs_policy = "pictures"`: pictures are about a third of the bytes
    (1.05 of 2.81 GiB on days 1–5);
  - more storage: a paid data pack and a higher `lfs_budget_gib`;
  - more disk on the dev machine: every committed file is kept twice there,
    as the working copy and in `.git/lfs/objects/` (ext4 has no
    copy-on-write).

  Until then the collector warns.
- **When:** the end-of-day step commits the day explicitly
  (`make lfs-commit DAY=… && make lfs-push`). The hourly collector's 23:xx
  run commits every finished day still pending (yesterday, after its last
  gather), and `bin/collect.sh` then pushes, after the archive lock is
  released. There is no push in the other hours.
- **Push:** `diary.py lfs-push` (`make lfs-push`) pushes `main` (`git lfs
  push`, then `git push`) only when every unpushed commit touches nothing
  but `build-history/` and `.gitignore`, and not when `main` is behind;
  anything else is pushed by hand. Then it checks that `git lfs ls-files`
  lists as many files as there are committed media.
- **Bandwidth:** the gallery workflow takes nothing from git (no checkout;
  a checkout added there must keep `lfs: false`). It builds from the
  release's gallery zips, and release downloads do not count against LFS
  (§6). Clones that do not need the media skip them:
  `GIT_LFS_SKIP_SMUDGE=1 git clone git@github.com:newkit/OCW-ART.git`, or
  once per machine `git lfs install --skip-smudge`; then `git lfs pull
  --include "build-history/2026-11-14/*"` fetches a single day. The
  coordinator's move to its new user on deb copies the media by rsync and
  clones with skip-smudge (OCW's `docs/MIGRATE-DEB-USER.md`). A git worktree
  of OCW-ART on deb is made with `GIT_LFS_SKIP_SMUDGE=1 git worktree add …`,
  else it copies every committed medium out of the local LFS store (disk).
- **Requirements:** git-lfs (`make deps`: apt or dnf, a hint for brew, and
  `git lfs install`). The collector and the LFS commands fail with "install
  git-lfs (make deps)" without it; `OCW_ART_LFS=0` turns LFS off (tests,
  machines without it).

## 3. The day video

About 1.5–3 minutes, 1920×1080, 30 fps, H.264 + AAC, built from these parts,
joined with short animated transitions (pixelize, slides, wipes …):

1. **Title** (≈6 s): the day's hero picture with a slow zoom; "OCW BUILD DIARY",
   **DAY N**, the date, the tagline typed out, the day's title. A bicycle bell rings.
2. **The day in N seconds** (≈10–26 s, time-lapse): every picture of the day in
   time order (no review sheets or before/after crops). A big clock shows the time
   of each picture; counters for commits, merges and pictures run up; on the
   right the commit log scrolls, the newest commit highlighted in pink.
3. **Chapters** (the story, ≈6–10 s each): a time stamp (gold) and a chapter
   title (violet lower third) slide in, then a caption is typed out. Shots are
   stills with a slow Ken-Burns zoom, video clips (optionally sped up, with a
   time-lapse badge) or before/after **split** shots. A yellow **sticker note**
   pops in with a joke or a pointer. A chapter can play a sound file of that day
   (e.g. the game's own audio) while the music ducks.
   - **Images stay on screen longer** (decided by the user 2026-11-14): stills
     and comparison splits run about 1.4× their earlier lengths, roughly
     3–5 s each. Video clips keep their lengths.
   - **Shots run in capture order** (decided by the user 2026-11-14): within a
     chapter the shots follow their `HHMMSS-` time, so images and videos mix
     chronologically. A card stays after the shot it follows.
   - **Today's features** (§2.7, optional, on by default): after the
     chapters, the merged spec rows of the day, six per page, 3.6 s per page.
4. **End card** (≈9 s): a mosaic of the day's pictures, the numbers of the day
   counting up (commits, merges, lines written, pictures and videos, tests
   passing), a closing line and a teaser for the next day.

**Diary video** (`ocw-build-diary.mp4`): a short opener ("The Build Diary",
the logo, a bell), then every day video in order. Rebuilding it after a new
day is the same as appending the new day to the previous diary.

### 3.1 Visual identity

- Colours from the logo (`assets/logos/ocw.svg`, a copy of OCW's `artwork/logos/`): rider pink `#FF1472`, deep
  violet `#3A2F55`, gold `#C98A00`; sticker yellow `#FFE45C`.
- Type: **Lato** (Black, Heavy, Semibold, Medium Italic) for titles and captions,
  **Fira Mono** (the app's UI font, `assets/fonts/`, copied from OCW's `crates/ocw-render/assets/fonts/`) for clocks,
  counters, the commit log and badges.
- Pictures that are not 16:9 sit on a blurred, darkened copy of themselves (no
  black bars). Time-lapse and end card get a light vignette.

### 3.2 Sound

- **Music** (`music.py`): synthesised by the tool itself (no samples, no
  licences), deterministic from the day's seed. The same seed gives the same
  samples, in every process.
- **A style per day** (decided by the user 2026-11-14: "make different music
  for different days"). Each day has its own musical identity: a band
  (timbres), a mode, a groove (swing), a drum kit and its own chord
  progressions.

  | Style | Mode | Band | Groove |
  |---|---|---|---|
  | `synthwave` | minor | detuned super-saw pad, saw bass in 16ths, triangle arpeggio with a dotted-8th echo, saw lead with vibrato, big gated snare | motorik, gated, half-time |
  | `funk` | dorian | filter-wah bass (syncopated 16ths, octave slaps), plucked clavinet stabs, FM lead, organ, ghost notes | swung 16ths |
  | `lofi` | major with 7th chords | FM electric-piano chords, round sine bass (lazy, walking), soft triangle lead, dusty kit, vinyl crackle | boom-bap and half-time, swung |
  | `chiptune` | major | square bass, pulse arpeggio, pulse lead, saw pad, chip kit (the band every day had until v1.6) | four-on-the-floor, half-time, breaks |
  | `darkchip` | dorian (or phrygian, minor) | rounded 25 % pulse lead in the middle register, slow triangle arpeggio with an echo, square/triangle bass over a sine sub, dark low-passed saw pad, soft kit with a rim click | a drum style per chapter in turn: half-time, four-on-the-floor with an open hat, 2-step, half-time break; a break under the time-lapse; kick and rim in the breakdown; tom fills |
  | `melodic-deep-house` | minor with 7th and 9th chords | warm sine-sub bass (syncopated, mostly the root), lush low-passed detuned pad whose filter opens over each 4-bar phrase, mellow plucked arpeggio and FM lead with a dotted-8th delay, soft clap, rim, shaker | four-on-the-floor with off-beat open hats and the clap on 2 and 4, a half-time breather; build-ups into the chapters, a kick-less breakdown |
  | `electro` | phrygian (the bII chord) | booming 808 bass (a sine dropping into its pitch, a little drive) in syncopated 16ths with octave jumps, sequenced saw arpeggio with an echo, pulse lead with a delay, low-passed saw pad, an 808 kit with a long kick, clap and a cowbell-like rim | 124–128 bpm broken electro beat (kick on 1, the "a" of 2, the "and" of 3; clap on 2 and 4), a drum style per chapter in turn: electro, broken, cowbell, half-time; hats and rim in the breakdown |
  | `trance` | minor (aeolian), i–VI–III–VII | rolling saw bass (three 16ths after every kick, never on the beat), detuned supersaw pad whose filter opens over each phrase, plucked 16th arpeggio with an echo, saw lead with vibrato and a delay, a punchy kit with a clap | 136–140 bpm four-on-the-floor with the open hat on every off-beat, a drum style per chapter in turn: trance, driving 16ths, rim and shaker, half-time lift; hats alone in the breakdown (day 11) |
  | `dub` | dorian, i–IV | round sine-sub bass in a melodic line that rests on the downbeat, plucked skank chords on 2 and 4 with a dotted-8th echo, a sustained organ, a reedy pulse lead (a melodica) with a long delay, a soft kit with a rim click | 72–76 bpm one drop (kick and rim on beat 3), swung 16ths, a drum style per chapter in turn: one drop, rockers, steppers, half-drop; rim and hats in the breakdown; dub stops (day 12) |
  | `acid` | minor with 7th chords | squelching 303-like bass (a saw through a resonant low-pass whose cutoff snaps open on every note) in 16ths with octave jumps, dry minor stabs off the beat, a hollow square lead with an echo, a dark low-passed saw pad, a 909-like kit with a clap | 126–130 bpm, a drum style per chapter in turn: four on the floor with the open hat off the beat, jacking (a 16th ride, an extra kick), a broken break, half-time; open hats and hats in the breakdown (day 14) |
  | `garage` | minor with 7th and 9th chords | bouncing sine-sub bass that skips with the kick and leaves gaps, chopped FM-Rhodes chord stabs, a plucked lead with an echo (a cut-up vocal), a soft sine pad, a crisp kit with a clap | 130–134 bpm 2-step (the kick on the one and past the third beat, the snare on 2 and 4), heavily swung 16th hats, a drum style per chapter in turn: 2-step, 2-step with a rim, speed garage, half-time; hats and rim in the breakdown (day 13) |
  | `ambient` | lydian with 7th and 9th chords | slow sine pad whose filter opens over each phrase, a sine drone (root, sometimes the fifth), music-box arpeggio and sparse music-box lead with an echo; **no drums** – no fills, crashes or risers | none: a quiet bed (day 10, the day without tokens) |
  | `liquid-dnb` | dorian with 7th and 9th chords | reese bass (two detuned low-passed saws) over a sine sub in long rolling notes, FM-Rhodes chords, airy detuned pad whose filter opens over each phrase, sparse FM lead with a dotted-8th delay, a crisp kit with ghost snares | 170–174 bpm two-step breakbeat (kick on 1 and the "and" of 3, snare on 2 and 4), a drum style per chapter in turn: two-step, rolling, ride, half-time; hats and rim in the breakdown |
  | `house` | mixolydian with 7ths | sine sub bass on the off-beats, piano stabs, plucked lead, organ, clap, open hats, shaker | four-on-the-floor |

  By default the day number picks the style. Days 1–5 are synthwave, funk,
  lofi, chiptune and house, then the cycle starts again. A day script can
  choose one (`style`) and a mode (`mode`: `major`, `minor`, `dorian`,
  `mixolydian`, `lydian`, `phrygian`; §4).
- **Sections follow the video:** *intro* under the title, *drive* under the
  time-lapse, one *groove* per chapter, *outro* under the end card. A bar
  belongs to the segment that holds its middle.
- **Variation within a day** (decided by the user 2026-11-14: "a bit
  monotone, make it a bit more varied"):
  - *Intro:* no drums, the pad's filter opens and the volume swells, the motif
    enters, and a riser leads into the drive.
  - *Drive:* the style's drive pattern, the motif stated as call and response
    in its second phrase, and a build-up at the end.
  - *Chapters:* each chapter picks its own progression (never the previous
    one), drum pattern (e.g. half-time, breakbeat, four-on-the-floor), bass
    line and arpeggio or stab pattern, and the lead plays in most of them.
    The 4-bar phrases swell slightly.
  - *Chapter changes:* the last bar of a chapter is a fill (toms), a build-up
    (snare roll crescendo and a noise riser) or a stop (everything breaks off
    at the half bar). The new chapter starts with a crash.
  - *Breakdown:* with 4 chapters or more, one chapter in the middle drops the
    drums and the bass.
  - *Bridge and key lift:* in videos over 90 s with 5 chapters or more, the
    chapter before the last third plays the bridge progression. From there
    on, including the end card, the key goes up 1–3 semitones (the style's
    lift).
  - *Outro:* a cadence (e.g. IV–V–I–I, VI–VII–i–i, ii–V–I–I) and the last
    answer ending on the root, while drums, bass and arpeggio thin out.
- **Melody:** a two-bar motif from the seed, with degrees relative to each
  bar's chord, so it follows the harmony. It develops over the video: every
  second chapter adds a variation (sequence, inversion, syncopation,
  ornament, thinning). Each phrase is a call (the motif or its variation)
  and a response (the same first bar, then a second bar moved to end on the
  root, held).
- **Levels:** the music is normalised to an RMS of about −19 dBFS, with peaks
  at most −2.5 dBFS (headroom for the effects). Chapters with game audio
  duck it. `music.stats` reports peak, RMS, brightness, zero-crossing rate
  and onsets per second. The tests (`tests/test_music.py`, in `make test`)
  check determinism, that the days sound different, that nothing clips, the
  loudness, and the variation.
- Tempo and key per day (`bpm`, `key`).
- **Effects**, also synthesised: bicycle bell (title), whooshes (transitions),
  pops (sticker notes), ticks (counters), a ding (end card).
- **Game audio** from the day's archive (e.g. the freehub demo) can be mixed in
  per chapter.

## 4. The day script (`days/YYYY-MM-DD.toml`)

The story is written per day. It can be changed at any time and the video
rendered again.

```toml
title = "A one-line title of the day"
tagline = "In which … (typed out on the title)"
hero = "HHMMSS-label.png"          # title background
bpm = 108                          # music tempo (optional)
key = "C"                          # music key, the tonic (optional)
style = "funk"                     # music style (optional; default from the day
                                   # number): synthwave, funk, lofi, chiptune, house,
                                   # darkchip, melodic-deep-house, liquid-dnb,
                                   # electro, ambient, trance, dub, garage, acid (not in the automatic
                                   # cycle)
mode = "dorian"                    # music mode (optional; default the style's):
                                   # major, minor, dorian, mixolydian, lydian
tests = 903                        # tests passing at the end of the day (optional;
                                   # else the highest "N tests" in a commit message)
outro = "Closing line on the end card."
teaser = "NEXT TIME: …"            # optional
title_seconds = 6.5                # optional
end_seconds = 9                    # optional
features_roll = true               # the closing "Today's features" roll (§2.7;
                                   # default true, false turns it off)
timelapse_skip = ["HHMMSS-x.jpg"]  # optional: pictures left out of the time-lapse
                                   # and the end card's mosaic (e.g. a screenshot
                                   # showing a real person's name); shell
                                   # patterns too ("*-calibration-*")
timelapse = false                  # optional: no time-lapse (default true; a day
                                   # without a build, §4.1)
stats = [[0, "COMMITS"], [1440, "DASHBOARD SAMPLES"]]
                                   # optional: the end card's numbers instead of
                                   # the journal's (§4.1)

[[chapter]]
time = "15:02"                     # when it happened (shown in gold)
title = "Hello, Liechtenstein"
caption = "The funny caption, typed out."
prompt = "the user's prompt that started it"   # optional, shown as a chat bubble
sound = "HHMMSS-audio.wav"         # optional: the day's sound file, music ducks
sound_gain = 1.0                   # optional
shots = [
  { file = "HHMMSS-x.png", seconds = 4.2, note = "sticker text" },     # still: Ken Burns
  { file = "HHMMSS-x.png", seconds = 4.2, focus = [0.42, 0.41, 2.5] }, # push in on a detail
                                                                       # (x, y as fractions, end zoom)
  { file = "HHMMSS-y.mp4", seconds = 4.0, start = 2.0, speed = 2 },    # clip, 2× time-lapse
  { split = ["before.png", "after.png"], seconds = 4.9 },              # before | after
  { card = true, seconds = 2.0 },                                      # plain violet card;
                                                                       # optional text = "…" (centred)
  { card = true, seconds = 4.0, incident = "00:39" },                  # an incident (§2.6);
                                                                       # optional text = "…"
]
```

`file` is a name in the day folder, or a path in the repository (e.g.
`assets/logos/ocw-512.png`), or `../YYYY-MM-DD/name` for another day.

Writing guidelines:

- 6–12 chapters in time order, each one thing that changed what you see or
  how it works. Use the journal (`journal.md`) and the contact sheets.
- Shots of a chapter in capture order (their `HHMMSS-` time), images and
  videos mixed; a card right after the shot it belongs to (§3).
- Stills about 3–5 s (3.5–4.9 s is typical), splits about 4.5–5 s; clips as
  long as the action needs (§3).
- Captions ≤ 120 characters, notes ≤ 40. One joke per chapter is plenty.
- Prefer shots that show change: first appearances, before/after, failures that
  look funny (a rider inside a tree is content).
- Facts must be true: times, numbers and names come from the journal.

### 4.1 A day without tokens (2026-11-20)

A build day can pass without a build: on 2026-11-20 the account's weekly
token limit had been reached the evening before ("You've hit your weekly
limit · resets Nov 21, 9am"), so there were no commits, prompts, tokens or
pictures. Such a day still gets its journal, its README entry and its video
(a day without media keeps its journal and README entry):

- **The note:** the coordinator writes the day's `incidents.md` (§2.6), which
  the journal shows under "Incidents".
- **The pictures:** `diary.py crab DAY` draws the diary's own – an ASCII crab
  in the terminal's orange on a dark terminal, in the spirit of the Claude
  Code CLI's mascot (drawn for the diary, not copied), turning its trouser
  pockets inside out while the token counter runs down from the day before's
  tokens to 0; a moth and some dust fly out, the crab shrugs and falls
  asleep; "2026-11-20 – no tokens left · weekly limit · resets Nov 21, 9:00".
  A 22 s clip (`120000-no-tokens-crab-pockets.mp4`), the terminal alone as
  the title's background and three stills, in the day folder (so the
  gallery, the day zip and Git LFS have them). Everything is text: each
  ASCII frame is a Fira Mono block of the videos' ASS layer, one block per
  colour so the monospace layers line up, drawn by ffmpeg (`crab.py`).
- **The video:** a short day script – no time-lapse (`timelapse = false`),
  no features roll, the clip as the one chapter, the end card's numbers
  from `stats` (0 commits, prompts, tokens and build runs; the dashboard's
  1,440 samples), the quiet `ambient` style. About 35 s.
- **The day number:** a day with a day script but no commits counts in the journal's
  day number, so 2026-11-20 is day 10 and the next build day day 11.

## 5. Workflow

Needs Python 3.11+ (`/usr/bin/python3` on Debian 13; the pyenv default 3.8
is too old), ffmpeg with libass, git-lfs, `zip`, the Lato font, and `gh`
(logged in) for fetching and publishing. `make deps` checks them and
installs ffmpeg, git-lfs and zip (apt on Debian, dnf on Fedora, a hint for
`brew` on macOS), then runs `git lfs install`. Pillow is not needed: ffmpeg
does every frame and every scaling. The tool runs on the dev machine; no
Rust build is involved.

**Layout** (since v2.0):

```
OCW-ART/
├── README.md, Makefile, LICENSE-MIT, LICENSE-APACHE
├── ocw-art.example.toml   # → ocw-art.toml (git-ignored): ocw_repo, lfs_policy, lfs_budget_gib
├── .gitattributes         # the day folders' media → Git LFS (§2.8)
├── .gitignore             # the build-history allow-list, with the managed lfs-days block
├── diary.py               # the command line (every `diary.py …` command)
├── ocwart/                # the Python package
│   ├── cli.py             #   the commands
│   ├── core.py            #   settings, paths, the lock, git/ffmpeg helpers
│   ├── mask.py            #   masking, the tracked files, check-masked (§2.3, §2.5)
│   ├── archive.py         #   fetch, gather, stamp (§2, §2.1)
│   ├── prompts.py         #   prompts and token usage (§2.3, §2.4)
│   ├── incidents.py       #   incidents (§2.6)
│   ├── agents.py          #   agent jobs (§2.7)
│   ├── features.py        #   the features log, pure (§2.7)
│   ├── journal.py         #   the day's journal (§2)
│   ├── render.py          #   contact sheets, the day and diary videos (§3)
│   ├── crab.py            #   a day without tokens: the ASCII crab (§4.1)
│   ├── subtitles.py       #   the ASS layer of the videos
│   ├── music.py, sfx.py   #   the music and the effects (§3.2)
│   ├── publish.py         #   day zips and videos → the release
│   ├── gallery.py         #   the gallery (§6)
│   ├── lfs.py             #   Git LFS, the budget (§2.8)
│   ├── readme.py          #   the generated README (§5.3)
│   └── collect.py         #   the hourly collector (§5.1)
├── bin/collect.sh         # the collector's entry (the systemd unit runs it)
├── systemd/               # ocw-art-collect.service / .timer
├── site/                  # the gallery's templates: page.html, gallery.css, gallery.js
├── .github/workflows/gallery.yml   # deploys the gallery to GitHub Pages
├── days/YYYY-MM-DD.toml   # the day scripts (§4)
├── assets/                # the OCW logo and Fira Mono (copies, assets/README.md)
├── docs/ART-PROJECT.md    # this document; docs/readme/: the README's template (§5.3)
├── tests/                 # unit tests (hermetic: fixture archives and repositories)
└── build-history/         # the archive (§2): text tracked, media in LFS or local
```

**Two checkouts.** This repository ([newkit/OCW-ART](https://github.com/newkit/OCW-ART))
holds the tool, the day scripts and the archive. OCW is read from its own
checkout, by default `../OCW` next to this one (on deb `~/data/git/OCW` next
to `~/data/git/OCW-ART`; after the coordinator's move to its new user on deb
`~/src/OCW` and `~/src/OCW-ART`). `OCW_REPO` (environment) or
`ocw_repo` in a git-ignored `ocw-art.toml` (see `ocw-art.example.toml`) point
elsewhere; `make ocw-repo` prints the one in use. From OCW the tool reads only:

- `git log` and `SPECIFICATION.md` (commits, merges, spec rows, day numbers);
- `test-output/` (media, the build log, `agents.jsonl`, `deploys.jsonl`,
  incidents) and the agent worktrees' `.claude/worktrees/*/test-output/`;
- `config/machines.toml` through OCW's `scripts/remote.sh … field`, for the
  mask list (in an agent worktree the main checkout's). **Without a machine
  list it refuses to mask** (`OCW_ART_NO_MACHINES=1` is for tests only).

It writes into OCW only the collector's status and logs
(`test-output/build-log/DAY/art.json`, `art-runs.jsonl`, `art.log`,
`incidents.jsonl`) and `agents.jsonl` (`agent-event`), so the build
dashboard's "Art project" panel keeps working unchanged.

```bash
make deps                     # ffmpeg, git-lfs, zip; git lfs install
make gather DAY=2026-11-13    # collect everything of the day, stamp times, journal
make sheets DAY=2026-11-13    # contact sheets: build-history/.work/DAY/sheets/
# write days/2026-11-13.toml (story, shots, jokes)
make render DAY=2026-11-13    # → build-history/diary/ocw-diary-day-NN-DAY.mp4
make diary                    # → build-history/diary/ocw-build-diary.mp4
make publish DAY=2026-11-13   # day zip + all videos → release build-history, then the gallery (§6)
make gallery                  # the gallery, locally (make gallery-preview: http://127.0.0.1:8000/)
make lfs-check                # the LFS total, the budget, the days left (§2.8)
make lfs-commit DAY=2026-11-13 && make lfs-push   # the day's media → Git LFS
make check                    # tracked text files and media names masked? (FIX=1 masks the text)
git commit build-history/index.md build-history/SHA256SUMS \
    build-history/2026-11-13/{journal.md,journal.json,tokens.json}
make test                     # unit tests of the tool, the gallery, LFS and the collector
```

or directly `diary.py gather|journal|sheet|render|diary|publish|all|collect|crab|gallery|lfs-budget|lfs-commit|lfs-push|check-masked [DAY…]`.

**At the end of every build day** (or when asked): the hourly collector (§5.1)
has already gathered the day and written its journal. The coordinator:

1. writes the day script and renders the day (`make render DAY=…`);
2. rebuilds the diary (`make diary`);
3. publishes (`make publish DAY=…`): the day zip, the videos and
   `SHA256SUMS` go to the release, then the gallery is rebuilt, its changed
   zips uploaded and GitHub Pages redeployed (`GALLERY=0` skips the
   gallery; `make gallery-publish` does it alone), then `README.md` is
   regenerated (§5.3);
4. commits the day's media to Git LFS and pushes (`make lfs-commit DAY=…
   && make lfs-push`; the collector's 23:xx run of the next day does it
   otherwise);
5. runs `make check` and commits the day's tracked text files (§2.5) and
   `README.md`.

During the day, keep every screenshot, video and sound in `test-output/`
(the test harnesses already do), so the gather step finds them.

### 5.1 The hourly collector (decided by the user 2026-11-14)

Collecting no longer waits for a session. A systemd user timer on the dev machine
(deb, the coordinator's machine with the OCW main checkout and the OCW-ART
checkout) collects the day's data every hour.

**Each hour** `bin/collect.sh` runs `diary.py collect`, which does:

1. **`gather` + `journal` for yesterday and today**, so the last hour before
   midnight is not lost. Other days can be given as arguments:
   `bin/collect.sh 2026-11-12`. `gather` is idempotent: sources are
   deduplicated by SHA-256, and the build log is updated in place. A day
   that fails is reported, and the other day is still collected. Each day's
   incidents are collected too (§2.6), and the status counts them.
2. **The mask check** (`check-masked`, §2.5) over all tracked text files
   and the media names. Any finding fails the run.
3. **The local gallery** (`gallery build`, §6): incremental, two ffmpeg
   processes, not published. `--no-gallery` or `OCW_ART_GALLERY=0` skips it.
4. **Contact sheets** (`sheet`) of today, only in the 23:xx run. They are
   heavier (ffmpeg); `--sheets` / `--no-sheets` force them on or off.
5. **Git LFS** (§2.8): every run reports the LFS total and the days left;
   the 23:xx run commits the finished days' media within the budget, one
   commit per day (`--lfs` / `--no-lfs` force it on or off). After
   `diary.py` has released the lock, `bin/collect.sh` pushes when that run
   made a commit (`lfs-push`). "LFS budget reached" is a warning in the
   status, not a failure. Without git-lfs the run still gathers, then fails
   with "install git-lfs (make deps)" (`OCW_ART_LFS=0` turns LFS off).

No Claude run, no render, no publish of videos or the gallery: the
coordinator writes the day script, renders and publishes in a session.

- **Lock:** runs never overlap. The script holds an `flock` on
  `build-history/.lock`. Every `diary.py` command takes the same lock,
  including manual runs, `check-masked --fix`, `gallery build|publish` and
  `lfs-commit`; plain `check-masked`, `lfs-budget`, `lfs-push` and `gallery
  serve` take none. A manual run waits for the collector (it says whose
  lock it waits for), and the collector waits up to 45 min
  (`OCW_ART_LOCK_WAIT`, seconds) for a manual run. If the lock is still held,
  the run gives up with status `locked` and exit 75, which is not a unit
  failure. The script sets `OCW_ART_LOCK_HELD=1` for the `diary.py` it starts,
  which then does not lock again.
- **Python:** `/usr/bin/python3` (3.11+; `OCW_ART_PYTHON` overrides), never the
  pyenv default 3.8. The script finds this checkout from its own path and
  OCW through `diary.py ocw-repo` (§5).
- **Overrides (tests):** `OCW_REPO` names the OCW checkout. `OCW_ART_HISTORY`
  replaces the archive. `OCW_TEST_OUTPUT` replaces OCW's `test-output/`
  (and receives the status): it is then the only source of `gather`, without
  the agent worktrees' `test-output/` (`OCW_ART_WORKTREES` names a worktrees
  folder, `""` none). `OCW_TRANSCRIPTS` replaces the Claude Code transcripts.
  `OCW_ART_GALLERY=0` and `OCW_ART_LFS=0` skip the gallery and LFS steps.
  `make test` checks that the real archive at the default place stays
  untouched (it holds the archive's lock and compares every file's size and
  mtime).
- **Status file:** OCW's `test-output/build-log/DAY/art.json` holds the latest run
  of DAY: start, end, status (`running`, `ok`, `failed`, `locked`), new
  files, media of today, the mask check, contact sheets yes/no, the gallery,
  LFS (`lfs`: policy, stored, pending, budget in GiB, days left; `lfs_push`),
  errors and warnings (masked), and new files and media per day. `art-runs.jsonl` next to it
  has one line per run. The exit code is 0 for ok, 1 for failed and 75 for
  locked.
- **Logs:** the output of every run is appended to OCW's `test-output/build-log/DAY/art.log`
  (one `=== start` / `=== exit` block per run). The systemd journal has it too
  (`journalctl --user -u ocw-art-collect`). The collector's own files are
  gathered into the day's `logs/build-log/` like the rest of the build log,
  but they do not count as new files.
- **Dashboard:** the build dashboard's "Art project" panel (and `--once`,
  `/api/status` → `art`) shows the last run from the newest `art.json`:
  time, status, new files, media of today, the mask check and errors. It is
  flagged **late** when no run has ended for 2.5 h.
- **Units:** `systemd/ocw-art-collect.service` (oneshot, `nice`, idle I/O,
  `TimeoutStartSec=150min`, which leaves room for the 23:xx LFS push;
  `ExecStart=…/bin/collect.sh`) and `ocw-art-collect.timer` (`OnCalendar=hourly`,
  `Persistent=true`, so missed runs are made up after boot, and
  `RandomizedDelaySec=5min`). The service sets `TMPDIR=%h/tmp` (deb's
  `/tmp` is RAM). The contact sheets are part of the 23:xx run,
  so there is no separate sheets timer.

```bash
make install-timer     # units → ~/.config/systemd/user/ (this checkout's path filled in),
                       # daemon-reload, enable --now ocw-art-collect.timer
make timer-status      # list-timers, the installed ExecStart, the last status file
make collect           # one run now (DAY=… for other days)
make uninstall-timer   # stop and remove the timer and service
sudo loginctl enable-linger $USER   # once: user timers run without a login session
```

Install the timer from the **OCW-ART checkout on the dev machine**, never
from a worktree: the units point to the checkout they were installed from.

### 5.2 History: from OCW to OCW-ART (2026-11-15)

Until 2026-11-15 the art project lived in OCW (`art/`, `scripts/art-collect.sh`,
`make art-*`), with its archive in OCW's `art/build-history/` (until
2026-11-14 `artwork/build-history/`) and the timer installed from OCW. On
2026-11-15 the timer was stopped, the archive moved on the same file system
into OCW-ART's `build-history/`, OCW's `art/` was removed, and the timer was
installed from OCW-ART. OCW's `make art-*` targets only print where they
went. Days 1–4 (videos, zips, `SHA256SUMS`, `index.md`) were copied to
OCW-ART's release with matching SHA-256; OCW's release still has them and
the README's product images (`world-*.jpg`, `readme-*.png`), which stay.
The restructure of v2.0 moved `collect.sh` to `bin/collect.sh`; the timer
was reinstalled (`make install-timer`) and `make timer-status` shows
`ExecStart=…/OCW-ART/bin/collect.sh`.

Another user (the coordinator's move to a new user on deb): clone OCW-ART
next to OCW (`~/src/OCW-ART` next to `~/src/OCW`) with
`GIT_LFS_SKIP_SMUDGE=1` (the media come by copy, not by download, §2.8),
copy the git-ignored and LFS media of `build-history/` into it (OCW's
`scripts/migrate-user.sh` and `docs/MIGRATE-DEB-USER.md` do it), then
`make deps` and `make install-timer` there.

### 5.3 The README (decided by the user 2026-11-15)

"A nice overview (visually) over the project, the evolution and the build
days. Link the images and videos." `README.md` is generated by
`diary.py readme` (`make readme`; `make publish` runs it after the gallery)
from:

- `docs/readme/README.template.md`: the hand-written parts (the idea, how it
  is made with a diagram, the layout, the commands, the licences and
  credits) with the slots `{{hero}}`, `{{totals}}`, `{{evolution}}` and
  `{{days}}`;
- `docs/readme/evolution.toml`: "How the game grew", hand-picked pictures
  with one-line captions (day 1's capsules on a green field, Liechtenstein,
  the Black Forest, Tenerife, the unicorn, seasons, weather, the browser,
  vegetation);
- per day, newest first: the title and tagline of `days/DAY.toml`, four
  pictures (the hero, then one still per chapter spread over the story,
  else pictures spread over the day), the day video, the day zip, the
  gallery, and the numbers of the journal (commits, merges, the spec
  versions from the features log, pictures, videos, tokens, the music
  style).

Pictures are the gallery's thumbnails on GitHub Pages (320 px; the hero one
web copy), each linking to its place in the gallery (`#N`). Videos are
poster thumbnails linking to the release assets, since github.com does not
play embedded release videos. Only pictures the built gallery holds are
used, and release links only for assets that exist (`gh`, else the local
files), so no link is dead once the gallery is published. The page itself
stays small (about 20 kB of Markdown, about 2 MB of thumbnails). The text is
masked and checked before it is written, and `check-masked` checks
`README.md` too (which is why its clone URLs are HTTPS: `git@github.com` looks
like an e-mail address).

## 6. The gallery (decided by the user 2026-11-15)

"I miss seeing the actual photos and videos": a static web site shows the
whole archive, day by day, at **<https://newkit.github.io/OCW-ART/>**
(GitHub Pages of OCW-ART).

- **Start page:** one card per day, newest first: the hero picture (the day
  script's `hero`, else the middle picture of the day), day number and date,
  the day's title, the number of pictures, videos and commits, and links to
  the day's gallery and video. At the top, the whole diary video and the
  release.
- **Day page:** a thumbnail grid of every picture and a poster frame of
  every video (with a play mark and the clip's length), in time order, with
  the time, the caption (the file name as words) and, for the shots the day
  video uses, "In the video: chapter – note". Clicking opens the web copy
  in a lightbox with previous / next (buttons, arrow keys, swipe), `Esc`,
  and a deep link (`#N`). Every item links to its full-size source: the day
  zip on the release (and the file name in it), for videos the day video.
  Until the day is published (no zip, no day video yet) the links say so.
  Without JavaScript every thumbnail still links to its web copy.
- **Not on Pages:** the raw MP4s and full-size originals (they are in the
  day zips and LFS), the audio.
- **Text:** captions, titles and notes are masked (§2.5) and every page is
  checked with the mask rules before the site is replaced; a file whose
  name holds a private pattern is left out. The pictures themselves are
  public already (day zips).
- **Footer:** the art project's licence (code MIT OR Apache-2.0) and "©
  OpenStreetMap contributors" (ODbL) for the map and world renders, as on
  the release.

### 6.1 Build

`diary.py gallery build` (`make gallery`; `make gallery-preview` serves it on
`http://127.0.0.1:8000/`) writes `build-history/.work/gallery/`:

- `cache/DAY/t/` thumbnails (320 px wide, JPEG `-q:v 4`, about 10 KB),
  `cache/DAY/w1280/` web copies (1280 px, `-q:v 3`, about 100 KB) and, when
  the budget needs them, `cache/DAY/w960/` (960 px, `-q:v 6`, about 45 KB);
  never scaled up. A video's poster is its frame at 40 % of its length.
  `cache/manifest.json` keys every source on its size and mtime: a run only
  makes what is new or changed (the first build of days 1–5, 2,239 items,
  took 2 minutes; an unchanged rebuild 2 seconds). One ffmpeg run makes
  both sizes; at most 4 ffmpeg processes at once (default 3, the collector
  2), under `nice` and idle I/O. A file ffmpeg cannot read gets "no
  preview" and is listed, the build goes on.
- `site/`: the pages from `site/page.html`, `gallery.css`, `gallery.js` and
  hard links to the cache. It is built in `site.new` and swapped in only
  when the mask check and the size guard pass.
- Tools: ffmpeg only (no Pillow, no other dependency).

### 6.2 Hosting: Pages from the release, no media in git

`diary.py gallery publish` (`make gallery-publish`; `make publish` runs it
after the day's publish):

1. builds the site;
2. uploads to the release `build-history`: `gallery-pages.zip` (the pages,
   CSS, JS, logo; small, every time) and one `gallery-YYYY-MM-DD.zip` per
   day with its thumbnails and web copies, only when they changed (a digest
   per day in `.work/gallery/published.json`) or are missing on the release;
3. starts the workflow `.github/workflows/gallery.yml` (`gh workflow run`),
   which downloads the `gallery-*.zip` assets, unpacks them and deploys them
   with `actions/upload-pages-artifact` and `actions/deploy-pages`
   (`--wait` follows it). `make gallery-deploy` only redeploys.

Why this way: the media stay out of git completely (no `gh-pages` branch,
whose objects every clone would fetch and whose force-pushed history would
still grow on GitHub). The site is built where the media are (the dev
machine), incrementally, including the current day before it has a day zip.
A build on the runner from the day zips would download 2–3 GB per deploy
(1.4 GB for day 4 alone) and make every thumbnail again. The workflow uses
no checkout, so it costs no LFS bandwidth (§2.8). Pages is set to "GitHub
Actions" as its source (`gh api -X POST repos/newkit/OCW-ART/pages -f
build_type=workflow`, once).

The hourly collector refreshes the local gallery but does not publish it:
an hourly upload of the day's zip (50–70 MB) and a redeploy would cost more
than it gives. The end-of-day publish refreshes it.

### 6.3 The size budget

Pages allows 1 GB per site. `--max-mb` (default 900, `MAX_MB=…`; at most 999)
is the budget of the whole site. Days 1–5 take 243 MB (about 50–70 MB a day
at full size), so the budget lasts about 10 more days at full size. Then:

1. While the site fits, every day is **full** (thumbnails and 1280 px copies).
2. When it does not, the oldest day steps down to **reduced** (960 px
   copies, about half the bytes), then the next oldest, until it fits.
3. When every day is reduced and it still does not fit, the oldest day steps
   down to **thumbnails only** (the lightbox shows the thumbnail and links
   to the day zip), then the next oldest. The newest day stays full the
   longest.
4. When even thumbnails only do not fit, the build stops with a message
   (raise `--max-mb` up to 999, or thin the thumbnails out: a later decision).

A stepped-down day says so on its page. The plan is computed fresh on every
build from the real file sizes, so the tiers move as days are added. The
workflow refuses to deploy a site of 1 GB or more.

## 7. Future elements (ideas, not built yet)

- A narrator voice (local TTS, e.g. Piper) reading the captions.
- Per-commit "diff art": lines added/removed as a growing skyline.
- A map of Liechtenstein (and later worlds) lighting up the roads ridden so far.
- Test results as a heartbeat line (passes per run over the day).
- Chapter music stingers per theme (night shift, release day).
- An auto-drafted day script from the journal, for a human to polish.
