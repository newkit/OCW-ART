# OCW build diary – day 12, 2026-11-22

46 commits (12 merges), +10926 / −1075 lines, 377 images, 10 videos, 0 sounds.

## Commits

| Time | Commit | |
|---|---|---|
| 09:13 | `a075e44` | The Voice page gets two rows, My voice and I hear; voice off becomes both rows off (spec 7.1.7 Q16 layout decided) |
| 09:32 | `d5deb0b` | Built: the Voice page has two separate rows, My voice and I hear; the old voice off is both rows off (spec 7.1.7 Q16) |
| 09:39 | `2688a68` | The lips move while a rider is heard speaking: a short pulse on the near model, never while muted (spec Phase 4 Q24 (a)) |
| 09:42 | `b70c42c` | Desktop voice test: voice.status shows My voice and I hear (spec 7.1.7 Q16) |
| 09:43 | `e5eac6f` | Voice page: the Participants row shows the call's state short (spec 7.1.7 Q16) |
| 09:46 | `667c7c4` | Voice scenes: the menu opens early, shots at 8 s (slow X11 software rendering) |
| 10:10 | `8d024a1` (merge) | Merge the Voice page with My voice and I hear rows, I hear nobody, old settings migrated (spec 7.1.7 Q16, 7.1.12; 5.26) |
| 11:11 | `6493daa` | The lips move while a rider is heard speaking: short eased pulses of the lower lip on the near model, never under the X mouth (spec Phase 4 Q24 (a), 5.27) |
| 11:11 | `04ffd3f` (merge) | Merge the lips moving while a rider is heard speaking, never while muted, near model only (spec Phase 4 Q24, 5.27) |
| 12:43 | `46d0aa1` | Release 0.2.5 |
| 12:57 | `30fff7e` | Input mapping stays a row of Settings → Controls (spec 3.2.5 Q1 (a)) |
| 12:58 | `cdd8818` | Wet leaves cost a little speed and add a wobble at speed; with damage on (never in group rides) a corner on wet leaves can end in a slide (spec 4.6.2 Q6 (b), (c)) |
| 13:03 | `0619b50` | Side roads with too little room at junctions: mouth at the main road's edge, blend from the side road's grade, sloped corner – built with J3 (spec 4.8.8 Q6 (d)) |
| 13:08 | `5a433ea` | Voice answers: spatial off keeps the range, a notice when the voice is on but nobody hears it, muted / blocked / 0 % all show headphones (spec 7.1.7 Q21, Q22, Q18) |
| 13:13 | `f8f2c50` | Road damage in the ride: bumps and more rolling resistance on bad surfaces; untagged roads drawn cleaner; damage amounts stay (spec Phase 8 Q12 (c), Q13 (b), Q14 (b)) |
| 13:31 | `3b318f2` | Voice: "nobody hears you" when My voice is turned on and nobody can hear it; Mute for me, 0 % volume and Block show headphones to that rider (spec 7.1.7 Q22 (b), Q18) |
| 13:59 | `bca116c` | scripts/shot-voice-notice.sh: Wayland screenshot of the "nobody hears you" voice notice (spec 7.1.7 Q22 (b)) |
| 14:04 | `da1c2d3` | J3 work in progress: side roads leave the main road's edge at their own grade with sloped corners (4.8.8 Q6 (d)), clusters, forks below 15 degrees, star-shaped outlines |
| 14:10 | `191ef32` (merge) | Merge the nobody-hears-you notice and headphones for muted, blocked and 0 % volume (spec 7.1.7 Q22, Q18; 5.33) |
| 14:12 | `e6b7662` | Built: wet leaves on the road cost a little speed and wobble the bike at speed; with damage on, outside group rides, a fast corner on them can end in a slide (spec 4.6.2 Q6 (b), (c)) |
| 14:13 | `e8684fd` | J3: clusters share one patch, forks below 15 degrees, mini-roundabout discs (section JMRB), fixed point for cluster side arms; star-shape fix dropped (poor surfaces) |
| 14:16 | `bfa1039` | Road damage in the ride: bumps (trainer kick, camera shake, sound, a little speed) and up to 50 % more rolling resistance on bad surfaces, server-authoritative from the drawn damage; untagged roads drawn cleaner (spec Phase 8 Q12 (c), Q14 (b)) |
| 14:16 | `251a1c5` (merge) | Merge origin/main; road damage in the ride renumbered to spec 5.34 |
| 14:18 | `b1ba946` | J3: formatting, cluster and mini-roundabout summary in world-builder junctions, scenes and render script for the J3 before/after |
| 14:23 | `27b86ec` | road_feel: a named type for the located strip (clippy type_complexity) |
| 14:29 | `cfa9219` (merge) | Merge wet leaves on the road: a little speed cost and sway, a slide with damage on outside group rides (spec 4.6.2 Q6, 5.34) |
| 14:30 | `11c0d13` | Road damage's rolling resistance adds to the weather's factor (and wet leaves'), never multiplies it |
| 14:43 | `183780f` | Built: smooth junctions J3 with 4.8.8 Q6 (d) – side roads leave the main road's edge at their own grade with sloped corners, clusters, forks below 15 degrees, mini-roundabout discs; packages, lint tables, open question Q7 on kinks (spec 5.31) |
| 14:44 | `1c7ac68` | road_bumps: rustfmt |
| 15:21 | `36c17cb` | J3: wheel contact on the T junction as the world builder shapes it (the crease at the main road's edge: 12 mm beside the centre), scene names in the J3 render script |
| 15:21 | `69556f2` (merge) | Merge origin/main (wet leaves); road damage in the ride renumbered to spec 5.35, both on the shared rolling-resistance hook |
| 15:23 | `555f03c` | J3: formatting |
| 15:34 | `3388780` (merge) | Merge road damage in the ride (bumps, trainer kick, shake, sound, more rolling resistance) and untagged roads drawn cleaner (spec Phase 8 Q12, Q14; 5.35) |
| 15:36 | `c941bfe` (merge) | Merge remote-tracking branch 'origin/main' into worktree-agent-a326c373840a77e9b |
| 15:36 | `fc97900` | J3 packages: the road condition from OSM (world-builder condition, section RCND) before the junctions |
| 15:45 | `3de92e0` | J3 packages with the OSM road condition (RCND): sizes, times, hashes (spec 5.36) |
| 15:51 | `7325f56` (merge) | Merge junctions J3 and 4.8.8 Q6 (d): side roads from the main road's edge at their own grade, clusters, forks, mini-roundabout discs, section JMRB, JNCT layout 2 (spec 4.8.8, 5.36; new open question 4.8.8 Q7; rebuilt packages not installed) |
| 15:57 | `103ca25` | Street lamps never stand in a road, only beside it (spec: Street lamps rule, 15H) |
| 16:25 | `e88fbd9` | Street lamps never stand in a road: feet beside every carriageway and junction surface, moved along the road or to the kerb, else left out; lint lamp.foot.* (spec 5.38, world look Street lamps rule, 15H) |
| 16:57 | `4684142` | Browser app on iPhones: a lost WebGL context stops the app and loads the ride once, a killed ride rides on with less memory then stops with the reason, phones keep 3 x 3 tiles (spec 14 Phase 10 B7, B2, 5.37) |
| 16:57 | `f24a862` | lamp-rule-shots: drop the Tenerife junction scene (the free-ride start lands on a track away from the lamp) |
| 17:11 | `dc549a0` (merge) | Merge street lamps only beside the road: no pole foot in any carriageway or junction surface, moved to the kerb or along the road or left out, with a lint (spec 5.38) |
| 17:28 | `ebb51df` | iPhone restarts: the WebGPU fallback is loop-proof by its URL alone, so it keeps falling back once per ride and remembering the failure (test-web-gpu's same-tab cases; spec 5.37) |
| 17:53 | `8ed1061` (merge) | Merge the fix for the browser app restarting on an iPhone: a lost WebGL context stops the app, no fallback reload loop, a killed tab rides on with less memory once, phones keep fewer tiles (spec Phase 10 B7, 5.39) |
| 17:59 | `a2fc2b0` | Riders move smoothly at 25 fps: a snapshot read a frame late is extrapolated and timed by its server tick (spec 6.3 Fixed v5.38) |
| 17:59 | `d02da08` (merge) | Merge smooth rider motion when snapshots are read a tick late (low frame rates, 25 fps capture videos): snapshots timed by their server tick (spec 6.3, 5.40) |

## Builds and build servers

137 build/test runs on the build machines, 21.0 h in total, 7 failed; 1440 server samples; cargo compiled 7618 crates in 3.2 h, 2.9 h waiting for build slots.

| Machine | Runs | Hours | Cargo h | Crates | Waited h | Failed | Online |
|---|---|---|---|---|---|---|---|
| Weela | 0 | 0.0 | 0.0 | 0 | 0.0 | 0 | 0% |
| Win11Builder | 9 | 2.0 | 0.8 | 808 | 0.2 | 1 | 100% |
| leela | 26 | 1.8 | 0.0 | 0 | 0.2 | 1 | 100% |
| macos | 14 | 0.2 | 0.1 | 138 | 0.0 | 1 | 100% |
| marge | 88 | 16.9 | 2.3 | 6672 | 2.5 | 4 | 100% |

Failed runs:

- 09:46 marge: `cargo fmt --all && cargo run -q -p ocw-assets --release -- model export-all 2>&1` (exit 128, log `build-log/094625-marge-2412709.log`)
- 13:17 macos: `cargo test -p ocw-world leaves && cargo test -p ocw-sim leaves && cargo test -p ` (exit 101, log `build-log/131708-macos-2804545.log`)
- 13:22 marge: `OCW_J3_OUT=$HOME/src/OCW/data/j3-build/iter scripts/j3-build.sh pilot/liechtenst` (exit 127, log `build-log/132249-marge-2815068.log`)
- 13:59 leela: `cargo run -q --release -p ocw-world --example feel_spots -- ~/ocw-feel-data/liec` (exit 1, log `build-log/135943-leela-2875036.log`)
- 14:16 Win11Builder: `cargo clippy -p ocw-desktop --all-targets -- -D warnings 2>&1 | Select-Object -L` (exit 101, log `build-log/141653-Win11Builder-2937292.log`)
- 14:37 marge: `scripts/j3-scenes.sh adlerkreisel,bergstrasse,kaltenbronner,medianias,bf-narrow,` (exit 2, log `build-log/143741-marge-2971119.log`)
- 16:08 marge: `bash ~/tmp/ocw-ios-a35a/base.sh` (exit 127, log `build-log/160859-marge-3190933.log`)

Longest runs:

- 61 min on marge: `cargo fmt --all; git diff --stat 2>/dev/null | tail -3; make check > $HOME/tmp/m`
- 51 min on marge: `set -e; make check; make test-smoke; echo ALL-CHECKS-OK`
- 45 min on marge: `make check > $HOME/tmp/lamp-check.log 2>&1; echo check=$?; make test-web-build >`
- 44 min on marge: `set -e; make check; make test-smoke; make test-web; echo ALL-CHECKS-OK`
- 41 min on marge: `source ~/.cargo/env; for t in test-web-build test-web-gpu test-web test-web-webk`

## Token usage

761.3 M tokens in 2,275 model messages (output 1.3 M, cache reads 750.7 M, cache writes 9.3 M, uncached input 5 k). Full breakdown: [tokens.json](tokens.json).

| Feature | Tokens | Output | Messages |
|---|---|---|---|
| Other | 315.6 M | 674 k | 866 |
| Planning & spec | 167.3 M | 265 k | 559 |
| Audio & voice | 100.9 M | 178 k | 355 |
| Materials & look | 84.2 M | 36 k | 101 |
| Riders & bikes | 45.1 M | 93 k | 203 |
| Build, release & infra | 19.5 M | 38 k | 86 |
| Art project | 11.8 M | 42 k | 83 |
| Worlds & terrain | 10.9 M | 8 k | 14 |
| UI & menus | 5.9 M | 5 k | 8 |

| Task | Feature | Tokens | Output |
|---|---|---|---|
| agent: Junctions J3 with side-road fix (Q6 d) | Other | 192.9 M | 349 k |
| agent: Road damage in the ride (Phase 8 Q12, Q14) | Planning & spec | 96.3 M | 150 k |
| agent: Fix the browser app restarting on iOS | Planning & spec | 53.0 M | 106 k |
| agent: Voice page: My voice and I hear | Audio & voice | 50.6 M | 105 k |
| coordination: i see the ingame graphics realy qquick, like a coiple of ms and then it restart | Materials & look | 48.7 M | 17 k |
| agent: Wet leaves affect the ride (4.6.2 Q6) | Other | 47.1 M | 128 k |
| agent: Fix jumpy/laggy rider motion (regression) | Riders & bikes | 39.7 M | 88 k |
| coordination: Answers: **Phase 8 – Textures and Regional Look** - **Phase 8 Q12 – Potholes in … | Materials & look | 35.4 M | 19 k |
| agent: Street lamps only beside the road | Other | 35.0 M | 109 k |
| agent: Lips move while speaking (Q24) | Other | 30.1 M | 85 k |
| coordination: Answers to open questeions follow here: **7.1.7 Open questions (for the user)** … | Audio & voice | 29.5 M | 8 k |
| agent: Voice Q22 notice, Q18 headphones | Audio & voice | 18.0 M | 62 k |
| coordination: update open question section | Planning & spec | 16.4 M | 9 k |
| agent: Day 11 video (21 Nov), art README | Art project | 11.8 M | 42 k |
| agent: Release 0.2.5, all platforms + web | Build, release & infra | 9.0 M | 30 k |
| coordination: one rule for the world (save it in the according spec sections): do not put ligh… | Worlds & terrain | 5.0 M | 3 k |
| coordination: Answers: **7.1.7 Open questions (for the user)** - **7.1.7 Q21 – voice.spatial o… | UI & menus | 4.5 M | 3 k |
| coordination: i am on ios 26 with an iphone 15 | Other | 4.2 M | 1 k |
| coordination: Browser version seems to be broken, keeps restarting on my IOS. Test and fix. | Build, release & infra | 4.1 M | 3 k |
| coordination: bump version and build a new release, upload to GH | Build, release & infra | 3.6 M | 3 k |
| coordination: Answer: **4.8.8 Smooth junctions (investigation 2026-11-15; J1 built 2026-11-16,… | Worlds & terrain | 3.0 M | 3 k |
| coordination: Answer: **4.6.2 Near-field ground detail (planned and built 2026-11-17, v4.72)**… | Riders & bikes | 2.9 M | 3 k |
| coordination: is the git history of OCW clean from all (unneeded) images/binaries now? | Worlds & terrain | 2.9 M | 2 k |
| coordination: answer: **Phase 4 Q24 â€“ The mouth while speaking (follow-up of the face):** si… | Audio & voice | 2.8 M | 2 k |
| coordination: q16 build proposal | Build, release & infra | 2.7 M | 2 k |
| coordination: give me a summary of the7.1.16 layout and q16 | Other | 2.7 M | 2 k |
| coordination: I noticed that the rider does not move smooth anymore, its laggy/jumpy. investig… | Riders & bikes | 2.5 M | 2 k |
| coordination: Is the day 11 video already created? | Other | 2.1 M | 1 k |
| coordination: i tried opening it on safari and firefox on ios, both in the browser | Planning & spec | 1.7 M | 1 k |
| coordination: i only saw the jumping in the videos, didnt test the desktop app yet. | Other | 1.7 M | 1 k |
| coordination: Answer open question: **3.2.5 Input mapping, and the junction's exits on Delete … | UI & menus | 1.5 M | 1 k |

## Prompts

19 prompts (full text: [prompts.md](prompts.md)).

| Time | Prompt |
|---|---|
| 09:08 | give me a summary of the7.1.16 layout and q16 |
| 09:08 | Is the day 11 video already created? |
| 09:13 | q16 build proposal |
| 09:39 | answer:  **Phase 4 Q24 â€“ The mouth while speaking (follow-up of the face):** since v4.47 riders have faces with lips. The voice chat alrea |
| 09:40 | update open question section |
| 12:41 | bump version and build a new release, upload to GH |
| 12:55 | is the git history of OCW clean from all (unneeded) images/binaries now? |
| 12:57 | Answer open question: **3.2.5 Input mapping, and the junction's exits on Delete / Page Down (2026-11-21; built v5.21)**  - **3.2.5 Q1 – Wher |
| 12:58 | Answer:   **4.6.2 Near-field ground detail (planned and built 2026-11-17, v4.72)**  - **4.6.2 Q6 – Wet leaves on the road and the ride:** th |
| 13:03 | Answer:   **4.8.8 Smooth junctions (investigation 2026-11-15; J1 built 2026-11-16, J2 built 2026-11-19, J3 planned)**  - **4.8.8 Q6 – Side r |
| 13:08 | Answers: **7.1.7 Open questions (for the user)**  - **7.1.7 Q21 – voice.spatial off with the hearing range:** voice is normally spatial: oth |
| 13:13 | Answers:  **Phase 8 – Textures and Regional Look**  - **Phase 8 Q12 – Potholes in the ride feel:** since v4.75 the roads show cracks, pothol |
| 15:55 | Browser version seems to be broken, keeps restarting on my IOS. Test and fix. |
| 15:57 | one rule for the world (save it in the according spec sections): do not put lights/latern poles in the road, only at the side. |
| 16:07 | I noticed that the rider does not move smooth anymore, its laggy/jumpy. investigate and fix. |
| 16:08 | i only saw the jumping in the videos, didnt test the desktop app yet. |
| 16:09 | i am on ios 26 with an iphone 15 |
| 16:21 | i tried opening it on safari and firefox on ios, both in the browser |
| 16:22 | i see the ingame graphics realy qquick, like a coiple of ms and then it restart |

## Features

17 spec versions added, 9 landed by a merge; 4 deploys, 1 releases.

| Spec | Feature | Landed | Check (marge) |
|---|---|---|---|
| 5.24 | The Voice page gets two separate rows | 09:13 `a075e44` | – |
| 5.25 | The lips move while a rider is heard speaking | 09:39 `2688a68` | – |
| 5.26 | Built: the Voice page has two separate rows, *My voice* and *I hear* | 10:10 `8d024a1` (merge) | – |
| 5.27 | Built: the lips move while a rider is heard speaking | 11:11 `04ffd3f` (merge) | – |
| 5.28 | Input mapping stays a row of Settings → Controls | 12:57 `30fff7e` | – |
| 5.29 | Wet leaves on the road cost a little speed and add a small wobble at speed | 12:58 `cdd8818` | – |
| 5.30 | Side roads with too little room at junctions | 13:03 `0619b50` | – |
| 5.31 | Voice answers | 13:08 `5a433ea` | – |
| 5.32 | Road damage in the ride | 13:13 `f8f2c50` | – |
| 5.33 | Voice: "nobody hears you" on the HUD when My voice is turned on and nobody can hear it | 14:10 `191ef32` (merge) | – |
| 5.34 | Built: wet leaves on the road cost a little speed and wobble the bike at speed | 14:29 `cfa9219` (merge) | ok at 14:29, 74 suites, 3167 passed, 0 failed (commit) |
| 5.35 | Road damage in the ride built | 15:34 `3388780` (merge) | ok at 15:21 (commit) |
| 5.36 | Built: smooth junctions J3 with 4.8.8 Q6 | 15:51 `7325f56` (merge) | ok at 16:15, 3 suites, 101 passed, 0 failed (commit) |
| 5.37 | Street lamps never stand in a road, only beside it | 15:57 `103ca25` | – |
| 5.38 | Built: street lamps never stand in a road | 17:11 `dc549a0` (merge) | – |
| 5.39 | Fixed: the browser app restarting on an iPhone | 17:53 `8ed1061` (merge) | ok at 17:54, 74 suites, 3202 passed, 0 failed (commit) |
| 5.40 | The riders move smoothly again at 25 frames a second | 17:59 `d02da08` (merge) | ok at 18:00, 74 suites, 3207 passed, 0 failed (commit) |

Deploys:

- 11:13 marge: `04ffd3f` (ok)
- 11:14 leela: `04ffd3f` (ok)
- 18:46 marge: `d02da08` (ok)
- 18:47 leela: `d02da08` (ok)

Releases:

- 20:27 v0.2.5 (pre-release)

## Agent jobs

11 jobs (coordinator log agents.jsonl).

| Task | Branch | Start | End | Status | Interrupted | Merged |
|---|---|---|---|---|---|---|
| Day 11 video (2026-11-21) | a4a3008b | 00:09 | 00:32 | merged |  |  |
| Voice page: My voice and I hear (7.1.7 Q16) | abf67c31 | 09:13 | 10:11 | merged |  |  |
| Lips move while speaking (Phase 4 Q24) | a3bc704e | 09:40 | 11:13 | merged |  |  |
| Release 0.2.5, all platforms + web | afe2e619 | 12:41 | 20:30 | merged |  |  |
| Wet leaves affect the ride (4.6.2 Q6) | a3aeb030 | 12:59 | 15:22 | merged |  |  |
| Junctions J3 with side-road fix (4.8.8 Q6 d) | a326c373 | 13:03 | 15:52 | merged |  |  |
| Voice Q22 notice, Q18 headphones | a8c0efe2 | 13:09 | 14:12 | merged |  |  |
| Road damage in the ride (Phase 8 Q12, Q14) | addcd5dd | 13:13 | 15:35 | merged |  |  |
| Fix the browser app restarting on iOS | a35a158a | 15:56 | 17:55 | merged |  |  |
| Street lamps only beside the road | a7af0f87 | 15:58 | 17:13 | merged |  |  |
| Fix jumpy/laggy rider motion (regression) | a6ffd7a9 | 16:08 | 18:45 | merged |  |  |

## Incidents

36 collected (disk-full 1, janitor-delete 29, machine-offline 3, machine-online 2, runs-failed 1), 0 with root-cause notes ([incidents.md](incidents.md)).

| Time | Kind | Machine | What |
|---|---|---|---|
| 00:00 | machine-offline | Weela | Weela unreachable (no route to host) |
| 00:00 | disk-full | Win11Builder | disk C: on Win11Builder at 96 % |
| 10:10 | janitor-delete | marge | janitor delete OCW-worktree-agent-abf67c311ed0566a9/target (37.6 GB) |
| 10:10 | janitor-delete | leela | janitor delete OCW-worktree-agent-abf67c311ed0566a9/target (6.6 GB) |
| 11:12 | janitor-delete | marge | janitor delete OCW-worktree-agent-a3bc704eeaa8ea44c/target (41.5 GB) |
| 11:12 | janitor-delete | leela | janitor delete OCW-worktree-agent-a3bc704eeaa8ea44c/target (18.9 GB) |
| 12:15 | janitor-delete | Win11Builder | janitor delete OCW-worktree-agent-abf67c311ed0566a9/target (8.5 GB) |
| 14:11 | janitor-delete | marge | janitor delete OCW-worktree-agent-a8c0efe2aadc28186/target (41.3 GB) |
| 15:21 | janitor-delete | marge | janitor delete OCW-merge-leaves/target (26.2 GB) |
| 15:21 | janitor-delete | marge | janitor delete OCW-worktree-agent-a3aeb030bfa96a3ea/target (34.0 GB) |
| 15:34 | janitor-delete | marge | janitor delete OCW-worktree-agent-addcd5dd97528cec7/target (43.0 GB) |
| 15:34 | janitor-delete | leela | janitor delete OCW-worktree-agent-addcd5dd97528cec7/target (15.4 GB) |
| 15:51 | janitor-delete | marge | janitor delete OCW-worktree-agent-a326c373840a77e9b/target (47.5 GB) |
| 15:51 | janitor-delete | leela | janitor delete OCW-worktree-agent-a326c373840a77e9b/target (0.5 GB) |
| 16:08 | runs-failed | Win11Builder, leela, macos, marge | 7 failed remote.sh runs (Win11Builder 1, leela 1, macos 1, marge 4) |
| 16:10 | janitor-delete | Win11Builder | janitor delete OCW-worktree-agent-a8c0efe2aadc28186/target (8.9 GB) |
| 16:20 | janitor-delete | Win11Builder | janitor delete OCW-worktree-agent-a3aeb030bfa96a3ea/target (2.8 GB) |
| 16:29 | janitor-delete | macos | janitor delete OCW-worktree-agent-a326c373840a77e9b/target (3.1 GB) |
| 16:29 | janitor-delete | macos | janitor delete OCW-worktree-agent-a3aeb030bfa96a3ea/target (1.1 GB) |
| 16:29 | janitor-delete | macos | janitor delete OCW-worktree-agent-addcd5dd97528cec7/target (1.2 GB) |
| 16:57 | janitor-delete | marge | janitor delete OCW-lamp-rule-before/target (3.3 GB) |
| 17:12 | janitor-delete | marge | janitor delete OCW-worktree-agent-a7af0f878b7bd5a0b/target (34.1 GB) |
| 17:31 | janitor-delete | Win11Builder | janitor delete OCW-worktree-agent-addcd5dd97528cec7/target (2.8 GB) |
| 17:54 | janitor-delete | marge | janitor delete OCW-worktree-agent-a35a158ad167e5cc0/target (35.8 GB) |
| 18:44 | janitor-delete | marge | janitor delete OCW-merge-motion/target (31.7 GB) |
| 18:44 | janitor-delete | marge | janitor delete OCW-merge-ios/target (21.7 GB) |
| 18:44 | janitor-delete | marge | janitor delete OCW-fix-rider-motion-jitter/target (34.9 GB) |
| 18:44 | janitor-delete | leela | janitor delete OCW-fix-rider-motion-jitter/target (3.2 GB) |
| 20:28 | janitor-delete | marge | janitor delete OCW-HEAD/target (16.6 GB) |
| 20:28 | janitor-delete | macos | janitor delete OCW-HEAD/target (9.8 GB) |
| 20:29 | janitor-delete | Win11Builder | janitor failed OCW-HEAD/target (0.0 GB) |
| 21:04 | machine-offline | Win11Builder | Win11Builder unreachable (ssh error) |
| 21:06 | machine-online | Win11Builder | Win11Builder back online |
| 22:05 | janitor-delete | Win11Builder | janitor delete OCW/target (0.2 GB) |
| 22:15 | machine-offline | Win11Builder | Win11Builder unreachable (timeout) |
| 22:16 | machine-online | Win11Builder | Win11Builder back online |

## Media

| Time | File |
|---|---|
| 09:42:45 | [094245-shot-wayland-menu-voice-rows.jpg](094245-shot-wayland-menu-voice-rows.jpg) |
| 09:42:52 | [094252-shot-wayland-menu-voice-rows-on-selected-nobody.jpg](094252-shot-wayland-menu-voice-rows-on-selected-nobody.jpg) |
| 09:42:58 | [094258-shot-wayland-hud-voice-line.jpg](094258-shot-wayland-hud-voice-line.jpg) |
| 09:43:56 | [094356-shot-menu-voice-rows.jpg](094356-shot-menu-voice-rows.jpg) |
| 09:44:11 | [094411-shot-menu-voice-rows-on-selected-nobody.jpg](094411-shot-menu-voice-rows-on-selected-nobody.jpg) |
| 09:44:25 | [094425-shot-hud-voice-line.jpg](094425-shot-hud-voice-line.jpg) |
| 09:44:35 | [094435-shot-wayland-menu-voice-rows.jpg](094435-shot-wayland-menu-voice-rows.jpg) |
| 09:44:42 | [094442-shot-wayland-menu-voice-rows-on-selected-nobody.jpg](094442-shot-wayland-menu-voice-rows-on-selected-nobody.jpg) |
| 09:44:48 | [094448-shot-wayland-hud-voice-line.jpg](094448-shot-wayland-hud-voice-line.jpg) |
| 09:47:22 | [094722-shot-menu-voice-rows.jpg](094722-shot-menu-voice-rows.jpg) |
| 09:47:39 | [094739-shot-menu-voice-rows-on-selected-nobody.jpg](094739-shot-menu-voice-rows-on-selected-nobody.jpg) |
| 09:47:56 | [094756-shot-hud-voice-line.jpg](094756-shot-hud-voice-line.jpg) |
| 09:54:46 | [095446-q16-voice-rows-browser-hud-voice-line.jpg](095446-q16-voice-rows-browser-hud-voice-line.jpg) |
| 09:54:46 | [095446-q16-voice-rows-browser-voice-page-on-selected-nobody.jpg](095446-q16-voice-rows-browser-voice-page-on-selected-nobody.jpg) |
| 09:54:46 | [095446-q16-voice-rows-browser-voice-page.jpg](095446-q16-voice-rows-browser-voice-page.jpg) |
| 10:44:31 | [104431-q24-lips-lips-muted.jpg](104431-q24-lips-lips-muted.jpg) |
| 10:44:31 | [104431-q24-lips-lips-muted.mp4](104431-q24-lips-lips-muted.mp4) |
| 10:44:31 | [104431-q24-lips-lips-speaking-mouth-frames.png](104431-q24-lips-lips-speaking-mouth-frames.png) |
| 10:44:31 | [104431-q24-lips-lips-speaking.jpg](104431-q24-lips-lips-speaking.jpg) |
| 10:44:31 | [104431-q24-lips-lips-speaking.mp4](104431-q24-lips-lips-speaking.mp4) |
| 10:50:52 | [105052-shot-ocw.jpg](105052-shot-ocw.jpg) |
| 10:51:01 | [105101-shot-wayland-ocw-wayland.jpg](105101-shot-wayland-ocw-wayland.jpg) |
| 11:06:23 | [110623-web-web-calendar-select.jpg](110623-web-web-calendar-select.jpg) |
| 11:06:23 | [110623-web-web-calendar.jpg](110623-web-web-calendar.jpg) |
| 11:06:23 | [110623-web-web-console.jpg](110623-web-web-console.jpg) |
| 11:06:23 | [110623-web-web-damage-crash.jpg](110623-web-web-damage-crash.jpg) |
| 11:06:23 | [110623-web-web-damage-fresh.jpg](110623-web-web-damage-fresh.jpg) |
| 11:06:23 | [110623-web-web-devices-collapsed.jpg](110623-web-web-devices-collapsed.jpg) |
| 11:06:23 | [110623-web-web-devices-expanded.jpg](110623-web-web-devices-expanded.jpg) |
| 11:06:23 | [110623-web-web-downloads-OCW-2026-11-22-11-07-51.jpg](110623-web-web-downloads-OCW-2026-11-22-11-07-51.jpg) |
| 11:06:23 | [110623-web-web-downloads-ocw-2026-11-22-11-08-18.webm](110623-web-web-downloads-ocw-2026-11-22-11-08-18.webm) |
| 11:06:23 | [110623-web-web-gamepad.jpg](110623-web-web-gamepad.jpg) |
| 11:06:23 | [110623-web-web-gps.jpg](110623-web-web-gps.jpg) |
| 11:06:23 | [110623-web-web-history-delete.jpg](110623-web-web-history-delete.jpg) |
| 11:06:23 | [110623-web-web-history-ride-file.jpg](110623-web-web-history-ride-file.jpg) |
| 11:06:23 | [110623-web-web-history-ride-map.jpg](110623-web-web-history-ride-map.jpg) |
| 11:06:23 | [110623-web-web-hud.jpg](110623-web-web-hud.jpg) |
| 11:06:23 | [110623-web-web-input-mapping-capture.jpg](110623-web-web-input-mapping-capture.jpg) |
| 11:06:23 | [110623-web-web-input-mapping-junctions.jpg](110623-web-web-input-mapping-junctions.jpg) |
| 11:06:23 | [110623-web-web-input-mapping-swapped.jpg](110623-web-web-input-mapping-swapped.jpg) |
| 11:06:23 | [110623-web-web-input-mapping.jpg](110623-web-web-input-mapping.jpg) |
| 11:06:23 | [110623-web-web-join.jpg](110623-web-web-join.jpg) |
| 11:06:23 | [110623-web-web-menu.jpg](110623-web-web-menu.jpg) |
| 11:06:23 | [110623-web-web-photo-preview.jpg](110623-web-web-photo-preview.jpg) |
| 11:06:23 | [110623-web-web-ride.jpg](110623-web-web-ride.jpg) |
| 11:06:23 | [110623-web-web-riders.jpg](110623-web-web-riders.jpg) |
| 11:06:23 | [110623-web-web-settings.jpg](110623-web-web-settings.jpg) |
| 11:06:23 | [110623-web-web-strava-recording-downloaded.jpg](110623-web-web-strava-recording-downloaded.jpg) |
| 11:06:23 | [110623-web-web-strava-recording-saved-to-folder.jpg](110623-web-web-strava-recording-saved-to-folder.jpg) |
| 11:06:23 | [110623-web-web-strava-recording.jpg](110623-web-web-strava-recording.jpg) |
| 11:06:23 | [110623-web-web-strava-row.jpg](110623-web-web-strava-row.jpg) |
| 11:06:23 | [110623-web-web-strava-steps.jpg](110623-web-web-strava-steps.jpg) |
| 11:06:23 | [110623-web-web-touch-hints.jpg](110623-web-web-touch-hints.jpg) |
| 11:06:23 | [110623-web-web-touch-hold.jpg](110623-web-web-touch-hold.jpg) |
| 11:06:23 | [110623-web-web-unicorn-flight.jpg](110623-web-web-unicorn-flight.jpg) |
| 11:06:23 | [110623-web-web-unicorn-inspect.jpg](110623-web-web-unicorn-inspect.jpg) |
| 11:06:23 | [110623-web-web-unicorn-menu.jpg](110623-web-web-unicorn-menu.jpg) |
| 11:06:23 | [110623-web-web-weather.jpg](110623-web-web-weather.jpg) |
| 11:06:23 | [110623-web-web-workout-map.jpg](110623-web-web-workout-map.jpg) |
| 11:06:23 | [110623-web-web.jpg](110623-web-web.jpg) |
| 13:38:24 | [133824-shot-wayland-status-headphones-zero-volume.jpg](133824-shot-wayland-status-headphones-zero-volume.jpg) |
| 13:46:36 | [134636-shot-wayland-status-headphones-mute-and-zero-volume.jpg](134636-shot-wayland-status-headphones-mute-and-zero-volume.jpg) |
| 13:58:41 | [135841-voice-notice-2026-11-22-nobody-hears-you.jpg](135841-voice-notice-2026-11-22-nobody-hears-you.jpg) |
| 14:10:43 | [141043-wet-leaves-bf-wet-leaves-slide-wayland.jpg](141043-wet-leaves-bf-wet-leaves-slide-wayland.jpg) |
| 14:10:47 | [141047-2026-11-22-road-feel-shot-wayland-feel-after-vaduz-residential.jpg](141047-2026-11-22-road-feel-shot-wayland-feel-after-vaduz-residential.jpg) |
| 14:10:48 | [141048-wet-leaves-bf-wet-leaves-slide-wayland.mp4](141048-wet-leaves-bf-wet-leaves-slide-wayland.mp4) |
| 14:10:57 | [141057-2026-11-22-road-feel-shot-wayland-feel-after-vaduz-secondary.jpg](141057-2026-11-22-road-feel-shot-wayland-feel-after-vaduz-secondary.jpg) |
| 14:11:08 | [141108-2026-11-22-road-feel-shot-wayland-feel-after-vaduz-primary.jpg](141108-2026-11-22-road-feel-shot-wayland-feel-after-vaduz-primary.jpg) |
| 14:11:22 | [141122-2026-11-22-road-feel-shot-wayland-feel-after-blackforest-primary.jpg](141122-2026-11-22-road-feel-shot-wayland-feel-after-blackforest-primary.jpg) |
| 14:11:35 | [141135-2026-11-22-road-feel-shot-wayland-feel-after-blackforest-residential.jpg](141135-2026-11-22-road-feel-shot-wayland-feel-after-blackforest-residential.jpg) |
| 14:11:35 | [141135-wet-leaves-bf-wet-leaves-wobble-wayland.jpg](141135-wet-leaves-bf-wet-leaves-wobble-wayland.jpg) |
| 14:11:40 | [141140-wet-leaves-bf-wet-leaves-wobble-wayland.mp4](141140-wet-leaves-bf-wet-leaves-wobble-wayland.mp4) |
| 14:11:47 | [141147-2026-11-22-road-feel-shot-wayland-feel-after-tenerife-primary.jpg](141147-2026-11-22-road-feel-shot-wayland-feel-after-tenerife-primary.jpg) |
| 14:12:00 | [141200-2026-11-22-road-feel-shot-wayland-feel-after-tenerife-residential.jpg](141200-2026-11-22-road-feel-shot-wayland-feel-after-tenerife-residential.jpg) |
| 14:12:10 | [141210-2026-11-22-road-feel-shot-wayland-feel-after-vaduz-tagged-bad.jpg](141210-2026-11-22-road-feel-shot-wayland-feel-after-vaduz-tagged-bad.jpg) |
| 14:12:44 | [141244-2026-11-22-road-feel-shot-wayland-feel-before-vaduz-residential.jpg](141244-2026-11-22-road-feel-shot-wayland-feel-before-vaduz-residential.jpg) |
| 14:12:54 | [141254-2026-11-22-road-feel-shot-wayland-feel-before-vaduz-secondary.jpg](141254-2026-11-22-road-feel-shot-wayland-feel-before-vaduz-secondary.jpg) |
| 14:13:04 | [141304-2026-11-22-road-feel-shot-wayland-feel-before-vaduz-primary.jpg](141304-2026-11-22-road-feel-shot-wayland-feel-before-vaduz-primary.jpg) |
| 14:13:17 | [141317-2026-11-22-road-feel-shot-wayland-feel-before-blackforest-primary.jpg](141317-2026-11-22-road-feel-shot-wayland-feel-before-blackforest-primary.jpg) |
| 14:13:29 | [141329-2026-11-22-road-feel-shot-wayland-feel-before-blackforest-residential.jpg](141329-2026-11-22-road-feel-shot-wayland-feel-before-blackforest-residential.jpg) |
| 14:13:41 | [141341-2026-11-22-road-feel-shot-wayland-feel-before-tenerife-primary.jpg](141341-2026-11-22-road-feel-shot-wayland-feel-before-tenerife-primary.jpg) |
| 14:13:53 | [141353-2026-11-22-road-feel-shot-wayland-feel-before-tenerife-residential.jpg](141353-2026-11-22-road-feel-shot-wayland-feel-before-tenerife-residential.jpg) |
| 14:14:04 | [141404-2026-11-22-road-feel-shot-wayland-feel-before-vaduz-tagged-bad.jpg](141404-2026-11-22-road-feel-shot-wayland-feel-before-vaduz-tagged-bad.jpg) |
| 14:14:16 | [141416-2026-11-22-road-feel-shot-wayland-feel-before-blackforest-tagged-bad.jpg](141416-2026-11-22-road-feel-shot-wayland-feel-before-blackforest-tagged-bad.jpg) |
| 14:14:29 | [141429-2026-11-22-road-feel-shot-wayland-feel-after-blackforest-tagged-bad.jpg](141429-2026-11-22-road-feel-shot-wayland-feel-after-blackforest-tagged-bad.jpg) |
| 14:15:37 | [141537-2026-11-22-road-feel-video-wayland-feel-ride-blackforest-bad-1280.mp4](141537-2026-11-22-road-feel-video-wayland-feel-ride-blackforest-bad-1280.mp4) |
| 14:15:37 | [141537-2026-11-22-road-feel-video-wayland-feel-ride-blackforest-bad.jpg](141537-2026-11-22-road-feel-video-wayland-feel-ride-blackforest-bad.jpg) |
| 14:15:37 | [141537-2026-11-22-road-feel-video-wayland-feel-ride-blackforest-bad.mp4](141537-2026-11-22-road-feel-video-wayland-feel-ride-blackforest-bad.mp4) |
| 14:55:32 | [145532-junctions-j3-before-wayland-junction-bergstrasse-rider.jpg](145532-junctions-j3-before-wayland-junction-bergstrasse-rider.jpg) |
| 14:55:42 | [145542-junctions-j3-before-wayland-junction-bergstrasse-drone.jpg](145542-junctions-j3-before-wayland-junction-bergstrasse-drone.jpg) |
| 14:55:53 | [145553-junctions-j3-before-wayland-junction-adlerkreisel-rider.jpg](145553-junctions-j3-before-wayland-junction-adlerkreisel-rider.jpg) |
| 14:56:03 | [145603-junctions-j3-before-wayland-junction-adlerkreisel-drone.jpg](145603-junctions-j3-before-wayland-junction-adlerkreisel-drone.jpg) |
| 14:56:17 | [145617-junctions-j3-before-wayland-junction-kaltenbronner-rider.jpg](145617-junctions-j3-before-wayland-junction-kaltenbronner-rider.jpg) |
| 14:56:30 | [145630-junctions-j3-before-wayland-junction-kaltenbronner-drone.jpg](145630-junctions-j3-before-wayland-junction-kaltenbronner-drone.jpg) |
| 14:56:43 | [145643-junctions-j3-before-wayland-junction-medianias-rider.jpg](145643-junctions-j3-before-wayland-junction-medianias-rider.jpg) |
| 14:56:57 | [145657-junctions-j3-before-wayland-junction-medianias-drone.jpg](145657-junctions-j3-before-wayland-junction-medianias-drone.jpg) |
| 14:57:10 | [145710-junctions-j3-before-wayland-junction-bf-narrow-rider.jpg](145710-junctions-j3-before-wayland-junction-bf-narrow-rider.jpg) |
| 14:57:23 | [145723-junctions-j3-before-wayland-junction-bf-narrow-drone.jpg](145723-junctions-j3-before-wayland-junction-bf-narrow-drone.jpg) |
| 14:57:35 | [145735-junctions-j3-before-wayland-junction-fork-rider.jpg](145735-junctions-j3-before-wayland-junction-fork-rider.jpg) |
| 14:57:46 | [145746-junctions-j3-before-wayland-junction-fork-drone.jpg](145746-junctions-j3-before-wayland-junction-fork-drone.jpg) |
| 14:57:56 | [145756-junctions-j3-before-wayland-junction-dual-rider.jpg](145756-junctions-j3-before-wayland-junction-dual-rider.jpg) |
| 14:58:07 | [145807-junctions-j3-before-wayland-junction-dual-drone.jpg](145807-junctions-j3-before-wayland-junction-dual-drone.jpg) |
| 14:58:18 | [145818-junctions-j3-before-wayland-junction-mini-rider.jpg](145818-junctions-j3-before-wayland-junction-mini-rider.jpg) |
| 14:58:29 | [145829-junctions-j3-before-wayland-junction-mini-drone.jpg](145829-junctions-j3-before-wayland-junction-mini-drone.jpg) |
| 14:58:41 | [145841-junctions-j3-after-wayland-junction-bergstrasse-rider.jpg](145841-junctions-j3-after-wayland-junction-bergstrasse-rider.jpg) |
| 14:58:53 | [145853-junctions-j3-after-wayland-junction-bergstrasse-drone.jpg](145853-junctions-j3-after-wayland-junction-bergstrasse-drone.jpg) |
| 14:59:04 | [145904-junctions-j3-after-wayland-junction-adlerkreisel-rider.jpg](145904-junctions-j3-after-wayland-junction-adlerkreisel-rider.jpg) |
| 14:59:16 | [145916-junctions-j3-after-wayland-junction-adlerkreisel-drone.jpg](145916-junctions-j3-after-wayland-junction-adlerkreisel-drone.jpg) |
| 14:59:30 | [145930-junctions-j3-after-wayland-junction-kaltenbronner-rider.jpg](145930-junctions-j3-after-wayland-junction-kaltenbronner-rider.jpg) |
| 14:59:44 | [145944-junctions-j3-after-wayland-junction-kaltenbronner-drone.jpg](145944-junctions-j3-after-wayland-junction-kaltenbronner-drone.jpg) |
| 14:59:58 | [145958-junctions-j3-after-wayland-junction-medianias-rider.jpg](145958-junctions-j3-after-wayland-junction-medianias-rider.jpg) |
| 15:00:12 | [150012-junctions-j3-after-wayland-junction-medianias-drone.jpg](150012-junctions-j3-after-wayland-junction-medianias-drone.jpg) |
| 15:00:26 | [150026-junctions-j3-after-wayland-junction-bf-narrow-rider.jpg](150026-junctions-j3-after-wayland-junction-bf-narrow-rider.jpg) |
| 15:00:40 | [150040-junctions-j3-after-wayland-junction-bf-narrow-drone.jpg](150040-junctions-j3-after-wayland-junction-bf-narrow-drone.jpg) |
| 15:00:51 | [150051-junctions-j3-after-wayland-junction-fork-rider.jpg](150051-junctions-j3-after-wayland-junction-fork-rider.jpg) |
| 15:01:03 | [150103-junctions-j3-after-wayland-junction-fork-drone.jpg](150103-junctions-j3-after-wayland-junction-fork-drone.jpg) |
| 15:01:14 | [150114-junctions-j3-after-wayland-junction-dual-rider.jpg](150114-junctions-j3-after-wayland-junction-dual-rider.jpg) |
| 15:01:26 | [150126-junctions-j3-after-wayland-junction-dual-drone.jpg](150126-junctions-j3-after-wayland-junction-dual-drone.jpg) |
| 15:01:37 | [150137-junctions-j3-after-wayland-junction-mini-rider.jpg](150137-junctions-j3-after-wayland-junction-mini-rider.jpg) |
| 15:01:49 | [150149-junctions-j3-after-wayland-junction-mini-drone.jpg](150149-junctions-j3-after-wayland-junction-mini-drone.jpg) |
| 15:02:11 | [150211-junctions-j3-before-x11-junction-bergstrasse-rider.jpg](150211-junctions-j3-before-x11-junction-bergstrasse-rider.jpg) |
| 15:02:53 | [150253-junctions-j3-before-x11-junction-bergstrasse-drone.jpg](150253-junctions-j3-before-x11-junction-bergstrasse-drone.jpg) |
| 15:03:27 | [150327-junctions-j3-before-x11-junction-adlerkreisel-rider.jpg](150327-junctions-j3-before-x11-junction-adlerkreisel-rider.jpg) |
| 15:03:55 | [150355-junctions-j3-before-x11-junction-adlerkreisel-drone.jpg](150355-junctions-j3-before-x11-junction-adlerkreisel-drone.jpg) |
| 15:04:32 | [150432-junctions-j3-before-x11-junction-kaltenbronner-rider.jpg](150432-junctions-j3-before-x11-junction-kaltenbronner-rider.jpg) |
| 15:05:19 | [150519-junctions-j3-before-x11-junction-kaltenbronner-drone.jpg](150519-junctions-j3-before-x11-junction-kaltenbronner-drone.jpg) |
| 15:05:48 | [150548-junctions-j3-before-x11-junction-medianias-rider.jpg](150548-junctions-j3-before-x11-junction-medianias-rider.jpg) |
| 15:06:14 | [150614-junctions-j3-before-x11-junction-medianias-drone.jpg](150614-junctions-j3-before-x11-junction-medianias-drone.jpg) |
| 15:06:49 | [150649-junctions-j3-before-x11-junction-bf-narrow-rider.jpg](150649-junctions-j3-before-x11-junction-bf-narrow-rider.jpg) |
| 15:07:18 | [150718-junctions-j3-before-x11-junction-bf-narrow-drone.jpg](150718-junctions-j3-before-x11-junction-bf-narrow-drone.jpg) |
| 15:07:36 | [150736-junctions-j3-before-x11-junction-fork-rider.jpg](150736-junctions-j3-before-x11-junction-fork-rider.jpg) |
| 15:07:58 | [150758-junctions-j3-before-x11-junction-fork-drone.jpg](150758-junctions-j3-before-x11-junction-fork-drone.jpg) |
| 15:08:16 | [150816-junctions-j3-before-x11-junction-dual-rider.jpg](150816-junctions-j3-before-x11-junction-dual-rider.jpg) |
| 15:08:40 | [150840-junctions-j3-before-x11-junction-dual-drone.jpg](150840-junctions-j3-before-x11-junction-dual-drone.jpg) |
| 15:09:05 | [150905-junctions-j3-before-x11-junction-mini-rider.jpg](150905-junctions-j3-before-x11-junction-mini-rider.jpg) |
| 15:09:32 | [150932-junctions-j3-before-x11-junction-mini-drone.jpg](150932-junctions-j3-before-x11-junction-mini-drone.jpg) |
| 15:09:55 | [150955-junctions-j3-after-x11-junction-bergstrasse-rider.jpg](150955-junctions-j3-after-x11-junction-bergstrasse-rider.jpg) |
| 15:10:32 | [151032-junctions-j3-after-x11-junction-bergstrasse-drone.jpg](151032-junctions-j3-after-x11-junction-bergstrasse-drone.jpg) |
| 15:11:02 | [151102-junctions-j3-after-x11-junction-adlerkreisel-rider.jpg](151102-junctions-j3-after-x11-junction-adlerkreisel-rider.jpg) |
| 15:11:20 | [151120-junctions-j3-after-x11-junction-adlerkreisel-drone.jpg](151120-junctions-j3-after-x11-junction-adlerkreisel-drone.jpg) |
| 15:11:46 | [151146-junctions-j3-after-x11-junction-kaltenbronner-rider.jpg](151146-junctions-j3-after-x11-junction-kaltenbronner-rider.jpg) |
| 15:12:14 | [151214-junctions-j3-after-x11-junction-kaltenbronner-drone.jpg](151214-junctions-j3-after-x11-junction-kaltenbronner-drone.jpg) |
| 15:12:38 | [151238-junctions-j3-after-x11-junction-medianias-rider.jpg](151238-junctions-j3-after-x11-junction-medianias-rider.jpg) |
| 15:13:00 | [151300-junctions-j3-after-x11-junction-medianias-drone.jpg](151300-junctions-j3-after-x11-junction-medianias-drone.jpg) |
| 15:15:57 | [151557-junctions-j3-after-x11-junction-bf-narrow-rider.jpg](151557-junctions-j3-after-x11-junction-bf-narrow-rider.jpg) |
| 15:16:34 | [151634-junctions-j3-after-x11-junction-bf-narrow-drone.jpg](151634-junctions-j3-after-x11-junction-bf-narrow-drone.jpg) |
| 15:19:07 | [151907-junctions-j3-after-x11-junction-fork-rider.jpg](151907-junctions-j3-after-x11-junction-fork-rider.jpg) |
| 15:21:06 | [152106-junctions-j3-after-x11-junction-fork-drone.jpg](152106-junctions-j3-after-x11-junction-fork-drone.jpg) |
| 15:21:22 | [152122-junctions-j3-after-x11-junction-dual-rider.jpg](152122-junctions-j3-after-x11-junction-dual-rider.jpg) |
| 15:21:38 | [152138-junctions-j3-after-x11-junction-dual-drone.jpg](152138-junctions-j3-after-x11-junction-dual-drone.jpg) |
| 15:21:55 | [152155-junctions-j3-after-x11-junction-mini-rider.jpg](152155-junctions-j3-after-x11-junction-mini-rider.jpg) |
| 15:22:14 | [152214-junctions-j3-after-x11-junction-mini-drone.jpg](152214-junctions-j3-after-x11-junction-mini-drone.jpg) |
| 15:50:01 | [155001-shot-ocw.jpg](155001-shot-ocw.jpg) |
| 15:50:10 | [155010-shot-wayland-ocw-wayland.jpg](155010-shot-wayland-ocw-wayland.jpg) |
| 16:09:21 | [160921-web-ios-baseline-hills-1min.png](160921-web-ios-baseline-hills-1min.png) |
| 16:09:21 | [160921-web-ios-baseline-hills-2min.png](160921-web-ios-baseline-hills-2min.png) |
| 16:09:21 | [160921-web-ios-baseline-hills-start.png](160921-web-ios-baseline-hills-start.png) |
| 16:09:21 | [160921-web-ios-baseline-liechtenstein-1min.png](160921-web-ios-baseline-liechtenstein-1min.png) |
| 16:09:21 | [160921-web-ios-baseline-liechtenstein-2min.png](160921-web-ios-baseline-liechtenstein-2min.png) |
| 16:09:21 | [160921-web-ios-baseline-liechtenstein-3min.png](160921-web-ios-baseline-liechtenstein-3min.png) |
| 16:09:21 | [160921-web-ios-baseline-liechtenstein-4min.png](160921-web-ios-baseline-liechtenstein-4min.png) |
| 16:09:21 | [160921-web-ios-baseline-liechtenstein-end.png](160921-web-ios-baseline-liechtenstein-end.png) |
| 16:09:21 | [160921-web-ios-baseline-liechtenstein-start.png](160921-web-ios-baseline-liechtenstein-start.png) |
| 16:13:33 | [161333-web-ios-baseline-black-forest-north-landscape-1min.png](161333-web-ios-baseline-black-forest-north-landscape-1min.png) |
| 16:13:33 | [161333-web-ios-baseline-black-forest-north-landscape-2min.png](161333-web-ios-baseline-black-forest-north-landscape-2min.png) |
| 16:13:33 | [161333-web-ios-baseline-black-forest-north-landscape-3min.png](161333-web-ios-baseline-black-forest-north-landscape-3min.png) |
| 16:13:33 | [161333-web-ios-baseline-black-forest-north-landscape-4min.png](161333-web-ios-baseline-black-forest-north-landscape-4min.png) |
| 16:13:33 | [161333-web-ios-baseline-black-forest-north-landscape-end.png](161333-web-ios-baseline-black-forest-north-landscape-end.png) |
| 16:13:33 | [161333-web-ios-baseline-black-forest-north-landscape-start.png](161333-web-ios-baseline-black-forest-north-landscape-start.png) |
| 16:13:33 | [161333-web-ios-baseline-tenerife-1min.png](161333-web-ios-baseline-tenerife-1min.png) |
| 16:13:33 | [161333-web-ios-baseline-tenerife-2min.png](161333-web-ios-baseline-tenerife-2min.png) |
| 16:13:33 | [161333-web-ios-baseline-tenerife-3min.png](161333-web-ios-baseline-tenerife-3min.png) |
| 16:13:33 | [161333-web-ios-baseline-tenerife-4min.png](161333-web-ios-baseline-tenerife-4min.png) |
| 16:13:33 | [161333-web-ios-baseline-tenerife-end.png](161333-web-ios-baseline-tenerife-end.png) |
| 16:13:33 | [161333-web-ios-baseline-tenerife-start.png](161333-web-ios-baseline-tenerife-start.png) |
| 16:24:20 | [162420-web-ios-live-live-hills-1min.png](162420-web-ios-live-live-hills-1min.png) |
| 16:24:20 | [162420-web-ios-live-live-hills-2min.png](162420-web-ios-live-live-hills-2min.png) |
| 16:24:20 | [162420-web-ios-live-live-hills-end.png](162420-web-ios-live-live-hills-end.png) |
| 16:24:20 | [162420-web-ios-live-live-hills-start.png](162420-web-ios-live-live-hills-start.png) |
| 16:24:20 | [162420-web-ios-live-live-liechtenstein-1min.png](162420-web-ios-live-live-liechtenstein-1min.png) |
| 16:24:20 | [162420-web-ios-live-live-liechtenstein-2min.png](162420-web-ios-live-live-liechtenstein-2min.png) |
| 16:24:20 | [162420-web-ios-live-live-liechtenstein-3min.png](162420-web-ios-live-live-liechtenstein-3min.png) |
| 16:24:20 | [162420-web-ios-live-live-liechtenstein-end.png](162420-web-ios-live-live-liechtenstein-end.png) |
| 16:24:20 | [162420-web-ios-live-live-liechtenstein-start.png](162420-web-ios-live-live-liechtenstein-start.png) |
| 16:27:45 | [162745-web-ios-live-live-tenerife-1min.png](162745-web-ios-live-live-tenerife-1min.png) |
| 16:27:45 | [162745-web-ios-live-live-tenerife-2min.png](162745-web-ios-live-live-tenerife-2min.png) |
| 16:27:45 | [162745-web-ios-live-live-tenerife-3min.png](162745-web-ios-live-live-tenerife-3min.png) |
| 16:27:45 | [162745-web-ios-live-live-tenerife-end.png](162745-web-ios-live-live-tenerife-end.png) |
| 16:27:45 | [162745-web-ios-live-live-tenerife-start.png](162745-web-ios-live-live-tenerife-start.png) |
| 16:40:45 | [164045-lamp-rule-vaduz-street-day-before-wayland.jpg](164045-lamp-rule-vaduz-street-day-before-wayland.jpg) |
| 16:44:30 | [164430-web-ios-after-hills-1min.png](164430-web-ios-after-hills-1min.png) |
| 16:44:30 | [164430-web-ios-after-hills-2min.png](164430-web-ios-after-hills-2min.png) |
| 16:44:30 | [164430-web-ios-after-hills-3min.png](164430-web-ios-after-hills-3min.png) |
| 16:44:30 | [164430-web-ios-after-hills-4min.png](164430-web-ios-after-hills-4min.png) |
| 16:44:30 | [164430-web-ios-after-hills-5min.png](164430-web-ios-after-hills-5min.png) |
| 16:44:30 | [164430-web-ios-after-hills-context-lost-again.png](164430-web-ios-after-hills-context-lost-again.png) |
| 16:44:30 | [164430-web-ios-after-hills-context-reloaded.png](164430-web-ios-after-hills-context-reloaded.png) |
| 16:44:30 | [164430-web-ios-after-hills-end.png](164430-web-ios-after-hills-end.png) |
| 16:44:30 | [164430-web-ios-after-hills-start.png](164430-web-ios-after-hills-start.png) |
| 16:44:30 | [164430-web-ios-after-liechtenstein-landscape-1min.png](164430-web-ios-after-liechtenstein-landscape-1min.png) |
| 16:44:30 | [164430-web-ios-after-liechtenstein-landscape-2min.png](164430-web-ios-after-liechtenstein-landscape-2min.png) |
| 16:44:30 | [164430-web-ios-after-liechtenstein-landscape-3min.png](164430-web-ios-after-liechtenstein-landscape-3min.png) |
| 16:44:30 | [164430-web-ios-after-liechtenstein-landscape-4min.png](164430-web-ios-after-liechtenstein-landscape-4min.png) |
| 16:44:30 | [164430-web-ios-after-liechtenstein-landscape-died-once.png](164430-web-ios-after-liechtenstein-landscape-died-once.png) |
| 16:44:30 | [164430-web-ios-after-liechtenstein-landscape-died-twice.png](164430-web-ios-after-liechtenstein-landscape-died-twice.png) |
| 16:44:30 | [164430-web-ios-after-liechtenstein-landscape-end.png](164430-web-ios-after-liechtenstein-landscape-end.png) |
| 16:44:30 | [164430-web-ios-after-liechtenstein-landscape-start.png](164430-web-ios-after-liechtenstein-landscape-start.png) |
| 16:48:17 | [164817-motion-after-loop-bunch.jpg](164817-motion-after-loop-bunch.jpg) |
| 16:48:18 | [164818-motion-before-loop-bunch.jpg](164818-motion-before-loop-bunch.jpg) |
| 16:48:18 | [164818-motion-before-loop-bunch.mp4](164818-motion-before-loop-bunch.mp4) |
| 16:48:19 | [164819-motion-after-loop-bunch.mp4](164819-motion-after-loop-bunch.mp4) |
| 16:49:28 | [164928-motion-before-after-frames-100-109.jpg](164928-motion-before-after-frames-100-109.jpg) |
| 16:50:34 | [165034-web-ios-after-black-forest-north-landscape-1min.png](165034-web-ios-after-black-forest-north-landscape-1min.png) |
| 16:50:34 | [165034-web-ios-after-black-forest-north-landscape-2min.png](165034-web-ios-after-black-forest-north-landscape-2min.png) |
| 16:50:34 | [165034-web-ios-after-black-forest-north-landscape-3min.png](165034-web-ios-after-black-forest-north-landscape-3min.png) |
| 16:50:34 | [165034-web-ios-after-black-forest-north-landscape-4min.png](165034-web-ios-after-black-forest-north-landscape-4min.png) |
| 16:50:34 | [165034-web-ios-after-black-forest-north-landscape-5min.png](165034-web-ios-after-black-forest-north-landscape-5min.png) |
| 16:50:34 | [165034-web-ios-after-black-forest-north-landscape-context-lost-again.png](165034-web-ios-after-black-forest-north-landscape-context-lost-again.png) |
| 16:50:34 | [165034-web-ios-after-black-forest-north-landscape-context-reloaded.png](165034-web-ios-after-black-forest-north-landscape-context-reloaded.png) |
| 16:50:34 | [165034-web-ios-after-black-forest-north-landscape-end.png](165034-web-ios-after-black-forest-north-landscape-end.png) |
| 16:50:34 | [165034-web-ios-after-black-forest-north-landscape-start.png](165034-web-ios-after-black-forest-north-landscape-start.png) |
| 16:50:34 | [165034-web-ios-after-tenerife-1min.png](165034-web-ios-after-tenerife-1min.png) |
| 16:50:34 | [165034-web-ios-after-tenerife-2min.png](165034-web-ios-after-tenerife-2min.png) |
| 16:50:34 | [165034-web-ios-after-tenerife-3min.png](165034-web-ios-after-tenerife-3min.png) |
| 16:50:34 | [165034-web-ios-after-tenerife-4min.png](165034-web-ios-after-tenerife-4min.png) |
| 16:50:34 | [165034-web-ios-after-tenerife-end.png](165034-web-ios-after-tenerife-end.png) |
| 16:50:34 | [165034-web-ios-after-tenerife-start.png](165034-web-ios-after-tenerife-start.png) |
| 16:50:59 | [165059-lamp-rule-vaduz-street-day-after-wayland.jpg](165059-lamp-rule-vaduz-street-day-after-wayland.jpg) |
| 16:51:13 | [165113-lamp-rule-vaduz-street-night-before-wayland.jpg](165113-lamp-rule-vaduz-street-night-before-wayland.jpg) |
| 16:51:28 | [165128-lamp-rule-vaduz-street-night-after-wayland.jpg](165128-lamp-rule-vaduz-street-night-after-wayland.jpg) |
| 16:51:42 | [165142-lamp-rule-liechtenstein-junction-day-before-wayland.jpg](165142-lamp-rule-liechtenstein-junction-day-before-wayland.jpg) |
| 16:51:57 | [165157-lamp-rule-liechtenstein-junction-day-after-wayland.jpg](165157-lamp-rule-liechtenstein-junction-day-after-wayland.jpg) |
| 16:52:11 | [165211-lamp-rule-liechtenstein-junction-night-before-wayland.jpg](165211-lamp-rule-liechtenstein-junction-night-before-wayland.jpg) |
| 16:52:26 | [165226-lamp-rule-liechtenstein-junction-night-after-wayland.jpg](165226-lamp-rule-liechtenstein-junction-night-after-wayland.jpg) |
| 16:52:50 | [165250-lamp-rule-blackforest-village-day-before-wayland.jpg](165250-lamp-rule-blackforest-village-day-before-wayland.jpg) |
| 16:53:14 | [165314-lamp-rule-blackforest-village-day-after-wayland.jpg](165314-lamp-rule-blackforest-village-day-after-wayland.jpg) |
| 16:53:38 | [165338-lamp-rule-blackforest-village-night-before-wayland.jpg](165338-lamp-rule-blackforest-village-night-before-wayland.jpg) |
| 16:54:02 | [165402-lamp-rule-blackforest-village-night-after-wayland.jpg](165402-lamp-rule-blackforest-village-night-after-wayland.jpg) |
| 16:54:26 | [165426-lamp-rule-tenerife-town-day-before-wayland.jpg](165426-lamp-rule-tenerife-town-day-before-wayland.jpg) |
| 16:54:50 | [165450-lamp-rule-tenerife-town-day-after-wayland.jpg](165450-lamp-rule-tenerife-town-day-after-wayland.jpg) |
| 16:55:13 | [165513-lamp-rule-tenerife-town-night-before-wayland.jpg](165513-lamp-rule-tenerife-town-night-before-wayland.jpg) |
| 16:55:38 | [165538-lamp-rule-tenerife-town-night-after-wayland.jpg](165538-lamp-rule-tenerife-town-night-after-wayland.jpg) |
| 16:56:01 | [165601-lamp-rule-tenerife-junction-day-before-wayland.jpg](165601-lamp-rule-tenerife-junction-day-before-wayland.jpg) |
| 16:56:23 | [165623-lamp-rule-tenerife-junction-day-after-wayland.jpg](165623-lamp-rule-tenerife-junction-day-after-wayland.jpg) |
| 16:56:44 | [165644-lamp-rule-tenerife-junction-night-before-wayland.jpg](165644-lamp-rule-tenerife-junction-night-before-wayland.jpg) |
| 16:57:07 | [165707-lamp-rule-tenerife-junction-night-after-wayland.jpg](165707-lamp-rule-tenerife-junction-night-after-wayland.jpg) |
| 17:10:42 | [171042-shot-ocw.jpg](171042-shot-ocw.jpg) |
| 17:10:52 | [171052-shot-wayland-ocw-wayland.jpg](171052-shot-wayland-ocw-wayland.jpg) |
| 17:18:57 | [171857-web-web-gpu-forced-webgpu.jpg](171857-web-web-gpu-forced-webgpu.jpg) |
| 17:18:57 | [171857-web-web-gpu-iphone-safari.jpg](171857-web-web-gpu-iphone-safari.jpg) |
| 17:18:57 | [171857-web-web-gpu-uncaptured-webgl2.jpg](171857-web-web-gpu-uncaptured-webgl2.jpg) |
| 17:18:57 | [171857-web-web-gpu-webgpu.jpg](171857-web-web-gpu-webgpu.jpg) |
| 17:28:14 | [172814-web-web-calendar-select.jpg](172814-web-web-calendar-select.jpg) |
| 17:28:14 | [172814-web-web-calendar.jpg](172814-web-web-calendar.jpg) |
| 17:28:14 | [172814-web-web-console.jpg](172814-web-web-console.jpg) |
| 17:28:14 | [172814-web-web-damage-crash.jpg](172814-web-web-damage-crash.jpg) |
| 17:28:14 | [172814-web-web-damage-fresh.jpg](172814-web-web-damage-fresh.jpg) |
| 17:28:14 | [172814-web-web-devices-collapsed.jpg](172814-web-web-devices-collapsed.jpg) |
| 17:28:14 | [172814-web-web-devices-expanded.jpg](172814-web-web-devices-expanded.jpg) |
| 17:28:14 | [172814-web-web-gamepad.jpg](172814-web-web-gamepad.jpg) |
| 17:28:14 | [172814-web-web-gps.jpg](172814-web-web-gps.jpg) |
| 17:28:14 | [172814-web-web-history-delete.jpg](172814-web-web-history-delete.jpg) |
| 17:28:14 | [172814-web-web-history-ride-file.jpg](172814-web-web-history-ride-file.jpg) |
| 17:28:14 | [172814-web-web-history-ride-map.jpg](172814-web-web-history-ride-map.jpg) |
| 17:28:14 | [172814-web-web-hud.jpg](172814-web-web-hud.jpg) |
| 17:28:14 | [172814-web-web-input-mapping-capture.jpg](172814-web-web-input-mapping-capture.jpg) |
| 17:28:14 | [172814-web-web-input-mapping-junctions.jpg](172814-web-web-input-mapping-junctions.jpg) |
| 17:28:14 | [172814-web-web-input-mapping-swapped.jpg](172814-web-web-input-mapping-swapped.jpg) |
| 17:28:14 | [172814-web-web-input-mapping.jpg](172814-web-web-input-mapping.jpg) |
| 17:28:14 | [172814-web-web-join.jpg](172814-web-web-join.jpg) |
| 17:28:14 | [172814-web-web-menu.jpg](172814-web-web-menu.jpg) |
| 17:28:14 | [172814-web-web-photo-preview.jpg](172814-web-web-photo-preview.jpg) |
| 17:28:14 | [172814-web-web-ride.jpg](172814-web-web-ride.jpg) |
| 17:28:14 | [172814-web-web-riders.jpg](172814-web-web-riders.jpg) |
| 17:28:14 | [172814-web-web-settings.jpg](172814-web-web-settings.jpg) |
| 17:28:14 | [172814-web-web-strava-recording-downloaded.jpg](172814-web-web-strava-recording-downloaded.jpg) |
| 17:28:14 | [172814-web-web-strava-recording-saved-to-folder.jpg](172814-web-web-strava-recording-saved-to-folder.jpg) |
| 17:28:14 | [172814-web-web-strava-recording.jpg](172814-web-web-strava-recording.jpg) |
| 17:28:14 | [172814-web-web-strava-row.jpg](172814-web-web-strava-row.jpg) |
| 17:28:14 | [172814-web-web-strava-steps.jpg](172814-web-web-strava-steps.jpg) |
| 17:28:14 | [172814-web-web-touch-hints.jpg](172814-web-web-touch-hints.jpg) |
| 17:28:14 | [172814-web-web-touch-hold.jpg](172814-web-web-touch-hold.jpg) |
| 17:28:14 | [172814-web-web-unicorn-flight.jpg](172814-web-web-unicorn-flight.jpg) |
| 17:28:14 | [172814-web-web-unicorn-inspect.jpg](172814-web-web-unicorn-inspect.jpg) |
| 17:28:14 | [172814-web-web-unicorn-menu.jpg](172814-web-web-unicorn-menu.jpg) |
| 17:28:14 | [172814-web-web-weather.jpg](172814-web-web-weather.jpg) |
| 17:28:14 | [172814-web-web-workout-map.jpg](172814-web-web-workout-map.jpg) |
| 17:28:14 | [172814-web-web.jpg](172814-web-web.jpg) |
| 17:36:39 | [173639-web-web-webkit-iphone-hints.png](173639-web-web-webkit-iphone-hints.png) |
| 17:36:39 | [173639-web-web-webkit-iphone-hold.png](173639-web-web-webkit-iphone-hold.png) |
| 17:36:39 | [173639-web-web-webkit-iphone-landscape-hints.png](173639-web-web-webkit-iphone-landscape-hints.png) |
| 17:36:39 | [173639-web-web-webkit-iphone-landscape-hold.png](173639-web-web-webkit-iphone-landscape-hold.png) |
| 17:36:39 | [173639-web-web-webkit-iphone-landscape-riding.png](173639-web-web-webkit-iphone-landscape-riding.png) |
| 17:36:39 | [173639-web-web-webkit-iphone-landscape-stopped.png](173639-web-web-webkit-iphone-landscape-stopped.png) |
| 17:36:39 | [173639-web-web-webkit-iphone-landscape.png](173639-web-web-webkit-iphone-landscape.png) |
| 17:36:39 | [173639-web-web-webkit-iphone-riding.png](173639-web-web-webkit-iphone-riding.png) |
| 17:36:39 | [173639-web-web-webkit-iphone-start.png](173639-web-web-webkit-iphone-start.png) |
| 17:36:39 | [173639-web-web-webkit-iphone-stopped.png](173639-web-web-webkit-iphone-stopped.png) |
| 17:36:39 | [173639-web-web-webkit-iphone.png](173639-web-web-webkit-iphone.png) |
| 17:36:39 | [173639-web-web-webkit-mac.png](173639-web-web-webkit-mac.png) |
| 17:42:38 | [174238-shot-ocw.jpg](174238-shot-ocw.jpg) |
| 17:42:48 | [174248-shot-wayland-ocw-wayland.jpg](174248-shot-wayland-ocw-wayland.jpg) |
| 17:44:52 | [174452-web-web-gpu-device-webgl2.jpg](174452-web-web-gpu-device-webgl2.jpg) |
| 17:44:52 | [174452-web-web-gpu-forced-webgpu.jpg](174452-web-web-gpu-forced-webgpu.jpg) |
| 17:44:52 | [174452-web-web-gpu-iphone-safari.jpg](174452-web-web-gpu-iphone-safari.jpg) |
| 17:44:52 | [174452-web-web-gpu-noframe-webgl2.jpg](174452-web-web-gpu-noframe-webgl2.jpg) |
| 17:44:52 | [174452-web-web-gpu-uncaptured-webgl2.jpg](174452-web-web-gpu-uncaptured-webgl2.jpg) |
| 17:44:52 | [174452-web-web-gpu-webgpu.jpg](174452-web-web-gpu-webgpu.jpg) |
| 17:46:24 | [174624-web-ios-final-hills-1min.png](174624-web-ios-final-hills-1min.png) |
| 17:46:24 | [174624-web-ios-final-hills-2min.png](174624-web-ios-final-hills-2min.png) |
| 17:46:24 | [174624-web-ios-final-hills-3min.png](174624-web-ios-final-hills-3min.png) |
| 17:46:24 | [174624-web-ios-final-hills-context-lost-again.png](174624-web-ios-final-hills-context-lost-again.png) |
| 17:46:24 | [174624-web-ios-final-hills-context-reloaded.png](174624-web-ios-final-hills-context-reloaded.png) |
| 17:46:24 | [174624-web-ios-final-hills-end.png](174624-web-ios-final-hills-end.png) |
| 17:46:24 | [174624-web-ios-final-hills-start.png](174624-web-ios-final-hills-start.png) |
| 17:50:18 | [175018-web-ios-final-liechtenstein-1min.png](175018-web-ios-final-liechtenstein-1min.png) |
| 17:50:18 | [175018-web-ios-final-liechtenstein-2min.png](175018-web-ios-final-liechtenstein-2min.png) |
| 17:50:18 | [175018-web-ios-final-liechtenstein-died-once.png](175018-web-ios-final-liechtenstein-died-once.png) |
| 17:50:18 | [175018-web-ios-final-liechtenstein-died-twice.png](175018-web-ios-final-liechtenstein-died-twice.png) |
| 17:50:18 | [175018-web-ios-final-liechtenstein-end.png](175018-web-ios-final-liechtenstein-end.png) |
| 17:50:18 | [175018-web-ios-final-liechtenstein-start.png](175018-web-ios-final-liechtenstein-start.png) |
| 17:55:58 | [175558-web-web-calendar-select.jpg](175558-web-web-calendar-select.jpg) |
| 17:55:58 | [175558-web-web-calendar.jpg](175558-web-web-calendar.jpg) |
| 17:55:58 | [175558-web-web-console.jpg](175558-web-web-console.jpg) |
| 17:55:58 | [175558-web-web-damage-crash.jpg](175558-web-web-damage-crash.jpg) |
| 17:55:58 | [175558-web-web-damage-fresh.jpg](175558-web-web-damage-fresh.jpg) |
| 17:55:58 | [175558-web-web-devices-collapsed.jpg](175558-web-web-devices-collapsed.jpg) |
| 17:55:58 | [175558-web-web-devices-expanded.jpg](175558-web-web-devices-expanded.jpg) |
| 17:55:58 | [175558-web-web-downloads-OCW-2026-11-22-17-57-32.jpg](175558-web-web-downloads-OCW-2026-11-22-17-57-32.jpg) |
| 17:55:58 | [175558-web-web-downloads-ocw-2026-11-22-17-58-02.webm](175558-web-web-downloads-ocw-2026-11-22-17-58-02.webm) |
| 17:55:58 | [175558-web-web-gamepad.jpg](175558-web-web-gamepad.jpg) |
| 17:55:58 | [175558-web-web-gps.jpg](175558-web-web-gps.jpg) |
| 17:55:58 | [175558-web-web-history-delete.jpg](175558-web-web-history-delete.jpg) |
| 17:55:58 | [175558-web-web-history-ride-file.jpg](175558-web-web-history-ride-file.jpg) |
| 17:55:58 | [175558-web-web-history-ride-map.jpg](175558-web-web-history-ride-map.jpg) |
| 17:55:58 | [175558-web-web-hud.jpg](175558-web-web-hud.jpg) |
| 17:55:58 | [175558-web-web-input-mapping-capture.jpg](175558-web-web-input-mapping-capture.jpg) |
| 17:55:58 | [175558-web-web-input-mapping-junctions.jpg](175558-web-web-input-mapping-junctions.jpg) |
| 17:55:58 | [175558-web-web-input-mapping-swapped.jpg](175558-web-web-input-mapping-swapped.jpg) |
| 17:55:58 | [175558-web-web-input-mapping.jpg](175558-web-web-input-mapping.jpg) |
| 17:55:58 | [175558-web-web-join.jpg](175558-web-web-join.jpg) |
| 17:55:58 | [175558-web-web-menu.jpg](175558-web-web-menu.jpg) |
| 17:55:58 | [175558-web-web-photo-preview.jpg](175558-web-web-photo-preview.jpg) |
| 17:55:58 | [175558-web-web-ride.jpg](175558-web-web-ride.jpg) |
| 17:55:58 | [175558-web-web-riders.jpg](175558-web-web-riders.jpg) |
| 17:55:58 | [175558-web-web-settings.jpg](175558-web-web-settings.jpg) |
| 17:55:58 | [175558-web-web-strava-recording-downloaded.jpg](175558-web-web-strava-recording-downloaded.jpg) |
| 17:55:58 | [175558-web-web-strava-recording-saved-to-folder.jpg](175558-web-web-strava-recording-saved-to-folder.jpg) |
| 17:55:58 | [175558-web-web-strava-recording.jpg](175558-web-web-strava-recording.jpg) |
| 17:55:58 | [175558-web-web-strava-row.jpg](175558-web-web-strava-row.jpg) |
| 17:55:58 | [175558-web-web-strava-steps.jpg](175558-web-web-strava-steps.jpg) |
| 17:55:58 | [175558-web-web-touch-hints.jpg](175558-web-web-touch-hints.jpg) |
| 17:55:58 | [175558-web-web-touch-hold.jpg](175558-web-web-touch-hold.jpg) |
| 17:55:58 | [175558-web-web-unicorn-flight.jpg](175558-web-web-unicorn-flight.jpg) |
| 17:55:58 | [175558-web-web-unicorn-inspect.jpg](175558-web-web-unicorn-inspect.jpg) |
| 17:55:58 | [175558-web-web-unicorn-menu.jpg](175558-web-web-unicorn-menu.jpg) |
| 17:55:58 | [175558-web-web-weather.jpg](175558-web-web-weather.jpg) |
| 17:55:58 | [175558-web-web-workout-map.jpg](175558-web-web-workout-map.jpg) |
| 17:55:58 | [175558-web-web.jpg](175558-web-web.jpg) |
| 20:15:01 | [201501-windows-icon-0.2.5-ocw-desktop-128.png](201501-windows-icon-0.2.5-ocw-desktop-128.png) |
| 20:15:01 | [201501-windows-icon-0.2.5-ocw-desktop-16.png](201501-windows-icon-0.2.5-ocw-desktop-16.png) |
| 20:15:01 | [201501-windows-icon-0.2.5-ocw-desktop-24.png](201501-windows-icon-0.2.5-ocw-desktop-24.png) |
| 20:15:01 | [201501-windows-icon-0.2.5-ocw-desktop-32.png](201501-windows-icon-0.2.5-ocw-desktop-32.png) |
| 20:15:01 | [201501-windows-icon-0.2.5-ocw-desktop-48.png](201501-windows-icon-0.2.5-ocw-desktop-48.png) |
| 20:15:01 | [201501-windows-icon-0.2.5-ocw-desktop-64.png](201501-windows-icon-0.2.5-ocw-desktop-64.png) |
| 20:15:02 | [201502-windows-icon-0.2.5-ocw-desktop-256.png](201502-windows-icon-0.2.5-ocw-desktop-256.png) |
| 20:15:03 | [201503-windows-icon-0.2.5-ocw-studio-128.png](201503-windows-icon-0.2.5-ocw-studio-128.png) |
| 20:15:03 | [201503-windows-icon-0.2.5-ocw-studio-16.png](201503-windows-icon-0.2.5-ocw-studio-16.png) |
| 20:15:03 | [201503-windows-icon-0.2.5-ocw-studio-24.png](201503-windows-icon-0.2.5-ocw-studio-24.png) |
| 20:15:03 | [201503-windows-icon-0.2.5-ocw-studio-256.png](201503-windows-icon-0.2.5-ocw-studio-256.png) |
| 20:15:03 | [201503-windows-icon-0.2.5-ocw-studio-32.png](201503-windows-icon-0.2.5-ocw-studio-32.png) |
| 20:15:03 | [201503-windows-icon-0.2.5-ocw-studio-48.png](201503-windows-icon-0.2.5-ocw-studio-48.png) |
| 20:15:03 | [201503-windows-icon-0.2.5-ocw-studio-64.png](201503-windows-icon-0.2.5-ocw-studio-64.png) |
| 20:15:20 | [201520-release-0.2.5-appimage-x11.jpg](201520-release-0.2.5-appimage-x11.jpg) |
| 20:15:47 | [201547-release-0.2.5-appimage-wayland.jpg](201547-release-0.2.5-appimage-wayland.jpg) |
| 20:16:10 | [201610-release-0.2.5-tarball-x11.jpg](201610-release-0.2.5-tarball-x11.jpg) |
| 20:16:36 | [201636-release-0.2.5-tarball-wayland.jpg](201636-release-0.2.5-tarball-wayland.jpg) |
| 20:16:52 | [201652-release-0.2.5-studio-wayland.jpg](201652-release-0.2.5-studio-wayland.jpg) |
| 20:17:09 | [201709-release-0.2.5-studio-x11.jpg](201709-release-0.2.5-studio-x11.jpg) |
| 20:17:22 | [201722-release-0.2.5-web-webgpu-web-world-cached-loading.jpg](201722-release-0.2.5-web-webgpu-web-world-cached-loading.jpg) |
| 20:17:22 | [201722-release-0.2.5-web-webgpu-web-world-cached.jpg](201722-release-0.2.5-web-webgpu-web-world-cached.jpg) |
| 20:17:22 | [201722-release-0.2.5-web-webgpu-web-world-first-loading.jpg](201722-release-0.2.5-web-webgpu-web-world-first-loading.jpg) |
| 20:17:22 | [201722-release-0.2.5-web-webgpu-web-world.jpg](201722-release-0.2.5-web-webgpu-web-world.jpg) |
| 20:17:50 | [201750-release-0.2.5-web-webgl2-web-world-webgl2-cached-loading.jpg](201750-release-0.2.5-web-webgl2-web-world-webgl2-cached-loading.jpg) |
| 20:17:50 | [201750-release-0.2.5-web-webgl2-web-world-webgl2-cached.jpg](201750-release-0.2.5-web-webgl2-web-world-webgl2-cached.jpg) |
| 20:17:50 | [201750-release-0.2.5-web-webgl2-web-world-webgl2-first-loading.jpg](201750-release-0.2.5-web-webgl2-web-world-webgl2-first-loading.jpg) |
| 20:17:50 | [201750-release-0.2.5-web-webgl2-web-world-webgl2.jpg](201750-release-0.2.5-web-webgl2-web-world-webgl2.jpg) |
