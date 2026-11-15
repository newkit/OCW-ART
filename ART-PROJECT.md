# OCW Build Diary – Art Project Specification

Version 1.9 – 15 November 2026

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
  2026-11-14 `artwork/build-history/`; `diary.py` stops with a message while
  the archive is still at the old place, §5.2). Media never go into git
  (OCW spec §11.3; OCW's history was rewritten on 2026-11-12 to remove
  them); its text files are tracked, masked (§2.5).
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
  longest runs, and each server's online share. The day video's end card shows
  BUILD RUNS and BUILD HOURS.
- `OCW_BUILD_LOG=0` turns the run log off for a single command.

### 2.3 The prompts

The user's prompts to Claude Code (the conversation that builds OCW) are part
of the story.

- **Source:** the Claude Code session transcripts of the project
  (`~/.claude/projects/*OCW*/*.jsonl`, `OCW_TRANSCRIPTS` overrides the root): the
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

### 2.5 Text in git, media not (decided by the user 2026-11-14)

The archive's text record is versioned with the code; its media are not.

| In `build-history/` | Git |
|---|---|
| `index.md`, `SHA256SUMS` | **tracked** |
| per day `journal.md`, `journal.json`, `tokens.json` | **tracked** |
| media (jpg/png/mp4/wav/webm …), the day zips, `diary/*.mp4` | ignored (GitHub release `build-history`) |
| per day `logs/` (unmasked originals), `prompts.*` (published masked in the zip), `.txt` verdicts | ignored |
| `.work/` (render and contact-sheet files), `.lock` | ignored |

- `.gitignore` ignores `/build-history/**` and re-includes exactly the
  tracked files above.
