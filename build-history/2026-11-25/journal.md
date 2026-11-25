# OCW build diary – day 15, 2026-11-25

48 commits (10 merges), +10782 / −937 lines, 367 images, 6 videos, 0 sounds.

## Commits

| Time | Commit | |
|---|---|---|
| 04:14 | `c473eb11` | Built: the browser reads its WebTransport connections in a Web Worker, snapshot jitter 13.6 -> 0.1 ms (60 fps) and 24.4 -> 0.1 ms (25 fps), the others 4x smoother; own rider worse at 25 fps (open) (Phase 10, 10G B3 worker, 5.81) |
| 05:04 | `75c64ff6` | Network worker on by default for the sensor bridge only, the game link opt-in (net-worker=on): the own rider still moved less smoothly with it even with the worker's stamps in the ArrivalClock (Phase 10, 10G B3 worker, 5.81) |
| 05:05 | `d9bc9fb1` (merge) | Merge the sensor bridge read in a Web Worker (0.36 ms old on arrival) with the game link on the page's thread by default; net-worker=on opts the game link into the worker (10G B3, 5.81) |
| 05:07 | `2c0abf94` | While sharing its trainer with a browser the desktop shows a simple Sharing screen and pauses its own ride (10D.2) |
| 06:26 | `d4276df6` | Built: the desktop's Sharing screen while a browser rides with its trainer, its own ride paused (10D.2, 5.83) |
| 06:27 | `b8572b79` (merge) | Merge the desktop's Sharing screen: while a browser rides on its trainer the desktop shows the browser, live readings, the grade it sets, the bridge and Stop sharing, its own ride paused (10D.2, 5.83) |
| 08:25 | `347c53f8` | Riders change between the draped and the handshake grip on the hoods; sprints in the drops, out of the saddle, rocking the bike (Phase 4 Q31 and sprint behaviour) |
| 09:00 | `3f336a8f` | Part tiles keep the gain against the base part for the reference rider (Phase 4 Q26 (a)) |
| 09:05 | `d22f8b6b` | Build caps per kind (rolling, aero, weight) so a better part never lowers the others' gains (Phase 4 Q27 (b)) |
| 09:09 | `b4c2cffc` | Kit pickers as tiles with a row of colour swatches (Phase 4 Q30 (a)) |
| 09:14 | `9b0e9139` | Built: riders hold the road hoods draped or in the handshake grip and change every 20-90 s; sprints go to the drops deep in the hooks, out of the saddle, rocking the bike (14 Phase 4 Q31, 2.6, v5.85) |
| 09:30 | `cba2f214` | Build caps per kind: rolling, aero, weight and drivetrain each within its own share of the limit (Phase 4 Q27 (b) built) |
| 09:39 | `293c6c55` | Q31 scenes: the sprint shots and the video from the front quarter (the chase camera lags at sprint speed) |
| 09:44 | `9e70227f` (merge) | Merge riders' hood grips (draped and handshake, changing every 20–90 s) and the sprint (drops, out of the saddle, the bike rocking) (Phase 4 Q31, 2.6; 5.88) |
| 09:48 | `a0f23639` | Junctions share a short edge and take the room a far end leaves (4.8.8 Rule, J9) |
| 10:06 | `9f32a289` (merge) | Merge build caps per kind: rolling, aero, weight and drivetrain each within their own budget, so a better part never lowers another part's gain (Phase 4 Q27 (b), 4G Caps; 5.89) |
| 10:06 | `7f4cebf5` | Format the J9 tests |
| 10:58 | `3940bcb3` | Kit pickers as tiles with a row of colour swatches above them (Phase 4 Q30 (a)) |
| 11:32 | `1fb8e6c2` | Kit tile scenes step to the right mirror slots; rustfmt |
| 11:56 | `029cdcf3` | Kit tiles frame the item: shorts on the legs, socks on the feet; tiles in the selected colour; std swatch marked |
| 11:57 | `0829ea18` | rustfmt; spec: kit tile framing and std swatch |
| 12:15 | `9cbd20cc` (merge) | Merge kit pickers as tiles: shorts, socks, shoes and gloves as picture tiles with a row of colour swatches above them (Phase 4 Q30 (a), 4N; 5.90) |
| 12:30 | `58ed70f9` | Built: the sides of a road are as smooth as the road, J9 (4.8.8 Rule) |
| 12:51 | `23c74451` | Rule: test pictures and videos vary the riders' bodies, kit and bike setup |
| 12:54 | `76f86d5e` | A painted crossing stays where OSM has it: no shared patch or longer mouth swallows one (4.8.8 Rule, J9) |
| 13:08 | `e0f43b25` | Spec 4.8.8 Built (J9): painted crossings stay where OSM has them; Liechtenstein rebuilt |
| 13:17 | `89b2322a` (merge) | Merge J9: two close junctions share one surface, arms take the room before a bridge or split, painted crossings stay where OSM has them; side.corner −4 to −13 % (4.8.8 Rule, 5.91) |
| 13:58 | `a337a60a` | Release 0.2.6 |
| 15:07 | `06156163` | Height points win over the gradient limit, as built (16H Q8 (a)) |
| 15:07 | `52d4029f` | Spec: remove leftover conflict markers in 4N (Q30 and Q31 built lines kept) |
| 15:34 | `bc7469ce` | A world patch ships as its own .ocwpatch file next to the package, its checksum in the manifest (16H Q9 (a)) |
| 15:42 | `e02af7a3` | Official world patches in git under worlds/<region>/patches/ (16H Q10 (a)) |
| 15:54 | `2ee32aba` | Height point defaults stay 15 m snap and 100 m blend (16H Q11 (a)) |
| 15:59 | `fe185161` | Studio camera hovers by default, plane under View → Flight (16H Q12 (a)) |
| 16:04 | `f59c9cb3` | Spec 4.8.8 Built (J9): all five packages rebuilt with painted crossings kept in place (final lint, checksums, build machines; 5.91) |
| 19:39 | `5ad9844f` | Spec 16H Q14 elaborated: an example, what the game asks, what the studio does today, the shared trust list |
| 19:40 | `c3fe597b` | Spec 16H Q14: the studio does not read the trusted-keys list yet |
| 19:40 | `7d97fded` | Studio asks with the game's trust dialog for unknown user keys (16H Q14 (a)) |
| 20:22 | `429d9c25` | A world patch travels next to its package, its SHA-256 in the manifest; our patches live in worlds/<region>/patches/ (16H Q9 (a), Q10 (a); spec 5.98) |
| 20:36 | `2ce6b4cf` | Built: OCW Studio asks with the game's trust dialog for unknown user keys and shares the game's trusted-keys list (spec 16H Q14 (a), 5.98) |
| 20:43 | `3d16a5fc` | Fixed: no bubble on the rider's chin (4N, v5.98) |
| 20:48 | `65378fb8` | Studio 2D map shows the joined neighbouring packages and the aerial-photo layer (16H Q15 (a)) |
| 20:50 | `cca0eae8` | Studio 2D map: the world's border as a thin line (16H Q15) |
| 20:55 | `37f45eb8` (merge) | Merge world patches: <package>.ocwpatch shipped next to the package with its checksum in the manifest, official patches in git under worlds/<region>/patches/ (16H Q9 (a), Q10 (a); 5.99) |
| 20:57 | `c125ae44` (merge) | Merge the studio's trust dialog: a world signed by an unknown user key asks with the game's dialog, one trusted-keys list for both apps (16H Q14 (a); 6.00) |
| 21:27 | `21b0f664` (merge) | Merge the chin fix: one broad jaw instead of the 4-sided chin bubble, a gentler older jaw, beards covering it, the strap buckle under the chin (4N Fixed; 6.01) |
| 22:47 | `63480cea` | Built: OCW Studio's 2D map draws the joined neighbouring packages dimmed, the world's border as a thin line and the aerial photo as a layer, off by default (16H Q15 (a); spec 6.02) |
| 22:48 | `84be3af7` (merge) | Merge the studio's 2D map additions: neighbouring worlds dimmed, the world's border line, the aerial-photo layer (16H Q15 (a); 6.02) |

## Builds and build servers

171 build/test runs on the build machines, 37.2 h in total, 11 failed; 1440 server samples; cargo compiled 35841 crates in 9.7 h, 9.1 h waiting for build slots.

| Machine | Runs | Hours | Cargo h | Crates | Waited h | Failed | Online |
|---|---|---|---|---|---|---|---|
| Weela | 1 | 0.0 | 0.0 | 0 | 0.0 | 1 | 0% |
| Win11Builder | 7 | 1.7 | 1.6 | 2060 | 0.0 | 3 | 64% |
| leela | 28 | 10.1 | 3.8 | 14622 | 2.4 | 0 | 100% |
| macos | 18 | 3.5 | 0.4 | 845 | 1.1 | 1 | 100% |
| marge | 117 | 22.0 | 3.9 | 18314 | 5.5 | 6 | 100% |

Failed runs:

- 05:55 Win11Builder: `cargo clippy -p ocw-desktop --all-targets -- -D warnings 2>&1 | Select-String -P` (exit 1, log `build-log/055528-Win11Builder-1222554.log`)
- 05:55 Weela: `cargo clippy -p ocw-desktop --all-targets -- -D warnings 2>&1 | Select-String -P` (exit 1, log `build-log/055545-Weela-1222897.log`)
- 06:56 Win11Builder: `cargo clippy -p ocw-desktop --all-targets -- -D warnings; if ($LASTEXITCODE -eq ` (exit 1, log `build-log/065626-Win11Builder-1324779.log`)
- 08:22 marge: `scripts/j9-iter.sh base` (exit 127, log `build-log/082236-marge-1444174.log`)
- 08:37 marge: `cargo build --release -p ocw-desktop 2>&1 | tail -2; ls -la target/release/ocw-d` (exit 2, log `build-log/083713-marge-1459863.log`)
- 10:12 Win11Builder: `cargo test -p ocw-render --lib workshop; if ($LASTEXITCODE -eq 0) { cargo test -` (exit 101, log `build-log/101247-Win11Builder-1719530.log`)
- 13:53 macos: `cargo build --release -p world-builder 2>&1 | tail -1; D=$HOME/j9data; O=$HOME/j` (exit 1, log `build-log/135339-macos-2111519.log`)
- 19:47 marge: `source ~/.cargo/env 2>/dev/null; cargo fmt --all -- --check && cargo test -q -p ` (exit 1, log `build-log/194702-marge-2679001.log`)
- 19:47 marge: `source ~/.cargo/env 2>/dev/null; cargo fmt --all -- --check && cargo test -q -p ` (exit 101, log `build-log/194732-marge-2679717.log`)
- 19:59 marge: `set -e; D=/tmp/ocw-q14-shot; rm -rf $D; mkdir -p $D/keys $D/friend; cp ~/src/OCW` (exit 1, log `build-log/195950-marge-2694014.log`)
- 20:25 marge: `cargo fmt --all && cargo test -p ocw-assets --lib 2>&1 | grep -E "test result|FA` (exit 129, log `build-log/202556-marge-2753944.log`)

Longest runs:

