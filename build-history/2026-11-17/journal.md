# OCW build diary – day 7, 2026-11-17

78 commits (23 merges), +27921 / −2573 lines, 1039 images, 8 videos, 1 sounds.

## Commits

| Time | Commit | |
|---|---|---|
| 00:47 | `1eb1415` | Character editor refined, first step: unique names of every script, seven body shapes on base bodies A/B/C bounded to the weight's band, appearance age, 21 hair styles, moustache and beard (spec §14 Phase 4, 4N; v4.37) |
| 01:01 | `732ac02` | Voice: Block (remembered, both directions) and a per-rider volume in the participants' list (decision from the build dashboard; §7.1.7 Q9) |
| 01:02 | `0272f23` | Browsers join a desktop-hosted ride with V5: Host a ride opens WebTransport on PORT+1 together with the browser signalling bridge (decision from the build dashboard; §7.1.7 Q14) |
| 01:05 | `d2aa9e0` | Character editor: every body shape can be chosen whatever weight and height say; their shape is only a proposal (decision from the build dashboard; Phase 4 4N Q23, replaces Q13's band) |
| 01:06 | `8cd732c` | Character editor: the upper arms follow the shoulders' width of the body shape (spec §14 Phase 4, 4N) |
| 01:08 | `7f9b81e` | A new account starts in sneakers, jeans and a hoodie on an old rusty city bike; everything else is bought (decision from the build dashboard; Phase 4 Q16, W5) |
| 01:08 | `65b7a5e` | Spec Phase 4 Q16: mark the city bike's physics and the starter items' resale as proposals, not decided |
| 01:12 | `15cc6ae` | Riding needs no purchase: the starter city bike, sneakers, jeans and hoodie are ridden until bought items replace them (decision from the build dashboard; Phase 4 Q17) |
| 01:15 | `64f89b8` | Planned: one local config file for all local settings, and a start choice in the desktop app – connect to a server or ride locally (spec §3.2.4, open questions Q1–Q6) |
| 01:16 | `dd79de6` (merge) | Merge origin/main; body shapes decoupled from the weight: every shape can be chosen, weight and height only propose one (4N Q23, no band) |
| 02:10 | `682c759` | Dev cameras on the ride photographer's drone for videos: camera.drone pov/follow/off (spec §2.11, v4.45) |
| 02:12 | `6465e69` | Calendar: a Select button sets the selected day and goes back to World → Time, like a date picker's OK (spec §14 Phase 9, 9J, v4.45) |
| 02:22 | `c4c2101` | The legacy fog is the default again; the new fog of 10G stays as sky.fog new (the user's request; spec 4.45) |
| 03:02 | `c60c7df` | Character editor: a visual editor in both apps and a face for the rider (spec §14 Phase 4, 4N) |
| 03:05 | `99cfbdc` | photographer drone keeps the next shot a drone's until its visit ends (spec §2.11, v4.45) |
| 03:12 | `3fcea73` (merge) | Merge the refined character editor (4N first step): names, body A/B/C × seven shapes, age, hair and facial hair, the visual editor and the face (spec 4.46) |
| 03:49 | `f2267f8` (merge) | Merge the calendar's Select button: sets the selected day and goes back to World → Time (spec 4.46, 9J; open question 9H Q14) |
| 04:00 | `95cfeef` | Voice Block and per-rider volume built: Block keeps two riders apart both ways (game server + voice server), remembered, the blocked rider not told; a volume of 0-200 % per rider (spec 4.40, §7.1.7 Q9, §7.1.10) |
| 04:04 | `3a02503` | Drone follow camera closer (3 m behind, 1.2 m aside, 0.6 m up); hud off hides the junction fan too (spec §2.11, v4.45) |
| 04:04 | `7bf5fe2` | Character editor: shorter shape texts so the body page fits a 16:9 window (every_menu_page_fits_a_16_9_window_with_its_text) |
| 04:04 | `a3dfb1f` (merge) | Merge remote-tracking branch 'origin/main' into merge/4n |
| 04:27 | `a31544e` | Character editor pages fit a 16:9 window: shorter face, beard colour and tile texts; the page-fit test lists every page that is too tall |
| 04:31 | `bbbee64` | Drone follow camera: eye smoothing 0.12 s and an unsmoothed look-at point, so the drone stays in the picture at 13 m/s (spec §2.11, v4.45) |
| 04:42 | `4bbbc04` | Rider model re-exported on marge (the committed file came from Win11Builder and differed; export-all --check) |
| 04:43 | `f9835c9` | Bike stand: a small rendering of every selectable part and paint, with its speed gain in % (spec §14 Phase 4, 4G Built v4.45) |
| 05:06 | `d346868` (merge) | Merge voice Block and per-rider volume: Block both ways enforced through the server and LiveKit permissions, volume 0–200 % per rider, remembered (spec 4.48, §7.1.10) |
| 05:06 | `dcf5683` (merge) | Merge the bike stand's tiles: a rendering of every part and paint with its gain in % flat and on a 6 % climb (spec 4.49, Phase 4 4G; open questions Q26, Q27) |
| 05:07 | `e97fefe` (merge) | Merge the dev drone cameras (camera.drone pov/follow/off), a forced drone shot staying a drone, hud off hiding the junction arrow, and the drone video script (spec 4.50, §2.11) |
| 05:07 | `768cc96` | Merge fix: rustfmt's layout of the desktop menu's page list |
| 05:44 | `5f97438` | Character editor, step 2: a real face close-up, picture tiles rendered from the models, the workshop mirror's pickers as tiles (spec §14 Phase 4, 4N) |
| 06:32 | `a6bb5b8` | Character editor step 2 fixes from the screenshots: the road close-up aims at the face (not the neck pivot) from a little higher, the mirror close-up looks at the face (the magnified reflection was blurred), body tiles frame helmet to thighs, picture names smaller, grid cells keep their share (five columns showed as four) |
| 06:32 | `18815d6` | The rider split into model files as 4N N8 planned: hair pieces, moustaches, beards and the base bodies' parts are wearables of their own (Q25 resolved by following N8) |
| 06:50 | `6ef6150` | Character editor step 2: the face close-up rides along with the rider (smoothed in its frame, it trailed behind the head at speed) from 0.75 m; spec 4.51 with the second step's Built note and Q25 resolved (§14 Phase 4, 4N) |
| 06:51 | `becfdb4` | CLAUDE.md: send the user every test picture and video (it was only in one session's memory and got lost); agents list the paths, the coordinator sends them |
| 08:56 | `1745e0a` | Voice by range and audience, V3 and V4 (spec §7.1.11, 4.51): voices fade to silence at 300 m and the game server sends a rider's voice only to riders who can hear it; every ride is joined muted; Who hears me (No one by default, All nearby, Selected riders) and Voice room (Everybody, Selected riders) with riders chosen by name; a block always wins |
| 10:02 | `cc32a0f` (merge) | Merge voice V3/V4: range (full to 10 m, fading to 300 m), the server decides who hears whom, join muted, Who hears me, Voice room with selected riders (spec 4.51, §7.1.11) |
| 13:29 | `57cdc5a` | Skin tone selector: every tone a swatch tile in the menu and the mirror, the palette widened to 16 tones from very pale to very dark with warm and neutral / olive undertones; old values migrate to the nearest (asked 2026-11-17; spec §14 Phase 4, 4N) |
| 13:30 | `f4cf713` | rustfmt: the skin palette tests' layout |
| 13:31 | `56894d9` (merge) | Merge the character editor's second step: face close-up camera, picture tiles, the mirror's tiles, the model split (hair, facial hair, bodies) and 16 skin tones (spec 4.52, 4N) |
| 13:49 | `e804355` | Hair is edited and shown without the helmet; the helmet hangs on a hook on the workshop wall (the user's decision; 4N Q28) |
| 13:50 | `73cc35c` | The hair page keeps pictures only, the focused style named at the top (the user's decision; 4N Q29) |
| 14:26 | `86b93b6` | The rider has real hands: a palm, a thumb and four fingers with knuckle joints, wrapping every bike's grips, the phone held in the fingers, open with the arms up; the editor takes the helmet off for the hair and the face and hangs it on a hook beside the mirror (spec §14 Phase 4, 4N; Q28) |
| 14:26 | `2f1d1d9` (merge) | Merge remote-tracking branch 'origin/merge/char2' into char-editor-hands |
| 14:26 | `fc5606f` | Spec 4.55: the hands and the helmet off built (§14 Phase 4, 4N Built, hands; Built, helmet off; Q28) |
| 14:53 | `85995be` (merge) | Merge the real hands (five grip shapes, gloves following the fingers) and the helmet off while hair and face are edited, hanging on a hook on the workshop wall (spec 4.55, 4N Q25, Q28) |
| 15:40 | `e2868f1` | Fix five visible defects: a shaped palm, the helmet on its hook, relaxed standing hands, the HUD panel on narrow windows, the stand's card (spec 4.56) |
| 15:55 | `d9f8d06` | Field stands lie on the drawn terrain: no green slabs floating over Tenerife's terraces (spec 4.56, §4.6.1) |
| 15:56 | `d7e2dd4` | Relaxed hands curl less, the helmet's peg hidden in the shell, fmt and clippy (spec 4.56) |
| 16:37 | `5f87734` | Stands: a type alias for the drawn-stand cache (clippy type_complexity) |
| 16:37 | `7af2efa` (merge) | Merge crop stands on the drawn ground: no more floating green slabs (stands sample the terrain as drawn, incl. junction lowering; sides toward roads; low stands slope to the ground) (spec 4.56, §4.6.1) |
| 16:46 | `61fd990` (merge) | Merge five visible fixes: a shaped palm, the helmet hanging properly on its hook, relaxed standing hands, the HUD top panel fitting narrow windows, the bike stand's card fitting and weights with thousands separators (spec 4.57) |
| 16:47 | `2e640ef` | Spec 4G: the bike stand's open question is Q26 (renumbered at its merge) |
| 17:46 | `00007be` | Trees, bushes, lamps and posts stand on the drawn terrain; bike stand thumbnails framed on the part (spec 4.58, §4.6.1, 4G) |
| 18:09 | `cf98fa2` (merge) | Merge thumbnails framed on their part (groupset shows the drivetrain) and trees, plants, lamps and posts on the drawn ground (spec 4.58) |
| 18:38 | `504865a` | Bike stand and character tiles draw the whole thumbnail: checked and locked by a test (spec 4.59, 4G) |
| 18:42 | `b4c8a6a` (merge) | Merge a regression test that the tiles draw the whole thumbnail (bike stand and character tiles; spec 4.59) |
| 19:15 | `ea10964` | Thumbnails framed tight and centred: the drivetrain big in the groupset tiles, the head filling the hair and face tiles (spec 4.60, 4G, 4N) |
| 19:19 | `988e01a` (merge) | Merge tighter, centred thumbnail framing (multi-piece parts fit by their pieces) and larger, centred head shots (spec 4.60) |
| 19:36 | `3d83682` | Voice: selected riders always audible; everyone else fades from 5 m and is silent beyond 10 m (decision from the build dashboard; §7.1.7 Q20, changes Q10's range) |
| 19:48 | `b9adfae` | Drivetrain thumbnails without the wheels, square on from the drive side: the groupset tile shows chainrings, not a rear wheel (spec 4.61, 4G) |
| 19:49 | `89f7dd9` (merge) | Merge drivetrain thumbnails without the wheels, seen square on (spec 4.62, 4G) |
| 19:56 | `ef130d9` | Build dashboard 1.6.0: open questions kept current – 'Q30 (open) –' bullets read, a 15-minute timer fast-forwards the main checkout and lints the questions; spec: two answers in the readable form, new 4N Q31 |
| 19:56 | `5b7ce67` | Voice heard only close by (full to 5 m, silent beyond 10 m) and selected riders at any distance: built in both apps (spec 4.62, §7.1.11, §7.1.7 Q20) |
| 20:46 | `644ac51` | Windows executables carry the OCW logo: multi-size icon and version info in ocw-desktop, ocw-server and ocw-studio (spec 4.62, §11.3) |
| 20:47 | `c09b638` (merge) | Merge the OCW logo as the Windows executables' icon, with version info (ocw-desktop, ocw-server, ocw-studio; spec 4.64, §11.3) |
| 21:01 | `38bb88b` | Voice range: the Voice room hint fits the page, test fixes for the 10 m range (spec 4.62) |
| 21:02 | `a5e7936` (merge) | Merge the voice range of Q20: full to 5 m, silent beyond 10 m, selected riders always audible (spec 4.65, §7.1.11) |
| 21:24 | `9137c1f` | Strava: the game's FIT files upload as Virtual Rides with their GPS track and map; kept as virtual activity (checked by the user; §2.8.1) |
| 22:19 | `162ae1c` (merge) | Merge remote-tracking branch 'origin/main' into merge/voice-range |
| 22:29 | `1950938` | Hands hold the bar the right way up: palm down on hoods, tops and flat grips, inward on drops and TT bars; thumb inside the hood, the phone in the palm facing the eyes (spec 4.65, §14 Phase 4 4N) |
| 22:30 | `e59ba4b` (merge) | Merge the hand grips the right way up: palm down on hoods, tops and flat grips, inward on the drops and TT bars, thumb wrapping, the phone facing the eyes (spec 4.67, 4N) |
| 23:10 | `f6ee646` | OCW Studio has its own logo – a horn-gold pencil drawing the rainbow – as its icon on every platform (spec 4.66, §11.3, §14 Phase 16) |
| 23:11 | `ccc5d76` (merge) | Merge the OCW Studio logo: its own icon for the studio binaries on Windows, Linux and macOS, shared window-icon code (spec 4.68) |
| 23:25 | `26fc30f` | WIP road damage: cracks, sealing, alligator areas, potholes in road.wesl (spec §4.6) |
| 23:32 | `b92f0ca` | CLAUDE.md: record photos and videos of every automated test run, VR on Weela included, copy them back into test-output/ for the art project's collector |
| 23:38 | `8444074` (merge) | Merge origin/main into merge/grips |
| 23:47 | `be80788` | WIP road damage by OSM smoothness: section RCND, loose stones, ruts, concrete joints |
| 23:55 | `1f772c6` | Ride photos are saved in the user's photos folder, subfolder OCW (decision from the build dashboard, 2026-11-17; §2.11 Q3; spec 4.69) |

## Builds and build servers

444 build/test runs on the build machines, 71.6 h in total, 37 failed; 1436 server samples; cargo compiled 24305 crates in 10.8 h, 21.2 h waiting for build slots.

| Machine | Runs | Hours | Cargo h | Crates | Waited h | Failed | Online |
|---|---|---|---|---|---|---|---|
| Weela | 56 | 4.3 | 0.6 | 691 | 0.0 | 12 | 58% |
| Win11Builder | 42 | 6.3 | 3.6 | 3001 | 1.4 | 6 | 100% |
| leela | 0 | 0.0 | 0.0 | 0 | 0.0 | 0 | 0% |
| macos | 47 | 2.8 | 0.2 | 618 | 0.5 | 2 | 100% |
| marge | 299 | 58.2 | 6.4 | 19995 | 19.3 | 17 | 100% |

Failed runs:

- 00:36 Weela: `powershell -ExecutionPolicy Bypass -File scripts\win-gui-run.ps1 -Exe target\rel` (exit 1, log `build-log/003608-Weela-2473750.log`)
- 00:36 Weela: `powershell -ExecutionPolicy Bypass -File scripts\win-gui-run.ps1 -Exe target\rel` (exit 1, log `build-log/003624-Weela-2474220.log`)
- 00:51 Weela: `powershell -ExecutionPolicy Bypass -File scripts\win-gui-run.ps1 -Exe target\rel` (exit 5, log `build-log/005133-Weela-2492755.log`)
- 01:25 marge: `cargo fmt --all && git status --short && cargo clippy -p ocw-voice -p ocw-server` (exit 128, log `build-log/012513-marge-2608943.log`)
- 01:28 marge: `source ~/.cargo/env; cargo fmt --all --check && cargo test -p ocw-client calenda` (exit 1, log `build-log/012836-marge-2615118.log`)
- 01:35 Weela: `Test-Path target\release\openxr_loader.dll; powershell -ExecutionPolicy Bypass -` (exit 2, log `build-log/013535-Weela-2626344.log`)
- 01:35 Weela: `Test-Path target\release\openxr_loader.dll; powershell -ExecutionPolicy Bypass -` (exit 1, log `build-log/013547-Weela-2626815.log`)
- 02:33 Win11Builder: `cargo clippy -p ocw-core -p ocw-assets -p ocw-protocol -p ocw-client -p ocw-ui -` (exit 101, log `build-log/023319-Win11Builder-2716224.log`)
- 03:12 marge: `set -e; export CC=clang-21 CXX=clang++-21; make check; cargo run -q -p ocw-asset` (exit 2, log `build-log/031253-marge-2778440.log`)
- 04:04 marge: `set -e; export CC=clang-21 CXX=clang++-21; make check; cargo run -q -p ocw-asset` (exit 2, log `build-log/040458-marge-2843741.log`)
- 04:27 marge: `set -e; export CC=clang-21 CXX=clang++-21; make check; cargo run -q -p ocw-asset` (exit 1, log `build-log/042759-marge-2867755.log`)
- 05:07 marge: `set -e; export CC=clang-21 CXX=clang++-21; make check; cargo clippy --workspace ` (exit 2, log `build-log/050723-marge-2926550.log`)
- 05:23 marge: `cargo fmt --all && cargo test -p ocw-render -p ocw-client -p ocw-ui -p ocw-deskt` (exit 1, log `build-log/052322-marge-2943805.log`)
- 06:32 marge: `scripts/render-scenes.sh --out test-output/scenes/2026-11-17-063237 --only 'char` (exit 1, log `build-log/063237-marge-3029356.log`)
- 08:26 marge: `cargo fmt --all --check && cargo clippy --workspace --all-targets -- -D warnings` (exit 101, log `build-log/082653-marge-3161008.log`)
- 08:35 Weela: `foreach ($f in "scripts\ocw-kiosk.ps1","scripts\win-gui-run.ps1") { $e = $null; ` (exit 1, log `build-log/083534-Weela-3171211.log`)
- 08:36 Weela: `$ProgressPreference = "SilentlyContinue"; Set-ExecutionPolicy -Scope Process Byp` (exit 1, log `build-log/083606-Weela-3172091.log`)
- 08:39 Weela: `& ([scriptblock]::Create([Text.Encoding]::UTF8.GetString([Convert]::FromBase64St` (exit 1, log `build-log/083919-Weela-3176352.log`)
- 09:20 Weela: `cargo clippy -q -p ocw-desktop -p ocw-xr-openxr -p ocw-render --features ocw-des` (exit 1, log `build-log/092045-Weela-3232452.log`)
- 10:13 marge: `cargo fmt --all --check && cargo test -q -p ocw-render quality 2>&1 | grep -E "t` (exit 1, log `build-log/101324-marge-3300488.log`)
- 10:10 Weela: `cargo clippy -q -p ocw-desktop -p ocw-xr-openxr -p ocw-render --features ocw-des` (exit 255, log `build-log/101018-Weela-3297010.log`)
- 15:40 Win11Builder: `cargo clippy -p ocw-assets -p ocw-sim -p ocw-client -p ocw-render -p ocw-desktop` (exit 101, log `build-log/154040-Win11Builder-3692409.log`)
- 17:17 marge: `scripts/render-scenes.sh --out test-output/scenes/ground-thumbs-before --only 's` (exit 1, log `build-log/171706-marge-3815265.log`)
- 18:20 Win11Builder: `cargo clippy -p ocw-render --all-targets -- -D warnings 2>&1 | Select-Object -La` (exit 101, log `build-log/182025-Win11Builder-3893786.log`)
- 18:52 marge: `cargo fmt --all -- --check` (exit 1, log `build-log/185253-marge-3928306.log`)
- 19:49 marge: `source ~/.cargo/env; cargo fmt --all -- --check >/dev/null; echo FMT=$?; cargo t` (exit 1, log `build-log/194900-marge-4013893.log`)
- 20:06 marge: `cargo fmt --all --check && echo FMT-OK` (exit 1, log `build-log/200617-marge-4045241.log`)
- 20:06 marge: `cargo fmt --all --check >/dev/null && echo FMT-OK` (exit 1, log `build-log/200641-marge-4046111.log`)
- 20:24 Win11Builder: `powershell -NoProfile -ExecutionPolicy Bypass -File scripts\windows-icon-check.p` (exit 101, log `build-log/202410-Win11Builder-4064923.log`)
- 20:29 Weela: `Set-ExecutionPolicy -Scope Process Bypass -Force; & .\scripts\vr-soak.ps1 -Minut` (exit 255, log `build-log/202953-Weela-4071465.log`)
- 20:52 Weela: `Set-ExecutionPolicy -Scope Process Bypass -Force; $w = Join-Path $env:LOCALAPPDA` (exit 255, log `build-log/205205-Weela-4097070.log`)
- 21:24 Win11Builder: `cargo clippy -p ocw-assets --all-targets -- -D warnings 2>&1 | Select-Object -La` (exit 101, log `build-log/212420-Win11Builder-4150511.log`)
- 21:23 marge: `export OCW_FEATURES=vr; .claude/skills/run-ocw/drive.sh shot-wayland test-output` (exit 2, log `build-log/212317-marge-4149223.log`)
- 22:05 macos: `cargo clippy -p ocw-ui -p ocw-studio -p ocw-desktop -p ocw-winres --all-targets ` (exit 1, log `build-log/220539-macos-17141.log`)
- 22:21 marge: `cargo fmt --all && cargo test -p ocw-assets 2>&1 | tail -80; ls ~/.local/opt/ble` (exit 1, log `build-log/222124-marge-37456.log`)
- 23:09 Win11Builder: `cargo clippy -p ocw-world -p ocw-worldgen -p ocw-worldstore -p ocw-sim -p ocw-re` (exit 101, log `build-log/230956-Win11Builder-139523.log`)
- 23:50 macos: `cargo fmt --all; cargo clippy -p ocw-ui -p ocw-studio -p ocw-desktop --all-targe` (exit 1, log `build-log/235031-macos-214074.log`)

Longest runs:

- 98 min on marge: `cargo fmt --all; make check 2>&1 | grep -E "^test result|FAILED|^error|^warning|`
- 96 min on marge: `source ~/.cargo/env; set -o pipefail; r(){ echo "=== $*"; "$@" > /tmp/ocw-sel-$$`
- 95 min on marge: `bash .q9-checks.sh`
- 92 min on marge: `r(){ "$@" > /tmp/a0abe-step.log 2>&1; s=$?; echo "STEP $* => $s"; [ $s -ne 0 ] &`
- 77 min on marge: `set -e; export CC=clang-21 CXX=clang++-21; make check; cargo clippy --workspace `

## Token usage

2.07 B tokens in 6,001 model messages (output 3.9 M, cache reads 2.03 B, cache writes 34.2 M, uncached input 13 k). Full breakdown: [tokens.json](tokens.json).

| Feature | Tokens | Output | Messages |
|---|---|---|---|
| Other | 709.4 M | 1.1 M | 1,885 |
| Planning & spec | 502.9 M | 639 k | 1,047 |
| UI & menus | 329.8 M | 863 k | 1,105 |
| Audio & voice | 177.1 M | 434 k | 567 |
| Riders & bikes | 154.2 M | 407 k | 555 |
| Art project | 96.2 M | 245 k | 488 |
| Worlds & terrain | 84.8 M | 200 k | 330 |
| Materials & look | 7.6 M | 6 k | 9 |
| Build, release & infra | 3.6 M | 4 k | 8 |
| Multiplayer & server | 2.2 M | 5 k | 6 |
| Sky, time & weather | 467 k | 0 k | 1 |

| Task | Feature | Tokens | Output |
|---|---|---|---|
| agent: Character editor refined (Phase 4, 4N) | Planning & spec | 268.0 M | 218 k |
| agent: Character editor step 2: pictures, face cam, hands | Other | 249.5 M | 373 k |
| agent: VR session lost every ~60 s on Weela | Planning & spec | 138.6 M | 254 k |
| agent: Voice V3/V4: rooms, range, who hears me | Audio & voice | 94.1 M | 214 k |
| agent: VR: bike computer HUD, controllers, exit crash | UI & menus | 88.0 M | 194 k |
| coordination: make fog.legacy the default but keep the new mode as fog.new | Other | 86.5 M | 62 k |
| agent: VR kiosk mode on Weela | UI & menus | 71.3 M | 181 k |
| agent: Polish: palm, helmet hook, HUD overflow | UI & menus | 65.9 M | 143 k |
| agent: Ground detail: dirt, stones, plant debris | Planning & spec | 60.1 M | 142 k |
| agent: Voice: Block and per-rider volume (§7.1.7 Q9) | Audio & voice | 56.6 M | 148 k |
| coordination: q30: render me a couple of example and send me here before i answer | Other | 54.4 M | 29 k |
| agent: Fix floating meadow patches on Tenerife | Worlds & terrain | 51.6 M | 117 k |
| agent: Studio Models workspace viewer (E3) | Riders & bikes | 51.1 M | 179 k |
| agent: HUD navi map, lower right (retry) | UI & menus | 48.5 M | 193 k |
| agent: Road cracks and potholes | Other | 43.2 M | 157 k |
| agent: Workshop bike stand: part thumbnails and % gain | Riders & bikes | 40.3 M | 110 k |
| agent: OCW Build Diary Day 6 (2026-11-16) | Art project | 38.3 M | 80 k |
| agent: Fix groupset thumbnails and tree heights | Other | 38.1 M | 105 k |
| agent: Bike stand tiles: show whole thumbnail | Riders & bikes | 32.2 M | 101 k |
| agent: Fix hand grip orientation on the bars | Other | 30.7 M | 74 k |
| agent: Record drone videos (POV and outside) | Other | 26.5 M | 70 k |
| agent: Voice range: 5–10 m, selected always | Audio & voice | 26.1 M | 72 k |
| coordination: whats missing for the model viewer in studio? | Riders & bikes | 21.9 M | 9 k |
| agent: OCW Studio logo and app icons | Art project | 19.5 M | 74 k |
| coordination: can you send me a strava file for testing the upload manually? | Other | 18.3 M | 9 k |
| agent: Place names in packages and studio map | Worlds & terrain | 15.6 M | 73 k |
| agent: Calendar: Select button to set the date | Other | 13.1 M | 47 k |
| coordination: start weela vr kiosk | UI & menus | 12.8 M | 7 k |
| coordination: update the readme, replace artwork with newer pictures showing what the in game … | Art project | 11.4 M | 6 k |
| coordination: whats the difference between studio and world editor? | Worlds & terrain | 10.0 M | 4 k |
| coordination: on the VR settings issue, i have seen, that there is a bandwidth setting for the… | Planning & spec | 9.9 M | 10 k |
| agent: Q30 mock-ups: kit pickers as tiles | Other | 9.4 M | 37 k |
| coordination: add a map similar to the 2d map in the world builder to the HUD (lower right cor… | UI & menus | 9.4 M | 6 k |
| coordination: investigate why the VR app on weela keeps hanging | Planning & spec | 8.1 M | 6 k |
| agent: OCW logo as the Windows exe icon | Art project | 8.0 M | 49 k |
| coordination: link up | Other | 8.0 M | 2 k |
| coordination: you can shorten the 30 min test. it seems not to crash, but still lagging. so th… | Other | 8.0 M | 4 k |
| coordination: add skin tone selector to character editor | Other | 7.9 M | 5 k |
| coordination: what do you mean by "original narration text"? | Other | 7.9 M | 13 k |
| agent: HUD photo preview for 3 s | UI & menus | 7.0 M | 51 k |

## Prompts

86 prompts (full text: [prompts.md](prompts.md)).

| Time | Prompt |
|---|---|
| 00:15 | meta link now running as user |
| 00:17 | what do you mean by "original narration text"? |
| 00:30 | trigger creation of ART Project Day 6 |
| 00:51 | ready |
| 00:54 | any update on the art day 6? |
| 00:56 | VR: the HUD is pretty central, thats disturbing. put all the information in to a bike navi (e.g. similar to wahoo element bolt, just for ref |
| 00:57 | VT: mount the navi on the handlebar, central. a bit ahead of the handlebar. look at images to get an idea, |
| 01:03 | how to get in character editor? |
| 01:04 | install the latest already existing build on marge kiosk |
| 01:14 | planning -> spec: have a local config file in which all local settings are placed. when the desktop app starts, ask the user whether he woul |
| 01:16 | fix character editor: the character should be shown in screen and the accessories and changes should be visually and selectable. changes bec |
| 01:18 | bike tuning on bike stand: make smaller renderings of all selectable items. put an info on how many % gain it gives. |
| 01:20 | calendar: i miss the  select button that accepts and sets the selcted date. |
| 01:25 | redo the music for day 6, less squeeky and less happy. make something cooler with different drums styles |
| 01:26 | would be great to see the photographer and drones in the day 6 video. |
| 01:27 | if no video if the drone flying (pov and from putside) was recorded, create one |
| 01:28 | give the rider a mouth |
| 01:28 | and ears, eyes etc. |
| 01:32 | the "fog fix" looks strange. where did that need for it come frome? |
| 01:33 | whats the status rearding VR? |
| 01:37 | give the rider real hands |
| 01:48 | make fog.legacy the default but keep the new mode as fog.new |
| 06:50 | keep sending me the test images, i think this got lost. where would be the place to add this so that it does not get lost? |
| 08:24 | Implement and start a VR kiosk mode on the computer WELA. |
| 08:57 | stop the VR kiosk mode. The VR version keeps crashing: investigate and fix. I taped the headsets nose presence sensor, so you should be able |
| 08:58 | additionally, in VR i notices some flickering, investigate and stabilize. |
| 09:02 | can you send me a strava file for testing the upload manually? |
| 13:17 | add skin tone selector to character editor |
| 13:49 | Q28: yes, show without helmet. hang helmet on a hook on the wall. |
| 13:50 | Q29: fine |
| 13:50 | q30: render me a couple of example and send me here before i answer |
| 19:30 | start weela vr kiosk |
| 19:42 | start kiosk on weela again, whats the command? can you create a link on desktop? |
| 19:44 | add the ocw logo to the VR app, too. |
| 19:45 | investigate why the VR app on weela keeps hanging |
| 19:52 | update the question section in the build dashboard. add a job to do this periodically. |
| 19:53 | on the VR settings issue, i have seen, that there is a bandwidth setting for the meta link. maybe we need to increase this? |
| 20:00 | @"~/.claude/uploads/e04e9dc8-43c6-409c-a780-31815783e9fa/4991d5ef-2026-11-16_15-47-50.fit" i tested the file you sent me. it is accepted by  |
| 20:05 | i could test the usb cable for the VR gogles, let me know if you could pause the VR agent, so i can test. |
| 20:20 | teste weiter |
| 20:29 | link up |
| 20:35 | you can shorten the 30 min test. it seems not to crash, but still lagging. so there is some improvement |
| 20:51 | link up |
| 20:55 | this looked way better on weela, only little hangs in VR |
| 20:55 | i accindently closed the app |
| 20:58 | now i think vr crashed? |
| 21:00 | whats the difference between studio and world editor? |
| 21:05 | graphical cosmetic: the hand position on the handlebar looks wrong (upside down). check images on how the correct grip position and techniqu |
| 21:06 | graphical cosmetic (VR): the rider without the head looks weird, can show the head, but make sure that for the POV view its faded away? |
| 21:08 | VR mode: use the controls. create a sensible mapping. make one analog stick for front/back/left/right |
| 21:08 | start studio on marge |
| 21:10 | graphic enhancement: add some dirt, dust, stones, rockes, parts of plants/vegetation |
| 21:12 | whats the situation with the fit file for strava? |
| 21:14 | cleanup unneeded data on marge |
| 21:16 | send me ocw-test-ride-cycling.fit again |
| 21:21 | okay, this time i see the gps track in the activity. I had to select a map, maybe that was what I did wrong before. Just to show you an exam |
| 21:24 | yeah, the original fit file works, too. |
| 21:24 | weela is running out of battery because the power supply does not supply enough energy. |
| 21:28 | i changed the power profile on weela to balanced to save more energy |
| 21:36 | i updated weelas ip |
| 21:40 | i updated weelas ip |
| 21:40 | how to set windows network to private |
| 21:44 | how comes that after changing the ip airlink does not work anymore? |
| 21:50 | okay, headset is connected via usb |
| 21:51 | check weela |
| 21:54 | create a logo for the studio app and put it to artwork/logos. use it for studio binaries on all platforms |
| 21:57 | how long for weela test? battery is draining fast. watch it closely |
| 22:01 | will u start stodio on marge? |
| 22:07 | world builder: add names of cities. hide names of smaller places when it gets to crowded in the 2d map. |
| 22:07 | whats missing for the model viewer in studio? |
| 22:57 | deploy the latest desktop app to marge |
| 22:57 | add some cracks and potholes to the roads |
| 22:59 | continue VR development/testing on Weela |
| 23:01 | check for new weela ip |
| 23:03 | add a map similar to the 2d map in the world builder to the HUD (lower right corner). make it look like on a bike navi. |
| 23:05 | update the readme, replace artwork with newer pictures showing what the in game graphic looks like. update the github overview page for the  |
| 23:21 | just do the 5 minute check, headset connected |
| 23:31 | CLAUDE.MD: record videos and photos from the automated testing, also on VR. put this medias into the art project. |
| 23:37 | to determine the quality of the road (amount of cracks, potholes, defects, loose stones etc.) look at the OSM flag for the quality of the ta |
| 23:44 | yes, install ffmpeg on weela |
| 23:46 | start kiosk mode on wleela. add battery information for laptop weela and oculus to build dashboard |
| 23:50 | when a photo was taken, show it for 3 seconds in HUD |
| 23:51 | what version has the build you started on weela? i ask because it was running the desktop mirror in full screen and froze. i guess you need  |
| 23:53 | do we have a global config file where I could my strava account details? |
| 23:57 | add and use the devices.toml form that local config location as well. |
| 23:57 | add a default example strava config to that directory. |

## Features

29 spec versions added, 18 landed by a merge; 7 deploys, 0 releases.

| Spec | Feature | Landed | Check (marge) |
|---|---|---|---|
| 4.39 | Voice | 01:01 `732ac02` | – |
| 4.40 | Browsers join a ride hosted in the desktop app with V5 | 01:02 `0272f23` | – |
| 4.41 | Character editor | 01:05 `d2aa9e0` | – |
| 4.42 | A new account starts in sneakers, jeans and a hoodie on an old, rusty city bike | 01:08 `7f9b81e` | – |
| 4.43 | Riding needs no purchase | 01:12 `15cc6ae` | – |
| 4.44 | One local config file for all local settings, and a start choice in the desktop app | 01:15 `64f89b8` | – |
| 4.45 | The legacy fog is the default again | 02:22 `c4c2101` | – |
| 4.46 | Calendar | 04:04 `a3dfb1f` (merge) | ok at 04:27, 2 suites, 8 passed, 0 failed (commit) |
| 4.47 | Character editor refined, first step built in both apps | 04:04 `a3dfb1f` (merge) | ok at 04:27, 2 suites, 8 passed, 0 failed (commit) |
| 4.48 | Voice Block and per-rider volume built in both apps | 05:06 `d346868` (merge) | ok at 03:48 (branch) |
| 4.49 | Bike stand | 05:06 `dcf5683` (merge) | ok at 02:32 (branch) |
| 4.50 | Dev cameras on the ride photographer's drone for videos | 05:07 `e97fefe` (merge) | exit 2 at 05:07 (commit) |
| 4.51 | Voice by range and audience built in both apps, V3 and V4 | 10:02 `cc32a0f` (merge) | ok at 09:54, 3 suites, 315 passed, 0 failed (branch) |
| 4.52 | Character editor, second step built in both apps | 13:31 `56894d9` (merge) | ok at 14:01, 3 suites, 140 passed, 0 failed (commit) |
| 4.53 | Hair is edited and shown without the helmet | 13:49 `e804355` | – |
| 4.54 | The hair page keeps pictures only, with the focused style named at the top | 13:50 `73cc35c` | – |
| 4.55 | The rider has real hands, and the character editor takes the helmet off for the hair and… | 14:53 `85995be` (merge) | ok at 15:55, 40 suites, 2758 passed, 0 failed (commit) |
| 4.56 | Field stands lie on the drawn terrain | 16:37 `7af2efa` (merge) | – |
| 4.57 | Five visible defects fixed | 16:46 `61fd990` (merge) | ok at 16:23 (commit) |
| 4.58 | Trees, bushes, lamps and posts stand on the drawn terrain | 18:09 `cf98fa2` (merge) | ok at 18:38 (commit) |
| 4.59 | The bike stand's and the character editor's tiles draw the whole thumbnail | 18:42 `b4c8a6a` (merge) | ok at 18:46, 1 suites, 11 passed, 0 failed (commit) |
| 4.60 | Thumbnails framed tight and centred | 19:19 `988e01a` (merge) | ok at 19:21, 1 suites, 12 passed, 0 failed (commit) |
| 4.61 | Voice | 19:36 `3d83682` | – |
| 4.62 | Drivetrain thumbnails without the wheels, square on from the drive side | 19:49 `89f7dd9` (merge) | – |
| 4.63 | The build dashboard's open questions are kept current | 19:56 `ef130d9` | – |
| 4.64 | The Windows executables carry the OCW logo | 20:47 `c09b638` (merge) | ok at 21:55, 1 suites, 12 passed, 0 failed (commit) |
| 4.65 | Strava | 22:19 `162ae1c` (merge) | ok at 23:56, 40 suites, 2716 passed, 0 failed (commit) |
| 4.66 | Voice heard only close by | 22:19 `162ae1c` (merge) | ok at 23:56, 40 suites, 2716 passed, 0 failed (commit) |
| 4.68 | OCW Studio has its own logo | 23:11 `ccc5d76` (merge) | ok at 23:11, 71 suites, 2797 passed, 0 failed (commit) |

Deploys:

- 08:36 Weela: `a879904-dirty` (exit 1)
- 08:40 Weela: `8f1a170` (ok)
- 08:51 Weela: `25e7c0f` (ok)
- 08:54 Weela: `f522112` (ok)
- 19:31 Weela: `518cc98` (ok)
- 22:57 marge: `162ae1c` (ok)
- 23:46 Weela: `71dd998-dirty` (ok)

## Agent jobs

31 jobs (coordinator log agents.jsonl).

| Task | Branch | Start | End | Status | Interrupted | Merged |
|---|---|---|---|---|---|---|
| Render distance slider and dynamic mode (Phase 10, 10G) | a6eb7544 | 00:53 | 00:53 | merged |  |  |
| Ride photographer visible to other riders (§2.11, Q5) | a54266de | 00:53 | 00:53 | merged |  |  |
| OCW Build Diary Day 6 (2026-11-16) | ad1bc0c8 | 00:54 | 04:43 | reported |  |  |
| VR: bike computer instead of the central HUD, Touch controllers, exit crash (Phase 11) | a2ef93fb | 00:57 | 03:16 | reported |  |  |
| Voice: Block and per-rider volume (§7.1.7 Q9) | ad1e25db | 01:02 | 06:10 | merged |  |  |
| Workshop bike stand: part thumbnails and % gain | a0abe702 | 01:18 | 06:10 | merged |  |  |
| Calendar: Select button that sets the selected date | a9abb1ed | 01:21 | 04:01 | merged |  |  |
| Drone videos for the art project: POV and outside | aef8b101 | 01:27 | 06:10 | merged |  |  |
| Character editor refined (Phase 4, 4N) | ae162327 | 03:12 | 05:05 | merged |  |  |
| Character editor step 2: picture tiles, face camera, mirror tiles, hands (4N) | a21d0417 | 05:07 | 14:53 | merged |  |  |
| Voice V3/V4: range, who hears me, selected riders (§7.1) | a351b5f9 | 08:01 | 10:02 | merged |  |  |
| VR kiosk mode on Weela (Phase 11) | ac25994d | 08:24 | 10:55 | reported |  |  |
| Q30 mock-ups: kit pickers as tiles with colour swatches | a305124f | 13:51 | 14:28 | reported |  |  |
| Fix floating land-use patches (Tenerife) | ad3d60b8 | 15:02 | 16:38 | merged |  |  |
| Polish: palm, helmet hook, standing hands, HUD overflow, bike stand card | a7fb2fcb | 15:02 | 17:11 | merged |  |  |
| Fix groupset thumbnails and object heights on terrace edges | a5f445cd | 17:11 | 18:09 | merged |  |  |
| Bike stand tiles: show the whole thumbnail | a5378106 | 18:10 | 19:49 | merged |  |  |
| Voice range: fade 5–10 m, selected riders always audible (Q20) | a24df017 | 19:36 | 22:19 | merged |  |  |
| OCW logo as the Windows exe icon (VR kiosk shortcuts) | a0f193dd | 19:44 | 21:01 | merged |  |  |
| VR session lost every ~60 s on Weela (hangs) | a716a1c9 | 19:46 | 23:35 | reported | 1 |  |
| Fix hand grip orientation on the bars | ad1da90d | 21:05 | 23:38 | merged |  |  |
| Ground detail: dirt, dust, stones, rocks, plant debris | a95d1490 | 21:10 |  | started |  |  |
| OCW Studio logo and app icons on all platforms | a03e9957 | 21:54 | 23:11 | reported |  |  |
| Place names in world packages and the studio 2D map | a57dfc7b | 22:08 |  | started |  |  |
| Studio Models workspace: viewer, stats, validator, try-on (E3) + M2 diff/validator | a64cacd3 | 22:08 |  | started |  |  |
| Road cracks and potholes | a01e4422 | 22:58 |  | started |  |  |
| HUD navi map (lower right), like a bike computer | ad244726 | 23:03 | 23:04 | abandoned |  |  |
| HUD navi map (lower right), like a bike computer | ad1a2665 | 23:04 |  | started |  |  |
| README: new in-game pictures | a98ff53f | 23:05 |  | started |  |  |
| Dashboard: battery of Weela and the Quest | a578ee7f | 23:46 |  | started |  |  |
| HUD: show a new photo for 3 s | aa66d7f8 | 23:51 |  | started |  |  |

## Incidents

94 collected (disk-full 1, janitor-delete 83, machine-offline 5, machine-online 4, runs-failed 1), 0 with root-cause notes ([incidents.md](incidents.md)).

| Time | Kind | Machine | What |
|---|---|---|---|
| 00:00 | machine-offline | leela | leela unreachable (no route to host) |
| 00:35 | janitor-delete | marge | janitor delete OCW/target (0.4 GB) |
| 00:53 | janitor-delete | marge | janitor delete OCW-worktree-agent-a6eb7544099a15ede/target (50.2 GB) |
| 01:56 | janitor-delete | marge | janitor delete OCW-worktree-agent-a54266deef98aa31a/target (40.7 GB) |
| 01:56 | janitor-delete | marge | janitor delete OCW/target (0.3 GB) |
| 02:35 | janitor-delete | marge | janitor delete OCW/target (0.3 GB) |
| 03:37 | janitor-delete | marge | janitor delete OCW/target (1.4 GB) |
| 03:48 | janitor-delete | marge | janitor delete OCW/target (0.3 GB) |
| 04:02 | janitor-delete | marge | janitor delete OCW-worktree-agent-a9abb1ed44c38c6f6/target (36.8 GB) |
| 05:05 | janitor-delete | marge | janitor delete OCW-worktree-agent-ae162327472ee5da2/target (55.3 GB) |
| 05:05 | janitor-delete | Win11Builder | janitor delete OCW-worktree-agent-ae162327472ee5da2/target (4.2 GB) |
| 05:05 | janitor-delete | macos | janitor delete OCW-worktree-agent-ae162327472ee5da2/target (13.1 GB) |
| 05:10 | janitor-delete | marge | janitor delete OCW/target (0.7 GB) |
| 05:20 | janitor-delete | marge | janitor delete OCW/target (0.1 GB) |
| 05:31 | janitor-delete | marge | janitor delete OCW/target (0.4 GB) |
| 06:10 | janitor-delete | marge | janitor delete OCW-worktree-agent-ad1e25db3ea4d58a1/target (30.8 GB) |
| 06:10 | janitor-delete | Win11Builder | janitor delete OCW-worktree-agent-ad1e25db3ea4d58a1/target (2.5 GB) |
| 06:10 | janitor-delete | macos | janitor delete OCW-worktree-agent-ad1e25db3ea4d58a1/target (1.2 GB) |
| 06:10 | janitor-delete | marge | janitor delete OCW-worktree-agent-a0abe70272d7e0e1f/target (36.0 GB) |
| 06:11 | janitor-delete | Win11Builder | janitor delete OCW-worktree-agent-a0abe70272d7e0e1f/target (2.5 GB) |
| 06:11 | janitor-delete | macos | janitor delete OCW-worktree-agent-a0abe70272d7e0e1f/target (1.5 GB) |
| 06:11 | janitor-delete | marge | janitor delete OCW-drone-camera-videos/target (18.4 GB) |
| 06:43 | janitor-delete | marge | janitor delete OCW/target (0.0 GB) |
| 08:34 | janitor-delete | marge | janitor delete OCW/target (0.3 GB) |
| 09:35 | janitor-delete | marge | janitor delete OCW/target (1.7 GB) |
| 10:03 | janitor-delete | marge | janitor delete OCW-worktree-agent-a351b5f9f0911b5f0/target (47.8 GB) |
| 10:03 | janitor-delete | Win11Builder | janitor delete OCW-worktree-agent-a351b5f9f0911b5f0/target (2.9 GB) |
| 10:35 | machine-offline | Weela | Weela unreachable (timeout) |
| 10:46 | janitor-delete | marge | janitor delete OCW/target (0.4 GB) |
| 11:46 | janitor-delete | marge | janitor delete OCW/target (0.3 GB) |
| 12:37 | janitor-delete | marge | janitor delete OCW/target (0.6 GB) |
| 12:47 | janitor-delete | marge | janitor delete OCW/target (0.0 GB) |
| 13:27 | janitor-delete | marge | janitor delete OCW/target (1.6 GB) |
| 13:38 | janitor-delete | marge | janitor delete OCW/target (0.3 GB) |
| 14:09 | janitor-delete | marge | janitor delete OCW/target (0.5 GB) |
| 14:22 | janitor-delete | marge | janitor delete OCW-char-editor-step2/target (52.2 GB) |
| 14:22 | janitor-delete | Win11Builder | janitor delete OCW-char-editor-step2/target (3.0 GB) |
| 14:22 | janitor-delete | macos | janitor delete OCW-char-editor-step2/target (0.5 GB) |
| 14:53 | janitor-delete | marge | janitor delete OCW-char-editor-hands/target (32.2 GB) |
| 14:54 | janitor-delete | Win11Builder | janitor delete OCW-char-editor-hands/target (2.5 GB) |
| 15:30 | janitor-delete | marge | janitor delete OCW/target (2.1 GB) |
| 16:38 | janitor-delete | marge | janitor delete OCW-worktree-agent-ad3d60b8ee2a5929c/target (34.8 GB) |
| 16:38 | janitor-delete | macos | janitor delete OCW-worktree-agent-ad3d60b8ee2a5929c/target (2.7 GB) |
| 16:52 | janitor-delete | marge | janitor delete OCW/target (1.7 GB) |
| 17:11 | janitor-delete | marge | janitor delete OCW-worktree-agent-a7fb2fcbf933aacae/target (39.6 GB) |
| 17:11 | janitor-delete | Win11Builder | janitor delete OCW-worktree-agent-a7fb2fcbf933aacae/target (2.9 GB) |
| 17:11 | janitor-delete | macos | janitor delete OCW-worktree-agent-a7fb2fcbf933aacae/target (7.6 GB) |
| 17:52 | janitor-delete | marge | janitor delete OCW/target (0.0 GB) |
| 18:02 | janitor-delete | marge | janitor delete OCW/target (0.0 GB) |
| 18:09 | janitor-delete | marge | janitor delete OCW-worktree-agent-a5f445cdd9033599f/target (25.4 GB) |
| 18:09 | janitor-delete | Win11Builder | janitor delete OCW-worktree-agent-a5f445cdd9033599f/target (1.8 GB) |
| 18:09 | janitor-delete | macos | janitor delete OCW-worktree-agent-a5f445cdd9033599f/target (4.6 GB) |
| 18:43 | janitor-delete | marge | janitor delete OCW/target (0.3 GB) |
| 18:53 | janitor-delete | marge | janitor delete OCW/target (0.3 GB) |
| 19:03 | janitor-delete | marge | janitor delete OCW/target (0.6 GB) |
| 19:30 | machine-online | Weela | Weela back online |
| 20:01 | disk-full | marge | disk home on marge at 90 % |
| 20:17 | janitor-delete | marge | janitor alert  (0.0 GB) |
| 20:27 | janitor-delete | marge | janitor alert  (0.0 GB) |
| 20:27 | janitor-delete | marge | janitor delete OCW/target (0.0 GB) |

## Media

| Time | File |
|---|---|
| 00:54:05 | [005405-shot-wayland-char-shape-anorexia-a-mirror.jpg](005405-shot-wayland-char-shape-anorexia-a-mirror.jpg) |
| 00:58:50 | [005850-shot-wayland-char-shape-anorexia-a-mirror.jpg](005850-shot-wayland-char-shape-anorexia-a-mirror.jpg) |
| 01:02:35 | [010235-shot-wayland-char-shape-normal-b-mirror.jpg](010235-shot-wayland-char-shape-normal-b-mirror.jpg) |
| 01:02:45 | [010245-shot-wayland-char-shape-obese-b-ride.jpg](010245-shot-wayland-char-shape-obese-b-ride.jpg) |
| 01:02:56 | [010256-shot-wayland-char-age-70plus.jpg](010256-shot-wayland-char-age-70plus.jpg) |
| 01:03:06 | [010306-shot-wayland-char-hair-two-braids.jpg](010306-shot-wayland-char-hair-two-braids.jpg) |
| 01:03:16 | [010316-shot-wayland-char-beard-full.jpg](010316-shot-wayland-char-beard-full.jpg) |
| 01:03:57 | [010357-shot-wayland-char-shape-anorexia-a-mirror.jpg](010357-shot-wayland-char-shape-anorexia-a-mirror.jpg) |
| 01:04:07 | [010407-shot-wayland-char-shape-anorexia-a-ride.jpg](010407-shot-wayland-char-shape-anorexia-a-ride.jpg) |
| 01:04:16 | [010416-shot-wayland-char-shape-anorexia-b-mirror.jpg](010416-shot-wayland-char-shape-anorexia-b-mirror.jpg) |
| 01:04:26 | [010426-shot-wayland-char-shape-anorexia-b-ride.jpg](010426-shot-wayland-char-shape-anorexia-b-ride.jpg) |
| 01:04:34 | [010434-shot-wayland-char-shape-anorexia-c-mirror.jpg](010434-shot-wayland-char-shape-anorexia-c-mirror.jpg) |
| 01:04:45 | [010445-shot-wayland-char-shape-anorexia-c-ride.jpg](010445-shot-wayland-char-shape-anorexia-c-ride.jpg) |
| 01:04:53 | [010453-shot-wayland-char-shape-skinny-a-mirror.jpg](010453-shot-wayland-char-shape-skinny-a-mirror.jpg) |
| 01:05:03 | [010503-shot-wayland-char-shape-skinny-a-ride.jpg](010503-shot-wayland-char-shape-skinny-a-ride.jpg) |
| 01:05:12 | [010512-shot-wayland-char-shape-skinny-b-mirror.jpg](010512-shot-wayland-char-shape-skinny-b-mirror.jpg) |
| 01:05:22 | [010522-shot-wayland-char-shape-skinny-b-ride.jpg](010522-shot-wayland-char-shape-skinny-b-ride.jpg) |
| 01:05:30 | [010530-shot-wayland-char-shape-skinny-c-mirror.jpg](010530-shot-wayland-char-shape-skinny-c-mirror.jpg) |
| 01:05:41 | [010541-shot-wayland-char-shape-skinny-c-ride.jpg](010541-shot-wayland-char-shape-skinny-c-ride.jpg) |
| 01:05:49 | [010549-shot-wayland-char-shape-slim-a-mirror.jpg](010549-shot-wayland-char-shape-slim-a-mirror.jpg) |
| 01:06:00 | [010600-shot-wayland-char-shape-slim-a-ride.jpg](010600-shot-wayland-char-shape-slim-a-ride.jpg) |
| 01:06:08 | [010608-shot-wayland-char-shape-slim-b-mirror.jpg](010608-shot-wayland-char-shape-slim-b-mirror.jpg) |
| 01:06:18 | [010618-shot-wayland-char-shape-slim-b-ride.jpg](010618-shot-wayland-char-shape-slim-b-ride.jpg) |
| 01:06:27 | [010627-shot-wayland-char-shape-slim-c-mirror.jpg](010627-shot-wayland-char-shape-slim-c-mirror.jpg) |
| 01:06:37 | [010637-shot-wayland-char-shape-slim-c-ride.jpg](010637-shot-wayland-char-shape-slim-c-ride.jpg) |
| 01:06:45 | [010645-shot-wayland-char-shape-normal-a-mirror.jpg](010645-shot-wayland-char-shape-normal-a-mirror.jpg) |
| 01:06:56 | [010656-shot-wayland-char-shape-normal-a-ride.jpg](010656-shot-wayland-char-shape-normal-a-ride.jpg) |
| 01:07:04 | [010704-shot-wayland-char-shape-normal-b-mirror.jpg](010704-shot-wayland-char-shape-normal-b-mirror.jpg) |
| 01:07:14 | [010714-shot-wayland-char-shape-normal-b-ride.jpg](010714-shot-wayland-char-shape-normal-b-ride.jpg) |
| 01:07:23 | [010723-shot-wayland-char-shape-normal-c-mirror.jpg](010723-shot-wayland-char-shape-normal-c-mirror.jpg) |
| 01:07:33 | [010733-shot-wayland-char-shape-normal-c-ride.jpg](010733-shot-wayland-char-shape-normal-c-ride.jpg) |
| 01:07:42 | [010742-shot-wayland-char-shape-ample-a-mirror.jpg](010742-shot-wayland-char-shape-ample-a-mirror.jpg) |
| 01:07:52 | [010752-shot-wayland-char-shape-ample-a-ride.jpg](010752-shot-wayland-char-shape-ample-a-ride.jpg) |
| 01:08:00 | [010800-shot-wayland-char-shape-ample-b-mirror.jpg](010800-shot-wayland-char-shape-ample-b-mirror.jpg) |
| 01:08:11 | [010811-shot-wayland-char-shape-ample-b-ride.jpg](010811-shot-wayland-char-shape-ample-b-ride.jpg) |
| 01:08:19 | [010819-shot-wayland-char-shape-ample-c-mirror.jpg](010819-shot-wayland-char-shape-ample-c-mirror.jpg) |
| 01:08:30 | [010830-shot-wayland-char-shape-ample-c-ride.jpg](010830-shot-wayland-char-shape-ample-c-ride.jpg) |
| 01:08:38 | [010838-shot-wayland-char-shape-fat-a-mirror.jpg](010838-shot-wayland-char-shape-fat-a-mirror.jpg) |
| 01:08:48 | [010848-shot-wayland-char-shape-fat-a-ride.jpg](010848-shot-wayland-char-shape-fat-a-ride.jpg) |
| 01:08:57 | [010857-shot-wayland-char-shape-fat-b-mirror.jpg](010857-shot-wayland-char-shape-fat-b-mirror.jpg) |
| 01:09:07 | [010907-shot-wayland-char-shape-fat-b-ride.jpg](010907-shot-wayland-char-shape-fat-b-ride.jpg) |
| 01:10:37 | [011037-shot-wayland-char-shape-fat-c-mirror.jpg](011037-shot-wayland-char-shape-fat-c-mirror.jpg) |
| 01:12:52 | [011252-shot-wayland-char-shape-fat-c-ride.jpg](011252-shot-wayland-char-shape-fat-c-ride.jpg) |
| 01:13:11 | [011311-shot-wayland-char-shape-obese-a-mirror.jpg](011311-shot-wayland-char-shape-obese-a-mirror.jpg) |
| 01:13:37 | [011337-shot-wayland-char-shape-obese-a-ride.jpg](011337-shot-wayland-char-shape-obese-a-ride.jpg) |
| 01:13:46 | [011346-shot-wayland-char-shape-obese-b-mirror.jpg](011346-shot-wayland-char-shape-obese-b-mirror.jpg) |
| 01:13:56 | [011356-shot-wayland-char-shape-obese-b-ride.jpg](011356-shot-wayland-char-shape-obese-b-ride.jpg) |
| 01:14:05 | [011405-shot-wayland-char-shape-obese-c-mirror.jpg](011405-shot-wayland-char-shape-obese-c-mirror.jpg) |
| 01:14:15 | [011415-shot-wayland-char-shape-obese-c-ride.jpg](011415-shot-wayland-char-shape-obese-c-ride.jpg) |
| 01:14:26 | [011426-shot-wayland-char-age-20s.jpg](011426-shot-wayland-char-age-20s.jpg) |
| 01:14:36 | [011436-shot-wayland-char-age-30s.jpg](011436-shot-wayland-char-age-30s.jpg) |
| 01:14:47 | [011447-shot-wayland-char-age-40s.jpg](011447-shot-wayland-char-age-40s.jpg) |
| 01:14:57 | [011457-shot-wayland-char-age-50s.jpg](011457-shot-wayland-char-age-50s.jpg) |
| 01:15:08 | [011508-shot-wayland-char-age-60s.jpg](011508-shot-wayland-char-age-60s.jpg) |
| 01:15:18 | [011518-shot-wayland-char-age-70plus.jpg](011518-shot-wayland-char-age-70plus.jpg) |
| 01:15:29 | [011529-shot-wayland-char-hair-short.jpg](011529-shot-wayland-char-hair-short.jpg) |
| 01:15:39 | [011539-shot-wayland-char-hair-buzz-cut.jpg](011539-shot-wayland-char-hair-buzz-cut.jpg) |
| 01:15:50 | [011550-shot-wayland-char-hair-long.jpg](011550-shot-wayland-char-hair-long.jpg) |
| 01:16:03 | [011603-shot-wayland-char-hair-ponytail.jpg](011603-shot-wayland-char-hair-ponytail.jpg) |
| 01:16:13 | [011613-shot-wayland-char-hair-bun.jpg](011613-shot-wayland-char-hair-bun.jpg) |
| 01:16:24 | [011624-shot-wayland-char-hair-bald.jpg](011624-shot-wayland-char-hair-bald.jpg) |
| 01:16:34 | [011634-shot-wayland-char-hair-shaved.jpg](011634-shot-wayland-char-hair-shaved.jpg) |
| 01:16:45 | [011645-shot-wayland-char-hair-crew-cut.jpg](011645-shot-wayland-char-hair-crew-cut.jpg) |
| 01:16:55 | [011655-shot-wayland-char-hair-short-textured.jpg](011655-shot-wayland-char-hair-short-textured.jpg) |
| 01:17:06 | [011706-shot-wayland-char-hair-side-part.jpg](011706-shot-wayland-char-hair-side-part.jpg) |
| 01:17:16 | [011716-shot-wayland-char-hair-short-curly.jpg](011716-shot-wayland-char-hair-short-curly.jpg) |
| 01:17:27 | [011727-shot-wayland-char-hair-afro.jpg](011727-shot-wayland-char-hair-afro.jpg) |
| 01:17:37 | [011737-shot-wayland-char-hair-pixie.jpg](011737-shot-wayland-char-hair-pixie.jpg) |
| 01:17:48 | [011748-shot-wayland-char-hair-mid-length.jpg](011748-shot-wayland-char-hair-mid-length.jpg) |
| 01:18:08 | [011808-shot-wayland-char-editor-menu-body.jpg](011808-shot-wayland-char-editor-menu-body.jpg) |
| 01:18:08 | [011808-shot-wayland-char-hair-long-curly.jpg](011808-shot-wayland-char-hair-long-curly.jpg) |
| 01:18:22 | [011822-shot-wayland-char-hair-low-ponytail.jpg](011822-shot-wayland-char-hair-low-ponytail.jpg) |
| 01:18:24 | [011824-shot-wayland-char-editor-menu-hair.jpg](011824-shot-wayland-char-editor-menu-hair.jpg) |
| 01:18:28 | [011828-shot-char-editor-menu-body.jpg](011828-shot-char-editor-menu-body.jpg) |
| 01:18:37 | [011837-shot-wayland-char-hair-single-braid.jpg](011837-shot-wayland-char-hair-single-braid.jpg) |
| 01:18:40 | [011840-shot-wayland-char-editor-mirror-hair.jpg](011840-shot-wayland-char-editor-mirror-hair.jpg) |
| 01:18:52 | [011852-shot-wayland-char-hair-two-braids.jpg](011852-shot-wayland-char-hair-two-braids.jpg) |
| 01:18:57 | [011857-shot-char-editor-menu-hair.jpg](011857-shot-char-editor-menu-hair.jpg) |
| 01:19:02 | [011902-shot-wayland-char-hair-low-bun.jpg](011902-shot-wayland-char-hair-low-bun.jpg) |
| 01:19:17 | [011917-shot-wayland-char-hair-locs-tied-back.jpg](011917-shot-wayland-char-hair-locs-tied-back.jpg) |
| 01:19:27 | [011927-shot-wayland-char-hair-cornrows.jpg](011927-shot-wayland-char-hair-cornrows.jpg) |
| 01:19:38 | [011938-shot-wayland-char-moustache-classic.jpg](011938-shot-wayland-char-moustache-classic.jpg) |
| 01:19:39 | [011939-shot-char-editor-mirror-hair.jpg](011939-shot-char-editor-mirror-hair.jpg) |
| 01:19:48 | [011948-shot-wayland-char-moustache-chevron.jpg](011948-shot-wayland-char-moustache-chevron.jpg) |
| 01:19:59 | [011959-shot-wayland-char-moustache-handlebar.jpg](011959-shot-wayland-char-moustache-handlebar.jpg) |
| 01:20:09 | [012009-shot-wayland-char-moustache-horseshoe.jpg](012009-shot-wayland-char-moustache-horseshoe.jpg) |
| 01:20:20 | [012020-shot-wayland-char-moustache-pencil.jpg](012020-shot-wayland-char-moustache-pencil.jpg) |
| 01:20:30 | [012030-shot-wayland-char-beard-stubble.jpg](012030-shot-wayland-char-beard-stubble.jpg) |
| 01:20:41 | [012041-shot-wayland-char-beard-short-stubble-beard.jpg](012041-shot-wayland-char-beard-short-stubble-beard.jpg) |
| 01:20:51 | [012051-shot-wayland-char-beard-short-boxed.jpg](012051-shot-wayland-char-beard-short-boxed.jpg) |
| 01:21:02 | [012102-shot-wayland-char-beard-full.jpg](012102-shot-wayland-char-beard-full.jpg) |
| 01:21:12 | [012112-shot-wayland-char-beard-goatee.jpg](012112-shot-wayland-char-beard-goatee.jpg) |
| 01:21:22 | [012122-shot-wayland-char-beard-chin-strap.jpg](012122-shot-wayland-char-beard-chin-strap.jpg) |
| 01:21:33 | [012133-shot-wayland-char-beard-long.jpg](012133-shot-wayland-char-beard-long.jpg) |
| 01:23:06 | [012306-shot-char-shape-anorexia-a-mirror.jpg](012306-shot-char-shape-anorexia-a-mirror.jpg) |
| 01:24:33 | [012433-shot-char-shape-anorexia-a-ride.jpg](012433-shot-char-shape-anorexia-a-ride.jpg) |
| 01:25:22 | [012522-shot-char-shape-anorexia-b-mirror.jpg](012522-shot-char-shape-anorexia-b-mirror.jpg) |
| 01:25:45 | [012545-shot-char-shape-anorexia-b-ride.jpg](012545-shot-char-shape-anorexia-b-ride.jpg) |
| 01:26:37 | [012637-shot-char-shape-anorexia-c-mirror.jpg](012637-shot-char-shape-anorexia-c-mirror.jpg) |
| 01:27:17 | [012717-shot-char-shape-anorexia-c-ride.jpg](012717-shot-char-shape-anorexia-c-ride.jpg) |
| 01:28:27 | [012827-shot-char-shape-skinny-a-mirror.jpg](012827-shot-char-shape-skinny-a-mirror.jpg) |
| 01:29:08 | [012908-shot-char-shape-skinny-a-ride.jpg](012908-shot-char-shape-skinny-a-ride.jpg) |
| 01:29:28 | [012928-readme-readme-2026-11-17-bike-stand.jpg](012928-readme-readme-2026-11-17-bike-stand.jpg) |
| 01:29:28 | [012928-readme-readme-2026-11-17-browser.jpg](012928-readme-readme-2026-11-17-browser.jpg) |
| 01:29:28 | [012928-readme-readme-2026-11-17-hero.jpg](012928-readme-readme-2026-11-17-hero.jpg) |
| 01:29:28 | [012928-readme-readme-2026-11-17-malbun.jpg](012928-readme-readme-2026-11-17-malbun.jpg) |
| 01:29:28 | [012928-readme-readme-2026-11-17-mirror.jpg](012928-readme-readme-2026-11-17-mirror.jpg) |
| 01:29:28 | [012928-readme-readme-2026-11-17-rain.jpg](012928-readme-readme-2026-11-17-rain.jpg) |
| 01:29:28 | [012928-readme-readme-2026-11-17-rider-close.jpg](012928-readme-readme-2026-11-17-rider-close.jpg) |
| 01:29:28 | [012928-readme-readme-2026-11-17-schauinsland.jpg](012928-readme-readme-2026-11-17-schauinsland.jpg) |
| 01:29:28 | [012928-readme-readme-2026-11-17-sunset.jpg](012928-readme-readme-2026-11-17-sunset.jpg) |
| 01:29:28 | [012928-readme-readme-2026-11-17-teide.jpg](012928-readme-readme-2026-11-17-teide.jpg) |
| 01:29:28 | [012928-readme-readme-2026-11-17-vaduz-junction.jpg](012928-readme-readme-2026-11-17-vaduz-junction.jpg) |
| 01:30:11 | [013011-shot-char-shape-skinny-b-mirror.jpg](013011-shot-char-shape-skinny-b-mirror.jpg) |
| 01:30:46 | [013046-shot-char-shape-skinny-b-ride.jpg](013046-shot-char-shape-skinny-b-ride.jpg) |
| 01:31:34 | [013134-shot-char-shape-skinny-c-mirror.jpg](013134-shot-char-shape-skinny-c-mirror.jpg) |
| 01:32:48 | [013248-shot-char-shape-skinny-c-ride.jpg](013248-shot-char-shape-skinny-c-ride.jpg) |
| 01:35:03 | [013503-shot-char-shape-slim-a-mirror.jpg](013503-shot-char-shape-slim-a-mirror.jpg) |
| 01:35:37 | [013537-shot-char-shape-slim-a-ride.jpg](013537-shot-char-shape-slim-a-ride.jpg) |
| 01:36:23 | [013623-shot-char-shape-slim-b-mirror.jpg](013623-shot-char-shape-slim-b-mirror.jpg) |
| 01:36:50 | [013650-shot-char-shape-slim-b-ride.jpg](013650-shot-char-shape-slim-b-ride.jpg) |
| 01:37:40 | [013740-shot-char-shape-slim-c-mirror.jpg](013740-shot-char-shape-slim-c-mirror.jpg) |
| 01:38:22 | [013822-shot-char-shape-slim-c-ride.jpg](013822-shot-char-shape-slim-c-ride.jpg) |
| 01:39:26 | [013926-shot-char-shape-normal-a-mirror.jpg](013926-shot-char-shape-normal-a-mirror.jpg) |
| 01:40:05 | [014005-shot-char-shape-normal-a-ride.jpg](014005-shot-char-shape-normal-a-ride.jpg) |
| 01:41:09 | [014109-shot-char-shape-normal-b-mirror.jpg](014109-shot-char-shape-normal-b-mirror.jpg) |
| 01:41:48 | [014148-shot-char-shape-normal-b-ride.jpg](014148-shot-char-shape-normal-b-ride.jpg) |
| 01:42:51 | [014251-shot-char-shape-normal-c-mirror.jpg](014251-shot-char-shape-normal-c-mirror.jpg) |
| 01:43:51 | [014351-vr-weela-2026-11-17-left-eye-ahead.jpg](014351-vr-weela-2026-11-17-left-eye-ahead.jpg) |
| 01:43:51 | [014351-vr-weela-2026-11-17-left-eye-down.jpg](014351-vr-weela-2026-11-17-left-eye-down.jpg) |
| 01:44:06 | [014406-shot-char-shape-normal-c-ride.jpg](014406-shot-char-shape-normal-c-ride.jpg) |
| 01:45:08 | [014508-shot-char-shape-ample-a-mirror.jpg](014508-shot-char-shape-ample-a-mirror.jpg) |
| 01:45:48 | [014548-shot-char-shape-ample-a-ride.jpg](014548-shot-char-shape-ample-a-ride.jpg) |
| 01:46:48 | [014648-shot-char-shape-ample-b-mirror.jpg](014648-shot-char-shape-ample-b-mirror.jpg) |
| 01:47:26 | [014726-shot-char-shape-ample-b-ride.jpg](014726-shot-char-shape-ample-b-ride.jpg) |
| 01:48:33 | [014833-shot-char-shape-ample-c-mirror.jpg](014833-shot-char-shape-ample-c-mirror.jpg) |
| 01:49:15 | [014915-shot-char-shape-ample-c-ride.jpg](014915-shot-char-shape-ample-c-ride.jpg) |
| 01:50:21 | [015021-shot-char-shape-fat-a-mirror.jpg](015021-shot-char-shape-fat-a-mirror.jpg) |
| 01:51:01 | [015101-shot-char-shape-fat-a-ride.jpg](015101-shot-char-shape-fat-a-ride.jpg) |
| 01:52:02 | [015202-shot-char-shape-fat-b-mirror.jpg](015202-shot-char-shape-fat-b-mirror.jpg) |
| 01:52:42 | [015242-shot-char-shape-fat-b-ride.jpg](015242-shot-char-shape-fat-b-ride.jpg) |
| 01:53:23 | [015323-vr-weela-2026-11-17-left-eye-ahead-day.jpg](015323-vr-weela-2026-11-17-left-eye-ahead-day.jpg) |
| 01:53:23 | [015323-vr-weela-2026-11-17-left-eye-down-day.jpg](015323-vr-weela-2026-11-17-left-eye-down-day.jpg) |
| 01:53:48 | [015348-shot-char-shape-fat-c-mirror.jpg](015348-shot-char-shape-fat-c-mirror.jpg) |
| 01:54:28 | [015428-shot-char-shape-fat-c-ride.jpg](015428-shot-char-shape-fat-c-ride.jpg) |
| 01:55:26 | [015526-shot-char-shape-obese-a-mirror.jpg](015526-shot-char-shape-obese-a-mirror.jpg) |
| 01:55:56 | [015556-shot-char-shape-obese-a-ride.jpg](015556-shot-char-shape-obese-a-ride.jpg) |
| 01:56:55 | [015655-shot-char-shape-obese-b-mirror.jpg](015655-shot-char-shape-obese-b-mirror.jpg) |
| 01:57:29 | [015729-shot-char-shape-obese-b-ride.jpg](015729-shot-char-shape-obese-b-ride.jpg) |
| 01:58:20 | [015820-shot-char-shape-obese-c-mirror.jpg](015820-shot-char-shape-obese-c-mirror.jpg) |
| 01:58:59 | [015859-shot-char-shape-obese-c-ride.jpg](015859-shot-char-shape-obese-c-ride.jpg) |
| 01:59:43 | [015943-shot-char-age-20s.jpg](015943-shot-char-age-20s.jpg) |
| 02:00:25 | [020025-shot-char-age-30s.jpg](020025-shot-char-age-30s.jpg) |
| 02:01:07 | [020107-shot-char-age-40s.jpg](020107-shot-char-age-40s.jpg) |
| 02:01:52 | [020152-shot-char-age-50s.jpg](020152-shot-char-age-50s.jpg) |
| 02:02:33 | [020233-shot-char-age-60s.jpg](020233-shot-char-age-60s.jpg) |
| 02:03:13 | [020313-shot-char-age-70plus.jpg](020313-shot-char-age-70plus.jpg) |
| 02:03:55 | [020355-shot-char-hair-short.jpg](020355-shot-char-hair-short.jpg) |
| 02:04:38 | [020438-shot-char-hair-buzz-cut.jpg](020438-shot-char-hair-buzz-cut.jpg) |
| 02:05:22 | [020522-shot-char-hair-long.jpg](020522-shot-char-hair-long.jpg) |
| 02:06:04 | [020604-shot-char-hair-ponytail.jpg](020604-shot-char-hair-ponytail.jpg) |
| 02:06:44 | [020644-shot-char-hair-bun.jpg](020644-shot-char-hair-bun.jpg) |
| 02:07:14 | [020714-shot-char-hair-bald.jpg](020714-shot-char-hair-bald.jpg) |
| 02:07:57 | [020757-shot-char-hair-shaved.jpg](020757-shot-char-hair-shaved.jpg) |
| 02:08:31 | [020831-shot-char-hair-crew-cut.jpg](020831-shot-char-hair-crew-cut.jpg) |
| 02:08:55 | [020855-shot-char-hair-short-textured.jpg](020855-shot-char-hair-short-textured.jpg) |
| 02:09:16 | [020916-shot-char-hair-side-part.jpg](020916-shot-char-hair-side-part.jpg) |
| 02:09:37 | [020937-shot-char-hair-short-curly.jpg](020937-shot-char-hair-short-curly.jpg) |
| 02:09:57 | [020957-shot-char-hair-afro.jpg](020957-shot-char-hair-afro.jpg) |
| 02:10:17 | [021017-shot-char-hair-pixie.jpg](021017-shot-char-hair-pixie.jpg) |
| 02:10:42 | [021042-shot-char-hair-mid-length.jpg](021042-shot-char-hair-mid-length.jpg) |
| 02:11:04 | [021104-shot-char-hair-long-curly.jpg](021104-shot-char-hair-long-curly.jpg) |
| 02:11:35 | [021135-shot-char-hair-low-ponytail.jpg](021135-shot-char-hair-low-ponytail.jpg) |
| 02:12:03 | [021203-shot-char-hair-single-braid.jpg](021203-shot-char-hair-single-braid.jpg) |
| 02:12:29 | [021229-shot-char-hair-two-braids.jpg](021229-shot-char-hair-two-braids.jpg) |
| 02:13:00 | [021300-shot-char-hair-low-bun.jpg](021300-shot-char-hair-low-bun.jpg) |
| 02:14:21 | [021421-shot-char-hair-locs-tied-back.jpg](021421-shot-char-hair-locs-tied-back.jpg) |
| 02:14:57 | [021457-shot-char-hair-cornrows.jpg](021457-shot-char-hair-cornrows.jpg) |
| 02:15:33 | [021533-shot-char-moustache-classic.jpg](021533-shot-char-moustache-classic.jpg) |
| 02:16:07 | [021607-shot-char-moustache-chevron.jpg](021607-shot-char-moustache-chevron.jpg) |
| 02:16:43 | [021643-shot-char-moustache-handlebar.jpg](021643-shot-char-moustache-handlebar.jpg) |
| 02:17:02 | [021702-shot-wayland-char-editor-menu-body.jpg](021702-shot-wayland-char-editor-menu-body.jpg) |
| 02:17:11 | [021711-shot-wayland-char-editor-menu-hair.jpg](021711-shot-wayland-char-editor-menu-hair.jpg) |
| 02:17:20 | [021720-shot-char-moustache-horseshoe.jpg](021720-shot-char-moustache-horseshoe.jpg) |
| 02:17:21 | [021721-shot-wayland-char-editor-mirror-hair.jpg](021721-shot-wayland-char-editor-mirror-hair.jpg) |
| 02:17:33 | [021733-shot-wayland-char-editor-tiles-hair.jpg](021733-shot-wayland-char-editor-tiles-hair.jpg) |
| 02:17:43 | [021743-shot-wayland-char-editor-tiles-shape.jpg](021743-shot-wayland-char-editor-tiles-shape.jpg) |
| 02:17:54 | [021754-shot-wayland-char-editor-tiles-hair-colour.jpg](021754-shot-wayland-char-editor-tiles-hair-colour.jpg) |
| 02:17:55 | [021755-shot-char-moustache-pencil.jpg](021755-shot-char-moustache-pencil.jpg) |
| 02:18:05 | [021805-shot-wayland-char-face-front.jpg](021805-shot-wayland-char-face-front.jpg) |
| 02:18:16 | [021816-shot-wayland-char-face-three-quarter.jpg](021816-shot-wayland-char-face-three-quarter.jpg) |
| 02:18:27 | [021827-shot-wayland-char-face-side.jpg](021827-shot-wayland-char-face-side.jpg) |
| 02:18:29 | [021829-shot-char-beard-stubble.jpg](021829-shot-char-beard-stubble.jpg) |
| 02:18:38 | [021838-shot-wayland-char-face-70plus.jpg](021838-shot-wayland-char-face-70plus.jpg) |
| 02:18:48 | [021848-shot-wayland-char-face-muted.jpg](021848-shot-wayland-char-face-muted.jpg) |
| 02:18:55 | [021855-shot-char-beard-short-stubble-beard.jpg](021855-shot-char-beard-short-stubble-beard.jpg) |
| 02:19:24 | [021924-shot-char-editor-menu-body.jpg](021924-shot-char-editor-menu-body.jpg) |
| 02:19:26 | [021926-shot-char-beard-short-boxed.jpg](021926-shot-char-beard-short-boxed.jpg) |
| 02:20:02 | [022002-shot-char-beard-full.jpg](022002-shot-char-beard-full.jpg) |
| 02:20:05 | [022005-shot-char-editor-menu-hair.jpg](022005-shot-char-editor-menu-hair.jpg) |
| 02:20:24 | [022024-shot-char-beard-goatee.jpg](022024-shot-char-beard-goatee.jpg) |
| 02:20:42 | [022042-shot-char-editor-mirror-hair.jpg](022042-shot-char-editor-mirror-hair.jpg) |
| 02:20:47 | [022047-shot-char-beard-chin-strap.jpg](022047-shot-char-beard-chin-strap.jpg) |
| 02:21:08 | [022108-shot-char-editor-tiles-hair.jpg](022108-shot-char-editor-tiles-hair.jpg) |
| 02:21:09 | [022109-shot-char-beard-long.jpg](022109-shot-char-beard-long.jpg) |
| 02:21:32 | [022132-shot-char-editor-tiles-shape.jpg](022132-shot-char-editor-tiles-shape.jpg) |
| 02:21:33 | [022133-shot-char-editor-menu-body.jpg](022133-shot-char-editor-menu-body.jpg) |
| 02:21:58 | [022158-shot-char-editor-menu-hair.jpg](022158-shot-char-editor-menu-hair.jpg) |
| 02:21:58 | [022158-shot-char-editor-tiles-hair-colour.jpg](022158-shot-char-editor-tiles-hair-colour.jpg) |
| 02:22:30 | [022230-shot-char-face-front.jpg](022230-shot-char-face-front.jpg) |
| 02:22:48 | [022248-shot-char-editor-mirror-hair.jpg](022248-shot-char-editor-mirror-hair.jpg) |
| 02:23:03 | [022303-shot-char-face-three-quarter.jpg](022303-shot-char-face-three-quarter.jpg) |
| 02:23:40 | [022340-shot-char-face-side.jpg](022340-shot-char-face-side.jpg) |
| 02:24:23 | [022423-shot-char-face-70plus.jpg](022423-shot-char-face-70plus.jpg) |
| 02:25:07 | [022507-shot-char-face-muted.jpg](022507-shot-char-face-muted.jpg) |
| 02:26:33 | [022633-4n-character-shapes-mirror-wayland.jpg](022633-4n-character-shapes-mirror-wayland.jpg) |
| 02:26:35 | [022635-4n-character-ages-wayland.jpg](022635-4n-character-ages-wayland.jpg) |
| 02:26:35 | [022635-4n-character-shapes-ride-wayland.jpg](022635-4n-character-shapes-ride-wayland.jpg) |
| 02:26:37 | [022637-4n-character-hair-wayland.jpg](022637-4n-character-hair-wayland.jpg) |
| 02:26:38 | [022638-4n-character-facial-hair-wayland.jpg](022638-4n-character-facial-hair-wayland.jpg) |
| 02:26:40 | [022640-4n-character-shapes-mirror-x11.jpg](022640-4n-character-shapes-mirror-x11.jpg) |
| 02:26:42 | [022642-4n-character-shapes-ride-x11.jpg](022642-4n-character-shapes-ride-x11.jpg) |
| 02:26:43 | [022643-4n-character-ages-x11.jpg](022643-4n-character-ages-x11.jpg) |
| 02:26:45 | [022645-4n-character-hair-x11.jpg](022645-4n-character-hair-x11.jpg) |
| 02:26:46 | [022646-4n-character-facial-hair-x11.jpg](022646-4n-character-facial-hair-x11.jpg) |
| 02:26:47 | [022647-4n-character-editor-before-wayland.jpg](022647-4n-character-editor-before-wayland.jpg) |
| 02:26:49 | [022649-4n-character-editor-after-wayland.jpg](022649-4n-character-editor-after-wayland.jpg) |
| 02:26:50 | [022650-4n-character-editor-after-x11.jpg](022650-4n-character-editor-after-x11.jpg) |
| 02:42:14 | [024214-shot-wayland-bike-stand-tiles-wheels.jpg](024214-shot-wayland-bike-stand-tiles-wheels.jpg) |
| 02:42:41 | [024241-shot-wayland-bike-stand-tiles-capped.jpg](024241-shot-wayland-bike-stand-tiles-capped.jpg) |
| 02:43:07 | [024307-shot-wayland-bike-stand-tiles-paint.jpg](024307-shot-wayland-bike-stand-tiles-paint.jpg) |
| 02:43:33 | [024333-shot-wayland-bike-stand-tiles-profile-race.jpg](024333-shot-wayland-bike-stand-tiles-profile-race.jpg) |
| 03:09:12 | [030912-shot-wayland-bike-stand-tiles-wheels.jpg](030912-shot-wayland-bike-stand-tiles-wheels.jpg) |
| 03:09:38 | [030938-shot-wayland-bike-stand-tiles-capped.jpg](030938-shot-wayland-bike-stand-tiles-capped.jpg) |
| 03:10:05 | [031005-shot-wayland-bike-stand-tiles-paint.jpg](031005-shot-wayland-bike-stand-tiles-paint.jpg) |
| 03:10:31 | [031031-shot-wayland-bike-stand-tiles-profile-race.jpg](031031-shot-wayland-bike-stand-tiles-profile-race.jpg) |
| 03:15:32 | [031532-vr-weela-2026-11-17-vr-sim-down.jpg](031532-vr-weela-2026-11-17-vr-sim-down.jpg) |
| 03:43:03 | [034303-calendar-select-web-web-calendar-select.jpg](034303-calendar-select-web-web-calendar-select.jpg) |
| 03:43:03 | [034303-calendar-select-web-web-calendar.jpg](034303-calendar-select-web-web-calendar.jpg) |
| 03:43:03 | [034303-calendar-select-web-web-console.jpg](034303-calendar-select-web-web-console.jpg) |
| 03:43:03 | [034303-calendar-select-web-web-downloads-ocw-2026-11-17-03-44-16.jpg](034303-calendar-select-web-web-downloads-ocw-2026-11-17-03-44-16.jpg) |
| 03:43:03 | [034303-calendar-select-web-web-downloads-ocw-2026-11-17-03-44-20.webm](034303-calendar-select-web-web-downloads-ocw-2026-11-17-03-44-20.webm) |
| 03:43:03 | [034303-calendar-select-web-web-gamepad.jpg](034303-calendar-select-web-web-gamepad.jpg) |
| 03:43:03 | [034303-calendar-select-web-web-gps.jpg](034303-calendar-select-web-web-gps.jpg) |
| 03:43:03 | [034303-calendar-select-web-web-hud.jpg](034303-calendar-select-web-web-hud.jpg) |
| 03:43:03 | [034303-calendar-select-web-web-join.jpg](034303-calendar-select-web-web-join.jpg) |
| 03:43:03 | [034303-calendar-select-web-web-menu.jpg](034303-calendar-select-web-web-menu.jpg) |
| 03:43:03 | [034303-calendar-select-web-web-ride.jpg](034303-calendar-select-web-web-ride.jpg) |
| 03:43:03 | [034303-calendar-select-web-web-riders.jpg](034303-calendar-select-web-web-riders.jpg) |
| 03:43:03 | [034303-calendar-select-web-web-settings.jpg](034303-calendar-select-web-web-settings.jpg) |
| 03:43:03 | [034303-calendar-select-web-web-touch-hints.jpg](034303-calendar-select-web-web-touch-hints.jpg) |
| 03:43:03 | [034303-calendar-select-web-web-touch-hold.jpg](034303-calendar-select-web-web-touch-hold.jpg) |
| 03:43:03 | [034303-calendar-select-web-web-unicorn-flight.jpg](034303-calendar-select-web-web-unicorn-flight.jpg) |
| 03:43:03 | [034303-calendar-select-web-web-unicorn-inspect.jpg](034303-calendar-select-web-web-unicorn-inspect.jpg) |
| 03:43:03 | [034303-calendar-select-web-web-unicorn-menu.jpg](034303-calendar-select-web-web-unicorn-menu.jpg) |
| 03:43:03 | [034303-calendar-select-web-web-weather.jpg](034303-calendar-select-web-web-weather.jpg) |
| 03:43:03 | [034303-calendar-select-web-web.jpg](034303-calendar-select-web-web.jpg) |
| 03:46:17 | [034617-drone-videos-2026-11-17-drone-outside.jpg](034617-drone-videos-2026-11-17-drone-outside.jpg) |
| 03:47:03 | [034703-drone-videos-2026-11-17-drone-outside.mp4](034703-drone-videos-2026-11-17-drone-outside.mp4) |
| 03:48:04 | [034804-drone-videos-2026-11-17-drone-pov.jpg](034804-drone-videos-2026-11-17-drone-pov.jpg) |
| 03:48:10 | [034810-calendar-select-desktop-menu-time-calendar.jpg](034810-calendar-select-desktop-menu-time-calendar.jpg) |
| 03:48:32 | [034832-calendar-select-desktop-menu-time-calendar-select.jpg](034832-calendar-select-desktop-menu-time-calendar-select.jpg) |
| 03:48:38 | [034838-drone-videos-2026-11-17-drone-pov.mp4](034838-drone-videos-2026-11-17-drone-pov.mp4) |
| 03:50:23 | [035023-shot-bike-stand-tiles-wheels.jpg](035023-shot-bike-stand-tiles-wheels.jpg) |
| 03:57:26 | [035726-shot-bike-stand-tiles-capped.jpg](035726-shot-bike-stand-tiles-capped.jpg) |
| 03:58:26 | [035826-shot-bike-stand-tiles-paint.jpg](035826-shot-bike-stand-tiles-paint.jpg) |
| 03:59:25 | [035925-shot-bike-stand-tiles-profile-race.jpg](035925-shot-bike-stand-tiles-profile-race.jpg) |
| 04:27:56 | [042756-drone-videos-2026-11-17-drone-outside.jpg](042756-drone-videos-2026-11-17-drone-outside.jpg) |
| 04:28:52 | [042852-drone-videos-2026-11-17-drone-outside.mp4](042852-drone-videos-2026-11-17-drone-outside.mp4) |
| 04:29:56 | [042956-drone-videos-2026-11-17-drone-pov.jpg](042956-drone-videos-2026-11-17-drone-pov.jpg) |
| 04:30:47 | [043047-drone-videos-2026-11-17-drone-pov.mp4](043047-drone-videos-2026-11-17-drone-pov.mp4) |
| 04:31:21 | [043121-drone-videos-2026-11-17-still-outside-follow.jpg](043121-drone-videos-2026-11-17-still-outside-follow.jpg) |
| 04:31:21 | [043121-drone-videos-2026-11-17-still-outside-photo.jpg](043121-drone-videos-2026-11-17-still-outside-photo.jpg) |
| 04:31:22 | [043122-drone-videos-2026-11-17-still-pov-flash.jpg](043122-drone-videos-2026-11-17-still-pov-flash.jpg) |
| 04:31:22 | [043122-drone-videos-2026-11-17-still-pov-follow.jpg](043122-drone-videos-2026-11-17-still-pov-follow.jpg) |
| 04:31:22 | [043122-drone-videos-2026-11-17-still-pov-photo.jpg](043122-drone-videos-2026-11-17-still-pov-photo.jpg) |
| 04:31:28 | [043128-drone-videos-2026-11-17-still-outside-takeoff.jpg](043128-drone-videos-2026-11-17-still-outside-takeoff.jpg) |
| 04:41:20 | [044120-bike-stand-tiles-web-web-calendar.jpg](044120-bike-stand-tiles-web-web-calendar.jpg) |
| 04:41:20 | [044120-bike-stand-tiles-web-web-console.jpg](044120-bike-stand-tiles-web-web-console.jpg) |
| 04:41:20 | [044120-bike-stand-tiles-web-web-downloads-ocw-2026-11-17-04-42-34.jpg](044120-bike-stand-tiles-web-web-downloads-ocw-2026-11-17-04-42-34.jpg) |
| 04:41:20 | [044120-bike-stand-tiles-web-web-downloads-ocw-2026-11-17-04-42-37.webm](044120-bike-stand-tiles-web-web-downloads-ocw-2026-11-17-04-42-37.webm) |
| 04:41:20 | [044120-bike-stand-tiles-web-web-gamepad.jpg](044120-bike-stand-tiles-web-web-gamepad.jpg) |
| 04:41:20 | [044120-bike-stand-tiles-web-web-gps.jpg](044120-bike-stand-tiles-web-web-gps.jpg) |
| 04:41:20 | [044120-bike-stand-tiles-web-web-hud.jpg](044120-bike-stand-tiles-web-web-hud.jpg) |
| 04:41:20 | [044120-bike-stand-tiles-web-web-join.jpg](044120-bike-stand-tiles-web-web-join.jpg) |
| 04:41:20 | [044120-bike-stand-tiles-web-web-menu.jpg](044120-bike-stand-tiles-web-web-menu.jpg) |
| 04:41:20 | [044120-bike-stand-tiles-web-web-ride.jpg](044120-bike-stand-tiles-web-web-ride.jpg) |
| 04:41:20 | [044120-bike-stand-tiles-web-web-riders.jpg](044120-bike-stand-tiles-web-web-riders.jpg) |
| 04:41:20 | [044120-bike-stand-tiles-web-web-settings.jpg](044120-bike-stand-tiles-web-web-settings.jpg) |
| 04:41:20 | [044120-bike-stand-tiles-web-web-touch-hints.jpg](044120-bike-stand-tiles-web-web-touch-hints.jpg) |
| 04:41:20 | [044120-bike-stand-tiles-web-web-touch-hold.jpg](044120-bike-stand-tiles-web-web-touch-hold.jpg) |
| 04:41:20 | [044120-bike-stand-tiles-web-web-unicorn-flight.jpg](044120-bike-stand-tiles-web-web-unicorn-flight.jpg) |
| 04:41:20 | [044120-bike-stand-tiles-web-web-unicorn-inspect.jpg](044120-bike-stand-tiles-web-web-unicorn-inspect.jpg) |
| 04:41:20 | [044120-bike-stand-tiles-web-web-unicorn-menu.jpg](044120-bike-stand-tiles-web-web-unicorn-menu.jpg) |
| 04:41:20 | [044120-bike-stand-tiles-web-web-weather.jpg](044120-bike-stand-tiles-web-web-weather.jpg) |
| 04:41:20 | [044120-bike-stand-tiles-web-web.jpg](044120-bike-stand-tiles-web-web.jpg) |
| 05:49:24 | [054924-shot-wayland-char2-face-20s-slim.jpg](054924-shot-wayland-char2-face-20s-slim.jpg) |
| 05:49:33 | [054933-shot-wayland-char2-face-40s-normal-sport.jpg](054933-shot-wayland-char2-face-40s-normal-sport.jpg) |
| 05:49:43 | [054943-shot-wayland-char2-face-60s-ample-round.jpg](054943-shot-wayland-char2-face-60s-ample-round.jpg) |
| 05:49:53 | [054953-shot-wayland-char2-face-70plus-obese-b.jpg](054953-shot-wayland-char2-face-70plus-obese-b.jpg) |
| 05:50:02 | [055002-shot-wayland-char2-face-30s-skinny-c.jpg](055002-shot-wayland-char2-face-30s-skinny-c.jpg) |
| 05:50:34 | [055034-shot-wayland-char2-face-glasses-front.jpg](055034-shot-wayland-char2-face-glasses-front.jpg) |
| 05:50:45 | [055045-shot-wayland-char2-face-helmet-aero.jpg](055045-shot-wayland-char2-face-helmet-aero.jpg) |
| 05:51:27 | [055127-shot-wayland-char2-tiles-hair.jpg](055127-shot-wayland-char2-tiles-hair.jpg) |
| 05:51:59 | [055159-shot-wayland-char2-tiles-shape.jpg](055159-shot-wayland-char2-tiles-shape.jpg) |
| 05:52:26 | [055226-shot-wayland-char2-tiles-base.jpg](055226-shot-wayland-char2-tiles-base.jpg) |
| 05:52:57 | [055257-shot-wayland-char2-tiles-beard.jpg](055257-shot-wayland-char2-tiles-beard.jpg) |
| 05:53:29 | [055329-shot-wayland-char2-tiles-age.jpg](055329-shot-wayland-char2-tiles-age.jpg) |
| 05:54:11 | [055411-shot-wayland-char2-mirror-hair-tiles.jpg](055411-shot-wayland-char2-mirror-hair-tiles.jpg) |
| 05:54:48 | [055448-shot-wayland-char2-mirror-helmet-tiles.jpg](055448-shot-wayland-char2-mirror-helmet-tiles.jpg) |
| 05:55:24 | [055524-shot-wayland-char2-mirror-shape-tiles.jpg](055524-shot-wayland-char2-mirror-shape-tiles.jpg) |
| 06:11:33 | [061133-shot-ocw.jpg](061133-shot-ocw.jpg) |
| 06:11:42 | [061142-shot-wayland-ocw-wayland.jpg](061142-shot-wayland-ocw-wayland.jpg) |
| 06:23:47 | [062347-shot-ocw.jpg](062347-shot-ocw.jpg) |
| 06:25:13 | [062513-shot-wayland-ocw-wayland.jpg](062513-shot-wayland-ocw-wayland.jpg) |
| 06:32:37 | [063237-scenes-char2-tiles-age.jpg](063237-scenes-char2-tiles-age.jpg) |
| 06:32:58 | [063258-shot-wayland-char2-face-20s-slim.jpg](063258-shot-wayland-char2-face-20s-slim.jpg) |
| 06:33:08 | [063308-shot-wayland-char2-face-40s-normal-sport.jpg](063308-shot-wayland-char2-face-40s-normal-sport.jpg) |
| 06:33:17 | [063317-shot-wayland-char2-face-60s-ample-round.jpg](063317-shot-wayland-char2-face-60s-ample-round.jpg) |
| 06:33:27 | [063327-shot-wayland-char2-face-70plus-obese-b.jpg](063327-shot-wayland-char2-face-70plus-obese-b.jpg) |
| 06:33:36 | [063336-shot-wayland-char2-face-30s-skinny-c.jpg](063336-shot-wayland-char2-face-30s-skinny-c.jpg) |
| 06:34:07 | [063407-shot-wayland-char2-face-glasses-front.jpg](063407-shot-wayland-char2-face-glasses-front.jpg) |
| 06:34:18 | [063418-shot-wayland-char2-face-helmet-aero.jpg](063418-shot-wayland-char2-face-helmet-aero.jpg) |
| 06:35:00 | [063500-shot-wayland-char2-tiles-hair.jpg](063500-shot-wayland-char2-tiles-hair.jpg) |
| 06:35:45 | [063545-shot-wayland-char2-tiles-shape.jpg](063545-shot-wayland-char2-tiles-shape.jpg) |
| 06:36:12 | [063612-shot-wayland-char2-tiles-base.jpg](063612-shot-wayland-char2-tiles-base.jpg) |
| 06:36:43 | [063643-shot-wayland-char2-tiles-beard.jpg](063643-shot-wayland-char2-tiles-beard.jpg) |
| 06:37:56 | [063756-shot-wayland-char2-mirror-hair-tiles.jpg](063756-shot-wayland-char2-mirror-hair-tiles.jpg) |
| 06:38:33 | [063833-shot-wayland-char2-mirror-helmet-tiles.jpg](063833-shot-wayland-char2-mirror-helmet-tiles.jpg) |
| 06:39:09 | [063909-shot-wayland-char2-mirror-shape-tiles.jpg](063909-shot-wayland-char2-mirror-shape-tiles.jpg) |
| 06:45:33 | [064533-shot-wayland-char2-face-20s-slim.jpg](064533-shot-wayland-char2-face-20s-slim.jpg) |
| 06:45:42 | [064542-shot-wayland-char2-face-40s-normal-sport.jpg](064542-shot-wayland-char2-face-40s-normal-sport.jpg) |
| 06:45:52 | [064552-shot-wayland-char2-face-60s-ample-round.jpg](064552-shot-wayland-char2-face-60s-ample-round.jpg) |
| 06:46:01 | [064601-shot-wayland-char2-face-70plus-obese-b.jpg](064601-shot-wayland-char2-face-70plus-obese-b.jpg) |
| 06:46:11 | [064611-shot-wayland-char2-face-30s-skinny-c.jpg](064611-shot-wayland-char2-face-30s-skinny-c.jpg) |
| 06:46:42 | [064642-shot-wayland-char2-face-glasses-front.jpg](064642-shot-wayland-char2-face-glasses-front.jpg) |
| 06:46:52 | [064652-shot-wayland-char2-face-helmet-aero.jpg](064652-shot-wayland-char2-face-helmet-aero.jpg) |
| 06:47:39 | [064739-shot-wayland-char2-face-20s-slim.jpg](064739-shot-wayland-char2-face-20s-slim.jpg) |
| 06:47:49 | [064749-shot-wayland-char2-face-40s-normal-sport.jpg](064749-shot-wayland-char2-face-40s-normal-sport.jpg) |
| 06:47:58 | [064758-shot-wayland-char2-face-60s-ample-round.jpg](064758-shot-wayland-char2-face-60s-ample-round.jpg) |
| 06:48:08 | [064808-shot-wayland-char2-face-70plus-obese-b.jpg](064808-shot-wayland-char2-face-70plus-obese-b.jpg) |
| 06:48:17 | [064817-shot-wayland-char2-face-30s-skinny-c.jpg](064817-shot-wayland-char2-face-30s-skinny-c.jpg) |
| 06:48:48 | [064848-shot-wayland-char2-face-glasses-front.jpg](064848-shot-wayland-char2-face-glasses-front.jpg) |
| 06:48:59 | [064859-shot-wayland-char2-face-helmet-aero.jpg](064859-shot-wayland-char2-face-helmet-aero.jpg) |
| 06:49:40 | [064940-shot-wayland-char2-tiles-hair.jpg](064940-shot-wayland-char2-tiles-hair.jpg) |
| 08:43:02 | [084302-vr-kiosk-weela-2026-11-17-01-monitor-session-idle.png](084302-vr-kiosk-weela-2026-11-17-01-monitor-session-idle.png) |
| 08:56:53 | [085653-vr-kiosk-weela-2026-11-17-02-monitor-session-ready.png](085653-vr-kiosk-weela-2026-11-17-02-monitor-session-ready.png) |
| 09:43:37 | [094337-web-web-audio-livekit-livekit-ada.jpg](094337-web-web-audio-livekit-livekit-ada.jpg) |
| 09:43:37 | [094337-web-web-audio-livekit-livekit-bea.jpg](094337-web-web-audio-livekit-livekit-bea.jpg) |
| 09:43:37 | [094337-web-web-audio-livekit-livekit-blocked.jpg](094337-web-web-audio-livekit-livekit-blocked.jpg) |
| 09:43:37 | [094337-web-web-audio-livekit-livekit-range-far.jpg](094337-web-web-audio-livekit-livekit-range-far.jpg) |
| 09:43:37 | [094337-web-web-audio-livekit-livekit-selected.jpg](094337-web-web-audio-livekit-livekit-selected.jpg) |
| 09:43:37 | [094337-web-web-audio-livekit.mic.wav](094337-web-web-audio-livekit.mic.wav) |
| 10:11:02 | [101102-vr-kiosk-weela-2026-11-17-03-left-eye-console-screenshot.jpg](101102-vr-kiosk-weela-2026-11-17-03-left-eye-console-screenshot.jpg) |
| 13:28:00 | [132800-shot-wayland-char2-face-60s-ample-round.jpg](132800-shot-wayland-char2-face-60s-ample-round.jpg) |
| 13:28:11 | [132811-shot-wayland-char2-tiles-skin.jpg](132811-shot-wayland-char2-tiles-skin.jpg) |
| 13:28:22 | [132822-shot-wayland-char2-tiles-skin-light.jpg](132822-shot-wayland-char2-tiles-skin-light.jpg) |
| 13:28:36 | [132836-shot-wayland-char2-mirror-skin-tiles.jpg](132836-shot-wayland-char2-mirror-skin-tiles.jpg) |
| 14:12:59 | [141259-shot-wayland-q30-shorts-tiles.jpg](141259-shot-wayland-q30-shorts-tiles.jpg) |
| 14:13:41 | [141341-shot-wayland-q30-socks-tiles.jpg](141341-shot-wayland-q30-socks-tiles.jpg) |
| 14:14:23 | [141423-shot-wayland-q30-shoes-tiles.jpg](141423-shot-wayland-q30-shoes-tiles.jpg) |
| 14:15:05 | [141505-shot-wayland-q30-gloves-tiles.jpg](141505-shot-wayland-q30-gloves-tiles.jpg) |
| 14:27:17 | [142717-q30-kit-tiles-mockup-1-shorts-tiles.jpg](142717-q30-kit-tiles-mockup-1-shorts-tiles.jpg) |
| 14:27:17 | [142717-q30-kit-tiles-mockup-2-socks-tiles-yellow.jpg](142717-q30-kit-tiles-mockup-2-socks-tiles-yellow.jpg) |
| 14:27:17 | [142717-q30-kit-tiles-mockup-3-shoes-tiles.jpg](142717-q30-kit-tiles-mockup-3-shoes-tiles.jpg) |
| 14:27:17 | [142717-q30-kit-tiles-mockup-4-gloves-tiles.jpg](142717-q30-kit-tiles-mockup-4-gloves-tiles.jpg) |
| 14:27:17 | [142717-q30-kit-tiles-mockup-5-shorts-list-today.jpg](142717-q30-kit-tiles-mockup-5-shorts-list-today.jpg) |
| 14:27:17 | [142717-q30-kit-tiles-mockup-q30-overview.jpg](142717-q30-kit-tiles-mockup-q30-overview.jpg) |
| 14:39:11 | [143911-shot-wayland-hands-road-hoods-mitts.jpg](143911-shot-wayland-hands-road-hoods-mitts.jpg) |
| 14:39:18 | [143918-shot-ocw.jpg](143918-shot-ocw.jpg) |
| 14:39:19 | [143919-shot-wayland-hands-road-tops.jpg](143919-shot-wayland-hands-road-tops.jpg) |
| 14:39:31 | [143931-shot-wayland-ocw-wayland.jpg](143931-shot-wayland-ocw-wayland.jpg) |
| 14:39:33 | [143933-shot-wayland-hands-road-drops.jpg](143933-shot-wayland-hands-road-drops.jpg) |
| 14:39:41 | [143941-shot-wayland-hands-tt-extensions.jpg](143941-shot-wayland-hands-tt-extensions.jpg) |
| 14:39:50 | [143950-shot-wayland-hands-mtb-grips.jpg](143950-shot-wayland-hands-mtb-grips.jpg) |
| 14:39:58 | [143958-shot-wayland-hands-gravel-drops.jpg](143958-shot-wayland-hands-gravel-drops.jpg) |
| 14:40:07 | [144007-shot-wayland-hands-gloves-gel.jpg](144007-shot-wayland-hands-gloves-gel.jpg) |
| 14:40:15 | [144015-shot-wayland-hands-gloves-full.jpg](144015-shot-wayland-hands-gloves-full.jpg) |
| 14:40:24 | [144024-shot-wayland-hands-gloves-winter.jpg](144024-shot-wayland-hands-gloves-winter.jpg) |
| 14:40:33 | [144033-shot-wayland-hands-left-hoods.jpg](144033-shot-wayland-hands-left-hoods.jpg) |
| 14:40:42 | [144042-shot-wayland-hands-phone.jpg](144042-shot-wayland-hands-phone.jpg) |
| 14:41:29 | [144129-shot-wayland-hands-arms-up.jpg](144129-shot-wayland-hands-arms-up.jpg) |
| 14:42:11 | [144211-shot-wayland-bare-tiles-hair.jpg](144211-shot-wayland-bare-tiles-hair.jpg) |
| 14:42:22 | [144222-shot-wayland-bare-face-close-up.jpg](144222-shot-wayland-bare-face-close-up.jpg) |
| 14:42:33 | [144233-shot-wayland-bare-mirror-helmet-hook.jpg](144233-shot-wayland-bare-mirror-helmet-hook.jpg) |
| 14:43:15 | [144315-shot-wayland-bare-mirror-hair-tiles.jpg](144315-shot-wayland-bare-mirror-hair-tiles.jpg) |
| 15:15:38 | [151538-shot-wayland-fix-groupset-picker.jpg](151538-shot-wayland-fix-groupset-picker.jpg) |
| 15:16:03 | [151603-shot-wayland-fix-groupset-crankset.jpg](151603-shot-wayland-fix-groupset-crankset.jpg) |
| 15:16:17 | [151617-shot-wayland-fix-console-workshop.jpg](151617-shot-wayland-fix-console-workshop.jpg) |
| 15:16:48 | [151648-shot-wayland-fix-carbon-stand.jpg](151648-shot-wayland-fix-carbon-stand.jpg) |
| 15:17:19 | [151719-shot-wayland-fix-mtb-fork.jpg](151719-shot-wayland-fix-mtb-fork.jpg) |
| 15:17:51 | [151751-shot-wayland-fix-mtb-fork-front.jpg](151751-shot-wayland-fix-mtb-fork-front.jpg) |
| 15:18:01 | [151801-shot-wayland-fix-hip-number.jpg](151801-shot-wayland-fix-hip-number.jpg) |
| 15:18:19 | [151819-shot-wayland-fix-wild-kerb-vaduz.jpg](151819-shot-wayland-fix-wild-kerb-vaduz.jpg) |
| 15:18:30 | [151830-shot-wayland-fix-sidewalk-corners-vaduz.jpg](151830-shot-wayland-fix-sidewalk-corners-vaduz.jpg) |
| 15:18:40 | [151840-shot-wayland-fix-sidewalk-corners-aeule.jpg](151840-shot-wayland-fix-sidewalk-corners-aeule.jpg) |
| 15:18:49 | [151849-shot-wayland-fix-hud-1280x720.jpg](151849-shot-wayland-fix-hud-1280x720.jpg) |
| 15:18:57 | [151857-shot-wayland-fix-hud-1024x768.jpg](151857-shot-wayland-fix-hud-1024x768.jpg) |
| 15:19:05 | [151905-shot-wayland-fix-hud-1280x720-150.jpg](151905-shot-wayland-fix-hud-1280x720-150.jpg) |
| 15:19:31 | [151931-shot-wayland-fix-stand-tiles-frame.jpg](151931-shot-wayland-fix-stand-tiles-frame.jpg) |
| 15:19:56 | [151956-shot-wayland-fix-stand-tiles-groupset.jpg](151956-shot-wayland-fix-stand-tiles-groupset.jpg) |
| 15:20:10 | [152010-shot-wayland-fix-helmet-hook.jpg](152010-shot-wayland-fix-helmet-hook.jpg) |
| 15:20:24 | [152024-shot-wayland-fix-standing-hands.jpg](152024-shot-wayland-fix-standing-hands.jpg) |
| 15:24:44 | [152444-scenes-before-wl-stands-masca-km9.jpg](152444-scenes-before-wl-stands-masca-km9.jpg) |
| 15:24:58 | [152458-scenes-before-wl-stands-masca-km79.jpg](152458-scenes-before-wl-stands-masca-km79.jpg) |
| 15:25:11 | [152511-scenes-before-wl-stands-masca-km108.jpg](152511-scenes-before-wl-stands-masca-km108.jpg) |
| 15:25:25 | [152525-scenes-before-wl-stands-teide-km11.jpg](152525-scenes-before-wl-stands-teide-km11.jpg) |
| 15:25:38 | [152538-scenes-before-wl-stands-teide-km134.jpg](152538-scenes-before-wl-stands-teide-km134.jpg) |
| 15:25:52 | [152552-scenes-before-wl-stands-blackforest-maize.jpg](152552-scenes-before-wl-stands-blackforest-maize.jpg) |
| 15:26:11 | [152611-scenes-before-x11-stands-masca-km9.jpg](152611-scenes-before-x11-stands-masca-km9.jpg) |
| 15:26:32 | [152632-scenes-before-x11-stands-masca-km79.jpg](152632-scenes-before-x11-stands-masca-km79.jpg) |
| 15:26:51 | [152651-scenes-before-x11-stands-masca-km108.jpg](152651-scenes-before-x11-stands-masca-km108.jpg) |
| 15:27:11 | [152711-scenes-before-x11-stands-teide-km11.jpg](152711-scenes-before-x11-stands-teide-km11.jpg) |
| 15:27:30 | [152730-scenes-before-x11-stands-teide-km134.jpg](152730-scenes-before-x11-stands-teide-km134.jpg) |
| 15:27:50 | [152750-scenes-before-x11-stands-blackforest-maize.jpg](152750-scenes-before-x11-stands-blackforest-maize.jpg) |
| 15:40:22 | [154022-scenes-dbg-dbg-winter.jpg](154022-scenes-dbg-dbg-winter.jpg) |
| 15:40:38 | [154038-scenes-dbg-dbg-farcull.jpg](154038-scenes-dbg-dbg-farcull.jpg) |
| 15:40:53 | [154053-scenes-dbg-dbg-top.jpg](154053-scenes-dbg-dbg-top.jpg) |
| 15:41:09 | [154109-scenes-dbg-nojunc-dbg-farcull.jpg](154109-scenes-dbg-nojunc-dbg-farcull.jpg) |
| 15:42:02 | [154202-shot-wayland-fix-hud-1280x720.jpg](154202-shot-wayland-fix-hud-1280x720.jpg) |
| 15:50:43 | [155043-shot-wayland-fix-hud-1024x768.jpg](155043-shot-wayland-fix-hud-1024x768.jpg) |
| 15:50:52 | [155052-shot-wayland-fix-hud-1280x720-150.jpg](155052-shot-wayland-fix-hud-1280x720-150.jpg) |
| 15:51:18 | [155118-shot-wayland-fix-stand-tiles-frame.jpg](155118-shot-wayland-fix-stand-tiles-frame.jpg) |
| 15:51:44 | [155144-shot-wayland-fix-stand-tiles-groupset.jpg](155144-shot-wayland-fix-stand-tiles-groupset.jpg) |
| 15:51:58 | [155158-shot-wayland-fix-helmet-hook.jpg](155158-shot-wayland-fix-helmet-hook.jpg) |
| 15:52:12 | [155212-shot-wayland-fix-standing-hands.jpg](155212-shot-wayland-fix-standing-hands.jpg) |
| 16:18:32 | [161832-shot-wayland-hands-road-hoods-mitts.jpg](161832-shot-wayland-hands-road-hoods-mitts.jpg) |
| 16:21:07 | [162107-stands-on-terrain-2026-11-17-after-blackforest-maize-wayland.jpg](162107-stands-on-terrain-2026-11-17-after-blackforest-maize-wayland.jpg) |
| 16:21:07 | [162107-stands-on-terrain-2026-11-17-after-blackforest-maize-x11.jpg](162107-stands-on-terrain-2026-11-17-after-blackforest-maize-x11.jpg) |
| 16:21:07 | [162107-stands-on-terrain-2026-11-17-after-liechtenstein-cereal-wayland.jpg](162107-stands-on-terrain-2026-11-17-after-liechtenstein-cereal-wayland.jpg) |
| 16:21:07 | [162107-stands-on-terrain-2026-11-17-after-liechtenstein-cereal-x11.jpg](162107-stands-on-terrain-2026-11-17-after-liechtenstein-cereal-x11.jpg) |
| 16:21:07 | [162107-stands-on-terrain-2026-11-17-after-masca-km108-wayland.jpg](162107-stands-on-terrain-2026-11-17-after-masca-km108-wayland.jpg) |
| 16:21:07 | [162107-stands-on-terrain-2026-11-17-after-masca-km108-x11.jpg](162107-stands-on-terrain-2026-11-17-after-masca-km108-x11.jpg) |
| 16:21:07 | [162107-stands-on-terrain-2026-11-17-after-masca-km79-wayland.jpg](162107-stands-on-terrain-2026-11-17-after-masca-km79-wayland.jpg) |
| 16:21:07 | [162107-stands-on-terrain-2026-11-17-after-masca-km79-x11.jpg](162107-stands-on-terrain-2026-11-17-after-masca-km79-x11.jpg) |
| 16:21:07 | [162107-stands-on-terrain-2026-11-17-after-masca-km9-wayland.jpg](162107-stands-on-terrain-2026-11-17-after-masca-km9-wayland.jpg) |
| 16:21:07 | [162107-stands-on-terrain-2026-11-17-after-masca-km9-x11.jpg](162107-stands-on-terrain-2026-11-17-after-masca-km9-x11.jpg) |
| 16:21:07 | [162107-stands-on-terrain-2026-11-17-after-teide-km11-wayland.jpg](162107-stands-on-terrain-2026-11-17-after-teide-km11-wayland.jpg) |
| 16:21:07 | [162107-stands-on-terrain-2026-11-17-after-teide-km11-x11.jpg](162107-stands-on-terrain-2026-11-17-after-teide-km11-x11.jpg) |
| 16:21:07 | [162107-stands-on-terrain-2026-11-17-after-teide-km134-wayland.jpg](162107-stands-on-terrain-2026-11-17-after-teide-km134-wayland.jpg) |
| 16:21:07 | [162107-stands-on-terrain-2026-11-17-after-teide-km134-x11.jpg](162107-stands-on-terrain-2026-11-17-after-teide-km134-x11.jpg) |
| 16:21:07 | [162107-stands-on-terrain-2026-11-17-before-blackforest-maize-wayland.jpg](162107-stands-on-terrain-2026-11-17-before-blackforest-maize-wayland.jpg) |
| 16:21:07 | [162107-stands-on-terrain-2026-11-17-before-blackforest-maize-x11.jpg](162107-stands-on-terrain-2026-11-17-before-blackforest-maize-x11.jpg) |
| 16:21:07 | [162107-stands-on-terrain-2026-11-17-before-liechtenstein-cereal-wayland.jpg](162107-stands-on-terrain-2026-11-17-before-liechtenstein-cereal-wayland.jpg) |
| 16:21:07 | [162107-stands-on-terrain-2026-11-17-before-liechtenstein-cereal-x11.jpg](162107-stands-on-terrain-2026-11-17-before-liechtenstein-cereal-x11.jpg) |
| 16:21:07 | [162107-stands-on-terrain-2026-11-17-before-masca-km108-wayland.jpg](162107-stands-on-terrain-2026-11-17-before-masca-km108-wayland.jpg) |
| 16:21:07 | [162107-stands-on-terrain-2026-11-17-before-masca-km108-x11.jpg](162107-stands-on-terrain-2026-11-17-before-masca-km108-x11.jpg) |
| 16:21:07 | [162107-stands-on-terrain-2026-11-17-before-masca-km79-wayland.jpg](162107-stands-on-terrain-2026-11-17-before-masca-km79-wayland.jpg) |
| 16:21:07 | [162107-stands-on-terrain-2026-11-17-before-masca-km79-x11.jpg](162107-stands-on-terrain-2026-11-17-before-masca-km79-x11.jpg) |
| 16:21:07 | [162107-stands-on-terrain-2026-11-17-before-masca-km9-wayland.jpg](162107-stands-on-terrain-2026-11-17-before-masca-km9-wayland.jpg) |
| 16:21:07 | [162107-stands-on-terrain-2026-11-17-before-masca-km9-x11.jpg](162107-stands-on-terrain-2026-11-17-before-masca-km9-x11.jpg) |
| 16:21:07 | [162107-stands-on-terrain-2026-11-17-before-teide-km11-wayland.jpg](162107-stands-on-terrain-2026-11-17-before-teide-km11-wayland.jpg) |
| 16:21:07 | [162107-stands-on-terrain-2026-11-17-before-teide-km11-x11.jpg](162107-stands-on-terrain-2026-11-17-before-teide-km11-x11.jpg) |
| 16:21:07 | [162107-stands-on-terrain-2026-11-17-before-teide-km134-wayland.jpg](162107-stands-on-terrain-2026-11-17-before-teide-km134-wayland.jpg) |
| 16:21:07 | [162107-stands-on-terrain-2026-11-17-before-teide-km134-x11.jpg](162107-stands-on-terrain-2026-11-17-before-teide-km134-x11.jpg) |
| 16:21:11 | [162111-stands-on-terrain-2026-11-17-compare-masca-km108.jpg](162111-stands-on-terrain-2026-11-17-compare-masca-km108.jpg) |
| 16:21:11 | [162111-stands-on-terrain-2026-11-17-compare-masca-km79.jpg](162111-stands-on-terrain-2026-11-17-compare-masca-km79.jpg) |
| 16:21:11 | [162111-stands-on-terrain-2026-11-17-compare-masca-km9.jpg](162111-stands-on-terrain-2026-11-17-compare-masca-km9.jpg) |
| 16:21:11 | [162111-stands-on-terrain-2026-11-17-compare-teide-km11.jpg](162111-stands-on-terrain-2026-11-17-compare-teide-km11.jpg) |
| 16:21:12 | [162112-stands-on-terrain-2026-11-17-compare-blackforest-maize.jpg](162112-stands-on-terrain-2026-11-17-compare-blackforest-maize.jpg) |
| 16:21:12 | [162112-stands-on-terrain-2026-11-17-compare-liechtenstein-cereal.jpg](162112-stands-on-terrain-2026-11-17-compare-liechtenstein-cereal.jpg) |
| 16:21:12 | [162112-stands-on-terrain-2026-11-17-compare-teide-km134.jpg](162112-stands-on-terrain-2026-11-17-compare-teide-km134.jpg) |
| 16:23:57 | [162357-shot-wayland-hands-road-tops.jpg](162357-shot-wayland-hands-road-tops.jpg) |
| 16:24:07 | [162407-shot-wayland-hands-left-hoods.jpg](162407-shot-wayland-hands-left-hoods.jpg) |
| 16:24:21 | [162421-shot-wayland-fix-helmet-hook.jpg](162421-shot-wayland-fix-helmet-hook.jpg) |
| 16:24:25 | [162425-shot-ocw.jpg](162425-shot-ocw.jpg) |
| 16:24:34 | [162434-shot-wayland-ocw-wayland.jpg](162434-shot-wayland-ocw-wayland.jpg) |
| 16:24:35 | [162435-shot-wayland-fix-standing-hands.jpg](162435-shot-wayland-fix-standing-hands.jpg) |
| 17:24:40 | [172440-shot-wayland-stands-masca-km9.jpg](172440-shot-wayland-stands-masca-km9.jpg) |
| 17:25:06 | [172506-shot-wayland-fix-stand-tiles-groupset.jpg](172506-shot-wayland-fix-stand-tiles-groupset.jpg) |
| 17:25:19 | [172519-shot-wayland-stands-masca-km79.jpg](172519-shot-wayland-stands-masca-km79.jpg) |
| 17:25:33 | [172533-shot-wayland-stands-masca-km108.jpg](172533-shot-wayland-stands-masca-km108.jpg) |
| 17:25:49 | [172549-shot-wayland-ground-bf-schauinsland-slope.jpg](172549-shot-wayland-ground-bf-schauinsland-slope.jpg) |
| 17:26:04 | [172604-shot-wayland-ground-bf-schauinsland-slope-2.jpg](172604-shot-wayland-ground-bf-schauinsland-slope-2.jpg) |
| 17:26:18 | [172618-shot-wayland-ground-masca-km108-low.jpg](172618-shot-wayland-ground-masca-km108-low.jpg) |
| 17:27:49 | [172749-shot-wayland-thumbs-dump.jpg](172749-shot-wayland-thumbs-dump.jpg) |
| 17:30:13 | [173013-shot-wayland-thumbs-dump.jpg](173013-shot-wayland-thumbs-dump.jpg) |
| 17:31:33 | [173133-shot-wayland-stands-masca-km9.jpg](173133-shot-wayland-stands-masca-km9.jpg) |
| 17:31:58 | [173158-shot-wayland-fix-stand-tiles-groupset.jpg](173158-shot-wayland-fix-stand-tiles-groupset.jpg) |
| 17:32:12 | [173212-shot-wayland-stands-masca-km79.jpg](173212-shot-wayland-stands-masca-km79.jpg) |
| 17:32:26 | [173226-shot-wayland-stands-masca-km108.jpg](173226-shot-wayland-stands-masca-km108.jpg) |
| 17:32:41 | [173241-shot-wayland-ground-bf-schauinsland-slope.jpg](173241-shot-wayland-ground-bf-schauinsland-slope.jpg) |
| 17:32:56 | [173256-shot-wayland-ground-bf-schauinsland-slope-2.jpg](173256-shot-wayland-ground-bf-schauinsland-slope-2.jpg) |
| 17:33:10 | [173310-shot-wayland-ground-masca-km108-low.jpg](173310-shot-wayland-ground-masca-km108-low.jpg) |
| 17:34:12 | [173412-shot-wayland-thumbs-dump.jpg](173412-shot-wayland-thumbs-dump.jpg) |
| 17:36:24 | [173624-shot-wayland-fix-stand-tiles-groupset.jpg](173624-shot-wayland-fix-stand-tiles-groupset.jpg) |
| 17:37:25 | [173725-shot-wayland-thumbs-dump.jpg](173725-shot-wayland-thumbs-dump.jpg) |
| 17:39:39 | [173939-shot-wayland-fix-stand-tiles-groupset.jpg](173939-shot-wayland-fix-stand-tiles-groupset.jpg) |
| 17:40:40 | [174040-shot-wayland-thumbs-dump.jpg](174040-shot-wayland-thumbs-dump.jpg) |
| 17:42:26 | [174226-shot-wayland-thumbs-dump.jpg](174226-shot-wayland-thumbs-dump.jpg) |
| 17:44:02 | [174402-shot-wayland-thumbs-dump.jpg](174402-shot-wayland-thumbs-dump.jpg) |
| 17:47:54 | [174754-shot-wayland-thumbs-dump.jpg](174754-shot-wayland-thumbs-dump.jpg) |
| 17:48:50 | [174850-shot-wayland-fix-stand-tiles-groupset.jpg](174850-shot-wayland-fix-stand-tiles-groupset.jpg) |
| 17:49:52 | [174952-shot-wayland-thumbs-dump.jpg](174952-shot-wayland-thumbs-dump.jpg) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-compare-fix-stand-tiles-groupset.jpg](180804-fix-ground-thumbs-2026-11-17-compare-fix-stand-tiles-groupset.jpg) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-compare-ground-bf-schauinsland-slope-2.jpg](180804-fix-ground-thumbs-2026-11-17-compare-ground-bf-schauinsland-slope-2.jpg) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-compare-ground-bf-schauinsland-slope.jpg](180804-fix-ground-thumbs-2026-11-17-compare-ground-bf-schauinsland-slope.jpg) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-compare-ground-masca-km108-low.jpg](180804-fix-ground-thumbs-2026-11-17-compare-ground-masca-km108-low.jpg) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-compare-stands-masca-km108.jpg](180804-fix-ground-thumbs-2026-11-17-compare-stands-masca-km108.jpg) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-compare-stands-masca-km79.jpg](180804-fix-ground-thumbs-2026-11-17-compare-stands-masca-km79.jpg) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-compare-stands-masca-km9.jpg](180804-fix-ground-thumbs-2026-11-17-compare-stands-masca-km9.jpg) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-compare-thumb-road-cassette.png](180804-fix-ground-thumbs-2026-11-17-compare-thumb-road-cassette.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-compare-thumb-road-chain.png](180804-fix-ground-thumbs-2026-11-17-compare-thumb-road-chain.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-compare-thumb-road-cockpit.png](180804-fix-ground-thumbs-2026-11-17-compare-thumb-road-cockpit.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-compare-thumb-road-crankset.png](180804-fix-ground-thumbs-2026-11-17-compare-thumb-road-crankset.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-compare-thumb-road-groupset.png](180804-fix-ground-thumbs-2026-11-17-compare-thumb-road-groupset.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-mtb-bag-bag-top-tube.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-mtb-bag-bag-top-tube.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-mtb-bag-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-mtb-bag-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-mtb-bar-tape-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-mtb-bar-tape-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-mtb-bottle-cages-cage-carbon.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-mtb-bottle-cages-cage-carbon.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-mtb-bottle-cages-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-mtb-bottle-cages-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-mtb-cassette-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-mtb-cassette-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-mtb-chain-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-mtb-chain-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-mtb-cockpit-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-mtb-cockpit-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-mtb-computer-computer-large.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-mtb-computer-computer-large.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-mtb-computer-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-mtb-computer-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-mtb-crankset-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-mtb-crankset-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-mtb-frame-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-mtb-frame-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-mtb-groupset-groupset-mtb-electronic.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-mtb-groupset-groupset-mtb-electronic.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-mtb-groupset-groupset-mtb.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-mtb-groupset-groupset-mtb.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-mtb-groupset-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-mtb-groupset-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-mtb-lights-lights-set.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-mtb-lights-lights-set.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-mtb-lights-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-mtb-lights-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-mtb-paint-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-mtb-paint-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-mtb-pedals-pedals-spd.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-mtb-pedals-pedals-spd.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-mtb-pedals-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-mtb-pedals-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-mtb-saddle-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-mtb-saddle-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-mtb-seatpost-seatpost-carbon.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-mtb-seatpost-seatpost-carbon.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-mtb-seatpost-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-mtb-seatpost-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-mtb-tyres-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-mtb-tyres-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-mtb-tyres-tyre-mtb-xc.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-mtb-tyres-tyre-mtb-xc.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-mtb-wheels-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-mtb-wheels-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-bag-bag-top-tube.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-bag-bag-top-tube.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-bag-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-bag-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-bar-tape-bar-tape-tacky.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-bar-tape-bar-tape-tacky.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-bar-tape-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-bar-tape-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-bottle-cages-cage-carbon.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-bottle-cages-cage-carbon.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-bottle-cages-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-bottle-cages-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-cassette-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-cassette-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-chain-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-chain-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-cockpit-cockpit-carbon.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-cockpit-cockpit-carbon.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-cockpit-cockpit-extensions.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-cockpit-cockpit-extensions.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-cockpit-cockpit-integrated.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-cockpit-cockpit-integrated.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-cockpit-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-cockpit-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-computer-computer-large.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-computer-computer-large.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-computer-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-computer-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-crankset-crank-power.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-crankset-crank-power.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-crankset-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-crankset-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-frame-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-frame-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-groupset-groupset-electronic-top.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-groupset-groupset-electronic-top.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-groupset-groupset-electronic.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-groupset-groupset-electronic.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-groupset-groupset-mech.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-groupset-groupset-mech.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-groupset-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-groupset-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-lights-lights-set.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-lights-lights-set.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-lights-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-lights-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-paint-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-paint-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-pedals-pedals-road-carbon.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-pedals-pedals-road-carbon.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-pedals-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-pedals-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-saddle-saddle-short-nose.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-saddle-saddle-short-nose.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-saddle-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-saddle-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-seatpost-seatpost-carbon.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-seatpost-seatpost-carbon.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-seatpost-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-seatpost-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-tyres-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-tyres-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-tyres-tyre-road-25-tt.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-tyres-tyre-road-25-tt.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-tyres-tyre-road-28-training.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-tyres-tyre-road-28-training.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-tyres-tyre-road-28.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-tyres-tyre-road-28.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-wheels-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-wheels-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-wheels-wheel-alloy-performance.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-wheels-wheel-alloy-performance.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-wheels-wheel-alloy-training.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-wheels-wheel-alloy-training.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-wheels-wheel-carbon-45.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-wheels-wheel-carbon-45.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-wheels-wheel-carbon-50.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-road-wheels-wheel-carbon-50.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-tt-bag-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-tt-bag-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-tt-bar-tape-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-tt-bar-tape-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-tt-bottle-cages-cage-carbon.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-tt-bottle-cages-cage-carbon.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-tt-bottle-cages-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-tt-bottle-cages-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-tt-cassette-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-tt-cassette-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-tt-chain-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-tt-chain-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-tt-cockpit-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-tt-cockpit-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-tt-computer-computer-large.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-tt-computer-computer-large.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-tt-computer-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-tt-computer-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-tt-crankset-crank-power.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-tt-crankset-crank-power.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-tt-crankset-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-tt-crankset-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-tt-frame-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-tt-frame-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-tt-groupset-groupset-electronic-top.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-tt-groupset-groupset-electronic-top.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-tt-groupset-groupset-electronic.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-tt-groupset-groupset-electronic.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-tt-groupset-groupset-mech.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-tt-groupset-groupset-mech.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-tt-groupset-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-tt-groupset-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-tt-lights-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-tt-lights-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-tt-paint-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-tt-paint-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-tt-pedals-pedals-road-carbon.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-tt-pedals-pedals-road-carbon.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-tt-pedals-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-tt-pedals-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-tt-saddle-saddle-short-nose.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-tt-saddle-saddle-short-nose.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-tt-saddle-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-tt-saddle-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-tt-seatpost-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-tt-seatpost-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-tt-tyres-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-tt-tyres-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-tt-tyres-tyre-road-25-tt.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-tt-tyres-tyre-road-25-tt.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-tt-tyres-tyre-road-28-training.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-tt-tyres-tyre-road-28-training.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-tt-tyres-tyre-road-28.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-tt-tyres-tyre-road-28.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-tt-wheels-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-tt-wheels-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-tt-wheels-wheel-alloy-performance.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-tt-wheels-wheel-alloy-performance.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-tt-wheels-wheel-alloy-training.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-tt-wheels-wheel-alloy-training.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-tt-wheels-wheel-carbon-45.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-tt-wheels-wheel-carbon-45.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-tt-wheels-wheel-carbon-50.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-tt-wheels-wheel-carbon-50.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-after-tt-wheels-wheel-disc-tt.png](180804-fix-ground-thumbs-2026-11-17-thumbs-after-tt-wheels-wheel-disc-tt.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-mtb-bag-bag-top-tube.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-mtb-bag-bag-top-tube.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-mtb-bag-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-mtb-bag-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-mtb-bar-tape-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-mtb-bar-tape-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-mtb-bottle-cages-cage-carbon.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-mtb-bottle-cages-cage-carbon.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-mtb-bottle-cages-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-mtb-bottle-cages-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-mtb-cassette-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-mtb-cassette-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-mtb-chain-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-mtb-chain-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-mtb-cockpit-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-mtb-cockpit-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-mtb-computer-computer-large.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-mtb-computer-computer-large.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-mtb-computer-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-mtb-computer-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-mtb-crankset-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-mtb-crankset-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-mtb-frame-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-mtb-frame-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-mtb-groupset-groupset-mtb-electronic.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-mtb-groupset-groupset-mtb-electronic.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-mtb-groupset-groupset-mtb.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-mtb-groupset-groupset-mtb.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-mtb-groupset-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-mtb-groupset-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-mtb-lights-lights-set.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-mtb-lights-lights-set.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-mtb-lights-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-mtb-lights-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-mtb-paint-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-mtb-paint-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-mtb-pedals-pedals-spd.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-mtb-pedals-pedals-spd.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-mtb-pedals-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-mtb-pedals-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-mtb-saddle-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-mtb-saddle-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-mtb-seatpost-seatpost-carbon.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-mtb-seatpost-seatpost-carbon.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-mtb-seatpost-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-mtb-seatpost-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-mtb-tyres-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-mtb-tyres-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-mtb-tyres-tyre-mtb-xc.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-mtb-tyres-tyre-mtb-xc.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-mtb-wheels-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-mtb-wheels-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-bag-bag-top-tube.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-bag-bag-top-tube.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-bag-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-bag-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-bar-tape-bar-tape-tacky.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-bar-tape-bar-tape-tacky.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-bar-tape-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-bar-tape-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-bottle-cages-cage-carbon.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-bottle-cages-cage-carbon.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-bottle-cages-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-bottle-cages-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-cassette-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-cassette-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-chain-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-chain-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-cockpit-cockpit-carbon.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-cockpit-cockpit-carbon.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-cockpit-cockpit-extensions.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-cockpit-cockpit-extensions.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-cockpit-cockpit-integrated.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-cockpit-cockpit-integrated.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-cockpit-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-cockpit-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-computer-computer-large.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-computer-computer-large.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-computer-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-computer-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-crankset-crank-power.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-crankset-crank-power.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-crankset-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-crankset-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-frame-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-frame-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-groupset-groupset-electronic-top.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-groupset-groupset-electronic-top.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-groupset-groupset-electronic.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-groupset-groupset-electronic.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-groupset-groupset-mech.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-groupset-groupset-mech.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-groupset-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-groupset-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-lights-lights-set.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-lights-lights-set.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-lights-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-lights-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-paint-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-paint-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-pedals-pedals-road-carbon.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-pedals-pedals-road-carbon.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-pedals-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-pedals-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-saddle-saddle-short-nose.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-saddle-saddle-short-nose.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-saddle-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-saddle-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-seatpost-seatpost-carbon.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-seatpost-seatpost-carbon.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-seatpost-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-seatpost-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-tyres-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-tyres-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-tyres-tyre-road-25-tt.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-tyres-tyre-road-25-tt.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-tyres-tyre-road-28-training.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-tyres-tyre-road-28-training.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-tyres-tyre-road-28.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-tyres-tyre-road-28.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-wheels-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-wheels-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-wheels-wheel-alloy-performance.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-wheels-wheel-alloy-performance.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-wheels-wheel-alloy-training.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-wheels-wheel-alloy-training.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-wheels-wheel-carbon-45.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-wheels-wheel-carbon-45.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-wheels-wheel-carbon-50.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-road-wheels-wheel-carbon-50.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-tt-bag-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-tt-bag-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-tt-bar-tape-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-tt-bar-tape-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-tt-bottle-cages-cage-carbon.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-tt-bottle-cages-cage-carbon.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-tt-bottle-cages-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-tt-bottle-cages-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-tt-cassette-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-tt-cassette-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-tt-chain-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-tt-chain-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-tt-cockpit-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-tt-cockpit-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-tt-computer-computer-large.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-tt-computer-computer-large.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-tt-computer-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-tt-computer-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-tt-crankset-crank-power.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-tt-crankset-crank-power.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-tt-crankset-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-tt-crankset-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-tt-frame-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-tt-frame-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-tt-groupset-groupset-electronic-top.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-tt-groupset-groupset-electronic-top.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-tt-groupset-groupset-electronic.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-tt-groupset-groupset-electronic.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-tt-groupset-groupset-mech.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-tt-groupset-groupset-mech.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-tt-groupset-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-tt-groupset-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-tt-lights-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-tt-lights-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-tt-paint-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-tt-paint-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-tt-pedals-pedals-road-carbon.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-tt-pedals-pedals-road-carbon.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-tt-pedals-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-tt-pedals-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-tt-saddle-saddle-short-nose.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-tt-saddle-saddle-short-nose.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-tt-saddle-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-tt-saddle-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-tt-seatpost-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-tt-seatpost-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-tt-tyres-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-tt-tyres-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-tt-tyres-tyre-road-25-tt.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-tt-tyres-tyre-road-25-tt.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-tt-tyres-tyre-road-28-training.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-tt-tyres-tyre-road-28-training.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-tt-tyres-tyre-road-28.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-tt-tyres-tyre-road-28.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-tt-wheels-stock.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-tt-wheels-stock.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-tt-wheels-wheel-alloy-performance.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-tt-wheels-wheel-alloy-performance.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-tt-wheels-wheel-alloy-training.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-tt-wheels-wheel-alloy-training.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-tt-wheels-wheel-carbon-45.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-tt-wheels-wheel-carbon-45.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-tt-wheels-wheel-carbon-50.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-tt-wheels-wheel-carbon-50.png) |
| 18:08:04 | [180804-fix-ground-thumbs-2026-11-17-thumbs-before-tt-wheels-wheel-disc-tt.png](180804-fix-ground-thumbs-2026-11-17-thumbs-before-tt-wheels-wheel-disc-tt.png) |
| 18:08:05 | [180805-fix-ground-thumbs-2026-11-17-compare-thumb-road-pedals.png](180805-fix-ground-thumbs-2026-11-17-compare-thumb-road-pedals.png) |
| 18:08:05 | [180805-fix-ground-thumbs-2026-11-17-compare-thumb-road-saddle.png](180805-fix-ground-thumbs-2026-11-17-compare-thumb-road-saddle.png) |
| 18:08:05 | [180805-fix-ground-thumbs-2026-11-17-compare-thumb-road-tyres.png](180805-fix-ground-thumbs-2026-11-17-compare-thumb-road-tyres.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-compare-thumb-groupset.png](183741-fix-stand-tile-pictures-2026-11-17-compare-thumb-groupset.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-compare-thumb-vs-tile-groupset.png](183741-fix-stand-tile-pictures-2026-11-17-compare-thumb-vs-tile-groupset.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-compare-tile-groupset.png](183741-fix-stand-tile-pictures-2026-11-17-compare-tile-groupset.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-shots-char-editor-tiles-hair.jpg](183741-fix-stand-tile-pictures-2026-11-17-shots-char-editor-tiles-hair.jpg) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-shots-fix-stand-tiles-cockpit.jpg](183741-fix-stand-tile-pictures-2026-11-17-shots-fix-stand-tiles-cockpit.jpg) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-shots-fix-stand-tiles-groupset.jpg](183741-fix-stand-tile-pictures-2026-11-17-shots-fix-stand-tiles-groupset.jpg) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-shots-fix-stand-tiles-saddle.jpg](183741-fix-stand-tile-pictures-2026-11-17-shots-fix-stand-tiles-saddle.jpg) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-shots-fix-stand-tiles-tyres.jpg](183741-fix-stand-tile-pictures-2026-11-17-shots-fix-stand-tiles-tyres.jpg) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-shots-thumbs-dump.jpg](183741-fix-stand-tile-pictures-2026-11-17-shots-thumbs-dump.jpg) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-mtb-bag-bag-top-tube.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-mtb-bag-bag-top-tube.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-mtb-bag-stock.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-mtb-bag-stock.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-mtb-bar-tape-stock.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-mtb-bar-tape-stock.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-mtb-bottle-cages-cage-carbon.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-mtb-bottle-cages-cage-carbon.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-mtb-bottle-cages-stock.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-mtb-bottle-cages-stock.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-mtb-cassette-stock.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-mtb-cassette-stock.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-mtb-chain-stock.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-mtb-chain-stock.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-mtb-cockpit-stock.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-mtb-cockpit-stock.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-mtb-computer-computer-large.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-mtb-computer-computer-large.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-mtb-computer-stock.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-mtb-computer-stock.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-mtb-crankset-stock.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-mtb-crankset-stock.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-mtb-frame-stock.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-mtb-frame-stock.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-mtb-groupset-groupset-mtb-electronic.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-mtb-groupset-groupset-mtb-electronic.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-mtb-groupset-groupset-mtb.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-mtb-groupset-groupset-mtb.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-mtb-groupset-stock.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-mtb-groupset-stock.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-mtb-lights-lights-set.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-mtb-lights-lights-set.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-mtb-lights-stock.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-mtb-lights-stock.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-mtb-paint-stock.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-mtb-paint-stock.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-mtb-pedals-pedals-spd.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-mtb-pedals-pedals-spd.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-mtb-pedals-stock.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-mtb-pedals-stock.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-mtb-saddle-stock.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-mtb-saddle-stock.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-mtb-seatpost-seatpost-carbon.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-mtb-seatpost-seatpost-carbon.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-mtb-seatpost-stock.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-mtb-seatpost-stock.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-mtb-tyres-stock.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-mtb-tyres-stock.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-mtb-tyres-tyre-mtb-xc.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-mtb-tyres-tyre-mtb-xc.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-mtb-wheels-stock.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-mtb-wheels-stock.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-bag-bag-top-tube.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-bag-bag-top-tube.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-bag-stock.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-bag-stock.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-bar-tape-bar-tape-tacky.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-bar-tape-bar-tape-tacky.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-bar-tape-stock.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-bar-tape-stock.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-bottle-cages-cage-carbon.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-bottle-cages-cage-carbon.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-bottle-cages-stock.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-bottle-cages-stock.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-cassette-stock.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-cassette-stock.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-chain-stock.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-chain-stock.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-cockpit-cockpit-carbon.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-cockpit-cockpit-carbon.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-cockpit-cockpit-extensions.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-cockpit-cockpit-extensions.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-cockpit-cockpit-integrated.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-cockpit-cockpit-integrated.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-cockpit-stock.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-cockpit-stock.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-computer-computer-large.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-computer-computer-large.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-computer-stock.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-computer-stock.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-crankset-crank-power.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-crankset-crank-power.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-crankset-stock.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-crankset-stock.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-frame-stock.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-frame-stock.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-groupset-groupset-electronic-top.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-groupset-groupset-electronic-top.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-groupset-groupset-electronic.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-groupset-groupset-electronic.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-groupset-groupset-mech.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-groupset-groupset-mech.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-groupset-stock.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-groupset-stock.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-lights-lights-set.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-lights-lights-set.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-lights-stock.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-lights-stock.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-paint-stock.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-paint-stock.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-pedals-pedals-road-carbon.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-pedals-pedals-road-carbon.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-pedals-stock.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-pedals-stock.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-saddle-saddle-short-nose.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-saddle-saddle-short-nose.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-saddle-stock.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-saddle-stock.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-seatpost-seatpost-carbon.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-seatpost-seatpost-carbon.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-seatpost-stock.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-seatpost-stock.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-tyres-stock.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-tyres-stock.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-tyres-tyre-road-25-tt.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-tyres-tyre-road-25-tt.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-tyres-tyre-road-28-training.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-tyres-tyre-road-28-training.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-tyres-tyre-road-28.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-tyres-tyre-road-28.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-wheels-stock.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-wheels-stock.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-wheels-wheel-alloy-performance.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-wheels-wheel-alloy-performance.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-wheels-wheel-alloy-training.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-wheels-wheel-alloy-training.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-wheels-wheel-carbon-45.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-wheels-wheel-carbon-45.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-wheels-wheel-carbon-50.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-road-wheels-wheel-carbon-50.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-tt-bag-stock.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-tt-bag-stock.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-tt-bar-tape-stock.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-tt-bar-tape-stock.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-tt-bottle-cages-cage-carbon.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-tt-bottle-cages-cage-carbon.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-tt-bottle-cages-stock.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-tt-bottle-cages-stock.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-tt-cassette-stock.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-tt-cassette-stock.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-tt-chain-stock.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-tt-chain-stock.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-tt-cockpit-stock.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-tt-cockpit-stock.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-tt-computer-computer-large.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-tt-computer-computer-large.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-tt-computer-stock.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-tt-computer-stock.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-tt-crankset-crank-power.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-tt-crankset-crank-power.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-tt-crankset-stock.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-tt-crankset-stock.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-tt-frame-stock.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-tt-frame-stock.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-tt-groupset-groupset-electronic-top.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-tt-groupset-groupset-electronic-top.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-tt-groupset-groupset-electronic.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-tt-groupset-groupset-electronic.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-tt-groupset-groupset-mech.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-tt-groupset-groupset-mech.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-tt-groupset-stock.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-tt-groupset-stock.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-tt-lights-stock.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-tt-lights-stock.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-tt-paint-stock.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-tt-paint-stock.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-tt-pedals-pedals-road-carbon.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-tt-pedals-pedals-road-carbon.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-tt-pedals-stock.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-tt-pedals-stock.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-tt-saddle-saddle-short-nose.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-tt-saddle-saddle-short-nose.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-tt-saddle-stock.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-tt-saddle-stock.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-tt-seatpost-stock.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-tt-seatpost-stock.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-tt-tyres-stock.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-tt-tyres-stock.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-tt-tyres-tyre-road-25-tt.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-tt-tyres-tyre-road-25-tt.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-tt-tyres-tyre-road-28-training.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-tt-tyres-tyre-road-28-training.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-tt-tyres-tyre-road-28.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-tt-tyres-tyre-road-28.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-tt-wheels-stock.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-tt-wheels-stock.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-tt-wheels-wheel-alloy-performance.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-tt-wheels-wheel-alloy-performance.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-tt-wheels-wheel-alloy-training.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-tt-wheels-wheel-alloy-training.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-tt-wheels-wheel-carbon-45.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-tt-wheels-wheel-carbon-45.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-tt-wheels-wheel-carbon-50.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-tt-wheels-wheel-carbon-50.png) |
| 18:37:41 | [183741-fix-stand-tile-pictures-2026-11-17-thumbs-tt-wheels-wheel-disc-tt.png](183741-fix-stand-tile-pictures-2026-11-17-thumbs-tt-wheels-wheel-disc-tt.png) |
| 18:37:42 | [183742-fix-stand-tile-pictures-2026-11-17-compare-thumb-cockpit.png](183742-fix-stand-tile-pictures-2026-11-17-compare-thumb-cockpit.png) |
| 18:37:42 | [183742-fix-stand-tile-pictures-2026-11-17-compare-thumb-saddle.png](183742-fix-stand-tile-pictures-2026-11-17-compare-thumb-saddle.png) |
| 18:37:42 | [183742-fix-stand-tile-pictures-2026-11-17-compare-thumb-tyres.png](183742-fix-stand-tile-pictures-2026-11-17-compare-thumb-tyres.png) |
| 18:37:42 | [183742-fix-stand-tile-pictures-2026-11-17-compare-thumb-vs-tile-cockpit.png](183742-fix-stand-tile-pictures-2026-11-17-compare-thumb-vs-tile-cockpit.png) |
| 18:37:42 | [183742-fix-stand-tile-pictures-2026-11-17-compare-thumb-vs-tile-saddle.png](183742-fix-stand-tile-pictures-2026-11-17-compare-thumb-vs-tile-saddle.png) |
| 18:37:42 | [183742-fix-stand-tile-pictures-2026-11-17-compare-thumb-vs-tile-tyres.png](183742-fix-stand-tile-pictures-2026-11-17-compare-thumb-vs-tile-tyres.png) |
| 18:37:42 | [183742-fix-stand-tile-pictures-2026-11-17-compare-tile-cockpit.png](183742-fix-stand-tile-pictures-2026-11-17-compare-tile-cockpit.png) |
| 18:37:42 | [183742-fix-stand-tile-pictures-2026-11-17-compare-tile-saddle.png](183742-fix-stand-tile-pictures-2026-11-17-compare-tile-saddle.png) |
| 18:37:42 | [183742-fix-stand-tile-pictures-2026-11-17-compare-tile-tyres.png](183742-fix-stand-tile-pictures-2026-11-17-compare-tile-tyres.png) |
| 18:52:53 | [185253-scenes-char-editor-tiles-hair.jpg](185253-scenes-char-editor-tiles-hair.jpg) |
| 18:52:53 | [185253-scenes-fix-stand-tiles-cockpit.jpg](185253-scenes-fix-stand-tiles-cockpit.jpg) |
| 18:52:53 | [185253-scenes-fix-stand-tiles-groupset.jpg](185253-scenes-fix-stand-tiles-groupset.jpg) |
| 18:52:53 | [185253-scenes-fix-stand-tiles-saddle.jpg](185253-scenes-fix-stand-tiles-saddle.jpg) |
| 18:52:53 | [185253-scenes-fix-stand-tiles-tyres.jpg](185253-scenes-fix-stand-tiles-tyres.jpg) |
| 18:52:53 | [185253-scenes-thumbs-dump.jpg](185253-scenes-thumbs-dump.jpg) |
| 19:02:45 | [190245-fix-thumb-framing-2026-11-17-compare-fix-stand-tiles-cockpit.jpg](190245-fix-thumb-framing-2026-11-17-compare-fix-stand-tiles-cockpit.jpg) |
| 19:02:45 | [190245-fix-thumb-framing-2026-11-17-compare-fix-stand-tiles-groupset.jpg](190245-fix-thumb-framing-2026-11-17-compare-fix-stand-tiles-groupset.jpg) |
| 19:02:45 | [190245-fix-thumb-framing-2026-11-17-compare-fix-stand-tiles-saddle.jpg](190245-fix-thumb-framing-2026-11-17-compare-fix-stand-tiles-saddle.jpg) |
| 19:02:45 | [190245-fix-thumb-framing-2026-11-17-compare-fix-stand-tiles-tyres.jpg](190245-fix-thumb-framing-2026-11-17-compare-fix-stand-tiles-tyres.jpg) |
| 19:02:45 | [190245-fix-thumb-framing-2026-11-17-compare-tile-groupset.png](190245-fix-thumb-framing-2026-11-17-compare-tile-groupset.png) |
| 19:02:45 | [190245-fix-thumb-framing-2026-11-17-compare-tile-tyres-after.png](190245-fix-thumb-framing-2026-11-17-compare-tile-tyres-after.png) |
| 19:02:45 | [190245-fix-thumb-framing-2026-11-17-compare-tile-tyres.png](190245-fix-thumb-framing-2026-11-17-compare-tile-tyres.png) |
| 19:02:46 | [190246-fix-thumb-framing-2026-11-17-compare-hair-tiles-before.png](190246-fix-thumb-framing-2026-11-17-compare-hair-tiles-before.png) |
| 19:02:46 | [190246-fix-thumb-framing-2026-11-17-compare-tile-cockpit-after.png](190246-fix-thumb-framing-2026-11-17-compare-tile-cockpit-after.png) |
| 19:02:46 | [190246-fix-thumb-framing-2026-11-17-compare-tile-cockpit.png](190246-fix-thumb-framing-2026-11-17-compare-tile-cockpit.png) |
| 19:02:46 | [190246-fix-thumb-framing-2026-11-17-compare-tile-saddle-after.png](190246-fix-thumb-framing-2026-11-17-compare-tile-saddle-after.png) |
| 19:02:46 | [190246-fix-thumb-framing-2026-11-17-compare-tile-saddle.png](190246-fix-thumb-framing-2026-11-17-compare-tile-saddle.png) |
| 19:03:46 | [190346-scenes-char-editor-tiles-hair.jpg](190346-scenes-char-editor-tiles-hair.jpg) |
| 19:03:46 | [190346-scenes-fix-stand-tiles-groupset.jpg](190346-scenes-fix-stand-tiles-groupset.jpg) |
| 19:12:21 | [191221-fix-thumb-framing-2026-11-17-after-char-editor-tiles-hair.jpg](191221-fix-thumb-framing-2026-11-17-after-char-editor-tiles-hair.jpg) |
| 19:12:22 | [191222-fix-thumb-framing-2026-11-17-compare-char-editor-tiles-hair.jpg](191222-fix-thumb-framing-2026-11-17-compare-char-editor-tiles-hair.jpg) |
| 19:12:22 | [191222-fix-thumb-framing-2026-11-17-compare-hair-tiles-after.png](191222-fix-thumb-framing-2026-11-17-compare-hair-tiles-after.png) |
| 19:12:22 | [191222-fix-thumb-framing-2026-11-17-compare-hair-tiles.png](191222-fix-thumb-framing-2026-11-17-compare-hair-tiles.png) |
| 19:36:10 | [193610-fix-drivetrain-thumbs-2026-11-17-before-fix-stand-tiles-cassette.jpg](193610-fix-drivetrain-thumbs-2026-11-17-before-fix-stand-tiles-cassette.jpg) |
| 19:36:10 | [193610-fix-drivetrain-thumbs-2026-11-17-before-fix-stand-tiles-chain.jpg](193610-fix-drivetrain-thumbs-2026-11-17-before-fix-stand-tiles-chain.jpg) |
| 19:36:10 | [193610-fix-drivetrain-thumbs-2026-11-17-before-fix-stand-tiles-crankset.jpg](193610-fix-drivetrain-thumbs-2026-11-17-before-fix-stand-tiles-crankset.jpg) |
| 19:36:10 | [193610-fix-drivetrain-thumbs-2026-11-17-before-fix-stand-tiles-groupset.jpg](193610-fix-drivetrain-thumbs-2026-11-17-before-fix-stand-tiles-groupset.jpg) |
| 19:45:27 | [194527-fix-drivetrain-thumbs-2026-11-17-after-fix-stand-tiles-cassette.jpg](194527-fix-drivetrain-thumbs-2026-11-17-after-fix-stand-tiles-cassette.jpg) |
| 19:45:27 | [194527-fix-drivetrain-thumbs-2026-11-17-after-fix-stand-tiles-chain.jpg](194527-fix-drivetrain-thumbs-2026-11-17-after-fix-stand-tiles-chain.jpg) |
| 19:45:27 | [194527-fix-drivetrain-thumbs-2026-11-17-after-fix-stand-tiles-crankset.jpg](194527-fix-drivetrain-thumbs-2026-11-17-after-fix-stand-tiles-crankset.jpg) |
| 19:45:27 | [194527-fix-drivetrain-thumbs-2026-11-17-after-fix-stand-tiles-groupset.jpg](194527-fix-drivetrain-thumbs-2026-11-17-after-fix-stand-tiles-groupset.jpg) |
| 19:45:27 | [194527-fix-drivetrain-thumbs-2026-11-17-compare-fix-stand-tiles-groupset.jpg](194527-fix-drivetrain-thumbs-2026-11-17-compare-fix-stand-tiles-groupset.jpg) |
| 19:45:27 | [194527-fix-drivetrain-thumbs-2026-11-17-compare-tile-groupset-before.png](194527-fix-drivetrain-thumbs-2026-11-17-compare-tile-groupset-before.png) |
| 19:45:28 | [194528-fix-drivetrain-thumbs-2026-11-17-compare-fix-stand-tiles-cassette.jpg](194528-fix-drivetrain-thumbs-2026-11-17-compare-fix-stand-tiles-cassette.jpg) |
| 19:45:28 | [194528-fix-drivetrain-thumbs-2026-11-17-compare-fix-stand-tiles-chain.jpg](194528-fix-drivetrain-thumbs-2026-11-17-compare-fix-stand-tiles-chain.jpg) |
| 19:45:28 | [194528-fix-drivetrain-thumbs-2026-11-17-compare-fix-stand-tiles-crankset.jpg](194528-fix-drivetrain-thumbs-2026-11-17-compare-fix-stand-tiles-crankset.jpg) |
| 19:45:28 | [194528-fix-drivetrain-thumbs-2026-11-17-compare-tile-cassette-after.png](194528-fix-drivetrain-thumbs-2026-11-17-compare-tile-cassette-after.png) |
| 19:45:28 | [194528-fix-drivetrain-thumbs-2026-11-17-compare-tile-cassette-before.png](194528-fix-drivetrain-thumbs-2026-11-17-compare-tile-cassette-before.png) |
| 19:45:28 | [194528-fix-drivetrain-thumbs-2026-11-17-compare-tile-cassette.png](194528-fix-drivetrain-thumbs-2026-11-17-compare-tile-cassette.png) |
| 19:45:28 | [194528-fix-drivetrain-thumbs-2026-11-17-compare-tile-chain-after.png](194528-fix-drivetrain-thumbs-2026-11-17-compare-tile-chain-after.png) |
| 19:45:28 | [194528-fix-drivetrain-thumbs-2026-11-17-compare-tile-chain-before.png](194528-fix-drivetrain-thumbs-2026-11-17-compare-tile-chain-before.png) |
| 19:45:28 | [194528-fix-drivetrain-thumbs-2026-11-17-compare-tile-chain.png](194528-fix-drivetrain-thumbs-2026-11-17-compare-tile-chain.png) |
| 19:45:28 | [194528-fix-drivetrain-thumbs-2026-11-17-compare-tile-groupset-after.png](194528-fix-drivetrain-thumbs-2026-11-17-compare-tile-groupset-after.png) |
| 19:45:28 | [194528-fix-drivetrain-thumbs-2026-11-17-compare-tile-groupset.png](194528-fix-drivetrain-thumbs-2026-11-17-compare-tile-groupset.png) |
| 19:45:29 | [194529-fix-drivetrain-thumbs-2026-11-17-compare-tile-crankset-after.png](194529-fix-drivetrain-thumbs-2026-11-17-compare-tile-crankset-after.png) |
| 19:45:29 | [194529-fix-drivetrain-thumbs-2026-11-17-compare-tile-crankset-before.png](194529-fix-drivetrain-thumbs-2026-11-17-compare-tile-crankset-before.png) |
| 19:45:29 | [194529-fix-drivetrain-thumbs-2026-11-17-compare-tile-crankset.png](194529-fix-drivetrain-thumbs-2026-11-17-compare-tile-crankset.png) |
| 20:42:46 | [204246-windows-icon-2026-11-17-ocw-desktop-128.png](204246-windows-icon-2026-11-17-ocw-desktop-128.png) |
| 20:42:46 | [204246-windows-icon-2026-11-17-ocw-desktop-16.png](204246-windows-icon-2026-11-17-ocw-desktop-16.png) |
| 20:42:46 | [204246-windows-icon-2026-11-17-ocw-desktop-24.png](204246-windows-icon-2026-11-17-ocw-desktop-24.png) |
| 20:42:46 | [204246-windows-icon-2026-11-17-ocw-desktop-256.png](204246-windows-icon-2026-11-17-ocw-desktop-256.png) |
| 20:42:46 | [204246-windows-icon-2026-11-17-ocw-desktop-32.png](204246-windows-icon-2026-11-17-ocw-desktop-32.png) |
| 20:42:46 | [204246-windows-icon-2026-11-17-ocw-desktop-48.png](204246-windows-icon-2026-11-17-ocw-desktop-48.png) |
| 20:42:46 | [204246-windows-icon-2026-11-17-ocw-desktop-64.png](204246-windows-icon-2026-11-17-ocw-desktop-64.png) |
| 21:37:24 | [213724-shot-wayland-fix-grip-hoods-right.jpg](213724-shot-wayland-fix-grip-hoods-right.jpg) |
| 21:37:33 | [213733-shot-wayland-fix-grip-hoods-left.jpg](213733-shot-wayland-fix-grip-hoods-left.jpg) |
| 21:37:42 | [213742-shot-wayland-fix-grip-hoods-above.jpg](213742-shot-wayland-fix-grip-hoods-above.jpg) |
| 21:37:51 | [213751-shot-wayland-fix-grip-tops-right.jpg](213751-shot-wayland-fix-grip-tops-right.jpg) |
| 21:38:01 | [213801-shot-wayland-fix-grip-tops-left.jpg](213801-shot-wayland-fix-grip-tops-left.jpg) |
| 21:38:10 | [213810-shot-wayland-fix-grip-tops-above.jpg](213810-shot-wayland-fix-grip-tops-above.jpg) |
| 21:38:19 | [213819-shot-wayland-fix-grip-drops-right.jpg](213819-shot-wayland-fix-grip-drops-right.jpg) |
| 21:38:29 | [213829-shot-wayland-fix-grip-drops-left.jpg](213829-shot-wayland-fix-grip-drops-left.jpg) |
| 21:38:38 | [213838-shot-wayland-fix-grip-drops-above.jpg](213838-shot-wayland-fix-grip-drops-above.jpg) |
| 21:38:47 | [213847-shot-wayland-fix-grip-tt-right.jpg](213847-shot-wayland-fix-grip-tt-right.jpg) |
| 21:38:56 | [213856-shot-wayland-fix-grip-tt-left.jpg](213856-shot-wayland-fix-grip-tt-left.jpg) |
| 21:39:05 | [213905-shot-wayland-fix-grip-tt-above.jpg](213905-shot-wayland-fix-grip-tt-above.jpg) |
| 21:39:15 | [213915-shot-wayland-fix-grip-mtb-right.jpg](213915-shot-wayland-fix-grip-mtb-right.jpg) |
| 21:39:24 | [213924-shot-wayland-fix-grip-mtb-left.jpg](213924-shot-wayland-fix-grip-mtb-left.jpg) |
| 21:39:33 | [213933-shot-wayland-fix-grip-mtb-above.jpg](213933-shot-wayland-fix-grip-mtb-above.jpg) |
| 21:39:42 | [213942-shot-wayland-fix-grip-gravel-right.jpg](213942-shot-wayland-fix-grip-gravel-right.jpg) |
| 21:39:51 | [213951-shot-wayland-fix-grip-gravel-left.jpg](213951-shot-wayland-fix-grip-gravel-left.jpg) |
| 21:40:00 | [214000-shot-wayland-fix-grip-gravel-above.jpg](214000-shot-wayland-fix-grip-gravel-above.jpg) |
| 21:40:10 | [214010-shot-wayland-fix-grip-phone-right.jpg](214010-shot-wayland-fix-grip-phone-right.jpg) |
| 21:40:20 | [214020-shot-wayland-fix-grip-phone-left.jpg](214020-shot-wayland-fix-grip-phone-left.jpg) |
| 21:40:29 | [214029-shot-wayland-fix-grip-phone-above.jpg](214029-shot-wayland-fix-grip-phone-above.jpg) |
| 21:41:19 | [214119-shot-wayland-fix-grip-hoods-right.jpg](214119-shot-wayland-fix-grip-hoods-right.jpg) |
| 21:41:28 | [214128-shot-wayland-fix-grip-hoods-left.jpg](214128-shot-wayland-fix-grip-hoods-left.jpg) |
| 21:41:36 | [214136-shot-wayland-fix-grip-hoods-above.jpg](214136-shot-wayland-fix-grip-hoods-above.jpg) |
| 21:41:46 | [214146-shot-wayland-fix-grip-tops-right.jpg](214146-shot-wayland-fix-grip-tops-right.jpg) |
| 21:41:53 | [214153-vr-head-sim-both-eyes.jpg](214153-vr-head-sim-both-eyes.jpg) |
| 21:41:55 | [214155-shot-wayland-fix-grip-tops-left.jpg](214155-shot-wayland-fix-grip-tops-left.jpg) |
| 21:42:04 | [214204-shot-wayland-fix-grip-tops-above.jpg](214204-shot-wayland-fix-grip-tops-above.jpg) |
| 21:42:13 | [214213-shot-wayland-fix-grip-drops-right.jpg](214213-shot-wayland-fix-grip-drops-right.jpg) |
| 21:42:22 | [214222-shot-wayland-fix-grip-drops-left.jpg](214222-shot-wayland-fix-grip-drops-left.jpg) |
| 21:42:25 | [214225-vr-head-sim-chase-mirror.jpg](214225-vr-head-sim-chase-mirror.jpg) |
| 21:42:30 | [214230-shot-wayland-fix-grip-drops-above.jpg](214230-shot-wayland-fix-grip-drops-above.jpg) |
| 21:42:39 | [214239-shot-wayland-fix-grip-tt-right.jpg](214239-shot-wayland-fix-grip-tt-right.jpg) |
| 21:42:47 | [214247-shot-wayland-fix-grip-tt-left.jpg](214247-shot-wayland-fix-grip-tt-left.jpg) |
| 21:42:56 | [214256-shot-wayland-fix-grip-tt-above.jpg](214256-shot-wayland-fix-grip-tt-above.jpg) |
| 21:43:05 | [214305-shot-wayland-fix-grip-mtb-right.jpg](214305-shot-wayland-fix-grip-mtb-right.jpg) |
| 21:43:14 | [214314-shot-wayland-fix-grip-mtb-left.jpg](214314-shot-wayland-fix-grip-mtb-left.jpg) |
| 21:43:22 | [214322-shot-wayland-fix-grip-mtb-above.jpg](214322-shot-wayland-fix-grip-mtb-above.jpg) |
| 21:43:30 | [214330-shot-wayland-fix-grip-gravel-right.jpg](214330-shot-wayland-fix-grip-gravel-right.jpg) |
| 21:43:39 | [214339-shot-wayland-fix-grip-gravel-left.jpg](214339-shot-wayland-fix-grip-gravel-left.jpg) |
| 21:43:48 | [214348-shot-wayland-fix-grip-gravel-above.jpg](214348-shot-wayland-fix-grip-gravel-above.jpg) |
| 21:43:58 | [214358-shot-wayland-fix-grip-phone-right.jpg](214358-shot-wayland-fix-grip-phone-right.jpg) |
| 21:44:08 | [214408-shot-wayland-fix-grip-phone-left.jpg](214408-shot-wayland-fix-grip-phone-left.jpg) |
| 21:44:18 | [214418-shot-wayland-fix-grip-phone-above.jpg](214418-shot-wayland-fix-grip-phone-above.jpg) |
| 22:04:47 | [220447-studio-logo-2026-11-17-ocw-16.png](220447-studio-logo-2026-11-17-ocw-16.png) |
| 22:04:47 | [220447-studio-logo-2026-11-17-ocw-32.png](220447-studio-logo-2026-11-17-ocw-32.png) |
| 22:04:47 | [220447-studio-logo-2026-11-17-ocw-512.png](220447-studio-logo-2026-11-17-ocw-512.png) |
| 22:05:20 | [220520-studio-logo-2026-11-17-ocw-studio-16.png](220520-studio-logo-2026-11-17-ocw-studio-16.png) |
| 22:05:20 | [220520-studio-logo-2026-11-17-ocw-studio-32.png](220520-studio-logo-2026-11-17-ocw-studio-32.png) |
| 22:05:20 | [220520-studio-logo-2026-11-17-ocw-studio-512.png](220520-studio-logo-2026-11-17-ocw-studio-512.png) |
| 22:05:20 | [220520-studio-logo-2026-11-17-ocw-studio-svg-32-full-detail.png](220520-studio-logo-2026-11-17-ocw-studio-svg-32-full-detail.png) |
| 22:05:20 | [220520-studio-logo-2026-11-17-studio-logo-compare.png](220520-studio-logo-2026-11-17-studio-logo-compare.png) |
| 22:08:32 | [220832-ground-detail-try-tenerife-masca-km9-rider-off-x11.jpg](220832-ground-detail-try-tenerife-masca-km9-rider-off-x11.jpg) |
| 22:09:09 | [220909-ground-detail-try-tenerife-masca-km9-rider-on-x11.jpg](220909-ground-detail-try-tenerife-masca-km9-rider-on-x11.jpg) |
| 22:09:46 | [220946-ground-detail-try-tenerife-masca-km9-orbit-off-x11.jpg](220946-ground-detail-try-tenerife-masca-km9-orbit-off-x11.jpg) |
| 22:10:32 | [221032-ground-detail-try-tenerife-masca-km9-orbit-on-x11.jpg](221032-ground-detail-try-tenerife-masca-km9-orbit-on-x11.jpg) |
| 22:19:46 | [221946-ground-detail-tenerife-masca-km9-rider-off-x11.jpg](221946-ground-detail-tenerife-masca-km9-rider-off-x11.jpg) |
| 22:20:20 | [222020-ground-detail-tenerife-masca-km9-rider-off-wayland.jpg](222020-ground-detail-tenerife-masca-km9-rider-off-wayland.jpg) |
| 22:20:47 | [222047-ground-detail-tenerife-masca-km9-rider-on-x11.jpg](222047-ground-detail-tenerife-masca-km9-rider-on-x11.jpg) |
| 22:23:51 | [222351-ground-detail-tenerife-masca-km9-rider-on-wayland.jpg](222351-ground-detail-tenerife-masca-km9-rider-on-wayland.jpg) |
| 22:24:18 | [222418-ground-detail-tenerife-masca-km9-orbit-off-x11.jpg](222418-ground-detail-tenerife-masca-km9-orbit-off-x11.jpg) |
| 22:24:50 | [222450-ground-detail-tenerife-masca-km9-orbit-off-wayland.jpg](222450-ground-detail-tenerife-masca-km9-orbit-off-wayland.jpg) |
| 22:25:17 | [222517-ground-detail-tenerife-masca-km9-orbit-on-x11.jpg](222517-ground-detail-tenerife-masca-km9-orbit-on-x11.jpg) |
| 22:25:53 | [222553-ground-detail-tenerife-masca-km9-orbit-on-wayland.jpg](222553-ground-detail-tenerife-masca-km9-orbit-on-wayland.jpg) |
| 22:26:24 | [222624-ground-detail-blackforest-forest-road-rider-off-x11.jpg](222624-ground-detail-blackforest-forest-road-rider-off-x11.jpg) |
| 22:27:01 | [222701-ground-detail-blackforest-forest-road-rider-off-wayland.jpg](222701-ground-detail-blackforest-forest-road-rider-off-wayland.jpg) |
| 22:27:28 | [222728-ground-detail-blackforest-forest-road-rider-on-x11.jpg](222728-ground-detail-blackforest-forest-road-rider-on-x11.jpg) |
| 22:28:15 | [222815-ground-detail-blackforest-forest-road-rider-on-wayland.jpg](222815-ground-detail-blackforest-forest-road-rider-on-wayland.jpg) |
| 22:28:47 | [222847-ground-detail-blackforest-forest-road-orbit-off-x11.jpg](222847-ground-detail-blackforest-forest-road-orbit-off-x11.jpg) |
| 22:29:28 | [222928-ground-detail-blackforest-forest-road-orbit-off-wayland.jpg](222928-ground-detail-blackforest-forest-road-orbit-off-wayland.jpg) |
| 22:30:01 | [223001-ground-detail-blackforest-forest-road-orbit-on-x11.jpg](223001-ground-detail-blackforest-forest-road-orbit-on-x11.jpg) |
| 22:30:48 | [223048-ground-detail-blackforest-forest-road-orbit-on-wayland.jpg](223048-ground-detail-blackforest-forest-road-orbit-on-wayland.jpg) |
| 22:31:29 | [223129-shot-liechtenstein-meadow-road-rider-off-x11.jpg](223129-shot-liechtenstein-meadow-road-rider-off-x11.jpg) |
| 22:31:39 | [223139-shot-ocw.jpg](223139-shot-ocw.jpg) |
| 22:31:48 | [223148-shot-wayland-liechtenstein-meadow-road-rider-off-wayland.jpg](223148-shot-wayland-liechtenstein-meadow-road-rider-off-wayland.jpg) |
| 22:31:50 | [223150-shot-wayland-ocw-wayland.jpg](223150-shot-wayland-ocw-wayland.jpg) |
| 22:32:29 | [223229-shot-liechtenstein-meadow-road-rider-on-x11.jpg](223229-shot-liechtenstein-meadow-road-rider-on-x11.jpg) |
| 22:32:47 | [223247-shot-wayland-liechtenstein-meadow-road-rider-on-wayland.jpg](223247-shot-wayland-liechtenstein-meadow-road-rider-on-wayland.jpg) |
| 22:33:30 | [223330-shot-liechtenstein-meadow-road-orbit-off-x11.jpg](223330-shot-liechtenstein-meadow-road-orbit-off-x11.jpg) |
| 22:33:49 | [223349-shot-wayland-liechtenstein-meadow-road-orbit-off-wayland.jpg](223349-shot-wayland-liechtenstein-meadow-road-orbit-off-wayland.jpg) |
| 22:34:33 | [223433-shot-liechtenstein-meadow-road-orbit-on-x11.jpg](223433-shot-liechtenstein-meadow-road-orbit-on-x11.jpg) |
| 22:34:52 | [223452-shot-wayland-liechtenstein-meadow-road-orbit-on-wayland.jpg](223452-shot-wayland-liechtenstein-meadow-road-orbit-on-wayland.jpg) |
| 22:35:51 | [223551-shot-blackforest-autumn-rider-off-x11.jpg](223551-shot-blackforest-autumn-rider-off-x11.jpg) |
| 22:36:13 | [223613-shot-wayland-blackforest-autumn-rider-off-wayland.jpg](223613-shot-wayland-blackforest-autumn-rider-off-wayland.jpg) |
| 22:37:03 | [223703-shot-blackforest-autumn-rider-on-x11.jpg](223703-shot-blackforest-autumn-rider-on-x11.jpg) |
| 22:37:24 | [223724-studio-logo-2026-11-17-windows-exe-icon-ocw-studio-128.png](223724-studio-logo-2026-11-17-windows-exe-icon-ocw-studio-128.png) |
| 22:37:24 | [223724-studio-logo-2026-11-17-windows-exe-icon-ocw-studio-16.png](223724-studio-logo-2026-11-17-windows-exe-icon-ocw-studio-16.png) |
| 22:37:24 | [223724-studio-logo-2026-11-17-windows-exe-icon-ocw-studio-24.png](223724-studio-logo-2026-11-17-windows-exe-icon-ocw-studio-24.png) |
| 22:37:24 | [223724-studio-logo-2026-11-17-windows-exe-icon-ocw-studio-256.png](223724-studio-logo-2026-11-17-windows-exe-icon-ocw-studio-256.png) |
| 22:37:24 | [223724-studio-logo-2026-11-17-windows-exe-icon-ocw-studio-32.png](223724-studio-logo-2026-11-17-windows-exe-icon-ocw-studio-32.png) |
| 22:37:24 | [223724-studio-logo-2026-11-17-windows-exe-icon-ocw-studio-48.png](223724-studio-logo-2026-11-17-windows-exe-icon-ocw-studio-48.png) |
| 22:37:24 | [223724-studio-logo-2026-11-17-windows-exe-icon-ocw-studio-64.png](223724-studio-logo-2026-11-17-windows-exe-icon-ocw-studio-64.png) |
| 22:37:25 | [223725-shot-wayland-blackforest-autumn-rider-on-wayland.jpg](223725-shot-wayland-blackforest-autumn-rider-on-wayland.jpg) |
| 22:38:21 | [223821-shot-blackforest-autumn-orbit-off-x11.jpg](223821-shot-blackforest-autumn-orbit-off-x11.jpg) |
| 22:38:43 | [223843-shot-wayland-blackforest-autumn-orbit-off-wayland.jpg](223843-shot-wayland-blackforest-autumn-orbit-off-wayland.jpg) |
| 22:39:40 | [223940-shot-blackforest-autumn-orbit-on-x11.jpg](223940-shot-blackforest-autumn-orbit-on-x11.jpg) |
| 22:40:02 | [224002-shot-wayland-blackforest-autumn-orbit-on-wayland.jpg](224002-shot-wayland-blackforest-autumn-orbit-on-wayland.jpg) |
| 22:40:23 | [224023-ground-detail-liechtenstein-snow-rider-off-x11.jpg](224023-ground-detail-liechtenstein-snow-rider-off-x11.jpg) |
| 22:40:46 | [224046-ground-detail-liechtenstein-snow-rider-off-wayland.jpg](224046-ground-detail-liechtenstein-snow-rider-off-wayland.jpg) |
| 22:41:06 | [224106-ground-detail-liechtenstein-snow-rider-on-x11.jpg](224106-ground-detail-liechtenstein-snow-rider-on-x11.jpg) |
| 22:41:28 | [224128-ground-detail-liechtenstein-snow-rider-on-wayland.jpg](224128-ground-detail-liechtenstein-snow-rider-on-wayland.jpg) |
| 22:41:49 | [224149-ground-detail-liechtenstein-snow-orbit-off-x11.jpg](224149-ground-detail-liechtenstein-snow-orbit-off-x11.jpg) |
| 22:42:12 | [224212-ground-detail-liechtenstein-snow-orbit-off-wayland.jpg](224212-ground-detail-liechtenstein-snow-orbit-off-wayland.jpg) |
| 22:42:35 | [224235-ground-detail-liechtenstein-snow-orbit-on-x11.jpg](224235-ground-detail-liechtenstein-snow-orbit-on-x11.jpg) |
| 22:43:01 | [224301-ground-detail-liechtenstein-snow-orbit-on-wayland.jpg](224301-ground-detail-liechtenstein-snow-orbit-on-wayland.jpg) |
| 22:54:00 | [225400-web-web-calendar-select.jpg](225400-web-web-calendar-select.jpg) |
| 22:54:00 | [225400-web-web-calendar.jpg](225400-web-web-calendar.jpg) |
| 22:54:00 | [225400-web-web-console.jpg](225400-web-web-console.jpg) |
| 22:54:00 | [225400-web-web-downloads-ocw-2026-11-17-22-55-23.jpg](225400-web-web-downloads-ocw-2026-11-17-22-55-23.jpg) |
| 22:54:00 | [225400-web-web-downloads-ocw-2026-11-17-22-55-27.webm](225400-web-web-downloads-ocw-2026-11-17-22-55-27.webm) |
| 22:54:00 | [225400-web-web-gamepad.jpg](225400-web-web-gamepad.jpg) |
| 22:54:00 | [225400-web-web-gps.jpg](225400-web-web-gps.jpg) |
| 22:54:00 | [225400-web-web-hud.jpg](225400-web-web-hud.jpg) |
| 22:54:00 | [225400-web-web-join.jpg](225400-web-web-join.jpg) |
| 22:54:00 | [225400-web-web-menu.jpg](225400-web-web-menu.jpg) |
| 22:54:00 | [225400-web-web-ride.jpg](225400-web-web-ride.jpg) |
| 22:54:00 | [225400-web-web-riders.jpg](225400-web-web-riders.jpg) |
| 22:54:00 | [225400-web-web-settings.jpg](225400-web-web-settings.jpg) |
| 22:54:00 | [225400-web-web-touch-hints.jpg](225400-web-web-touch-hints.jpg) |
| 22:54:00 | [225400-web-web-touch-hold.jpg](225400-web-web-touch-hold.jpg) |
| 22:54:00 | [225400-web-web-unicorn-flight.jpg](225400-web-web-unicorn-flight.jpg) |
| 22:54:00 | [225400-web-web-unicorn-inspect.jpg](225400-web-web-unicorn-inspect.jpg) |
| 22:54:00 | [225400-web-web-unicorn-menu.jpg](225400-web-web-unicorn-menu.jpg) |
| 22:54:00 | [225400-web-web-weather.jpg](225400-web-web-weather.jpg) |
| 22:54:00 | [225400-web-web.jpg](225400-web-web.jpg) |
| 23:04:23 | [230423-web-web-world-cached-loading.jpg](230423-web-web-world-cached-loading.jpg) |
| 23:04:23 | [230423-web-web-world-cached.jpg](230423-web-web-world-cached.jpg) |
| 23:04:23 | [230423-web-web-world-first-loading.jpg](230423-web-web-world-first-loading.jpg) |
| 23:04:23 | [230423-web-web-world-teleport.jpg](230423-web-web-world-teleport.jpg) |
| 23:04:23 | [230423-web-web-world.jpg](230423-web-web-world.jpg) |
| 23:05:24 | [230524-web-web-world-webgl2-cached-loading.jpg](230524-web-web-world-webgl2-cached-loading.jpg) |
| 23:05:24 | [230524-web-web-world-webgl2-cached.jpg](230524-web-web-world-webgl2-cached.jpg) |
| 23:05:24 | [230524-web-web-world-webgl2-first-loading.jpg](230524-web-web-world-webgl2-first-loading.jpg) |
| 23:05:24 | [230524-web-web-world-webgl2-teleport.jpg](230524-web-web-world-webgl2-teleport.jpg) |
| 23:05:24 | [230524-web-web-world-webgl2.jpg](230524-web-web-world-webgl2.jpg) |
| 23:06:45 | [230645-ground-detail-liechtenstein-meadow-road-rider-off-x11.jpg](230645-ground-detail-liechtenstein-meadow-road-rider-off-x11.jpg) |
| 23:07:14 | [230714-ground-detail-liechtenstein-meadow-road-rider-off-wayland.jpg](230714-ground-detail-liechtenstein-meadow-road-rider-off-wayland.jpg) |
| 23:07:37 | [230737-ground-detail-liechtenstein-meadow-road-rider-on-x11.jpg](230737-ground-detail-liechtenstein-meadow-road-rider-on-x11.jpg) |
| 23:08:04 | [230804-ground-detail-liechtenstein-meadow-road-rider-on-wayland.jpg](230804-ground-detail-liechtenstein-meadow-road-rider-on-wayland.jpg) |
| 23:08:27 | [230827-ground-detail-liechtenstein-meadow-road-orbit-off-x11.jpg](230827-ground-detail-liechtenstein-meadow-road-orbit-off-x11.jpg) |
| 23:08:55 | [230855-ground-detail-liechtenstein-meadow-road-orbit-off-wayland.jpg](230855-ground-detail-liechtenstein-meadow-road-orbit-off-wayland.jpg) |
| 23:09:09 | [230909-studio-logo-2026-11-17-studio-window-x11.png](230909-studio-logo-2026-11-17-studio-window-x11.png) |
| 23:09:16 | [230916-ground-detail-liechtenstein-meadow-road-orbit-on-x11.jpg](230916-ground-detail-liechtenstein-meadow-road-orbit-on-x11.jpg) |
| 23:09:42 | [230942-ground-detail-liechtenstein-meadow-road-orbit-on-wayland.jpg](230942-ground-detail-liechtenstein-meadow-road-orbit-on-wayland.jpg) |
| 23:10:13 | [231013-ground-detail-blackforest-autumn-rider-off-x11.jpg](231013-ground-detail-blackforest-autumn-rider-off-x11.jpg) |
| 23:10:22 | [231022-studio-logo-2026-11-17-x11-window-icon.png](231022-studio-logo-2026-11-17-x11-window-icon.png) |
| 23:10:57 | [231057-ground-detail-blackforest-autumn-rider-off-wayland.jpg](231057-ground-detail-blackforest-autumn-rider-off-wayland.jpg) |
| 23:11:29 | [231129-ground-detail-blackforest-autumn-rider-on-x11.jpg](231129-ground-detail-blackforest-autumn-rider-on-x11.jpg) |
| 23:12:16 | [231216-ground-detail-blackforest-autumn-rider-on-wayland.jpg](231216-ground-detail-blackforest-autumn-rider-on-wayland.jpg) |
| 23:12:50 | [231250-ground-detail-blackforest-autumn-orbit-off-x11.jpg](231250-ground-detail-blackforest-autumn-orbit-off-x11.jpg) |
| 23:13:42 | [231342-ground-detail-blackforest-autumn-orbit-off-wayland.jpg](231342-ground-detail-blackforest-autumn-orbit-off-wayland.jpg) |
| 23:14:12 | [231412-ground-detail-blackforest-autumn-orbit-on-x11.jpg](231412-ground-detail-blackforest-autumn-orbit-on-x11.jpg) |
| 23:14:58 | [231458-ground-detail-blackforest-autumn-orbit-on-wayland.jpg](231458-ground-detail-blackforest-autumn-orbit-on-wayland.jpg) |
| 23:24:24 | [232424-vr-check-5min-eye-001.jpg](232424-vr-check-5min-eye-001.jpg) |
| 23:27:24 | [232724-vr-check-5min-computer-left-eye.jpg](232724-vr-check-5min-computer-left-eye.jpg) |
| 23:52:24 | [235224-models-e3-rider.jpg](235224-models-e3-rider.jpg) |
| 23:52:36 | [235236-models-e3-bike.jpg](235236-models-e3-bike.jpg) |
| 23:52:48 | [235248-models-e3-wireframe.jpg](235248-models-e3-wireframe.jpg) |
| 23:52:59 | [235259-models-e3-normals-highlight.jpg](235259-models-e3-normals-highlight.jpg) |
| 23:53:11 | [235311-models-e3-lod-auto-far.jpg](235311-models-e3-lod-auto-far.jpg) |
| 23:53:22 | [235322-models-e3-lod-near.jpg](235322-models-e3-lod-near.jpg) |
| 23:53:34 | [235334-models-e3-lod-tree-lod1.jpg](235334-models-e3-lod-tree-lod1.jpg) |
| 23:53:45 | [235345-models-e3-helmet-tryon-fat.jpg](235345-models-e3-helmet-tryon-fat.jpg) |
| 23:53:56 | [235356-models-e3-helmet-tryon-slim.jpg](235356-models-e3-helmet-tryon-slim.jpg) |
| 23:54:08 | [235408-models-e3-ride-drops.jpg](235408-models-e3-ride-drops.jpg) |
| 23:54:20 | [235420-models-e3-plant-scene-autumn.jpg](235420-models-e3-plant-scene-autumn.jpg) |
| 23:54:31 | [235431-models-e3-plant-scene-winter.jpg](235431-models-e3-plant-scene-winter.jpg) |
| 23:54:43 | [235443-models-e3-prop.jpg](235443-models-e3-prop.jpg) |
| 23:54:55 | [235455-models-e3-validator-panel.jpg](235455-models-e3-validator-panel.jpg) |
| 23:55:06 | [235506-models-e3-night.jpg](235506-models-e3-night.jpg) |
| 23:55:07 | [235507-vr-fallback-check-eye-001.jpg](235507-vr-fallback-check-eye-001.jpg) |
| 23:55:07 | [235507-vr-fallback-check-mirror-video.mp4](235507-vr-fallback-check-mirror-video.mp4) |