- **Masked:** the tracked files are written masked by `diary.py`
  (`journal`, `tokens`, `publish`'s `SHA256SUMS`), with the same mask as the
  zip's text (§2.3). The mask replaces each build machine's host with the
  machine's name and its user with `user`. The host and user list comes from
  `config/machines.toml`, read through `scripts/remote.sh … field`; its
  values are never printed. The mask also replaces any home directory
  (`/home/NAME`, `/Users/NAME`, `C:\Users\NAME`) with `~`, e-mail addresses
  with `<e-mail>` and private IP addresses with `<ip>`. A user name is masked
  as a word of its own (`claude@host`, `"claude"`). It is not masked inside a
  path or a name such as `~/.claude/` or `claude.ai`.
- **`diary.py check-masked`** (`make check`; the hourly collector runs
  it too) fails if a tracked file still holds a private pattern. It prints
  `file:line: kind`, never the value. `check-masked --fix` (`make check
  FIX=1`) masks the files in place, for files written before this rule
  (`index.md`, old journals). The untracked originals are left as they are.

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
  | `house` | mixolydian with 7ths | sine sub bass on the off-beats, piano stabs, plucked lead, organ, clap, open hats, shaker | four-on-the-floor |

  By default the day number picks the style. Days 1–5 are synthwave, funk,
  lofi, chiptune and house, then the cycle starts again. A day script can
  choose one (`style`) and a mode (`mode`: `major`, `minor`, `dorian`,
  `mixolydian`, `lydian`; §4).
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
  and onsets per second. The tests (`test_music.py`, in `make test`)
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
                                   # number): synthwave, funk, lofi, chiptune, house
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

[[chapter]]
time = "15:02"                     # when it happened (shown in gold)
title = "Hello, Liechtenstein"
caption = "The funny caption, typed out."
prompt = "the user's prompt that started it"   # optional, shown as a chat bubble
sound = "HHMMSS-audio.wav"         # optional: the day's sound file, music ducks
sound_gain = 1.0                   # optional
shots = [
  { file = "HHMMSS-x.png", seconds = 4.2, note = "sticker text" },     # still: Ken Burns
  { file = "HHMMSS-y.mp4", seconds = 4.0, start = 2.0, speed = 2 },    # clip, 2× time-lapse
  { split = ["before.png", "after.png"], seconds = 4.9 },              # before | after
  { card = true, seconds = 2.0 },                                      # plain violet card
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

## 5. Workflow

Needs Python 3.11+ (`/usr/bin/python3` on Debian 13; the pyenv default 3.8 is too
old), ffmpeg with libass, `zip`, and `gh` (logged in) for fetching/publishing.
The tool runs on the dev machine (no Rust build involved).

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
make gather DAY=2026-11-13    # collect everything of the day, stamp times, journal
make sheets DAY=2026-11-13    # contact sheets: build-history/.work/DAY/sheets/
# write days/2026-11-13.toml (story, shots, jokes)
make render DAY=2026-11-13    # → build-history/diary/ocw-diary-day-NN-DAY.mp4
make diary                    # → build-history/diary/ocw-build-diary.mp4
make publish DAY=2026-11-13   # day zip + all videos → release build-history of OCW-ART
make check                    # tracked text files masked? (FIX=1 masks them)
git commit build-history/index.md build-history/SHA256SUMS \
    build-history/2026-11-13/{journal.md,journal.json,tokens.json}
make test                     # unit tests of the tool and the collector
```

or directly `diary.py gather|journal|sheet|render|diary|publish|all|collect|check-masked [DAY…]`.

**At the end of every build day** (or when asked): the hourly collector (§5.1)
has already gathered the day and written its journal. The coordinator writes the
day script, renders the day, rebuilds the diary, publishes, and commits the day's
tracked text files (§2.5). During the day, keep every screenshot, video and sound
in `test-output/` (the test harnesses already do), so the gather step finds them.

### 5.1 The hourly collector (decided by the user 2026-11-14)

Collecting no longer waits for a session. A systemd user timer on the dev machine
(deb, the coordinator's machine with the OCW main checkout and the OCW-ART
checkout) collects the day's data every hour.

**Each hour** `collect.sh` runs `diary.py collect`, which does:

1. **`gather` + `journal` for yesterday and today**, so the last hour before
   midnight is not lost. Other days can be given as arguments:
   `collect.sh 2026-11-12`. `gather` is idempotent: sources are
   deduplicated by SHA-256, and the build log is updated in place. A day
   that fails is reported, and the other day is still collected. Each day's
   incidents are collected too (§2.6), and the status counts them.
2. **The mask check** (`check-masked`, §2.5) over all tracked text files.
   Any finding fails the run.
3. **Contact sheets** (`sheet`) of today, only in the 23:xx run. They are
   heavier (ffmpeg); `--sheets` / `--no-sheets` force them on or off.

No Claude run, no render, no publish: the coordinator writes the day script,
renders and publishes in a session.

- **Lock:** runs never overlap. The script holds an `flock` on
  `build-history/.lock`. Every `diary.py` command takes the same lock,
  including manual runs and `check-masked --fix`; plain `check-masked` reads
  only and takes none. A manual run waits for the collector (it says whose
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
  `make test` checks that a real archive at the default place and at the old
  place in OCW stays untouched (it holds each archive's lock and compares
  every file's size and mtime).
- **Status file:** OCW's `test-output/build-log/DAY/art.json` holds the latest run
  of DAY: start, end, status (`running`, `ok`, `failed`, `locked`), new
  files, media of today, the mask check, contact sheets yes/no, errors
  (masked), and new files and media per day. `art-runs.jsonl` next to it
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
  `TimeoutStartSec=75min`) and `ocw-art-collect.timer` (`OnCalendar=hourly`,
  `Persistent=true`, so missed runs are made up after boot, and
  `RandomizedDelaySec=5min`). The contact sheets are part of the 23:xx run,
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

### 5.2 Moving to OCW-ART (2026-11-15)

Until 2026-11-15 the art project lived in OCW (`art/`, `scripts/art-collect.sh`,
`make art-*`), with its archive in OCW's `art/build-history/` and the timer
installed from OCW. The move, once, on the dev machine; the timer and the
archive move together, so that the hourly collector never writes into a
half-moved archive. `ART` is the OCW-ART checkout, `OCW` the OCW main checkout
(on deb `~/data/git/OCW-ART` and `~/data/git/OCW`):

```bash
ART=~/data/git/OCW-ART OCW=~/data/git/OCW
# 1. stop the timer (installed from OCW; the units are the same files either way)
systemctl --user disable --now ocw-art-collect.timer
systemctl --user stop ocw-art-collect.service
flock "$OCW/art/build-history/.lock" true          # waits for a running diary.py to finish
# 2. move the archive (same file system: instant). ART's build-history/ holds
#    only tracked text, which the moved archive has in the same or a newer state.
rm -rf "$ART/build-history" && mv "$OCW/art/build-history" "$ART/build-history"
git -C "$ART" status --short build-history        # only journals the collector rewrote since
#    then merge OCW's cleanup branch (removes art/ from OCW) and: rm -rf "$OCW/art"
# 3. the timer from OCW-ART
make -C "$ART" install-timer                      # units now point to $ART/collect.sh
# 4. the first collector run (yesterday and today)
make -C "$ART" collect
# 5. the mask check, then commit the rewritten journals in OCW-ART
make -C "$ART" check && make -C "$ART" timer-status
```

- Before step 2 the tool refuses to work (`still in the OCW checkout`), and the
  collector's status says so on the dashboard; that is the old place check.
- After the move `make uninstall-timer` / `install-timer` are OCW-ART's;
  OCW's `make art-*` targets only print where they went.
- Publishing goes to OCW-ART's release `build-history`. Days 1–4 (videos, zips,
  `SHA256SUMS`, `index.md`) were copied there from OCW's release with matching
  SHA-256; OCW's release still has them and the README's product images
  (`world-*.jpg`, `readme-*.png`), which stay.
- Another user (the coordinator's move to a new user on deb): clone OCW-ART
  next to OCW (`~/src/OCW-ART` next to `~/src/OCW`), copy the git-ignored
  media of `build-history/` into it (OCW's `scripts/migrate-user.sh` and
  `docs/MIGRATE-DEB-USER.md` do it), then `make install-timer` there.

## 6. Future elements (ideas, not built yet)

- A narrator voice (local TTS, e.g. Piper) reading the captions.
- Per-commit "diff art": lines added/removed as a growing skyline.
- A map of Liechtenstein (and later worlds) lighting up the roads ridden so far.
- Test results as a heartbeat line (passes per run over the day).
- Chapter music stingers per theme (night shift, release day).
- An auto-drafted day script from the journal, for a human to polish.