- 119 min on leela: `cargo build --release -p world-builder 2>&1 | tail -1; rm -rf $HOME/j9out; mkdir`
- 115 min on leela: `make check && make test-web-build && make test-smoke && echo ALL-CHECKS-OK`
- 95 min on marge: `WB_PREBUILT=1 scripts/j9-build.sh tenerife/tenerife > $HOME/src/OCW/data/j9-buil`
- 83 min on macos: `OCW_SHA=a337a60a OCW_FEATURES=ocw-desktop/voice scripts/build-macos-app.sh && OC`
- 73 min on macos: `D=$HOME/j9data; O=$HOME/j9out/blackforest; F=$D/blackforest/freiburg-regbez.osm.`

## Token usage

863.4 M tokens in 2,756 model messages (output 1.5 M, cache reads 846.9 M, cache writes 14.9 M, uncached input 6 k). Full breakdown: [tokens.json](tokens.json).

| Feature | Tokens | Output | Messages |
|---|---|---|---|
| Other | 655.0 M | 1.0 M | 1,934 |
| Planning & spec | 70.8 M | 35 k | 120 |
| Worlds & terrain | 68.1 M | 206 k | 382 |
| Riders & bikes | 51.5 M | 123 k | 227 |
| Build, release & infra | 17.4 M | 77 k | 90 |
| Art project | 569 k | 1 k | 3 |

| Task | Feature | Tokens | Output |
|---|---|---|---|
| agent: J9: remaining junction side faults | Other | 266.6 M | 298 k |
| agent: B3: WebTransport reading in a Web Worker | Other | 63.9 M | 174 k |
| agent: Hood grips vary + sprint posture | Other | 55.8 M | 164 k |
| agent: Fix the bubble on the rider's chin | Riders & bikes | 46.9 M | 118 k |
| agent: Kit pickers as tiles with colour swatches | Other | 45.4 M | 92 k |
| agent: Day 14 video (2026-11-24) | Other | 44.8 M | 67 k |
| coordination: yes, a | Other | 42.8 M | 18 k |
| agent: Desktop Sharing screen while bridged | Worlds & terrain | 41.0 M | 106 k |
| agent: Studio 2D map: neighbours, aerial layer, border | Other | 36.7 M | 102 k |
| coordination: simd (a) | Other | 28.1 M | 10 k |
| coordination: Answer to desktop while sharing with a browser: • (c) a simple "sharing" screen | Planning & spec | 26.0 M | 9 k |
| coordination: next question | Planning & spec | 21.9 M | 11 k |
| agent: Studio trust dialog for unknown keys | Other | 21.4 M | 66 k |
| coordination: giVe me an oPen question | Planning & spec | 19.6 M | 9 k |
| agent: Release 0.2.6, all platforms + worlds | Worlds & terrain | 16.1 M | 48 k |
| coordination: a | Other | 12.4 M | 5 k |
| coordination: yes, include border | Other | 12.0 M | 17 k |
| agent: Build caps per kind (Phase 4 Q27 b) | Build, release & infra | 11.6 M | 69 k |
| agent: World patches: .ocwpatch shipping + git folder | Worlds & terrain | 10.4 M | 50 k |
| coordination: a, next | Other | 4.3 M | 9 k |
| coordination: to see the improvents i need a release. do j9 and do a bump and release. | Build, release & infra | 4.2 M | 2 k |
| coordination: b | Other | 3.4 M | 2 k |
| coordination: build option b, but keep a too and vary from time to time. also pay attention on… | Riders & bikes | 3.4 M | 3 k |
| coordination: create a sketch for a and b | Other | 3.4 M | 2 k |
| coordination: yes, a, next | Other | 3.3 M | 2 k |
| coordination: give me an open question | Planning & spec | 2.5 M | 4 k |
| coordination: looks like there is a bubble attached to the chin | Other | 2.0 M | 4 k |
| coordination: is there something waiting to be implemwnted? | Other | 2.0 M | 3 k |
| coordination: p4 q26, keep (a) | Other | 1.7 M | 1 k |
| coordination: give me annopen questiob | Other | 1.7 M | 0 k |
| coordination: did you fix the riders chin? if so, send me a photo | Riders & bikes | 1.2 M | 2 k |
| coordination: elborate 16hq14 | Other | 1.1 M | 5 k |
| coordination: yes, start a build for that | Build, release & infra | 999 k | 3 k |
| coordination: whats j9? | Other | 835 k | 1 k |
| coordination: yes, (a), show the neighboring world, when we have one. what happends when we do… | Worlds & terrain | 650 k | 2 k |
| coordination: make this a habit everytime you build a day video | Build, release & infra | 600 k | 2 k |
| coordination: update the readme of art project, mayke sure to link all data up to now. | Art project | 569 k | 1 k |
| coordination: okay, end the stuck j8 | Other | 563 k | 1 k |
| coordination: 16H Q14: yes, a | Other | 505 k | 0 k |
| coordination: yes | Other | 438 k | 2 k |

## Prompts

39 prompts (full text: [prompts.md](prompts.md)).

| Time | Prompt |
|---|---|
| 05:07 | Answer to desktop while sharing with a browser: 	•	(c) a simple "sharing" screen |
| 08:15 | whats j9? |
| 08:18 | to see the improvents i need a release. do j9 and do a bump and release. |
| 08:21 | give me annopen questiob |
| 08:22 | create a sketch for a and b |
| 08:24 | build option b, but keep a too and vary from time to time. also pay attention on how riders sprint, where they grap and how. add that to the |
| 08:25 | next question |
| 08:59 | p4 q26, keep (a) |
| 09:02 | next question |
| 09:05 | b |
| 09:08 | next question |
| 09:09 | yes, a |
| 12:51 | add a rule: when you do tests, do also vary the characters and the clothes, as well as the bike setzp. |
| 12:51 | giVe me an oPen question |
| 14:10 | next question |
| 14:51 | next question |
| 15:07 | a |
| 15:34 | next question |
| 15:34 | a, next |
| 15:42 | yes, a, next |
| 15:54 | a, next |
| 15:59 | a, next |
| 16:06 | next question |
| 19:35 | okay, end the stuck j8 |
| 19:36 | update the open questions in appendix c |
| 19:36 | yes |
| 19:37 | is there something waiting to be implemwnted? |
| 19:38 | yes, check j9 |
| 19:38 | elborate 16hq14 |
| 19:40 | yes, start a build for that |
| 19:48 | 16H Q14: yes, a |
| 20:02 | did you fix the riders chin? if so, send me a photo |
| 20:10 | looks like there is a bubble attached to the chin |
| 20:26 | i can't find the open questions/appendix in the spec, am i blind? |
| 20:32 | update the readme of art project, mayke sure to link all data up to now. |
| 20:32 | make this a habit everytime you build a day video |
| 20:32 | give me an open question |
| 20:48 | yes, (a), show the neighboring world, when we have one. what happends when we don't have one? |
| 20:50 | yes, include border |

## Features

22 spec versions added, 10 landed by a merge; 6 deploys, 1 releases.

| Spec | Feature | Landed | Check (marge) |
|---|---|---|---|
| 5.81 | Built: the sensor bridge is read in a Web Worker by default | 05:05 `d9bc9fb1` (merge) | – |
| 5.82 | Decided: while the desktop shares its trainer with a browser, it shows a simple *Sharing*… | 05:07 `2c0abf94` | – |
| 5.83 | Built: the desktop's *Sharing* screen | 06:27 `b8572b79` (merge) | ok at 08:54, 1 suites, 2 passed, 0 failed (commit) |
| 5.84 | Decided: Phase 4 Q31 – riders' hands change grip | 08:25 `347c53f8` | – |
| 5.85 | Decided: Phase 4 Q26 – the workshop's part tiles keep showing the gain against the slot's… | 09:00 `3f336a8f` | – |
| 5.86 | Decided: Phase 4 Q27 – the build caps work per kind | 09:05 `d22f8b6b` | – |
| 5.87 | Decided: Phase 4 Q30 – shorts, socks, shoes and gloves are picked from tiles like the par… | 09:09 `b4c2cffc` | – |
| 5.88 | Built: riders hold the road hoods in two grips | 09:44 `9e70227f` (merge) | ok at 09:44, 81 suites, 3517 passed, 0 failed (commit) |
| 5.89 | Built: the build caps per kind | 10:06 `9f32a289` (merge) | ok at 09:31, 81 suites, 3512 passed, 0 failed (commit) |
| 5.90 | Built: shorts, socks, shoes and gloves are picked from tiles | 12:15 `9cbd20cc` (merge) | ok at 12:15, 81 suites, 3526 passed, 0 failed (commit) |
| 5.91 | Built: the sides of a road are as smooth as the road, J9 | 13:17 `89b2322a` (merge) | ok at 13:09 (commit) |
| 5.92 | Decided: 16H Q8 – a world patch's height points win over the road class's gradient limit | 15:07 `06156163` | – |
| 5.93 | Decided: 16H Q9 – a world patch travels as its own file <package>.ocwpatch next to the pa… | 15:34 `bc7469ce` | – |
| 5.94 | Decided: 16H Q10 – the project's own world patches live in git, in worlds/<region>/patche… | 15:42 `e02af7a3` | – |
| 5.95 | Decided: 16H Q11 – a height point snaps to a road within 15 m of the click and its correc… | 15:54 `2ee32aba` | – |
| 5.96 | Decided: 16H Q12 – OCW Studio's 3D camera hovers by default | 15:59 `fe185161` | – |
| 5.97 | Decided: 16H Q14 – OCW Studio asks before opening a world signed by an unknown user key,… | 19:40 `7d97fded` | – |
| 5.98 | Decided: 16H Q15 – OCW Studio's 2D map also draws the neighbouring packages the game join… | 20:48 `65378fb8` | – |
| 5.99 | Built: a world patch travels as its own file <package>.ocwpatch next to the package, its… | 20:55 `37f45eb8` (merge) | – |
| 6.00 | Built: OCW Studio asks with the game's trust dialog before opening a world signed by an u… | 20:57 `c125ae44` (merge) | ok at 22:00, 1 suites, 3 passed, 0 failed (commit) |
| 6.01 | Fixed: no bubble on the rider's chin | 21:27 `21b0f664` (merge) | – |
| 6.02 | Built: OCW Studio's 2D map draws the neighbouring packages the game joins on, dimmed, the… | 22:48 `84be3af7` (merge) | ok at 22:48, 81 suites, 3550 passed, 0 failed (commit) |

Deploys:

- 07:39 marge: `b8572b79` (ok)
- 07:40 leela: `b8572b79` (ok)
- 16:47 marge: `f59c9cb3` (ok)
- 16:49 leela: `f59c9cb3` (ok)
- 22:09 marge: `21b0f664` (ok)
- 22:11 leela: `21b0f664` (ok)

Releases:

- 16:15 v0.2.6 (pre-release)

## Agent jobs

13 jobs (coordinator log agents.jsonl).

