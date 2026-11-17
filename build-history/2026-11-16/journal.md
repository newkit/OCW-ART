# OCW build diary – day 6, 2026-11-16

129 commits (30 merges), +58234 / −3080 lines, 667 images, 1 videos, 0 sounds.

## Commits

| Time | Commit | |
|---|---|---|
| 07:29 | `29c258a` | Dashboard decisions §4.8.8 Q2 (junction lines per world from real images; new §4.8.9 world-builder workflow) and Q3 (give-way lines only where OSM tags them) (spec 3.75) |
| 07:49 | `9cccd08` | CLAUDE.md: decision rows and commits say what was decided (not only 'Decision by the user'); test data uses only made-up names. Spec 3.75 row leads with its decisions |
| 07:53 | `b6bb074` | Riders in VR wear a VR headset on their avatar (spec 3.76, §2.6 Rider status signs) |
| 09:23 | `6e275aa` | Trainer: a steady road gives a steady load – the wind smoothed over 15 s with a hysteresis, the air's coefficient re-sent only from a 2 % change |
| 09:24 | `f087088` | cargo fmt |
| 09:25 | `e650761` | Character editor refined (planning): name, body type, age, hair, facial hair, build (spec 3.77, §14 Phase 4 4N, §2.6) |
| 09:26 | `aa24c31` | Touch steering planned: tap or hold the left / right side of the screen (spec 3.78, §3.2.3) |
| 09:27 | `f0b68a6` | At a junction the main road keeps its own surface, side roads adapt over 5–30 m (dashboard decision §4.8.8 Q1, spec 3.76) |
| 09:28 | `ffffece` | Build dashboard: a favicon – a bicycle wheel on the accent blue with a live status dot (green, amber, red, grey) |
| 09:28 | `9c37793` | Spec: the junction surface decision is version 3.79 (it reused 3.76, taken by the VR headset row) |
| 09:30 | `3de28fa` | Junction corners per world from real images: kerbs only where the region has them, radii measured (dashboard decision §4.8.8 Q4, spec 3.80) |
| 09:31 | `93a79ec` | The art project's history leaves OCW: art/ removed from every commit once the rewrite is approved (dashboard decision §11.3 Q1) |
| 09:37 | `cee51f7` | Build dashboard: a Restart button, and a changed config/machines.toml restarts it with the new machines |
| 09:44 | `80b0d53` | Spec 3.82: trainer – a steady road gives a steady load (the wind smoothed, the air's coefficient re-sent only from 2 %) |
| 10:10 | `ea2f2b0` | Never use /tmp on deb: temp files go to ~/tmp (CLAUDE.md); the dashboard unit sets TMPDIR, its Claude tasks section reads ~/tmp/claude-* too |
| 10:15 | `21348af` | Build dashboard 1.4.0: versioned – VERSION, --version, version and commit in the header and /api/status; open pages reload themselves on a new version |
| 10:17 | `a1f2b7c` | Touch steering: touch-down steers at once like a held arrow key, a tap is topped up to one step (dashboard decision §3.2.3 Q1, spec 3.83) |
| 10:19 | `8e8e649` | Touch lean steering works like the keys: the lean stays after the finger lifts (dashboard decision §3.2.3 Q2, spec 3.84) |
| 10:19 | `1800084` | A touch does not switch autodrive off: it moves the line, only the autodrive button ends it (dashboard decision §3.2.3 Q3, spec 3.85) |
| 12:01 | `27fb387` | Build dashboard 1.4.1: no cutover line on the Claude tasks card; the worktree list stays open (kept in the browser across refreshes and updates) |
| 12:11 | `06f1fb7` | Character editor: seven body shapes, unique names without a filter, every script, age on face/body/skin/hair, no renaming during a ride (user decisions 4N Q6–Q9, Q11, Q12, Q15; spec 3.86) |
| 12:15 | `e5c7188` | Character editor: body in two dimensions – base body A/B/C (shoulders, hips, chest) and the seven-step shape (user decision 4N Q6b, spec 3.87) |
| 12:26 | `c52b946` | W5 refined (planning): backend in ocw-server on PostgreSQL, one wallet and rider per account, no local wallet, 5,000 ♥ start to buy bike and kit, hosting kit built and hosting manual later (spec 3.88, §14 Phase 4 4O) |
| 12:27 | `0033521` | Touch steering in the desktop app too, on Windows / Linux touch screens (dashboard decision §3.2.3 Q6, parity rule) |
| 12:27 | `389fe4c` | In a ride one finger steers, a two-finger drag moves the camera (dashboard decision §3.2.3 Q7) |
| 12:28 | `0dbbe55` | Model files planned: export today's models into files named by function and shape, the apps use the files instead of the code (spec 3.91, §14 Phase 15 15H, stage MX) |
| 12:29 | `f28da5e` | The visible body shape is bounded to a band around weight and height, with a Match my weight marker (dashboard decision 4N Q13) |
| 12:29 | `9c4b862` | Character editor extras come later, not in its first step (dashboard decision 4N Q14) |
| 12:31 | `9143410` | Models: only exported model files, generator code removed; bike frame sizes kept, fitted at run time (dashboard decision Phase 15 Q7) |
| 12:32 | `dec712d` | Trees: at least three shape variants per species, more where variety needs it (dashboard decision Phase 15 Q8) |
| 12:32 | `db15f86` | The Blender add-on for model export is postponed (dashboard decision Phase 15 Q5) |
| 12:33 | `c6c3656` | After the export the model files are the only source; all shape generators deleted at once (dashboard decision Phase 15 Q6) |
| 12:34 | `c8928d1` | Signed in, riders are shown by their own rider name stored with the account; the provider's name is never shown (dashboard decision 4N Q10) |
| 12:34 | `f9d9c99` | All world packages rebuilt and deployed once junction J2 is checked (dashboard decision §4.8.8 Q5; all §4.8.8 questions decided) |
| 12:39 | `d0ad08a` | All four build machines build: leela again, Win11Builder for any work (the user: "use all build servers now"; spec 4.00, §11.2, CLAUDE.md) |
| 12:49 | `d502bfd` | World patches: the .ocwpatch format and its application in world-builder (spec §14 Phase 16 E5 step 1, v3.86) |
| 12:49 | `fbb94a1` | Voice built in and always on planned: the voice server comes with the app and every host starts it; Voice room Everybody by default, Selected riders as an option (asked by the user 2026-11-16; spec 4.01, §7.1) |
| 12:50 | `71b7e64` (merge) | Merge main into world patches (spec row renumbered to 4.02) |
| 13:01 | `44fd634` | OCW Studio shell built: ocw-edit and ocw-studio (spec §14 Phase 16 E1 core, v3.86) |
| 13:02 | `24ae641` | Studio: paths on screen show the home directory as ~ (screenshots are published; no user names) |
| 13:04 | `eb8b895` (merge) | Merge world patches: the .ocwpatch format (roads, removal, height points) and its application in world-builder, patch check (spec 4.02, Phase 16 E5 step 1) |
| 13:04 | `ecc198f` (merge) | Merge main into the studio shell (spec row renumbered to 4.03) |
| 13:05 | `b87a86e` | Studio: cargo fmt |
| 13:47 | `08486ed` (merge) | Merge the OCW Studio shell: ocw-edit (documents, undo / redo, autosave) and ocw-studio (package view with the game's renderer, flight controls, 2D map, World panel) (spec 4.03, Phase 16 E1 core) |
| 13:49 | `db37bfb` | Touching both sides at once does nothing, like ← + → (dashboard decision §3.2.3 Q4) |
| 13:50 | `a8294c4` | On touch the halves always steer; a junction exit is chosen by tapping the fan (dashboard decision §3.2.3 Q5) |
| 13:50 | `e37d94f` | Touch steering zones: full height below the top band, lower half as a setting (dashboard decision §3.2.3 Q8; all §3.2.3 questions decided) |
| 13:52 | `f2a2785` | Headphones only while the microphone is muted in a voice room (dashboard decision §2.6 Q1) |
| 13:54 | `fa30a67` | The phone shows while in the in-game menu, the console or the workout and world pickers (dashboard decision §2.6 Q2) |
| 13:58 | `205eda9` | The world editor's open questions as separate dashboard questions: world patches §16H Q6–Q11, studio §16H Q12–Q15 (spec 4.09) |
| 13:59 | `6e28aea` | W5 and character editor follow-up questions as dashboard questions: Phase 4 Q16–Q21 (W5), Q22 (unique names where), Q23 (body-shape band width) (spec 4.10) |
| 13:59 | `55374d0` | W5 stages: question references Q16–Q21 |
| 14:02 | `f2beddc` | Strava recording with S and ride photos from a virtual photographer planned (asked by the user; spec §2.8.1) |
| 14:06 | `952fc84` | Rider names reserved per account worldwide and unique on every server (user decision 4N Q22) |
| 14:08 | `893e1a0` | Rider status signs cannot be hidden: always visible to everybody (user decision §2.6 Q3) |
| 14:10 | `0f0fd58` | Strava recording: each S…S its own activity; photos local with a history folder link, only nice views, time in EXIF (user decisions §2.8.1 Q1–Q4) |
| 14:16 | `c879e2d` | Unicorn lands anywhere, wild mode on away from a road; free 2D off-road riding planned (asked by the user; Phase 13 13A, Q7–Q9 open) |
| 14:32 | `286ca95` | Remove the release/ folder (asked by the user): build notes live in the GitHub release notes; references updated (spec 4.16) |
| 14:38 | `9cc0364` | Voice: bundle LiveKit's livekit-server now, started by whoever hosts (user decision §7.1.7 Q1); voice questions renumbered §7.1.7 Q1–Q9 for the dashboard |
| 14:40 | `ca689b1` | Agents on the coordinator (deb) selectable in the build dashboard (asked by the user; spec 4.18, §11.2.1, dashboard 1.5.0) |
| 14:46 | `63bd86f` | Voice: join muted with an X mouth, Who hears me defaults to No one, voices fade to silence and are sent only to riders who can hear, macOS server from source, browser signalling bridge, UPnP while hosting (user decisions §7.1.7 Q2–Q8; follow-ups Q10, Q11) |
| 14:49 | `91d9d6b` | Voice signs split: X mouth = microphone muted, headphones = cannot hear you (per viewer); full volume to 10 m, fading to zero (user decisions §7.1.7 Q10, Q11; changes §2.6 Q1) |
| 15:03 | `3012fa8` (merge) | Merge main into the dashboard agent limit (spec row renumbered to 4.20) |
| 15:04 | `e9d9288` (merge) | Merge the agent limit for the coordinator: selectable in the build dashboard (default 5, 1–16), agents N of M, scripts/agent-slots.sh (spec 4.20, dashboard 1.5.0) |
| 15:24 | `06b3770` | Calendar on World -> Time: month grid banded with the place's season, moon, sun times, date and season shortcuts; choosing a season jumps the date (spec §14 Phase 9 S9, Q11/Q12) |
| 15:25 | `3db7694` | World patches as the World document: patch WorldOps with exact inverses, one road operation per target, height point commands, validators reusing the patch checks (spec §14 Phase 16 E5 step 2, 16C) |
| 15:25 | `f266595` | Studio: edit a world through its patch – click a road or height point in the 3D view or on the map, road and point panels, operations list with preview status, overlays, Save / Open patch, Build package (spec §14 Phase 16 E5 step 2) |
| 15:25 | `edde793` | World editing in OCW Studio through world patches built (spec 4.15, §14 Phase 16 16C Built (E5 step 2), 16F, new 16H Q7); README: the studio workflow |
| 15:27 | `dc3292c` (merge) | Merge main into the studio World workspace (spec row renumbered to 4.21; its questions as §16H Q16–Q18) |
| 16:10 | `6f6ca5e` (merge) | Merge the studio World workspace: editing a world through world patches – road attributes, removal, height points, save / open .ocwpatch, preview overlays, Build package (spec 4.21, Phase 16 E5 step 2) |
| 16:27 | `99fa2c8` | Model files: format, folder, loader and the export of today's models (Phase 15 M1, WIP) |
| 17:17 | `6199797` | Studio Routes workspace and BRouter: route document with undo / redo, built-in planner, GPX / TCX / GeoJSON / FIT import with map matching and problem sections, exports, elevation profile, Test ride (spec 4.22, §14 Phase 16 E1 rest and E2, 16D Built) |
| 17:27 | `87bb31d` | Strava recording with S built (spec §2.8.1 ST1–ST3); the ride photographer as its own feature: a person or a drone takes up to 5 photos of the nicest views per ride, with a flash (new §2.11, v4.21) |
| 17:28 | `898dd6b` (merge) | Merge main into Strava recording and the ride photographer (spec row renumbered to 4.22) |
| 17:29 | `4204c3f` | Touch steering built in both apps: tap or hold the left / right side to steer, two fingers move the camera, a tap on a junction fan arrow chooses that exit (spec §3.2.3, v4.12) |
| 17:30 | `045aba7` | Render distance: slider 1-60 km or unlimited with a dynamic mode on by default (spec §14 Phase 10, 10G) |
| 17:39 | `e9a50d4` (merge) | Merge Strava recording with S (its own activity per S…S, ST1–ST3) and the ride photographer as its own feature: view score, standing photographer or drone, flash and sound, off-screen photos with EXIF (spec 4.22, §2.8.1, §2.11) |
| 17:39 | `bea6411` | Model files built: format, folder, loader and the export of today's models (Phase 15 M1) |
| 17:40 | `147c9a7` (merge) | Merge main into touch steering (spec row renumbered to 4.23; photographer and touch hint plugins both added) |
| 17:48 | `6dd3a96` | Smooth junctions J1 (spec §4.8.8): junction surfaces from the road graph on the current packages |
| 17:58 | `6f84289` | Render distance: a failed probe goes back to the last good distance; no cutting when the distance is not what limits the frame rate (spec §14 Phase 10, 10G) |
| 17:58 | `865c471` (merge) | Merge main into the render distance branch |
| 17:59 | `7faf5a3` | Voice server bundled, V1: ocw-server --listen starts livekit-server itself (spec 4.22, §7.1.8 Built (V1)) |
| 18:00 | `42b01d6` (merge) | Merge touch steering in both apps: tap or hold the halves, taps topped up to one step, lean like the keys, fan taps for exits, two fingers move the camera, hints and settings (spec 4.23, §3.2.3) |
| 18:01 | `5b3ce3f` (merge) | Merge main into model files (spec row renumbered to 4.24) |
| 18:10 | `cd83910` | Render distance: cargo fmt |
| 18:13 | `f7a2888` | Junction seams analysis: tile build time, patched-only shares and fallback reasons (spec §4.8.8 J1) |
| 18:15 | `54ea70b` (merge) | Merge model files (Phase 15 M1): artwork/3dmodels in Git LFS, the model contract and checks, glTF reader / writer, ModelLibrary loader, 120 exported models (bikes with sizing, rider, helmets, 32 plant species × 3–5 variants) (spec 4.24) |
| 18:16 | `0de4a72` (merge) | Merge main into Voice V1 (spec row renumbered to 4.25) |
| 18:44 | `14e5a9e` (merge) | Merge Voice V1: ocw-server --listen starts the bundled livekit-server (fresh keys in the environment only, ready check, restart, no orphans), per-connection voice URLs, fetch-livekit-server.sh, make test-voice-bundled (spec 4.25, §7.1.8) |
| 18:44 | `923d2f3` | Studio routes: the map fits an opened route, a lighter route line, rounded distances; clippy fixes (spec 4.22, §14 Phase 16 16D) |
| 18:45 | `679bf52` (merge) | Merge main into the studio Routes workspace (spec row renumbered to 4.26; ocw-world gets plan next to photo / photo_drone) |
| 18:52 | `6f4d123` | Voice: the desktop client sees and hears the other riders on livekit-server 1.13.10 - the lost participant was the tests' event wait (spec 4.26, §7.1.8 Fixed) |
| 18:54 | `a7686ff` | Junction strips: skip pieces far from a junction, one cumulative per edge (tile build time); clippy (spec §4.8.8 J1) |
| 18:55 | `2e1d1c1` (merge) | Merge remote-tracking branch 'origin/main' into worktree-agent-a4077d5f86b70b3ed |
| 18:55 | `28866e7` | Win11Builder is used normally, like the other build machines: merge checks and the critical path included; only OCW_REMOTE_JOBS=2 stays (asked by the user; replaces the limits of spec 4.00; spec 4.26) |
| 18:57 | `a20de41` | Render distance built: slider and dynamic mode on by default, the display's refresh / 60 fps in the browser as the target (spec 4.23, §14 Phase 10, 10G Built) |
| 19:02 | `8668e33` (merge) | Merge the studio's Routes workspace and BRouter: built-in planner with profiles, BRouter client, route document with undo, GPX / TCX / GeoJSON import with matching, GPX / TCX / FIT / GeoJSON export, Test ride (spec 4.27, Phase 16 E1 rest, E2) |
| 19:22 | `9027449` | Calendar scene: menu steps spaced for slow debug frames (spec §14 Phase 9 S9) |
| 19:24 | `fe1b4b8` (merge) | Merge main into the calendar (spec row renumbered to 4.28) |
| 19:24 | `e4aae4c` | Calendar: spec references to v4.28 |
| 19:28 | `4861db2` | Smooth junctions, stage J1 built: junction surfaces from the road graph on the current packages (spec 4.26, §4.8.8) |
| 19:45 | `bbd87b2` | CLAUDE.md: model files are in Git LFS – agent worktrees run git lfs pull before their first remote build; start OCW agents from this checkout |
| 19:52 | `e689598` | Voice server with Host a ride, V2: the in-app host starts the bundled livekit-server through the shared launcher, lists the ports and opens them on the router by UPnP (spec 4.28, §7.1.6 V2, §7.1.9) |
| 19:56 | `75f205c` | The bib shorts no longer show through the jersey; the jersey has three back pockets (spec 4.28) |
| 20:09 | `a27a959` | Host a ride V2: Windows test imports, the integration test finds its own voice server by port (spec 4.28, §7.1.9) |
| 20:11 | `1d51167` | Jersey hem close to the bib instead of flared: no tail flapping in the crouch (spec 4.28) |
| 20:19 | `50c9b32` (merge) | Merge the calendar and season jumps (Phase 9 S9, spec 4.28) |
| 20:19 | `fa07399` (merge) | Merge smooth junctions J1: junction patches in the renderer on the current packages, ridden heights from the drawn surface (spec 4.29, §4.8.8) |
| 20:20 | `8dd32fb` (merge) | Merge the voice test fix: the tests' wait helper kept only the first event; both riders now see and hear each other in the tests (spec 4.30, §7.1.8) |
| 20:20 | `56c90fa` (merge) | Merge Voice V2: Host a ride starts the bundled voice server through the shared hosting code, ports page, UPnP port mapping (spec 4.31, §7.1.9) |
| 20:21 | `2a8a9da` | The bib's top inside the jersey is a lid on the torso: no look into the hollow torso (spec 4.28) |
| 20:48 | `a9dad68` | Other riders see the ride photographer, the drone and the flash (decision from the build dashboard; spec 4.32, §2.8.1 Q5, §2.11 Q2) |
| 21:01 | `f54256c` | Render distance: a shorter page note (the page fits a 16:9 window) |
| 21:10 | `66f55ba` | Rider status signs: X mouth for a muted microphone, headphones for "cannot hear you" (per viewer), the phone from the back pocket in the menu, the VR headset (spec 4.25, §2.6) |
| 21:24 | `f0dc26a` (merge) | Merge the bib / jersey fix and the jersey's back pockets (spec 4.33, §2.6) |
| 22:15 | `aa64367` (merge) | Merge rider status signs: X mouth when muted, headphones when a rider cannot hear you, phone from the back pocket in the menu, VR headset (spec 4.34, §2.6); new open questions §7.1.7 Q16, Q17 |
| 22:16 | `721a2ba` | Spec §7.1.7 Q16, Q17: question format the dashboard reads |
| 22:43 | `b7ec978` | Distant terrain fades into the sky at short render distances and on Low: the fog takes the atmosphere's measured horizon colour where the view is limited, far tiles beyond 2 × the distance are hidden (spec §14 Phase 10, 10G) |
| 22:58 | `8d88663` | setup-windows-buildserver.ps1: create the build user's profile with the Windows folder as working directory |
| 23:11 | `9f6fcdb` | setup-windows-buildserver.ps1 installs the build tools: Git with Git LFS and the VS Build Tools (C++) via winget, rustup as the build user; -VR checks the OpenXR runtime, -SkipTools leaves the tools out |
| 23:16 | `f048fb2` | Voice on the kiosk and a live test with the desktop app as a rider (spec 4.36, §7.1.8) |
| 23:20 | `6a02699` | Build machines: leela takes no new jobs; Weela is the Windows VR machine (Meta Quest on USB); the Windows setup script's new steps documented (spec 4.35, §11.2) |
| 23:26 | `5156fdf` (merge) | Merge remote-tracking branch 'origin/main' into merge/status-signs |
| 23:48 | `fb54ca7` | Other riders see the ride photographer: the shot goes through the server, every client draws the same person, drone flight and flash at the same game time (spec §2.11 Q2 = §2.8.1 Q5, v4.33) |
| 23:57 | `455b61a` | Distant terrain fades into the sky towards a low sun too: a warm directional glow in the fog, less fog colour where the atmosphere's haze adds more, far tiles hidden only where they rise above the eye (no holes from a summit) (spec §14 Phase 10, 10G) |
| 23:58 | `d945c23` (merge) | Merge render distance: slider and dynamic mode, distant terrain fades into the sky at short distances (spec 4.37, Phase 10 10G) |
| 23:58 | `de654e7` (merge) | Merge the shared ride photographer: other riders see the photographer, the drone and the flash, the shot relayed through the server (spec 4.38, §2.11, §2.8.1 Q5) |
| 23:59 | `088d46d` | Merge fix: rustfmt the desktop menu's page list |

## Builds and build servers

352 build/test runs on the build machines, 61.4 h in total, 19 failed; 1433 server samples; cargo compiled 21700 crates in 9.4 h, 21.2 h waiting for build slots.

| Machine | Runs | Hours | Cargo h | Crates | Waited h | Failed | Online |
|---|---|---|---|---|---|---|---|
| Weela | 0 | 0.0 | 0.0 | 0 | 0.0 | 0 | 96% |
| Win11Builder | 13 | 1.7 | 1.2 | 2788 | 0.0 | 0 | 100% |
| leela | 20 | 10.2 | 0.0 | 23 | 5.9 | 1 | 41% |
| macos | 64 | 3.7 | 0.8 | 1771 | 0.8 | 1 | 100% |
| marge | 255 | 45.9 | 7.4 | 17118 | 14.5 | 17 | 98% |

Failed runs:

- 07:12 marge: `set -e; export CC=clang-21 CXX=clang++-21; make check; cargo clippy --workspace ` (exit 2, log `build-log/071239-marge-1103443.log`)
- 07:15 marge: `set -e; export CC=clang-21 CXX=clang++-21; make check; cargo clippy --workspace ` (exit 2, log `build-log/071557-marge-1106563.log`)
- 07:15 macos: `set -e; cargo clippy -p ocw-xr -p ocw-render -p ocw-desktop --all-targets -- -D ` (exit 101, log `build-log/071557-macos-1106601.log`)
- 07:36 marge: `export CC=clang-21 CXX=clang++-21; make test-vr-monado` (exit 2, log `build-log/073614-marge-1134449.log`)
- 07:41 marge: `set -e; export CC=clang-21 CXX=clang++-21; cargo fmt --all -- --check; cargo cli` (exit 1, log `build-log/074155-marge-1139911.log`)
- 07:42 marge: `set -e; export CC=clang-21 CXX=clang++-21; cargo fmt --all -- --check; cargo cli` (exit 2, log `build-log/074214-marge-1140278.log`)
- 09:23 marge: `set -e; export CC=clang-21 CXX=clang++-21; make check; echo ALL-CHECKS-OK` (exit 2, log `build-log/092343-marge-1257076.log`)
- 09:44 marge: `   set -e   D=/var/tmp/ocw   put() { install -m $1 "$2" "$D/.$3.new" && mv -f "$` (exit 101, log `build-log/094422-marge-1277571.log`)
- 09:50 marge: `   set -e   D=/var/tmp/ocw   put() { install -m $1 "$2" "$D/.$3.new" && mv -f "$` (exit 101, log `build-log/095008-marge-1282623.log`)
- 08:39 marge: `set -e; export CC=clang-21 CXX=clang++-21; cargo fmt --all -- --check; cargo cli` (exit 255, log `build-log/083951-marge-1212316.log`)
- 10:07 marge: `set -e; export CC=clang-21 CXX=clang++-21; cargo fmt --all -- --check; cargo cli` (exit 1, log `build-log/100706-marge-1302993.log`)
- 10:07 marge: `set -e; export CC=clang-21 CXX=clang++-21; cargo fmt --all -- --check; cargo cli` (exit 101, log `build-log/100724-marge-1303373.log`)
- 10:07 marge: `set -e; export CC=clang-21 CXX=clang++-21; cargo fmt --all -- --check; cargo cli` (exit 101, log `build-log/100745-marge-1303802.log`)
- 13:04 marge: `set -e; make check; OCW_PACKAGE=ocw-studio .claude/skills/run-ocw/drive.sh shot-` (exit 2, log `build-log/130452-marge-1477880.log`)
- 14:05 marge: `set -e; export CC=clang-21 CXX=clang++-21; make check; cargo clippy --workspace ` (exit 124, log `build-log/140535-marge-1536934.log`)
- 14:26 leela: `cargo fmt --all -- --check` (exit 1, log `build-log/142659-leela-1560994.log`)
- 14:36 marge: `set -x; cargo test -p ocw-voice 2>&1 | grep -E "^test result|FAILED|panicked|Run` (exit 143, log `build-log/143632-marge-1582479.log`)
- 22:29 marge: `make test-voice-live 2>&1 | tail -25; echo ==== KIOSK; make test-kiosk 2>&1 | ta` (exit 1, log `build-log/222950-marge-2269277.log`)
- 23:59 marge: `set -e; export CC=clang-21 CXX=clang++-21; make check; cargo clippy --workspace ` (exit 2, log `build-log/235911-marge-2411191.log`)

Longest runs:

- 190 min on leela: `scripts/render-scenes.sh --out test-output/scenes/2026-11-16-152434 --only menu-`
- 124 min on leela: `cargo clippy --workspace --all-targets -- -D warnings 2>&1 | grep -E -A8 "^(erro`
- 86 min on marge: `set -e; export CC=clang-21 CXX=clang++-21; cargo fmt --all -- --check; cargo cli`
- 69 min on marge: `set -e; export CC=clang-21 CXX=clang++-21; make check; make test-smoke; make tes`
- 68 min on marge: `set -o pipefail; cargo fmt --all -- --check && echo FMT-OK; cargo clippy --works`

## Token usage

1.74 B tokens in 5,109 model messages (output 3.9 M, cache reads 1.70 B, cache writes 40.7 M, uncached input 11 k). Full breakdown: [tokens.json](tokens.json).

| Feature | Tokens | Output | Messages |
|---|---|---|---|
| Other | 901.8 M | 1.6 M | 2,312 |
| Riders & bikes | 261.0 M | 558 k | 798 |
| Audio & voice | 170.5 M | 464 k | 761 |
| Worlds & terrain | 108.9 M | 534 k | 390 |
| Build, release & infra | 85.5 M | 68 k | 116 |
| Planning & spec | 75.6 M | 297 k | 320 |
| Sky, time & weather | 62.7 M | 179 k | 200 |
| UI & menus | 55.6 M | 114 k | 171 |
| Multiplayer & server | 13.0 M | 23 k | 30 |
| Art project | 5.6 M | 6 k | 8 |
| Materials & look | 2.7 M | 2 k | 3 |

| Task | Feature | Tokens | Output |
|---|---|---|---|
| agent: Strava S-recording and photographer | Other | 207.6 M | 302 k |
| agent: Render distance slider and dynamic mode | Other | 171.5 M | 313 k |
| agent: Smooth junctions J1 in the renderer | Other | 146.4 M | 305 k |
| agent: Fix bib shorts showing through jersey | Other | 86.9 M | 194 k |
| agent: Phase 15 M1: model files | Riders & bikes | 74.0 M | 176 k |
| agent: Shared ride photographer for all riders | Riders & bikes | 63.0 M | 173 k |
| agent: Phase 9 S9: calendar and seasons | Sky, time & weather | 62.7 M | 179 k |
| coordination: question: could we speedup builds by putting the 3d engine part into a library w… | Build, release & infra | 60.8 M | 38 k |
| agent: Rider status signs (§2.6) | Riders & bikes | 56.6 M | 136 k |
| agent: Voice V2: Host a ride with voice, UPnP | Audio & voice | 55.9 M | 135 k |
| agent: Studio Routes workspace and BRouter | Worlds & terrain | 50.5 M | 226 k |
| coordination: W5 redfinment (planning, no building yet): include in ocw-server. build the host… | Riders & bikes | 47.2 M | 42 k |
| agent: Touch steering (§3.2.3) | Other | 46.0 M | 125 k |
| coordination: give the jersey back pockets. check images to see how that looks. | Other | 45.7 M | 28 k |
| agent: Character editor refined (Phase 4, 4N) | Planning & spec | 40.1 M | 164 k |
| agent: Studio shell and ocw-edit core | Other | 38.9 M | 154 k |
| agent: Fix desktop voice: other riders unheard | Audio & voice | 38.2 M | 84 k |
| agent: Studio World workspace editing via patches | Worlds & terrain | 36.0 M | 183 k |
| coordination: create cooler 8 bit synti music for day 5 video. | Other | 35.6 M | 35 k |
| agent: Voice V1: bundled livekit-server launcher | Audio & voice | 33.7 M | 128 k |
| agent: Live voice status and proposal | Audio & voice | 19.2 M | 65 k |
| coordination: create the daily art video for yesterday. use definition in art spec file. | Planning & spec | 17.9 M | 33 k |
| coordination: When the user answers a question via build-dashboard, i only see a "Decided by U… | UI & menus | 17.6 M | 26 k |
| agent: World patch format in world-builder | Worlds & terrain | 16.7 M | 115 k |
| coordination: photographer: in every ride, unless disabled in settings. | Other | 13.8 M | 7 k |
| coordination: do not put new jobs on leela and try to start the queued job on marge | Other | 12.9 M | 25 k |
| coordination: whats causing memory spikes / swap on deb? | Other | 12.7 M | 14 k |
| coordination: stop using /tmp on deb. add to CLAUDE.md | Other | 11.4 M | 12 k |
| coordination: add a restart button into the build dashboard. also a watcher for the machines.t… | UI & menus | 10.7 M | 17 k |
| coordination: Q10: full volume up to 10 m, then fading to zero. Q11: headphones means: cant he… | Other | 10.4 M | 9 k |
| coordination: allow win11builder to be used normalmy (femove spec 4.00) | Build, release & infra | 9.8 M | 8 k |
| coordination: okay, headset connected and meta link installed | Other | 8.3 M | 13 k |
| coordination: investigate first, where those names came from. local test data? | Other | 8.1 M | 11 k |
| coordination: voice check if there is an open question for 16 E5 - i see none. | Audio & voice | 8.0 M | 10 k |
| coordination: planning: when running on a touch capable device (e.g. IOS/Androidm but not limi… | Planning & spec | 8.0 M | 16 k |
| coordination: continue with step 6.5 | Other | 7.7 M | 19 k |
| coordination: what is the status about the model export/ import feature? Add to the plannung t… | Riders & bikes | 7.5 M | 12 k |
| coordination: create a suitable favicon for the build dashboard | UI & menus | 7.4 M | 10 k |
| coordination: bug: i noticed a difference between the resistance felt on the wahoo trainer to … | Other | 7.4 M | 15 k |
| coordination: Ready to build: yes, start with them in suggested order | Build, release & infra | 7.2 M | 11 k |

## Prompts

63 prompts (full text: [prompts.md](prompts.md)).

| Time | Prompt |
|---|---|
| 07:06 | yes delete them, then continue with step 6.4 |
| 07:09 | where are you running? |
| 07:09 | continue with step 6.5 |
| 07:23 | create the daily art video for yesterday. use definition in art spec file. |
| 07:29 | does OSM data contain information about kerbs? |
| 07:38 | Why do we release the *-osm-source.zip files? |
| 07:39 | investigate first, where those names came from. local test data? |
| 07:45 | I didn't see <name> named in the video. So use that video and leave out the images where that name is visible. Use only imaginary names in t |
| 07:46 | When the user answers a question via build-dashboard, i only see a "Decided by User" comment in the video (and git?) i assume. Fix that by u |
| 07:51 | spec add on character: when a user uses VR goggles, show him as wearing goggles, too. |
| 09:09 | bug: i noticed a difference between the resistance felt on the wahoo trainer to the inclination of the road. while the road was constantly a |
| 09:10 | create cooler 8 bit synti music for day 5 video. |
| 09:18 | planning: refine character editor in workshop. the user can give himself a name, chose his sex, age, haircut, hair color, mustache, body sha |
| 09:20 | planning: when running on a touch capable device (e.g. IOS/Androidm but not limited to that, check browser capabilities) we need a way to co |
| 09:26 | create a suitable favicon for the build dashboard |
| 09:33 | add a restart button into the build dashboard. also a watcher for the machines.toml config file so that changes are picked up automatically. |
| 09:42 | whats causing memory spikes / swap on deb? |
| 10:00 | yes, cleanup tmp, which are user files? whats the command to restart build dashboard? |
| 10:05 | stop using /tmp on deb. add to CLAUDE.md |
| 10:13 | start versioning the build dashboard. i do not see the favicon or the changes regarding the restart button. did you systemctl scripts change |
| 12:01 | dashboard: remove this "Not ready for the cutover: 0 running task(s), 1 remote run(s)". leave the worktree expanded, also after an update of |
| 12:01 | what are the next development steps? |
| 12:04 | is the charakter customze tool in the workshop done? and what about the world editor? |
| 12:07 | okay, start with the world edior. |
| 12:11 | Character editor Q6–Q15: how many base bodies, and how to label them; -> anorexia, skinny, slim, normal, ample, fat, obese  whether names mu |
| 12:14 | what do you need to know for W5 |
| 12:15 | Q6b: yes, keep the shoulder/hip/chest variants in as a second dimsion. |
| 12:24 | W5 redfinment (planning, no building yet): include in ocw-server. build the hosting parts, do the hosting manually later. Accounts are handl |
| 12:26 | what is the status about the model export/ import feature? Add to the plannung the export of the current models used into (named according t |
| 12:38 | use all build servers now |
| 12:43 | planning voice feature: i want all required binaries and libraries to be part of ocw-desktop (or the browser version) or if that's not possi |
| 13:57 | voice check if there is an open question for 16 E5 - i see none. |
| 14:00 | Strava planning: use hotkey S to start and stop strava recording. take a photo of the rider in the landscape showing nice views, choose came |
| 14:02 | what are next development items? |
| 14:04 | Ready to build: yes, start with them in suggested order |
| 14:06 | * Character editor (4N),      * Q22 (unique names per account or per server): unique per account and serverQ23 (band width) remain, and the  |
| 14:08 | Rider status signs (§2.6): headphones, phone and VR headset. Only Q3 is open: can a rider hide their own signs? -> no, always visible to eve |
| 14:09 | strava Q1 – Several recordings in one ride: each S … S becomes its own Strava activity  Q2 – How the photos reach Strava (the public API can |
| 14:15 | make it for the unicorn possible to convert into a rider everywhere, turn on wild mode when landing way from road. |
| 14:16 | if any of the features in the deb/build pipeline are independent from one another, start building in parallel on the other build servers, to |
| 14:18 | whenever there is a photo taken for strava, make an real photographer person appear in the game, looking the exact angle as he would in real |
| 14:25 | photographer add-on, if it's in a position where a human can not stand, e.g. above ground, over water, rocky terrain etc. make the photograp |
| 14:27 | make the amount of agents runable on the controller (deb) selectable in the build dashboard. |
| 14:29 | record also compile time for the art project |
| 14:30 | remove the OCW/release folder |
| 14:35 | bg task: status and proposal for live voice? |
| 14:35 | dont make the photographer part of strava, keep it as separate entitiy. |
| 14:35 | whats your proposal about the voice feature? |
| 14:38 | Q-V1 (a) bundle now |
| 14:45 | Q-V2: yes Q-V3: yes Q-V4: yes Q-V5: yes, Q-V6: spatial, but riders get quieter the further away until the are not audible at all. server: sa |
| 14:48 | Q10: full volume up to 10 m, then fading to zero. Q11: headphones means: cant hear you. the X means microphone muted. |
| 15:11 | photographer: in every ride, unless disabled in settings. |
| 15:28 | question: could we speedup builds by putting the 3d engine part into a library which we don't have to compile each and every time? |
| 18:55 | allow win11builder to be used normalmy (femove spec 4.00) |
| 19:05 | there is a graphic bug where the bib (bike trouser) is visible through the jersey. fix that. |
| 19:07 | give the jersey back pockets. check images to see how that looks. |
| 20:41 | do not put new jobs on leela and try to start the queued job on marge |
| 22:26 | yes |
| 22:57 | i tried the setup buildserver script for windows. It failes with the following error: PS ~\Downloads> .\setup-windows-buildserver.ps1 -Publi |
| 23:06 | i added a windows machine (weela) that will have the oculus attached via USB |
| 23:10 | add those required steps as admin to the buildserver setup script. |
| 23:19 | document the updates |
| 23:42 | okay, headset connected and meta link installed |

## Features

64 spec versions added, 19 landed by a merge; 6 deploys, 0 releases.

| Spec | Feature | Landed | Check (marge) |
|---|---|---|---|
| 3.75 | Junction markings per world from real images | 07:49 `9cccd08` | – |
| 3.76 | Riders in VR wear a VR headset on their avatar | 07:53 `b6bb074` | – |
| 3.77 | Character editor refined | 09:25 `e650761` | – |
| 3.78 | Touch steering planned | 09:26 `aa24c31` | – |
| 3.79 | At a junction the main road keeps its own surface | 09:28 `9c37793` | – |
| 3.80 | Junction corners per world from real images | 09:30 `3de28fa` | – |
| 3.81 | The art project's history leaves OCW | 09:31 `93a79ec` | – |
| 3.82 | Trainer | 09:44 `80b0d53` | – |
| 3.83 | Touch steering | 10:17 `a1f2b7c` | – |
| 3.84 | Touch lean steering works like the keys | 10:19 `8e8e649` | – |
| 3.85 | A touch does not switch autodrive off | 10:19 `1800084` | – |
| 3.86 | Character editor | 12:11 `06f1fb7` | – |
| 3.87 | Character editor | 12:15 `e5c7188` | – |
| 3.88 | W5 refined | 12:26 `c52b946` | – |
| 3.89 | Touch steering in the desktop app too, on Windows / Linux touch screens | 12:27 `0033521` | – |
| 3.90 | In a ride one finger steers and a two-finger drag moves the camera | 12:27 `389fe4c` | – |
| 3.91 | Model files | 12:28 `0dbbe55` | – |
| 3.92 | The visible body shape is bounded to a band around what weight and height give, with a *M… | 12:29 `f28da5e` | – |
| 3.93 | The character editor's extras come later, not in its first step | 12:29 `9c4b862` | – |
| 3.94 | Models | 12:31 `9143410` | – |
| 3.95 | Trees | 12:32 `dec712d` | – |
| 3.96 | The Blender add-on for model export is postponed | 12:32 `db15f86` | – |
| 3.97 | After the export the model files are the only source | 12:33 `c6c3656` | – |
| 3.98 | Signed in, riders are shown by their own rider name stored with the account | 12:34 `c8928d1` | – |
| 3.99 | All world packages are rebuilt and deployed once the junction profile work is checked | 12:34 `f9d9c99` | – |
| 4.00 | All four build machines build | 12:39 `d0ad08a` | – |
| 4.01 | Voice built in and always on | 12:49 `fbb94a1` | – |
| 4.02 | World patches | 13:04 `eb8b895` (merge) | ok at 12:50, 64 suites, 2307 passed, 0 failed (commit) |
| 4.03 | OCW Studio shell built | 13:47 `08486ed` (merge) | ok at 15:14, 1 suites, 38 passed, 0 failed (commit) |
| 4.04 | Touching both sides of the screen at once does nothing, like holding ← and → together | 13:49 `db37bfb` | – |
| 4.05 | On touch the screen halves always steer | 13:50 `a8294c4` | – |
| 4.06 | Touch steering zones cover the full screen height below the top band, with *lower half on… | 13:50 `e37d94f` | – |
| 4.07 | Headphones show on a rider only while their microphone is muted in a voice room, not when… | 13:52 `f2a2785` | – |
| 4.08 | A rider takes out the phone while in the in-game menu, the console or the workout and wor… | 13:54 `fa30a67` | – |
| 4.09 | The world editor's open questions are in the dashboard | 13:58 `205eda9` | – |
| 4.10 | W5's and the character editor's follow-up questions are in the dashboard | 13:59 `6e28aea` | – |
| 4.11 | Strava recording with the S key and ride photos from a virtual photographer planned | 14:02 `f2beddc` | – |
| 4.12 | Rider names are reserved per account worldwide and unique on every server | 14:06 `952fc84` | – |
| 4.13 | Rider status signs cannot be hidden | 14:08 `893e1a0` | – |
| 4.14 | Strava recording | 14:10 `0f0fd58` | – |
| 4.15 | The unicorn turns back into the rider anywhere | 14:16 `c879e2d` | – |
| 4.16 | The folder release/ is removed | 14:32 `286ca95` | – |
| 4.17 | Voice | 14:38 `9cc0364` | – |
| 4.18 | Voice | 14:46 `63bd86f` | – |
| 4.19 | Voice status signs split | 14:49 `91d9d6b` | – |
| 4.20 | Agents on the coordinator selectable in the build dashboard | 15:04 `e9d9288` (merge) | – |
| 4.21 | World editing in OCW Studio through world patches | 16:10 `6f6ca5e` (merge) | ok at 17:42 (commit) |
| 4.22 | Strava recording with S built and the ride photographer as its own feature | 17:39 `e9a50d4` (merge) | ok at 17:28, 67 suites, 2408 passed, 0 failed (commit) |
| 4.23 | Touch steering built in both apps | 18:00 `42b01d6` (merge) | ok at 17:40, 67 suites, 2435 passed, 0 failed (commit) |
| 4.24 | Model files | 18:15 `54ea70b` (merge) | ok at 21:09, 1 suites, 119 passed, 0 failed (commit) |
| 4.25 | Voice server bundled, V1 | 18:44 `14e5a9e` (merge) | ok at 18:16, 68 suites, 2470 passed, 0 failed (commit) |
| 4.26 | Win11Builder is used normally, like the other build machines | 18:55 `28866e7` | – |
| 4.27 | The studio's Routes workspace and the first external planner built | 19:02 `8668e33` (merge) | ok at 19:47, 1 suites, 10 passed, 0 failed (commit) |
| 4.28 | Calendar on World → Time | 20:19 `50c9b32` (merge) | ok at 15:24 (branch) |
| 4.29 | Smooth junctions, stage J1 built | 20:19 `fa07399` (merge) | ok at 19:14, 1 suites, 1 passed, 0 failed (branch) |
| 4.30 | Voice | 20:20 `8dd32fb` (merge) | ok at 19:35 (commit) |
| 4.31 | Voice server with Host a ride, V2 | 20:20 `56c90fa` (merge) | ok at 20:21, 71 suites, 2583 passed, 0 failed (commit) |
| 4.32 | Other riders see the ride photographer, the drone and the flash | 20:48 `a9dad68` | – |
| 4.33 | The bib shorts no longer show through the jersey, and the jersey has three back pockets | 21:24 `f0dc26a` (merge) | ok at 23:16, 3 suites, 3 passed, 0 failed (commit) |
| 4.34 | Rider status signs built in both apps | 22:15 `aa64367` (merge) | ok at 21:24, 5 suites, 396 passed, 0 failed (commit) |
| 4.35 | Build machines | 23:26 `5156fdf` (merge) | ok at 23:41, 3 suites, 303 passed, 2 failed (commit) |
| 4.36 | Voice on the kiosk, and a live test with the desktop app as a rider | 23:26 `5156fdf` (merge) | ok at 23:41, 3 suites, 303 passed, 2 failed (commit) |
| 4.37 | Render distance built | 23:58 `d945c23` (merge) | ok at 23:25, 2 suites, 8 passed, 0 failed (branch) |
| 4.38 | Other riders see the ride photographer | 23:58 `de654e7` (merge) | exit 2 at 23:59 (commit) |

Deploys:

- 07:06 marge: `c27c2a1` (ok)
- 09:44 marge: `80b0d53` (exit 101)
- 09:50 marge: `80b0d53` (exit 101)
- 09:52 marge: `80b0d53` (ok)
- 21:24 marge: `a9dad68` (ok)
- 23:24 marge: `f048fb2` (ok)

## Agent jobs

19 jobs (coordinator log agents.jsonl).

| Task | Branch | Start | End | Status | Interrupted | Merged |
|---|---|---|---|---|---|---|
| VR X1: merge of main, OpenXR loader, Monado fixes | vr-x1 | 23:55 | 15:04 | reported |  |  |
| World patches: .ocwpatch format and world-builder (Phase 16 E5 step 1) | a7fcbd87 | 12:08 | 13:04 | merged |  | `eb8b895` |
| OCW Studio shell: ocw-edit and ocw-studio (Phase 16 E1 core) | ace6db7c | 12:08 | 13:47 | merged |  | `08486ed` |
| Studio World workspace: editing through world patches (Phase 16 E5 step 2) | a81bcba0 | 13:48 | 16:10 | merged |  | `6f6ca5e` |
| Smooth junctions J1 in the renderer (§4.8.8) | a4077d5f | 14:06 | 21:22 | merged |  |  |
| Touch steering (§3.2.3) | a168816f | 14:06 | 18:00 | merged |  | `42b01d6` |
| Render distance slider and dynamic mode (Phase 10 10G) | a6eb7544 | 14:06 | 23:58 | reported |  |  |
| Model files (Phase 15 M1) | ab5c2453 | 14:17 | 18:15 | merged |  | `54ea70b` |
| Calendar and seasons (Phase 9 S9) | af90ba62 | 14:17 | 21:22 | merged |  |  |
| Strava recording with S, ride photographer (§2.8.1) | aaec8a31 | 14:17 | 17:39 | merged |  | `e9a50d4` |
| Agent limit for the coordinator in the build dashboard | a27713f6 | 14:32 | 15:04 | merged |  | `e9d9288` |
| Studio Routes workspace and BRouter (Phase 16 E1 rest, E2) | a1bfd2f9 | 16:11 | 19:02 | merged |  | `8668e33` |
| Voice V1: bundled livekit-server launcher (§7.1) | a51b5465 | 16:11 | 18:44 | merged |  | `14e5a9e` |
| Fix desktop voice: other riders unheard on livekit-server 1.13.10 (§7) | ae4dcf44 | 18:17 | 21:22 | merged |  |  |
| Rider status signs: X mouth, headphones, phone, VR headset (§2.6) | ab8082e5 | 18:17 | 23:26 | merged |  |  |
| Voice V2: Host a ride with voice, ports page, UPnP (§7.1) | a8437896 | 19:03 | 21:22 | merged |  |  |
| Bug: bib shorts visible through the jersey | a5a12b92 | 19:06 | 22:15 | merged |  |  |
| Ride photographer visible to other riders (§2.11, Q5) | a54266de | 20:48 | 23:50 | reported |  |  |
| Character editor refined (Phase 4, 4N) | ae162327 | 23:26 |  | started |  |  |

## Incidents

94 collected (janitor-delete 46, machine-offline 24, machine-online 23, runs-failed 1), 0 with root-cause notes ([incidents.md](incidents.md)).

| Time | Kind | Machine | What |
|---|---|---|---|
| 00:00 | machine-offline | leela | leela unreachable (timeout) |
| 08:19 | machine-offline | marge | marge unreachable (timeout) |
| 08:20 | machine-online | marge | marge back online |
| 08:23 | machine-offline | marge | marge unreachable (timeout) |
| 08:24 | machine-online | marge | marge back online |
| 08:28 | machine-offline | marge | marge unreachable (timeout) |
| 08:30 | machine-online | marge | marge back online |
| 08:40 | machine-offline | marge | marge unreachable (timeout) |
| 08:43 | machine-online | marge | marge back online |
| 08:52 | machine-offline | marge | marge unreachable (ssh error) |
| 08:53 | machine-online | marge | marge back online |
| 08:54 | machine-offline | marge | marge unreachable (ssh error) |
| 08:55 | machine-online | marge | marge back online |
| 09:43 | machine-offline | marge | marge unreachable (ssh error) |
| 09:44 | machine-online | marge | marge back online |
| 09:48 | machine-offline | marge | marge unreachable (timeout) |
| 09:49 | machine-online | marge | marge back online |
| 10:25 | machine-offline | marge | marge unreachable (no route to host) |
| 10:26 | machine-online | marge | marge back online |
| 10:30 | machine-offline | marge | marge unreachable (ssh error) |
| 10:31 | machine-online | marge | marge back online |
| 10:33 | machine-offline | marge | marge unreachable (ssh error) |
| 10:35 | machine-online | marge | marge back online |
| 10:38 | machine-offline | marge | marge unreachable (no route to host) |
| 10:39 | machine-online | marge | marge back online |
| 10:41 | machine-offline | marge | marge unreachable (ssh error) |
| 10:43 | machine-online | marge | marge back online |
| 11:00 | machine-offline | marge | marge unreachable (no route to host) |
| 11:01 | machine-online | marge | marge back online |
| 11:07 | machine-offline | marge | marge unreachable (ssh error) |
| 11:08 | machine-online | marge | marge back online |
| 11:11 | machine-offline | marge | marge unreachable (no route to host) |
| 11:12 | machine-online | marge | marge back online |
| 11:45 | machine-offline | marge | marge unreachable (timeout) |
| 11:46 | machine-online | marge | marge back online |
| 11:48 | machine-offline | marge | marge unreachable (no route to host) |
| 11:49 | machine-online | marge | marge back online |
| 11:52 | machine-offline | marge | marge unreachable (ssh error) |
| 11:54 | machine-online | marge | marge back online |
| 11:59 | machine-online | leela | leela back online |
| 12:11 | machine-offline | marge | marge unreachable (no route to host) |
| 12:13 | machine-online | marge | marge back online |
| 13:04 | janitor-delete | marge | janitor delete OCW-worktree-agent-a7fcbd8740a846616/target (22.2 GB) |
| 13:48 | janitor-delete | marge | janitor delete OCW-worktree-agent-ace6db7c90512ad26/target (32.7 GB) |
| 13:48 | janitor-delete | macos | janitor delete OCW-worktree-agent-ace6db7c90512ad26/target (0.1 GB) |
| 15:27 | janitor-delete | macos | janitor delete OCW-worktree-agent-a0eb3b759feb13978/target (0.8 GB) |
| 15:27 | janitor-delete | macos | janitor delete OCW-worktree-agent-a2e65303b0aed2f1c/target (0.8 GB) |
| 15:27 | janitor-delete | macos | janitor delete OCW-worktree-agent-a3b9cf0b40cbf0ccc/target (10.7 GB) |
| 15:27 | janitor-delete | macos | janitor delete OCW-worktree-agent-a7c12806972eb03b7/target (0.6 GB) |
| 15:27 | janitor-delete | macos | janitor delete OCW-worktree-agent-aa68e332f9744e170/target (0.7 GB) |
| 16:10 | janitor-delete | marge | janitor delete OCW-worktree-agent-a81bcba01b634ec7e/target (24.1 GB) |
| 16:26 | janitor-delete | macos | janitor delete OCW/target (2.7 GB) |
| 16:46 | janitor-delete | macos | janitor delete OCW/target (1.0 GB) |
| 17:39 | janitor-delete | marge | janitor delete OCW-worktree-agent-aaec8a3104b8ee776/target (27.9 GB) |
| 17:39 | janitor-delete | macos | janitor delete OCW-worktree-agent-aaec8a3104b8ee776/target (29.3 GB) |
| 18:01 | janitor-delete | leela | janitor delete OCW-worktree-agent-a168816fc82c593b6/target (14.0 GB) |
| 18:01 | janitor-delete | marge | janitor delete OCW-worktree-agent-a168816fc82c593b6/target (38.8 GB) |
| 18:01 | janitor-delete | macos | janitor delete OCW-worktree-agent-a168816fc82c593b6/target (0.4 GB) |
| 18:15 | janitor-delete | leela | janitor delete OCW-worktree-agent-ab5c245364ad2c44d/target (5.5 GB) |
| 18:15 | janitor-delete | marge | janitor delete OCW-worktree-agent-ab5c245364ad2c44d/target (40.7 GB) |

## Media

| Time | File |
|---|---|
| 13:18:00 | [131800-shot-wayland-studio-e1.jpg](131800-shot-wayland-studio-e1.jpg) |
| 14:29:28 | [142928-shot-wayland-junction-bergstrasse-rider.jpg](142928-shot-wayland-junction-bergstrasse-rider.jpg) |
| 14:29:40 | [142940-shot-wayland-junction-bergstrasse-drone.jpg](142940-shot-wayland-junction-bergstrasse-drone.jpg) |
| 14:29:51 | [142951-shot-wayland-junction-hagstrasse-rider.jpg](142951-shot-wayland-junction-hagstrasse-rider.jpg) |
| 14:30:02 | [143002-shot-wayland-junction-hagstrasse-drone.jpg](143002-shot-wayland-junction-hagstrasse-drone.jpg) |
| 14:30:14 | [143014-shot-wayland-junction-planknerstrasse-rider.jpg](143014-shot-wayland-junction-planknerstrasse-rider.jpg) |
| 14:30:25 | [143025-shot-wayland-junction-planknerstrasse-drone.jpg](143025-shot-wayland-junction-planknerstrasse-drone.jpg) |
| 14:30:36 | [143036-shot-wayland-junction-adlerkreisel-rider.jpg](143036-shot-wayland-junction-adlerkreisel-rider.jpg) |
| 14:30:47 | [143047-shot-wayland-junction-adlerkreisel-drone.jpg](143047-shot-wayland-junction-adlerkreisel-drone.jpg) |
| 14:30:58 | [143058-shot-wayland-junction-landstrasse-split-rider.jpg](143058-shot-wayland-junction-landstrasse-split-rider.jpg) |
| 14:31:10 | [143110-shot-wayland-junction-landstrasse-split-drone.jpg](143110-shot-wayland-junction-landstrasse-split-drone.jpg) |
| 14:31:21 | [143121-shot-wayland-junction-vorarlberger-rider.jpg](143121-shot-wayland-junction-vorarlberger-rider.jpg) |
| 14:31:32 | [143132-shot-wayland-junction-vorarlberger-drone.jpg](143132-shot-wayland-junction-vorarlberger-drone.jpg) |
| 14:31:43 | [143143-shot-wayland-junction-spoerryweg-rider.jpg](143143-shot-wayland-junction-spoerryweg-rider.jpg) |
| 14:31:55 | [143155-shot-wayland-junction-spoerryweg-drone.jpg](143155-shot-wayland-junction-spoerryweg-drone.jpg) |
| 14:34:40 | [143440-shot-junction-bergstrasse-rider.jpg](143440-shot-junction-bergstrasse-rider.jpg) |
| 14:35:40 | [143540-shot-junction-bergstrasse-drone.jpg](143540-shot-junction-bergstrasse-drone.jpg) |
| 14:36:52 | [143652-shot-junction-hagstrasse-rider.jpg](143652-shot-junction-hagstrasse-rider.jpg) |
| 14:37:56 | [143756-shot-junction-hagstrasse-drone.jpg](143756-shot-junction-hagstrasse-drone.jpg) |
| 14:39:12 | [143912-shot-junction-planknerstrasse-rider.jpg](143912-shot-junction-planknerstrasse-rider.jpg) |
| 14:40:04 | [144004-shot-junction-planknerstrasse-drone.jpg](144004-shot-junction-planknerstrasse-drone.jpg) |
| 14:41:08 | [144108-shot-junction-adlerkreisel-rider.jpg](144108-shot-junction-adlerkreisel-rider.jpg) |
| 14:42:09 | [144209-shot-junction-adlerkreisel-drone.jpg](144209-shot-junction-adlerkreisel-drone.jpg) |
| 14:43:11 | [144311-shot-junction-landstrasse-split-rider.jpg](144311-shot-junction-landstrasse-split-rider.jpg) |
| 14:44:05 | [144405-shot-junction-landstrasse-split-drone.jpg](144405-shot-junction-landstrasse-split-drone.jpg) |
| 14:45:24 | [144524-shot-junction-vorarlberger-rider.jpg](144524-shot-junction-vorarlberger-rider.jpg) |
| 14:46:20 | [144620-shot-junction-vorarlberger-drone.jpg](144620-shot-junction-vorarlberger-drone.jpg) |
| 14:47:20 | [144720-shot-junction-spoerryweg-rider.jpg](144720-shot-junction-spoerryweg-rider.jpg) |
| 14:48:15 | [144815-shot-junction-spoerryweg-drone.jpg](144815-shot-junction-spoerryweg-drone.jpg) |
| 15:10:40 | [151040-web-web-console.jpg](151040-web-web-console.jpg) |
| 15:10:40 | [151040-web-web-gamepad.jpg](151040-web-web-gamepad.jpg) |
| 15:10:40 | [151040-web-web-gps.jpg](151040-web-web-gps.jpg) |
| 15:10:40 | [151040-web-web-hud.jpg](151040-web-web-hud.jpg) |
| 15:10:40 | [151040-web-web-join.jpg](151040-web-web-join.jpg) |
| 15:10:40 | [151040-web-web-menu.jpg](151040-web-web-menu.jpg) |
| 15:10:40 | [151040-web-web-ride.jpg](151040-web-web-ride.jpg) |
| 15:10:40 | [151040-web-web-riders.jpg](151040-web-web-riders.jpg) |
| 15:10:40 | [151040-web-web-settings.jpg](151040-web-web-settings.jpg) |
| 15:10:40 | [151040-web-web-touch-hints.jpg](151040-web-web-touch-hints.jpg) |
| 15:10:40 | [151040-web-web-touch-hold.jpg](151040-web-web-touch-hold.jpg) |
| 15:10:40 | [151040-web-web-unicorn-flight.jpg](151040-web-web-unicorn-flight.jpg) |
| 15:10:40 | [151040-web-web-unicorn-inspect.jpg](151040-web-web-unicorn-inspect.jpg) |
| 15:10:40 | [151040-web-web-unicorn-menu.jpg](151040-web-web-unicorn-menu.jpg) |
| 15:10:40 | [151040-web-web-weather.jpg](151040-web-web-weather.jpg) |
| 15:10:40 | [151040-web-web.jpg](151040-web-web.jpg) |
| 15:24:32 | [152432-agent-studio-e5-shot-wayland-studio-e5-patch.jpg](152432-agent-studio-e5-shot-wayland-studio-e5-patch.jpg) |
| 15:37:51 | [153751-shot-ocw-touch-desktop.jpg](153751-shot-ocw-touch-desktop.jpg) |
| 16:26:10 | [162610-photographer-st-chase-chase-10-photographer.jpg](162610-photographer-st-chase-chase-10-photographer.jpg) |
| 16:26:13 | [162613-photographer-st-chase-chase-11-photographer.jpg](162613-photographer-st-chase-chase-11-photographer.jpg) |
| 16:26:16 | [162616-photographer-st-chase-chase-12-photographer.jpg](162616-photographer-st-chase-chase-12-photographer.jpg) |
| 16:30:30 | [163030-web-web-calendar.jpg](163030-web-web-calendar.jpg) |
| 16:42:16 | [164216-photographer-drone-chase-chase-01-photographer.jpg](164216-photographer-drone-chase-chase-01-photographer.jpg) |
| 16:42:19 | [164219-photographer-drone-chase-chase-02-photographer.jpg](164219-photographer-drone-chase-chase-02-photographer.jpg) |
| 16:43:50 | [164350-photographer-drone-chase-chase-03-photographer.jpg](164350-photographer-drone-chase-chase-03-photographer.jpg) |
| 16:43:53 | [164353-photographer-drone-chase-chase-04-drone.jpg](164353-photographer-drone-chase-chase-04-drone.jpg) |
| 16:43:54 | [164354-shot-wayland-junction-bergstrasse-rider.jpg](164354-shot-wayland-junction-bergstrasse-rider.jpg) |
| 16:43:56 | [164356-photographer-drone-chase-chase-05-drone.jpg](164356-photographer-drone-chase-chase-05-drone.jpg) |
| 16:43:59 | [164359-photographer-drone-chase-chase-06-drone.jpg](164359-photographer-drone-chase-chase-06-drone.jpg) |
| 16:44:02 | [164402-photographer-drone-chase-chase-07-drone.jpg](164402-photographer-drone-chase-chase-07-drone.jpg) |
| 16:44:05 | [164405-photographer-drone-chase-chase-08-photographer.jpg](164405-photographer-drone-chase-chase-08-photographer.jpg) |
| 16:44:05 | [164405-shot-wayland-junction-bergstrasse-drone.jpg](164405-shot-wayland-junction-bergstrasse-drone.jpg) |
| 16:44:08 | [164408-photographer-drone-chase-chase-09-photographer.jpg](164408-photographer-drone-chase-chase-09-photographer.jpg) |
| 16:44:11 | [164411-photographer-drone-chase-chase-10-photographer.jpg](164411-photographer-drone-chase-chase-10-photographer.jpg) |
| 16:44:14 | [164414-photographer-drone-chase-chase-11-photographer.jpg](164414-photographer-drone-chase-chase-11-photographer.jpg) |
| 16:44:16 | [164416-shot-wayland-junction-hagstrasse-rider.jpg](164416-shot-wayland-junction-hagstrasse-rider.jpg) |
| 16:44:17 | [164417-photographer-drone-chase-chase-12-photographer.jpg](164417-photographer-drone-chase-chase-12-photographer.jpg) |
| 16:44:20 | [164420-photographer-drone-chase-chase-13-photographer.jpg](164420-photographer-drone-chase-chase-13-photographer.jpg) |
| 16:44:23 | [164423-photographer-drone-chase-chase-14-photographer.jpg](164423-photographer-drone-chase-chase-14-photographer.jpg) |
| 16:44:26 | [164426-photographer-drone-chase-chase-15-photographer.jpg](164426-photographer-drone-chase-chase-15-photographer.jpg) |
| 16:44:27 | [164427-shot-wayland-junction-hagstrasse-drone.jpg](164427-shot-wayland-junction-hagstrasse-drone.jpg) |
| 16:44:29 | [164429-photographer-drone-chase-chase-16-photographer.jpg](164429-photographer-drone-chase-chase-16-photographer.jpg) |
| 16:44:38 | [164438-shot-wayland-junction-planknerstrasse-rider.jpg](164438-shot-wayland-junction-planknerstrasse-rider.jpg) |
| 16:44:49 | [164449-shot-wayland-junction-planknerstrasse-drone.jpg](164449-shot-wayland-junction-planknerstrasse-drone.jpg) |
| 16:45:00 | [164500-shot-wayland-junction-adlerkreisel-rider.jpg](164500-shot-wayland-junction-adlerkreisel-rider.jpg) |
| 16:45:11 | [164511-shot-wayland-junction-adlerkreisel-drone.jpg](164511-shot-wayland-junction-adlerkreisel-drone.jpg) |
| 16:45:22 | [164522-shot-wayland-junction-landstrasse-split-rider.jpg](164522-shot-wayland-junction-landstrasse-split-rider.jpg) |
| 16:45:33 | [164533-shot-wayland-junction-landstrasse-split-drone.jpg](164533-shot-wayland-junction-landstrasse-split-drone.jpg) |
| 16:45:44 | [164544-shot-wayland-junction-vorarlberger-rider.jpg](164544-shot-wayland-junction-vorarlberger-rider.jpg) |
| 16:45:56 | [164556-shot-wayland-junction-vorarlberger-drone.jpg](164556-shot-wayland-junction-vorarlberger-drone.jpg) |
| 16:46:07 | [164607-shot-wayland-junction-spoerryweg-rider.jpg](164607-shot-wayland-junction-spoerryweg-rider.jpg) |
| 16:46:19 | [164619-shot-wayland-junction-spoerryweg-drone.jpg](164619-shot-wayland-junction-spoerryweg-drone.jpg) |
| 16:46:37 | [164637-photographer-drone-chase-chase-17-photographer.jpg](164637-photographer-drone-chase-chase-17-photographer.jpg) |
| 16:46:40 | [164640-photographer-drone-chase-chase-18-photographer.jpg](164640-photographer-drone-chase-chase-18-photographer.jpg) |
| 16:46:43 | [164643-photographer-drone-chase-chase-19-photographer.jpg](164643-photographer-drone-chase-chase-19-photographer.jpg) |
| 16:46:46 | [164646-photographer-drone-chase-chase-20-photographer.jpg](164646-photographer-drone-chase-chase-20-photographer.jpg) |
| 16:46:49 | [164649-photographer-drone-chase-chase-21-photographer.jpg](164649-photographer-drone-chase-chase-21-photographer.jpg) |
| 16:46:52 | [164652-photographer-drone-chase-chase-22-photographer.jpg](164652-photographer-drone-chase-chase-22-photographer.jpg) |
| 16:46:55 | [164655-photographer-drone-chase-chase-23-photographer.jpg](164655-photographer-drone-chase-chase-23-photographer.jpg) |
| 16:46:58 | [164658-photographer-drone-chase-chase-24-photographer.jpg](164658-photographer-drone-chase-chase-24-photographer.jpg) |
| 16:47:01 | [164701-photographer-drone-chase-chase-25-photographer.jpg](164701-photographer-drone-chase-chase-25-photographer.jpg) |
| 16:47:44 | [164744-photographer-drone-end.jpg](164744-photographer-drone-end.jpg) |
| 16:47:45 | [164745-photographer-drone-photos-photo-1.jpg](164745-photographer-drone-photos-photo-1.jpg) |
| 16:47:45 | [164745-photographer-drone-photos-photo-2.jpg](164745-photographer-drone-photos-photo-2.jpg) |
| 16:47:45 | [164745-photographer-drone-photos-photo-3.jpg](164745-photographer-drone-photos-photo-3.jpg) |
| 16:47:54 | [164754-photographer-st-chase-chase-01-photographer.jpg](164754-photographer-st-chase-chase-01-photographer.jpg) |
| 16:50:02 | [165002-photographer-st-chase-chase-02-photographer.jpg](165002-photographer-st-chase-chase-02-photographer.jpg) |
| 16:50:05 | [165005-photographer-st-chase-chase-03-photographer.jpg](165005-photographer-st-chase-chase-03-photographer.jpg) |
| 16:52:58 | [165258-photographer-st-chase-chase-04-photographer.jpg](165258-photographer-st-chase-chase-04-photographer.jpg) |
| 16:53:01 | [165301-photographer-st-chase-chase-05-photographer.jpg](165301-photographer-st-chase-chase-05-photographer.jpg) |
| 16:53:04 | [165304-photographer-st-chase-chase-06-photographer.jpg](165304-photographer-st-chase-chase-06-photographer.jpg) |
| 16:55:40 | [165540-photographer-st-chase-chase-07-photographer.jpg](165540-photographer-st-chase-chase-07-photographer.jpg) |
| 16:55:43 | [165543-photographer-st-chase-chase-08-photographer.jpg](165543-photographer-st-chase-chase-08-photographer.jpg) |
| 16:55:46 | [165546-photographer-st-chase-chase-09-photographer.jpg](165546-photographer-st-chase-chase-09-photographer.jpg) |
| 16:55:50 | [165550-photographer-st-end.jpg](165550-photographer-st-end.jpg) |
| 16:55:51 | [165551-photographer-st-photos-photo-1.jpg](165551-photographer-st-photos-photo-1.jpg) |
| 16:55:51 | [165551-photographer-st-photos-photo-2.jpg](165551-photographer-st-photos-photo-2.jpg) |
| 16:55:51 | [165551-photographer-st-photos-photo-3.jpg](165551-photographer-st-photos-photo-3.jpg) |
| 16:55:51 | [165551-photographer-st-photos-photo-4.jpg](165551-photographer-st-photos-photo-4.jpg) |
| 16:58:10 | [165810-phase15-m1-rider-before.png](165810-phase15-m1-rider-before.png) |
| 16:58:20 | [165820-phase15-m1-rider-after.png](165820-phase15-m1-rider-after.png) |
| 16:58:30 | [165830-phase15-m1-bikes-before.png](165830-phase15-m1-bikes-before.png) |
| 16:58:41 | [165841-phase15-m1-bikes-after.png](165841-phase15-m1-bikes-after.png) |
| 16:59:00 | [165900-phase15-m1-trees-generator.png](165900-phase15-m1-trees-generator.png) |
| 16:59:19 | [165919-phase15-m1-trees-files.png](165919-phase15-m1-trees-files.png) |
| 16:59:40 | [165940-phase15-m1-trees-before.png](165940-phase15-m1-trees-before.png) |
| 16:59:59 | [165959-phase15-m1-trees-far-generator.png](165959-phase15-m1-trees-far-generator.png) |
| 17:00:19 | [170019-phase15-m1-trees-far-files.png](170019-phase15-m1-trees-far-files.png) |
| 17:04:48 | [170448-web-web-console.jpg](170448-web-web-console.jpg) |
| 17:04:48 | [170448-web-web-gamepad.jpg](170448-web-web-gamepad.jpg) |
| 17:04:48 | [170448-web-web-gps.jpg](170448-web-web-gps.jpg) |
| 17:04:48 | [170448-web-web-hud.jpg](170448-web-web-hud.jpg) |
| 17:04:48 | [170448-web-web-join.jpg](170448-web-web-join.jpg) |
| 17:04:48 | [170448-web-web-menu.jpg](170448-web-web-menu.jpg) |
| 17:04:48 | [170448-web-web-ride.jpg](170448-web-web-ride.jpg) |
| 17:04:48 | [170448-web-web-riders.jpg](170448-web-web-riders.jpg) |
| 17:04:48 | [170448-web-web-settings.jpg](170448-web-web-settings.jpg) |
| 17:04:48 | [170448-web-web-touch-hints.jpg](170448-web-web-touch-hints.jpg) |
| 17:04:48 | [170448-web-web-touch-hold.jpg](170448-web-web-touch-hold.jpg) |
| 17:04:48 | [170448-web-web-unicorn-flight.jpg](170448-web-web-unicorn-flight.jpg) |
| 17:04:48 | [170448-web-web-unicorn-inspect.jpg](170448-web-web-unicorn-inspect.jpg) |
| 17:04:48 | [170448-web-web-unicorn-menu.jpg](170448-web-web-unicorn-menu.jpg) |
| 17:04:48 | [170448-web-web-weather.jpg](170448-web-web-weather.jpg) |
| 17:04:48 | [170448-web-web.jpg](170448-web-web.jpg) |
| 17:05:26 | [170526-shot-junction-bergstrasse-rider.jpg](170526-shot-junction-bergstrasse-rider.jpg) |
| 17:06:46 | [170646-shot-junction-bergstrasse-drone.jpg](170646-shot-junction-bergstrasse-drone.jpg) |
| 17:07:45 | [170745-shot-junction-hagstrasse-rider.jpg](170745-shot-junction-hagstrasse-rider.jpg) |
| 17:08:20 | [170820-shot-junction-hagstrasse-drone.jpg](170820-shot-junction-hagstrasse-drone.jpg) |
| 17:09:02 | [170902-shot-junction-planknerstrasse-rider.jpg](170902-shot-junction-planknerstrasse-rider.jpg) |
| 17:09:30 | [170930-shot-junction-planknerstrasse-drone.jpg](170930-shot-junction-planknerstrasse-drone.jpg) |
| 17:09:58 | [170958-shot-junction-adlerkreisel-rider.jpg](170958-shot-junction-adlerkreisel-rider.jpg) |
| 17:10:30 | [171030-shot-junction-adlerkreisel-drone.jpg](171030-shot-junction-adlerkreisel-drone.jpg) |
| 17:11:07 | [171107-shot-junction-landstrasse-split-rider.jpg](171107-shot-junction-landstrasse-split-rider.jpg) |
| 17:11:44 | [171144-shot-junction-landstrasse-split-drone.jpg](171144-shot-junction-landstrasse-split-drone.jpg) |
| 17:12:54 | [171254-shot-junction-vorarlberger-rider.jpg](171254-shot-junction-vorarlberger-rider.jpg) |
| 17:13:47 | [171347-shot-junction-vorarlberger-drone.jpg](171347-shot-junction-vorarlberger-drone.jpg) |
| 17:14:42 | [171442-shot-junction-spoerryweg-rider.jpg](171442-shot-junction-spoerryweg-rider.jpg) |
| 17:15:36 | [171536-shot-junction-spoerryweg-drone.jpg](171536-shot-junction-spoerryweg-drone.jpg) |
| 17:39:49 | [173949-photographer-photographer-drone-chase-chase-01-photographer.jpg](173949-photographer-photographer-drone-chase-chase-01-photographer.jpg) |
| 17:39:49 | [173949-photographer-photographer-drone-chase-chase-02-photographer.jpg](173949-photographer-photographer-drone-chase-chase-02-photographer.jpg) |
| 17:39:49 | [173949-photographer-photographer-drone-chase-chase-03-photographer.jpg](173949-photographer-photographer-drone-chase-chase-03-photographer.jpg) |
| 17:39:49 | [173949-photographer-photographer-drone-chase-chase-04-drone.jpg](173949-photographer-photographer-drone-chase-chase-04-drone.jpg) |
| 17:39:49 | [173949-photographer-photographer-drone-chase-chase-05-drone.jpg](173949-photographer-photographer-drone-chase-chase-05-drone.jpg) |
| 17:39:49 | [173949-photographer-photographer-drone-chase-chase-06-drone.jpg](173949-photographer-photographer-drone-chase-chase-06-drone.jpg) |
| 17:39:49 | [173949-photographer-photographer-drone-chase-chase-07-drone.jpg](173949-photographer-photographer-drone-chase-chase-07-drone.jpg) |
| 17:39:49 | [173949-photographer-photographer-drone-chase-chase-08-photographer.jpg](173949-photographer-photographer-drone-chase-chase-08-photographer.jpg) |
| 17:39:49 | [173949-photographer-photographer-drone-chase-chase-09-photographer.jpg](173949-photographer-photographer-drone-chase-chase-09-photographer.jpg) |
| 17:39:49 | [173949-photographer-photographer-drone-chase-chase-10-photographer.jpg](173949-photographer-photographer-drone-chase-chase-10-photographer.jpg) |
| 17:39:49 | [173949-photographer-photographer-drone-chase-chase-11-drone.jpg](173949-photographer-photographer-drone-chase-chase-11-drone.jpg) |
| 17:39:49 | [173949-photographer-photographer-drone-chase-chase-12-drone.jpg](173949-photographer-photographer-drone-chase-chase-12-drone.jpg) |
| 17:39:49 | [173949-photographer-photographer-drone-chase-chase-13-drone.jpg](173949-photographer-photographer-drone-chase-chase-13-drone.jpg) |
| 17:39:49 | [173949-photographer-photographer-drone-chase-chase-14-photographer.jpg](173949-photographer-photographer-drone-chase-chase-14-photographer.jpg) |
| 17:39:49 | [173949-photographer-photographer-drone-chase-chase-15-photographer.jpg](173949-photographer-photographer-drone-chase-chase-15-photographer.jpg) |
| 17:39:49 | [173949-photographer-photographer-drone-chase-chase-16-photographer.jpg](173949-photographer-photographer-drone-chase-chase-16-photographer.jpg) |
| 17:39:49 | [173949-photographer-photographer-drone-chase-chase-17-drone.jpg](173949-photographer-photographer-drone-chase-chase-17-drone.jpg) |
| 17:39:49 | [173949-photographer-photographer-drone-chase-chase-18-drone.jpg](173949-photographer-photographer-drone-chase-chase-18-drone.jpg) |
| 17:39:49 | [173949-photographer-photographer-drone-chase-chase-19-drone.jpg](173949-photographer-photographer-drone-chase-chase-19-drone.jpg) |
| 17:39:49 | [173949-photographer-photographer-drone-chase-chase-20-drone.jpg](173949-photographer-photographer-drone-chase-chase-20-drone.jpg) |
| 17:39:49 | [173949-photographer-photographer-drone-chase-chase-21-photographer.jpg](173949-photographer-photographer-drone-chase-chase-21-photographer.jpg) |
| 17:39:49 | [173949-photographer-photographer-drone-chase-chase-22-photographer.jpg](173949-photographer-photographer-drone-chase-chase-22-photographer.jpg) |
| 17:39:49 | [173949-photographer-photographer-drone-chase-chase-23-photographer.jpg](173949-photographer-photographer-drone-chase-chase-23-photographer.jpg) |
| 17:39:49 | [173949-photographer-photographer-drone-chase-chase-24-photographer.jpg](173949-photographer-photographer-drone-chase-chase-24-photographer.jpg) |
| 17:39:49 | [173949-photographer-photographer-drone-chase-chase-25-photographer.jpg](173949-photographer-photographer-drone-chase-chase-25-photographer.jpg) |
| 17:39:49 | [173949-photographer-photographer-drone-chase-chase-26-photographer.jpg](173949-photographer-photographer-drone-chase-chase-26-photographer.jpg) |
| 17:39:49 | [173949-photographer-photographer-drone-end.jpg](173949-photographer-photographer-drone-end.jpg) |
| 17:39:49 | [173949-photographer-photographer-drone-photos-photo-1.jpg](173949-photographer-photographer-drone-photos-photo-1.jpg) |
| 17:39:49 | [173949-photographer-photographer-drone-photos-photo-2.jpg](173949-photographer-photographer-drone-photos-photo-2.jpg) |
| 17:39:49 | [173949-photographer-photographer-drone-photos-photo-3.jpg](173949-photographer-photographer-drone-photos-photo-3.jpg) |
| 17:58:25 | [175825-junctions-j1-after-wayland-junction-adlerkreisel-drone.jpg](175825-junctions-j1-after-wayland-junction-adlerkreisel-drone.jpg) |
| 17:58:25 | [175825-junctions-j1-after-wayland-junction-adlerkreisel-rider.jpg](175825-junctions-j1-after-wayland-junction-adlerkreisel-rider.jpg) |
| 17:58:25 | [175825-junctions-j1-after-wayland-junction-bergstrasse-drone.jpg](175825-junctions-j1-after-wayland-junction-bergstrasse-drone.jpg) |
| 17:58:25 | [175825-junctions-j1-after-wayland-junction-bergstrasse-rider.jpg](175825-junctions-j1-after-wayland-junction-bergstrasse-rider.jpg) |
| 17:58:25 | [175825-junctions-j1-after-wayland-junction-hagstrasse-drone.jpg](175825-junctions-j1-after-wayland-junction-hagstrasse-drone.jpg) |
| 17:58:25 | [175825-junctions-j1-after-wayland-junction-hagstrasse-rider.jpg](175825-junctions-j1-after-wayland-junction-hagstrasse-rider.jpg) |
| 17:58:25 | [175825-junctions-j1-after-wayland-junction-landstrasse-split-drone.jpg](175825-junctions-j1-after-wayland-junction-landstrasse-split-drone.jpg) |
| 17:58:25 | [175825-junctions-j1-after-wayland-junction-landstrasse-split-rider.jpg](175825-junctions-j1-after-wayland-junction-landstrasse-split-rider.jpg) |
| 17:58:25 | [175825-junctions-j1-after-wayland-junction-planknerstrasse-drone.jpg](175825-junctions-j1-after-wayland-junction-planknerstrasse-drone.jpg) |
| 17:58:25 | [175825-junctions-j1-after-wayland-junction-planknerstrasse-rider.jpg](175825-junctions-j1-after-wayland-junction-planknerstrasse-rider.jpg) |
| 17:58:25 | [175825-junctions-j1-after-wayland-junction-spoerryweg-drone.jpg](175825-junctions-j1-after-wayland-junction-spoerryweg-drone.jpg) |
| 17:58:25 | [175825-junctions-j1-after-wayland-junction-spoerryweg-rider.jpg](175825-junctions-j1-after-wayland-junction-spoerryweg-rider.jpg) |
| 17:58:25 | [175825-junctions-j1-after-wayland-junction-vorarlberger-drone.jpg](175825-junctions-j1-after-wayland-junction-vorarlberger-drone.jpg) |
| 17:58:25 | [175825-junctions-j1-after-wayland-junction-vorarlberger-rider.jpg](175825-junctions-j1-after-wayland-junction-vorarlberger-rider.jpg) |
| 17:58:25 | [175825-junctions-j1-after-x11-junction-adlerkreisel-drone.jpg](175825-junctions-j1-after-x11-junction-adlerkreisel-drone.jpg) |
| 17:58:25 | [175825-junctions-j1-after-x11-junction-adlerkreisel-rider.jpg](175825-junctions-j1-after-x11-junction-adlerkreisel-rider.jpg) |
| 17:58:25 | [175825-junctions-j1-after-x11-junction-bergstrasse-drone.jpg](175825-junctions-j1-after-x11-junction-bergstrasse-drone.jpg) |
| 17:58:25 | [175825-junctions-j1-after-x11-junction-bergstrasse-rider.jpg](175825-junctions-j1-after-x11-junction-bergstrasse-rider.jpg) |
| 17:58:25 | [175825-junctions-j1-after-x11-junction-hagstrasse-drone.jpg](175825-junctions-j1-after-x11-junction-hagstrasse-drone.jpg) |
| 17:58:25 | [175825-junctions-j1-after-x11-junction-hagstrasse-rider.jpg](175825-junctions-j1-after-x11-junction-hagstrasse-rider.jpg) |
| 17:58:25 | [175825-junctions-j1-after-x11-junction-landstrasse-split-drone.jpg](175825-junctions-j1-after-x11-junction-landstrasse-split-drone.jpg) |
| 17:58:25 | [175825-junctions-j1-after-x11-junction-landstrasse-split-rider.jpg](175825-junctions-j1-after-x11-junction-landstrasse-split-rider.jpg) |
| 17:58:25 | [175825-junctions-j1-after-x11-junction-planknerstrasse-drone.jpg](175825-junctions-j1-after-x11-junction-planknerstrasse-drone.jpg) |
| 17:58:25 | [175825-junctions-j1-after-x11-junction-planknerstrasse-rider.jpg](175825-junctions-j1-after-x11-junction-planknerstrasse-rider.jpg) |
| 17:58:25 | [175825-junctions-j1-after-x11-junction-spoerryweg-drone.jpg](175825-junctions-j1-after-x11-junction-spoerryweg-drone.jpg) |
| 17:58:25 | [175825-junctions-j1-after-x11-junction-spoerryweg-rider.jpg](175825-junctions-j1-after-x11-junction-spoerryweg-rider.jpg) |
| 17:58:25 | [175825-junctions-j1-after-x11-junction-vorarlberger-drone.jpg](175825-junctions-j1-after-x11-junction-vorarlberger-drone.jpg) |
| 17:58:25 | [175825-junctions-j1-after-x11-junction-vorarlberger-rider.jpg](175825-junctions-j1-after-x11-junction-vorarlberger-rider.jpg) |
| 18:09:51 | [180951-shot-wayland-routes-workspace.jpg](180951-shot-wayland-routes-workspace.jpg) |
| 18:10:37 | [181037-scenes-view-distance-view-distance-12km.jpg](181037-scenes-view-distance-view-distance-12km.jpg) |
| 18:10:37 | [181037-scenes-view-distance-view-distance-2km.jpg](181037-scenes-view-distance-view-distance-2km.jpg) |
| 18:10:37 | [181037-scenes-view-distance-view-distance-unlimited.jpg](181037-scenes-view-distance-view-distance-unlimited.jpg) |
| 18:21:19 | [182119-shot-wayland-routes-workspace.jpg](182119-shot-wayland-routes-workspace.jpg) |
| 18:34:43 | [183443-shot-wayland-menu-time-calendar.jpg](183443-shot-wayland-menu-time-calendar.jpg) |
| 18:55:27 | [185527-shot-wayland-menu-time-calendar.jpg](185527-shot-wayland-menu-time-calendar.jpg) |
| 18:55:50 | [185550-scenes-menu-time-calendar.jpg](185550-scenes-menu-time-calendar.jpg) |
| 18:55:57 | [185557-web-web.jpg](185557-web-web.jpg) |
| 20:10:02 | [201002-host-voice-hosting.jpg](201002-host-voice-hosting.jpg) |
| 20:25:14 | [202514-bib-jersey-2026-11-16-after-bib-chase-riding.jpg](202514-bib-jersey-2026-11-16-after-bib-chase-riding.jpg) |
| 20:25:14 | [202514-bib-jersey-2026-11-16-after-bib-close-back-riding.jpg](202514-bib-jersey-2026-11-16-after-bib-close-back-riding.jpg) |
| 20:25:14 | [202514-bib-jersey-2026-11-16-after-bib-close-back-slim.jpg](202514-bib-jersey-2026-11-16-after-bib-close-back-slim.jpg) |
| 20:25:14 | [202514-bib-jersey-2026-11-16-after-bib-close-back-standing.jpg](202514-bib-jersey-2026-11-16-after-bib-close-back-standing.jpg) |
| 20:25:14 | [202514-bib-jersey-2026-11-16-after-bib-close-front-riding.jpg](202514-bib-jersey-2026-11-16-after-bib-close-front-riding.jpg) |
| 20:25:14 | [202514-bib-jersey-2026-11-16-after-bib-close-side-riding.jpg](202514-bib-jersey-2026-11-16-after-bib-close-side-riding.jpg) |
| 20:25:14 | [202514-bib-jersey-2026-11-16-after-bib-close-side-sprint.jpg](202514-bib-jersey-2026-11-16-after-bib-close-side-sprint.jpg) |
| 20:25:14 | [202514-bib-jersey-2026-11-16-after-bib-close-side-standing.jpg](202514-bib-jersey-2026-11-16-after-bib-close-side-standing.jpg) |
| 20:25:14 | [202514-bib-jersey-2026-11-16-after-bib-close-side-strong.jpg](202514-bib-jersey-2026-11-16-after-bib-close-side-strong.jpg) |
| 20:25:14 | [202514-bib-jersey-2026-11-16-after-bib-pockets-accent.jpg](202514-bib-jersey-2026-11-16-after-bib-pockets-accent.jpg) |
| 20:25:14 | [202514-bib-jersey-2026-11-16-after-bib-pockets-close.jpg](202514-bib-jersey-2026-11-16-after-bib-pockets-close.jpg) |
| 20:25:14 | [202514-bib-jersey-2026-11-16-after-bib-workshop-mirror.jpg](202514-bib-jersey-2026-11-16-after-bib-workshop-mirror.jpg) |
| 20:25:14 | [202514-bib-jersey-2026-11-16-before-bib-chase-riding.jpg](202514-bib-jersey-2026-11-16-before-bib-chase-riding.jpg) |
| 20:25:14 | [202514-bib-jersey-2026-11-16-before-bib-close-back-riding.jpg](202514-bib-jersey-2026-11-16-before-bib-close-back-riding.jpg) |
| 20:25:14 | [202514-bib-jersey-2026-11-16-before-bib-close-back-slim.jpg](202514-bib-jersey-2026-11-16-before-bib-close-back-slim.jpg) |
| 20:25:14 | [202514-bib-jersey-2026-11-16-before-bib-close-back-standing.jpg](202514-bib-jersey-2026-11-16-before-bib-close-back-standing.jpg) |
| 20:25:14 | [202514-bib-jersey-2026-11-16-before-bib-close-front-riding.jpg](202514-bib-jersey-2026-11-16-before-bib-close-front-riding.jpg) |
| 20:25:14 | [202514-bib-jersey-2026-11-16-before-bib-close-side-riding.jpg](202514-bib-jersey-2026-11-16-before-bib-close-side-riding.jpg) |
| 20:25:14 | [202514-bib-jersey-2026-11-16-before-bib-close-side-sprint.jpg](202514-bib-jersey-2026-11-16-before-bib-close-side-sprint.jpg) |
| 20:25:14 | [202514-bib-jersey-2026-11-16-before-bib-close-side-standing.jpg](202514-bib-jersey-2026-11-16-before-bib-close-side-standing.jpg) |
| 20:25:14 | [202514-bib-jersey-2026-11-16-before-bib-close-side-strong.jpg](202514-bib-jersey-2026-11-16-before-bib-close-side-strong.jpg) |
| 20:25:14 | [202514-bib-jersey-2026-11-16-before-bib-workshop-mirror.jpg](202514-bib-jersey-2026-11-16-before-bib-workshop-mirror.jpg) |
| 20:25:14 | [202514-bib-jersey-2026-11-16-compare-bib-chase-riding-before-after.jpg](202514-bib-jersey-2026-11-16-compare-bib-chase-riding-before-after.jpg) |
| 20:25:14 | [202514-bib-jersey-2026-11-16-compare-bib-close-back-riding-before-after.jpg](202514-bib-jersey-2026-11-16-compare-bib-close-back-riding-before-after.jpg) |
| 20:25:14 | [202514-bib-jersey-2026-11-16-compare-bib-close-back-slim-before-after.jpg](202514-bib-jersey-2026-11-16-compare-bib-close-back-slim-before-after.jpg) |
| 20:25:14 | [202514-bib-jersey-2026-11-16-compare-bib-close-back-standing-before-after.jpg](202514-bib-jersey-2026-11-16-compare-bib-close-back-standing-before-after.jpg) |
| 20:25:14 | [202514-bib-jersey-2026-11-16-compare-bib-close-front-riding-before-after.jpg](202514-bib-jersey-2026-11-16-compare-bib-close-front-riding-before-after.jpg) |
| 20:25:14 | [202514-bib-jersey-2026-11-16-compare-bib-close-side-riding-before-after.jpg](202514-bib-jersey-2026-11-16-compare-bib-close-side-riding-before-after.jpg) |
| 20:25:14 | [202514-bib-jersey-2026-11-16-compare-bib-close-side-sprint-before-after.jpg](202514-bib-jersey-2026-11-16-compare-bib-close-side-sprint-before-after.jpg) |
| 20:25:14 | [202514-bib-jersey-2026-11-16-compare-bib-close-side-standing-before-after.jpg](202514-bib-jersey-2026-11-16-compare-bib-close-side-standing-before-after.jpg) |
| 20:25:14 | [202514-bib-jersey-2026-11-16-compare-bib-close-side-strong-before-after.jpg](202514-bib-jersey-2026-11-16-compare-bib-close-side-strong-before-after.jpg) |
| 20:25:14 | [202514-bib-jersey-2026-11-16-compare-bib-workshop-mirror-before-after.jpg](202514-bib-jersey-2026-11-16-compare-bib-workshop-mirror-before-after.jpg) |
| 21:22:50 | [212250-video-wayland-status-phone-grab.jpg](212250-video-wayland-status-phone-grab.jpg) |
| 21:22:50 | [212250-video-wayland-status-phone-grab.mp4](212250-video-wayland-status-phone-grab.mp4) |
| 21:22:59 | [212259-shot-wayland-status-phone-hold.jpg](212259-shot-wayland-status-phone-hold.jpg) |
| 21:23:07 | [212307-shot-wayland-status-mouth-muted.jpg](212307-shot-wayland-status-mouth-muted.jpg) |
| 21:23:15 | [212315-shot-wayland-status-vr-headset.jpg](212315-shot-wayland-status-vr-headset.jpg) |
| 21:23:25 | [212325-shot-wayland-status-headphones.jpg](212325-shot-wayland-status-headphones.jpg) |
| 21:23:37 | [212337-shot-wayland-status-group-mixed.jpg](212337-shot-wayland-status-group-mixed.jpg) |
| 22:42:58 | [224258-fog-fix-2026-11-16-bf-high-12km-before-after.jpg](224258-fog-fix-2026-11-16-bf-high-12km-before-after.jpg) |
| 22:42:58 | [224258-fog-fix-2026-11-16-bf-high-2km-before-after.jpg](224258-fog-fix-2026-11-16-bf-high-2km-before-after.jpg) |
| 22:42:58 | [224258-fog-fix-2026-11-16-bf-high-unlimited-before-after.jpg](224258-fog-fix-2026-11-16-bf-high-unlimited-before-after.jpg) |
| 22:42:58 | [224258-fog-fix-2026-11-16-bf-low-8km-before-after.jpg](224258-fog-fix-2026-11-16-bf-low-8km-before-after.jpg) |
| 22:42:58 | [224258-fog-fix-2026-11-16-bf-medium-30km-before-after.jpg](224258-fog-fix-2026-11-16-bf-medium-30km-before-after.jpg) |
| 22:42:58 | [224258-fog-fix-2026-11-16-bf-mist-12km-before-after.jpg](224258-fog-fix-2026-11-16-bf-mist-12km-before-after.jpg) |
| 22:42:58 | [224258-fog-fix-2026-11-16-bf-rain-12km-before-after.jpg](224258-fog-fix-2026-11-16-bf-rain-12km-before-after.jpg) |
| 22:42:58 | [224258-fog-fix-2026-11-16-bf-sunset-12km-before-after.jpg](224258-fog-fix-2026-11-16-bf-sunset-12km-before-after.jpg) |
| 22:42:58 | [224258-fog-fix-2026-11-16-bf-sunset-2km-before-after.jpg](224258-fog-fix-2026-11-16-bf-sunset-2km-before-after.jpg) |
| 22:42:58 | [224258-fog-fix-2026-11-16-calib-t1200-az0.png](224258-fog-fix-2026-11-16-calib-t1200-az0.png) |
| 22:42:58 | [224258-fog-fix-2026-11-16-calib-t1500-az0.png](224258-fog-fix-2026-11-16-calib-t1500-az0.png) |
| 22:42:58 | [224258-fog-fix-2026-11-16-calib-t1630-az0.png](224258-fog-fix-2026-11-16-calib-t1630-az0.png) |
| 22:42:58 | [224258-fog-fix-2026-11-16-calib-t1715-az0.png](224258-fog-fix-2026-11-16-calib-t1715-az0.png) |
| 22:42:58 | [224258-fog-fix-2026-11-16-calib-t1740-az0.png](224258-fog-fix-2026-11-16-calib-t1740-az0.png) |
| 22:42:58 | [224258-fog-fix-2026-11-16-calib-t1800-az0.png](224258-fog-fix-2026-11-16-calib-t1800-az0.png) |
| 22:42:58 | [224258-fog-fix-2026-11-16-calib-t1820-az0.png](224258-fog-fix-2026-11-16-calib-t1820-az0.png) |
| 22:42:58 | [224258-fog-fix-2026-11-16-calib-t1845-az0.png](224258-fog-fix-2026-11-16-calib-t1845-az0.png) |
| 22:42:58 | [224258-fog-fix-2026-11-16-calib-t2000-az0.png](224258-fog-fix-2026-11-16-calib-t2000-az0.png) |
| 22:42:58 | [224258-fog-fix-2026-11-16-pairs-bf-high-12km-after.png](224258-fog-fix-2026-11-16-pairs-bf-high-12km-after.png) |
| 22:42:58 | [224258-fog-fix-2026-11-16-pairs-bf-high-12km-before.png](224258-fog-fix-2026-11-16-pairs-bf-high-12km-before.png) |
| 22:42:58 | [224258-fog-fix-2026-11-16-pairs-bf-high-2km-after.png](224258-fog-fix-2026-11-16-pairs-bf-high-2km-after.png) |
| 22:42:58 | [224258-fog-fix-2026-11-16-pairs-bf-high-2km-before.png](224258-fog-fix-2026-11-16-pairs-bf-high-2km-before.png) |
| 22:42:58 | [224258-fog-fix-2026-11-16-pairs-bf-high-unlimited-after.png](224258-fog-fix-2026-11-16-pairs-bf-high-unlimited-after.png) |
| 22:42:58 | [224258-fog-fix-2026-11-16-pairs-bf-high-unlimited-before.png](224258-fog-fix-2026-11-16-pairs-bf-high-unlimited-before.png) |
| 22:42:58 | [224258-fog-fix-2026-11-16-pairs-bf-low-8km-after.png](224258-fog-fix-2026-11-16-pairs-bf-low-8km-after.png) |
| 22:42:58 | [224258-fog-fix-2026-11-16-pairs-bf-low-8km-before.png](224258-fog-fix-2026-11-16-pairs-bf-low-8km-before.png) |
| 22:42:58 | [224258-fog-fix-2026-11-16-pairs-bf-medium-30km-after.png](224258-fog-fix-2026-11-16-pairs-bf-medium-30km-after.png) |
| 22:42:58 | [224258-fog-fix-2026-11-16-pairs-bf-medium-30km-before.png](224258-fog-fix-2026-11-16-pairs-bf-medium-30km-before.png) |
| 22:42:58 | [224258-fog-fix-2026-11-16-pairs-bf-mist-12km-after.png](224258-fog-fix-2026-11-16-pairs-bf-mist-12km-after.png) |
| 22:42:58 | [224258-fog-fix-2026-11-16-pairs-bf-mist-12km-before.png](224258-fog-fix-2026-11-16-pairs-bf-mist-12km-before.png) |
| 22:42:58 | [224258-fog-fix-2026-11-16-pairs-bf-rain-12km-after.png](224258-fog-fix-2026-11-16-pairs-bf-rain-12km-after.png) |
| 22:42:58 | [224258-fog-fix-2026-11-16-pairs-bf-rain-12km-before.png](224258-fog-fix-2026-11-16-pairs-bf-rain-12km-before.png) |
| 22:42:58 | [224258-fog-fix-2026-11-16-pairs-bf-sunset-12km-after.png](224258-fog-fix-2026-11-16-pairs-bf-sunset-12km-after.png) |
| 22:42:58 | [224258-fog-fix-2026-11-16-pairs-bf-sunset-12km-before.png](224258-fog-fix-2026-11-16-pairs-bf-sunset-12km-before.png) |
| 22:42:58 | [224258-fog-fix-2026-11-16-pairs-bf-sunset-2km-after.png](224258-fog-fix-2026-11-16-pairs-bf-sunset-2km-after.png) |
| 22:42:58 | [224258-fog-fix-2026-11-16-pairs-bf-sunset-2km-before.png](224258-fog-fix-2026-11-16-pairs-bf-sunset-2km-before.png) |
| 22:42:58 | [224258-fog-fix-2026-11-16-pairs-tf-high-12km-after.png](224258-fog-fix-2026-11-16-pairs-tf-high-12km-after.png) |
| 22:42:58 | [224258-fog-fix-2026-11-16-pairs-tf-high-12km-before.png](224258-fog-fix-2026-11-16-pairs-tf-high-12km-before.png) |
| 22:42:58 | [224258-fog-fix-2026-11-16-pairs-tf-high-2km-after.png](224258-fog-fix-2026-11-16-pairs-tf-high-2km-after.png) |
| 22:42:58 | [224258-fog-fix-2026-11-16-pairs-tf-high-2km-before.png](224258-fog-fix-2026-11-16-pairs-tf-high-2km-before.png) |
| 22:42:58 | [224258-fog-fix-2026-11-16-pairs-tf-high-unlimited-after.png](224258-fog-fix-2026-11-16-pairs-tf-high-unlimited-after.png) |
| 22:42:58 | [224258-fog-fix-2026-11-16-pairs-tf-high-unlimited-before.png](224258-fog-fix-2026-11-16-pairs-tf-high-unlimited-before.png) |
| 22:42:58 | [224258-fog-fix-2026-11-16-pairs-tf-low-8km-after.png](224258-fog-fix-2026-11-16-pairs-tf-low-8km-after.png) |
| 22:42:58 | [224258-fog-fix-2026-11-16-pairs-tf-low-8km-before.png](224258-fog-fix-2026-11-16-pairs-tf-low-8km-before.png) |
| 22:42:58 | [224258-fog-fix-2026-11-16-pairs-tf-medium-30km-after.png](224258-fog-fix-2026-11-16-pairs-tf-medium-30km-after.png) |
| 22:42:58 | [224258-fog-fix-2026-11-16-pairs-tf-medium-30km-before.png](224258-fog-fix-2026-11-16-pairs-tf-medium-30km-before.png) |
| 22:42:58 | [224258-fog-fix-2026-11-16-pairs-tf-mist-12km-after.png](224258-fog-fix-2026-11-16-pairs-tf-mist-12km-after.png) |
| 22:42:58 | [224258-fog-fix-2026-11-16-pairs-tf-mist-12km-before.png](224258-fog-fix-2026-11-16-pairs-tf-mist-12km-before.png) |
| 22:42:58 | [224258-fog-fix-2026-11-16-pairs-tf-rain-12km-after.png](224258-fog-fix-2026-11-16-pairs-tf-rain-12km-after.png) |
| 22:42:58 | [224258-fog-fix-2026-11-16-pairs-tf-rain-12km-before.png](224258-fog-fix-2026-11-16-pairs-tf-rain-12km-before.png) |
| 22:42:58 | [224258-fog-fix-2026-11-16-pairs-tf-sunset-12km-after.png](224258-fog-fix-2026-11-16-pairs-tf-sunset-12km-after.png) |
| 22:42:58 | [224258-fog-fix-2026-11-16-pairs-tf-sunset-12km-before.png](224258-fog-fix-2026-11-16-pairs-tf-sunset-12km-before.png) |
| 22:42:58 | [224258-fog-fix-2026-11-16-pairs-tf-sunset-2km-after.png](224258-fog-fix-2026-11-16-pairs-tf-sunset-2km-after.png) |
| 22:42:58 | [224258-fog-fix-2026-11-16-pairs-tf-sunset-2km-before.png](224258-fog-fix-2026-11-16-pairs-tf-sunset-2km-before.png) |
| 22:42:58 | [224258-fog-fix-2026-11-16-tf-high-12km-before-after.jpg](224258-fog-fix-2026-11-16-tf-high-12km-before-after.jpg) |
| 22:42:58 | [224258-fog-fix-2026-11-16-tf-high-2km-before-after.jpg](224258-fog-fix-2026-11-16-tf-high-2km-before-after.jpg) |
| 22:42:58 | [224258-fog-fix-2026-11-16-tf-high-unlimited-before-after.jpg](224258-fog-fix-2026-11-16-tf-high-unlimited-before-after.jpg) |
| 22:42:58 | [224258-fog-fix-2026-11-16-tf-low-8km-before-after.jpg](224258-fog-fix-2026-11-16-tf-low-8km-before-after.jpg) |
| 22:42:58 | [224258-fog-fix-2026-11-16-tf-medium-30km-before-after.jpg](224258-fog-fix-2026-11-16-tf-medium-30km-before-after.jpg) |
| 22:42:58 | [224258-fog-fix-2026-11-16-tf-mist-12km-before-after.jpg](224258-fog-fix-2026-11-16-tf-mist-12km-before-after.jpg) |
| 22:42:58 | [224258-fog-fix-2026-11-16-tf-rain-12km-before-after.jpg](224258-fog-fix-2026-11-16-tf-rain-12km-before-after.jpg) |
| 22:42:58 | [224258-fog-fix-2026-11-16-tf-sunset-12km-before-after.jpg](224258-fog-fix-2026-11-16-tf-sunset-12km-before-after.jpg) |
| 22:42:58 | [224258-fog-fix-2026-11-16-tf-sunset-2km-before-after.jpg](224258-fog-fix-2026-11-16-tf-sunset-2km-before-after.jpg) |
| 23:00:06 | [230006-photographer-shared-x11-a-end.jpg](230006-photographer-shared-x11-a-end.jpg) |
| 23:00:07 | [230007-photographer-shared-x11-b-end.jpg](230007-photographer-shared-x11-b-end.jpg) |
| 23:33:35 | [233335-photographer-shared-wayland-b-chase-chase-01-other-photographer.jpg](233335-photographer-shared-wayland-b-chase-chase-01-other-photographer.jpg) |
| 23:33:38 | [233338-photographer-shared-wayland-b-chase-chase-02-other-drone.jpg](233338-photographer-shared-wayland-b-chase-chase-02-other-drone.jpg) |
| 23:33:41 | [233341-photographer-shared-wayland-b-chase-chase-03-other-drone.jpg](233341-photographer-shared-wayland-b-chase-chase-03-other-drone.jpg) |
| 23:33:44 | [233344-photographer-shared-wayland-b-chase-chase-04-other-drone.jpg](233344-photographer-shared-wayland-b-chase-chase-04-other-drone.jpg) |
| 23:33:47 | [233347-photographer-shared-wayland-b-chase-chase-05-other-drone.jpg](233347-photographer-shared-wayland-b-chase-chase-05-other-drone.jpg) |
| 23:33:50 | [233350-photographer-shared-wayland-b-chase-chase-06-other-drone.jpg](233350-photographer-shared-wayland-b-chase-chase-06-other-drone.jpg) |
| 23:33:53 | [233353-photographer-shared-wayland-b-chase-chase-07-other-drone.jpg](233353-photographer-shared-wayland-b-chase-chase-07-other-drone.jpg) |
| 23:33:56 | [233356-photographer-shared-wayland-b-chase-chase-08-other-drone.jpg](233356-photographer-shared-wayland-b-chase-chase-08-other-drone.jpg) |
| 23:33:59 | [233359-photographer-shared-wayland-b-chase-chase-09-other-drone.jpg](233359-photographer-shared-wayland-b-chase-chase-09-other-drone.jpg) |
| 23:34:02 | [233402-photographer-shared-wayland-b-chase-chase-10-other-drone.jpg](233402-photographer-shared-wayland-b-chase-chase-10-other-drone.jpg) |
| 23:34:05 | [233405-photographer-shared-wayland-b-chase-chase-11-other-drone.jpg](233405-photographer-shared-wayland-b-chase-chase-11-other-drone.jpg) |
| 23:34:08 | [233408-photographer-shared-wayland-b-chase-chase-12-other-drone.jpg](233408-photographer-shared-wayland-b-chase-chase-12-other-drone.jpg) |
| 23:34:10 | [233410-photographer-shared-wayland-b-chase-chase-13-other-flash.jpg](233410-photographer-shared-wayland-b-chase-chase-13-other-flash.jpg) |
| 23:34:10 | [233410-photographer-shared-wayland-b-chase-chase-14-other-flash.jpg](233410-photographer-shared-wayland-b-chase-chase-14-other-flash.jpg) |
| 23:34:11 | [233411-photographer-shared-wayland-b-chase-chase-15-other-flash.jpg](233411-photographer-shared-wayland-b-chase-chase-15-other-flash.jpg) |
| 23:34:11 | [233411-photographer-shared-wayland-b-chase-chase-16-other-flash.jpg](233411-photographer-shared-wayland-b-chase-chase-16-other-flash.jpg) |
| 23:34:11 | [233411-photographer-shared-wayland-b-chase-chase-17-other-flash.jpg](233411-photographer-shared-wayland-b-chase-chase-17-other-flash.jpg) |
| 23:34:14 | [233414-photographer-shared-wayland-b-chase-chase-18-other-drone.jpg](233414-photographer-shared-wayland-b-chase-chase-18-other-drone.jpg) |
| 23:36:44 | [233644-photographer-shared-wayland-a-end.jpg](233644-photographer-shared-wayland-a-end.jpg) |
| 23:36:47 | [233647-photographer-shared-wayland-b-end.jpg](233647-photographer-shared-wayland-b-end.jpg) |
| 23:36:48 | [233648-photographer-shared-wayland-a-photos-photo-1.jpg](233648-photographer-shared-wayland-a-photos-photo-1.jpg) |
| 23:39:30 | [233930-photographer-shared-x11-b-chase-chase-01-other-photographer.jpg](233930-photographer-shared-x11-b-chase-chase-01-other-photographer.jpg) |
| 23:39:33 | [233933-photographer-shared-x11-b-chase-chase-02-other-drone.jpg](233933-photographer-shared-x11-b-chase-chase-02-other-drone.jpg) |
| 23:39:36 | [233936-photographer-shared-x11-b-chase-chase-03-other-drone.jpg](233936-photographer-shared-x11-b-chase-chase-03-other-drone.jpg) |
| 23:39:39 | [233939-photographer-shared-x11-b-chase-chase-04-other-drone.jpg](233939-photographer-shared-x11-b-chase-chase-04-other-drone.jpg) |
| 23:39:42 | [233942-photographer-shared-x11-b-chase-chase-05-other-drone.jpg](233942-photographer-shared-x11-b-chase-chase-05-other-drone.jpg) |
| 23:39:45 | [233945-photographer-shared-x11-b-chase-chase-06-other-drone.jpg](233945-photographer-shared-x11-b-chase-chase-06-other-drone.jpg) |
| 23:39:48 | [233948-photographer-shared-x11-b-chase-chase-07-other-drone.jpg](233948-photographer-shared-x11-b-chase-chase-07-other-drone.jpg) |
| 23:39:52 | [233952-photographer-shared-x11-b-chase-chase-08-other-drone.jpg](233952-photographer-shared-x11-b-chase-chase-08-other-drone.jpg) |
| 23:39:55 | [233955-photographer-shared-x11-b-chase-chase-09-other-drone.jpg](233955-photographer-shared-x11-b-chase-chase-09-other-drone.jpg) |
| 23:39:58 | [233958-photographer-shared-x11-b-chase-chase-10-other-drone.jpg](233958-photographer-shared-x11-b-chase-chase-10-other-drone.jpg) |
| 23:40:01 | [234001-photographer-shared-x11-b-chase-chase-11-other-drone.jpg](234001-photographer-shared-x11-b-chase-chase-11-other-drone.jpg) |
| 23:40:03 | [234003-photographer-shared-x11-b-chase-chase-12-other-flash.jpg](234003-photographer-shared-x11-b-chase-chase-12-other-flash.jpg) |
| 23:40:06 | [234006-photographer-shared-x11-b-chase-chase-13-other-drone.jpg](234006-photographer-shared-x11-b-chase-chase-13-other-drone.jpg) |
| 23:42:36 | [234236-photographer-shared-x11-a-end.jpg](234236-photographer-shared-x11-a-end.jpg) |
| 23:42:41 | [234241-photographer-shared-x11-b-end.jpg](234241-photographer-shared-x11-b-end.jpg) |
| 23:42:45 | [234245-photographer-shared-x11-a-photos-photo-1.jpg](234245-photographer-shared-x11-a-photos-photo-1.jpg) |
| 23:57:38 | [235738-fog-fix-2026-11-16-bf-high-12km-before-after.jpg](235738-fog-fix-2026-11-16-bf-high-12km-before-after.jpg) |
| 23:57:38 | [235738-fog-fix-2026-11-16-bf-high-2km-before-after.jpg](235738-fog-fix-2026-11-16-bf-high-2km-before-after.jpg) |
| 23:57:38 | [235738-fog-fix-2026-11-16-bf-high-unlimited-before-after.jpg](235738-fog-fix-2026-11-16-bf-high-unlimited-before-after.jpg) |
| 23:57:38 | [235738-fog-fix-2026-11-16-bf-low-8km-away-from-sun-before-after.jpg](235738-fog-fix-2026-11-16-bf-low-8km-away-from-sun-before-after.jpg) |
| 23:57:38 | [235738-fog-fix-2026-11-16-bf-low-8km-before-after.jpg](235738-fog-fix-2026-11-16-bf-low-8km-before-after.jpg) |
| 23:57:38 | [235738-fog-fix-2026-11-16-bf-low-8km-toward-sun-before-after.jpg](235738-fog-fix-2026-11-16-bf-low-8km-toward-sun-before-after.jpg) |
| 23:57:38 | [235738-fog-fix-2026-11-16-bf-medium-30km-before-after.jpg](235738-fog-fix-2026-11-16-bf-medium-30km-before-after.jpg) |
| 23:57:38 | [235738-fog-fix-2026-11-16-bf-mist-12km-before-after.jpg](235738-fog-fix-2026-11-16-bf-mist-12km-before-after.jpg) |
| 23:57:38 | [235738-fog-fix-2026-11-16-bf-rain-12km-before-after.jpg](235738-fog-fix-2026-11-16-bf-rain-12km-before-after.jpg) |
| 23:57:38 | [235738-fog-fix-2026-11-16-bf-sunset-12km-away-from-sun-before-after.jpg](235738-fog-fix-2026-11-16-bf-sunset-12km-away-from-sun-before-after.jpg) |
| 23:57:38 | [235738-fog-fix-2026-11-16-bf-sunset-12km-before-after.jpg](235738-fog-fix-2026-11-16-bf-sunset-12km-before-after.jpg) |
| 23:57:38 | [235738-fog-fix-2026-11-16-bf-sunset-12km-toward-sun-before-after.jpg](235738-fog-fix-2026-11-16-bf-sunset-12km-toward-sun-before-after.jpg) |
| 23:57:38 | [235738-fog-fix-2026-11-16-bf-sunset-2km-before-after.jpg](235738-fog-fix-2026-11-16-bf-sunset-2km-before-after.jpg) |
| 23:57:38 | [235738-fog-fix-2026-11-16-calib-t1200-az0.png](235738-fog-fix-2026-11-16-calib-t1200-az0.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-calib-t1500-az0.png](235738-fog-fix-2026-11-16-calib-t1500-az0.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-calib-t1630-az0.png](235738-fog-fix-2026-11-16-calib-t1630-az0.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-calib-t1715-az0.png](235738-fog-fix-2026-11-16-calib-t1715-az0.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-calib-t1740-az0.png](235738-fog-fix-2026-11-16-calib-t1740-az0.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-calib-t1800-az0.png](235738-fog-fix-2026-11-16-calib-t1800-az0.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-calib-t1820-az0.png](235738-fog-fix-2026-11-16-calib-t1820-az0.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-calib-t1845-az0.png](235738-fog-fix-2026-11-16-calib-t1845-az0.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-calib-t2000-az0.png](235738-fog-fix-2026-11-16-calib-t2000-az0.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1500-az000.png](235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1500-az000.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1500-az030.png](235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1500-az030.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1500-az060.png](235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1500-az060.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1500-az090.png](235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1500-az090.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1500-az120.png](235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1500-az120.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1500-az150.png](235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1500-az150.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1500-az180.png](235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1500-az180.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1500-az210.png](235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1500-az210.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1500-az240.png](235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1500-az240.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1500-az270.png](235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1500-az270.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1500-az300.png](235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1500-az300.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1500-az330.png](235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1500-az330.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1600-az000.png](235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1600-az000.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1600-az030.png](235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1600-az030.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1600-az060.png](235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1600-az060.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1600-az090.png](235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1600-az090.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1600-az120.png](235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1600-az120.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1600-az150.png](235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1600-az150.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1600-az180.png](235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1600-az180.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1600-az210.png](235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1600-az210.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1600-az240.png](235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1600-az240.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1600-az270.png](235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1600-az270.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1600-az300.png](235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1600-az300.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1600-az330.png](235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1600-az330.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1630-az000.png](235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1630-az000.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1630-az030.png](235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1630-az030.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1630-az060.png](235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1630-az060.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1630-az090.png](235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1630-az090.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1630-az120.png](235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1630-az120.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1630-az150.png](235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1630-az150.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1630-az180.png](235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1630-az180.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1630-az210.png](235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1630-az210.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1630-az240.png](235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1630-az240.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1630-az270.png](235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1630-az270.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1630-az300.png](235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1630-az300.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1630-az330.png](235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1630-az330.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1800-az000.png](235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1800-az000.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1800-az030.png](235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1800-az030.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1800-az060.png](235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1800-az060.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1800-az090.png](235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1800-az090.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1800-az120.png](235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1800-az120.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1800-az150.png](235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1800-az150.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1800-az180.png](235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1800-az180.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1800-az210.png](235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1800-az210.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1800-az240.png](235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1800-az240.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1800-az270.png](235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1800-az270.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1800-az300.png](235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1800-az300.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1800-az330.png](235738-fog-fix-2026-11-16-direction-calibration-bf-auto-t1800-az330.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-t1500-az000.png](235738-fog-fix-2026-11-16-direction-calibration-bf-t1500-az000.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-t1500-az030.png](235738-fog-fix-2026-11-16-direction-calibration-bf-t1500-az030.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-t1500-az060.png](235738-fog-fix-2026-11-16-direction-calibration-bf-t1500-az060.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-t1500-az090.png](235738-fog-fix-2026-11-16-direction-calibration-bf-t1500-az090.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-t1500-az120.png](235738-fog-fix-2026-11-16-direction-calibration-bf-t1500-az120.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-t1500-az150.png](235738-fog-fix-2026-11-16-direction-calibration-bf-t1500-az150.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-t1500-az180.png](235738-fog-fix-2026-11-16-direction-calibration-bf-t1500-az180.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-t1500-az210.png](235738-fog-fix-2026-11-16-direction-calibration-bf-t1500-az210.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-t1500-az240.png](235738-fog-fix-2026-11-16-direction-calibration-bf-t1500-az240.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-t1500-az270.png](235738-fog-fix-2026-11-16-direction-calibration-bf-t1500-az270.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-t1500-az300.png](235738-fog-fix-2026-11-16-direction-calibration-bf-t1500-az300.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-t1500-az330.png](235738-fog-fix-2026-11-16-direction-calibration-bf-t1500-az330.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-t1600-az000.png](235738-fog-fix-2026-11-16-direction-calibration-bf-t1600-az000.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-t1600-az030.png](235738-fog-fix-2026-11-16-direction-calibration-bf-t1600-az030.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-t1600-az060.png](235738-fog-fix-2026-11-16-direction-calibration-bf-t1600-az060.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-t1600-az090.png](235738-fog-fix-2026-11-16-direction-calibration-bf-t1600-az090.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-t1600-az120.png](235738-fog-fix-2026-11-16-direction-calibration-bf-t1600-az120.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-t1600-az150.png](235738-fog-fix-2026-11-16-direction-calibration-bf-t1600-az150.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-t1600-az180.png](235738-fog-fix-2026-11-16-direction-calibration-bf-t1600-az180.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-t1600-az210.png](235738-fog-fix-2026-11-16-direction-calibration-bf-t1600-az210.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-t1600-az240.png](235738-fog-fix-2026-11-16-direction-calibration-bf-t1600-az240.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-t1600-az270.png](235738-fog-fix-2026-11-16-direction-calibration-bf-t1600-az270.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-t1600-az300.png](235738-fog-fix-2026-11-16-direction-calibration-bf-t1600-az300.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-t1600-az330.png](235738-fog-fix-2026-11-16-direction-calibration-bf-t1600-az330.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-t1630-az000.png](235738-fog-fix-2026-11-16-direction-calibration-bf-t1630-az000.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-t1630-az030.png](235738-fog-fix-2026-11-16-direction-calibration-bf-t1630-az030.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-t1630-az060.png](235738-fog-fix-2026-11-16-direction-calibration-bf-t1630-az060.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-t1630-az090.png](235738-fog-fix-2026-11-16-direction-calibration-bf-t1630-az090.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-t1630-az120.png](235738-fog-fix-2026-11-16-direction-calibration-bf-t1630-az120.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-t1630-az150.png](235738-fog-fix-2026-11-16-direction-calibration-bf-t1630-az150.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-t1630-az180.png](235738-fog-fix-2026-11-16-direction-calibration-bf-t1630-az180.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-t1630-az210.png](235738-fog-fix-2026-11-16-direction-calibration-bf-t1630-az210.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-t1630-az240.png](235738-fog-fix-2026-11-16-direction-calibration-bf-t1630-az240.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-t1630-az270.png](235738-fog-fix-2026-11-16-direction-calibration-bf-t1630-az270.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-t1630-az300.png](235738-fog-fix-2026-11-16-direction-calibration-bf-t1630-az300.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-t1630-az330.png](235738-fog-fix-2026-11-16-direction-calibration-bf-t1630-az330.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-t1800-az000.png](235738-fog-fix-2026-11-16-direction-calibration-bf-t1800-az000.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-t1800-az030.png](235738-fog-fix-2026-11-16-direction-calibration-bf-t1800-az030.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-t1800-az060.png](235738-fog-fix-2026-11-16-direction-calibration-bf-t1800-az060.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-t1800-az090.png](235738-fog-fix-2026-11-16-direction-calibration-bf-t1800-az090.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-t1800-az120.png](235738-fog-fix-2026-11-16-direction-calibration-bf-t1800-az120.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-t1800-az150.png](235738-fog-fix-2026-11-16-direction-calibration-bf-t1800-az150.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-t1800-az180.png](235738-fog-fix-2026-11-16-direction-calibration-bf-t1800-az180.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-t1800-az210.png](235738-fog-fix-2026-11-16-direction-calibration-bf-t1800-az210.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-t1800-az240.png](235738-fog-fix-2026-11-16-direction-calibration-bf-t1800-az240.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-t1800-az270.png](235738-fog-fix-2026-11-16-direction-calibration-bf-t1800-az270.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-t1800-az300.png](235738-fog-fix-2026-11-16-direction-calibration-bf-t1800-az300.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-bf-t1800-az330.png](235738-fog-fix-2026-11-16-direction-calibration-bf-t1800-az330.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1630-az000.png](235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1630-az000.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1630-az030.png](235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1630-az030.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1630-az060.png](235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1630-az060.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1630-az090.png](235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1630-az090.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1630-az120.png](235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1630-az120.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1630-az150.png](235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1630-az150.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1630-az180.png](235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1630-az180.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1630-az210.png](235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1630-az210.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1630-az240.png](235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1630-az240.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1630-az270.png](235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1630-az270.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1630-az300.png](235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1630-az300.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1630-az330.png](235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1630-az330.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1715-az000.png](235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1715-az000.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1715-az030.png](235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1715-az030.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1715-az060.png](235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1715-az060.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1715-az090.png](235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1715-az090.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1715-az120.png](235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1715-az120.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1715-az150.png](235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1715-az150.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1715-az180.png](235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1715-az180.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1715-az210.png](235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1715-az210.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1715-az240.png](235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1715-az240.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1715-az270.png](235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1715-az270.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1715-az300.png](235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1715-az300.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1715-az330.png](235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1715-az330.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1740-az000.png](235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1740-az000.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1740-az030.png](235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1740-az030.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1740-az060.png](235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1740-az060.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1740-az090.png](235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1740-az090.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1740-az120.png](235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1740-az120.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1740-az150.png](235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1740-az150.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1740-az180.png](235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1740-az180.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1740-az210.png](235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1740-az210.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1740-az240.png](235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1740-az240.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1740-az270.png](235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1740-az270.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1740-az300.png](235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1740-az300.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1740-az330.png](235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1740-az330.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1800-az000.png](235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1800-az000.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1800-az030.png](235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1800-az030.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1800-az060.png](235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1800-az060.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1800-az090.png](235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1800-az090.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1800-az120.png](235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1800-az120.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1800-az150.png](235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1800-az150.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1800-az180.png](235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1800-az180.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1800-az210.png](235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1800-az210.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1800-az240.png](235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1800-az240.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1800-az270.png](235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1800-az270.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1800-az300.png](235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1800-az300.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1800-az330.png](235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1800-az330.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1810-az000.png](235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1810-az000.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1810-az030.png](235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1810-az030.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1810-az060.png](235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1810-az060.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1810-az090.png](235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1810-az090.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1810-az120.png](235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1810-az120.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1810-az150.png](235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1810-az150.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1810-az180.png](235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1810-az180.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1810-az210.png](235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1810-az210.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1810-az240.png](235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1810-az240.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1810-az270.png](235738-fog-fix-2026-11-16-direction-calibration-tf-auto-t1810-az270.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-grey-0.2.png](235738-fog-fix-2026-11-16-direction-calibration-tf-grey-0.2.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-grey-0.4.png](235738-fog-fix-2026-11-16-direction-calibration-tf-grey-0.4.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-grey-0.6.png](235738-fog-fix-2026-11-16-direction-calibration-tf-grey-0.6.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-grey-0.8.png](235738-fog-fix-2026-11-16-direction-calibration-tf-grey-0.8.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-grey-1.0.png](235738-fog-fix-2026-11-16-direction-calibration-tf-grey-1.0.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-grey-1.2.png](235738-fog-fix-2026-11-16-direction-calibration-tf-grey-1.2.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-grey-1.5.png](235738-fog-fix-2026-11-16-direction-calibration-tf-grey-1.5.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-grey-2.0.png](235738-fog-fix-2026-11-16-direction-calibration-tf-grey-2.0.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-grey-2.5.png](235738-fog-fix-2026-11-16-direction-calibration-tf-grey-2.5.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-t1630-az000.png](235738-fog-fix-2026-11-16-direction-calibration-tf-t1630-az000.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-t1630-az030.png](235738-fog-fix-2026-11-16-direction-calibration-tf-t1630-az030.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-t1630-az060.png](235738-fog-fix-2026-11-16-direction-calibration-tf-t1630-az060.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-t1630-az090.png](235738-fog-fix-2026-11-16-direction-calibration-tf-t1630-az090.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-t1630-az120.png](235738-fog-fix-2026-11-16-direction-calibration-tf-t1630-az120.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-t1630-az150.png](235738-fog-fix-2026-11-16-direction-calibration-tf-t1630-az150.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-t1630-az180.png](235738-fog-fix-2026-11-16-direction-calibration-tf-t1630-az180.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-t1630-az210.png](235738-fog-fix-2026-11-16-direction-calibration-tf-t1630-az210.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-t1630-az240.png](235738-fog-fix-2026-11-16-direction-calibration-tf-t1630-az240.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-t1630-az270.png](235738-fog-fix-2026-11-16-direction-calibration-tf-t1630-az270.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-t1630-az300.png](235738-fog-fix-2026-11-16-direction-calibration-tf-t1630-az300.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-t1630-az330.png](235738-fog-fix-2026-11-16-direction-calibration-tf-t1630-az330.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-t1715-az000.png](235738-fog-fix-2026-11-16-direction-calibration-tf-t1715-az000.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-t1715-az030.png](235738-fog-fix-2026-11-16-direction-calibration-tf-t1715-az030.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-t1715-az060.png](235738-fog-fix-2026-11-16-direction-calibration-tf-t1715-az060.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-t1715-az090.png](235738-fog-fix-2026-11-16-direction-calibration-tf-t1715-az090.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-t1715-az120.png](235738-fog-fix-2026-11-16-direction-calibration-tf-t1715-az120.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-t1715-az150.png](235738-fog-fix-2026-11-16-direction-calibration-tf-t1715-az150.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-t1715-az180.png](235738-fog-fix-2026-11-16-direction-calibration-tf-t1715-az180.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-t1715-az210.png](235738-fog-fix-2026-11-16-direction-calibration-tf-t1715-az210.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-t1715-az240.png](235738-fog-fix-2026-11-16-direction-calibration-tf-t1715-az240.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-t1715-az270.png](235738-fog-fix-2026-11-16-direction-calibration-tf-t1715-az270.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-t1715-az300.png](235738-fog-fix-2026-11-16-direction-calibration-tf-t1715-az300.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-t1715-az330.png](235738-fog-fix-2026-11-16-direction-calibration-tf-t1715-az330.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-t1740-az000.png](235738-fog-fix-2026-11-16-direction-calibration-tf-t1740-az000.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-t1740-az030.png](235738-fog-fix-2026-11-16-direction-calibration-tf-t1740-az030.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-t1740-az060.png](235738-fog-fix-2026-11-16-direction-calibration-tf-t1740-az060.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-t1740-az090.png](235738-fog-fix-2026-11-16-direction-calibration-tf-t1740-az090.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-t1740-az120.png](235738-fog-fix-2026-11-16-direction-calibration-tf-t1740-az120.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-t1740-az150.png](235738-fog-fix-2026-11-16-direction-calibration-tf-t1740-az150.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-t1740-az180.png](235738-fog-fix-2026-11-16-direction-calibration-tf-t1740-az180.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-t1740-az210.png](235738-fog-fix-2026-11-16-direction-calibration-tf-t1740-az210.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-t1740-az240.png](235738-fog-fix-2026-11-16-direction-calibration-tf-t1740-az240.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-t1740-az270.png](235738-fog-fix-2026-11-16-direction-calibration-tf-t1740-az270.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-t1740-az300.png](235738-fog-fix-2026-11-16-direction-calibration-tf-t1740-az300.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-t1740-az330.png](235738-fog-fix-2026-11-16-direction-calibration-tf-t1740-az330.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-t1800-az000.png](235738-fog-fix-2026-11-16-direction-calibration-tf-t1800-az000.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-t1800-az030.png](235738-fog-fix-2026-11-16-direction-calibration-tf-t1800-az030.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-t1800-az060.png](235738-fog-fix-2026-11-16-direction-calibration-tf-t1800-az060.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-t1800-az090.png](235738-fog-fix-2026-11-16-direction-calibration-tf-t1800-az090.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-t1800-az120.png](235738-fog-fix-2026-11-16-direction-calibration-tf-t1800-az120.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-t1800-az150.png](235738-fog-fix-2026-11-16-direction-calibration-tf-t1800-az150.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-t1800-az180.png](235738-fog-fix-2026-11-16-direction-calibration-tf-t1800-az180.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-t1800-az210.png](235738-fog-fix-2026-11-16-direction-calibration-tf-t1800-az210.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-t1800-az240.png](235738-fog-fix-2026-11-16-direction-calibration-tf-t1800-az240.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-t1800-az270.png](235738-fog-fix-2026-11-16-direction-calibration-tf-t1800-az270.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-t1800-az300.png](235738-fog-fix-2026-11-16-direction-calibration-tf-t1800-az300.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-t1800-az330.png](235738-fog-fix-2026-11-16-direction-calibration-tf-t1800-az330.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-t1810-az000.png](235738-fog-fix-2026-11-16-direction-calibration-tf-t1810-az000.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-t1810-az030.png](235738-fog-fix-2026-11-16-direction-calibration-tf-t1810-az030.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-t1810-az060.png](235738-fog-fix-2026-11-16-direction-calibration-tf-t1810-az060.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-t1810-az090.png](235738-fog-fix-2026-11-16-direction-calibration-tf-t1810-az090.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-t1810-az120.png](235738-fog-fix-2026-11-16-direction-calibration-tf-t1810-az120.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-t1810-az150.png](235738-fog-fix-2026-11-16-direction-calibration-tf-t1810-az150.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-t1810-az180.png](235738-fog-fix-2026-11-16-direction-calibration-tf-t1810-az180.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-t1810-az210.png](235738-fog-fix-2026-11-16-direction-calibration-tf-t1810-az210.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-t1810-az240.png](235738-fog-fix-2026-11-16-direction-calibration-tf-t1810-az240.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-t1810-az270.png](235738-fog-fix-2026-11-16-direction-calibration-tf-t1810-az270.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-t1810-az300.png](235738-fog-fix-2026-11-16-direction-calibration-tf-t1810-az300.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-direction-calibration-tf-t1810-az330.png](235738-fog-fix-2026-11-16-direction-calibration-tf-t1810-az330.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-pairs-bf-high-12km-after.png](235738-fog-fix-2026-11-16-pairs-bf-high-12km-after.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-pairs-bf-high-12km-before.png](235738-fog-fix-2026-11-16-pairs-bf-high-12km-before.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-pairs-bf-high-2km-after.png](235738-fog-fix-2026-11-16-pairs-bf-high-2km-after.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-pairs-bf-high-2km-before.png](235738-fog-fix-2026-11-16-pairs-bf-high-2km-before.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-pairs-bf-high-unlimited-after.png](235738-fog-fix-2026-11-16-pairs-bf-high-unlimited-after.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-pairs-bf-high-unlimited-before.png](235738-fog-fix-2026-11-16-pairs-bf-high-unlimited-before.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-pairs-bf-low-8km-after.png](235738-fog-fix-2026-11-16-pairs-bf-low-8km-after.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-pairs-bf-low-8km-away-from-sun-after.png](235738-fog-fix-2026-11-16-pairs-bf-low-8km-away-from-sun-after.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-pairs-bf-low-8km-away-from-sun-before.png](235738-fog-fix-2026-11-16-pairs-bf-low-8km-away-from-sun-before.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-pairs-bf-low-8km-before.png](235738-fog-fix-2026-11-16-pairs-bf-low-8km-before.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-pairs-bf-low-8km-toward-sun-after.png](235738-fog-fix-2026-11-16-pairs-bf-low-8km-toward-sun-after.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-pairs-bf-low-8km-toward-sun-before.png](235738-fog-fix-2026-11-16-pairs-bf-low-8km-toward-sun-before.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-pairs-bf-medium-30km-after.png](235738-fog-fix-2026-11-16-pairs-bf-medium-30km-after.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-pairs-bf-medium-30km-before.png](235738-fog-fix-2026-11-16-pairs-bf-medium-30km-before.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-pairs-bf-mist-12km-after.png](235738-fog-fix-2026-11-16-pairs-bf-mist-12km-after.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-pairs-bf-mist-12km-before.png](235738-fog-fix-2026-11-16-pairs-bf-mist-12km-before.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-pairs-bf-rain-12km-after.png](235738-fog-fix-2026-11-16-pairs-bf-rain-12km-after.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-pairs-bf-rain-12km-before.png](235738-fog-fix-2026-11-16-pairs-bf-rain-12km-before.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-pairs-bf-sunset-12km-after.png](235738-fog-fix-2026-11-16-pairs-bf-sunset-12km-after.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-pairs-bf-sunset-12km-away-from-sun-after.png](235738-fog-fix-2026-11-16-pairs-bf-sunset-12km-away-from-sun-after.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-pairs-bf-sunset-12km-away-from-sun-before.png](235738-fog-fix-2026-11-16-pairs-bf-sunset-12km-away-from-sun-before.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-pairs-bf-sunset-12km-before.png](235738-fog-fix-2026-11-16-pairs-bf-sunset-12km-before.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-pairs-bf-sunset-12km-toward-sun-after.png](235738-fog-fix-2026-11-16-pairs-bf-sunset-12km-toward-sun-after.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-pairs-bf-sunset-12km-toward-sun-before.png](235738-fog-fix-2026-11-16-pairs-bf-sunset-12km-toward-sun-before.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-pairs-bf-sunset-2km-after.png](235738-fog-fix-2026-11-16-pairs-bf-sunset-2km-after.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-pairs-bf-sunset-2km-before.png](235738-fog-fix-2026-11-16-pairs-bf-sunset-2km-before.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-pairs-tf-high-12km-after.png](235738-fog-fix-2026-11-16-pairs-tf-high-12km-after.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-pairs-tf-high-12km-before.png](235738-fog-fix-2026-11-16-pairs-tf-high-12km-before.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-pairs-tf-high-2km-after.png](235738-fog-fix-2026-11-16-pairs-tf-high-2km-after.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-pairs-tf-high-2km-before.png](235738-fog-fix-2026-11-16-pairs-tf-high-2km-before.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-pairs-tf-high-unlimited-after.png](235738-fog-fix-2026-11-16-pairs-tf-high-unlimited-after.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-pairs-tf-high-unlimited-before.png](235738-fog-fix-2026-11-16-pairs-tf-high-unlimited-before.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-pairs-tf-low-8km-after.png](235738-fog-fix-2026-11-16-pairs-tf-low-8km-after.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-pairs-tf-low-8km-before.png](235738-fog-fix-2026-11-16-pairs-tf-low-8km-before.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-pairs-tf-medium-30km-after.png](235738-fog-fix-2026-11-16-pairs-tf-medium-30km-after.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-pairs-tf-medium-30km-before.png](235738-fog-fix-2026-11-16-pairs-tf-medium-30km-before.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-pairs-tf-mist-12km-after.png](235738-fog-fix-2026-11-16-pairs-tf-mist-12km-after.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-pairs-tf-mist-12km-before.png](235738-fog-fix-2026-11-16-pairs-tf-mist-12km-before.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-pairs-tf-rain-12km-after.png](235738-fog-fix-2026-11-16-pairs-tf-rain-12km-after.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-pairs-tf-rain-12km-before.png](235738-fog-fix-2026-11-16-pairs-tf-rain-12km-before.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-pairs-tf-sunset-12km-after.png](235738-fog-fix-2026-11-16-pairs-tf-sunset-12km-after.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-pairs-tf-sunset-12km-before.png](235738-fog-fix-2026-11-16-pairs-tf-sunset-12km-before.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-pairs-tf-sunset-2km-after.png](235738-fog-fix-2026-11-16-pairs-tf-sunset-2km-after.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-pairs-tf-sunset-2km-away-from-sun-after.png](235738-fog-fix-2026-11-16-pairs-tf-sunset-2km-away-from-sun-after.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-pairs-tf-sunset-2km-away-from-sun-before.png](235738-fog-fix-2026-11-16-pairs-tf-sunset-2km-away-from-sun-before.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-pairs-tf-sunset-2km-before.png](235738-fog-fix-2026-11-16-pairs-tf-sunset-2km-before.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-pairs-tf-sunset-2km-toward-sun-after.png](235738-fog-fix-2026-11-16-pairs-tf-sunset-2km-toward-sun-after.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-pairs-tf-sunset-2km-toward-sun-before.png](235738-fog-fix-2026-11-16-pairs-tf-sunset-2km-toward-sun-before.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-pairs-tf-sunset-8km-away-from-sun-after.png](235738-fog-fix-2026-11-16-pairs-tf-sunset-8km-away-from-sun-after.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-pairs-tf-sunset-8km-away-from-sun-before.png](235738-fog-fix-2026-11-16-pairs-tf-sunset-8km-away-from-sun-before.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-pairs-tf-sunset-8km-toward-sun-after.png](235738-fog-fix-2026-11-16-pairs-tf-sunset-8km-toward-sun-after.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-pairs-tf-sunset-8km-toward-sun-before.png](235738-fog-fix-2026-11-16-pairs-tf-sunset-8km-toward-sun-before.png) |
| 23:57:38 | [235738-fog-fix-2026-11-16-tf-high-12km-before-after.jpg](235738-fog-fix-2026-11-16-tf-high-12km-before-after.jpg) |
| 23:57:38 | [235738-fog-fix-2026-11-16-tf-high-2km-before-after.jpg](235738-fog-fix-2026-11-16-tf-high-2km-before-after.jpg) |
| 23:57:38 | [235738-fog-fix-2026-11-16-tf-high-unlimited-before-after.jpg](235738-fog-fix-2026-11-16-tf-high-unlimited-before-after.jpg) |
| 23:57:38 | [235738-fog-fix-2026-11-16-tf-low-8km-before-after.jpg](235738-fog-fix-2026-11-16-tf-low-8km-before-after.jpg) |
| 23:57:38 | [235738-fog-fix-2026-11-16-tf-medium-30km-before-after.jpg](235738-fog-fix-2026-11-16-tf-medium-30km-before-after.jpg) |
| 23:57:38 | [235738-fog-fix-2026-11-16-tf-mist-12km-before-after.jpg](235738-fog-fix-2026-11-16-tf-mist-12km-before-after.jpg) |
| 23:57:38 | [235738-fog-fix-2026-11-16-tf-rain-12km-before-after.jpg](235738-fog-fix-2026-11-16-tf-rain-12km-before-after.jpg) |
| 23:57:38 | [235738-fog-fix-2026-11-16-tf-sunset-12km-before-after.jpg](235738-fog-fix-2026-11-16-tf-sunset-12km-before-after.jpg) |
| 23:57:38 | [235738-fog-fix-2026-11-16-tf-sunset-2km-away-from-sun-before-after.jpg](235738-fog-fix-2026-11-16-tf-sunset-2km-away-from-sun-before-after.jpg) |
| 23:57:38 | [235738-fog-fix-2026-11-16-tf-sunset-2km-before-after.jpg](235738-fog-fix-2026-11-16-tf-sunset-2km-before-after.jpg) |
| 23:57:38 | [235738-fog-fix-2026-11-16-tf-sunset-2km-toward-sun-before-after.jpg](235738-fog-fix-2026-11-16-tf-sunset-2km-toward-sun-before-after.jpg) |
| 23:57:38 | [235738-fog-fix-2026-11-16-tf-sunset-8km-away-from-sun-before-after.jpg](235738-fog-fix-2026-11-16-tf-sunset-8km-away-from-sun-before-after.jpg) |
| 23:57:38 | [235738-fog-fix-2026-11-16-tf-sunset-8km-toward-sun-before-after.jpg](235738-fog-fix-2026-11-16-tf-sunset-8km-toward-sun-before-after.jpg) |
| 23:57:39 | [235739-fog-fix-2026-11-16-direction-calibration-tf-auto-t1810-az300.png](235739-fog-fix-2026-11-16-direction-calibration-tf-auto-t1810-az300.png) |
| 23:57:39 | [235739-fog-fix-2026-11-16-direction-calibration-tf-auto-t1810-az330.png](235739-fog-fix-2026-11-16-direction-calibration-tf-auto-t1810-az330.png) |
