# OCW build diary – day 11, 2026-11-21

15 commits (5 merges), +5381 / −801 lines, 180 images, 3 videos, 0 sounds.

## Commits

| Time | Commit | |
|---|---|---|
| 09:06 | `23d0e6b` | Side roads keep their class gradient after the junction blend where they can: grade and vertical-curvature limits applied again with the junction surfaces fixed, steep intervals linted by cause (spec 4.8.8 J2b, 4.8.1, 4.8.3, 5.18) |
| 09:07 | `cee8e94` (merge) | Merge origin/main into the J2b branch (spec 5.18 on top of 5.17) |
| 09:08 | `8657770` | Hosting and voice answers: NAT-PMP / PCP only when riders report routers without UPnP, a Voice switch in Host a ride, mute status per viewer as one yes / no, one shared list of selected riders (spec 7.1.7 Q13, Q15, Q17, Q19; 5.18) |
| 09:44 | `e1884b9` | A Voice switch in Host a ride and the headphones worked out per viewer by the server: the lists of whom a rider muted never leave the server (spec 7.1.7 Q15, Q17; 5.19) |
| 09:45 | `9e58cdd` (merge) | Merge side roads keeping their class gradient after the junction blend (J2b), the gradient lint by cause (spec 4.8.8, 5.19; new open question 4.8.8 Q6; rebuilt packages not installed) |
| 09:53 | `b9eeb5a` | Delete / Page Down choose the junction's exit, ← / → only steer, Page Up / Down no longer change the power; Input mapping page with capture and swap, saved in ocw.toml (spec 3.2.5, 5.18) |
| 10:09 | `9ef0451` | Headphones module also for wasm; neutral Host a ride summary note; headphones scenes seen from the front (spec 7.1.7 Q15, Q17) |
| 10:39 | `33f76cf` (merge) | Merge a Voice switch in Host a ride and the headphones worked out per viewer on the server, the mute lists never sent (spec 7.1.7 Q15, Q17; 5.20) |
| 10:52 | `29e46a5` | Input mapping scenes: later shots, so slow X11 runs reach the page (spec 3.2.5) |
| 10:53 | `c42099f` (merge) | Merge Delete / Page Down for the junction's exits (←/→ only steer, Page Up/Down no longer change power) and the Input mapping page with remapping saved in ocw.toml (spec 3.2.5, 5.21) |
| 11:53 | `774fa01` | Spatial crash sounds and the client predicting bumps with other riders (spec 14 Phase 12, 5.22) |
| 12:06 | `e03d7ae` | ocw-audio: the air-absorption check of the spatial cue test matches the law (35 m vs 5 m: about a third) |
| 12:18 | `54fed58` (merge) | Merge spatial crash sounds of other riders and the client predicting bumps with other riders (spec Phase 12, 5.22) |
| 13:54 | `4ae9436` | Browser memory per resident tile: Tenerife 2.1 GB -> 0.7 GB, Black Forest north 2.0 GB -> 0.9 GB of wasm memory, picture unchanged (spec Phase 10 B2, 5.23) |
| 14:10 | `554982a` | Heap counter test: no race between the live bytes and their peak (spec Phase 10 B2) |

## Builds and build servers

64 build/test runs on the build machines, 9.6 h in total, 0 failed; 1440 server samples; cargo compiled 878 crates in 1.2 h, 0.5 h waiting for build slots.

| Machine | Runs | Hours | Cargo h | Crates | Waited h | Failed | Online |
|---|---|---|---|---|---|---|---|
| Weela | 0 | 0.0 | 0.0 | 0 | 0.0 | 0 | 0% |
| Win11Builder | 4 | 2.6 | 0.3 | 22 | 0.4 | 0 | 100% |
| leela | 9 | 0.5 | 0.1 | 15 | 0.0 | 0 | 100% |
| macos | 0 | 0.0 | 0.0 | 0 | 0.0 | 0 | 100% |
| marge | 51 | 6.6 | 0.8 | 841 | 0.1 | 0 | 100% |

Longest runs:

- 53 min on Win11Builder: `cargo clippy -p ocw-desktop --all-targets -- -D warnings 2>&1 | Select-Object -L`
- 38 min on Win11Builder: `cargo clippy -q --workspace --all-targets -- -D warnings 2>&1 | Select-String -P`
- 37 min on marge: `for t in check test-web-build test-smoke test-web test-web-webkit; do make $t > `
- 37 min on marge: `make check > /tmp/j2b-check.log 2>&1; echo "check $?"; tail -5 /tmp/j2b-check.lo`
- 35 min on marge: `set -e; make check; make test-smoke; make test-web; make test-web-webkit; echo A`

## Token usage

320.9 M tokens in 1,072 model messages (output 623 k, cache reads 314.6 M, cache writes 5.7 M, uncached input 2 k). Full breakdown: [tokens.json](tokens.json).