| Task | Branch | Start | End | Status | Interrupted | Merged |
|---|---|---|---|---|---|---|
| Day 14 video (2026-11-24) | ad4f94da | 00:08 | 00:57 | merged |  |  |
| B3: WebTransport reading in a Web Worker | a2f92b46 | 01:08 | 05:46 | merged |  |  |
| Desktop Sharing screen while the bridge is paired | ac4538e8 | 05:08 | 06:56 | merged |  |  |
| J9: remaining junction side faults, packages for the release | ab692ee7 | 08:19 | 16:06 | merged |  |  |
| Hood grips vary (draped / handshake) and sprint posture | a035bde7 | 08:25 | 10:41 | merged |  |  |
| Build caps per kind (Phase 4 Q27 b) | acf93870 | 09:06 | 12:03 | merged |  |  |
| Kit pickers as tiles with colour swatches (Phase 4 Q30 a) | a84893a6 | 09:09 | 12:51 | merged |  |  |
| Release 0.2.6, all platforms + J9 worlds | ae2f826c | 13:58 | 16:16 | reported |  |  |
| World patches: .ocwpatch next to the package, official patches in git (16H Q9, Q10) | a074c1ca | 19:39 | 20:56 | merged |  |  |
| Studio trust dialog for unknown user keys (16H Q14 a) | a1428acf | 19:41 | 21:26 | merged |  |  |
| Fix the bubble on the rider's chin | chin | 20:10 |  | started |  |  |
| Fix the bubble on the rider's chin | a7634b60 | 20:10 | 22:09 | merged |  |  |
| Studio 2D map: neighbouring worlds, aerial layer, border (16H Q15 a) | a48a69f9 | 21:27 | 23:18 | merged |  |  |

## Incidents

42 collected (disk-full 1, janitor-delete 29, machine-offline 4, machine-online 3, runs-failed 1, unit-failed 4), 0 with root-cause notes ([incidents.md](incidents.md)).

| Time | Kind | Machine | What |
|---|---|---|---|
| 00:00 | machine-offline | Weela | Weela unreachable (no route to host) |
| 00:00 | machine-offline | Win11Builder | Win11Builder unreachable (no route to host) |
| 05:44 | janitor-delete | leela | janitor delete OCW-merge-b3w/target (32.6 GB) |
| 05:45 | janitor-delete | leela | janitor delete OCW-worktree-agent-a2f92b4653d455fcf/target (11.1 GB) |
| 05:45 | janitor-delete | marge | janitor delete OCW-worktree-agent-a2f92b4653d455fcf/target (43.4 GB) |
| 06:04 | unit-failed | deb | ocw-art-collect.service failed (exit-code) |
| 06:54 | janitor-delete | marge | janitor delete OCW-merge-sharing/target (32.6 GB) |
| 06:55 | janitor-delete | marge | janitor delete OCW-worktree-agent-ac4538e8aa1507e52/target (51.1 GB) |
| 06:55 | janitor-delete | leela | janitor delete OCW-worktree-agent-ac4538e8aa1507e52/target (6.3 GB) |
| 07:04 | unit-failed | deb | ocw-art-collect.service failed (exit-code) |
| 08:03 | unit-failed | deb | ocw-art-collect.service failed (exit-code) |
| 08:37 | machine-online | Win11Builder | Win11Builder back online |
| 08:37 | disk-full | Win11Builder | disk C: on Win11Builder at 96 % |
| 08:40 | machine-offline | Win11Builder | Win11Builder unreachable (ssh error) |
| 08:41 | machine-online | Win11Builder | Win11Builder back online |
| 08:54 | janitor-delete | Win11Builder | janitor delete OCW/target (3.1 GB) |
| 09:02 | unit-failed | deb | ocw-art-collect.service failed (exit-code) |
| 10:39 | janitor-delete | marge | janitor delete OCW-worktree-agent-a035bde700eac4da0/target (37.8 GB) |
| 10:39 | janitor-delete | marge | janitor delete OCW-merge-q31/target (33.2 GB) |
| 12:01 | janitor-delete | leela | janitor delete OCW-merge-q27/target (32.7 GB) |
| 12:01 | janitor-delete | marge | janitor delete OCW-worktree-agent-acf9387027895d279/target (34.2 GB) |
| 12:50 | janitor-delete | marge | janitor delete OCW-merge-q30/target (32.7 GB) |
| 12:50 | janitor-delete | marge | janitor delete OCW-worktree-agent-a84893a6b55005fb9/target (40.7 GB) |
| 13:07 | janitor-delete | Win11Builder | janitor delete OCW-worktree-agent-a84893a6b55005fb9/target (12.8 GB) |
| 13:15 | janitor-delete | macos | janitor delete OCW-worktree-agent-acf9387027895d279/target (6.6 GB) |
| 13:58 | janitor-delete | leela | janitor delete OCW-merge-j9/target (32.7 GB) |
| 16:06 | janitor-delete | marge | janitor delete OCW-worktree-agent-ab692ee78e235e3a6/target (47.5 GB) |
| 16:06 | janitor-delete | leela | janitor delete OCW-worktree-agent-ab692ee78e235e3a6/target (0.5 GB) |
| 20:25 | runs-failed | Weela, Win11Builder, macos, marge | 11 failed remote.sh runs (Weela 1, Win11Builder 3, macos 1, marge 6) |
| 20:55 | janitor-delete | marge | janitor delete OCW-merge-patches/target (32.7 GB) |
| 20:55 | janitor-delete | marge | janitor delete OCW-worktree-agent-a074c1ca91e50f058/target (34.5 GB) |
| 21:12 | machine-offline | Win11Builder | Win11Builder unreachable (timeout) |
| 21:13 | machine-online | Win11Builder | Win11Builder back online |
| 21:25 | janitor-delete | marge | janitor delete OCW-merge-trust/target (32.8 GB) |
| 21:25 | janitor-delete | marge | janitor delete OCW-worktree-agent-a1428acfb0cfceb95/target (7.9 GB) |
| 21:25 | janitor-delete | leela | janitor delete OCW-worktree-agent-a1428acfb0cfceb95/target (39.3 GB) |
| 22:07 | janitor-delete | leela | janitor delete OCW-merge-chin/target (32.7 GB) |
| 22:07 | janitor-delete | leela | janitor delete OCW-worktree-agent-a7634b603eab8e729/target (32.7 GB) |
| 22:07 | janitor-delete | marge | janitor delete OCW-worktree-agent-a7634b603eab8e729/target (8.5 GB) |
| 23:16 | janitor-delete | marge | janitor delete OCW-merge-map/target (32.8 GB) |
| 23:16 | janitor-delete | marge | janitor delete OCW-worktree-agent-a48a69f9733b946da/target (10.2 GB) |
| 23:16 | janitor-delete | leela | janitor delete OCW-worktree-agent-a48a69f9733b946da/target (32.8 GB) |

## Media

