# OCW build diary – day 8, 2026-11-18

75 commits (28 merges), +27013 / −1847 lines, 942 images, 9 videos, 0 sounds.

## Commits

| Time | Commit | |
|---|---|---|
| 00:01 | `392669c` | Build dashboard 1.7.0: battery of laptops and the Meta Quest on the machine cards |
| 00:04 | `8e3f79c` | Road damage: format, clippy, the remaining RoadStrip literals |
| 00:09 | `5b98228` | Config secrets in a separate secrets.toml; Connect to a server = address field + recent servers; no start choice in the browser; 'cannot hear you' only by choice; who hears me and whom I hear are two separate voice settings (decisions from the build dashboard, 2026-11-18; §3.2.4 Q2/Q5/Q6, §7.1.7 Q12/Q16; spec 4.70) |
| 00:09 | `52152c7` (merge) | Merge the build dashboard's battery readings: Weela's laptop battery (draining on mains warned), the Quest's battery and Link state from the runtime's log and cache (dashboard 1.7.0) |
| 00:25 | `439f253` | The HUD has a navigation map in the lower right corner, styled like a bike computer (spec 4.68, §3.2 Navigation map) |
| 00:26 | `97a9e22` (merge) | Merge origin/main into merge/studio-logo |
| 00:27 | `092bb0e` | Keep the remembered devices in ~/.config/ocw/devices.toml and install an example strava.toml there on kiosk deploys (spec 4.70) |
| 00:27 | `1caf480` | Release 0.2.3 |
| 00:31 | `489d971` (merge) | Merge remote-tracking branch 'origin/main' into worktree-agent-a01e442248925aa9a |
| 00:36 | `a2fa503` | CLAUDE.md: the kiosk app is stopped and has no autostart; never re-enable it unless the user asks |
| 01:07 | `8491d33` | OCW Studio's Models workspace shows every model file: browser, viewer, stats, the validator's findings and the try-on; ocw-assets model import / export / diff and the extended validator (spec 4.66, §14 Phase 16 16B / E3, Phase 15 M2 15J) |
| 01:07 | `ef95087` | Near-field ground detail beside the roads: stones, gravel, rocks, dirt patches, tufts, stalks, ferns, shrubs, leaves, needles, cones, twigs (spec 4.71, §4.6.2) |
| 01:08 | `01dac42` (merge) | Merge OCW Studio's Models workspace (E3) and the model tools (M2): browser, viewer with light presets, LOD, gizmos, try-on, the extended validator, model diff / import / export (spec 4.71) |
| 01:17 | `3be1452` | CLAUDE.md: never record a build machine's whole desktop for test media; only the app's window |
| 01:23 | `a4b6861` | road.damage: draw every road in one OSM smoothness (screenshots of each level); spec 4.71 draft |
| 01:26 | `de42d4b` | Road damage: skip what the pixel footprint fades, wheel tracks once, shorter reach |
| 01:30 | `fc20600` | README: new in-game pictures of today's main (HUD, riders, workshop, browser) |
| 01:31 | `267ad66` (merge) | Merge the README's new in-game pictures of 2026-11-17 (hero, worlds, workshop, bike stand, browser) |
| 01:47 | `e2684ca` | Navigation map: the fps cost measured on marge (map on 38.6 fps, off 38.5 fps; spec §3.2) |
| 02:34 | `eab6c7b` | Road damage: larger, more frequent potholes on bad roads; stones in the surface's tone; stronger cracks |
| 02:39 | `ff38918` (merge) | Merge origin/main into merge/models-e3 |
| 02:40 | `9bb45b6` (merge) | Merge the near-field ground detail: stones, gravel, dirt, moss, leaves, twigs and small plants beside the road, by region, season and snow (spec 4.72) |
| 02:43 | `229287e` | Spec 4.71: smoothness shares per world, fps on marge |
| 02:57 | `29dd08b` | Release scripts: scripts/release-linux.sh (AppImage + tarball with ocw-studio) and scripts/release-web.sh (browser zip with README), used for v0.2.3 |
| 02:59 | `5ff8dc4` (merge) | Merge the release scripts used for 0.2.3 (scripts/release-linux.sh, scripts/release-web.sh) |
| 03:15 | `a111f5d` | Place names in the world packages and on the studio's 2D map: smaller places hidden when crowded (spec 4.66, §4.7, §14 Phase 16 16A) |
| 03:25 | `78fa791` (merge) | Merge origin/main into merge/ground-detail |
| 03:28 | `2516418` | ocw-weather: compare the Open-Meteo visibility within 0.1 m (MSVC parses 34419.996, so the Windows test failed) |
| 03:28 | `c1d7a41` (merge) | Merge the HUD navigation map: a bike-computer style map in the lower right, heading-up, route in magenta, next-turn banner, auto zoom, night palette; the shared ocw-map crate (spec 4.73) |
| 03:59 | `3393004` | A photo just saved shows for 3 seconds in the HUD; photos and screenshots go to the Pictures folder's OCW, in the browser to a folder chosen once or as OCW-… downloads (spec 4.73, §3.2 Photo preview, §2.11 Q3) |
| 04:01 | `2fdc8de` (merge) | Merge remote-tracking branch 'origin/main' into worktree-agent-a01e442248925aa9a |
| 04:11 | `b9846ba` | Simple Strava upload for every rider, no API app: Upload to Strava (in your browser) and Marked as uploaded on a ride's page (spec 4.71, §2.8.1 Simple upload) |
| 04:25 | `1311863` (merge) | Merge the 3-second photo preview in the HUD and the photos folder Pictures/OCW (desktop and browser; spec 4.74, §2.11 Q3) |
| 04:32 | `ca55633` (merge) | Merge remote-tracking branch 'origin/main' into worktree-agent-a01c5b7f390a5e38e |
| 04:59 | `19a2ab8` (merge) | Merge cracks, potholes and loose stones on the roads, set by OSM smoothness (surface, tracktype; RCND package section, world-builder condition; spec 4.75) |
| 05:00 | `f9e733f` (merge) | Merge origin/main (photo preview, Pictures/OCW photos folder) into strava-simple-upload; the Strava upload copies the ride's photos from the photos folder through their sidecars; Strava row renumbered 4.76 |
| 05:02 | `35b8b0b` | ocw-map: the test package's road strip gets the new condition field (merge of road damage) |
| 05:24 | `e0c8eae` (merge) | Merge origin/main; place names on the HUD navigation map: PLCE places fill the labels hook, chosen by zoom and decluttered with layout_labels (spec 4.74, §3.2 Navigation map) |
| 05:33 | `c568f57` (merge) | Merge the simple Strava upload in the browser for every rider (no API app, no subscription): ride page row, file manager + strava.com/upload/select, Marked as uploaded; S records without strava.toml (spec 4.76) |
| 06:20 | `c1685a8` | Navigation map names: a long name beside the rider goes above the arrow, boxes move into the map, the text node uses the layout's box (no clipped names); regression test (spec 4.74) |
| 06:20 | `9d2c2c1` | cargo fmt (navigation map names) |
| 06:27 | `3fece53` | Navigation map names over the route and the riders' dots, on a translucent pill in the map's ground colour (day and night); stacking regression test (spec 4.74) |
| 06:28 | `d97076a` (merge) | Merge place names: PLCE package section, world-builder places, decluttered labels on the studio map and on the HUD navi map (spec 4.77) |
| 06:28 | `c05846c` | ocw-world: the places test's comment names spec 4.77 (renumbered at merge) |
| 06:54 | `ff5e128` | README: link the OCW Build Diary (the art project) at the top – the diary video, the day galleries, the repository |
| 07:08 | `a31b7d5` | Standalone VR starts with WebXR on the Quest 1: V8 WebXR basic first, measure in the headset, then decide between V3 and native (Phase 14 Q5 decided; plan 14I; spec 4.78) |
| 09:32 | `04a94fb` | Frame time p50 / p95 in the render-rate log and measure-fps.sh; feature-fps-cost.sh measures single render features on a quiet machine |
| 10:34 | `c8fcfb5` | Every Strava (S … S) recording is written to the user's home directory: FIT and photos in a subfolder of ~/Pictures/OCW named by ISO date and location (the user; §2.8.1, Q7 superseded; spec 4.79) |
| 10:37 | `cdc7736` | Strava recordings go to ~/Activities/OCW, user-configurable (activities.folder in the settings file, Menu → Settings); other photos stay in ~/Pictures/OCW (the user; §2.8.1; spec 4.80) |
| 10:41 | `c2c6abe` | Bike forks raked forward: the blades run down the steering axis and bend forward to the axle (spec §14 Phase 15, bug fix) |
| 10:42 | `1dfd88d` | Plan for ANT+ heart-rate straps: second device backend over an ANT USB stick, desktop first; planning only, open questions (spec 4.79) |
| 10:43 | `05860eb` (merge) | Merge the plan for ANT+ heart-rate straps (§3.4.1, Phase 17; planning, open questions; spec 4.81) |
| 11:00 | `87bf557` | Spec 4.79 / 15K: the fork raked forward (bug fix note); rustfmt of the fork tests |
| 11:12 | `dfc65f6` | Every S recording is written to its own folder in ~/Activities/OCW (FIT and photos, YYYY-MM-DD <place>), in both apps; the simple upload opens that folder (§2.8.1; spec 4.81) |
| 11:15 | `153e3dd` | One folder for everything OCW saves: ~/Activities/OCW; the photos folder ~/Pictures/OCW and photos.folder go away (the user; §2.8.1, §2.11; spec 4.82) |
| 11:15 | `bafcfe5` (merge) | Merge origin/main (spec 4.82: one folder for everything) |
| 11:30 | `62052ca` (merge) | Merge the bike forks raked forward: blades curve forward to the axle, the MTB fork ahead of the steering axis; all six bikes re-exported (spec 4.83, 15K) |
| 11:32 | `eeef7f1` | One folder for everything: screenshots and loose photos go to a per-day folder in ~/Activities/OCW; the photos folder and photos.folder are gone (§2.8.1, spec 4.82 built as 4.83) |
| 11:39 | `b68adc4` | CI: install the Linux packages without recommends (126 MB → a fraction) and give each apt attempt its own 5 min limit, so a slow mirror is retried instead of timing out the step |
| 11:49 | `2f76e3f` | test-activities-folder.sh: pictures at game times (X11 software rendering lags the wall clock) |
| 12:03 | `5657002` (merge) | Merge origin/main into merge/fork |
| 12:23 | `ee694b8` (merge) | Merge one folder for everything: S recordings (FIT + photos) in ~/Activities/OCW/<date place>, loose photos per day, activities.folder in settings and Menu, the photos folder removed; S in the browser too (spec 4.84) |
| 12:41 | `9dbe804` | README: where OCW keeps its files on Linux, Windows and macOS (config, data, activities folders, the overrides, the browser) |
| 12:42 | `1e659ad` | Strava recording without Strava set up: S always records, the recording waits locally and is uploaded once credentials are provided (the user; §2.8.1) |
| 12:47 | `ef0fa38` (merge) | Merge remote-tracking branch 'origin/main' into merge/activities |
| 13:30 | `f3faffd` | Strava recordings made without Strava set up wait and are uploaded once the credentials come; ask before more than three (spec §2.8.1, 4.86) |
| 13:34 | `e5bf0eb` | CLAUDE.md: Weela takes general building tasks too; watch its battery (user 2026-11-18) |
| 14:13 | `6b716af` (merge) | Merge remote-tracking branch 'origin/main' into strava-pending |
| 14:14 | `8c44d49` (merge) | Merge Strava recordings without set-up: waiting locally, uploaded when credentials appear (also while running), ask before more than 3; ride-page states (spec 4.86) |
| 14:15 | `4fa23fa` | Release 0.2.4 |
| 18:41 | `6165503` | Ground detail, road damage and the HUD navigation map cost under 0.2 ms a frame each at 1080p High on marge's GPU – measured on a quiet machine, nothing to cut (spec 4.87) |
| 18:42 | `5023175` (merge) | Merge the frame-rate cost of ground detail, road damage and the navi map, measured on a quiet marge: each under 0.2 ms at 1080p High; --log-fps p50/p95, scripts/feature-fps-cost.sh (spec 4.87) |
| 21:23 | `14b7572` | CLAUDE.md: leela builds again with a battery guard (stop below 20 %, start above 80 %; user 2026-11-18) |
| 21:32 | `d981459` | Build dashboard 1.8.0: battery guard – leela stops building below 20 % and builds again above 80 % |
| 21:33 | `d6c7640` (merge) | Merge the build dashboard's battery guard per machine (leela: stop below 20 %, start above 80 %; dashboard 1.8.0) |

## Builds and build servers

138 build/test runs on the build machines, 48.1 h in total, 15 failed; 1439 server samples; cargo compiled 23477 crates in 7.4 h, 20.9 h waiting for build slots.

| Machine | Runs | Hours | Cargo h | Crates | Waited h | Failed | Online |
|---|---|---|---|---|---|---|---|
| Weela | 0 | 0.0 | 0.0 | 0 | 0.0 | 0 | 64% |
| Win11Builder | 26 | 6.6 | 1.7 | 1450 | 3.0 | 7 | 100% |
| leela | 0 | 0.0 | 0.0 | 0 | 0.0 | 0 | 12% |
| macos | 25 | 3.4 | 0.6 | 1487 | 1.1 | 1 | 100% |
| marge | 87 | 38.1 | 5.1 | 20540 | 16.8 | 7 | 100% |

Failed runs:

- 00:23 Win11Builder: `cargo clippy -p ocw-world -p ocw-worldgen -p ocw-worldstore -p ocw-sim -p ocw-re` (exit 101, log `build-log/002335-Win11Builder-279631.log`)
- 01:20 Win11Builder: `cargo clippy -p ocw-desktop --all-targets -- -D warnings 2>&1 | Select-String -P` (exit 101, log `build-log/012029-Win11Builder-391231.log`)
- 02:41 Win11Builder: `cargo fmt --all -- --check; if ($LASTEXITCODE) { "FMT-FAILED"; exit 1 }; cargo c` (exit 1, log `build-log/024103-Win11Builder-527840.log`)
- 03:26 Win11Builder: `cargo fmt -p ocw-weather -- --check; if ($LASTEXITCODE) { "FMT-FAILED" }; cargo ` (exit 101, log `build-log/032650-Win11Builder-622986.log`)
- 03:27 Win11Builder: `cargo test -q -p ocw-weather --test real_weather 2>&1 | Select-String -Context 0` (exit 255, log `build-log/032723-Win11Builder-623741.log`)
- 04:59 marge: `set -e; make check; make test-smoke; echo ALL-CHECKS-OK` (exit 2, log `build-log/045927-marge-769364.log`)
- 05:02 Win11Builder: `cargo clippy -p ocw-map -p ocw-world -p ocw-worldgen -p ocw-render -p ocw-studio` (exit 1, log `build-log/050236-Win11Builder-776178.log`)
- 05:33 marge: `set -e; make check; make test-smoke; echo ALL-CHECKS-OK` (exit 2, log `build-log/053341-marge-832153.log`)
- 10:32 marge: `cargo test -q -p ocw-assets --lib forks_are_raked_forward 2>&1 | tail -15 && car` (exit 128, log `build-log/103230-marge-1296067.log`)
- 10:53 marge: `set -e; cargo fmt --all -- --check; echo FMT_OK; cargo clippy -q --workspace --a` (exit 1, log `build-log/105323-marge-1324830.log`)
- 13:07 marge: `cargo fmt --all && out=test-output/2026-11-18/strava-pending && scripts/test-str` (exit 1, log `build-log/130729-marge-1550257.log`)
- 13:07 Win11Builder: `cargo clippy -p ocw-desktop --all-targets -- -D warnings 2>&1 | Select-String -P` (exit 101, log `build-log/130733-Win11Builder-1550424.log`)
- 14:16 macos: `OCW_SHA=4fa23fa OCW_FEATURES=ocw-desktop/voice scripts/build-macos-app.sh && OCW` (exit 101, log `build-log/141651-macos-1658147.log`)
- 18:34 marge: `OCW_TEST_OUTPUT=off test-output/feature-fps-cost/shots.sh` (exit 127, log `build-log/183410-marge-2016774.log`)
- 18:39 marge: `cargo fmt --all --check && cargo clippy -q -p ocw-render -p ocw-desktop --all-ta` (exit 127, log `build-log/183910-marge-2023063.log`)

Longest runs:

- 152 min on marge: `crates/ocw-world/examples/road-damage-job2.sh`
- 110 min on marge: `scripts/release-linux.sh`
- 105 min on marge: `cargo build -p ocw-desktop 2>&1 | tail -2 && bash test-output/pp-shots.sh`
- 104 min on marge: `bash test-output/pp-full.sh`
- 96 min on marge: `cargo fmt --all --check && echo FMT-OK; cargo clippy --workspace --all-targets -`

## Token usage

883.3 M tokens in 2,779 model messages (output 1.5 M, cache reads 855.9 M, cache writes 25.8 M, uncached input 6 k). Full breakdown: [tokens.json](tokens.json).

| Feature | Tokens | Output | Messages |
|---|---|---|---|
| Other | 341.5 M | 690 k | 1,118 |
| UI & menus | 237.7 M | 309 k | 637 |
| Build, release & infra | 128.5 M | 199 k | 473 |
| Worlds & terrain | 70.0 M | 106 k | 185 |
| Planning & spec | 49.9 M | 80 k | 133 |
| Riders & bikes | 32.3 M | 73 k | 175 |
| Art project | 22.4 M | 32 k | 54 |
| Sky, time & weather | 942 k | 1 k | 4 |

| Task | Feature | Tokens | Output |
|---|---|---|---|
| agent: HUD photo preview for 3 s | UI & menus | 93.7 M | 127 k |
| agent: Road cracks and potholes | Other | 82.1 M | 57 k |
| coordination: can you stop and disable the kiosk app? dont make it startup per default | UI & menus | 72.4 M | 80 k |
| agent: S recordings to ~/Pictures/OCW/<date place> | Other | 69.1 M | 159 k |
| agent: Place names in packages and studio map | Worlds & terrain | 66.6 M | 98 k |
| agent: Strava manual upload, no API app | Other | 65.7 M | 130 k |
| agent: HUD navi map, lower right (retry) | UI & menus | 55.5 M | 44 k |
| coordination: use weela for building tasks, too. keep an eye on the battery consumption. | Build, release & infra | 53.4 M | 26 k |
| agent: WebXR W0 + W1 spike (Quest 1) | Other | 35.0 M | 136 k |
| agent: Strava: record now, upload when set up | Other | 34.0 M | 113 k |
| agent: Fix the bike fork direction | Riders & bikes | 26.6 M | 65 k |
| agent: Release 0.2.3, all platforms + web | Build, release & infra | 25.6 M | 63 k |
| agent: Ground detail: dirt, stones, plant debris | Planning & spec | 19.8 M | 16 k |
| agent: Day 7 video, melodic deep house | Other | 16.0 M | 53 k |
| coordination: add the battery watcher for leela. stop building on leela when battery <20% and … | Build, release & infra | 16.0 M | 8 k |
| coordination: fix the failing gh runner job | Other | 15.5 M | 9 k |
| agent: Quiet-machine fps: ground detail, road damage, navi map | Build, release & infra | 14.2 M | 57 k |
| agent: VR session lost every ~60 s on Weela | Planning & spec | 13.3 M | 9 k |
| coordination: how q5 is decided? | Other | 9.7 M | 6 k |
| agent: Release 0.2.4, all platforms + web | Build, release & infra | 9.4 M | 34 k |
| agent: Dashboard battery guard per machine | UI & menus | 8.4 M | 48 k |
| coordination: collect all day 7 media and create the day video. use music style: melodic deep … | Other | 8.2 M | 6 k |
| coordination: add to specification: for the art project: estimate also the co2 footprint for t… | Art project | 6.9 M | 7 k |
| coordination: once thats done and merged, bump version and release all platforms. | Build, release & infra | 6.8 M | 3 k |
| agent: README: new in-game pictures | Art project | 6.1 M | 15 k |
| coordination: instead of "~/Pictures/OCW" put it to "~/Activities/OCW". Make it user configura… | UI & menus | 5.5 M | 5 k |
| coordination: spec update and implement: allow strava recording even if strava not set up. jus… | Planning & spec | 5.4 M | 6 k |
| coordination: link the art project in the ocw readme and vice versa | Art project | 4.9 M | 4 k |
| coordination: Spec that the activity and photos for a Strava (s...s) recording should always b… | Planning & spec | 4.8 M | 6 k |
| agent: Plan ANT+ heart rate support (spec) | Planning & spec | 4.3 M | 40 k |
| coordination: where is the config stored on windows? document for all platforms in readme. | Art project | 4.0 M | 4 k |
| coordination: plan for this: start with V8 WebXR basic (about 1–2 days). After the first heads… | Worlds & terrain | 3.3 M | 9 k |
| agent: Studio Models workspace viewer (E3) | Riders & bikes | 3.3 M | 5 k |
| coordination: bump version and push a release for all plattforms including browser | Build, release & infra | 3.2 M | 7 k |
| coordination: plan for ANT+ heart rate sensor support | Planning & spec | 2.4 M | 3 k |
| coordination: turn around the bike fork (check images), it should point forwarrd, not backward… | Riders & bikes | 2.4 M | 2 k |
| coordination: is there a way to upload strave rides without a subscription? | Other | 2.3 M | 7 k |
| agent: Dashboard: Weela + Quest battery | UI & menus | 2.2 M | 5 k |
| coordination: Remove the photo folder and just use the activities folder and put everything th… | Other | 1.2 M | 2 k |
| coordination: is 3d acceleration used when the hw has it? | Other | 1.1 M | 1 k |

## Prompts

23 prompts (full text: [prompts.md](prompts.md)).