| Feature | Tokens | Output | Messages |
|---|---|---|---|
| Audio & voice | 131.4 M | 202 k | 385 |
| Planning & spec | 83.1 M | 159 k | 279 |
| Other | 62.6 M | 142 k | 242 |
| Art project | 33.9 M | 110 k | 139 |
| Build, release & infra | 9.9 M | 10 k | 26 |
| UI & menus | 0 k | 0 k | 1 |

| Task | Feature | Tokens | Output |
|---|---|---|---|
| agent: Phase 10 B2: browser tile memory | Planning & spec | 83.1 M | 159 k |
| coordination: Answers to open questeions follow here: **7.1.7 Open questions (for the user)** … | Audio & voice | 74.9 M | 34 k |
| agent: Junction exit keys and input mapping | Other | 58.9 M | 131 k |
| agent: Voice switch and per-viewer mute | Audio & voice | 36.6 M | 93 k |
| agent: Day videos 19 and 20 Nov, art README | Art project | 27.5 M | 103 k |
| agent: Phase 12: crash sounds, bump prediction | Audio & voice | 19.8 M | 76 k |
| agent: J2 follow-up: grade limits, rebuild | Build, release & infra | 9.9 M | 10 k |
| coordination: when you have tokens. create the next videos. for yesterday, where there where n… | Art project | 6.4 M | 8 k |
| agent: Privacy review of day sheets | Other | 3.7 M | 11 k |
| coordination: The cursor keys are double used, for steering and also for selecting which road … | UI & menus | 0 k | 0 k |

## Prompts

3 prompts (full text: [prompts.md](prompts.md)).

| Time | Prompt |
|---|---|
| 08:23 | The cursor keys are double used, for steering and also for selecting which road to ride. Use del key to switch leftwards through the option, |
| 09:04 | when you have tokens. create the next videos. for yesterday, where there where no tokens, create a video about the fact that there where no  |
| 09:08 | Answers to open questeions follow here: **7.1.7 Open questions (for the user)**  - **7.1.7 Q13 â€“ NAT-PMP / PCP besides UPnP:** when a ride |

## Features

6 spec versions added, 4 landed by a merge; 4 deploys, 0 releases.

| Spec | Feature | Landed | Check (marge) |
|---|---|---|---|
| 5.18 | Hosting and voice answers | 09:08 `8657770` | – |
| 5.19 | Side roads keep their class gradient after the junction blend where they can | 09:45 `9e58cdd` (merge) | ok at 09:07 (commit) |
| 5.20 | Built: a Voice switch in Host a ride and the headphones worked out per viewer by the serv… | 10:39 `33f76cf` (merge) | ok at 10:09 (commit) |
| 5.21 | Delete / Page Down choose the junction's exit to the left / right, ← / → only steer, Page… | 10:53 `c42099f` (merge) | ok at 11:52, 1 suites, 1 passed, 0 failed (commit) |
| 5.22 | Built: other riders' crashes and bumps are heard from where they happen, and the client p… | 12:18 `54fed58` (merge) | ok at 13:21, 1 suites, 1 passed, 0 failed (commit) |
| 5.23 | The browser app's memory on the big worlds cut to a third | 13:54 `4ae9436` | – |

Deploys:

- 11:30 marge: `c42099f` (ok)
- 11:31 leela: `c42099f` (ok)
- 15:14 marge: `554982a` (ok)
- 15:16 leela: `554982a` (ok)

## Agent jobs

7 jobs (coordinator log agents.jsonl).

| Task | Branch | Start | End | Status | Interrupted | Merged |
|---|---|---|---|---|---|---|
| Phone-sized HUD for the browser | ace384c5 | 09:06 | 09:06 | merged |  |  |
| Day videos 2026-11-19 and 2026-11-20 | a53e7da9 | 09:08 | 09:49 | merged |  |  |
| Junction exit keys and input mapping | aebb34f8 | 09:08 | 11:29 | merged |  |  |
| Voice switch (Q15) and per-viewer mute (Q17) | a649c026 | 09:09 | 11:29 | merged |  |  |
| J2 follow-up: grade limits, rebuild | a22862f8 | 09:45 | 09:46 | merged |  |  |
| Phase 12: crash sounds, bump prediction | a391bd88 | 11:36 | 12:19 | merged |  |  |
| Phase 10 B2: browser tile memory | a3d60721 | 13:07 | 15:14 | merged |  |  |

## Incidents

36 collected (disk-full 1, janitor-delete 18, machine-offline 2, machine-online 1, unit-failed 14), 0 with root-cause notes ([incidents.md](incidents.md)).