| Time | File |
|---|---|
| 01:53:29 | [015329-web-b3w-web-mp-f0-off.jpg](015329-web-b3w-web-mp-f0-off.jpg) |
| 01:54:15 | [015415-web-b3w-web-mp-f0-auto.jpg](015415-web-b3w-web-mp-f0-auto.jpg) |
| 01:55:00 | [015500-web-b3w-web-mp-f40-off.jpg](015500-web-b3w-web-mp-f40-off.jpg) |
| 01:55:48 | [015548-web-b3w-web-mp-f40-auto.jpg](015548-web-b3w-web-mp-f40-auto.jpg) |
| 01:56:35 | [015635-web-b3w-web-mp-refuse.jpg](015635-web-b3w-web-mp-refuse.jpg) |
| 02:03:08 | [020308-web-b3w-rounds-web-mp-r1-f40-auto.jpg](020308-web-b3w-rounds-web-mp-r1-f40-auto.jpg) |
| 02:03:56 | [020356-web-b3w-rounds-web-mp-r1-f40-off.jpg](020356-web-b3w-rounds-web-mp-r1-f40-off.jpg) |
| 02:04:43 | [020443-web-b3w-rounds-web-mp-r1-f0-auto.jpg](020443-web-b3w-rounds-web-mp-r1-f0-auto.jpg) |
| 02:05:28 | [020528-web-b3w-rounds-web-mp-r1-f0-off.jpg](020528-web-b3w-rounds-web-mp-r1-f0-off.jpg) |
| 02:06:14 | [020614-web-b3w-rounds-web-mp-r2-f40-auto.jpg](020614-web-b3w-rounds-web-mp-r2-f40-auto.jpg) |
| 02:07:01 | [020701-web-b3w-rounds-web-mp-r2-f40-off.jpg](020701-web-b3w-rounds-web-mp-r2-f40-off.jpg) |
| 02:07:48 | [020748-web-b3w-rounds-web-mp-r2-f0-auto.jpg](020748-web-b3w-rounds-web-mp-r2-f0-auto.jpg) |
| 02:08:34 | [020834-web-b3w-rounds-web-mp-r2-f0-off.jpg](020834-web-b3w-rounds-web-mp-r2-f0-off.jpg) |
| 02:09:20 | [020920-web-b3w-rounds-web-mp-r3-f40-auto.jpg](020920-web-b3w-rounds-web-mp-r3-f40-auto.jpg) |
| 02:10:07 | [021007-web-b3w-rounds-web-mp-r3-f40-off.jpg](021007-web-b3w-rounds-web-mp-r3-f40-off.jpg) |
| 02:10:54 | [021054-web-b3w-rounds-web-mp-r3-f0-auto.jpg](021054-web-b3w-rounds-web-mp-r3-f0-auto.jpg) |
| 02:11:39 | [021139-web-b3w-rounds-web-mp-r3-f0-off.jpg](021139-web-b3w-rounds-web-mp-r3-f0-off.jpg) |
| 02:27:32 | [022732-bridge-bridge-browser-menu.jpg](022732-bridge-bridge-browser-menu.jpg) |
| 02:27:32 | [022732-bridge-bridge-browser-riding-late.jpg](022732-bridge-bridge-browser-riding-late.jpg) |
| 02:27:32 | [022732-bridge-bridge-browser-riding.jpg](022732-bridge-bridge-browser-riding.jpg) |
| 02:27:32 | [022732-bridge-bridge-desktop.jpg](022732-bridge-bridge-desktop.jpg) |
| 02:34:02 | [023402-web-b3w-video-web-mp-video-f40-worker.jpg](023402-web-b3w-video-web-mp-video-f40-worker.jpg) |
| 02:34:02 | [023402-web-b3w-video-web-mp-video-f40-worker.mp4](023402-web-b3w-video-web-mp-video-f40-worker.mp4) |
| 02:40:19 | [024019-web-b3w-rounds2-web-mp-r1-f40-auto.jpg](024019-web-b3w-rounds2-web-mp-r1-f40-auto.jpg) |
| 02:41:06 | [024106-web-b3w-rounds2-web-mp-r1-f40-off.jpg](024106-web-b3w-rounds2-web-mp-r1-f40-off.jpg) |
| 02:41:53 | [024153-web-b3w-rounds2-web-mp-r1-f0-auto.jpg](024153-web-b3w-rounds2-web-mp-r1-f0-auto.jpg) |
| 02:42:38 | [024238-web-b3w-rounds2-web-mp-r1-f0-off.jpg](024238-web-b3w-rounds2-web-mp-r1-f0-off.jpg) |
| 02:43:24 | [024324-web-b3w-rounds2-web-mp-r2-f40-auto.jpg](024324-web-b3w-rounds2-web-mp-r2-f40-auto.jpg) |
| 02:44:11 | [024411-web-b3w-rounds2-web-mp-r2-f40-off.jpg](024411-web-b3w-rounds2-web-mp-r2-f40-off.jpg) |
| 02:44:59 | [024459-web-b3w-rounds2-web-mp-r2-f0-auto.jpg](024459-web-b3w-rounds2-web-mp-r2-f0-auto.jpg) |
| 02:45:44 | [024544-web-b3w-rounds2-web-mp-r2-f0-off.jpg](024544-web-b3w-rounds2-web-mp-r2-f0-off.jpg) |
| 02:46:30 | [024630-web-b3w-rounds2-web-mp-r3-f40-auto.jpg](024630-web-b3w-rounds2-web-mp-r3-f40-auto.jpg) |
| 02:47:17 | [024717-web-b3w-rounds2-web-mp-r3-f40-off.jpg](024717-web-b3w-rounds2-web-mp-r3-f40-off.jpg) |
| 02:48:05 | [024805-web-b3w-rounds2-web-mp-r3-f0-auto.jpg](024805-web-b3w-rounds2-web-mp-r3-f0-auto.jpg) |
| 02:48:50 | [024850-web-b3w-rounds2-web-mp-r3-f0-off.jpg](024850-web-b3w-rounds2-web-mp-r3-f0-off.jpg) |
| 02:54:19 | [025419-bridge-bridge-browser-menu.jpg](025419-bridge-bridge-browser-menu.jpg) |
| 02:54:19 | [025419-bridge-bridge-browser-riding-late.jpg](025419-bridge-bridge-browser-riding-late.jpg) |
| 02:54:19 | [025419-bridge-bridge-browser-riding.jpg](025419-bridge-bridge-browser-riding.jpg) |
| 02:54:19 | [025419-bridge-bridge-desktop.jpg](025419-bridge-bridge-desktop.jpg) |
| 03:02:58 | [030258-web-b3w-diag-web-mp-r1-f40-auto.jpg](030258-web-b3w-diag-web-mp-r1-f40-auto.jpg) |
| 03:03:45 | [030345-web-b3w-diag-web-mp-r1-f40-off.jpg](030345-web-b3w-diag-web-mp-r1-f40-off.jpg) |
| 03:04:32 | [030432-web-b3w-diag-web-mp-r2-f40-auto.jpg](030432-web-b3w-diag-web-mp-r2-f40-auto.jpg) |
| 03:05:20 | [030520-web-b3w-diag-web-mp-r2-f40-off.jpg](030520-web-b3w-diag-web-mp-r2-f40-off.jpg) |
| 03:13:15 | [031315-web-b3w-final-web-mp-r1-f40-auto.jpg](031315-web-b3w-final-web-mp-r1-f40-auto.jpg) |
| 03:14:02 | [031402-web-b3w-final-web-mp-r1-f40-off.jpg](031402-web-b3w-final-web-mp-r1-f40-off.jpg) |
| 03:14:49 | [031449-web-b3w-final-web-mp-r1-f0-auto.jpg](031449-web-b3w-final-web-mp-r1-f0-auto.jpg) |
| 03:15:35 | [031535-web-b3w-final-web-mp-r1-f0-off.jpg](031535-web-b3w-final-web-mp-r1-f0-off.jpg) |
| 03:16:20 | [031620-web-b3w-final-web-mp-r2-f40-auto.jpg](031620-web-b3w-final-web-mp-r2-f40-auto.jpg) |
| 03:17:08 | [031708-web-b3w-final-web-mp-r2-f40-off.jpg](031708-web-b3w-final-web-mp-r2-f40-off.jpg) |
| 03:17:55 | [031755-web-b3w-final-web-mp-r2-f0-auto.jpg](031755-web-b3w-final-web-mp-r2-f0-auto.jpg) |
| 03:18:41 | [031841-web-b3w-final-web-mp-r2-f0-off.jpg](031841-web-b3w-final-web-mp-r2-f0-off.jpg) |
| 03:19:27 | [031927-web-b3w-final-web-mp-r3-f40-auto.jpg](031927-web-b3w-final-web-mp-r3-f40-auto.jpg) |
| 03:20:14 | [032014-web-b3w-final-web-mp-r3-f40-off.jpg](032014-web-b3w-final-web-mp-r3-f40-off.jpg) |
| 03:21:02 | [032102-web-b3w-final-web-mp-r3-f0-auto.jpg](032102-web-b3w-final-web-mp-r3-f0-auto.jpg) |
| 03:21:47 | [032147-web-b3w-final-web-mp-r3-f0-off.jpg](032147-web-b3w-final-web-mp-r3-f0-off.jpg) |
| 03:22:33 | [032233-web-b3w-final-web-mp-refuse.jpg](032233-web-b3w-final-web-mp-refuse.jpg) |
| 03:22:58 | [032258-web-b3w-final-web-mp-video-f40-worker.jpg](032258-web-b3w-final-web-mp-video-f40-worker.jpg) |
| 03:22:58 | [032258-web-b3w-final-web-mp-video-f40-worker.mp4](032258-web-b3w-final-web-mp-video-f40-worker.mp4) |
| 03:28:16 | [032816-bridge-bridge-browser-menu.jpg](032816-bridge-bridge-browser-menu.jpg) |
| 03:28:16 | [032816-bridge-bridge-browser-riding-late.jpg](032816-bridge-bridge-browser-riding-late.jpg) |
| 03:28:16 | [032816-bridge-bridge-browser-riding.jpg](032816-bridge-bridge-browser-riding.jpg) |
| 03:28:16 | [032816-bridge-bridge-desktop.jpg](032816-bridge-bridge-desktop.jpg) |
| 03:50:04 | [035004-web-web-webkit-iphone-hints.png](035004-web-web-webkit-iphone-hints.png) |
| 03:50:04 | [035004-web-web-webkit-iphone-hold.png](035004-web-web-webkit-iphone-hold.png) |
| 03:50:04 | [035004-web-web-webkit-iphone-landscape-hints.png](035004-web-web-webkit-iphone-landscape-hints.png) |
| 03:50:04 | [035004-web-web-webkit-iphone-landscape-hold.png](035004-web-web-webkit-iphone-landscape-hold.png) |
| 03:50:04 | [035004-web-web-webkit-iphone-landscape-riding.png](035004-web-web-webkit-iphone-landscape-riding.png) |
| 03:50:04 | [035004-web-web-webkit-iphone-landscape-stopped.png](035004-web-web-webkit-iphone-landscape-stopped.png) |
| 03:50:04 | [035004-web-web-webkit-iphone-landscape.png](035004-web-web-webkit-iphone-landscape.png) |
| 03:50:04 | [035004-web-web-webkit-iphone-riding.png](035004-web-web-webkit-iphone-riding.png) |
| 03:50:04 | [035004-web-web-webkit-iphone-start.png](035004-web-web-webkit-iphone-start.png) |
| 03:50:04 | [035004-web-web-webkit-iphone-stopped.png](035004-web-web-webkit-iphone-stopped.png) |
| 03:50:04 | [035004-web-web-webkit-iphone.png](035004-web-web-webkit-iphone.png) |
| 03:50:04 | [035004-web-web-webkit-layout-android-360x640.png](035004-web-web-webkit-layout-android-360x640.png) |
| 03:50:04 | [035004-web-web-webkit-layout-android-640x360.png](035004-web-web-webkit-layout-android-640x360.png) |
| 03:50:04 | [035004-web-web-webkit-layout-iphone-390x844.png](035004-web-web-webkit-layout-iphone-390x844.png) |
| 03:50:04 | [035004-web-web-webkit-layout-iphone-844x390.png](035004-web-web-webkit-layout-iphone-844x390.png) |
| 03:50:04 | [035004-web-web-webkit-mac.png](035004-web-web-webkit-mac.png) |
| 03:50:04 | [035004-web-web-webkit-too-old-ride.png](035004-web-web-webkit-too-old-ride.png) |
| 04:11:03 | [041103-bridge-bridge-browser-menu.jpg](041103-bridge-bridge-browser-menu.jpg) |
| 04:11:03 | [041103-bridge-bridge-browser-riding-late.jpg](041103-bridge-bridge-browser-riding-late.jpg) |
| 04:11:03 | [041103-bridge-bridge-browser-riding.jpg](041103-bridge-bridge-browser-riding.jpg) |
| 04:11:03 | [041103-bridge-bridge-desktop.jpg](041103-bridge-bridge-desktop.jpg) |
| 04:12:49 | [041249-web-b3w-final2-web-mp.jpg](041249-web-b3w-final2-web-mp.jpg) |
| 04:13:25 | [041325-web-b3w-final2-web-mp-refuse.jpg](041325-web-b3w-final2-web-mp-refuse.jpg) |
| 04:22:02 | [042202-web-b3w-fix-web-mp-r1-f40-auto.jpg](042202-web-b3w-fix-web-mp-r1-f40-auto.jpg) |
| 04:22:49 | [042249-web-b3w-fix-web-mp-r1-f40-off.jpg](042249-web-b3w-fix-web-mp-r1-f40-off.jpg) |
| 04:23:37 | [042337-web-b3w-fix-web-mp-r1-f0-auto.jpg](042337-web-b3w-fix-web-mp-r1-f0-auto.jpg) |
| 04:24:22 | [042422-web-b3w-fix-web-mp-r1-f0-off.jpg](042422-web-b3w-fix-web-mp-r1-f0-off.jpg) |
| 04:25:08 | [042508-web-b3w-fix-web-mp-r2-f40-auto.jpg](042508-web-b3w-fix-web-mp-r2-f40-auto.jpg) |
| 04:25:56 | [042556-web-b3w-fix-web-mp-r2-f40-off.jpg](042556-web-b3w-fix-web-mp-r2-f40-off.jpg) |
| 04:26:43 | [042643-web-b3w-fix-web-mp-r2-f0-auto.jpg](042643-web-b3w-fix-web-mp-r2-f0-auto.jpg) |
| 04:27:29 | [042729-web-b3w-fix-web-mp-r2-f0-off.jpg](042729-web-b3w-fix-web-mp-r2-f0-off.jpg) |
| 04:28:14 | [042814-web-b3w-fix-web-mp-r3-f40-auto.jpg](042814-web-b3w-fix-web-mp-r3-f40-auto.jpg) |
| 04:29:02 | [042902-web-b3w-fix-web-mp-r3-f40-off.jpg](042902-web-b3w-fix-web-mp-r3-f40-off.jpg) |
| 04:29:49 | [042949-web-b3w-fix-web-mp-r3-f0-auto.jpg](042949-web-b3w-fix-web-mp-r3-f0-auto.jpg) |
| 04:30:35 | [043035-web-b3w-fix-web-mp-r3-f0-off.jpg](043035-web-b3w-fix-web-mp-r3-f0-off.jpg) |
| 04:40:25 | [044025-web-web-webkit-iphone-hints.png](044025-web-web-webkit-iphone-hints.png) |
| 04:40:25 | [044025-web-web-webkit-iphone-hold.png](044025-web-web-webkit-iphone-hold.png) |
| 04:40:25 | [044025-web-web-webkit-iphone-landscape-hints.png](044025-web-web-webkit-iphone-landscape-hints.png) |
| 04:40:25 | [044025-web-web-webkit-iphone-landscape-hold.png](044025-web-web-webkit-iphone-landscape-hold.png) |
| 04:40:25 | [044025-web-web-webkit-iphone-landscape-riding.png](044025-web-web-webkit-iphone-landscape-riding.png) |
| 04:40:25 | [044025-web-web-webkit-iphone-landscape-stopped.png](044025-web-web-webkit-iphone-landscape-stopped.png) |
| 04:40:25 | [044025-web-web-webkit-iphone-landscape.png](044025-web-web-webkit-iphone-landscape.png) |
| 04:40:25 | [044025-web-web-webkit-iphone-riding.png](044025-web-web-webkit-iphone-riding.png) |
| 04:40:25 | [044025-web-web-webkit-iphone-stopped.png](044025-web-web-webkit-iphone-stopped.png) |
| 04:40:25 | [044025-web-web-webkit-iphone.png](044025-web-web-webkit-iphone.png) |
| 04:40:25 | [044025-web-web-webkit-layout-android-360x640.png](044025-web-web-webkit-layout-android-360x640.png) |
| 04:40:25 | [044025-web-web-webkit-layout-android-640x360.png](044025-web-web-webkit-layout-android-640x360.png) |
| 04:40:25 | [044025-web-web-webkit-layout-iphone-390x844.png](044025-web-web-webkit-layout-iphone-390x844.png) |
| 04:40:25 | [044025-web-web-webkit-layout-iphone-844x390.png](044025-web-web-webkit-layout-iphone-844x390.png) |
| 04:40:25 | [044025-web-web-webkit-mac.png](044025-web-web-webkit-mac.png) |
| 04:56:17 | [045617-web-web-mp.jpg](045617-web-web-mp.jpg) |
| 05:01:37 | [050137-bridge-bridge-browser-menu.jpg](050137-bridge-bridge-browser-menu.jpg) |
| 05:01:37 | [050137-bridge-bridge-browser-riding-late.jpg](050137-bridge-bridge-browser-riding-late.jpg) |
| 05:01:37 | [050137-bridge-bridge-browser-riding.jpg](050137-bridge-bridge-browser-riding.jpg) |
| 05:01:37 | [050137-bridge-bridge-desktop.jpg](050137-bridge-bridge-desktop.jpg) |
| 05:03:23 | [050323-web-b3w-optin-web-mp-on.jpg](050323-web-b3w-optin-web-mp-on.jpg) |
| 05:03:49 | [050349-web-b3w-optin-web-mp-refuse.jpg](050349-web-b3w-optin-web-mp-refuse.jpg) |
| 05:55:54 | [055554-bridge-bridge-browser-menu.jpg](055554-bridge-bridge-browser-menu.jpg) |
| 05:55:54 | [055554-bridge-bridge-browser-riding-late.jpg](055554-bridge-bridge-browser-riding-late.jpg) |
| 05:55:54 | [055554-bridge-bridge-browser-riding.jpg](055554-bridge-bridge-browser-riding.jpg) |
| 05:55:54 | [055554-bridge-bridge-desktop-015s.jpg](055554-bridge-bridge-desktop-015s.jpg) |
| 05:55:54 | [055554-bridge-bridge-desktop-030s.jpg](055554-bridge-bridge-desktop-030s.jpg) |
| 05:55:54 | [055554-bridge-bridge-desktop-045s.jpg](055554-bridge-bridge-desktop-045s.jpg) |
| 05:55:54 | [055554-bridge-bridge-desktop-060s.jpg](055554-bridge-bridge-desktop-060s.jpg) |
| 05:55:54 | [055554-bridge-bridge-desktop-075s.jpg](055554-bridge-bridge-desktop-075s.jpg) |
| 05:55:54 | [055554-bridge-bridge-desktop-090s.jpg](055554-bridge-bridge-desktop-090s.jpg) |
| 05:55:54 | [055554-bridge-bridge-desktop-105s.jpg](055554-bridge-bridge-desktop-105s.jpg) |
| 05:55:54 | [055554-bridge-bridge-desktop-120s.jpg](055554-bridge-bridge-desktop-120s.jpg) |
| 05:55:54 | [055554-bridge-bridge-desktop-135s.jpg](055554-bridge-bridge-desktop-135s.jpg) |
| 05:55:54 | [055554-bridge-bridge-desktop-150s.jpg](055554-bridge-bridge-desktop-150s.jpg) |
| 05:55:54 | [055554-bridge-bridge-desktop-165s.jpg](055554-bridge-bridge-desktop-165s.jpg) |
| 05:55:54 | [055554-bridge-bridge-desktop-180s.jpg](055554-bridge-bridge-desktop-180s.jpg) |
| 05:55:54 | [055554-bridge-bridge-desktop-195s.jpg](055554-bridge-bridge-desktop-195s.jpg) |
| 05:55:54 | [055554-bridge-bridge-desktop.jpg](055554-bridge-bridge-desktop.jpg) |
| 06:13:19 | [061319-bridge-bridge-browser-menu.jpg](061319-bridge-bridge-browser-menu.jpg) |
| 06:13:19 | [061319-bridge-bridge-browser-riding-late.jpg](061319-bridge-bridge-browser-riding-late.jpg) |
| 06:13:19 | [061319-bridge-bridge-browser-riding.jpg](061319-bridge-bridge-browser-riding.jpg) |
| 06:13:19 | [061319-bridge-bridge-desktop-015s.jpg](061319-bridge-bridge-desktop-015s.jpg) |
| 06:13:19 | [061319-bridge-bridge-desktop-030s.jpg](061319-bridge-bridge-desktop-030s.jpg) |
| 06:13:19 | [061319-bridge-bridge-desktop-045s.jpg](061319-bridge-bridge-desktop-045s.jpg) |
| 06:13:19 | [061319-bridge-bridge-desktop-060s.jpg](061319-bridge-bridge-desktop-060s.jpg) |
| 06:13:19 | [061319-bridge-bridge-desktop-075s.jpg](061319-bridge-bridge-desktop-075s.jpg) |
| 06:13:19 | [061319-bridge-bridge-desktop-090s.jpg](061319-bridge-bridge-desktop-090s.jpg) |
| 06:13:19 | [061319-bridge-bridge-desktop-105s.jpg](061319-bridge-bridge-desktop-105s.jpg) |
| 06:13:19 | [061319-bridge-bridge-desktop-120s.jpg](061319-bridge-bridge-desktop-120s.jpg) |
| 06:13:19 | [061319-bridge-bridge-desktop-135s.jpg](061319-bridge-bridge-desktop-135s.jpg) |
| 06:13:19 | [061319-bridge-bridge-desktop-150s.jpg](061319-bridge-bridge-desktop-150s.jpg) |
| 06:13:19 | [061319-bridge-bridge-desktop-165s.jpg](061319-bridge-bridge-desktop-165s.jpg) |
| 06:13:19 | [061319-bridge-bridge-desktop-180s.jpg](061319-bridge-bridge-desktop-180s.jpg) |
| 06:13:19 | [061319-bridge-bridge-desktop-195s.jpg](061319-bridge-bridge-desktop-195s.jpg) |
| 06:13:19 | [061319-bridge-bridge-desktop.jpg](061319-bridge-bridge-desktop.jpg) |
| 09:06:14 | [090614-347c53f8-dirty-shot-ocw.jpg](090614-347c53f8-dirty-shot-ocw.jpg) |
| 09:06:23 | [090623-347c53f8-dirty-shot-wayland-ocw-wayland.jpg](090623-347c53f8-dirty-shot-wayland-ocw-wayland.jpg) |
| 09:09:00 | [090900-347c53f8-dirty-shot-wayland-q31-draped-side.jpg](090900-347c53f8-dirty-shot-wayland-q31-draped-side.jpg) |
| 09:15:09 | [091509-347c53f8-dirty-shot-wayland-q31-draped-above.jpg](091509-347c53f8-dirty-shot-wayland-q31-draped-above.jpg) |
| 09:15:17 | [091517-347c53f8-dirty-shot-wayland-q31-handshake-side.jpg](091517-347c53f8-dirty-shot-wayland-q31-handshake-side.jpg) |
| 09:15:25 | [091525-347c53f8-dirty-shot-wayland-q31-handshake-front.jpg](091525-347c53f8-dirty-shot-wayland-q31-handshake-front.jpg) |
| 09:15:34 | [091534-347c53f8-dirty-shot-wayland-q31-handshake-above.jpg](091534-347c53f8-dirty-shot-wayland-q31-handshake-above.jpg) |
| 09:15:42 | [091542-347c53f8-dirty-shot-wayland-q31-sprint-drops-side.jpg](091542-347c53f8-dirty-shot-wayland-q31-sprint-drops-side.jpg) |
| 09:15:50 | [091550-347c53f8-dirty-shot-wayland-q31-sprint-body.jpg](091550-347c53f8-dirty-shot-wayland-q31-sprint-body.jpg) |
| 09:15:59 | [091559-347c53f8-dirty-shot-wayland-q31-sprint-front.jpg](091559-347c53f8-dirty-shot-wayland-q31-sprint-front.jpg) |
| 09:16:48 | [091648-347c53f8-dirty-video-wayland-q31-grip-then-sprint-video.jpg](091648-347c53f8-dirty-video-wayland-q31-grip-then-sprint-video.jpg) |
| 09:16:48 | [091648-347c53f8-dirty-video-wayland-q31-grip-then-sprint-video.mp4](091648-347c53f8-dirty-video-wayland-q31-grip-then-sprint-video.mp4) |
| 09:26:35 | [092635-j9-sides-li-letzanaweg-corner-j8.jpg](092635-j9-sides-li-letzanaweg-corner-j8.jpg) |
| 09:26:50 | [092650-j9-sides-li-letzanaweg-side-j8.jpg](092650-j9-sides-li-letzanaweg-side-j8.jpg) |
| 09:27:06 | [092706-j9-sides-li-t-j8.jpg](092706-j9-sides-li-t-j8.jpg) |
| 09:27:22 | [092722-j9-sides-li-fork-j8.jpg](092722-j9-sides-li-fork-j8.jpg) |
| 09:27:48 | [092748-j9-sides-bf-path-j8.jpg](092748-j9-sides-bf-path-j8.jpg) |
| 09:28:04 | [092804-j9-sides-li-j8-run4721-j8.jpg](092804-j9-sides-li-j8-run4721-j8.jpg) |
| 09:28:19 | [092819-j9-sides-li-j8-run4792-j8.jpg](092819-j9-sides-li-j8-run4792-j8.jpg) |
| 09:28:33 | [092833-j9-sides-li-j8-fix3392-j8.jpg](092833-j9-sides-li-j8-fix3392-j8.jpg) |
| 09:28:48 | [092848-j9-sides-li-j9-fix2009-j8.jpg](092848-j9-sides-li-j9-fix2009-j8.jpg) |
| 09:29:03 | [092903-j9-sides-li-j9-fix5952-j8.jpg](092903-j9-sides-li-j9-fix5952-j8.jpg) |
| 09:29:18 | [092918-j9-sides-li-j9-fix2716-j8.jpg](092918-j9-sides-li-j9-fix2716-j8.jpg) |
| 09:29:33 | [092933-j9-sides-li-j9-fix966-j8.jpg](092933-j9-sides-li-j9-fix966-j8.jpg) |
| 09:29:48 | [092948-j9-sides-li-j9-fix617-j8.jpg](092948-j9-sides-li-j9-fix617-j8.jpg) |
| 09:30:04 | [093004-j9-sides-li-j9-fix483-j8.jpg](093004-j9-sides-li-j9-fix483-j8.jpg) |
| 09:37:44 | [093744-9b0e9139-dirty-shot-wayland-q31-sprint-drops-side.jpg](093744-9b0e9139-dirty-shot-wayland-q31-sprint-drops-side.jpg) |
| 09:37:53 | [093753-9b0e9139-dirty-shot-wayland-q31-sprint-body.jpg](093753-9b0e9139-dirty-shot-wayland-q31-sprint-body.jpg) |
| 09:39:01 | [093901-9b0e9139-dirty-video-wayland-q31-grip-then-sprint-video.jpg](093901-9b0e9139-dirty-video-wayland-q31-grip-then-sprint-video.jpg) |
| 09:39:01 | [093901-9b0e9139-dirty-video-wayland-q31-grip-then-sprint-video.mp4](093901-9b0e9139-dirty-video-wayland-q31-grip-then-sprint-video.mp4) |
| 09:39:45 | [093945-d22f8b6b-dirty-shot-wayland-bike-stand-tiles-capped.jpg](093945-d22f8b6b-dirty-shot-wayland-bike-stand-tiles-capped.jpg) |
| 10:04:26 | [100426-cba2f214-shot-ocw.jpg](100426-cba2f214-shot-ocw.jpg) |
| 10:04:35 | [100435-cba2f214-shot-wayland-ocw-wayland.jpg](100435-cba2f214-shot-wayland-ocw-wayland.jpg) |
| 10:05:02 | [100502-cba2f214-shot-wayland-bike-stand-tiles-capped.jpg](100502-cba2f214-shot-wayland-bike-stand-tiles-capped.jpg) |
| 10:48:17 | [104817-j9-sides-li-fork-j9.jpg](104817-j9-sides-li-fork-j9.jpg) |
| 10:48:17 | [104817-j9-sides-li-j8-fix3392-j9.jpg](104817-j9-sides-li-j8-fix3392-j9.jpg) |
| 10:48:17 | [104817-j9-sides-li-j8-run4721-j9.jpg](104817-j9-sides-li-j8-run4721-j9.jpg) |
| 10:48:17 | [104817-j9-sides-li-j8-run4792-j9.jpg](104817-j9-sides-li-j8-run4792-j9.jpg) |
| 10:48:17 | [104817-j9-sides-li-j9-fix2009-j9.jpg](104817-j9-sides-li-j9-fix2009-j9.jpg) |
| 10:48:17 | [104817-j9-sides-li-j9-fix2716-j9.jpg](104817-j9-sides-li-j9-fix2716-j9.jpg) |
| 10:48:17 | [104817-j9-sides-li-j9-fix483-j9.jpg](104817-j9-sides-li-j9-fix483-j9.jpg) |
| 10:48:17 | [104817-j9-sides-li-j9-fix5952-j9.jpg](104817-j9-sides-li-j9-fix5952-j9.jpg) |
| 10:48:17 | [104817-j9-sides-li-j9-fix617-j9.jpg](104817-j9-sides-li-j9-fix617-j9.jpg) |
| 10:48:17 | [104817-j9-sides-li-j9-fix966-j9.jpg](104817-j9-sides-li-j9-fix966-j9.jpg) |
| 10:48:17 | [104817-j9-sides-li-letzanaweg-corner-j9.jpg](104817-j9-sides-li-letzanaweg-corner-j9.jpg) |
| 10:48:17 | [104817-j9-sides-li-letzanaweg-side-j9.jpg](104817-j9-sides-li-letzanaweg-side-j9.jpg) |
| 10:48:17 | [104817-j9-sides-li-t-j9.jpg](104817-j9-sides-li-t-j9.jpg) |
| 11:17:28 | [111728-j9-smoke-7f4cebf5-dirty-shot-ocw.jpg](111728-j9-smoke-7f4cebf5-dirty-shot-ocw.jpg) |
| 11:17:38 | [111738-j9-smoke-7f4cebf5-dirty-shot-wayland-ocw-wayland.jpg](111738-j9-smoke-7f4cebf5-dirty-shot-wayland-ocw-wayland.jpg) |
| 11:24:38 | [112438-3940bcb3-shot-wayland-workshop-gloves-colour.jpg](112438-3940bcb3-shot-wayland-workshop-gloves-colour.jpg) |
| 11:25:03 | [112503-3940bcb3-shot-wayland-workshop-gloves-colour-phone.jpg](112503-3940bcb3-shot-wayland-workshop-gloves-colour-phone.jpg) |
| 11:25:29 | [112529-3940bcb3-shot-wayland-workshop-shorts-colour.jpg](112529-3940bcb3-shot-wayland-workshop-shorts-colour.jpg) |
| 11:25:54 | [112554-3940bcb3-shot-wayland-workshop-socks-tiles.jpg](112554-3940bcb3-shot-wayland-workshop-socks-tiles.jpg) |
| 11:26:19 | [112619-3940bcb3-shot-wayland-workshop-shoes-colour.jpg](112619-3940bcb3-shot-wayland-workshop-shoes-colour.jpg) |
| 11:28:14 | [112814-j9-sides-bf-path-j9.jpg](112814-j9-sides-bf-path-j9.jpg) |
| 11:52:28 | [115228-3940bcb3-shot-ocw.jpg](115228-3940bcb3-shot-ocw.jpg) |
| 11:52:37 | [115237-3940bcb3-shot-wayland-ocw-wayland.jpg](115237-3940bcb3-shot-wayland-ocw-wayland.jpg) |
| 11:53:08 | [115308-3940bcb3-dirty-shot-wayland-workshop-gloves-colour.jpg](115308-3940bcb3-dirty-shot-wayland-workshop-gloves-colour.jpg) |
| 11:53:33 | [115333-3940bcb3-dirty-shot-wayland-workshop-gloves-colour-phone.jpg](115333-3940bcb3-dirty-shot-wayland-workshop-gloves-colour-phone.jpg) |
| 11:53:59 | [115359-3940bcb3-dirty-shot-wayland-workshop-shorts-colour.jpg](115359-3940bcb3-dirty-shot-wayland-workshop-shorts-colour.jpg) |
| 11:54:24 | [115424-3940bcb3-dirty-shot-wayland-workshop-socks-tiles.jpg](115424-3940bcb3-dirty-shot-wayland-workshop-socks-tiles.jpg) |
| 11:54:50 | [115450-3940bcb3-dirty-shot-wayland-workshop-shoes-colour.jpg](115450-3940bcb3-dirty-shot-wayland-workshop-shoes-colour.jpg) |
| 11:58:17 | [115817-0829ea18-shot-wayland-workshop-gloves-colour.jpg](115817-0829ea18-shot-wayland-workshop-gloves-colour.jpg) |
| 11:58:42 | [115842-0829ea18-shot-wayland-workshop-gloves-colour-phone.jpg](115842-0829ea18-shot-wayland-workshop-gloves-colour-phone.jpg) |
| 11:59:08 | [115908-0829ea18-shot-wayland-workshop-shorts-colour.jpg](115908-0829ea18-shot-wayland-workshop-shorts-colour.jpg) |
| 11:59:33 | [115933-0829ea18-shot-wayland-workshop-socks-tiles.jpg](115933-0829ea18-shot-wayland-workshop-socks-tiles.jpg) |
| 11:59:59 | [115959-0829ea18-shot-wayland-workshop-shoes-colour.jpg](115959-0829ea18-shot-wayland-workshop-shoes-colour.jpg) |
| 12:38:37 | [123837-j9-plans-fix2009-j9.png](123837-j9-plans-fix2009-j9.png) |
| 12:44:47 | [124447-j9-plans-fix2009-j8.png](124447-j9-plans-fix2009-j8.png) |
| 13:08:31 | [130831-j9-sides-li-fork-j9.jpg](130831-j9-sides-li-fork-j9.jpg) |
| 13:08:31 | [130831-j9-sides-li-j8-fix3392-j9.jpg](130831-j9-sides-li-j8-fix3392-j9.jpg) |
| 13:08:31 | [130831-j9-sides-li-j8-run4721-j9.jpg](130831-j9-sides-li-j8-run4721-j9.jpg) |
| 13:08:31 | [130831-j9-sides-li-j8-run4792-j9.jpg](130831-j9-sides-li-j8-run4792-j9.jpg) |
| 13:08:31 | [130831-j9-sides-li-j9-fix2009-j9.jpg](130831-j9-sides-li-j9-fix2009-j9.jpg) |
| 13:08:31 | [130831-j9-sides-li-j9-fix2716-j9.jpg](130831-j9-sides-li-j9-fix2716-j9.jpg) |
| 13:08:31 | [130831-j9-sides-li-j9-fix483-j9.jpg](130831-j9-sides-li-j9-fix483-j9.jpg) |
| 13:08:31 | [130831-j9-sides-li-j9-fix5952-j9.jpg](130831-j9-sides-li-j9-fix5952-j9.jpg) |
| 13:08:31 | [130831-j9-sides-li-j9-fix617-j9.jpg](130831-j9-sides-li-j9-fix617-j9.jpg) |
| 13:08:31 | [130831-j9-sides-li-j9-fix966-j9.jpg](130831-j9-sides-li-j9-fix966-j9.jpg) |
| 13:08:31 | [130831-j9-sides-li-letzanaweg-corner-j9.jpg](130831-j9-sides-li-letzanaweg-corner-j9.jpg) |
| 13:08:31 | [130831-j9-sides-li-letzanaweg-side-j9.jpg](130831-j9-sides-li-letzanaweg-side-j9.jpg) |
| 13:08:31 | [130831-j9-sides-li-t-j9.jpg](130831-j9-sides-li-t-j9.jpg) |
| 14:38:36 | [143836-2026-11-25-release-0.2.6-windows-icon-ocw-desktop-128.png](143836-2026-11-25-release-0.2.6-windows-icon-ocw-desktop-128.png) |
| 14:38:36 | [143836-2026-11-25-release-0.2.6-windows-icon-ocw-desktop-16.png](143836-2026-11-25-release-0.2.6-windows-icon-ocw-desktop-16.png) |
| 14:38:36 | [143836-2026-11-25-release-0.2.6-windows-icon-ocw-desktop-24.png](143836-2026-11-25-release-0.2.6-windows-icon-ocw-desktop-24.png) |
| 14:38:36 | [143836-2026-11-25-release-0.2.6-windows-icon-ocw-desktop-256.png](143836-2026-11-25-release-0.2.6-windows-icon-ocw-desktop-256.png) |
| 14:38:36 | [143836-2026-11-25-release-0.2.6-windows-icon-ocw-desktop-32.png](143836-2026-11-25-release-0.2.6-windows-icon-ocw-desktop-32.png) |
| 14:38:36 | [143836-2026-11-25-release-0.2.6-windows-icon-ocw-desktop-48.png](143836-2026-11-25-release-0.2.6-windows-icon-ocw-desktop-48.png) |
| 14:38:36 | [143836-2026-11-25-release-0.2.6-windows-icon-ocw-desktop-64.png](143836-2026-11-25-release-0.2.6-windows-icon-ocw-desktop-64.png) |
| 14:38:36 | [143836-2026-11-25-release-0.2.6-windows-icon-ocw-studio-128.png](143836-2026-11-25-release-0.2.6-windows-icon-ocw-studio-128.png) |
| 14:38:36 | [143836-2026-11-25-release-0.2.6-windows-icon-ocw-studio-16.png](143836-2026-11-25-release-0.2.6-windows-icon-ocw-studio-16.png) |
| 14:38:36 | [143836-2026-11-25-release-0.2.6-windows-icon-ocw-studio-24.png](143836-2026-11-25-release-0.2.6-windows-icon-ocw-studio-24.png) |
| 14:38:36 | [143836-2026-11-25-release-0.2.6-windows-icon-ocw-studio-256.png](143836-2026-11-25-release-0.2.6-windows-icon-ocw-studio-256.png) |
| 14:38:36 | [143836-2026-11-25-release-0.2.6-windows-icon-ocw-studio-32.png](143836-2026-11-25-release-0.2.6-windows-icon-ocw-studio-32.png) |
| 14:38:36 | [143836-2026-11-25-release-0.2.6-windows-icon-ocw-studio-48.png](143836-2026-11-25-release-0.2.6-windows-icon-ocw-studio-48.png) |
| 14:38:36 | [143836-2026-11-25-release-0.2.6-windows-icon-ocw-studio-64.png](143836-2026-11-25-release-0.2.6-windows-icon-ocw-studio-64.png) |
| 15:50:00 | [155000-2026-11-25-release-0.2.6-web-webgpu-web-calendar-select.jpg](155000-2026-11-25-release-0.2.6-web-webgpu-web-calendar-select.jpg) |
| 15:50:00 | [155000-2026-11-25-release-0.2.6-web-webgpu-web-calendar.jpg](155000-2026-11-25-release-0.2.6-web-webgpu-web-calendar.jpg) |
| 15:50:00 | [155000-2026-11-25-release-0.2.6-web-webgpu-web-console.jpg](155000-2026-11-25-release-0.2.6-web-webgpu-web-console.jpg) |
| 15:50:00 | [155000-2026-11-25-release-0.2.6-web-webgpu-web-damage-crash.jpg](155000-2026-11-25-release-0.2.6-web-webgpu-web-damage-crash.jpg) |
| 15:50:00 | [155000-2026-11-25-release-0.2.6-web-webgpu-web-damage-fresh.jpg](155000-2026-11-25-release-0.2.6-web-webgpu-web-damage-fresh.jpg) |
| 15:50:00 | [155000-2026-11-25-release-0.2.6-web-webgpu-web-devices-collapsed.jpg](155000-2026-11-25-release-0.2.6-web-webgpu-web-devices-collapsed.jpg) |
| 15:50:00 | [155000-2026-11-25-release-0.2.6-web-webgpu-web-devices-expanded.jpg](155000-2026-11-25-release-0.2.6-web-webgpu-web-devices-expanded.jpg) |
| 15:50:00 | [155000-2026-11-25-release-0.2.6-web-webgpu-web-downloads-OCW-2026-11-25-15-51-26.jpg](155000-2026-11-25-release-0.2.6-web-webgpu-web-downloads-OCW-2026-11-25-15-51-26.jpg) |
| 15:50:00 | [155000-2026-11-25-release-0.2.6-web-webgpu-web-downloads-ocw-2026-11-25-15-51-52.webm](155000-2026-11-25-release-0.2.6-web-webgpu-web-downloads-ocw-2026-11-25-15-51-52.webm) |
| 15:50:00 | [155000-2026-11-25-release-0.2.6-web-webgpu-web-gamepad.jpg](155000-2026-11-25-release-0.2.6-web-webgpu-web-gamepad.jpg) |
| 15:50:00 | [155000-2026-11-25-release-0.2.6-web-webgpu-web-gps.jpg](155000-2026-11-25-release-0.2.6-web-webgpu-web-gps.jpg) |
| 15:50:00 | [155000-2026-11-25-release-0.2.6-web-webgpu-web-history-delete.jpg](155000-2026-11-25-release-0.2.6-web-webgpu-web-history-delete.jpg) |
| 15:50:00 | [155000-2026-11-25-release-0.2.6-web-webgpu-web-history-ride-file.jpg](155000-2026-11-25-release-0.2.6-web-webgpu-web-history-ride-file.jpg) |
| 15:50:00 | [155000-2026-11-25-release-0.2.6-web-webgpu-web-history-ride-map.jpg](155000-2026-11-25-release-0.2.6-web-webgpu-web-history-ride-map.jpg) |
| 15:50:00 | [155000-2026-11-25-release-0.2.6-web-webgpu-web-hud.jpg](155000-2026-11-25-release-0.2.6-web-webgpu-web-hud.jpg) |
| 15:50:00 | [155000-2026-11-25-release-0.2.6-web-webgpu-web-input-mapping-capture.jpg](155000-2026-11-25-release-0.2.6-web-webgpu-web-input-mapping-capture.jpg) |
| 15:50:00 | [155000-2026-11-25-release-0.2.6-web-webgpu-web-input-mapping-junctions.jpg](155000-2026-11-25-release-0.2.6-web-webgpu-web-input-mapping-junctions.jpg) |
| 15:50:00 | [155000-2026-11-25-release-0.2.6-web-webgpu-web-input-mapping-swapped.jpg](155000-2026-11-25-release-0.2.6-web-webgpu-web-input-mapping-swapped.jpg) |
| 15:50:00 | [155000-2026-11-25-release-0.2.6-web-webgpu-web-input-mapping.jpg](155000-2026-11-25-release-0.2.6-web-webgpu-web-input-mapping.jpg) |
| 15:50:00 | [155000-2026-11-25-release-0.2.6-web-webgpu-web-join.jpg](155000-2026-11-25-release-0.2.6-web-webgpu-web-join.jpg) |
| 15:50:00 | [155000-2026-11-25-release-0.2.6-web-webgpu-web-menu.jpg](155000-2026-11-25-release-0.2.6-web-webgpu-web-menu.jpg) |
| 15:50:00 | [155000-2026-11-25-release-0.2.6-web-webgpu-web-photo-preview.jpg](155000-2026-11-25-release-0.2.6-web-webgpu-web-photo-preview.jpg) |
| 15:50:00 | [155000-2026-11-25-release-0.2.6-web-webgpu-web-ride.jpg](155000-2026-11-25-release-0.2.6-web-webgpu-web-ride.jpg) |
| 15:50:00 | [155000-2026-11-25-release-0.2.6-web-webgpu-web-riders.jpg](155000-2026-11-25-release-0.2.6-web-webgpu-web-riders.jpg) |
| 15:50:00 | [155000-2026-11-25-release-0.2.6-web-webgpu-web-settings.jpg](155000-2026-11-25-release-0.2.6-web-webgpu-web-settings.jpg) |
| 15:50:00 | [155000-2026-11-25-release-0.2.6-web-webgpu-web-strava-recording-downloaded.jpg](155000-2026-11-25-release-0.2.6-web-webgpu-web-strava-recording-downloaded.jpg) |
| 15:50:00 | [155000-2026-11-25-release-0.2.6-web-webgpu-web-strava-recording-saved-to-folder.jpg](155000-2026-11-25-release-0.2.6-web-webgpu-web-strava-recording-saved-to-folder.jpg) |
| 15:50:00 | [155000-2026-11-25-release-0.2.6-web-webgpu-web-strava-recording.jpg](155000-2026-11-25-release-0.2.6-web-webgpu-web-strava-recording.jpg) |
| 15:50:00 | [155000-2026-11-25-release-0.2.6-web-webgpu-web-strava-row.jpg](155000-2026-11-25-release-0.2.6-web-webgpu-web-strava-row.jpg) |
| 15:50:00 | [155000-2026-11-25-release-0.2.6-web-webgpu-web-strava-steps.jpg](155000-2026-11-25-release-0.2.6-web-webgpu-web-strava-steps.jpg) |
| 15:50:00 | [155000-2026-11-25-release-0.2.6-web-webgpu-web-touch-hints.jpg](155000-2026-11-25-release-0.2.6-web-webgpu-web-touch-hints.jpg) |
| 15:50:00 | [155000-2026-11-25-release-0.2.6-web-webgpu-web-touch-hold.jpg](155000-2026-11-25-release-0.2.6-web-webgpu-web-touch-hold.jpg) |
| 15:50:00 | [155000-2026-11-25-release-0.2.6-web-webgpu-web-unicorn-flight.jpg](155000-2026-11-25-release-0.2.6-web-webgpu-web-unicorn-flight.jpg) |
| 15:50:00 | [155000-2026-11-25-release-0.2.6-web-webgpu-web-unicorn-inspect.jpg](155000-2026-11-25-release-0.2.6-web-webgpu-web-unicorn-inspect.jpg) |
| 15:50:00 | [155000-2026-11-25-release-0.2.6-web-webgpu-web-unicorn-menu.jpg](155000-2026-11-25-release-0.2.6-web-webgpu-web-unicorn-menu.jpg) |
| 15:50:00 | [155000-2026-11-25-release-0.2.6-web-webgpu-web-weather.jpg](155000-2026-11-25-release-0.2.6-web-webgpu-web-weather.jpg) |
| 15:50:00 | [155000-2026-11-25-release-0.2.6-web-webgpu-web-workout-map.jpg](155000-2026-11-25-release-0.2.6-web-webgpu-web-workout-map.jpg) |
| 15:50:00 | [155000-2026-11-25-release-0.2.6-web-webgpu-web.jpg](155000-2026-11-25-release-0.2.6-web-webgpu-web.jpg) |
| 15:52:24 | [155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-calendar-select.jpg](155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-calendar-select.jpg) |
| 15:52:24 | [155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-calendar.jpg](155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-calendar.jpg) |
| 15:52:24 | [155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-console.jpg](155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-console.jpg) |
| 15:52:24 | [155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-damage-crash.jpg](155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-damage-crash.jpg) |
| 15:52:24 | [155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-damage-fresh.jpg](155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-damage-fresh.jpg) |
| 15:52:24 | [155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-devices-collapsed.jpg](155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-devices-collapsed.jpg) |
| 15:52:24 | [155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-devices-expanded.jpg](155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-devices-expanded.jpg) |
| 15:52:24 | [155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-downloads-OCW-2026-11-25-15-53-47.jpg](155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-downloads-OCW-2026-11-25-15-53-47.jpg) |
| 15:52:24 | [155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-downloads-ocw-2026-11-25-15-54-14.webm](155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-downloads-ocw-2026-11-25-15-54-14.webm) |
| 15:52:24 | [155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-gamepad.jpg](155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-gamepad.jpg) |
| 15:52:24 | [155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-gps.jpg](155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-gps.jpg) |
| 15:52:24 | [155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-history-delete.jpg](155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-history-delete.jpg) |
| 15:52:24 | [155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-history-ride-file.jpg](155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-history-ride-file.jpg) |
| 15:52:24 | [155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-history-ride-map.jpg](155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-history-ride-map.jpg) |
| 15:52:24 | [155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-hud.jpg](155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-hud.jpg) |
| 15:52:24 | [155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-input-mapping-capture.jpg](155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-input-mapping-capture.jpg) |
| 15:52:24 | [155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-input-mapping-junctions.jpg](155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-input-mapping-junctions.jpg) |
| 15:52:24 | [155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-input-mapping-swapped.jpg](155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-input-mapping-swapped.jpg) |
| 15:52:24 | [155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-input-mapping.jpg](155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-input-mapping.jpg) |
| 15:52:24 | [155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-join.jpg](155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-join.jpg) |
| 15:52:24 | [155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-menu.jpg](155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-menu.jpg) |
| 15:52:24 | [155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-photo-preview.jpg](155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-photo-preview.jpg) |
| 15:52:24 | [155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-ride.jpg](155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-ride.jpg) |
| 15:52:24 | [155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-riders.jpg](155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-riders.jpg) |
| 15:52:24 | [155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-settings.jpg](155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-settings.jpg) |
| 15:52:24 | [155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-strava-recording-downloaded.jpg](155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-strava-recording-downloaded.jpg) |
| 15:52:24 | [155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-strava-recording-saved-to-folder.jpg](155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-strava-recording-saved-to-folder.jpg) |
| 15:52:24 | [155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-strava-recording.jpg](155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-strava-recording.jpg) |
| 15:52:24 | [155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-strava-row.jpg](155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-strava-row.jpg) |
| 15:52:24 | [155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-strava-steps.jpg](155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-strava-steps.jpg) |
| 15:52:24 | [155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-touch-hints.jpg](155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-touch-hints.jpg) |
| 15:52:24 | [155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-touch-hold.jpg](155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-touch-hold.jpg) |
| 15:52:24 | [155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-unicorn-flight.jpg](155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-unicorn-flight.jpg) |
| 15:52:24 | [155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-unicorn-inspect.jpg](155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-unicorn-inspect.jpg) |
| 15:52:24 | [155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-unicorn-menu.jpg](155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-unicorn-menu.jpg) |
| 15:52:24 | [155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-weather.jpg](155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-weather.jpg) |
| 15:52:24 | [155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-workout-map.jpg](155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2-workout-map.jpg) |
| 15:52:24 | [155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2.jpg](155224-2026-11-25-release-0.2.6-web-webgl2-web-webgl2.jpg) |
| 15:55:20 | [155520-2026-11-25-release-0.2.6-smoke-web-world-web-world-cached-loading.jpg](155520-2026-11-25-release-0.2.6-smoke-web-world-web-world-cached-loading.jpg) |
| 15:55:20 | [155520-2026-11-25-release-0.2.6-smoke-web-world-web-world-cached.jpg](155520-2026-11-25-release-0.2.6-smoke-web-world-web-world-cached.jpg) |
| 15:55:20 | [155520-2026-11-25-release-0.2.6-smoke-web-world-web-world-first-loading.jpg](155520-2026-11-25-release-0.2.6-smoke-web-world-web-world-first-loading.jpg) |
| 15:55:20 | [155520-2026-11-25-release-0.2.6-smoke-web-world-web-world.jpg](155520-2026-11-25-release-0.2.6-smoke-web-world-web-world.jpg) |
| 15:56:43 | [155643-2026-11-25-release-0.2.6-smoke-appimage-x11.jpg](155643-2026-11-25-release-0.2.6-smoke-appimage-x11.jpg) |
| 20:12:51 | [201251-7d97fded-dirty-shot-wayland-studio-trust-dialog.jpg](201251-7d97fded-dirty-shot-wayland-studio-trust-dialog.jpg) |
| 20:35:51 | [203551-7d97fded-dirty-shot-ocw.jpg](203551-7d97fded-dirty-shot-ocw.jpg) |
| 20:36:02 | [203602-7d97fded-dirty-shot-wayland-ocw-wayland.jpg](203602-7d97fded-dirty-shot-wayland-ocw-wayland.jpg) |
| 20:38:26 | [203826-7d97fded-dirty-shot-wayland-chin-a-front.jpg](203826-7d97fded-dirty-shot-wayland-chin-a-front.jpg) |
| 20:38:37 | [203837-7d97fded-dirty-shot-wayland-chin-a-side.jpg](203837-7d97fded-dirty-shot-wayland-chin-a-side.jpg) |
| 20:38:48 | [203848-7d97fded-dirty-shot-wayland-chin-a-below.jpg](203848-7d97fded-dirty-shot-wayland-chin-a-below.jpg) |
| 20:38:59 | [203859-7d97fded-dirty-shot-wayland-chin-b-light-below.jpg](203859-7d97fded-dirty-shot-wayland-chin-b-light-below.jpg) |
| 20:39:10 | [203910-7d97fded-dirty-shot-wayland-chin-c-aero-side.jpg](203910-7d97fded-dirty-shot-wayland-chin-c-aero-side.jpg) |
| 20:39:21 | [203921-7d97fded-dirty-shot-wayland-chin-d-tt-front-below.jpg](203921-7d97fded-dirty-shot-wayland-chin-d-tt-front-below.jpg) |
| 20:39:32 | [203932-7d97fded-dirty-shot-wayland-chin-e-70-chinstrap-below.jpg](203932-7d97fded-dirty-shot-wayland-chin-e-70-chinstrap-below.jpg) |
| 20:39:43 | [203943-7d97fded-dirty-shot-wayland-chin-f-bare-editor.jpg](203943-7d97fded-dirty-shot-wayland-chin-f-bare-editor.jpg) |
| 20:39:54 | [203954-7d97fded-dirty-shot-wayland-chin-f-bare-editor-clean.jpg](203954-7d97fded-dirty-shot-wayland-chin-f-bare-editor-clean.jpg) |
| 20:40:04 | [204004-7d97fded-dirty-shot-wayland-chin-g-far.jpg](204004-7d97fded-dirty-shot-wayland-chin-g-far.jpg) |
| 20:40:56 | [204056-7d97fded-dirty-shot-wayland-chin-a-front.jpg](204056-7d97fded-dirty-shot-wayland-chin-a-front.jpg) |
| 20:41:08 | [204108-7d97fded-dirty-shot-wayland-chin-a-side.jpg](204108-7d97fded-dirty-shot-wayland-chin-a-side.jpg) |
| 20:41:19 | [204119-7d97fded-dirty-shot-wayland-chin-a-below.jpg](204119-7d97fded-dirty-shot-wayland-chin-a-below.jpg) |
| 20:41:29 | [204129-7d97fded-dirty-shot-wayland-chin-b-light-below.jpg](204129-7d97fded-dirty-shot-wayland-chin-b-light-below.jpg) |
| 20:41:39 | [204139-7d97fded-dirty-shot-wayland-chin-c-aero-side.jpg](204139-7d97fded-dirty-shot-wayland-chin-c-aero-side.jpg) |
| 20:41:50 | [204150-7d97fded-dirty-shot-wayland-chin-d-tt-front-below.jpg](204150-7d97fded-dirty-shot-wayland-chin-d-tt-front-below.jpg) |
| 20:42:00 | [204200-7d97fded-dirty-shot-wayland-chin-e-70-chinstrap-below.jpg](204200-7d97fded-dirty-shot-wayland-chin-e-70-chinstrap-below.jpg) |
| 20:42:11 | [204211-7d97fded-dirty-shot-wayland-chin-f-bare-editor.jpg](204211-7d97fded-dirty-shot-wayland-chin-f-bare-editor.jpg) |
| 20:42:22 | [204222-7d97fded-dirty-shot-wayland-chin-f-bare-editor-clean.jpg](204222-7d97fded-dirty-shot-wayland-chin-f-bare-editor-clean.jpg) |
| 20:42:33 | [204233-7d97fded-dirty-shot-wayland-chin-g-far.jpg](204233-7d97fded-dirty-shot-wayland-chin-g-far.jpg) |
| 20:42:52 | [204252-chin-bubble-pairs-chin-a-below-before-after.jpg](204252-chin-bubble-pairs-chin-a-below-before-after.jpg) |
| 20:42:52 | [204252-chin-bubble-pairs-chin-a-front-before-after.jpg](204252-chin-bubble-pairs-chin-a-front-before-after.jpg) |
| 20:42:52 | [204252-chin-bubble-pairs-chin-a-side-before-after.jpg](204252-chin-bubble-pairs-chin-a-side-before-after.jpg) |
| 20:42:52 | [204252-chin-bubble-pairs-chin-b-light-below-before-after.jpg](204252-chin-bubble-pairs-chin-b-light-below-before-after.jpg) |
| 20:42:52 | [204252-chin-bubble-pairs-chin-c-aero-side-before-after.jpg](204252-chin-bubble-pairs-chin-c-aero-side-before-after.jpg) |
| 20:42:53 | [204253-chin-bubble-geometry-after-helmets-beards.png](204253-chin-bubble-geometry-after-helmets-beards.png) |
| 20:42:53 | [204253-chin-bubble-geometry-beards-before-after-proto.png](204253-chin-bubble-geometry-beards-before-after-proto.png) |
| 20:42:53 | [204253-chin-bubble-geometry-before-chin-marked.png](204253-chin-bubble-geometry-before-chin-marked.png) |
| 20:42:53 | [204253-chin-bubble-pairs-chin-d-tt-front-below-before-after.jpg](204253-chin-bubble-pairs-chin-d-tt-front-below-before-after.jpg) |
| 20:42:53 | [204253-chin-bubble-pairs-chin-e-70-chinstrap-below-before-after.jpg](204253-chin-bubble-pairs-chin-e-70-chinstrap-below-before-after.jpg) |
| 20:42:53 | [204253-chin-bubble-pairs-chin-f-bare-editor-before-after.jpg](204253-chin-bubble-pairs-chin-f-bare-editor-before-after.jpg) |
| 20:42:53 | [204253-chin-bubble-pairs-chin-f-bare-editor-clean-before-after.jpg](204253-chin-bubble-pairs-chin-f-bare-editor-clean-before-after.jpg) |
| 20:42:53 | [204253-chin-bubble-pairs-chin-g-far-before-after.jpg](204253-chin-bubble-pairs-chin-g-far-before-after.jpg) |
| 22:01:23 | [220123-studio-map-q15-bf-middle-neighbours.jpg](220123-studio-map-q15-bf-middle-neighbours.jpg) |
| 22:01:44 | [220144-studio-map-q15-bf-middle-border.jpg](220144-studio-map-q15-bf-middle-border.jpg) |
| 22:02:06 | [220206-studio-map-q15-bf-middle-aerial-off.jpg](220206-studio-map-q15-bf-middle-aerial-off.jpg) |
| 22:02:27 | [220227-studio-map-q15-bf-middle-aerial-on.jpg](220227-studio-map-q15-bf-middle-aerial-on.jpg) |
| 22:02:43 | [220243-studio-map-q15-li-border.jpg](220243-studio-map-q15-li-border.jpg) |
| 22:02:59 | [220259-studio-map-q15-li-aerial-off.jpg](220259-studio-map-q15-li-aerial-off.jpg) |
| 22:03:14 | [220314-studio-map-q15-li-aerial-on.jpg](220314-studio-map-q15-li-aerial-on.jpg) |