| Time | Prompt |
|---|---|
| 00:07 | is there a way to upload strave rides without a subscription? |
| 00:23 | is the sun already visible in the game? |
| 00:26 | bump version and push a release for  all plattforms including browser |
| 00:31 | how much effort (time/tokens) for building the standalond Oculus rift ap? |
| 00:32 | can you implement the simple strava upload for users without subscription? |
| 00:35 | can you stop and disable the kiosk app? dont make it startup per default |
| 06:52 | link the art project in the ocw readme and vice versa |
| 06:54 | is 3d acceleration used when the hw has it? |
| 07:07 | plan for this: start with V8 WebXR basic (about 1–2 days). After the first headset run, measure the frame rate on the Quest 1. Then decide w |
| 07:08 | how q5 is decided? |
| 09:24 | collect all day 7 media and create the day video. use music style: melodic deep house |
| 10:24 | turn around the bike fork (check images), it should point forwarrd, not backwards as of now |
| 10:31 | plan for ANT+ heart rate sensor support |
| 10:34 | Spec that the activity and photos for a Strava (s...s) recording should always be written to the users home dir (do we have a dir there alre |
| 10:37 | instead of "~/Pictures/OCW" put it to "~/Activities/OCW". Make it user configurable in config file and UI Menu -> Settings. |
| 11:14 | Remove the photo folder and just use the activities folder and put everything there. |
| 11:27 | add to specification: for the art project: estimate also the co2 footprint for the token usage and log that and show it in the video |
| 11:38 | fix the failing gh runner job |
| 12:40 | where is the config stored on windows? document for all platforms in readme. |
| 12:41 | spec update and implement: allow strava recording even if strava not set up. just save the recording locally and do the upload when credetia |
| 12:43 | once thats done and merged, bump version and release all platforms. |
| 13:33 | use weela for building tasks, too. keep an eye on the battery consumption. |
| 21:21 | add the battery watcher for leela. stop building on leela when battery <20% and only start when >80% |

## Features

20 spec versions added, 16 landed by a merge; 0 deploys, 2 releases.

| Spec | Feature | Landed | Check (marge) |
|---|---|---|---|
| 4.67 | The hands hold the bar the right way up | 00:26 `97a9e22` (merge) | – |
| 4.69 | Ride photos are saved in the user's photos folder, subfolder OCW | 00:26 `97a9e22` (merge) | – |
| 4.70 | Config secrets in a separate secrets.toml | 00:26 `97a9e22` (merge) | – |
| 4.71 | OCW Studio's Models workspace shows every model file | 01:08 `01dac42` (merge) | ok at 01:08, 72 suites, 2832 passed, 0 failed (commit) |
| 4.72 | Near-field ground detail | 02:40 `9bb45b6` (merge) | – |
| 4.73 | The HUD has a navigation map in the lower right corner, styled like a bike computer | 03:28 `c1d7a41` (merge) | ok at 03:28, 74 suites, 2866 passed, 0 failed (commit) |
| 4.74 | A photo just saved shows for 3 seconds in the HUD | 04:25 `1311863` (merge) | ok at 04:25, 74 suites, 2878 passed, 0 failed (commit) |
| 4.75 | Cracks, potholes and loose stones on the roads, by OSM smoothness | 04:59 `19a2ab8` (merge) | exit 2 at 04:59 (commit) |
| 4.76 | Simple Strava upload for every rider, no API app | 05:33 `c568f57` (merge) | ok at 06:04 (commit) |
| 4.77 | Place names in the world packages, on the studio's 2D map and on the HUD's navigation map | 06:28 `d97076a` (merge) | ok at 06:28, 74 suites, 2925 passed, 0 failed (commit) |
| 4.78 | Standalone VR starts with WebXR on the Quest 1 | 07:08 `a31b7d5` | – |
| 4.79 | Every Strava recording is written to the user's home directory | 10:34 `c8fcfb5` | – |
| 4.80 | Strava recordings go to ~/Activities/OCW, a folder the user sets in the settings file and… | 10:37 `cdc7736` | – |
| 4.81 | Plan for ANT+ heart-rate straps | 10:43 `05860eb` (merge) | – |
| 4.82 | One folder for everything | 11:15 `153e3dd` | – |
| 4.83 | Bike forks raked forward | 11:30 `62052ca` (merge) | ok at 11:30, 74 suites, 2927 passed, 0 failed (commit) |
| 4.84 | Strava recording without Strava set up | 12:47 `ef0fa38` (merge) | ok at 13:00, 5 suites, 683 passed, 0 failed (commit) |
| 4.85 | One folder for everything, built | 12:47 `ef0fa38` (merge) | ok at 13:00, 5 suites, 683 passed, 0 failed (commit) |
| 4.86 | Strava recordings made without Strava set up wait and are uploaded once the credentials c… | 14:14 `8c44d49` (merge) | – |
| 4.87 | Ground detail, road damage and the HUD navigation map cost under 0.2 ms a frame each at 1… | 18:42 `5023175` (merge) | ok at 18:42, 74 suites, 2948 passed, 0 failed (commit) |

Releases:

- 15:00 v0.2.4 (pre-release)
- 02:56 v0.2.3 (pre-release)

## Agent jobs

21 jobs (coordinator log agents.jsonl).

| Task | Branch | Start | End | Status | Interrupted | Merged |
|---|---|---|---|---|---|---|
| Dashboard: battery of Weela and the Quest | a578ee7f | 00:09 | 00:09 | merged |  |  |
| OCW Studio logo and app icons on all platforms | a03e9957 | 00:26 | 00:26 | merged |  |  |
| Release 0.2.3: all platforms and the browser | a087f238 | 00:28 | 02:59 | merged |  |  |
| Strava: simple upload in the browser, no API app | a01c5b7f | 00:33 | 06:05 | merged |  |  |
| Studio Models workspace viewer (E3) + model tools (M2) | a64cacd3 | 01:08 | 02:39 | merged |  |  |
| Ground detail: dirt, stones, plant debris | a95d1490 | 01:18 | 03:25 | merged |  |  |
| VR: fallback, no autostart, ffmpeg | a716a1c9 | 01:18 | 01:18 | reported |  |  |
| README: new in-game pictures | a98ff53f | 01:31 | 01:31 | merged |  |  |
| HUD navi map (lower right), like a bike computer | ad1a2665 | 01:57 | 04:23 | merged |  |  |
| Place names in packages and the studio map | a57dfc7b | 03:16 | 06:53 | merged |  |  |
| HUD: show a new photo for 3 s; photos in Pictures/OCW | aa66d7f8 | 04:05 | 04:57 | merged |  |  |
| Road cracks and potholes from OSM smoothness | a01e4422 | 04:09 | 05:32 | merged |  |  |
| WebXR on the Quest 1: W0 platform check, W1 spike | afa9d0fc | 07:08 | 08:15 | reported |  |  |
| Frame-rate cost on a quiet marge: ground detail, road damage, navi map | ac5f29b3 | 09:11 | 19:01 | merged |  |  |
| Art: day 7 video, melodic deep house | ae27345c | 09:25 | 09:49 | merged |  |  |
| Bike fork pointing forward | a3a217ad | 10:25 | 12:03 | merged |  |  |
| Plan: ANT+ heart rate support | aa3aa462 | 10:32 | 10:43 | merged |  |  |
| S recordings to ~/Pictures/OCW/<date place> | a367743c | 10:35 | 12:47 | merged |  |  |
| Strava: record without set-up, upload when credentials appear | a32984c5 | 12:42 | 14:14 | merged |  |  |
| Release 0.2.4: all platforms and the browser | aad4cbe9 | 14:16 | 15:01 | merged |  |  |
| Dashboard: battery guard per machine (leela 20/80) | ad48f3db | 21:23 | 21:34 | merged |  |  |

## Incidents

51 collected (disk-full 2, janitor-delete 35, machine-offline 7, machine-online 6, runs-failed 1), 0 with root-cause notes ([incidents.md](incidents.md)).

| Time | Kind | Machine | What |
|---|---|---|---|
| 00:00 | machine-offline | leela | leela unreachable (no route to host) |
| 00:09 | disk-full | Win11Builder | disk C: on Win11Builder at 90 % |
| 00:27 | janitor-delete | marge | janitor delete OCW-worktree-agent-a03e9957572339d7f/target (29.1 GB) |
| 00:32 | janitor-delete | Win11Builder | janitor delete OCW-worktree-agent-a09cdbcff127205c5/target (6.0 GB) |
| 00:32 | janitor-delete | Win11Builder | janitor delete OCW-worktree-agent-a18d20449774f2675/target (2.1 GB) |
| 00:32 | janitor-delete | Win11Builder | janitor delete OCW-worktree-agent-a3b9cf0b40cbf0ccc/target (4.8 GB) |
| 00:32 | janitor-delete | Win11Builder | janitor delete OCW-worktree-agent-a4e6bc385ccdf40f0/target (3.3 GB) |
| 00:32 | janitor-delete | Win11Builder | janitor delete OCW-worktree-agent-a507bcaff0a2af98c/target (6.2 GB) |
| 00:32 | janitor-delete | Win11Builder | janitor delete OCW-worktree-agent-a5378106956080801/target (1.8 GB) |
| 00:32 | janitor-delete | Win11Builder | janitor delete OCW-worktree-agent-a54266deef98aa31a/target (2.8 GB) |
| 00:32 | janitor-delete | Win11Builder | janitor delete OCW-worktree-agent-a8a0d2c6eeb4556d9/target (5.5 GB) |
| 00:32 | janitor-delete | Win11Builder | janitor delete OCW-worktree-agent-a99613c9983b557e5/target (2.0 GB) |
| 00:32 | janitor-delete | Win11Builder | janitor delete OCW-worktree-agent-ab886c17ece2bab7f/target (2.3 GB) |
| 00:32 | janitor-delete | Win11Builder | janitor delete OCW-worktree-agent-ac264ba6885768656/target (5.5 GB) |
| 00:32 | janitor-delete | Win11Builder | janitor delete OCW-worktree-agent-acafa3212c0c9925a/target (2.0 GB) |
| 00:32 | janitor-delete | Win11Builder | janitor delete OCW-worktree-agent-acf229e1ec2f3ec92/target (5.2 GB) |
| 00:32 | janitor-delete | Win11Builder | janitor delete OCW-worktree-agent-ad17650ac131c55d2/target (4.1 GB) |
| 00:33 | machine-offline | Weela | Weela unreachable (no route to host) |
| 00:34 | janitor-delete | Win11Builder | janitor delete OCW/target (39.8 GB) |
| 00:38 | machine-online | Weela | Weela back online |
| 02:40 | janitor-delete | marge | janitor delete OCW-worktree-agent-a64cacd30a467fa11/target (29.1 GB) |
| 02:59 | janitor-delete | marge | janitor delete OCW-release-0.2.3/target (13.7 GB) |
| 03:26 | janitor-delete | marge | janitor delete OCW-worktree-agent-a95d14905b4271774/target (36.7 GB) |
| 04:24 | janitor-delete | marge | janitor delete OCW-worktree-agent-ad1a26650524c097b/target (34.1 GB) |
| 04:58 | janitor-delete | marge | janitor delete OCW-worktree-agent-aa66d7f8e51beba78/target (30.3 GB) |
| 05:33 | janitor-delete | marge | janitor delete OCW-worktree-agent-a01e442248925aa9a/target (42.6 GB) |
| 06:06 | janitor-delete | marge | janitor delete OCW-worktree-agent-a01c5b7f390a5e38e/target (47.2 GB) |
| 06:53 | janitor-delete | marge | janitor delete OCW-worktree-agent-a57dfc7b2ec3683fd/target (62.8 GB) |
| 11:31 | disk-full | macos | disk home on macos at 90 % |
| 11:34 | janitor-delete | macos | janitor delete OCW/target (0.9 GB) |
| 11:44 | janitor-delete | macos | janitor delete OCW/target (2.6 GB) |
| 12:04 | janitor-delete | marge | janitor delete OCW-worktree-agent-a3a217ad67fa320ad/target (30.9 GB) |
| 12:48 | janitor-delete | marge | janitor delete OCW-worktree-agent-a367743c92249633c/target (42.2 GB) |
| 14:15 | janitor-delete | marge | janitor delete OCW-strava-pending/target (36.1 GB) |
| 15:20 | machine-offline | Weela | Weela unreachable (no route to host) |
| 15:22 | machine-online | leela | leela back online |
| 15:24 | machine-offline | leela | leela unreachable (no route to host) |
| 15:33 | machine-online | leela | leela back online |
| 15:37 | machine-offline | leela | leela unreachable (no route to host) |
| 16:19 | machine-offline | Win11Builder | Win11Builder unreachable (timeout) |
| 16:20 | machine-online | Win11Builder | Win11Builder back online |
| 18:39 | runs-failed | Win11Builder, macos, marge | 15 failed remote.sh runs (Win11Builder 7, macos 1, marge 7) |
| 19:02 | janitor-delete | marge | janitor delete OCW-worktree-agent-ac5f29b36c9ad1f2e/target (10.3 GB) |
| 19:51 | janitor-delete | macos | janitor delete OCW/target (0.2 GB) |
| 20:11 | janitor-delete | macos | janitor delete OCW/target (0.0 GB) |
| 21:03 | machine-offline | Win11Builder | Win11Builder unreachable (timeout) |
| 21:04 | machine-online | Win11Builder | Win11Builder back online |
| 21:11 | machine-online | leela | leela back online |
| 22:55 | janitor-delete | macos | janitor delete OCW-worktree-agent-a03e9957572339d7f/target (6.1 GB) |
| 23:05 | janitor-delete | macos | janitor delete OCW/target (0.1 GB) |
| 23:15 | janitor-delete | macos | janitor delete OCW/target (0.4 GB) |

## Media

| Time | File |
|---|---|
| 00:15:47 | [001547-scenes-navi-wayland-navi-li-free-day.jpg](001547-scenes-navi-wayland-navi-li-free-day.jpg) |
| 00:16:02 | [001602-scenes-navi-wayland-navi-li-route-night.jpg](001602-scenes-navi-wayland-navi-li-route-night.jpg) |
| 00:16:16 | [001616-scenes-navi-wayland-navi-li-route-day-720p.jpg](001616-scenes-navi-wayland-navi-li-route-day-720p.jpg) |
| 00:16:35 | [001635-scenes-navi-wayland-navi-bf-free-day.jpg](001635-scenes-navi-wayland-navi-bf-free-day.jpg) |
| 00:16:53 | [001653-scenes-navi-wayland-navi-bf-route-night.jpg](001653-scenes-navi-wayland-navi-bf-route-night.jpg) |
| 00:17:09 | [001709-scenes-navi-wayland-navi-tf-free-day.jpg](001709-scenes-navi-wayland-navi-tf-free-day.jpg) |
| 00:17:26 | [001726-scenes-navi-wayland-navi-tf-route-night.jpg](001726-scenes-navi-wayland-navi-tf-route-night.jpg) |
| 00:18:01 | [001801-shot-navi-li-free-day.jpg](001801-shot-navi-li-free-day.jpg) |
| 00:18:26 | [001826-shot-navi-li-route-night.jpg](001826-shot-navi-li-route-night.jpg) |
| 00:19:09 | [001909-shot-navi-bf-route-night.jpg](001909-shot-navi-bf-route-night.jpg) |
| 00:19:42 | [001942-shot-navi-tf-free-day.jpg](001942-shot-navi-tf-free-day.jpg) |
| 00:39:17 | [003917-shot-liechtenstein-meadow-road-rider-off-x11.jpg](003917-shot-liechtenstein-meadow-road-rider-off-x11.jpg) |
| 00:39:36 | [003936-shot-wayland-liechtenstein-meadow-road-rider-off-wayland.jpg](003936-shot-wayland-liechtenstein-meadow-road-rider-off-wayland.jpg) |
| 00:40:19 | [004019-shot-liechtenstein-meadow-road-rider-on-x11.jpg](004019-shot-liechtenstein-meadow-road-rider-on-x11.jpg) |
| 00:40:37 | [004037-shot-wayland-liechtenstein-meadow-road-rider-on-wayland.jpg](004037-shot-wayland-liechtenstein-meadow-road-rider-on-wayland.jpg) |
| 00:41:14 | [004114-shot-liechtenstein-meadow-road-orbit-off-x11.jpg](004114-shot-liechtenstein-meadow-road-orbit-off-x11.jpg) |
| 00:41:33 | [004133-shot-wayland-liechtenstein-meadow-road-orbit-off-wayland.jpg](004133-shot-wayland-liechtenstein-meadow-road-orbit-off-wayland.jpg) |
| 00:42:13 | [004213-shot-liechtenstein-meadow-road-orbit-on-x11.jpg](004213-shot-liechtenstein-meadow-road-orbit-on-x11.jpg) |
| 00:42:32 | [004232-shot-wayland-liechtenstein-meadow-road-orbit-on-wayland.jpg](004232-shot-wayland-liechtenstein-meadow-road-orbit-on-wayland.jpg) |
| 00:43:19 | [004319-shot-blackforest-autumn-rider-off-x11.jpg](004319-shot-blackforest-autumn-rider-off-x11.jpg) |
| 00:43:40 | [004340-shot-wayland-blackforest-autumn-rider-off-wayland.jpg](004340-shot-wayland-blackforest-autumn-rider-off-wayland.jpg) |
| 00:44:14 | [004414-shot-blackforest-autumn-rider-on-x11.jpg](004414-shot-blackforest-autumn-rider-on-x11.jpg) |
| 00:44:34 | [004434-shot-wayland-blackforest-autumn-rider-on-wayland.jpg](004434-shot-wayland-blackforest-autumn-rider-on-wayland.jpg) |
| 00:45:14 | [004514-shot-blackforest-autumn-orbit-off-x11.jpg](004514-shot-blackforest-autumn-orbit-off-x11.jpg) |
| 00:45:35 | [004535-shot-wayland-blackforest-autumn-orbit-off-wayland.jpg](004535-shot-wayland-blackforest-autumn-orbit-off-wayland.jpg) |
| 00:46:21 | [004621-shot-blackforest-autumn-orbit-on-x11.jpg](004621-shot-blackforest-autumn-orbit-on-x11.jpg) |
| 00:46:42 | [004642-shot-wayland-blackforest-autumn-orbit-on-wayland.jpg](004642-shot-wayland-blackforest-autumn-orbit-on-wayland.jpg) |
| 00:51:48 | [005148-road-damage-2026-11-18-after-damage-li-main-rider.jpg](005148-road-damage-2026-11-18-after-damage-li-main-rider.jpg) |
| 00:52:01 | [005201-road-damage-2026-11-18-after-damage-li-main-close.jpg](005201-road-damage-2026-11-18-after-damage-li-main-close.jpg) |
| 00:52:15 | [005215-road-damage-2026-11-18-after-damage-li-minor-rider.jpg](005215-road-damage-2026-11-18-after-damage-li-minor-rider.jpg) |
| 00:52:27 | [005227-road-damage-2026-11-18-after-damage-li-minor-close.jpg](005227-road-damage-2026-11-18-after-damage-li-minor-close.jpg) |
| 00:52:40 | [005240-road-damage-2026-11-18-after-damage-li-minor-wet-rider.jpg](005240-road-damage-2026-11-18-after-damage-li-minor-wet-rider.jpg) |
| 00:52:53 | [005253-road-damage-2026-11-18-after-damage-li-minor-wet-close.jpg](005253-road-damage-2026-11-18-after-damage-li-minor-wet-close.jpg) |
| 00:53:06 | [005306-road-damage-2026-11-18-after-damage-li-track-rider.jpg](005306-road-damage-2026-11-18-after-damage-li-track-rider.jpg) |
| 00:53:19 | [005319-road-damage-2026-11-18-after-damage-li-track-close.jpg](005319-road-damage-2026-11-18-after-damage-li-track-close.jpg) |
| 00:53:32 | [005332-road-damage-2026-11-18-after-damage-li-smooth-excellent-close.jpg](005332-road-damage-2026-11-18-after-damage-li-smooth-excellent-close.jpg) |
| 00:53:45 | [005345-road-damage-2026-11-18-after-damage-li-smooth-good-close.jpg](005345-road-damage-2026-11-18-after-damage-li-smooth-good-close.jpg) |
| 00:53:58 | [005358-road-damage-2026-11-18-after-damage-li-smooth-intermediate-close.jpg](005358-road-damage-2026-11-18-after-damage-li-smooth-intermediate-close.jpg) |
| 00:54:11 | [005411-road-damage-2026-11-18-after-damage-li-smooth-bad-close.jpg](005411-road-damage-2026-11-18-after-damage-li-smooth-bad-close.jpg) |
| 00:54:25 | [005425-road-damage-2026-11-18-after-damage-li-smooth-very-bad-close.jpg](005425-road-damage-2026-11-18-after-damage-li-smooth-very-bad-close.jpg) |
| 00:54:38 | [005438-road-damage-2026-11-18-after-damage-li-smooth-horrible-close.jpg](005438-road-damage-2026-11-18-after-damage-li-smooth-horrible-close.jpg) |
| 00:54:51 | [005451-road-damage-2026-11-18-after-damage-li-smooth-very-horrible-close.jpg](005451-road-damage-2026-11-18-after-damage-li-smooth-very-horrible-close.jpg) |
| 00:55:05 | [005505-road-damage-2026-11-18-after-damage-li-junction-rider.jpg](005505-road-damage-2026-11-18-after-damage-li-junction-rider.jpg) |
| 00:55:18 | [005518-road-damage-2026-11-18-after-damage-li-junction-close.jpg](005518-road-damage-2026-11-18-after-damage-li-junction-close.jpg) |
| 00:55:35 | [005535-road-damage-2026-11-18-after-damage-bf-main-rider.jpg](005535-road-damage-2026-11-18-after-damage-bf-main-rider.jpg) |
| 00:55:52 | [005552-road-damage-2026-11-18-after-damage-bf-main-close.jpg](005552-road-damage-2026-11-18-after-damage-bf-main-close.jpg) |
| 00:56:09 | [005609-road-damage-2026-11-18-after-damage-bf-minor-rider.jpg](005609-road-damage-2026-11-18-after-damage-bf-minor-rider.jpg) |
| 00:56:27 | [005627-road-damage-2026-11-18-after-damage-bf-minor-close.jpg](005627-road-damage-2026-11-18-after-damage-bf-minor-close.jpg) |
| 00:56:43 | [005643-road-damage-2026-11-18-after-damage-bf-minor-wet-rider.jpg](005643-road-damage-2026-11-18-after-damage-bf-minor-wet-rider.jpg) |
| 00:56:59 | [005659-road-damage-2026-11-18-after-damage-bf-minor-wet-close.jpg](005659-road-damage-2026-11-18-after-damage-bf-minor-wet-close.jpg) |
| 00:57:15 | [005715-road-damage-2026-11-18-after-damage-bf-track-rider.jpg](005715-road-damage-2026-11-18-after-damage-bf-track-rider.jpg) |
| 00:57:33 | [005733-road-damage-2026-11-18-after-damage-bf-track-close.jpg](005733-road-damage-2026-11-18-after-damage-bf-track-close.jpg) |
| 00:57:50 | [005750-road-damage-2026-11-18-after-damage-bf-smooth-excellent-close.jpg](005750-road-damage-2026-11-18-after-damage-bf-smooth-excellent-close.jpg) |
| 00:58:07 | [005807-road-damage-2026-11-18-after-damage-bf-smooth-good-close.jpg](005807-road-damage-2026-11-18-after-damage-bf-smooth-good-close.jpg) |
| 00:58:25 | [005825-road-damage-2026-11-18-after-damage-bf-smooth-intermediate-close.jpg](005825-road-damage-2026-11-18-after-damage-bf-smooth-intermediate-close.jpg) |
| 00:58:42 | [005842-road-damage-2026-11-18-after-damage-bf-smooth-bad-close.jpg](005842-road-damage-2026-11-18-after-damage-bf-smooth-bad-close.jpg) |
| 00:58:59 | [005859-road-damage-2026-11-18-after-damage-bf-smooth-very-bad-close.jpg](005859-road-damage-2026-11-18-after-damage-bf-smooth-very-bad-close.jpg) |
| 00:59:16 | [005916-road-damage-2026-11-18-after-damage-bf-smooth-horrible-close.jpg](005916-road-damage-2026-11-18-after-damage-bf-smooth-horrible-close.jpg) |
| 00:59:34 | [005934-road-damage-2026-11-18-after-damage-bf-smooth-very-horrible-close.jpg](005934-road-damage-2026-11-18-after-damage-bf-smooth-very-horrible-close.jpg) |
| 00:59:51 | [005951-road-damage-2026-11-18-after-damage-bf-smooth-impassable-close.jpg](005951-road-damage-2026-11-18-after-damage-bf-smooth-impassable-close.jpg) |
| 01:00:08 | [010008-road-damage-2026-11-18-after-damage-bf-junction-rider.jpg](010008-road-damage-2026-11-18-after-damage-bf-junction-rider.jpg) |
| 01:00:26 | [010026-road-damage-2026-11-18-after-damage-bf-junction-close.jpg](010026-road-damage-2026-11-18-after-damage-bf-junction-close.jpg) |
| 01:00:42 | [010042-road-damage-2026-11-18-after-damage-tf-main-rider.jpg](010042-road-damage-2026-11-18-after-damage-tf-main-rider.jpg) |
| 01:00:59 | [010059-road-damage-2026-11-18-after-damage-tf-main-close.jpg](010059-road-damage-2026-11-18-after-damage-tf-main-close.jpg) |
| 01:01:14 | [010114-road-damage-2026-11-18-after-damage-tf-minor-rider.jpg](010114-road-damage-2026-11-18-after-damage-tf-minor-rider.jpg) |
| 01:01:30 | [010130-road-damage-2026-11-18-after-damage-tf-minor-close.jpg](010130-road-damage-2026-11-18-after-damage-tf-minor-close.jpg) |
| 01:01:46 | [010146-road-damage-2026-11-18-after-damage-tf-minor-wet-rider.jpg](010146-road-damage-2026-11-18-after-damage-tf-minor-wet-rider.jpg) |
| 01:02:02 | [010202-road-damage-2026-11-18-after-damage-tf-minor-wet-close.jpg](010202-road-damage-2026-11-18-after-damage-tf-minor-wet-close.jpg) |
| 01:02:18 | [010218-road-damage-2026-11-18-after-damage-tf-track-rider.jpg](010218-road-damage-2026-11-18-after-damage-tf-track-rider.jpg) |
| 01:02:34 | [010234-road-damage-2026-11-18-after-damage-tf-track-close.jpg](010234-road-damage-2026-11-18-after-damage-tf-track-close.jpg) |
| 01:02:49 | [010249-road-damage-2026-11-18-after-damage-tf-smooth-excellent-close.jpg](010249-road-damage-2026-11-18-after-damage-tf-smooth-excellent-close.jpg) |
| 01:03:04 | [010304-road-damage-2026-11-18-after-damage-tf-smooth-good-close.jpg](010304-road-damage-2026-11-18-after-damage-tf-smooth-good-close.jpg) |
| 01:03:19 | [010319-road-damage-2026-11-18-after-damage-tf-smooth-intermediate-close.jpg](010319-road-damage-2026-11-18-after-damage-tf-smooth-intermediate-close.jpg) |
| 01:03:34 | [010334-road-damage-2026-11-18-after-damage-tf-smooth-bad-close.jpg](010334-road-damage-2026-11-18-after-damage-tf-smooth-bad-close.jpg) |
| 01:03:50 | [010350-road-damage-2026-11-18-after-damage-tf-smooth-very-bad-close.jpg](010350-road-damage-2026-11-18-after-damage-tf-smooth-very-bad-close.jpg) |
| 01:04:04 | [010404-models-e3-rider.jpg](010404-models-e3-rider.jpg) |
| 01:04:06 | [010406-road-damage-2026-11-18-after-damage-tf-smooth-horrible-close.jpg](010406-road-damage-2026-11-18-after-damage-tf-smooth-horrible-close.jpg) |
| 01:04:16 | [010416-models-e3-bike.jpg](010416-models-e3-bike.jpg) |
| 01:04:20 | [010420-road-damage-2026-11-18-after-damage-tf-smooth-very-horrible-close.jpg](010420-road-damage-2026-11-18-after-damage-tf-smooth-very-horrible-close.jpg) |
| 01:04:27 | [010427-models-e3-wireframe.jpg](010427-models-e3-wireframe.jpg) |
| 01:04:35 | [010435-road-damage-2026-11-18-after-damage-tf-smooth-impassable-close.jpg](010435-road-damage-2026-11-18-after-damage-tf-smooth-impassable-close.jpg) |
| 01:04:38 | [010438-models-e3-normals-highlight.jpg](010438-models-e3-normals-highlight.jpg) |
| 01:04:50 | [010450-models-e3-lod-auto-far.jpg](010450-models-e3-lod-auto-far.jpg) |
| 01:04:50 | [010450-road-damage-2026-11-18-after-damage-tf-junction-rider.jpg](010450-road-damage-2026-11-18-after-damage-tf-junction-rider.jpg) |
| 01:05:01 | [010501-models-e3-lod-near.jpg](010501-models-e3-lod-near.jpg) |
| 01:05:04 | [010504-road-damage-2026-11-18-after-damage-tf-junction-close.jpg](010504-road-damage-2026-11-18-after-damage-tf-junction-close.jpg) |
| 01:05:13 | [010513-models-e3-lod1-chosen.jpg](010513-models-e3-lod1-chosen.jpg) |
| 01:05:17 | [010517-road-damage-2026-11-18-before-damage-li-main-rider.jpg](010517-road-damage-2026-11-18-before-damage-li-main-rider.jpg) |
| 01:05:24 | [010524-models-e3-lod-tree-lod1.jpg](010524-models-e3-lod-tree-lod1.jpg) |
| 01:05:30 | [010530-road-damage-2026-11-18-before-damage-li-main-close.jpg](010530-road-damage-2026-11-18-before-damage-li-main-close.jpg) |
| 01:05:35 | [010535-models-e3-helmet-tryon-fat.jpg](010535-models-e3-helmet-tryon-fat.jpg) |
| 01:05:42 | [010542-road-damage-2026-11-18-before-damage-li-minor-rider.jpg](010542-road-damage-2026-11-18-before-damage-li-minor-rider.jpg) |
| 01:05:47 | [010547-models-e3-helmet-tryon-slim.jpg](010547-models-e3-helmet-tryon-slim.jpg) |
| 01:05:54 | [010554-road-damage-2026-11-18-before-damage-li-minor-close.jpg](010554-road-damage-2026-11-18-before-damage-li-minor-close.jpg) |
| 01:05:58 | [010558-models-e3-ride-drops.jpg](010558-models-e3-ride-drops.jpg) |
| 01:06:07 | [010607-road-damage-2026-11-18-before-damage-li-minor-wet-rider.jpg](010607-road-damage-2026-11-18-before-damage-li-minor-wet-rider.jpg) |
| 01:06:09 | [010609-models-e3-plant-scene-autumn.jpg](010609-models-e3-plant-scene-autumn.jpg) |
| 01:06:19 | [010619-road-damage-2026-11-18-before-damage-li-minor-wet-close.jpg](010619-road-damage-2026-11-18-before-damage-li-minor-wet-close.jpg) |
| 01:06:21 | [010621-models-e3-plant-scene-winter.jpg](010621-models-e3-plant-scene-winter.jpg) |
| 01:06:31 | [010631-road-damage-2026-11-18-before-damage-li-track-rider.jpg](010631-road-damage-2026-11-18-before-damage-li-track-rider.jpg) |
| 01:06:32 | [010632-models-e3-prop.jpg](010632-models-e3-prop.jpg) |
| 01:06:43 | [010643-road-damage-2026-11-18-before-damage-li-track-close.jpg](010643-road-damage-2026-11-18-before-damage-li-track-close.jpg) |
| 01:06:44 | [010644-models-e3-validator-panel.jpg](010644-models-e3-validator-panel.jpg) |
| 01:06:55 | [010655-models-e3-night.jpg](010655-models-e3-night.jpg) |
| 01:06:56 | [010656-road-damage-2026-11-18-before-damage-li-smooth-excellent-close.jpg](010656-road-damage-2026-11-18-before-damage-li-smooth-excellent-close.jpg) |
| 01:07:08 | [010708-road-damage-2026-11-18-before-damage-li-smooth-good-close.jpg](010708-road-damage-2026-11-18-before-damage-li-smooth-good-close.jpg) |
| 01:07:20 | [010720-road-damage-2026-11-18-before-damage-li-smooth-intermediate-close.jpg](010720-road-damage-2026-11-18-before-damage-li-smooth-intermediate-close.jpg) |
| 01:07:33 | [010733-road-damage-2026-11-18-before-damage-li-smooth-bad-close.jpg](010733-road-damage-2026-11-18-before-damage-li-smooth-bad-close.jpg) |
| 01:07:45 | [010745-road-damage-2026-11-18-before-damage-li-smooth-very-bad-close.jpg](010745-road-damage-2026-11-18-before-damage-li-smooth-very-bad-close.jpg) |
| 01:07:58 | [010758-road-damage-2026-11-18-before-damage-li-smooth-horrible-close.jpg](010758-road-damage-2026-11-18-before-damage-li-smooth-horrible-close.jpg) |
| 01:08:11 | [010811-road-damage-2026-11-18-before-damage-li-smooth-very-horrible-close.jpg](010811-road-damage-2026-11-18-before-damage-li-smooth-very-horrible-close.jpg) |
| 01:08:23 | [010823-road-damage-2026-11-18-before-damage-li-junction-rider.jpg](010823-road-damage-2026-11-18-before-damage-li-junction-rider.jpg) |
| 01:08:36 | [010836-road-damage-2026-11-18-before-damage-li-junction-close.jpg](010836-road-damage-2026-11-18-before-damage-li-junction-close.jpg) |
| 01:08:48 | [010848-scenes-navi-wayland-navi-li-free-day.jpg](010848-scenes-navi-wayland-navi-li-free-day.jpg) |
| 01:08:54 | [010854-road-damage-2026-11-18-before-damage-bf-main-rider.jpg](010854-road-damage-2026-11-18-before-damage-bf-main-rider.jpg) |
| 01:09:02 | [010902-scenes-navi-wayland-navi-li-route-night.jpg](010902-scenes-navi-wayland-navi-li-route-night.jpg) |
| 01:09:12 | [010912-road-damage-2026-11-18-before-damage-bf-main-close.jpg](010912-road-damage-2026-11-18-before-damage-bf-main-close.jpg) |
| 01:09:16 | [010916-scenes-navi-wayland-navi-li-route-day-720p.jpg](010916-scenes-navi-wayland-navi-li-route-day-720p.jpg) |
| 01:09:31 | [010931-road-damage-2026-11-18-before-damage-bf-minor-rider.jpg](010931-road-damage-2026-11-18-before-damage-bf-minor-rider.jpg) |
| 01:09:33 | [010933-scenes-navi-wayland-navi-bf-free-day.jpg](010933-scenes-navi-wayland-navi-bf-free-day.jpg) |
| 01:09:50 | [010950-road-damage-2026-11-18-before-damage-bf-minor-close.jpg](010950-road-damage-2026-11-18-before-damage-bf-minor-close.jpg) |
| 01:09:50 | [010950-scenes-navi-wayland-navi-bf-route-night.jpg](010950-scenes-navi-wayland-navi-bf-route-night.jpg) |
| 01:10:06 | [011006-scenes-navi-wayland-navi-tf-free-day.jpg](011006-scenes-navi-wayland-navi-tf-free-day.jpg) |
| 01:10:09 | [011009-road-damage-2026-11-18-before-damage-bf-minor-wet-rider.jpg](011009-road-damage-2026-11-18-before-damage-bf-minor-wet-rider.jpg) |
| 01:10:22 | [011022-scenes-navi-wayland-navi-tf-route-night.jpg](011022-scenes-navi-wayland-navi-tf-route-night.jpg) |
| 01:10:28 | [011028-road-damage-2026-11-18-before-damage-bf-minor-wet-close.jpg](011028-road-damage-2026-11-18-before-damage-bf-minor-wet-close.jpg) |
| 01:10:47 | [011047-road-damage-2026-11-18-before-damage-bf-track-rider.jpg](011047-road-damage-2026-11-18-before-damage-bf-track-rider.jpg) |
| 01:11:05 | [011105-scenes-navi-wayland-navi-fps-on.jpg](011105-scenes-navi-wayland-navi-fps-on.jpg) |
| 01:11:06 | [011106-road-damage-2026-11-18-before-damage-bf-track-close.jpg](011106-road-damage-2026-11-18-before-damage-bf-track-close.jpg) |
| 01:11:26 | [011126-road-damage-2026-11-18-before-damage-bf-smooth-excellent-close.jpg](011126-road-damage-2026-11-18-before-damage-bf-smooth-excellent-close.jpg) |
| 01:11:46 | [011146-road-damage-2026-11-18-before-damage-bf-smooth-good-close.jpg](011146-road-damage-2026-11-18-before-damage-bf-smooth-good-close.jpg) |
| 01:11:48 | [011148-scenes-navi-wayland-navi-fps-off.jpg](011148-scenes-navi-wayland-navi-fps-off.jpg) |
| 01:12:06 | [011206-road-damage-2026-11-18-before-damage-bf-smooth-intermediate-close.jpg](011206-road-damage-2026-11-18-before-damage-bf-smooth-intermediate-close.jpg) |
| 01:12:08 | [011208-scenes-navi-x11-navi-li-free-day.jpg](011208-scenes-navi-x11-navi-li-free-day.jpg) |
| 01:12:27 | [011227-road-damage-2026-11-18-before-damage-bf-smooth-bad-close.jpg](011227-road-damage-2026-11-18-before-damage-bf-smooth-bad-close.jpg) |
| 01:12:42 | [011242-scenes-navi-x11-navi-li-route-night.jpg](011242-scenes-navi-x11-navi-li-route-night.jpg) |
| 01:12:47 | [011247-road-damage-2026-11-18-before-damage-bf-smooth-very-bad-close.jpg](011247-road-damage-2026-11-18-before-damage-bf-smooth-very-bad-close.jpg) |
| 01:13:06 | [011306-road-damage-2026-11-18-before-damage-bf-smooth-horrible-close.jpg](011306-road-damage-2026-11-18-before-damage-bf-smooth-horrible-close.jpg) |
| 01:13:15 | [011315-scenes-navi-x11-navi-bf-route-night.jpg](011315-scenes-navi-x11-navi-bf-route-night.jpg) |
| 01:13:27 | [011327-road-damage-2026-11-18-before-damage-bf-smooth-very-horrible-close.jpg](011327-road-damage-2026-11-18-before-damage-bf-smooth-very-horrible-close.jpg) |
| 01:13:48 | [011348-road-damage-2026-11-18-before-damage-bf-smooth-impassable-close.jpg](011348-road-damage-2026-11-18-before-damage-bf-smooth-impassable-close.jpg) |
| 01:13:54 | [011354-scenes-navi-x11-navi-tf-free-day.jpg](011354-scenes-navi-x11-navi-tf-free-day.jpg) |
| 01:14:09 | [011409-road-damage-2026-11-18-before-damage-bf-junction-rider.jpg](011409-road-damage-2026-11-18-before-damage-bf-junction-rider.jpg) |
| 01:14:30 | [011430-road-damage-2026-11-18-before-damage-bf-junction-close.jpg](011430-road-damage-2026-11-18-before-damage-bf-junction-close.jpg) |
| 01:14:46 | [011446-road-damage-2026-11-18-before-damage-tf-main-rider.jpg](011446-road-damage-2026-11-18-before-damage-tf-main-rider.jpg) |
| 01:14:53 | [011453-scenes-navi-x11-navi-fps-on.jpg](011453-scenes-navi-x11-navi-fps-on.jpg) |
| 01:15:01 | [011501-road-damage-2026-11-18-before-damage-tf-main-close.jpg](011501-road-damage-2026-11-18-before-damage-tf-main-close.jpg) |
| 01:15:17 | [011517-road-damage-2026-11-18-before-damage-tf-minor-rider.jpg](011517-road-damage-2026-11-18-before-damage-tf-minor-rider.jpg) |
| 01:15:32 | [011532-road-damage-2026-11-18-before-damage-tf-minor-close.jpg](011532-road-damage-2026-11-18-before-damage-tf-minor-close.jpg) |
| 01:15:48 | [011548-road-damage-2026-11-18-before-damage-tf-minor-wet-rider.jpg](011548-road-damage-2026-11-18-before-damage-tf-minor-wet-rider.jpg) |
| 01:15:54 | [011554-scenes-navi-x11-navi-fps-off.jpg](011554-scenes-navi-x11-navi-fps-off.jpg) |
| 01:16:03 | [011603-road-damage-2026-11-18-before-damage-tf-minor-wet-close.jpg](011603-road-damage-2026-11-18-before-damage-tf-minor-wet-close.jpg) |
| 01:16:18 | [011618-road-damage-2026-11-18-before-damage-tf-track-rider.jpg](011618-road-damage-2026-11-18-before-damage-tf-track-rider.jpg) |
| 01:16:34 | [011634-road-damage-2026-11-18-before-damage-tf-track-close.jpg](011634-road-damage-2026-11-18-before-damage-tf-track-close.jpg) |
| 01:16:46 | [011646-release-0.2.3-windows-icon-ocw-desktop-128.png](011646-release-0.2.3-windows-icon-ocw-desktop-128.png) |
| 01:16:46 | [011646-release-0.2.3-windows-icon-ocw-desktop-16.png](011646-release-0.2.3-windows-icon-ocw-desktop-16.png) |
| 01:16:46 | [011646-release-0.2.3-windows-icon-ocw-desktop-24.png](011646-release-0.2.3-windows-icon-ocw-desktop-24.png) |
| 01:16:46 | [011646-release-0.2.3-windows-icon-ocw-desktop-256.png](011646-release-0.2.3-windows-icon-ocw-desktop-256.png) |
| 01:16:46 | [011646-release-0.2.3-windows-icon-ocw-desktop-32.png](011646-release-0.2.3-windows-icon-ocw-desktop-32.png) |
| 01:16:46 | [011646-release-0.2.3-windows-icon-ocw-desktop-48.png](011646-release-0.2.3-windows-icon-ocw-desktop-48.png) |
| 01:16:46 | [011646-release-0.2.3-windows-icon-ocw-desktop-64.png](011646-release-0.2.3-windows-icon-ocw-desktop-64.png) |
| 01:16:46 | [011646-release-0.2.3-windows-icon-ocw-studio-128.png](011646-release-0.2.3-windows-icon-ocw-studio-128.png) |
| 01:16:46 | [011646-release-0.2.3-windows-icon-ocw-studio-16.png](011646-release-0.2.3-windows-icon-ocw-studio-16.png) |
| 01:16:46 | [011646-release-0.2.3-windows-icon-ocw-studio-24.png](011646-release-0.2.3-windows-icon-ocw-studio-24.png) |
| 01:16:46 | [011646-release-0.2.3-windows-icon-ocw-studio-256.png](011646-release-0.2.3-windows-icon-ocw-studio-256.png) |
| 01:16:46 | [011646-release-0.2.3-windows-icon-ocw-studio-32.png](011646-release-0.2.3-windows-icon-ocw-studio-32.png) |
| 01:16:46 | [011646-release-0.2.3-windows-icon-ocw-studio-48.png](011646-release-0.2.3-windows-icon-ocw-studio-48.png) |
| 01:16:46 | [011646-release-0.2.3-windows-icon-ocw-studio-64.png](011646-release-0.2.3-windows-icon-ocw-studio-64.png) |
| 01:16:49 | [011649-road-damage-2026-11-18-before-damage-tf-smooth-excellent-close.jpg](011649-road-damage-2026-11-18-before-damage-tf-smooth-excellent-close.jpg) |
| 01:17:05 | [011705-road-damage-2026-11-18-before-damage-tf-smooth-good-close.jpg](011705-road-damage-2026-11-18-before-damage-tf-smooth-good-close.jpg) |
| 01:17:20 | [011720-road-damage-2026-11-18-before-damage-tf-smooth-intermediate-close.jpg](011720-road-damage-2026-11-18-before-damage-tf-smooth-intermediate-close.jpg) |
| 01:17:36 | [011736-road-damage-2026-11-18-before-damage-tf-smooth-bad-close.jpg](011736-road-damage-2026-11-18-before-damage-tf-smooth-bad-close.jpg) |
| 01:17:52 | [011752-road-damage-2026-11-18-before-damage-tf-smooth-very-bad-close.jpg](011752-road-damage-2026-11-18-before-damage-tf-smooth-very-bad-close.jpg) |
| 01:18:07 | [011807-road-damage-2026-11-18-before-damage-tf-smooth-horrible-close.jpg](011807-road-damage-2026-11-18-before-damage-tf-smooth-horrible-close.jpg) |
| 01:18:23 | [011823-road-damage-2026-11-18-before-damage-tf-smooth-very-horrible-close.jpg](011823-road-damage-2026-11-18-before-damage-tf-smooth-very-horrible-close.jpg) |
| 01:18:39 | [011839-road-damage-2026-11-18-before-damage-tf-smooth-impassable-close.jpg](011839-road-damage-2026-11-18-before-damage-tf-smooth-impassable-close.jpg) |
| 01:18:54 | [011854-road-damage-2026-11-18-before-damage-tf-junction-rider.jpg](011854-road-damage-2026-11-18-before-damage-tf-junction-rider.jpg) |
| 01:19:10 | [011910-road-damage-2026-11-18-before-damage-tf-junction-close.jpg](011910-road-damage-2026-11-18-before-damage-tf-junction-close.jpg) |
| 01:19:32 | [011932-road-damage-2026-11-18-after-x11-damage-li-minor-rider.jpg](011932-road-damage-2026-11-18-after-x11-damage-li-minor-rider.jpg) |
| 01:20:02 | [012002-road-damage-2026-11-18-after-x11-damage-li-minor-close.jpg](012002-road-damage-2026-11-18-after-x11-damage-li-minor-close.jpg) |
| 01:20:28 | [012028-road-damage-2026-11-18-after-x11-damage-li-minor-wet-rider.jpg](012028-road-damage-2026-11-18-after-x11-damage-li-minor-wet-rider.jpg) |
| 01:20:51 | [012051-road-damage-2026-11-18-after-x11-damage-li-minor-wet-close.jpg](012051-road-damage-2026-11-18-after-x11-damage-li-minor-wet-close.jpg) |
| 01:21:16 | [012116-road-damage-2026-11-18-before-x11-damage-li-minor-rider.jpg](012116-road-damage-2026-11-18-before-x11-damage-li-minor-rider.jpg) |
| 01:21:42 | [012142-road-damage-2026-11-18-before-x11-damage-li-minor-close.jpg](012142-road-damage-2026-11-18-before-x11-damage-li-minor-close.jpg) |
| 01:22:03 | [012203-road-damage-2026-11-18-before-x11-damage-li-minor-wet-rider.jpg](012203-road-damage-2026-11-18-before-x11-damage-li-minor-wet-rider.jpg) |
| 01:22:24 | [012224-road-damage-2026-11-18-before-x11-damage-li-minor-wet-close.jpg](012224-road-damage-2026-11-18-before-x11-damage-li-minor-wet-close.jpg) |
| 01:37:49 | [013749-web-navi-li-day-webgpu-web-world-first-loading.jpg](013749-web-navi-li-day-webgpu-web-world-first-loading.jpg) |
| 01:37:49 | [013749-web-navi-li-day-webgpu-web-world-teleport.jpg](013749-web-navi-li-day-webgpu-web-world-teleport.jpg) |
| 01:37:49 | [013749-web-navi-li-day-webgpu-web-world.jpg](013749-web-navi-li-day-webgpu-web-world.jpg) |
| 01:38:33 | [013833-web-navi-li-night-webgpu-web-world-first-loading.jpg](013833-web-navi-li-night-webgpu-web-world-first-loading.jpg) |
| 01:38:33 | [013833-web-navi-li-night-webgpu-web-world-teleport.jpg](013833-web-navi-li-night-webgpu-web-world-teleport.jpg) |
| 01:38:33 | [013833-web-navi-li-night-webgpu-web-world.jpg](013833-web-navi-li-night-webgpu-web-world.jpg) |
| 01:39:17 | [013917-web-navi-li-day-webgl2-web-world-webgl2-first-loading.jpg](013917-web-navi-li-day-webgl2-web-world-webgl2-first-loading.jpg) |
| 01:39:17 | [013917-web-navi-li-day-webgl2-web-world-webgl2-teleport.jpg](013917-web-navi-li-day-webgl2-web-world-webgl2-teleport.jpg) |
| 01:39:17 | [013917-web-navi-li-day-webgl2-web-world-webgl2.jpg](013917-web-navi-li-day-webgl2-web-world-webgl2.jpg) |
| 01:40:01 | [014001-web-navi-li-night-webgl2-web-world-webgl2-first-loading.jpg](014001-web-navi-li-night-webgl2-web-world-webgl2-first-loading.jpg) |
| 01:40:01 | [014001-web-navi-li-night-webgl2-web-world-webgl2-teleport.jpg](014001-web-navi-li-night-webgl2-web-world-webgl2-teleport.jpg) |
| 01:40:01 | [014001-web-navi-li-night-webgl2-web-world-webgl2.jpg](014001-web-navi-li-night-webgl2-web-world-webgl2.jpg) |
| 01:46:55 | [014655-places-liechtenstein-1-whole.jpg](014655-places-liechtenstein-1-whole.jpg) |
| 01:47:36 | [014736-shot-ocw.jpg](014736-shot-ocw.jpg) |
| 01:47:45 | [014745-shot-wayland-ocw-wayland.jpg](014745-shot-wayland-ocw-wayland.jpg) |
| 01:51:41 | [015141-places-liechtenstein-2-vaduz-12m.jpg](015141-places-liechtenstein-2-vaduz-12m.jpg) |
| 01:53:48 | [015348-web-web-calendar-select.jpg](015348-web-web-calendar-select.jpg) |
| 01:53:48 | [015348-web-web-calendar.jpg](015348-web-web-calendar.jpg) |
| 01:53:48 | [015348-web-web-console.jpg](015348-web-web-console.jpg) |
| 01:53:48 | [015348-web-web-downloads-ocw-2026-11-18-01-55-05.jpg](015348-web-web-downloads-ocw-2026-11-18-01-55-05.jpg) |
| 01:53:48 | [015348-web-web-downloads-ocw-2026-11-18-01-55-08.webm](015348-web-web-downloads-ocw-2026-11-18-01-55-08.webm) |
| 01:53:48 | [015348-web-web-gamepad.jpg](015348-web-web-gamepad.jpg) |
| 01:53:48 | [015348-web-web-gps.jpg](015348-web-web-gps.jpg) |
| 01:53:48 | [015348-web-web-hud.jpg](015348-web-web-hud.jpg) |
| 01:53:48 | [015348-web-web-join.jpg](015348-web-web-join.jpg) |
| 01:53:48 | [015348-web-web-menu.jpg](015348-web-web-menu.jpg) |
| 01:53:48 | [015348-web-web-ride.jpg](015348-web-web-ride.jpg) |
| 01:53:48 | [015348-web-web-riders.jpg](015348-web-web-riders.jpg) |
| 01:53:48 | [015348-web-web-settings.jpg](015348-web-web-settings.jpg) |
| 01:53:48 | [015348-web-web-touch-hints.jpg](015348-web-web-touch-hints.jpg) |
| 01:53:48 | [015348-web-web-touch-hold.jpg](015348-web-web-touch-hold.jpg) |
| 01:53:48 | [015348-web-web-unicorn-flight.jpg](015348-web-web-unicorn-flight.jpg) |
| 01:53:48 | [015348-web-web-unicorn-inspect.jpg](015348-web-web-unicorn-inspect.jpg) |
| 01:53:48 | [015348-web-web-unicorn-menu.jpg](015348-web-web-unicorn-menu.jpg) |
| 01:53:48 | [015348-web-web-weather.jpg](015348-web-web-weather.jpg) |
| 01:53:48 | [015348-web-web.jpg](015348-web-web.jpg) |
| 01:55:31 | [015531-places-liechtenstein-3-vaduz-3m.jpg](015531-places-liechtenstein-3-vaduz-3m.jpg) |
| 01:56:37 | [015637-places-tenerife-1-whole.jpg](015637-places-tenerife-1-whole.jpg) |
| 01:57:44 | [015744-places-tenerife-2-north-east-35m.jpg](015744-places-tenerife-2-north-east-35m.jpg) |
| 01:58:50 | [015850-places-tenerife-3-puerto-6m.jpg](015850-places-tenerife-3-puerto-6m.jpg) |
| 01:59:28 | [015928-road-damage-2026-11-18-compare-damage-bf-junction-close.jpg](015928-road-damage-2026-11-18-compare-damage-bf-junction-close.jpg) |
| 01:59:29 | [015929-road-damage-2026-11-18-compare-damage-bf-junction-rider.jpg](015929-road-damage-2026-11-18-compare-damage-bf-junction-rider.jpg) |
| 01:59:29 | [015929-road-damage-2026-11-18-compare-damage-bf-main-close.jpg](015929-road-damage-2026-11-18-compare-damage-bf-main-close.jpg) |
| 01:59:29 | [015929-road-damage-2026-11-18-compare-damage-bf-main-rider.jpg](015929-road-damage-2026-11-18-compare-damage-bf-main-rider.jpg) |
| 01:59:29 | [015929-road-damage-2026-11-18-compare-damage-bf-minor-close.jpg](015929-road-damage-2026-11-18-compare-damage-bf-minor-close.jpg) |
| 01:59:29 | [015929-road-damage-2026-11-18-compare-damage-bf-minor-rider.jpg](015929-road-damage-2026-11-18-compare-damage-bf-minor-rider.jpg) |
| 01:59:29 | [015929-road-damage-2026-11-18-compare-damage-bf-minor-wet-close.jpg](015929-road-damage-2026-11-18-compare-damage-bf-minor-wet-close.jpg) |
| 01:59:29 | [015929-road-damage-2026-11-18-compare-damage-bf-minor-wet-rider.jpg](015929-road-damage-2026-11-18-compare-damage-bf-minor-wet-rider.jpg) |
| 01:59:29 | [015929-road-damage-2026-11-18-compare-damage-bf-smooth-bad-close.jpg](015929-road-damage-2026-11-18-compare-damage-bf-smooth-bad-close.jpg) |
| 01:59:30 | [015930-road-damage-2026-11-18-compare-damage-bf-smooth-excellent-close.jpg](015930-road-damage-2026-11-18-compare-damage-bf-smooth-excellent-close.jpg) |
| 01:59:30 | [015930-road-damage-2026-11-18-compare-damage-bf-smooth-good-close.jpg](015930-road-damage-2026-11-18-compare-damage-bf-smooth-good-close.jpg) |
| 01:59:30 | [015930-road-damage-2026-11-18-compare-damage-bf-smooth-horrible-close.jpg](015930-road-damage-2026-11-18-compare-damage-bf-smooth-horrible-close.jpg) |
| 01:59:30 | [015930-road-damage-2026-11-18-compare-damage-bf-smooth-impassable-close.jpg](015930-road-damage-2026-11-18-compare-damage-bf-smooth-impassable-close.jpg) |
| 01:59:30 | [015930-road-damage-2026-11-18-compare-damage-bf-smooth-intermediate-close.jpg](015930-road-damage-2026-11-18-compare-damage-bf-smooth-intermediate-close.jpg) |
| 01:59:30 | [015930-road-damage-2026-11-18-compare-damage-bf-smooth-very-bad-close.jpg](015930-road-damage-2026-11-18-compare-damage-bf-smooth-very-bad-close.jpg) |
| 01:59:30 | [015930-road-damage-2026-11-18-compare-damage-bf-smooth-very-horrible-close.jpg](015930-road-damage-2026-11-18-compare-damage-bf-smooth-very-horrible-close.jpg) |
| 01:59:30 | [015930-road-damage-2026-11-18-compare-damage-bf-track-close.jpg](015930-road-damage-2026-11-18-compare-damage-bf-track-close.jpg) |
| 01:59:31 | [015931-road-damage-2026-11-18-compare-damage-bf-track-rider.jpg](015931-road-damage-2026-11-18-compare-damage-bf-track-rider.jpg) |
| 01:59:31 | [015931-road-damage-2026-11-18-compare-damage-li-junction-close.jpg](015931-road-damage-2026-11-18-compare-damage-li-junction-close.jpg) |
| 01:59:31 | [015931-road-damage-2026-11-18-compare-damage-li-junction-rider.jpg](015931-road-damage-2026-11-18-compare-damage-li-junction-rider.jpg) |
| 01:59:31 | [015931-road-damage-2026-11-18-compare-damage-li-main-close.jpg](015931-road-damage-2026-11-18-compare-damage-li-main-close.jpg) |
| 01:59:31 | [015931-road-damage-2026-11-18-compare-damage-li-main-rider.jpg](015931-road-damage-2026-11-18-compare-damage-li-main-rider.jpg) |
| 01:59:31 | [015931-road-damage-2026-11-18-compare-damage-li-minor-close.jpg](015931-road-damage-2026-11-18-compare-damage-li-minor-close.jpg) |
| 01:59:31 | [015931-road-damage-2026-11-18-compare-damage-li-minor-rider.jpg](015931-road-damage-2026-11-18-compare-damage-li-minor-rider.jpg) |
| 01:59:31 | [015931-road-damage-2026-11-18-compare-damage-li-minor-wet-close.jpg](015931-road-damage-2026-11-18-compare-damage-li-minor-wet-close.jpg) |
| 01:59:32 | [015932-road-damage-2026-11-18-compare-damage-li-minor-wet-rider.jpg](015932-road-damage-2026-11-18-compare-damage-li-minor-wet-rider.jpg) |
| 01:59:32 | [015932-road-damage-2026-11-18-compare-damage-li-smooth-bad-close.jpg](015932-road-damage-2026-11-18-compare-damage-li-smooth-bad-close.jpg) |
| 01:59:32 | [015932-road-damage-2026-11-18-compare-damage-li-smooth-excellent-close.jpg](015932-road-damage-2026-11-18-compare-damage-li-smooth-excellent-close.jpg) |
| 01:59:32 | [015932-road-damage-2026-11-18-compare-damage-li-smooth-good-close.jpg](015932-road-damage-2026-11-18-compare-damage-li-smooth-good-close.jpg) |
| 01:59:32 | [015932-road-damage-2026-11-18-compare-damage-li-smooth-horrible-close.jpg](015932-road-damage-2026-11-18-compare-damage-li-smooth-horrible-close.jpg) |
| 01:59:32 | [015932-road-damage-2026-11-18-compare-damage-li-smooth-intermediate-close.jpg](015932-road-damage-2026-11-18-compare-damage-li-smooth-intermediate-close.jpg) |
| 01:59:32 | [015932-road-damage-2026-11-18-compare-damage-li-smooth-very-bad-close.jpg](015932-road-damage-2026-11-18-compare-damage-li-smooth-very-bad-close.jpg) |
| 01:59:33 | [015933-road-damage-2026-11-18-compare-damage-li-smooth-very-horrible-close.jpg](015933-road-damage-2026-11-18-compare-damage-li-smooth-very-horrible-close.jpg) |
| 01:59:33 | [015933-road-damage-2026-11-18-compare-damage-li-track-close.jpg](015933-road-damage-2026-11-18-compare-damage-li-track-close.jpg) |
| 01:59:33 | [015933-road-damage-2026-11-18-compare-damage-li-track-rider.jpg](015933-road-damage-2026-11-18-compare-damage-li-track-rider.jpg) |
| 01:59:33 | [015933-road-damage-2026-11-18-compare-damage-tf-junction-close.jpg](015933-road-damage-2026-11-18-compare-damage-tf-junction-close.jpg) |
| 01:59:33 | [015933-road-damage-2026-11-18-compare-damage-tf-junction-rider.jpg](015933-road-damage-2026-11-18-compare-damage-tf-junction-rider.jpg) |
| 01:59:33 | [015933-road-damage-2026-11-18-compare-damage-tf-main-close.jpg](015933-road-damage-2026-11-18-compare-damage-tf-main-close.jpg) |
| 01:59:33 | [015933-road-damage-2026-11-18-compare-damage-tf-main-rider.jpg](015933-road-damage-2026-11-18-compare-damage-tf-main-rider.jpg) |
| 01:59:33 | [015933-road-damage-2026-11-18-compare-damage-tf-minor-close.jpg](015933-road-damage-2026-11-18-compare-damage-tf-minor-close.jpg) |
| 01:59:34 | [015934-road-damage-2026-11-18-compare-damage-tf-minor-rider.jpg](015934-road-damage-2026-11-18-compare-damage-tf-minor-rider.jpg) |
| 01:59:34 | [015934-road-damage-2026-11-18-compare-damage-tf-minor-wet-close.jpg](015934-road-damage-2026-11-18-compare-damage-tf-minor-wet-close.jpg) |
| 01:59:34 | [015934-road-damage-2026-11-18-compare-damage-tf-minor-wet-rider.jpg](015934-road-damage-2026-11-18-compare-damage-tf-minor-wet-rider.jpg) |
| 01:59:34 | [015934-road-damage-2026-11-18-compare-damage-tf-smooth-bad-close.jpg](015934-road-damage-2026-11-18-compare-damage-tf-smooth-bad-close.jpg) |
| 01:59:34 | [015934-road-damage-2026-11-18-compare-damage-tf-smooth-excellent-close.jpg](015934-road-damage-2026-11-18-compare-damage-tf-smooth-excellent-close.jpg) |
| 01:59:34 | [015934-road-damage-2026-11-18-compare-damage-tf-smooth-good-close.jpg](015934-road-damage-2026-11-18-compare-damage-tf-smooth-good-close.jpg) |
| 01:59:34 | [015934-road-damage-2026-11-18-compare-damage-tf-smooth-horrible-close.jpg](015934-road-damage-2026-11-18-compare-damage-tf-smooth-horrible-close.jpg) |
| 01:59:34 | [015934-road-damage-2026-11-18-compare-damage-tf-smooth-impassable-close.jpg](015934-road-damage-2026-11-18-compare-damage-tf-smooth-impassable-close.jpg) |
| 01:59:35 | [015935-road-damage-2026-11-18-compare-damage-tf-smooth-intermediate-close.jpg](015935-road-damage-2026-11-18-compare-damage-tf-smooth-intermediate-close.jpg) |
| 01:59:35 | [015935-road-damage-2026-11-18-compare-damage-tf-smooth-very-bad-close.jpg](015935-road-damage-2026-11-18-compare-damage-tf-smooth-very-bad-close.jpg) |
| 01:59:35 | [015935-road-damage-2026-11-18-compare-damage-tf-smooth-very-horrible-close.jpg](015935-road-damage-2026-11-18-compare-damage-tf-smooth-very-horrible-close.jpg) |
| 01:59:35 | [015935-road-damage-2026-11-18-compare-damage-tf-track-close.jpg](015935-road-damage-2026-11-18-compare-damage-tf-track-close.jpg) |
| 01:59:35 | [015935-road-damage-2026-11-18-compare-damage-tf-track-rider.jpg](015935-road-damage-2026-11-18-compare-damage-tf-track-rider.jpg) |
| 02:09:09 | [020909-photo-preview-photos-wayland-OCW-2026-11-18-02-09-09.jpg](020909-photo-preview-photos-wayland-OCW-2026-11-18-02-09-09.jpg) |
| 02:09:11 | [020911-photo-preview-photos-wayland-OCW-2026-11-18-02-09-11.jpg](020911-photo-preview-photos-wayland-OCW-2026-11-18-02-09-11.jpg) |
| 02:09:12 | [020912-photo-preview-screenshot-preview-wayland.jpg](020912-photo-preview-screenshot-preview-wayland.jpg) |
| 02:09:43 | [020943-photo-preview-screenshot-preview-off-x11.jpg](020943-photo-preview-screenshot-preview-off-x11.jpg) |
| 02:10:43 | [021043-photo-preview-photos-video-OCW-2026-11-18-02-09-51.jpg](021043-photo-preview-photos-video-OCW-2026-11-18-02-09-51.jpg) |
| 02:12:02 | [021202-photo-preview-screenshot-preview-x11.jpg](021202-photo-preview-screenshot-preview-x11.jpg) |
| 02:12:07 | [021207-photo-preview-screenshot-preview-x11.mp4](021207-photo-preview-screenshot-preview-x11.mp4) |
| 02:12:44 | [021244-photo-preview-photographer-chase-chase-01-preview.jpg](021244-photo-preview-photographer-chase-chase-01-preview.jpg) |
| 02:14:49 | [021449-photo-preview-photographer-chase-chase-02-photographer.jpg](021449-photo-preview-photographer-chase-chase-02-photographer.jpg) |
| 02:14:52 | [021452-photo-preview-photographer-chase-chase-03-photographer.jpg](021452-photo-preview-photographer-chase-chase-03-photographer.jpg) |
| 02:14:55 | [021455-photo-preview-photographer-chase-chase-04-preview.jpg](021455-photo-preview-photographer-chase-chase-04-preview.jpg) |
| 02:16:57 | [021657-photo-preview-photographer-end.jpg](021657-photo-preview-photographer-end.jpg) |
| 02:16:58 | [021658-photo-preview-photographer-photos-OCW-2026-11-18-01-12-37-photo-1.jpg](021658-photo-preview-photographer-photos-OCW-2026-11-18-01-12-37-photo-1.jpg) |
| 02:16:58 | [021658-photo-preview-photographer-photos-OCW-2026-11-18-01-12-37-photo-2.jpg](021658-photo-preview-photographer-photos-OCW-2026-11-18-01-12-37-photo-2.jpg) |
| 02:20:05 | [022005-road-damage-2026-11-18-levels-level-bf-minor-off-top.jpg](022005-road-damage-2026-11-18-levels-level-bf-minor-off-top.jpg) |
| 02:20:22 | [022022-road-damage-2026-11-18-levels-level-bf-minor-excellent-top.jpg](022022-road-damage-2026-11-18-levels-level-bf-minor-excellent-top.jpg) |
| 02:20:40 | [022040-road-damage-2026-11-18-levels-level-bf-minor-good-top.jpg](022040-road-damage-2026-11-18-levels-level-bf-minor-good-top.jpg) |
| 02:20:57 | [022057-road-damage-2026-11-18-levels-level-bf-minor-good-rider.jpg](022057-road-damage-2026-11-18-levels-level-bf-minor-good-rider.jpg) |
| 02:21:15 | [022115-road-damage-2026-11-18-levels-level-bf-minor-intermediate-top.jpg](022115-road-damage-2026-11-18-levels-level-bf-minor-intermediate-top.jpg) |
| 02:21:32 | [022132-road-damage-2026-11-18-levels-level-bf-minor-intermediate-rider.jpg](022132-road-damage-2026-11-18-levels-level-bf-minor-intermediate-rider.jpg) |
| 02:21:50 | [022150-road-damage-2026-11-18-levels-level-bf-minor-bad-top.jpg](022150-road-damage-2026-11-18-levels-level-bf-minor-bad-top.jpg) |
| 02:22:07 | [022207-road-damage-2026-11-18-levels-level-bf-minor-bad-rider.jpg](022207-road-damage-2026-11-18-levels-level-bf-minor-bad-rider.jpg) |
| 02:22:20 | [022220-release-0.2.3-linux-tar-x11.jpg](022220-release-0.2.3-linux-tar-x11.jpg) |
| 02:22:24 | [022224-road-damage-2026-11-18-levels-level-bf-minor-very-bad-top.jpg](022224-road-damage-2026-11-18-levels-level-bf-minor-very-bad-top.jpg) |
| 02:22:33 | [022233-release-0.2.3-linux-tar-wayland.jpg](022233-release-0.2.3-linux-tar-wayland.jpg) |
| 02:22:40 | [022240-road-damage-2026-11-18-levels-level-bf-minor-very-bad-rider.jpg](022240-road-damage-2026-11-18-levels-level-bf-minor-very-bad-rider.jpg) |
| 02:22:47 | [022247-release-0.2.3-linux-studio-wayland.jpg](022247-release-0.2.3-linux-studio-wayland.jpg) |
| 02:22:56 | [022256-road-damage-2026-11-18-levels-level-bf-minor-horrible-top.jpg](022256-road-damage-2026-11-18-levels-level-bf-minor-horrible-top.jpg) |
| 02:23:11 | [022311-road-damage-2026-11-18-levels-level-bf-minor-horrible-rider.jpg](022311-road-damage-2026-11-18-levels-level-bf-minor-horrible-rider.jpg) |
| 02:23:25 | [022325-release-0.2.3-linux-appimage-x11.jpg](022325-release-0.2.3-linux-appimage-x11.jpg) |
| 02:23:28 | [022328-road-damage-2026-11-18-levels-level-bf-minor-bad-wet.jpg](022328-road-damage-2026-11-18-levels-level-bf-minor-bad-wet.jpg) |
| 02:23:45 | [022345-road-damage-2026-11-18-levels-level-bf-minor-horrible-wet.jpg](022345-road-damage-2026-11-18-levels-level-bf-minor-horrible-wet.jpg) |
| 02:23:50 | [022350-release-0.2.3-linux-appimage-wayland.jpg](022350-release-0.2.3-linux-appimage-wayland.jpg) |
| 02:23:58 | [022358-road-damage-2026-11-18-levels-level-li-minor-off-top.jpg](022358-road-damage-2026-11-18-levels-level-li-minor-off-top.jpg) |
| 02:24:10 | [022410-road-damage-2026-11-18-levels-level-li-minor-excellent-top.jpg](022410-road-damage-2026-11-18-levels-level-li-minor-excellent-top.jpg) |
| 02:24:23 | [022423-road-damage-2026-11-18-levels-level-li-minor-good-top.jpg](022423-road-damage-2026-11-18-levels-level-li-minor-good-top.jpg) |
| 02:24:35 | [022435-road-damage-2026-11-18-levels-level-li-minor-good-rider.jpg](022435-road-damage-2026-11-18-levels-level-li-minor-good-rider.jpg) |
| 02:24:48 | [022448-road-damage-2026-11-18-levels-level-li-minor-intermediate-top.jpg](022448-road-damage-2026-11-18-levels-level-li-minor-intermediate-top.jpg) |
| 02:25:02 | [022502-road-damage-2026-11-18-levels-level-li-minor-intermediate-rider.jpg](022502-road-damage-2026-11-18-levels-level-li-minor-intermediate-rider.jpg) |
| 02:25:15 | [022515-road-damage-2026-11-18-levels-level-li-minor-bad-top.jpg](022515-road-damage-2026-11-18-levels-level-li-minor-bad-top.jpg) |
| 02:25:28 | [022528-road-damage-2026-11-18-levels-level-li-minor-bad-rider.jpg](022528-road-damage-2026-11-18-levels-level-li-minor-bad-rider.jpg) |
| 02:25:42 | [022542-road-damage-2026-11-18-levels-level-li-minor-very-bad-top.jpg](022542-road-damage-2026-11-18-levels-level-li-minor-very-bad-top.jpg) |
| 02:25:55 | [022555-road-damage-2026-11-18-levels-level-li-minor-very-bad-rider.jpg](022555-road-damage-2026-11-18-levels-level-li-minor-very-bad-rider.jpg) |
| 02:26:09 | [022609-road-damage-2026-11-18-levels-level-li-minor-horrible-top.jpg](022609-road-damage-2026-11-18-levels-level-li-minor-horrible-top.jpg) |
| 02:26:22 | [022622-road-damage-2026-11-18-levels-level-li-minor-horrible-rider.jpg](022622-road-damage-2026-11-18-levels-level-li-minor-horrible-rider.jpg) |
| 02:26:35 | [022635-road-damage-2026-11-18-levels-level-li-minor-bad-wet.jpg](022635-road-damage-2026-11-18-levels-level-li-minor-bad-wet.jpg) |
| 02:26:49 | [022649-road-damage-2026-11-18-levels-level-li-minor-horrible-wet.jpg](022649-road-damage-2026-11-18-levels-level-li-minor-horrible-wet.jpg) |
| 02:27:05 | [022705-road-damage-2026-11-18-levels-level-tf-minor-bad-top.jpg](022705-road-damage-2026-11-18-levels-level-tf-minor-bad-top.jpg) |
| 02:27:21 | [022721-road-damage-2026-11-18-levels-level-tf-minor-bad-rider.jpg](022721-road-damage-2026-11-18-levels-level-tf-minor-bad-rider.jpg) |
| 02:27:37 | [022737-road-damage-2026-11-18-levels-level-tf-minor-horrible-top.jpg](022737-road-damage-2026-11-18-levels-level-tf-minor-horrible-top.jpg) |
| 02:27:53 | [022753-road-damage-2026-11-18-levels-level-tf-minor-horrible-rider.jpg](022753-road-damage-2026-11-18-levels-level-tf-minor-horrible-rider.jpg) |
| 02:28:09 | [022809-road-damage-2026-11-18-levels-level-tf-minor-bad-wet.jpg](022809-road-damage-2026-11-18-levels-level-tf-minor-bad-wet.jpg) |
| 02:28:25 | [022825-road-damage-2026-11-18-levels-level-tf-minor-horrible-wet.jpg](022825-road-damage-2026-11-18-levels-level-tf-minor-horrible-wet.jpg) |
| 02:28:39 | [022839-road-damage-2026-11-18-levels-level-li-main-bad-top.jpg](022839-road-damage-2026-11-18-levels-level-li-main-bad-top.jpg) |
| 02:28:52 | [022852-road-damage-2026-11-18-levels-level-li-main-bad-rider.jpg](022852-road-damage-2026-11-18-levels-level-li-main-bad-rider.jpg) |
| 02:29:06 | [022906-road-damage-2026-11-18-levels-level-li-main-horrible-top.jpg](022906-road-damage-2026-11-18-levels-level-li-main-horrible-top.jpg) |
| 02:29:19 | [022919-road-damage-2026-11-18-levels-level-li-main-horrible-rider.jpg](022919-road-damage-2026-11-18-levels-level-li-main-horrible-rider.jpg) |
| 02:29:33 | [022933-road-damage-2026-11-18-levels-level-li-main-bad-wet.jpg](022933-road-damage-2026-11-18-levels-level-li-main-bad-wet.jpg) |
| 02:29:46 | [022946-road-damage-2026-11-18-levels-level-li-main-horrible-wet.jpg](022946-road-damage-2026-11-18-levels-level-li-main-horrible-wet.jpg) |
| 02:29:59 | [022959-road-damage-2026-11-18-levels-level-li-track-bad-top.jpg](022959-road-damage-2026-11-18-levels-level-li-track-bad-top.jpg) |
| 02:30:12 | [023012-road-damage-2026-11-18-levels-level-li-track-bad-rider.jpg](023012-road-damage-2026-11-18-levels-level-li-track-bad-rider.jpg) |
| 02:30:26 | [023026-road-damage-2026-11-18-levels-level-li-track-horrible-top.jpg](023026-road-damage-2026-11-18-levels-level-li-track-horrible-top.jpg) |
| 02:30:39 | [023039-road-damage-2026-11-18-levels-level-li-track-horrible-rider.jpg](023039-road-damage-2026-11-18-levels-level-li-track-horrible-rider.jpg) |
| 02:30:52 | [023052-road-damage-2026-11-18-levels-level-li-track-bad-wet.jpg](023052-road-damage-2026-11-18-levels-level-li-track-bad-wet.jpg) |
| 02:31:06 | [023106-road-damage-2026-11-18-levels-level-li-track-horrible-wet.jpg](023106-road-damage-2026-11-18-levels-level-li-track-horrible-wet.jpg) |
| 02:44:49 | [024449-release-0.2.3-web-webgpu-web-world-first-loading.jpg](024449-release-0.2.3-web-webgpu-web-world-first-loading.jpg) |
| 02:44:49 | [024449-release-0.2.3-web-webgpu-web-world.jpg](024449-release-0.2.3-web-webgpu-web-world.jpg) |
| 02:45:20 | [024520-release-0.2.3-web-webgl2-web-world-webgl2-first-loading.jpg](024520-release-0.2.3-web-webgl2-web-world-webgl2-first-loading.jpg) |
| 02:45:20 | [024520-release-0.2.3-web-webgl2-web-world-webgl2.jpg](024520-release-0.2.3-web-webgl2-web-world-webgl2.jpg) |
| 02:45:54 | [024554-release-0.2.3-web-unsigned-web-world-first-loading.jpg](024554-release-0.2.3-web-unsigned-web-world-first-loading.jpg) |
| 02:45:54 | [024554-release-0.2.3-web-unsigned-web-world.jpg](024554-release-0.2.3-web-unsigned-web-world.jpg) |
| 03:17:41 | [031741-shot-wayland-level-bf-minor-off-top.jpg](031741-shot-wayland-level-bf-minor-off-top.jpg) |
| 03:17:59 | [031759-shot-wayland-level-bf-minor-excellent-top.jpg](031759-shot-wayland-level-bf-minor-excellent-top.jpg) |
| 03:18:16 | [031816-shot-wayland-level-bf-minor-good-top.jpg](031816-shot-wayland-level-bf-minor-good-top.jpg) |
| 03:18:33 | [031833-shot-wayland-level-bf-minor-good-rider.jpg](031833-shot-wayland-level-bf-minor-good-rider.jpg) |
| 03:18:51 | [031851-shot-wayland-level-bf-minor-intermediate-top.jpg](031851-shot-wayland-level-bf-minor-intermediate-top.jpg) |
| 03:19:09 | [031909-shot-wayland-level-bf-minor-intermediate-rider.jpg](031909-shot-wayland-level-bf-minor-intermediate-rider.jpg) |
| 03:19:25 | [031925-shot-wayland-level-bf-minor-bad-top.jpg](031925-shot-wayland-level-bf-minor-bad-top.jpg) |
| 03:19:43 | [031943-shot-wayland-level-bf-minor-bad-rider.jpg](031943-shot-wayland-level-bf-minor-bad-rider.jpg) |
| 03:20:00 | [032000-shot-wayland-level-bf-minor-very-bad-top.jpg](032000-shot-wayland-level-bf-minor-very-bad-top.jpg) |
| 03:20:18 | [032018-shot-wayland-level-bf-minor-very-bad-rider.jpg](032018-shot-wayland-level-bf-minor-very-bad-rider.jpg) |
| 03:20:35 | [032035-shot-wayland-level-bf-minor-horrible-top.jpg](032035-shot-wayland-level-bf-minor-horrible-top.jpg) |
| 03:20:53 | [032053-shot-wayland-level-bf-minor-horrible-rider.jpg](032053-shot-wayland-level-bf-minor-horrible-rider.jpg) |
| 03:21:10 | [032110-shot-wayland-level-bf-minor-bad-wet.jpg](032110-shot-wayland-level-bf-minor-bad-wet.jpg) |
| 03:21:27 | [032127-shot-wayland-level-bf-minor-horrible-wet.jpg](032127-shot-wayland-level-bf-minor-horrible-wet.jpg) |
| 03:21:40 | [032140-shot-wayland-level-li-minor-off-top.jpg](032140-shot-wayland-level-li-minor-off-top.jpg) |
| 03:21:53 | [032153-shot-wayland-level-li-minor-excellent-top.jpg](032153-shot-wayland-level-li-minor-excellent-top.jpg) |
| 03:22:06 | [032206-shot-wayland-level-li-minor-good-top.jpg](032206-shot-wayland-level-li-minor-good-top.jpg) |
| 03:22:19 | [032219-shot-wayland-level-li-minor-good-rider.jpg](032219-shot-wayland-level-li-minor-good-rider.jpg) |
| 03:22:32 | [032232-shot-wayland-level-li-minor-intermediate-top.jpg](032232-shot-wayland-level-li-minor-intermediate-top.jpg) |
| 03:22:45 | [032245-shot-wayland-level-li-minor-intermediate-rider.jpg](032245-shot-wayland-level-li-minor-intermediate-rider.jpg) |
| 03:22:58 | [032258-shot-wayland-level-li-minor-bad-top.jpg](032258-shot-wayland-level-li-minor-bad-top.jpg) |
| 03:23:11 | [032311-shot-wayland-level-li-minor-bad-rider.jpg](032311-shot-wayland-level-li-minor-bad-rider.jpg) |
| 03:23:24 | [032324-shot-wayland-level-li-minor-very-bad-top.jpg](032324-shot-wayland-level-li-minor-very-bad-top.jpg) |
| 03:23:36 | [032336-shot-wayland-level-li-minor-very-bad-rider.jpg](032336-shot-wayland-level-li-minor-very-bad-rider.jpg) |
| 03:23:49 | [032349-shot-wayland-level-li-minor-horrible-top.jpg](032349-shot-wayland-level-li-minor-horrible-top.jpg) |
| 03:24:03 | [032403-shot-wayland-level-li-minor-horrible-rider.jpg](032403-shot-wayland-level-li-minor-horrible-rider.jpg) |
| 03:24:16 | [032416-shot-wayland-level-li-minor-bad-wet.jpg](032416-shot-wayland-level-li-minor-bad-wet.jpg) |
| 03:24:29 | [032429-shot-wayland-level-li-minor-horrible-wet.jpg](032429-shot-wayland-level-li-minor-horrible-wet.jpg) |
| 03:24:45 | [032445-shot-wayland-level-tf-minor-bad-top.jpg](032445-shot-wayland-level-tf-minor-bad-top.jpg) |
| 03:25:02 | [032502-shot-wayland-level-tf-minor-bad-rider.jpg](032502-shot-wayland-level-tf-minor-bad-rider.jpg) |
| 03:25:18 | [032518-shot-wayland-level-tf-minor-horrible-top.jpg](032518-shot-wayland-level-tf-minor-horrible-top.jpg) |
| 03:25:34 | [032534-shot-wayland-level-tf-minor-horrible-rider.jpg](032534-shot-wayland-level-tf-minor-horrible-rider.jpg) |
| 03:25:50 | [032550-shot-wayland-level-tf-minor-bad-wet.jpg](032550-shot-wayland-level-tf-minor-bad-wet.jpg) |
| 03:26:06 | [032606-shot-wayland-level-tf-minor-horrible-wet.jpg](032606-shot-wayland-level-tf-minor-horrible-wet.jpg) |
| 03:26:20 | [032620-shot-wayland-level-li-main-bad-top.jpg](032620-shot-wayland-level-li-main-bad-top.jpg) |
| 03:26:33 | [032633-shot-wayland-level-li-main-bad-rider.jpg](032633-shot-wayland-level-li-main-bad-rider.jpg) |
| 03:26:47 | [032647-shot-wayland-level-li-main-horrible-top.jpg](032647-shot-wayland-level-li-main-horrible-top.jpg) |
| 03:27:00 | [032700-shot-wayland-level-li-main-horrible-rider.jpg](032700-shot-wayland-level-li-main-horrible-rider.jpg) |
| 03:27:13 | [032713-shot-wayland-level-li-main-bad-wet.jpg](032713-shot-wayland-level-li-main-bad-wet.jpg) |
| 03:27:27 | [032727-shot-wayland-level-li-main-horrible-wet.jpg](032727-shot-wayland-level-li-main-horrible-wet.jpg) |
| 03:27:40 | [032740-shot-wayland-level-li-track-bad-top.jpg](032740-shot-wayland-level-li-track-bad-top.jpg) |
| 03:27:53 | [032753-shot-wayland-level-li-track-bad-rider.jpg](032753-shot-wayland-level-li-track-bad-rider.jpg) |
| 03:28:07 | [032807-shot-wayland-level-li-track-horrible-top.jpg](032807-shot-wayland-level-li-track-horrible-top.jpg) |
| 03:28:20 | [032820-shot-wayland-level-li-track-horrible-rider.jpg](032820-shot-wayland-level-li-track-horrible-rider.jpg) |
| 03:28:34 | [032834-shot-wayland-level-li-track-bad-wet.jpg](032834-shot-wayland-level-li-track-bad-wet.jpg) |
| 03:28:47 | [032847-shot-wayland-level-li-track-horrible-wet.jpg](032847-shot-wayland-level-li-track-horrible-wet.jpg) |
| 03:32:05 | [033205-shot-ocw.jpg](033205-shot-ocw.jpg) |
| 03:38:57 | [033857-shot-wayland-ocw-wayland.jpg](033857-shot-wayland-ocw-wayland.jpg) |
| 03:42:38 | [034238-photo-preview-web-web-photo-preview.jpg](034238-photo-preview-web-web-photo-preview.jpg) |
| 03:55:16 | [035516-photo-preview-runs-x11-Pictures-OCW-OCW-2026-11-18-03-55-13.jpg](035516-photo-preview-runs-x11-Pictures-OCW-OCW-2026-11-18-03-55-13.jpg) |
| 03:55:19 | [035519-photo-preview-runs-x11-Pictures-OCW-OCW-2026-11-18-03-55-17.jpg](035519-photo-preview-runs-x11-Pictures-OCW-OCW-2026-11-18-03-55-17.jpg) |
| 03:55:19 | [035519-photo-preview-runs-x11-hud-chase-01-preview.jpg](035519-photo-preview-runs-x11-hud-chase-01-preview.jpg) |
| 03:55:21 | [035521-photo-preview-runs-x11-hud-chase-02-preview.jpg](035521-photo-preview-runs-x11-hud-chase-02-preview.jpg) |
| 03:55:30 | [035530-photo-preview-runs-x11-end.jpg](035530-photo-preview-runs-x11-end.jpg) |
| 03:55:37 | [035537-photo-preview-runs-wayland-Pictures-OCW-OCW-2026-11-18-03-55-37.jpg](035537-photo-preview-runs-wayland-Pictures-OCW-OCW-2026-11-18-03-55-37.jpg) |
| 03:55:38 | [035538-photo-preview-runs-wayland-hud-chase-01-preview.jpg](035538-photo-preview-runs-wayland-hud-chase-01-preview.jpg) |
| 03:55:39 | [035539-photo-preview-runs-wayland-Pictures-OCW-OCW-2026-11-18-03-55-39.jpg](035539-photo-preview-runs-wayland-Pictures-OCW-OCW-2026-11-18-03-55-39.jpg) |
| 03:55:39 | [035539-photo-preview-runs-wayland-hud-chase-02-preview.jpg](035539-photo-preview-runs-wayland-hud-chase-02-preview.jpg) |
| 03:56:09 | [035609-web-web-calendar-select.jpg](035609-web-web-calendar-select.jpg) |
| 03:56:09 | [035609-web-web-calendar.jpg](035609-web-web-calendar.jpg) |
| 03:56:09 | [035609-web-web-console.jpg](035609-web-web-console.jpg) |
| 03:56:09 | [035609-web-web-downloads-ocw-2026-11-18-03-57-27.jpg](035609-web-web-downloads-ocw-2026-11-18-03-57-27.jpg) |
| 03:56:09 | [035609-web-web-downloads-ocw-2026-11-18-03-57-31.webm](035609-web-web-downloads-ocw-2026-11-18-03-57-31.webm) |
| 03:56:09 | [035609-web-web-gamepad.jpg](035609-web-web-gamepad.jpg) |
| 03:56:09 | [035609-web-web-gps.jpg](035609-web-web-gps.jpg) |
| 03:56:09 | [035609-web-web-hud.jpg](035609-web-web-hud.jpg) |
| 03:56:09 | [035609-web-web-join.jpg](035609-web-web-join.jpg) |
| 03:56:09 | [035609-web-web-menu.jpg](035609-web-web-menu.jpg) |
| 03:56:09 | [035609-web-web-ride.jpg](035609-web-web-ride.jpg) |
| 03:56:09 | [035609-web-web-riders.jpg](035609-web-web-riders.jpg) |
| 03:56:09 | [035609-web-web-settings.jpg](035609-web-web-settings.jpg) |
| 03:56:09 | [035609-web-web-touch-hints.jpg](035609-web-web-touch-hints.jpg) |
| 03:56:09 | [035609-web-web-touch-hold.jpg](035609-web-web-touch-hold.jpg) |
| 03:56:09 | [035609-web-web-unicorn-flight.jpg](035609-web-web-unicorn-flight.jpg) |
| 03:56:09 | [035609-web-web-unicorn-inspect.jpg](035609-web-web-unicorn-inspect.jpg) |
| 03:56:09 | [035609-web-web-unicorn-menu.jpg](035609-web-web-unicorn-menu.jpg) |
| 03:56:09 | [035609-web-web-weather.jpg](035609-web-web-weather.jpg) |
| 03:56:09 | [035609-web-web.jpg](035609-web-web.jpg) |
| 03:56:14 | [035614-photo-preview-runs-wayland-end.jpg](035614-photo-preview-runs-wayland-end.jpg) |
| 03:56:44 | [035644-photo-preview-runs-off-Pictures-OCW-OCW-2026-11-18-03-56-40.jpg](035644-photo-preview-runs-off-Pictures-OCW-OCW-2026-11-18-03-56-40.jpg) |
| 03:56:44 | [035644-photo-preview-runs-off-end.jpg](035644-photo-preview-runs-off-end.jpg) |
| 03:57:29 | [035729-photo-preview-runs-video-Pictures-OCW-OCW-2026-11-18-03-56-50.jpg](035729-photo-preview-runs-video-Pictures-OCW-OCW-2026-11-18-03-56-50.jpg) |
| 03:58:25 | [035825-photo-preview-runs-video-preview-x11.jpg](035825-photo-preview-runs-video-preview-x11.jpg) |
| 03:58:31 | [035831-photo-preview-runs-video-preview-x11.mp4](035831-photo-preview-runs-video-preview-x11.mp4) |
| 03:58:41 | [035841-road-damage-2026-11-18-web-web-world-cached-loading.jpg](035841-road-damage-2026-11-18-web-web-world-cached-loading.jpg) |
| 03:58:41 | [035841-road-damage-2026-11-18-web-web-world-cached.jpg](035841-road-damage-2026-11-18-web-web-world-cached.jpg) |
| 03:58:41 | [035841-road-damage-2026-11-18-web-web-world-first-loading.jpg](035841-road-damage-2026-11-18-web-web-world-first-loading.jpg) |
| 03:58:41 | [035841-road-damage-2026-11-18-web-web-world-teleport.jpg](035841-road-damage-2026-11-18-web-web-world-teleport.jpg) |
| 03:58:41 | [035841-road-damage-2026-11-18-web-web-world.jpg](035841-road-damage-2026-11-18-web-web-world.jpg) |
| 03:59:36 | [035936-road-damage-2026-11-18-web-web-world-webgl2-cached-loading.jpg](035936-road-damage-2026-11-18-web-web-world-webgl2-cached-loading.jpg) |
| 03:59:36 | [035936-road-damage-2026-11-18-web-web-world-webgl2-cached.jpg](035936-road-damage-2026-11-18-web-web-world-webgl2-cached.jpg) |
| 03:59:36 | [035936-road-damage-2026-11-18-web-web-world-webgl2-first-loading.jpg](035936-road-damage-2026-11-18-web-web-world-webgl2-first-loading.jpg) |
| 03:59:36 | [035936-road-damage-2026-11-18-web-web-world-webgl2-teleport.jpg](035936-road-damage-2026-11-18-web-web-world-webgl2-teleport.jpg) |
| 03:59:36 | [035936-road-damage-2026-11-18-web-web-world-webgl2.jpg](035936-road-damage-2026-11-18-web-web-world-webgl2.jpg) |
| 04:00:00 | [040000-strava-manual-2026-11-18-shot-ride-page-shot.jpg](040000-strava-manual-2026-11-18-shot-ride-page-shot.jpg) |
| 04:00:57 | [040057-strava-manual-2026-11-18-shot-wayland-ride-page-shot-wayland.jpg](040057-strava-manual-2026-11-18-shot-wayland-ride-page-shot-wayland.jpg) |
| 04:05:03 | [040503-strava-manual-2026-11-18-shot-ride-page-shot.jpg](040503-strava-manual-2026-11-18-shot-ride-page-shot.jpg) |
| 04:06:05 | [040605-strava-manual-2026-11-18-shot-wayland-ride-page-shot-wayland.jpg](040605-strava-manual-2026-11-18-shot-wayland-ride-page-shot-wayland.jpg) |
| 04:13:32 | [041332-strava-manual-2026-11-18-shot-ride-page-shot.jpg](041332-strava-manual-2026-11-18-shot-ride-page-shot.jpg) |
| 04:17:22 | [041722-strava-manual-2026-11-18-shot-ride-page-shot.jpg](041722-strava-manual-2026-11-18-shot-ride-page-shot.jpg) |
| 04:22:39 | [042239-strava-manual-2026-11-18-shot-ride-page-shot.jpg](042239-strava-manual-2026-11-18-shot-ride-page-shot.jpg) |
| 04:29:48 | [042948-web-web-calendar-select.jpg](042948-web-web-calendar-select.jpg) |
| 04:29:48 | [042948-web-web-calendar.jpg](042948-web-web-calendar.jpg) |
| 04:29:48 | [042948-web-web-console.jpg](042948-web-web-console.jpg) |
| 04:29:48 | [042948-web-web-gamepad.jpg](042948-web-web-gamepad.jpg) |
| 04:29:48 | [042948-web-web-gps.jpg](042948-web-web-gps.jpg) |
| 04:29:48 | [042948-web-web-hud.jpg](042948-web-web-hud.jpg) |
| 04:29:48 | [042948-web-web-join.jpg](042948-web-web-join.jpg) |
| 04:29:48 | [042948-web-web-menu.jpg](042948-web-web-menu.jpg) |
| 04:29:48 | [042948-web-web-ride.jpg](042948-web-web-ride.jpg) |
| 04:29:48 | [042948-web-web-riders.jpg](042948-web-web-riders.jpg) |
| 04:29:48 | [042948-web-web-settings.jpg](042948-web-web-settings.jpg) |
| 04:29:48 | [042948-web-web-strava-row.jpg](042948-web-web-strava-row.jpg) |
| 04:29:48 | [042948-web-web-strava-steps.jpg](042948-web-web-strava-steps.jpg) |
| 04:29:48 | [042948-web-web-touch-hints.jpg](042948-web-web-touch-hints.jpg) |
| 04:29:48 | [042948-web-web-touch-hold.jpg](042948-web-web-touch-hold.jpg) |
| 04:29:48 | [042948-web-web-unicorn-flight.jpg](042948-web-web-unicorn-flight.jpg) |
| 04:29:48 | [042948-web-web-unicorn-inspect.jpg](042948-web-web-unicorn-inspect.jpg) |
| 04:29:48 | [042948-web-web-unicorn-menu.jpg](042948-web-web-unicorn-menu.jpg) |
| 04:29:48 | [042948-web-web-weather.jpg](042948-web-web-weather.jpg) |
| 04:29:48 | [042948-web-web.jpg](042948-web-web.jpg) |
| 04:41:39 | [044139-places-navi-vaduz-day.jpg](044139-places-navi-vaduz-day.jpg) |
| 04:42:29 | [044229-places-navi-vaduz-night.jpg](044229-places-navi-vaduz-night.jpg) |
| 04:43:38 | [044338-shot-ocw.jpg](044338-shot-ocw.jpg) |
| 04:43:48 | [044348-shot-wayland-ocw-wayland.jpg](044348-shot-wayland-ocw-wayland.jpg) |
| 04:43:56 | [044356-places-navi-freiburg-day.jpg](044356-places-navi-freiburg-day.jpg) |
| 04:45:27 | [044527-places-navi-freiburg-night.jpg](044527-places-navi-freiburg-night.jpg) |
| 04:46:45 | [044645-places-navi-puerto-de-la-cruz-day.jpg](044645-places-navi-puerto-de-la-cruz-day.jpg) |
| 04:48:01 | [044801-places-navi-puerto-de-la-cruz-night.jpg](044801-places-navi-puerto-de-la-cruz-night.jpg) |
| 04:51:47 | [045147-places-navi-v2-navi-vaduz-day-z7.jpg](045147-places-navi-v2-navi-vaduz-day-z7.jpg) |
| 04:52:34 | [045234-places-navi-v2-navi-vaduz-day-z4.jpg](045234-places-navi-v2-navi-vaduz-day-z4.jpg) |
| 04:53:25 | [045325-places-navi-v2-navi-vaduz-night-z4.jpg](045325-places-navi-v2-navi-vaduz-night-z4.jpg) |
| 04:54:51 | [045451-places-navi-v2-navi-freiburg-day-z7.jpg](045451-places-navi-v2-navi-freiburg-day-z7.jpg) |
| 04:56:21 | [045621-places-navi-v2-navi-freiburg-day-z4.jpg](045621-places-navi-v2-navi-freiburg-day-z4.jpg) |
| 04:57:45 | [045745-places-navi-v2-navi-freiburg-night-z4.jpg](045745-places-navi-v2-navi-freiburg-night-z4.jpg) |
| 04:58:55 | [045855-places-navi-v2-navi-puerto-de-la-cruz-day-z7.jpg](045855-places-navi-v2-navi-puerto-de-la-cruz-day-z7.jpg) |
| 05:00:04 | [050004-places-navi-v2-navi-puerto-de-la-cruz-day-z4.jpg](050004-places-navi-v2-navi-puerto-de-la-cruz-day-z4.jpg) |
| 05:01:17 | [050117-places-navi-v2-navi-puerto-de-la-cruz-night-z4.jpg](050117-places-navi-v2-navi-puerto-de-la-cruz-night-z4.jpg) |
| 05:10:33 | [051033-shot-ocw.jpg](051033-shot-ocw.jpg) |
| 05:10:44 | [051044-shot-wayland-ocw-wayland.jpg](051044-shot-wayland-ocw-wayland.jpg) |
| 05:14:29 | [051429-marge-archive-shot-ocw.jpg](051429-marge-archive-shot-ocw.jpg) |
| 05:14:39 | [051439-marge-archive-shot-wayland-ocw-wayland.jpg](051439-marge-archive-shot-wayland-ocw-wayland.jpg) |
| 05:15:13 | [051513-marge-archive-shot-navi-vaduz-day-z7.jpg](051513-marge-archive-shot-navi-vaduz-day-z7.jpg) |
| 05:15:46 | [051546-marge-archive-shot-navi-vaduz-day-z4.jpg](051546-marge-archive-shot-navi-vaduz-day-z4.jpg) |
| 05:16:18 | [051618-marge-archive-shot-navi-vaduz-night-z4.jpg](051618-marge-archive-shot-navi-vaduz-night-z4.jpg) |
| 05:17:40 | [051740-marge-archive-shot-navi-freiburg-day-z7.jpg](051740-marge-archive-shot-navi-freiburg-day-z7.jpg) |
| 05:19:06 | [051906-marge-archive-shot-navi-freiburg-day-z4.jpg](051906-marge-archive-shot-navi-freiburg-day-z4.jpg) |
| 05:19:27 | [051927-web-web-calendar-select.jpg](051927-web-web-calendar-select.jpg) |
| 05:19:27 | [051927-web-web-calendar.jpg](051927-web-web-calendar.jpg) |
| 05:19:27 | [051927-web-web-console.jpg](051927-web-web-console.jpg) |
| 05:19:27 | [051927-web-web-gamepad.jpg](051927-web-web-gamepad.jpg) |
| 05:19:27 | [051927-web-web-gps.jpg](051927-web-web-gps.jpg) |
| 05:19:27 | [051927-web-web-hud.jpg](051927-web-web-hud.jpg) |
| 05:19:27 | [051927-web-web-join.jpg](051927-web-web-join.jpg) |
| 05:19:27 | [051927-web-web-menu.jpg](051927-web-web-menu.jpg) |
| 05:19:27 | [051927-web-web-photo-preview.jpg](051927-web-web-photo-preview.jpg) |
| 05:19:27 | [051927-web-web-ride.jpg](051927-web-web-ride.jpg) |
| 05:19:27 | [051927-web-web-riders.jpg](051927-web-web-riders.jpg) |
| 05:19:27 | [051927-web-web-settings.jpg](051927-web-web-settings.jpg) |
| 05:19:27 | [051927-web-web-strava-row.jpg](051927-web-web-strava-row.jpg) |
| 05:19:27 | [051927-web-web-strava-steps.jpg](051927-web-web-strava-steps.jpg) |
| 05:19:27 | [051927-web-web-touch-hints.jpg](051927-web-web-touch-hints.jpg) |
| 05:19:27 | [051927-web-web-touch-hold.jpg](051927-web-web-touch-hold.jpg) |
| 05:19:27 | [051927-web-web-unicorn-flight.jpg](051927-web-web-unicorn-flight.jpg) |
| 05:19:27 | [051927-web-web-unicorn-inspect.jpg](051927-web-web-unicorn-inspect.jpg) |
| 05:19:27 | [051927-web-web-unicorn-menu.jpg](051927-web-web-unicorn-menu.jpg) |
| 05:19:27 | [051927-web-web-weather.jpg](051927-web-web-weather.jpg) |
| 05:19:27 | [051927-web-web.jpg](051927-web-web.jpg) |
| 05:20:36 | [052036-marge-archive-shot-navi-freiburg-night-z4.jpg](052036-marge-archive-shot-navi-freiburg-night-z4.jpg) |
| 05:21:52 | [052152-marge-archive-shot-navi-puerto-de-la-cruz-day-z7.jpg](052152-marge-archive-shot-navi-puerto-de-la-cruz-day-z7.jpg) |
| 05:23:09 | [052309-marge-archive-shot-navi-puerto-de-la-cruz-day-z4.jpg](052309-marge-archive-shot-navi-puerto-de-la-cruz-day-z4.jpg) |
| 05:24:20 | [052420-marge-archive-shot-navi-puerto-de-la-cruz-night-z4.jpg](052420-marge-archive-shot-navi-puerto-de-la-cruz-night-z4.jpg) |
| 05:40:19 | [054019-places-navi-v4-navi-vaduz-day-z7.jpg](054019-places-navi-v4-navi-vaduz-day-z7.jpg) |
| 05:41:34 | [054134-places-navi-v4-navi-vaduz-day-z4.jpg](054134-places-navi-v4-navi-vaduz-day-z4.jpg) |
| 05:42:50 | [054250-places-navi-v4-navi-vaduz-night-z4.jpg](054250-places-navi-v4-navi-vaduz-night-z4.jpg) |
| 05:44:42 | [054442-places-navi-v4-navi-freiburg-day-z7.jpg](054442-places-navi-v4-navi-freiburg-day-z7.jpg) |
| 05:46:33 | [054633-places-navi-v4-navi-freiburg-day-z4.jpg](054633-places-navi-v4-navi-freiburg-day-z4.jpg) |
| 05:48:18 | [054818-places-navi-v4-navi-freiburg-night-z4.jpg](054818-places-navi-v4-navi-freiburg-night-z4.jpg) |
| 05:50:03 | [055003-places-navi-v4-navi-puerto-de-la-cruz-day-z7.jpg](055003-places-navi-v4-navi-puerto-de-la-cruz-day-z7.jpg) |
| 05:51:51 | [055151-places-navi-v4-navi-puerto-de-la-cruz-day-z4.jpg](055151-places-navi-v4-navi-puerto-de-la-cruz-day-z4.jpg) |
| 05:53:38 | [055338-places-navi-v4-navi-puerto-de-la-cruz-night-z4.jpg](055338-places-navi-v4-navi-puerto-de-la-cruz-night-z4.jpg) |
| 06:05:10 | [060510-places-navi-v5-navi-vaduz-day-z7.jpg](060510-places-navi-v5-navi-vaduz-day-z7.jpg) |
| 06:06:17 | [060617-places-navi-v5-navi-vaduz-day-z4.jpg](060617-places-navi-v5-navi-vaduz-day-z4.jpg) |
| 06:07:24 | [060724-places-navi-v5-navi-vaduz-night-z4.jpg](060724-places-navi-v5-navi-vaduz-night-z4.jpg) |
| 06:09:07 | [060907-places-navi-v5-navi-freiburg-day-z7.jpg](060907-places-navi-v5-navi-freiburg-day-z7.jpg) |
| 06:10:52 | [061052-places-navi-v5-navi-freiburg-day-z4.jpg](061052-places-navi-v5-navi-freiburg-day-z4.jpg) |
| 06:12:35 | [061235-places-navi-v5-navi-freiburg-night-z4.jpg](061235-places-navi-v5-navi-freiburg-night-z4.jpg) |
| 06:14:14 | [061414-places-navi-v5-navi-puerto-de-la-cruz-day-z7.jpg](061414-places-navi-v5-navi-puerto-de-la-cruz-day-z7.jpg) |
| 06:15:54 | [061554-places-navi-v5-navi-puerto-de-la-cruz-day-z4-after-90s.jpg](061554-places-navi-v5-navi-puerto-de-la-cruz-day-z4-after-90s.jpg) |
| 06:17:33 | [061733-places-navi-v5-navi-puerto-de-la-cruz-night-z4-after-90s.jpg](061733-places-navi-v5-navi-puerto-de-la-cruz-night-z4-after-90s.jpg) |
| 06:19:51 | [061951-places-navi-v5-navi-puerto-de-la-cruz-day-z4.jpg](061951-places-navi-v5-navi-puerto-de-la-cruz-day-z4.jpg) |
| 06:19:51 | [061951-places-navi-v5-navi-puerto-de-la-cruz-night-z4.jpg](061951-places-navi-v5-navi-puerto-de-la-cruz-night-z4.jpg) |
| 06:24:57 | [062457-places-navi-v6-navi-puerto-de-la-cruz-day-z4.jpg](062457-places-navi-v6-navi-puerto-de-la-cruz-day-z4.jpg) |
| 06:25:47 | [062547-places-navi-v6-navi-puerto-de-la-cruz-night-z4.jpg](062547-places-navi-v6-navi-puerto-de-la-cruz-night-z4.jpg) |
| 06:26:54 | [062654-places-navi-v6-navi-vaduz-day-z7.jpg](062654-places-navi-v6-navi-vaduz-day-z7.jpg) |
| 07:38:22 | [073822-web-xr-web-xr-after.jpg](073822-web-xr-web-xr-after.jpg) |
| 07:38:22 | [073822-web-xr-web-xr-flat.jpg](073822-web-xr-web-xr-flat.jpg) |
| 07:38:22 | [073822-web-xr-web-xr-unsupported.jpg](073822-web-xr-web-xr-unsupported.jpg) |
| 07:38:22 | [073822-web-xr-web-xr-xr-copy.png](073822-web-xr-web-xr-xr-copy.png) |
| 07:38:22 | [073822-web-xr-web-xr-xr-down.jpg](073822-web-xr-web-xr-xr-down.jpg) |
| 07:38:22 | [073822-web-xr-web-xr-xr-left.jpg](073822-web-xr-web-xr-xr-left.jpg) |
| 07:38:22 | [073822-web-xr-web-xr-xr-right.jpg](073822-web-xr-web-xr-xr-right.jpg) |
| 07:38:22 | [073822-web-xr-web-xr-xr-sweep-000.jpg](073822-web-xr-web-xr-xr-sweep-000.jpg) |
| 07:38:22 | [073822-web-xr-web-xr-xr-sweep-001.jpg](073822-web-xr-web-xr-xr-sweep-001.jpg) |
| 07:38:22 | [073822-web-xr-web-xr-xr-sweep-002.jpg](073822-web-xr-web-xr-xr-sweep-002.jpg) |
| 07:38:22 | [073822-web-xr-web-xr-xr-sweep-003.jpg](073822-web-xr-web-xr-xr-sweep-003.jpg) |
| 07:38:22 | [073822-web-xr-web-xr-xr-sweep-004.jpg](073822-web-xr-web-xr-xr-sweep-004.jpg) |
| 07:38:22 | [073822-web-xr-web-xr-xr-sweep-005.jpg](073822-web-xr-web-xr-xr-sweep-005.jpg) |
| 07:38:22 | [073822-web-xr-web-xr-xr-sweep-006.jpg](073822-web-xr-web-xr-xr-sweep-006.jpg) |
| 07:38:22 | [073822-web-xr-web-xr-xr-sweep-007.jpg](073822-web-xr-web-xr-xr-sweep-007.jpg) |
| 07:38:22 | [073822-web-xr-web-xr-xr-sweep-008.jpg](073822-web-xr-web-xr-xr-sweep-008.jpg) |
| 07:38:22 | [073822-web-xr-web-xr-xr-sweep-009.jpg](073822-web-xr-web-xr-xr-sweep-009.jpg) |
| 07:38:22 | [073822-web-xr-web-xr-xr-sweep-010.jpg](073822-web-xr-web-xr-xr-sweep-010.jpg) |
| 07:38:22 | [073822-web-xr-web-xr-xr-sweep-011.jpg](073822-web-xr-web-xr-xr-sweep-011.jpg) |
| 07:38:22 | [073822-web-xr-web-xr-xr-sweep-012.jpg](073822-web-xr-web-xr-xr-sweep-012.jpg) |
| 07:38:22 | [073822-web-xr-web-xr-xr-sweep-013.jpg](073822-web-xr-web-xr-xr-sweep-013.jpg) |
| 07:38:22 | [073822-web-xr-web-xr-xr-sweep-014.jpg](073822-web-xr-web-xr-xr-sweep-014.jpg) |
| 07:38:22 | [073822-web-xr-web-xr-xr-sweep-015.jpg](073822-web-xr-web-xr-xr-sweep-015.jpg) |
| 07:38:22 | [073822-web-xr-web-xr-xr-sweep-016.jpg](073822-web-xr-web-xr-xr-sweep-016.jpg) |
| 07:38:22 | [073822-web-xr-web-xr-xr-sweep-017.jpg](073822-web-xr-web-xr-xr-sweep-017.jpg) |
| 07:38:22 | [073822-web-xr-web-xr-xr-sweep-018.jpg](073822-web-xr-web-xr-xr-sweep-018.jpg) |
| 07:38:22 | [073822-web-xr-web-xr-xr-sweep-019.jpg](073822-web-xr-web-xr-xr-sweep-019.jpg) |
| 07:38:22 | [073822-web-xr-web-xr-xr-sweep-020.jpg](073822-web-xr-web-xr-xr-sweep-020.jpg) |
| 07:38:22 | [073822-web-xr-web-xr-xr-sweep-021.jpg](073822-web-xr-web-xr-xr-sweep-021.jpg) |
| 07:38:22 | [073822-web-xr-web-xr-xr-sweep-022.jpg](073822-web-xr-web-xr-xr-sweep-022.jpg) |
| 07:38:22 | [073822-web-xr-web-xr-xr-sweep-023.jpg](073822-web-xr-web-xr-xr-sweep-023.jpg) |
| 07:38:22 | [073822-web-xr-web-xr-xr-sweep-024.jpg](073822-web-xr-web-xr-xr-sweep-024.jpg) |
| 07:38:22 | [073822-web-xr-web-xr-xr-sweep-025.jpg](073822-web-xr-web-xr-xr-sweep-025.jpg) |
| 07:38:22 | [073822-web-xr-web-xr-xr-sweep-026.jpg](073822-web-xr-web-xr-xr-sweep-026.jpg) |
| 07:38:22 | [073822-web-xr-web-xr-xr-sweep-027.jpg](073822-web-xr-web-xr-xr-sweep-027.jpg) |
| 07:38:22 | [073822-web-xr-web-xr-xr-sweep-028.jpg](073822-web-xr-web-xr-xr-sweep-028.jpg) |
| 07:38:22 | [073822-web-xr-web-xr-xr-sweep-029.jpg](073822-web-xr-web-xr-xr-sweep-029.jpg) |
| 07:38:22 | [073822-web-xr-web-xr-xr-sweep-030.jpg](073822-web-xr-web-xr-xr-sweep-030.jpg) |
| 07:38:22 | [073822-web-xr-web-xr-xr-sweep-031.jpg](073822-web-xr-web-xr-xr-sweep-031.jpg) |
| 07:38:22 | [073822-web-xr-web-xr-xr-sweep-032.jpg](073822-web-xr-web-xr-xr-sweep-032.jpg) |
| 07:38:22 | [073822-web-xr-web-xr-xr-sweep-033.jpg](073822-web-xr-web-xr-xr-sweep-033.jpg) |
| 07:38:22 | [073822-web-xr-web-xr-xr-sweep-034.jpg](073822-web-xr-web-xr-xr-sweep-034.jpg) |
| 07:38:22 | [073822-web-xr-web-xr-xr-sweep-035.jpg](073822-web-xr-web-xr-xr-sweep-035.jpg) |
| 07:38:22 | [073822-web-xr-web-xr-xr-sweep-036.jpg](073822-web-xr-web-xr-xr-sweep-036.jpg) |
| 07:38:22 | [073822-web-xr-web-xr-xr-sweep-037.jpg](073822-web-xr-web-xr-xr-sweep-037.jpg) |
| 07:38:22 | [073822-web-xr-web-xr-xr-sweep-038.jpg](073822-web-xr-web-xr-xr-sweep-038.jpg) |
| 07:38:22 | [073822-web-xr-web-xr-xr-sweep-039.jpg](073822-web-xr-web-xr-xr-sweep-039.jpg) |
| 07:38:22 | [073822-web-xr-web-xr-xr-sweep-040.jpg](073822-web-xr-web-xr-xr-sweep-040.jpg) |
| 07:38:22 | [073822-web-xr-web-xr-xr-sweep-041.jpg](073822-web-xr-web-xr-xr-sweep-041.jpg) |
| 07:38:22 | [073822-web-xr-web-xr-xr-sweep-042.jpg](073822-web-xr-web-xr-xr-sweep-042.jpg) |
| 07:38:22 | [073822-web-xr-web-xr-xr-sweep-043.jpg](073822-web-xr-web-xr-xr-sweep-043.jpg) |
| 07:38:22 | [073822-web-xr-web-xr-xr-sweep-044.jpg](073822-web-xr-web-xr-xr-sweep-044.jpg) |
| 07:38:22 | [073822-web-xr-web-xr-xr-sweep-045.jpg](073822-web-xr-web-xr-xr-sweep-045.jpg) |
| 07:38:22 | [073822-web-xr-web-xr-xr-sweep-046.jpg](073822-web-xr-web-xr-xr-sweep-046.jpg) |
| 07:38:22 | [073822-web-xr-web-xr-xr-sweep-047.jpg](073822-web-xr-web-xr-xr-sweep-047.jpg) |
| 07:38:22 | [073822-web-xr-web-xr-xr-sweep.mp4](073822-web-xr-web-xr-xr-sweep.mp4) |
| 07:38:22 | [073822-web-xr-web-xr-xr-turned.jpg](073822-web-xr-web-xr-xr-turned.jpg) |
| 07:38:22 | [073822-web-xr-web-xr-xr-view.jpg](073822-web-xr-web-xr-xr-view.jpg) |
| 08:08:13 | [080813-web-xr-web-xr-after.jpg](080813-web-xr-web-xr-after.jpg) |
| 08:08:13 | [080813-web-xr-web-xr-flat.jpg](080813-web-xr-web-xr-flat.jpg) |
| 08:08:13 | [080813-web-xr-web-xr-unsupported.jpg](080813-web-xr-web-xr-unsupported.jpg) |
| 08:08:13 | [080813-web-xr-web-xr-xr-copy.png](080813-web-xr-web-xr-xr-copy.png) |
| 08:08:13 | [080813-web-xr-web-xr-xr-down.jpg](080813-web-xr-web-xr-xr-down.jpg) |
| 08:08:13 | [080813-web-xr-web-xr-xr-left.jpg](080813-web-xr-web-xr-xr-left.jpg) |
| 08:08:13 | [080813-web-xr-web-xr-xr-right.jpg](080813-web-xr-web-xr-xr-right.jpg) |
| 08:08:13 | [080813-web-xr-web-xr-xr-sweep-000.jpg](080813-web-xr-web-xr-xr-sweep-000.jpg) |
| 08:08:13 | [080813-web-xr-web-xr-xr-sweep-001.jpg](080813-web-xr-web-xr-xr-sweep-001.jpg) |
| 08:08:13 | [080813-web-xr-web-xr-xr-sweep-002.jpg](080813-web-xr-web-xr-xr-sweep-002.jpg) |
| 08:08:13 | [080813-web-xr-web-xr-xr-sweep-003.jpg](080813-web-xr-web-xr-xr-sweep-003.jpg) |
| 08:08:13 | [080813-web-xr-web-xr-xr-sweep-004.jpg](080813-web-xr-web-xr-xr-sweep-004.jpg) |
| 08:08:13 | [080813-web-xr-web-xr-xr-sweep-005.jpg](080813-web-xr-web-xr-xr-sweep-005.jpg) |
| 08:08:13 | [080813-web-xr-web-xr-xr-sweep-006.jpg](080813-web-xr-web-xr-xr-sweep-006.jpg) |
| 08:08:13 | [080813-web-xr-web-xr-xr-sweep-007.jpg](080813-web-xr-web-xr-xr-sweep-007.jpg) |
| 08:08:13 | [080813-web-xr-web-xr-xr-sweep-008.jpg](080813-web-xr-web-xr-xr-sweep-008.jpg) |
| 08:08:13 | [080813-web-xr-web-xr-xr-sweep-009.jpg](080813-web-xr-web-xr-xr-sweep-009.jpg) |
| 08:08:13 | [080813-web-xr-web-xr-xr-sweep-010.jpg](080813-web-xr-web-xr-xr-sweep-010.jpg) |
| 08:08:13 | [080813-web-xr-web-xr-xr-sweep-011.jpg](080813-web-xr-web-xr-xr-sweep-011.jpg) |
| 08:08:13 | [080813-web-xr-web-xr-xr-sweep-012.jpg](080813-web-xr-web-xr-xr-sweep-012.jpg) |
| 08:08:13 | [080813-web-xr-web-xr-xr-sweep-013.jpg](080813-web-xr-web-xr-xr-sweep-013.jpg) |
| 08:08:13 | [080813-web-xr-web-xr-xr-sweep-014.jpg](080813-web-xr-web-xr-xr-sweep-014.jpg) |
| 08:08:13 | [080813-web-xr-web-xr-xr-sweep-015.jpg](080813-web-xr-web-xr-xr-sweep-015.jpg) |
| 08:08:13 | [080813-web-xr-web-xr-xr-sweep-016.jpg](080813-web-xr-web-xr-xr-sweep-016.jpg) |
| 08:08:13 | [080813-web-xr-web-xr-xr-sweep-017.jpg](080813-web-xr-web-xr-xr-sweep-017.jpg) |
| 08:08:13 | [080813-web-xr-web-xr-xr-sweep-018.jpg](080813-web-xr-web-xr-xr-sweep-018.jpg) |
| 08:08:13 | [080813-web-xr-web-xr-xr-sweep-019.jpg](080813-web-xr-web-xr-xr-sweep-019.jpg) |
| 08:08:13 | [080813-web-xr-web-xr-xr-sweep-020.jpg](080813-web-xr-web-xr-xr-sweep-020.jpg) |
| 08:08:13 | [080813-web-xr-web-xr-xr-sweep-021.jpg](080813-web-xr-web-xr-xr-sweep-021.jpg) |
| 08:08:13 | [080813-web-xr-web-xr-xr-sweep-022.jpg](080813-web-xr-web-xr-xr-sweep-022.jpg) |
| 08:08:13 | [080813-web-xr-web-xr-xr-sweep-023.jpg](080813-web-xr-web-xr-xr-sweep-023.jpg) |
| 08:08:13 | [080813-web-xr-web-xr-xr-sweep-024.jpg](080813-web-xr-web-xr-xr-sweep-024.jpg) |
| 08:08:13 | [080813-web-xr-web-xr-xr-sweep-025.jpg](080813-web-xr-web-xr-xr-sweep-025.jpg) |
| 08:08:13 | [080813-web-xr-web-xr-xr-sweep-026.jpg](080813-web-xr-web-xr-xr-sweep-026.jpg) |
| 08:08:13 | [080813-web-xr-web-xr-xr-sweep-027.jpg](080813-web-xr-web-xr-xr-sweep-027.jpg) |
| 08:08:13 | [080813-web-xr-web-xr-xr-sweep-028.jpg](080813-web-xr-web-xr-xr-sweep-028.jpg) |
| 08:08:13 | [080813-web-xr-web-xr-xr-sweep-029.jpg](080813-web-xr-web-xr-xr-sweep-029.jpg) |
| 08:08:13 | [080813-web-xr-web-xr-xr-sweep-030.jpg](080813-web-xr-web-xr-xr-sweep-030.jpg) |
| 08:08:13 | [080813-web-xr-web-xr-xr-sweep-031.jpg](080813-web-xr-web-xr-xr-sweep-031.jpg) |
| 08:08:13 | [080813-web-xr-web-xr-xr-sweep-032.jpg](080813-web-xr-web-xr-xr-sweep-032.jpg) |
| 08:08:13 | [080813-web-xr-web-xr-xr-sweep-033.jpg](080813-web-xr-web-xr-xr-sweep-033.jpg) |
| 08:08:13 | [080813-web-xr-web-xr-xr-sweep-034.jpg](080813-web-xr-web-xr-xr-sweep-034.jpg) |
| 08:08:13 | [080813-web-xr-web-xr-xr-sweep-035.jpg](080813-web-xr-web-xr-xr-sweep-035.jpg) |
| 08:08:13 | [080813-web-xr-web-xr-xr-sweep-036.jpg](080813-web-xr-web-xr-xr-sweep-036.jpg) |
| 08:08:13 | [080813-web-xr-web-xr-xr-sweep-037.jpg](080813-web-xr-web-xr-xr-sweep-037.jpg) |
| 08:08:13 | [080813-web-xr-web-xr-xr-sweep-038.jpg](080813-web-xr-web-xr-xr-sweep-038.jpg) |
| 08:08:13 | [080813-web-xr-web-xr-xr-sweep-039.jpg](080813-web-xr-web-xr-xr-sweep-039.jpg) |
| 08:08:13 | [080813-web-xr-web-xr-xr-sweep-040.jpg](080813-web-xr-web-xr-xr-sweep-040.jpg) |
| 08:08:13 | [080813-web-xr-web-xr-xr-sweep-041.jpg](080813-web-xr-web-xr-xr-sweep-041.jpg) |
| 08:08:13 | [080813-web-xr-web-xr-xr-sweep-042.jpg](080813-web-xr-web-xr-xr-sweep-042.jpg) |
| 08:08:13 | [080813-web-xr-web-xr-xr-sweep-043.jpg](080813-web-xr-web-xr-xr-sweep-043.jpg) |
| 08:08:13 | [080813-web-xr-web-xr-xr-sweep-044.jpg](080813-web-xr-web-xr-xr-sweep-044.jpg) |
| 08:08:13 | [080813-web-xr-web-xr-xr-sweep-045.jpg](080813-web-xr-web-xr-xr-sweep-045.jpg) |
| 08:08:13 | [080813-web-xr-web-xr-xr-sweep-046.jpg](080813-web-xr-web-xr-xr-sweep-046.jpg) |
| 08:08:13 | [080813-web-xr-web-xr-xr-sweep-047.jpg](080813-web-xr-web-xr-xr-sweep-047.jpg) |
| 08:08:13 | [080813-web-xr-web-xr-xr-sweep.mp4](080813-web-xr-web-xr-xr-sweep.mp4) |
| 08:08:13 | [080813-web-xr-web-xr-xr-turned.jpg](080813-web-xr-web-xr-xr-turned.jpg) |
| 08:08:13 | [080813-web-xr-web-xr-xr-view.jpg](080813-web-xr-web-xr-xr-view.jpg) |
| 08:08:52 | [080852-web-web-calendar-select.jpg](080852-web-web-calendar-select.jpg) |
| 08:08:52 | [080852-web-web-calendar.jpg](080852-web-web-calendar.jpg) |
| 08:08:52 | [080852-web-web-console.jpg](080852-web-web-console.jpg) |
| 08:08:52 | [080852-web-web-downloads-OCW-2026-11-18-08-10-03.jpg](080852-web-web-downloads-OCW-2026-11-18-08-10-03.jpg) |
| 08:08:52 | [080852-web-web-downloads-ocw-2026-11-18-08-10-12.webm](080852-web-web-downloads-ocw-2026-11-18-08-10-12.webm) |
| 08:08:52 | [080852-web-web-gamepad.jpg](080852-web-web-gamepad.jpg) |
| 08:08:52 | [080852-web-web-gps.jpg](080852-web-web-gps.jpg) |
| 08:08:52 | [080852-web-web-hud.jpg](080852-web-web-hud.jpg) |
| 08:08:52 | [080852-web-web-join.jpg](080852-web-web-join.jpg) |
| 08:08:52 | [080852-web-web-menu.jpg](080852-web-web-menu.jpg) |
| 08:08:52 | [080852-web-web-photo-preview.jpg](080852-web-web-photo-preview.jpg) |
| 08:08:52 | [080852-web-web-ride.jpg](080852-web-web-ride.jpg) |
| 08:08:52 | [080852-web-web-riders.jpg](080852-web-web-riders.jpg) |
| 08:08:52 | [080852-web-web-settings.jpg](080852-web-web-settings.jpg) |
| 08:08:52 | [080852-web-web-strava-row.jpg](080852-web-web-strava-row.jpg) |
| 08:08:52 | [080852-web-web-strava-steps.jpg](080852-web-web-strava-steps.jpg) |
| 08:08:52 | [080852-web-web-touch-hints.jpg](080852-web-web-touch-hints.jpg) |
| 08:08:52 | [080852-web-web-touch-hold.jpg](080852-web-web-touch-hold.jpg) |
| 08:08:52 | [080852-web-web-unicorn-flight.jpg](080852-web-web-unicorn-flight.jpg) |
| 08:08:52 | [080852-web-web-unicorn-inspect.jpg](080852-web-web-unicorn-inspect.jpg) |
| 08:08:52 | [080852-web-web-unicorn-menu.jpg](080852-web-web-unicorn-menu.jpg) |
| 08:08:52 | [080852-web-web-weather.jpg](080852-web-web-weather.jpg) |
| 08:08:52 | [080852-web-web.jpg](080852-web-web.jpg) |
| 08:10:30 | [081030-web-web-webgl2-calendar-select.jpg](081030-web-web-webgl2-calendar-select.jpg) |
| 08:10:30 | [081030-web-web-webgl2-calendar.jpg](081030-web-web-webgl2-calendar.jpg) |
| 08:10:30 | [081030-web-web-webgl2-console.jpg](081030-web-web-webgl2-console.jpg) |
| 08:10:30 | [081030-web-web-webgl2-downloads-OCW-2026-11-18-08-11-40.jpg](081030-web-web-webgl2-downloads-OCW-2026-11-18-08-11-40.jpg) |
| 08:10:30 | [081030-web-web-webgl2-downloads-ocw-2026-11-18-08-11-49.webm](081030-web-web-webgl2-downloads-ocw-2026-11-18-08-11-49.webm) |
| 08:10:30 | [081030-web-web-webgl2-gamepad.jpg](081030-web-web-webgl2-gamepad.jpg) |
| 08:10:30 | [081030-web-web-webgl2-gps.jpg](081030-web-web-webgl2-gps.jpg) |
| 08:10:30 | [081030-web-web-webgl2-hud.jpg](081030-web-web-webgl2-hud.jpg) |
| 08:10:30 | [081030-web-web-webgl2-join.jpg](081030-web-web-webgl2-join.jpg) |
| 08:10:30 | [081030-web-web-webgl2-menu.jpg](081030-web-web-webgl2-menu.jpg) |
| 08:10:30 | [081030-web-web-webgl2-photo-preview.jpg](081030-web-web-webgl2-photo-preview.jpg) |
| 08:10:30 | [081030-web-web-webgl2-ride.jpg](081030-web-web-webgl2-ride.jpg) |
| 08:10:30 | [081030-web-web-webgl2-riders.jpg](081030-web-web-webgl2-riders.jpg) |
| 08:10:30 | [081030-web-web-webgl2-settings.jpg](081030-web-web-webgl2-settings.jpg) |
| 08:10:30 | [081030-web-web-webgl2-strava-row.jpg](081030-web-web-webgl2-strava-row.jpg) |
| 08:10:30 | [081030-web-web-webgl2-strava-steps.jpg](081030-web-web-webgl2-strava-steps.jpg) |
| 08:10:30 | [081030-web-web-webgl2-touch-hints.jpg](081030-web-web-webgl2-touch-hints.jpg) |
| 08:10:30 | [081030-web-web-webgl2-touch-hold.jpg](081030-web-web-webgl2-touch-hold.jpg) |
| 08:10:30 | [081030-web-web-webgl2-unicorn-flight.jpg](081030-web-web-webgl2-unicorn-flight.jpg) |
| 08:10:30 | [081030-web-web-webgl2-unicorn-inspect.jpg](081030-web-web-webgl2-unicorn-inspect.jpg) |
| 08:10:30 | [081030-web-web-webgl2-unicorn-menu.jpg](081030-web-web-webgl2-unicorn-menu.jpg) |
| 08:10:30 | [081030-web-web-webgl2-weather.jpg](081030-web-web-webgl2-weather.jpg) |
| 08:10:30 | [081030-web-web-webgl2.jpg](081030-web-web-webgl2.jpg) |
| 08:12:05 | [081205-web-web-compare-webgl2-graphics.jpg](081205-web-web-compare-webgl2-graphics.jpg) |
| 08:12:05 | [081205-web-web-compare-webgl2-low.jpg](081205-web-web-compare-webgl2-low.jpg) |
| 08:12:05 | [081205-web-web-compare-webgpu-high.jpg](081205-web-web-compare-webgpu-high.jpg) |
| 08:12:05 | [081205-web-web-compare.jpg](081205-web-web-compare.jpg) |
| 08:12:51 | [081251-web-web-gpu-device-webgl2.jpg](081251-web-web-gpu-device-webgl2.jpg) |
| 08:12:51 | [081251-web-web-gpu-forced-webgpu.jpg](081251-web-web-gpu-forced-webgpu.jpg) |
| 08:12:51 | [081251-web-web-gpu-iphone-safari.jpg](081251-web-web-gpu-iphone-safari.jpg) |
| 08:12:51 | [081251-web-web-gpu-noframe-webgl2.jpg](081251-web-web-gpu-noframe-webgl2.jpg) |
| 08:12:51 | [081251-web-web-gpu-uncaptured-webgl2.jpg](081251-web-web-gpu-uncaptured-webgl2.jpg) |
| 08:12:51 | [081251-web-web-gpu-webgpu.jpg](081251-web-web-gpu-webgpu.jpg) |
| 10:36:43 | [103643-shot-before-road-aero-x11-studio.jpg](103643-shot-before-road-aero-x11-studio.jpg) |
| 10:37:11 | [103711-shot-before-road-aero-x11-stand.jpg](103711-shot-before-road-aero-x11-stand.jpg) |
| 10:37:27 | [103727-shot-before-road-aero-x11-ride.jpg](103727-shot-before-road-aero-x11-ride.jpg) |
| 10:37:45 | [103745-shot-before-road-climbing-x11-studio.jpg](103745-shot-before-road-climbing-x11-studio.jpg) |
| 10:38:11 | [103811-shot-before-road-climbing-x11-stand.jpg](103811-shot-before-road-climbing-x11-stand.jpg) |
| 10:38:27 | [103827-shot-before-road-climbing-x11-ride.jpg](103827-shot-before-road-climbing-x11-ride.jpg) |
| 10:38:39 | [103839-shot-before-road-endurance-x11-studio.jpg](103839-shot-before-road-endurance-x11-studio.jpg) |
| 10:39:00 | [103900-shot-before-road-endurance-x11-stand.jpg](103900-shot-before-road-endurance-x11-stand.jpg) |
| 10:39:23 | [103923-shot-before-road-endurance-x11-ride.jpg](103923-shot-before-road-endurance-x11-ride.jpg) |
| 10:39:40 | [103940-shot-before-gravel-x11-studio.jpg](103940-shot-before-gravel-x11-studio.jpg) |
| 10:40:08 | [104008-shot-before-gravel-x11-stand.jpg](104008-shot-before-gravel-x11-stand.jpg) |
| 10:41:51 | [104151-fork-rake-after-after-road-aero-x11-studio.jpg](104151-fork-rake-after-after-road-aero-x11-studio.jpg) |
| 10:41:52 | [104152-fork-rake-after-after-road-aero-x11-fork.jpg](104152-fork-rake-after-after-road-aero-x11-fork.jpg) |
| 10:42:25 | [104225-fork-rake-after-after-road-aero-x11-stand.jpg](104225-fork-rake-after-after-road-aero-x11-stand.jpg) |
| 10:42:54 | [104254-fork-rake-after-after-road-aero-x11-ride.jpg](104254-fork-rake-after-after-road-aero-x11-ride.jpg) |
| 10:43:09 | [104309-fork-rake-after-after-road-climbing-x11-studio.jpg](104309-fork-rake-after-after-road-climbing-x11-studio.jpg) |
| 10:43:11 | [104311-fork-rake-after-after-road-climbing-x11-fork.jpg](104311-fork-rake-after-after-road-climbing-x11-fork.jpg) |
| 10:43:35 | [104335-fork-rake-after-after-road-climbing-x11-stand.jpg](104335-fork-rake-after-after-road-climbing-x11-stand.jpg) |
| 10:44:13 | [104413-fork-rake-after-after-road-climbing-x11-ride.jpg](104413-fork-rake-after-after-road-climbing-x11-ride.jpg) |
| 10:44:29 | [104429-fork-rake-after-after-road-endurance-x11-studio.jpg](104429-fork-rake-after-after-road-endurance-x11-studio.jpg) |
| 10:44:31 | [104431-fork-rake-after-after-road-endurance-x11-fork.jpg](104431-fork-rake-after-after-road-endurance-x11-fork.jpg) |
| 10:45:04 | [104504-fork-rake-after-after-road-endurance-x11-stand.jpg](104504-fork-rake-after-after-road-endurance-x11-stand.jpg) |
| 10:45:37 | [104537-fork-rake-after-after-road-endurance-x11-ride.jpg](104537-fork-rake-after-after-road-endurance-x11-ride.jpg) |
| 10:45:50 | [104550-fork-rake-after-after-gravel-x11-studio.jpg](104550-fork-rake-after-after-gravel-x11-studio.jpg) |
| 10:45:52 | [104552-fork-rake-after-after-gravel-x11-fork.jpg](104552-fork-rake-after-after-gravel-x11-fork.jpg) |
| 10:46:27 | [104627-fork-rake-after-after-gravel-x11-stand.jpg](104627-fork-rake-after-after-gravel-x11-stand.jpg) |
| 10:46:48 | [104648-fork-rake-after-after-gravel-x11-ride.jpg](104648-fork-rake-after-after-gravel-x11-ride.jpg) |
| 10:47:00 | [104700-fork-rake-after-after-tt-x11-studio.jpg](104700-fork-rake-after-after-tt-x11-studio.jpg) |
| 10:47:03 | [104703-fork-rake-after-after-tt-x11-fork.jpg](104703-fork-rake-after-after-tt-x11-fork.jpg) |
| 10:47:35 | [104735-fork-rake-after-after-tt-x11-stand.jpg](104735-fork-rake-after-after-tt-x11-stand.jpg) |
| 10:48:03 | [104803-fork-rake-after-after-tt-x11-ride.jpg](104803-fork-rake-after-after-tt-x11-ride.jpg) |
| 10:48:17 | [104817-fork-rake-after-after-mtb-hardtail-x11-studio.jpg](104817-fork-rake-after-after-mtb-hardtail-x11-studio.jpg) |
| 10:48:18 | [104818-fork-rake-after-after-mtb-hardtail-x11-fork.jpg](104818-fork-rake-after-after-mtb-hardtail-x11-fork.jpg) |
| 10:48:37 | [104837-fork-rake-after-after-mtb-hardtail-x11-stand.jpg](104837-fork-rake-after-after-mtb-hardtail-x11-stand.jpg) |
| 10:49:04 | [104904-fork-rake-after-after-mtb-hardtail-x11-ride.jpg](104904-fork-rake-after-after-mtb-hardtail-x11-ride.jpg) |
| 10:49:18 | [104918-fork-rake-after-after-road-aero-wayland-fork.jpg](104918-fork-rake-after-after-road-aero-wayland-fork.jpg) |
| 10:49:18 | [104918-fork-rake-after-after-road-aero-wayland-studio.jpg](104918-fork-rake-after-after-road-aero-wayland-studio.jpg) |
| 10:49:32 | [104932-fork-rake-after-after-road-aero-wayland-stand.jpg](104932-fork-rake-after-after-road-aero-wayland-stand.jpg) |
| 10:49:43 | [104943-fork-rake-before-before-road-aero-x11-fork.jpg](104943-fork-rake-before-before-road-aero-x11-fork.jpg) |
| 10:49:43 | [104943-fork-rake-before-before-road-aero-x11-studio.jpg](104943-fork-rake-before-before-road-aero-x11-studio.jpg) |
| 10:49:46 | [104946-fork-rake-after-after-road-aero-wayland-ride.jpg](104946-fork-rake-after-after-road-aero-wayland-ride.jpg) |
| 10:49:57 | [104957-fork-rake-after-after-road-climbing-wayland-fork.jpg](104957-fork-rake-after-after-road-climbing-wayland-fork.jpg) |
| 10:49:57 | [104957-fork-rake-after-after-road-climbing-wayland-studio.jpg](104957-fork-rake-after-after-road-climbing-wayland-studio.jpg) |
| 10:49:58 | [104958-fork-rake-before-before-road-aero-x11-stand.jpg](104958-fork-rake-before-before-road-aero-x11-stand.jpg) |
| 10:50:10 | [105010-fork-rake-after-after-road-climbing-wayland-stand.jpg](105010-fork-rake-after-after-road-climbing-wayland-stand.jpg) |
| 10:50:22 | [105022-fork-rake-before-before-road-aero-x11-ride.jpg](105022-fork-rake-before-before-road-aero-x11-ride.jpg) |
| 10:50:24 | [105024-fork-rake-after-after-road-climbing-wayland-ride.jpg](105024-fork-rake-after-after-road-climbing-wayland-ride.jpg) |
| 10:50:34 | [105034-fork-rake-before-before-road-climbing-x11-studio.jpg](105034-fork-rake-before-before-road-climbing-x11-studio.jpg) |
| 10:50:35 | [105035-fork-rake-after-after-road-endurance-wayland-studio.jpg](105035-fork-rake-after-after-road-endurance-wayland-studio.jpg) |
| 10:50:35 | [105035-fork-rake-before-before-road-climbing-x11-fork.jpg](105035-fork-rake-before-before-road-climbing-x11-fork.jpg) |
| 10:50:36 | [105036-fork-rake-after-after-road-endurance-wayland-fork.jpg](105036-fork-rake-after-after-road-endurance-wayland-fork.jpg) |
| 10:50:49 | [105049-fork-rake-after-after-road-endurance-wayland-stand.jpg](105049-fork-rake-after-after-road-endurance-wayland-stand.jpg) |
| 10:50:50 | [105050-fork-rake-before-before-road-climbing-x11-stand.jpg](105050-fork-rake-before-before-road-climbing-x11-stand.jpg) |
| 10:51:02 | [105102-fork-rake-after-after-road-endurance-wayland-ride.jpg](105102-fork-rake-after-after-road-endurance-wayland-ride.jpg) |
| 10:51:13 | [105113-fork-rake-before-before-road-climbing-x11-ride.jpg](105113-fork-rake-before-before-road-climbing-x11-ride.jpg) |
| 10:51:14 | [105114-fork-rake-after-after-gravel-wayland-fork.jpg](105114-fork-rake-after-after-gravel-wayland-fork.jpg) |
| 10:51:14 | [105114-fork-rake-after-after-gravel-wayland-studio.jpg](105114-fork-rake-after-after-gravel-wayland-studio.jpg) |
| 10:51:25 | [105125-fork-rake-before-before-road-endurance-x11-studio.jpg](105125-fork-rake-before-before-road-endurance-x11-studio.jpg) |
| 10:51:26 | [105126-fork-rake-before-before-road-endurance-x11-fork.jpg](105126-fork-rake-before-before-road-endurance-x11-fork.jpg) |
| 10:51:27 | [105127-fork-rake-after-after-gravel-wayland-stand.jpg](105127-fork-rake-after-after-gravel-wayland-stand.jpg) |
| 10:51:41 | [105141-fork-rake-after-after-gravel-wayland-ride.jpg](105141-fork-rake-after-after-gravel-wayland-ride.jpg) |
| 10:51:41 | [105141-fork-rake-before-before-road-endurance-x11-stand.jpg](105141-fork-rake-before-before-road-endurance-x11-stand.jpg) |
| 10:51:52 | [105152-fork-rake-after-after-tt-wayland-studio.jpg](105152-fork-rake-after-after-tt-wayland-studio.jpg) |
| 10:51:53 | [105153-fork-rake-after-after-tt-wayland-fork.jpg](105153-fork-rake-after-after-tt-wayland-fork.jpg) |
| 10:52:04 | [105204-fork-rake-before-before-road-endurance-x11-ride.jpg](105204-fork-rake-before-before-road-endurance-x11-ride.jpg) |
| 10:52:06 | [105206-fork-rake-after-after-tt-wayland-stand.jpg](105206-fork-rake-after-after-tt-wayland-stand.jpg) |
| 10:52:16 | [105216-fork-rake-before-before-gravel-x11-studio.jpg](105216-fork-rake-before-before-gravel-x11-studio.jpg) |
| 10:52:17 | [105217-fork-rake-before-before-gravel-x11-fork.jpg](105217-fork-rake-before-before-gravel-x11-fork.jpg) |
| 10:52:19 | [105219-fork-rake-after-after-tt-wayland-ride.jpg](105219-fork-rake-after-after-tt-wayland-ride.jpg) |
| 10:52:30 | [105230-fork-rake-after-after-mtb-hardtail-wayland-studio.jpg](105230-fork-rake-after-after-mtb-hardtail-wayland-studio.jpg) |
| 10:52:31 | [105231-fork-rake-after-after-mtb-hardtail-wayland-fork.jpg](105231-fork-rake-after-after-mtb-hardtail-wayland-fork.jpg) |
| 10:52:31 | [105231-fork-rake-before-before-gravel-x11-stand.jpg](105231-fork-rake-before-before-gravel-x11-stand.jpg) |
| 10:52:44 | [105244-fork-rake-after-after-mtb-hardtail-wayland-stand.jpg](105244-fork-rake-after-after-mtb-hardtail-wayland-stand.jpg) |
| 10:52:54 | [105254-fork-rake-before-before-gravel-x11-ride.jpg](105254-fork-rake-before-before-gravel-x11-ride.jpg) |
| 10:52:57 | [105257-fork-rake-after-after-mtb-hardtail-wayland-ride.jpg](105257-fork-rake-after-after-mtb-hardtail-wayland-ride.jpg) |
| 10:53:06 | [105306-fork-rake-before-before-tt-x11-studio.jpg](105306-fork-rake-before-before-tt-x11-studio.jpg) |
| 10:53:07 | [105307-fork-rake-before-before-tt-x11-fork.jpg](105307-fork-rake-before-before-tt-x11-fork.jpg) |
| 10:53:37 | [105337-fork-rake-before-before-tt-x11-stand.jpg](105337-fork-rake-before-before-tt-x11-stand.jpg) |
| 10:53:58 | [105358-fork-rake-before-before-tt-x11-ride.jpg](105358-fork-rake-before-before-tt-x11-ride.jpg) |
| 10:54:11 | [105411-fork-rake-before-before-mtb-hardtail-x11-studio.jpg](105411-fork-rake-before-before-mtb-hardtail-x11-studio.jpg) |
| 10:54:12 | [105412-fork-rake-before-before-mtb-hardtail-x11-fork.jpg](105412-fork-rake-before-before-mtb-hardtail-x11-fork.jpg) |
| 10:54:58 | [105458-fork-rake-before-before-mtb-hardtail-x11-stand.jpg](105458-fork-rake-before-before-mtb-hardtail-x11-stand.jpg) |
| 10:55:20 | [105520-fork-rake-before-before-mtb-hardtail-x11-ride.jpg](105520-fork-rake-before-before-mtb-hardtail-x11-ride.jpg) |
| 10:55:32 | [105532-fork-rake-before-before-road-aero-wayland-studio.jpg](105532-fork-rake-before-before-road-aero-wayland-studio.jpg) |
| 10:55:33 | [105533-fork-rake-before-before-road-aero-wayland-fork.jpg](105533-fork-rake-before-before-road-aero-wayland-fork.jpg) |
| 10:55:46 | [105546-fork-rake-before-before-road-aero-wayland-stand.jpg](105546-fork-rake-before-before-road-aero-wayland-stand.jpg) |
| 10:55:59 | [105559-fork-rake-before-before-road-aero-wayland-ride.jpg](105559-fork-rake-before-before-road-aero-wayland-ride.jpg) |
| 10:56:10 | [105610-fork-rake-before-before-road-climbing-wayland-studio.jpg](105610-fork-rake-before-before-road-climbing-wayland-studio.jpg) |
| 10:56:11 | [105611-fork-rake-before-before-road-climbing-wayland-fork.jpg](105611-fork-rake-before-before-road-climbing-wayland-fork.jpg) |
| 10:56:24 | [105624-fork-rake-before-before-road-climbing-wayland-stand.jpg](105624-fork-rake-before-before-road-climbing-wayland-stand.jpg) |
| 10:56:37 | [105637-fork-rake-before-before-road-climbing-wayland-ride.jpg](105637-fork-rake-before-before-road-climbing-wayland-ride.jpg) |
| 10:56:48 | [105648-fork-rake-before-before-road-endurance-wayland-fork.jpg](105648-fork-rake-before-before-road-endurance-wayland-fork.jpg) |
| 10:56:48 | [105648-fork-rake-before-before-road-endurance-wayland-studio.jpg](105648-fork-rake-before-before-road-endurance-wayland-studio.jpg) |
| 10:57:02 | [105702-fork-rake-before-before-road-endurance-wayland-stand.jpg](105702-fork-rake-before-before-road-endurance-wayland-stand.jpg) |
| 10:57:15 | [105715-fork-rake-before-before-road-endurance-wayland-ride.jpg](105715-fork-rake-before-before-road-endurance-wayland-ride.jpg) |
| 10:57:27 | [105727-fork-rake-before-before-gravel-wayland-fork.jpg](105727-fork-rake-before-before-gravel-wayland-fork.jpg) |
| 10:57:27 | [105727-fork-rake-before-before-gravel-wayland-studio.jpg](105727-fork-rake-before-before-gravel-wayland-studio.jpg) |
| 10:57:41 | [105741-fork-rake-before-before-gravel-wayland-stand.jpg](105741-fork-rake-before-before-gravel-wayland-stand.jpg) |
| 10:57:55 | [105755-fork-rake-before-before-gravel-wayland-ride.jpg](105755-fork-rake-before-before-gravel-wayland-ride.jpg) |
| 10:58:06 | [105806-fork-rake-before-before-tt-wayland-studio.jpg](105806-fork-rake-before-before-tt-wayland-studio.jpg) |
| 10:58:07 | [105807-fork-rake-before-before-tt-wayland-fork.jpg](105807-fork-rake-before-before-tt-wayland-fork.jpg) |
| 10:58:20 | [105820-fork-rake-before-before-tt-wayland-stand.jpg](105820-fork-rake-before-before-tt-wayland-stand.jpg) |
| 10:58:34 | [105834-fork-rake-before-before-tt-wayland-ride.jpg](105834-fork-rake-before-before-tt-wayland-ride.jpg) |
| 10:58:46 | [105846-fork-rake-before-before-mtb-hardtail-wayland-fork.jpg](105846-fork-rake-before-before-mtb-hardtail-wayland-fork.jpg) |
| 10:58:46 | [105846-fork-rake-before-before-mtb-hardtail-wayland-studio.jpg](105846-fork-rake-before-before-mtb-hardtail-wayland-studio.jpg) |
| 10:59:00 | [105900-fork-rake-before-before-mtb-hardtail-wayland-stand.jpg](105900-fork-rake-before-before-mtb-hardtail-wayland-stand.jpg) |
| 10:59:14 | [105914-fork-rake-before-before-mtb-hardtail-wayland-ride.jpg](105914-fork-rake-before-before-mtb-hardtail-wayland-ride.jpg) |
| 10:59:45 | [105945-fork-rake-compare-compare-gravel-wayland-fork.jpg](105945-fork-rake-compare-compare-gravel-wayland-fork.jpg) |
| 10:59:45 | [105945-fork-rake-compare-compare-gravel-x11-fork.jpg](105945-fork-rake-compare-compare-gravel-x11-fork.jpg) |
| 10:59:45 | [105945-fork-rake-compare-compare-road-aero-wayland-fork.jpg](105945-fork-rake-compare-compare-road-aero-wayland-fork.jpg) |
| 10:59:45 | [105945-fork-rake-compare-compare-road-aero-x11-fork.jpg](105945-fork-rake-compare-compare-road-aero-x11-fork.jpg) |
| 10:59:45 | [105945-fork-rake-compare-compare-road-climbing-wayland-fork.jpg](105945-fork-rake-compare-compare-road-climbing-wayland-fork.jpg) |
| 10:59:45 | [105945-fork-rake-compare-compare-road-climbing-x11-fork.jpg](105945-fork-rake-compare-compare-road-climbing-x11-fork.jpg) |
| 10:59:45 | [105945-fork-rake-compare-compare-road-endurance-wayland-fork.jpg](105945-fork-rake-compare-compare-road-endurance-wayland-fork.jpg) |
| 10:59:45 | [105945-fork-rake-compare-compare-road-endurance-x11-fork.jpg](105945-fork-rake-compare-compare-road-endurance-x11-fork.jpg) |
| 10:59:45 | [105945-fork-rake-compare-compare-tt-x11-fork.jpg](105945-fork-rake-compare-compare-tt-x11-fork.jpg) |
| 10:59:46 | [105946-fork-rake-compare-compare-mtb-hardtail-wayland-fork.jpg](105946-fork-rake-compare-compare-mtb-hardtail-wayland-fork.jpg) |
| 10:59:46 | [105946-fork-rake-compare-compare-mtb-hardtail-x11-fork.jpg](105946-fork-rake-compare-compare-mtb-hardtail-x11-fork.jpg) |
| 10:59:46 | [105946-fork-rake-compare-compare-tt-wayland-fork.jpg](105946-fork-rake-compare-compare-tt-wayland-fork.jpg) |
| 11:28:25 | [112825-shot-ocw.jpg](112825-shot-ocw.jpg) |
| 11:28:35 | [112835-shot-wayland-ocw-wayland.jpg](112835-shot-wayland-ocw-wayland.jpg) |
| 11:43:37 | [114337-activities-folder-stop-x11.jpg](114337-activities-folder-stop-x11.jpg) |
| 11:45:05 | [114505-activities-folder-upload-x11.jpg](114505-activities-folder-upload-x11.jpg) |
| 11:46:27 | [114627-activities-folder-stop-wayland.jpg](114627-activities-folder-stop-wayland.jpg) |
| 11:47:50 | [114750-activities-folder-upload-wayland.jpg](114750-activities-folder-upload-wayland.jpg) |
| 11:48:24 | [114824-shot-ocw.jpg](114824-shot-ocw.jpg) |
| 11:48:34 | [114834-shot-wayland-ocw-wayland.jpg](114834-shot-wayland-ocw-wayland.jpg) |
| 12:07:18 | [120718-activities-folder-stop-x11.jpg](120718-activities-folder-stop-x11.jpg) |
| 12:10:15 | [121015-activities-folder-stop-x11-end.jpg](121015-activities-folder-stop-x11-end.jpg) |
| 12:11:29 | [121129-web-web-calendar-select.jpg](121129-web-web-calendar-select.jpg) |
| 12:11:29 | [121129-web-web-calendar.jpg](121129-web-web-calendar.jpg) |
| 12:11:29 | [121129-web-web-console.jpg](121129-web-web-console.jpg) |
| 12:11:29 | [121129-web-web-gamepad.jpg](121129-web-web-gamepad.jpg) |
| 12:11:29 | [121129-web-web-gps.jpg](121129-web-web-gps.jpg) |
| 12:11:29 | [121129-web-web-hud.jpg](121129-web-web-hud.jpg) |
| 12:11:29 | [121129-web-web-join.jpg](121129-web-web-join.jpg) |
| 12:11:29 | [121129-web-web-menu.jpg](121129-web-web-menu.jpg) |
| 12:11:29 | [121129-web-web-photo-preview.jpg](121129-web-web-photo-preview.jpg) |
| 12:11:29 | [121129-web-web-ride.jpg](121129-web-web-ride.jpg) |
| 12:11:29 | [121129-web-web-riders.jpg](121129-web-web-riders.jpg) |
| 12:11:29 | [121129-web-web-settings.jpg](121129-web-web-settings.jpg) |
| 12:11:29 | [121129-web-web-strava-recording-downloaded.jpg](121129-web-web-strava-recording-downloaded.jpg) |
| 12:11:29 | [121129-web-web-strava-recording-saved-to-folder.jpg](121129-web-web-strava-recording-saved-to-folder.jpg) |
| 12:11:29 | [121129-web-web-strava-recording.jpg](121129-web-web-strava-recording.jpg) |
| 12:11:29 | [121129-web-web-strava-row.jpg](121129-web-web-strava-row.jpg) |
| 12:11:29 | [121129-web-web-strava-steps.jpg](121129-web-web-strava-steps.jpg) |
| 12:11:29 | [121129-web-web-touch-hints.jpg](121129-web-web-touch-hints.jpg) |
| 12:11:29 | [121129-web-web-touch-hold.jpg](121129-web-web-touch-hold.jpg) |
| 12:11:29 | [121129-web-web-unicorn-flight.jpg](121129-web-web-unicorn-flight.jpg) |
| 12:11:29 | [121129-web-web-unicorn-inspect.jpg](121129-web-web-unicorn-inspect.jpg) |
| 12:11:29 | [121129-web-web-unicorn-menu.jpg](121129-web-web-unicorn-menu.jpg) |
| 12:11:29 | [121129-web-web-weather.jpg](121129-web-web-weather.jpg) |
| 12:11:29 | [121129-web-web.jpg](121129-web-web.jpg) |
| 12:15:00 | [121500-activities-folder-upload-x11.jpg](121500-activities-folder-upload-x11.jpg) |
| 12:17:29 | [121729-activities-folder-upload-x11-end.jpg](121729-activities-folder-upload-x11-end.jpg) |
| 12:18:59 | [121859-activities-folder-stop-wayland.jpg](121859-activities-folder-stop-wayland.jpg) |
| 12:19:36 | [121936-activities-folder-stop-wayland-end.jpg](121936-activities-folder-stop-wayland-end.jpg) |
| 12:20:57 | [122057-activities-folder-upload-wayland.jpg](122057-activities-folder-upload-wayland.jpg) |
| 12:21:29 | [122129-activities-folder-upload-wayland-end.jpg](122129-activities-folder-upload-wayland-end.jpg) |
| 13:17:20 | [131720-strava-pending-stop-x11.jpg](131720-strava-pending-stop-x11.jpg) |
| 13:17:42 | [131742-strava-pending-waiting-x11.jpg](131742-strava-pending-waiting-x11.jpg) |
| 13:20:24 | [132024-strava-pending-waiting-x11-end.jpg](132024-strava-pending-waiting-x11-end.jpg) |
| 13:22:22 | [132222-strava-pending-question-x11.jpg](132222-strava-pending-question-x11.jpg) |
| 13:22:33 | [132233-strava-pending-uploaded-x11.jpg](132233-strava-pending-uploaded-x11.jpg) |
| 13:22:52 | [132252-strava-pending-on-strava-x11.jpg](132252-strava-pending-on-strava-x11.jpg) |
| 13:25:35 | [132535-strava-pending-uploaded-x11-end.jpg](132535-strava-pending-uploaded-x11-end.jpg) |
| 13:26:17 | [132617-strava-pending-stop-wayland.jpg](132617-strava-pending-stop-wayland.jpg) |
| 13:26:26 | [132626-strava-pending-waiting-wayland.jpg](132626-strava-pending-waiting-wayland.jpg) |
| 13:27:13 | [132713-strava-pending-waiting-wayland-end.jpg](132713-strava-pending-waiting-wayland-end.jpg) |
| 13:27:47 | [132747-strava-pending-question-wayland.jpg](132747-strava-pending-question-wayland.jpg) |
| 13:27:52 | [132752-strava-pending-uploaded-wayland.jpg](132752-strava-pending-uploaded-wayland.jpg) |
| 13:28:00 | [132800-strava-pending-on-strava-wayland.jpg](132800-strava-pending-on-strava-wayland.jpg) |
| 13:28:47 | [132847-strava-pending-uploaded-wayland-end.jpg](132847-strava-pending-uploaded-wayland-end.jpg) |
| 13:46:44 | [134644-shot-ocw.jpg](134644-shot-ocw.jpg) |
| 13:46:53 | [134653-shot-wayland-ocw-wayland.jpg](134653-shot-wayland-ocw-wayland.jpg) |
| 13:58:02 | [135802-web-web-calendar-select.jpg](135802-web-web-calendar-select.jpg) |
| 13:58:02 | [135802-web-web-calendar.jpg](135802-web-web-calendar.jpg) |
| 13:58:02 | [135802-web-web-console.jpg](135802-web-web-console.jpg) |
| 13:58:02 | [135802-web-web-downloads-OCW-2026-11-18-13-59-14.jpg](135802-web-web-downloads-OCW-2026-11-18-13-59-14.jpg) |
| 13:58:02 | [135802-web-web-downloads-ocw-2026-11-18-13-59-35.webm](135802-web-web-downloads-ocw-2026-11-18-13-59-35.webm) |
| 13:58:02 | [135802-web-web-gamepad.jpg](135802-web-web-gamepad.jpg) |
| 13:58:02 | [135802-web-web-gps.jpg](135802-web-web-gps.jpg) |
| 13:58:02 | [135802-web-web-hud.jpg](135802-web-web-hud.jpg) |
| 13:58:02 | [135802-web-web-join.jpg](135802-web-web-join.jpg) |
| 13:58:02 | [135802-web-web-menu.jpg](135802-web-web-menu.jpg) |
| 13:58:02 | [135802-web-web-photo-preview.jpg](135802-web-web-photo-preview.jpg) |
| 13:58:02 | [135802-web-web-ride.jpg](135802-web-web-ride.jpg) |
| 13:58:02 | [135802-web-web-riders.jpg](135802-web-web-riders.jpg) |
| 13:58:02 | [135802-web-web-settings.jpg](135802-web-web-settings.jpg) |
| 13:58:02 | [135802-web-web-strava-recording-downloaded.jpg](135802-web-web-strava-recording-downloaded.jpg) |
| 13:58:02 | [135802-web-web-strava-recording-saved-to-folder.jpg](135802-web-web-strava-recording-saved-to-folder.jpg) |
| 13:58:02 | [135802-web-web-strava-recording.jpg](135802-web-web-strava-recording.jpg) |
| 13:58:02 | [135802-web-web-strava-row.jpg](135802-web-web-strava-row.jpg) |
| 13:58:02 | [135802-web-web-strava-steps.jpg](135802-web-web-strava-steps.jpg) |
| 13:58:02 | [135802-web-web-touch-hints.jpg](135802-web-web-touch-hints.jpg) |
| 13:58:02 | [135802-web-web-touch-hold.jpg](135802-web-web-touch-hold.jpg) |
| 13:58:02 | [135802-web-web-unicorn-flight.jpg](135802-web-web-unicorn-flight.jpg) |
| 13:58:02 | [135802-web-web-unicorn-inspect.jpg](135802-web-web-unicorn-inspect.jpg) |
| 13:58:02 | [135802-web-web-unicorn-menu.jpg](135802-web-web-unicorn-menu.jpg) |
| 13:58:02 | [135802-web-web-weather.jpg](135802-web-web-weather.jpg) |
| 13:58:02 | [135802-web-web.jpg](135802-web-web.jpg) |
| 14:01:53 | [140153-strava-pending-stop-x11.jpg](140153-strava-pending-stop-x11.jpg) |
| 14:02:15 | [140215-strava-pending-waiting-x11.jpg](140215-strava-pending-waiting-x11.jpg) |
| 14:04:59 | [140459-strava-pending-waiting-x11-end.jpg](140459-strava-pending-waiting-x11-end.jpg) |
| 14:06:55 | [140655-strava-pending-question-x11.jpg](140655-strava-pending-question-x11.jpg) |
| 14:07:07 | [140707-strava-pending-uploaded-x11.jpg](140707-strava-pending-uploaded-x11.jpg) |
| 14:07:25 | [140725-strava-pending-on-strava-x11.jpg](140725-strava-pending-on-strava-x11.jpg) |
| 14:10:09 | [141009-strava-pending-uploaded-x11-end.jpg](141009-strava-pending-uploaded-x11-end.jpg) |
| 14:10:51 | [141051-strava-pending-stop-wayland.jpg](141051-strava-pending-stop-wayland.jpg) |
| 14:11:00 | [141100-strava-pending-waiting-wayland.jpg](141100-strava-pending-waiting-wayland.jpg) |
| 14:11:47 | [141147-strava-pending-waiting-wayland-end.jpg](141147-strava-pending-waiting-wayland-end.jpg) |
| 14:12:21 | [141221-strava-pending-question-wayland.jpg](141221-strava-pending-question-wayland.jpg) |
| 14:12:26 | [141226-strava-pending-uploaded-wayland.jpg](141226-strava-pending-uploaded-wayland.jpg) |
| 14:12:34 | [141234-strava-pending-on-strava-wayland.jpg](141234-strava-pending-on-strava-wayland.jpg) |
| 14:13:21 | [141321-strava-pending-uploaded-wayland-end.jpg](141321-strava-pending-uploaded-wayland-end.jpg) |
| 14:34:28 | [143428-release-0.2.4-web-webgpu-web-world-cached-loading.jpg](143428-release-0.2.4-web-webgpu-web-world-cached-loading.jpg) |
| 14:34:28 | [143428-release-0.2.4-web-webgpu-web-world-cached.jpg](143428-release-0.2.4-web-webgpu-web-world-cached.jpg) |
| 14:34:28 | [143428-release-0.2.4-web-webgpu-web-world-first-loading.jpg](143428-release-0.2.4-web-webgpu-web-world-first-loading.jpg) |
| 14:34:28 | [143428-release-0.2.4-web-webgpu-web-world.jpg](143428-release-0.2.4-web-webgpu-web-world.jpg) |
| 14:34:31 | [143431-release-0.2.4-appimage-x11.jpg](143431-release-0.2.4-appimage-x11.jpg) |
| 14:34:58 | [143458-release-0.2.4-appimage-wayland.jpg](143458-release-0.2.4-appimage-wayland.jpg) |
| 14:35:02 | [143502-release-0.2.4-web-webgl2-web-world-webgl2-cached-loading.jpg](143502-release-0.2.4-web-webgl2-web-world-webgl2-cached-loading.jpg) |
| 14:35:02 | [143502-release-0.2.4-web-webgl2-web-world-webgl2-cached.jpg](143502-release-0.2.4-web-webgl2-web-world-webgl2-cached.jpg) |
| 14:35:02 | [143502-release-0.2.4-web-webgl2-web-world-webgl2-first-loading.jpg](143502-release-0.2.4-web-webgl2-web-world-webgl2-first-loading.jpg) |
| 14:35:02 | [143502-release-0.2.4-web-webgl2-web-world-webgl2.jpg](143502-release-0.2.4-web-webgl2-web-world-webgl2.jpg) |
| 14:35:22 | [143522-release-0.2.4-tarball-x11.jpg](143522-release-0.2.4-tarball-x11.jpg) |
| 14:35:48 | [143548-release-0.2.4-tarball-wayland.jpg](143548-release-0.2.4-tarball-wayland.jpg) |
| 14:36:04 | [143604-release-0.2.4-studio-wayland.jpg](143604-release-0.2.4-studio-wayland.jpg) |
| 14:36:21 | [143621-release-0.2.4-studio-x11.jpg](143621-release-0.2.4-studio-x11.jpg) |
| 18:35:49 | [183549-feature-fps-cost-shots-blackforest-mummelsee-km7-all-on.jpg](183549-feature-fps-cost-shots-blackforest-mummelsee-km7-all-on.jpg) |
| 18:36:08 | [183608-feature-fps-cost-shots-tenerife-masca-km9-all-on.jpg](183608-feature-fps-cost-shots-tenerife-masca-km9-all-on.jpg) |
| 18:36:26 | [183626-feature-fps-cost-shots-liechtenstein-vaduz-free-all-on.jpg](183626-feature-fps-cost-shots-liechtenstein-vaduz-free-all-on.jpg) |
| 18:36:45 | [183645-feature-fps-cost-shots-tenerife-puerto-teide-km4-horrible-all-on.jpg](183645-feature-fps-cost-shots-tenerife-puerto-teide-km4-horrible-all-on.jpg) |
| 21:32:27 | [213227-dashboard-battery-guard-battery-guard-cards.png](213227-dashboard-battery-guard-battery-guard-cards.png) |