| Time | Kind | Machine | What |
|---|---|---|---|
| 00:00 | machine-offline | Weela | Weela unreachable (no route to host) |
| 00:00 | disk-full | Win11Builder | disk C: on Win11Builder at 92 % |
| 09:05 | janitor-delete | marge | janitor delete OCW-merge-phone/target (31.4 GB) |
| 09:05 | janitor-delete | marge | janitor delete OCW-worktree-agent-ace384c5ecb630278/target (39.6 GB) |
| 09:05 | janitor-delete | marge | janitor delete OCW-worktree-agent-ab9dfed42b5483ead/target (30.9 GB) |
| 09:05 | janitor-delete | leela | janitor delete OCW-worktree-agent-ab9dfed42b5483ead/target (13.8 GB) |
| 09:12 | janitor-delete | macos | janitor delete OCW-worktree-agent-ab9dfed42b5483ead/target (12.4 GB) |
| 09:45 | janitor-delete | marge | janitor delete OCW-worktree-agent-a22862f8e310614ff/target (30.3 GB) |
| 09:45 | janitor-delete | leela | janitor delete OCW-worktree-agent-a22862f8e310614ff/target (1.9 GB) |
| 10:05 | unit-failed | deb | ocw-art-collect.service failed (exit-code) |
| 10:28 | janitor-delete | Win11Builder | janitor delete OCW-worktree-agent-a5d32401a371b9b03/target (8.2 GB) |
| 10:28 | janitor-delete | Win11Builder | janitor delete OCW-worktree-agent-aa7255b2dbab91239/target (3.0 GB) |
| 11:03 | unit-failed | deb | ocw-art-collect.service failed (exit-code) |
| 11:28 | janitor-delete | marge | janitor delete OCW-merge-voice/target (33.9 GB) |
| 11:28 | janitor-delete | marge | janitor delete OCW-worktree-agent-a649c02685a063272/target (36.6 GB) |
| 11:28 | janitor-delete | marge | janitor delete OCW-worktree-agent-aebb34f8957e5db45/target (44.0 GB) |
| 11:28 | janitor-delete | leela | janitor delete OCW-worktree-agent-aebb34f8957e5db45/target (6.2 GB) |
| 12:05 | unit-failed | deb | ocw-art-collect.service failed (exit-code) |
| 12:18 | janitor-delete | marge | janitor delete OCW-worktree-agent-a391bd88145028b9d/target (31.5 GB) |
| 12:26 | janitor-delete | Win11Builder | janitor delete OCW-worktree-agent-a649c02685a063272/target (8.9 GB) |
| 13:05 | unit-failed | deb | ocw-art-collect.service failed (exit-code) |
| 14:04 | unit-failed | deb | ocw-art-collect.service failed (exit-code) |
| 15:00 | unit-failed | deb | ocw-art-collect.service failed (exit-code) |
| 15:01 | janitor-delete | Win11Builder | janitor delete OCW-worktree-agent-aebb34f8957e5db45/target (8.0 GB) |
| 15:13 | janitor-delete | marge | janitor delete OCW-worktree-agent-a3d60721476281995/target (37.0 GB) |
| 15:13 | janitor-delete | leela | janitor delete OCW-worktree-agent-a3d60721476281995/target (12.7 GB) |
| 16:03 | unit-failed | deb | ocw-art-collect.service failed (exit-code) |
| 17:05 | unit-failed | deb | ocw-art-collect.service failed (exit-code) |
| 18:05 | unit-failed | deb | ocw-art-collect.service failed (exit-code) |
| 19:03 | unit-failed | deb | ocw-art-collect.service failed (exit-code) |
| 20:01 | unit-failed | deb | ocw-art-collect.service failed (exit-code) |
| 21:04 | machine-offline | Win11Builder | Win11Builder unreachable (ssh error) |
| 21:04 | unit-failed | deb | ocw-art-collect.service failed (exit-code) |
| 21:05 | machine-online | Win11Builder | Win11Builder back online |
| 22:04 | unit-failed | deb | ocw-art-collect.service failed (exit-code) |
| 23:02 | unit-failed | deb | ocw-art-collect.service failed (exit-code) |

## Media

| Time | File |
|---|---|
| 10:00:17 | [100017-shot-wayland-menu-input-mapping.jpg](100017-shot-wayland-menu-input-mapping.jpg) |
| 10:00:28 | [100028-shot-wayland-menu-input-mapping-junctions.jpg](100028-shot-wayland-menu-input-mapping-junctions.jpg) |
| 10:00:39 | [100039-shot-wayland-menu-input-mapping-capture.jpg](100039-shot-wayland-menu-input-mapping-capture.jpg) |
| 10:00:45 | [100045-shot-wayland-freeride-junction-keys.jpg](100045-shot-wayland-freeride-junction-keys.jpg) |
| 10:00:59 | [100059-shot-wayland-menu-host-options-voice.jpg](100059-shot-wayland-menu-host-options-voice.jpg) |
| 10:01:19 | [100119-shot-wayland-menu-host-options-voice-off.jpg](100119-shot-wayland-menu-host-options-voice-off.jpg) |
| 10:06:40 | [100640-shot-wayland-menu-host-summary-voice-off.jpg](100640-shot-wayland-menu-host-summary-voice-off.jpg) |
| 10:07:02 | [100702-shot-wayland-status-headphones-per-viewer.jpg](100702-shot-wayland-status-headphones-per-viewer.jpg) |
| 10:07:12 | [100712-shot-ocw.jpg](100712-shot-ocw.jpg) |
| 10:07:21 | [100721-shot-wayland-ocw-wayland.jpg](100721-shot-wayland-ocw-wayland.jpg) |
| 10:08:36 | [100836-shot-wayland-menu-host-summary-voice-off.jpg](100836-shot-wayland-menu-host-summary-voice-off.jpg) |
| 10:08:47 | [100847-shot-wayland-status-headphones-per-viewer.jpg](100847-shot-wayland-status-headphones-per-viewer.jpg) |
| 10:08:57 | [100857-shot-wayland-status-headphones-per-viewer-b.jpg](100857-shot-wayland-status-headphones-per-viewer-b.jpg) |
| 10:09:51 | [100951-shot-menu-input-mapping.jpg](100951-shot-menu-input-mapping.jpg) |
| 10:10:17 | [101017-shot-menu-input-mapping-junctions.jpg](101017-shot-menu-input-mapping-junctions.jpg) |
| 10:10:35 | [101035-shot-menu-input-mapping-capture.jpg](101035-shot-menu-input-mapping-capture.jpg) |
| 10:11:06 | [101106-shot-freeride-junction-keys.jpg](101106-shot-freeride-junction-keys.jpg) |
| 10:11:30 | [101130-shot-menu-host-options-voice.jpg](101130-shot-menu-host-options-voice.jpg) |
| 10:11:48 | [101148-shot-menu-host-options-voice-off.jpg](101148-shot-menu-host-options-voice-off.jpg) |
| 10:12:15 | [101215-shot-menu-host-summary-voice-off.jpg](101215-shot-menu-host-summary-voice-off.jpg) |
| 10:12:38 | [101238-shot-menu-hosting-voice-off.jpg](101238-shot-menu-hosting-voice-off.jpg) |
| 10:15:15 | [101515-shot-status-headphones-per-viewer.jpg](101515-shot-status-headphones-per-viewer.jpg) |
| 10:20:49 | [102049-shot-status-headphones-per-viewer-b.jpg](102049-shot-status-headphones-per-viewer-b.jpg) |
| 10:21:00 | [102100-shot-ocw.jpg](102100-shot-ocw.jpg) |
| 10:21:10 | [102110-shot-wayland-ocw-wayland.jpg](102110-shot-wayland-ocw-wayland.jpg) |
| 10:22:18 | [102218-shot-menu-host-options-voice.jpg](102218-shot-menu-host-options-voice.jpg) |
| 10:23:21 | [102321-shot-menu-host-options-voice-off.jpg](102321-shot-menu-host-options-voice-off.jpg) |
| 10:24:23 | [102423-shot-menu-host-summary-voice-off.jpg](102423-shot-menu-host-summary-voice-off.jpg) |
| 10:24:24 | [102424-shot-ocw.jpg](102424-shot-ocw.jpg) |
| 10:24:34 | [102434-shot-wayland-ocw-wayland.jpg](102434-shot-wayland-ocw-wayland.jpg) |
| 10:25:33 | [102533-shot-menu-hosting-voice-off.jpg](102533-shot-menu-hosting-voice-off.jpg) |
| 10:27:29 | [102729-shot-menu-host-options-voice.jpg](102729-shot-menu-host-options-voice.jpg) |
| 10:29:02 | [102902-shot-menu-host-options-voice-off.jpg](102902-shot-menu-host-options-voice-off.jpg) |
| 10:30:40 | [103040-shot-menu-host-summary-voice-off.jpg](103040-shot-menu-host-summary-voice-off.jpg) |
| 10:31:52 | [103152-shot-menu-hosting-voice-off.jpg](103152-shot-menu-hosting-voice-off.jpg) |
| 10:33:37 | [103337-shot-menu-host-options-voice.jpg](103337-shot-menu-host-options-voice.jpg) |
| 10:35:05 | [103505-shot-menu-host-options-voice-off.jpg](103505-shot-menu-host-options-voice-off.jpg) |
| 10:36:40 | [103640-shot-menu-host-summary-voice-off.jpg](103640-shot-menu-host-summary-voice-off.jpg) |
| 10:37:48 | [103748-shot-menu-hosting-voice-off.jpg](103748-shot-menu-hosting-voice-off.jpg) |
| 10:39:52 | [103952-web-web-calendar-select.jpg](103952-web-web-calendar-select.jpg) |
| 10:39:52 | [103952-web-web-calendar.jpg](103952-web-web-calendar.jpg) |
| 10:39:52 | [103952-web-web-console.jpg](103952-web-web-console.jpg) |
| 10:39:52 | [103952-web-web-damage-crash.jpg](103952-web-web-damage-crash.jpg) |
| 10:39:52 | [103952-web-web-damage-fresh.jpg](103952-web-web-damage-fresh.jpg) |
| 10:39:52 | [103952-web-web-devices-collapsed.jpg](103952-web-web-devices-collapsed.jpg) |
| 10:39:52 | [103952-web-web-devices-expanded.jpg](103952-web-web-devices-expanded.jpg) |
| 10:39:52 | [103952-web-web-gamepad.jpg](103952-web-web-gamepad.jpg) |
| 10:39:52 | [103952-web-web-gps.jpg](103952-web-web-gps.jpg) |
| 10:39:52 | [103952-web-web-history-delete.jpg](103952-web-web-history-delete.jpg) |
| 10:39:52 | [103952-web-web-history-ride-file.jpg](103952-web-web-history-ride-file.jpg) |
| 10:39:52 | [103952-web-web-history-ride-map.jpg](103952-web-web-history-ride-map.jpg) |
| 10:39:52 | [103952-web-web-hud.jpg](103952-web-web-hud.jpg) |
| 10:39:52 | [103952-web-web-input-mapping-capture.jpg](103952-web-web-input-mapping-capture.jpg) |
| 10:39:52 | [103952-web-web-input-mapping-junctions.jpg](103952-web-web-input-mapping-junctions.jpg) |
| 10:39:52 | [103952-web-web-input-mapping-swapped.jpg](103952-web-web-input-mapping-swapped.jpg) |
| 10:39:52 | [103952-web-web-input-mapping.jpg](103952-web-web-input-mapping.jpg) |
| 10:39:52 | [103952-web-web-join.jpg](103952-web-web-join.jpg) |
| 10:39:52 | [103952-web-web-menu.jpg](103952-web-web-menu.jpg) |
| 10:39:52 | [103952-web-web-photo-preview.jpg](103952-web-web-photo-preview.jpg) |
| 10:39:52 | [103952-web-web-ride.jpg](103952-web-web-ride.jpg) |
| 10:39:52 | [103952-web-web-riders.jpg](103952-web-web-riders.jpg) |
| 10:39:52 | [103952-web-web-settings.jpg](103952-web-web-settings.jpg) |
| 10:39:52 | [103952-web-web-strava-recording-downloaded.jpg](103952-web-web-strava-recording-downloaded.jpg) |
| 10:39:52 | [103952-web-web-strava-recording-saved-to-folder.jpg](103952-web-web-strava-recording-saved-to-folder.jpg) |
| 10:39:52 | [103952-web-web-strava-recording.jpg](103952-web-web-strava-recording.jpg) |
| 10:39:52 | [103952-web-web-strava-row.jpg](103952-web-web-strava-row.jpg) |
| 10:39:52 | [103952-web-web-strava-steps.jpg](103952-web-web-strava-steps.jpg) |
| 10:39:52 | [103952-web-web-touch-hints.jpg](103952-web-web-touch-hints.jpg) |
| 10:39:52 | [103952-web-web-touch-hold.jpg](103952-web-web-touch-hold.jpg) |
| 10:39:52 | [103952-web-web-unicorn-flight.jpg](103952-web-web-unicorn-flight.jpg) |
| 10:39:52 | [103952-web-web-unicorn-inspect.jpg](103952-web-web-unicorn-inspect.jpg) |
| 10:39:52 | [103952-web-web-unicorn-menu.jpg](103952-web-web-unicorn-menu.jpg) |
| 10:39:52 | [103952-web-web-weather.jpg](103952-web-web-weather.jpg) |
| 10:39:52 | [103952-web-web-workout-map.jpg](103952-web-web-workout-map.jpg) |
| 10:39:52 | [103952-web-web.jpg](103952-web-web.jpg) |
| 10:46:07 | [104607-web-web-world-first-loading.jpg](104607-web-web-world-first-loading.jpg) |
| 10:46:07 | [104607-web-web-world-junction-keys.jpg](104607-web-web-world-junction-keys.jpg) |
| 10:46:07 | [104607-web-web-world.jpg](104607-web-web-world.jpg) |
| 10:47:16 | [104716-shot-menu-input-mapping.jpg](104716-shot-menu-input-mapping.jpg) |
| 10:47:53 | [104753-shot-menu-input-mapping-junctions.jpg](104753-shot-menu-input-mapping-junctions.jpg) |
| 10:48:27 | [104827-shot-menu-input-mapping-capture.jpg](104827-shot-menu-input-mapping-capture.jpg) |
| 10:49:09 | [104909-shot-menu-input-mapping.jpg](104909-shot-menu-input-mapping.jpg) |
| 10:49:29 | [104929-shot-menu-input-mapping-junctions.jpg](104929-shot-menu-input-mapping-junctions.jpg) |
| 10:49:50 | [104950-shot-menu-input-mapping-capture.jpg](104950-shot-menu-input-mapping-capture.jpg) |
| 10:50:38 | [105038-shot-menu-input-mapping.jpg](105038-shot-menu-input-mapping.jpg) |
| 10:51:20 | [105120-shot-menu-input-mapping-junctions.jpg](105120-shot-menu-input-mapping-junctions.jpg) |
| 10:52:07 | [105207-shot-menu-input-mapping-capture.jpg](105207-shot-menu-input-mapping-capture.jpg) |
| 11:59:36 | [115936-video-wayland-collision-bump-video.jpg](115936-video-wayland-collision-bump-video.jpg) |
| 11:59:36 | [115936-video-wayland-collision-bump-video.mp4](115936-video-wayland-collision-bump-video.mp4) |
| 12:05:25 | [120525-video-wayland-k12-group-bump-video.jpg](120525-video-wayland-k12-group-bump-video.jpg) |
| 12:05:25 | [120525-video-wayland-k12-group-bump-video.mp4](120525-video-wayland-k12-group-bump-video.mp4) |
| 13:31:29 | [133129-web-memory-before-liechtenstein-webgpu-web-world-first-loading.jpg](133129-web-memory-before-liechtenstein-webgpu-web-world-first-loading.jpg) |
| 13:31:29 | [133129-web-memory-before-liechtenstein-webgpu-web-world-teleport.jpg](133129-web-memory-before-liechtenstein-webgpu-web-world-teleport.jpg) |
| 13:31:29 | [133129-web-memory-before-liechtenstein-webgpu-web-world.jpg](133129-web-memory-before-liechtenstein-webgpu-web-world.jpg) |
| 13:32:19 | [133219-web-memory-before-tenerife-webgpu-web-world-first-loading.jpg](133219-web-memory-before-tenerife-webgpu-web-world-first-loading.jpg) |
| 13:32:19 | [133219-web-memory-before-tenerife-webgpu-web-world-teleport.jpg](133219-web-memory-before-tenerife-webgpu-web-world-teleport.jpg) |
| 13:32:19 | [133219-web-memory-before-tenerife-webgpu-web-world.jpg](133219-web-memory-before-tenerife-webgpu-web-world.jpg) |
| 13:33:11 | [133311-web-memory-before-black-forest-north-webgpu-web-world-first-loading.jpg](133311-web-memory-before-black-forest-north-webgpu-web-world-first-loading.jpg) |
| 13:33:11 | [133311-web-memory-before-black-forest-north-webgpu-web-world-teleport.jpg](133311-web-memory-before-black-forest-north-webgpu-web-world-teleport.jpg) |
| 13:33:11 | [133311-web-memory-before-black-forest-north-webgpu-web-world.jpg](133311-web-memory-before-black-forest-north-webgpu-web-world.jpg) |
| 13:34:03 | [133403-web-memory-before-liechtenstein-webgl2-web-world-webgl2-first-loading.jpg](133403-web-memory-before-liechtenstein-webgl2-web-world-webgl2-first-loading.jpg) |
| 13:34:03 | [133403-web-memory-before-liechtenstein-webgl2-web-world-webgl2-teleport.jpg](133403-web-memory-before-liechtenstein-webgl2-web-world-webgl2-teleport.jpg) |
| 13:34:03 | [133403-web-memory-before-liechtenstein-webgl2-web-world-webgl2.jpg](133403-web-memory-before-liechtenstein-webgl2-web-world-webgl2.jpg) |
| 13:34:55 | [133455-web-memory-before-tenerife-webgl2-web-world-webgl2-first-loading.jpg](133455-web-memory-before-tenerife-webgl2-web-world-webgl2-first-loading.jpg) |
| 13:34:55 | [133455-web-memory-before-tenerife-webgl2-web-world-webgl2-teleport.jpg](133455-web-memory-before-tenerife-webgl2-web-world-webgl2-teleport.jpg) |
| 13:34:55 | [133455-web-memory-before-tenerife-webgl2-web-world-webgl2.jpg](133455-web-memory-before-tenerife-webgl2-web-world-webgl2.jpg) |
| 13:35:49 | [133549-web-memory-before-black-forest-north-webgl2-web-world-webgl2-first-loading.jpg](133549-web-memory-before-black-forest-north-webgl2-web-world-webgl2-first-loading.jpg) |
| 13:35:49 | [133549-web-memory-before-black-forest-north-webgl2-web-world-webgl2-teleport.jpg](133549-web-memory-before-black-forest-north-webgl2-web-world-webgl2-teleport.jpg) |
| 13:35:49 | [133549-web-memory-before-black-forest-north-webgl2-web-world-webgl2.jpg](133549-web-memory-before-black-forest-north-webgl2-web-world-webgl2.jpg) |
| 13:46:31 | [134631-web-memory-after-liechtenstein-webgpu-web-world-first-loading.jpg](134631-web-memory-after-liechtenstein-webgpu-web-world-first-loading.jpg) |
| 13:46:31 | [134631-web-memory-after-liechtenstein-webgpu-web-world-teleport.jpg](134631-web-memory-after-liechtenstein-webgpu-web-world-teleport.jpg) |
| 13:46:31 | [134631-web-memory-after-liechtenstein-webgpu-web-world.jpg](134631-web-memory-after-liechtenstein-webgpu-web-world.jpg) |
| 13:47:21 | [134721-web-memory-after-tenerife-webgpu-web-world-first-loading.jpg](134721-web-memory-after-tenerife-webgpu-web-world-first-loading.jpg) |
| 13:47:21 | [134721-web-memory-after-tenerife-webgpu-web-world-teleport.jpg](134721-web-memory-after-tenerife-webgpu-web-world-teleport.jpg) |
| 13:47:21 | [134721-web-memory-after-tenerife-webgpu-web-world.jpg](134721-web-memory-after-tenerife-webgpu-web-world.jpg) |
| 13:48:12 | [134812-web-memory-after-black-forest-north-webgpu-web-world-first-loading.jpg](134812-web-memory-after-black-forest-north-webgpu-web-world-first-loading.jpg) |
| 13:48:12 | [134812-web-memory-after-black-forest-north-webgpu-web-world-teleport.jpg](134812-web-memory-after-black-forest-north-webgpu-web-world-teleport.jpg) |
| 13:48:12 | [134812-web-memory-after-black-forest-north-webgpu-web-world.jpg](134812-web-memory-after-black-forest-north-webgpu-web-world.jpg) |
| 13:49:03 | [134903-web-memory-after-liechtenstein-webgl2-web-world-webgl2-first-loading.jpg](134903-web-memory-after-liechtenstein-webgl2-web-world-webgl2-first-loading.jpg) |
| 13:49:03 | [134903-web-memory-after-liechtenstein-webgl2-web-world-webgl2-teleport.jpg](134903-web-memory-after-liechtenstein-webgl2-web-world-webgl2-teleport.jpg) |
| 13:49:03 | [134903-web-memory-after-liechtenstein-webgl2-web-world-webgl2.jpg](134903-web-memory-after-liechtenstein-webgl2-web-world-webgl2.jpg) |
| 13:49:56 | [134956-web-memory-after-tenerife-webgl2-web-world-webgl2-first-loading.jpg](134956-web-memory-after-tenerife-webgl2-web-world-webgl2-first-loading.jpg) |
| 13:49:56 | [134956-web-memory-after-tenerife-webgl2-web-world-webgl2-teleport.jpg](134956-web-memory-after-tenerife-webgl2-web-world-webgl2-teleport.jpg) |
| 13:49:56 | [134956-web-memory-after-tenerife-webgl2-web-world-webgl2.jpg](134956-web-memory-after-tenerife-webgl2-web-world-webgl2.jpg) |
| 13:50:49 | [135049-web-memory-after-black-forest-north-webgl2-web-world-webgl2-first-loading.jpg](135049-web-memory-after-black-forest-north-webgl2-web-world-webgl2-first-loading.jpg) |
| 13:50:49 | [135049-web-memory-after-black-forest-north-webgl2-web-world-webgl2-teleport.jpg](135049-web-memory-after-black-forest-north-webgl2-web-world-webgl2-teleport.jpg) |
| 13:50:49 | [135049-web-memory-after-black-forest-north-webgl2-web-world-webgl2.jpg](135049-web-memory-after-black-forest-north-webgl2-web-world-webgl2.jpg) |
| 13:52:15 | [135215-web-memory-compare-black-forest-north-webgl2-before-after.jpg](135215-web-memory-compare-black-forest-north-webgl2-before-after.jpg) |
| 13:52:15 | [135215-web-memory-compare-black-forest-north-webgpu-before-after.jpg](135215-web-memory-compare-black-forest-north-webgpu-before-after.jpg) |
| 13:52:15 | [135215-web-memory-compare-liechtenstein-webgl2-before-after.jpg](135215-web-memory-compare-liechtenstein-webgl2-before-after.jpg) |
| 13:52:15 | [135215-web-memory-compare-liechtenstein-webgpu-before-after.jpg](135215-web-memory-compare-liechtenstein-webgpu-before-after.jpg) |
| 13:52:15 | [135215-web-memory-compare-tenerife-webgl2-before-after.jpg](135215-web-memory-compare-tenerife-webgl2-before-after.jpg) |
| 13:52:15 | [135215-web-memory-compare-tenerife-webgpu-before-after.jpg](135215-web-memory-compare-tenerife-webgpu-before-after.jpg) |
| 14:23:26 | [142326-web-web-calendar-select.jpg](142326-web-web-calendar-select.jpg) |
| 14:23:26 | [142326-web-web-calendar.jpg](142326-web-web-calendar.jpg) |
| 14:23:26 | [142326-web-web-console.jpg](142326-web-web-console.jpg) |
| 14:23:26 | [142326-web-web-damage-crash.jpg](142326-web-web-damage-crash.jpg) |
| 14:23:26 | [142326-web-web-damage-fresh.jpg](142326-web-web-damage-fresh.jpg) |
| 14:23:26 | [142326-web-web-devices-collapsed.jpg](142326-web-web-devices-collapsed.jpg) |
| 14:23:26 | [142326-web-web-devices-expanded.jpg](142326-web-web-devices-expanded.jpg) |
| 14:23:26 | [142326-web-web-downloads-OCW-2026-11-21-14-24-54.jpg](142326-web-web-downloads-OCW-2026-11-21-14-24-54.jpg) |
| 14:23:26 | [142326-web-web-downloads-ocw-2026-11-21-14-25-21.webm](142326-web-web-downloads-ocw-2026-11-21-14-25-21.webm) |
| 14:23:26 | [142326-web-web-gamepad.jpg](142326-web-web-gamepad.jpg) |
| 14:23:26 | [142326-web-web-gps.jpg](142326-web-web-gps.jpg) |
| 14:23:26 | [142326-web-web-history-delete.jpg](142326-web-web-history-delete.jpg) |
| 14:23:26 | [142326-web-web-history-ride-file.jpg](142326-web-web-history-ride-file.jpg) |
| 14:23:26 | [142326-web-web-history-ride-map.jpg](142326-web-web-history-ride-map.jpg) |
| 14:23:26 | [142326-web-web-hud.jpg](142326-web-web-hud.jpg) |
| 14:23:26 | [142326-web-web-input-mapping-capture.jpg](142326-web-web-input-mapping-capture.jpg) |
| 14:23:26 | [142326-web-web-input-mapping-junctions.jpg](142326-web-web-input-mapping-junctions.jpg) |
| 14:23:26 | [142326-web-web-input-mapping-swapped.jpg](142326-web-web-input-mapping-swapped.jpg) |
| 14:23:26 | [142326-web-web-input-mapping.jpg](142326-web-web-input-mapping.jpg) |
| 14:23:26 | [142326-web-web-join.jpg](142326-web-web-join.jpg) |
| 14:23:26 | [142326-web-web-menu.jpg](142326-web-web-menu.jpg) |
| 14:23:26 | [142326-web-web-photo-preview.jpg](142326-web-web-photo-preview.jpg) |
| 14:23:26 | [142326-web-web-ride.jpg](142326-web-web-ride.jpg) |
| 14:23:26 | [142326-web-web-riders.jpg](142326-web-web-riders.jpg) |
| 14:23:26 | [142326-web-web-settings.jpg](142326-web-web-settings.jpg) |
| 14:23:26 | [142326-web-web-strava-recording-downloaded.jpg](142326-web-web-strava-recording-downloaded.jpg) |
| 14:23:26 | [142326-web-web-strava-recording-saved-to-folder.jpg](142326-web-web-strava-recording-saved-to-folder.jpg) |
| 14:23:26 | [142326-web-web-strava-recording.jpg](142326-web-web-strava-recording.jpg) |
| 14:23:26 | [142326-web-web-strava-row.jpg](142326-web-web-strava-row.jpg) |
| 14:23:26 | [142326-web-web-strava-steps.jpg](142326-web-web-strava-steps.jpg) |
| 14:23:26 | [142326-web-web-touch-hints.jpg](142326-web-web-touch-hints.jpg) |
| 14:23:26 | [142326-web-web-touch-hold.jpg](142326-web-web-touch-hold.jpg) |
| 14:23:26 | [142326-web-web-unicorn-flight.jpg](142326-web-web-unicorn-flight.jpg) |
| 14:23:26 | [142326-web-web-unicorn-inspect.jpg](142326-web-web-unicorn-inspect.jpg) |
| 14:23:26 | [142326-web-web-unicorn-menu.jpg](142326-web-web-unicorn-menu.jpg) |
| 14:23:26 | [142326-web-web-weather.jpg](142326-web-web-weather.jpg) |
| 14:23:26 | [142326-web-web-workout-map.jpg](142326-web-web-workout-map.jpg) |
| 14:23:26 | [142326-web-web.jpg](142326-web-web.jpg) |
| 14:30:04 | [143004-web-web-webkit-iphone-hints.png](143004-web-web-webkit-iphone-hints.png) |
| 14:30:04 | [143004-web-web-webkit-iphone-hold.png](143004-web-web-webkit-iphone-hold.png) |
| 14:30:04 | [143004-web-web-webkit-iphone-landscape-hints.png](143004-web-web-webkit-iphone-landscape-hints.png) |
| 14:30:04 | [143004-web-web-webkit-iphone-landscape-hold.png](143004-web-web-webkit-iphone-landscape-hold.png) |
| 14:30:04 | [143004-web-web-webkit-iphone-landscape-riding.png](143004-web-web-webkit-iphone-landscape-riding.png) |
| 14:30:04 | [143004-web-web-webkit-iphone-landscape-stopped.png](143004-web-web-webkit-iphone-landscape-stopped.png) |
| 14:30:04 | [143004-web-web-webkit-iphone-landscape.png](143004-web-web-webkit-iphone-landscape.png) |
| 14:30:04 | [143004-web-web-webkit-iphone-riding.png](143004-web-web-webkit-iphone-riding.png) |
| 14:30:04 | [143004-web-web-webkit-iphone-start.png](143004-web-web-webkit-iphone-start.png) |
| 14:30:04 | [143004-web-web-webkit-iphone-stopped.png](143004-web-web-webkit-iphone-stopped.png) |
| 14:30:04 | [143004-web-web-webkit-iphone.png](143004-web-web-webkit-iphone.png) |
| 14:30:04 | [143004-web-web-webkit-mac.png](143004-web-web-webkit-mac.png) |
