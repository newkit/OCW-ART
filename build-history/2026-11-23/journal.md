# OCW build diary – day 13, 2026-11-23

64 commits (17 merges), +23954 / −1814 lines, 827 images, 11 videos, 0 sounds.

## Commits

| Time | Commit | |
|---|---|---|
| 08:44 | `4ad62fdb` | Season jumps to the nearest representative day, the calendar sets the day at once; worlds without marked seasons offer only the jumps that change something (spec Phase 9 Q13 (a), Q14 (a)) |
| 09:21 | `dcb87d05` | Season page checks whether the place has seasons: weak in Tenerife (one line, Summer and Winter only), all six in Liechtenstein and the Black Forest; no leaf fall from Tenerife's evergreen woods (spec Phase 9 Q13) |
| 09:52 | `5adfcd42` (merge) | Merge the season check: places with weak seasons (e.g. Tenerife) say so and offer only summer and winter, evergreen woods shed almost no leaves (spec Phase 9 Q13, 5.42) |
| 10:24 | `0c296af5` | Street lamps mapped in OSM stand where mapped (moved beside the road when on it, the rows skip them); every lamp pole is an obstacle; point obstacles collide with their files' col_* proxies (world look Street lamps, Phase 12 K3, 15H / 15N) |
| 10:24 | `19e2aea3` (merge) | Merge remote-tracking branch 'origin/main' into worktree-agent-a765cbc595ec59a84 |
| 10:27 | `f006581a` | Street lamps: list the tiles with mapped lamps in world-builder street-lamps, Schaan and Santa Cruz scenes, the rebuilt packages' numbers (spec 5.43) |
| 10:59 | `ade1978a` | Trees keep their leaf state at every distance (a see-through crown of twigs on bare trees, the same thinning crowns near and far); the junction fan is off in Unicorn mode and back when riding (spec 4.6.1 Fixed v5.42, 2.2.1, 5.42) |
| 11:04 | `ea3eb92f` (merge) | Merge street lamps from OSM lamp nodes and lamp poles as obstacles, obstacle shapes from the props files' collision proxies (spec Street lamps, K3, 15N; 5.43) |
| 11:30 | `06d85426` (merge) | Merge the tree LOD fix (near and far crowns follow one rule, bare trees keep a see-through twig crown) and the junction fan hidden in flight (5.44) |
| 11:45 | `9e0d8469` | OCW Studio Models workspace edits (E4): the model document with undo, gizmo, points, proxies in both forms, slots and materials, metadata, fixes, save with the model diff first, re-import (spec 16B, 16F E4; 5.44) |
| 11:50 | `a4d0f04e` | Phones draw at pixel ratio 1.5, start at the page's size and keep the world only along their course: the iPhone's tab memory cut by a quarter to a half (spec 14 Phase 10 B7, B2) |
| 11:53 | `81f4abd9` | Models E4: re-import sets the canonical generator as model import does; the Blender round trip picture; ONLY= for the shots script (spec 16B; 5.44) |
| 11:57 | `bba21c4f` | Phones: the world's driver takes the options the app set (the course cut and residency reached the decode only on the app side) |
| 12:32 | `ab990042` | The memory mode is applied to the world's options in one place, before the page hands them to the driver (regression test for the course cut that never reached the decode) |
| 12:36 | `078570dc` (merge) | Merge OCW Studio E4: editing models in the Models workspace (gizmo, rename/re-parent, anchors, proxies in both forms, paint slots, materials, metadata, validator fixes, diff before save, Blender re-import, all undoable; 5.45) |
| 12:40 | `375a21d5` | A phone's land use is indexed with the course's tiles only: no copy of the whole section first (Tenerife: 75 MB less at the start) |
| 12:43 | `07b46dce` | Built: the unicorn's wing beat, gallop, flight and landing play in OCW Studio's Models viewer from the game's animation; OSM street lamps rebuilt into the middle and south Black Forest packages (5.45) |
| 12:55 | `fcdb5d1d` | Studio: rustfmt the flight cycles' header line |
| 13:01 | `a2ada226` | Spec 5.42: the iPhone's memory – phones at pixel ratio 1.5, the world along the course, the guard and the death steps, measured per world (14 Phase 10 B7, B2 10G) |
| 13:02 | `e8fd6ab4` (merge) | Merge iPhone browser memory cuts: page-size first frame, pixel ratio 1.5 on WebKit phones, small phone shadow maps, 1280x720 photos, one tile meshed at a time, the course cut of the world base, a memory guard and stepwise fallback (5.46) |
| 13:48 | `ab7fb492` (merge) | Merge OSM street lamps for Black Forest middle and south (lamps-build) and the unicorn's flight cycles in OCW Studio's Models viewer (5.47) |
| 13:50 | `a73daf50` | Plant files fixed in the generator before their Blender sources: shading scaled to at most 1 with shade_scale, leaf normals on the front side (Phase 15 Q11 (a), 5.48) |
| 13:55 | `94767ce8` | Off the road every slope is ridden at its real gradient, the trainer caps its resistance anyway (Phase 13 Q7 (b), 5.49) |
| 13:56 | `2775d720` | The unicorn lands anywhere on land except water, buildings and obstacles; on the route in events and fixed routes (Phase 13 Q8 (a), 5.50) |
| 13:56 | `d7681321` | Riding off the road counts like any riding: FIT distance, elevation, time and the real GPS track, hearts by work (Phase 13 Q9 (a), 5.51) |
| 14:02 | `ffe319ae` | Junction profile tools for spec 4.8.8 Q6 (d) / Q7: side-road profiles of two packages, slope charts, fixed-camera shots |
| 14:27 | `a67ff35b` | Junction kinks smoothed: creases rounded and never above the main road, blended junctions smoothed, light terrain smoothing (4.8.8 Q7 (d), 5.52) |
| 14:47 | `f5455606` | Phase 13A off-road riding, stage 1: the ground map, 2D riding on the terrain in the session, landing anywhere in free ride |
| 15:21 | `d526dc9a` | Phase 13A off-road riding, stage 2: prediction, client, landing ring, spec (v5.52) |
| 15:50 | `a17760b0` | Plant files survive Blender: vertex colours kept at most 1 with extras.ocw.shade_scale, every leaf triangle with its normals on its front; the 108 plant files re-exported (spec 15G Q11 (a), 15P, v5.47) |
| 15:50 | `fc78507a` (merge) | Merge Phase 13A: riding off the road after a unicorn landing – land anywhere on land (red ring on water, buildings, obstacles), real gradients, the FIT track and hearts off-road, rejoining roads (5.53) |
| 15:55 | `4ec7834f` | Built: junction kinks smoothed (4.8.8 Q7 (d)) – creases rounded, side roads never above the main road, blended junctions on one plane, light terrain smoothing; packages rebuilt into data/j4-build (5.53) |
| 16:38 | `cb69a327` (merge) | Merge plant files that survive Blender: shading scaled to at most 1 with shade_scale, leaf normals on their own front; 108 of 108 plant files unchanged in the round trip (Phase 15 Q11 (a), 5.54) |
| 16:54 | `2023f700` | Fix the flaky heap trace test: frame 2 follows a 256 MiB allocation, far above the parallel tests' noise |
| 17:24 | `5eba81ea` | Rule: the sides of a road are as smooth as the road – side bands follow the rounded corners and the smoothed profile, no gap, hole or lip (4.8.8 Rule, 5.55) |
| 17:27 | `c45e59fd` | WIP: J4 follow-up (never above main, junction_room guard, corner verges) |
| 17:28 | `28819586` (merge) | Merge remote-tracking branch 'origin/main' into worktree-agent-a26ac3f82bbda79f8 |
| 17:50 | `1dd2ce82` | J4 follow-up: never above the main road (mesh refined and cut, strips under it near the carriageway), creases and planes never make a road steeper (junction_room below J3), corner verges meet the arms' verges, lint side.* (4.8.8 Q7, Rule; 5.56) |
| 18:08 | `7013fc71` (merge) | Merge J4: junction kinks smoothed (creases rounded where there is room, blended junctions on a plane), side roads cut below the main road, junction_room below J3, light terrain smoothing, lint side.*; packages in j4-build, not installed (4.8.8 Q7 (d), 5.56) |
| 18:08 | `9968b832` | Plant shade scale test: allow one 1/1000 step between the generator and the shipped file (the Mac's fused multiply-adds round 1.025 vs 1.026) |
| 19:14 | `386bbb8b` | J5 WIP: junction sides follow the edge lines with rounded corners, mouth rows lean with the main road / blended plane, sides smoothed along the outline, lint side.* measured against the surface's slope (4.8.8 Rule) |
| 19:47 | `0c952ede` | Off the road every drawn tree is an obstacle, trunks made on demand near the rider (Phase 13 Q10 (a)) |
| 19:53 | `faec1699` | J5: the sides of a junction follow their roads – outlines along the real edge lines with rounded corners leaving each mouth along its strip, mouth rows leaning with the main road or the blended plane and turning flat past the mouth, the sides' heights smoothed along the outline, corner verges as wide as the ground asks (no wall), strips without folds at the mouth; lint side.* measured against the surface's slope (4.8.8 Rule) |
| 19:53 | `0164808d` | Collision proxies: a modelled mesh or a scaled unit empty, both kept (Phase 15 Q9 (a)) |
| 20:00 | `fe764355` | Plants re-exported with their lowest point at the stem base, held props marked held (Phase 15 Q10 (a)) |
| 20:00 | `0222ac2b` | Unicorn and rider files survive Blender: cones to one tip, lips and mouth inside smoothed by corner angle; make test-blender 221 of 221 (Phase 15 Q11 follow-up, 15P, 5.57) |
| 20:01 | `6320e4bc` (merge) | Merge main (Phase 15 Q10 (a) decided) |
| 20:14 | `7acacdd8` | J5: clippy (side lift loops, VertexRule kept in an Arc), the lint test of the sloping plane dropped (it passes on J4 too), the shots and charts scripts for J5 (4.8.8 Rule) |
| 20:23 | `2b89c5f9` | J5: clippy type aliases in the side lint |
| 20:51 | `0860b539` | Street lamp poles as obstacles in the browser too (streamed tiles near the rider, dropped with them); the first ride's hints apart on a phone (spec 12 K3, 3.2.3; 5.57) |
| 20:53 | `d797f262` | Built: off the road every drawn tree is an obstacle – trunks made on demand near riders deep in a wood from the trees the renderer draws; a crash at speed, a stop at walking pace (Phase 13 Q10 (a), 5.58) |
| 20:54 | `99c7d2fe` | J5: a corner's verge keeps near the arms' widths at its ends (no notch beside the arm's verge) |
| 21:36 | `150c93d8` | Woods on the server: the trees baked per tile at load (37 MB for the northern Black Forest instead of 310 MB of inputs), radii in whole millimetres on every path; scenes in an inner wood (Phase 13 Q10) |
| 21:42 | `2971aee0` | Built: the sides of a road are as smooth as the road (4.8.8 Rule, J5) – spec with the J5 packages' lint (side.corner halved, side.kink 7 – 10 % fewer, not at 0: short arms, non-star chains, steep junctions), charts with the J5 package (v5.57) |
| 21:48 | `384aa115` | Browser lamp bump: the local server's contacts in netStats, dev.lamp coasting at 0 W in test-web-ios; the Android layout cases with element full screen; spec 5.57 numbers |
| 21:55 | `c0895277` | J5: fmt |
| 21:58 | `7020bbdb` | Q10 scenes in a dense wood of the northern Black Forest (runs of 4 and 9 m at a trunk); woods_bench finds runs inside the wood |
| 21:58 | `269e12dd` (merge) | Merge Phase 13 Q10 (a): off the road every drawn tree is an obstacle – trunks made per 40 m cell around off-road riders, the same trees as drawn, baked per tile on the server (5.60) |
| 22:03 | `cf7552ac` (merge) | Merge J5: road sides follow the road – corner outlines along the real road edges with rounded corners, tilted mouth rows, verges as wide as the drop, side.* lint measured against the surface slope; packages in j5-build, not installed (4.8.8 Rule, 5.61) |
| 22:44 | `ec048655` | Plants stand on their stem base, held props marked held: the origin warning clean on every model file (Phase 15 Q10 (a), 5.61) |
| 22:47 | `55b60864` (merge) | Merge every model file survives Blender (unicorn ears and horn as cones, lips with corner-angle normals; 221 of 221) and every model stands on its origin (Phase 15 Q10 (a)) (5.62, 5.63) |
| 22:48 | `f18e33e8` (merge) | Merge origin/main (woods Q10 (a), J5) into the browser lamp poles / phone hints branch; spec row renumbered 5.64 |
| 23:56 | `890b6e2c` | Browser lamp poles only while the own rider is in wild mode (dropped back on the road): Liechtenstein with main's woods 439.8 MB peak (main 444.8); spec 5.64 numbers |
| 23:57 | `7d15976d` (merge) | Merge lamp poles as obstacles in the browser (ring around a wild rider) and the phone layout without overlaps (K3, 3.2.3; 5.64) |

## Builds and build servers

342 build/test runs on the build machines, 49.6 h in total, 5 failed; 1440 server samples; cargo compiled 22414 crates in 8.5 h, 8.7 h waiting for build slots.

| Machine | Runs | Hours | Cargo h | Crates | Waited h | Failed | Online |
|---|---|---|---|---|---|---|---|
| Weela | 0 | 0.0 | 0.0 | 0 | 0.0 | 0 | 0% |
| Win11Builder | 4 | 0.6 | 0.5 | 52 | 0.0 | 0 | 100% |
| leela | 55 | 7.1 | 2.1 | 8340 | 0.8 | 2 | 100% |
| macos | 42 | 1.5 | 0.2 | 40 | 0.0 | 0 | 100% |
| marge | 241 | 40.4 | 5.6 | 13982 | 7.9 | 3 | 100% |

Failed runs:

- 13:02 leela: `make check && make test-web-build && make test-smoke && make test-web-webkit && ` (exit 2, log `build-log/130226-leela-1419206.log`)
- 14:58 marge: `for f in ~/src/OCW/data/j3-build/pilot/liechtenstein.ocwpkg ~/j4/iter1/pilot/lie` (exit 1, log `build-log/145802-marge-1699918.log`)
- 16:38 leela: `make check && make test-web-build && make test-smoke && cargo run -q -p ocw-asse` (exit 2, log `build-log/163848-leela-1897130.log`)
- 23:32 marge: `cargo build --release -p ocw-worldgen --example above_probe 2>&1 | grep -E "^err` (exit 1, log `build-log/233228-marge-2866955.log`)
- 23:44 marge: `scripts/j6-build.sh 2>&1` (exit 143, log `build-log/234402-marge-2887568.log`)

Longest runs:

- 107 min on marge: `scripts/j5-build.sh 2>&1`
- 66 min on marge: `make web >/dev/null 2>&1 || echo WEB-BUILD-FAILED; scripts/test-web-webkit.py --`
- 53 min on marge: `make check && make test-web-build && make test-smoke && echo ALL-CHECKS-OK`
- 49 min on marge: `scripts/j4-build.sh > ~/src/OCW/data/j4-build/build.log 2>&1; echo done`
- 48 min on marge: `make check && make test-smoke`

## Token usage

1.36 B tokens in 4,165 model messages (output 2.7 M, cache reads 1.33 B, cache writes 25.3 M, uncached input 9 k). Full breakdown: [tokens.json](tokens.json).

| Feature | Tokens | Output | Messages |
|---|---|---|---|
| Planning & spec | 485.3 M | 877 k | 1,476 |
| Other | 326.4 M | 681 k | 962 |
| Worlds & terrain | 217.0 M | 480 k | 562 |
| Riders & bikes | 117.0 M | 293 k | 437 |
| Materials & look | 109.0 M | 131 k | 317 |
| Sky, time & weather | 35.3 M | 81 k | 150 |
| Build, release & infra | 34.5 M | 74 k | 148 |
| Art project | 20.1 M | 47 k | 95 |
| UI & menus | 17.0 M | 8 k | 18 |

| Task | Feature | Tokens | Output |
|---|---|---|---|
| agent: iPhone: cut browser memory drastically | Planning & spec | 172.9 M | 241 k |
| agent: Smooth road sides rule: corners and mouths | Other | 147.5 M | 302 k |
| agent: J3 Q7 (d): smooth kinks, terrain, rebuild | Worlds & terrain | 139.1 M | 311 k |
| agent: J6: verge V-notch and remaining side faults | Other | 110.4 M | 241 k |
| agent: Phase 13A: ride off the road after landing | Planning & spec | 90.8 M | 190 k |
| agent: Phase 13 Q10: trees as obstacles off-road | Planning & spec | 87.9 M | 186 k |
| agent: Browser: lamp obstacles + phone overlap | Planning & spec | 74.1 M | 145 k |
| agent: Fix bald trees on approach, unicorn shadow | Materials & look | 72.9 M | 124 k |
| agent: OCW Studio E4: Models workspace editing | Riders & bikes | 57.6 M | 169 k |
| agent: OSM lamps, lamps and props as obstacles | Worlds & terrain | 57.3 M | 145 k |
| agent: Unicorn head and rider lip survive Blender | Riders & bikes | 53.5 M | 121 k |
| agent: Plant files survive Blender (Q11 a) | Planning & spec | 45.6 M | 102 k |
| coordination: i see the ingame graphics realy qquick, like a coiple of ms and then it restart | Materials & look | 36.0 M | 6 k |
| coordination: yes, (a) | Other | 30.9 M | 27 k |
| agent: Season check for worlds without seasons | Sky, time & weather | 29.8 M | 78 k |
| agent: Pictures: Q6 side-road mouths and creases | Other | 20.3 M | 77 k |
| agent: Day 12 video (22 Nov), art README | Art project | 20.1 M | 47 k |
| agent: BF lamps rebuild + Studio unicorn cycles | Build, release & infra | 18.3 M | 56 k |
| coordination: i noticed some flickering of the road turn hud, at least in unicorn mode. tuen i… | UI & menus | 17.0 M | 8 k |
| coordination: q6: the crease fix of making the road longer and more equal is good. make sure t… | Worlds & terrain | 16.8 M | 23 k |
| coordination: can you make a rule in woeld building that smoothens the sides, too? | Build, release & infra | 11.7 M | 14 k |
| coordination: is the a feature in spec file waiting for developement that we could start? | Planning & spec | 6.5 M | 3 k |
| coordination: show me a foto of the face of the rider | Riders & bikes | 5.9 M | 2 k |
| coordination: what are next steps to be implemented | Other | 5.5 M | 14 k |
| coordination: Answer to open questions: **Phase 9 – Sky, Time, Seasons and Weather** - **Phase… | Sky, time & weather | 5.5 M | 4 k |
| coordination: the mobile browser version still crashes, on safari I have seen the blue hint bo… | Build, release & infra | 4.6 M | 4 k |
| coordination: q9 (a) | Other | 4.2 M | 8 k |
| coordination: do what you recommend: start 2 and 3 together now. They make the world more soli… | Worlds & terrain | 3.7 M | 2 k |
| coordination: in the meantime, give ma another open question | Planning & spec | 3.0 M | 5 k |
| coordination: yes, (a). next question | Planning & spec | 2.9 M | 3 k |
| coordination: there is a bug recently intoduced: the trees turn bald (without leaves) all of a… | Other | 2.8 M | 2 k |
| coordination: show me en example of what you did with Q6 qnd what you did with the creases | Other | 2.7 M | 6 k |
| coordination: give me one open question | Planning & spec | 859 k | 2 k |
| coordination: answer: yes, (a) | Other | 736 k | 1 k |
| coordination: give me an open question | Planning & spec | 716 k | 1 k |
| coordination: (b), i guess the trainer will cap at somepoint anyway | Other | 692 k | 2 k |
| coordination: q8 (a) | Other | 465 k | 1 k |
| coordination: give me another quest | Other | 229 k | 0 k |

## Prompts

22 prompts (full text: [prompts.md](prompts.md)).

| Time | Prompt |
|---|---|
| 08:43 | Answer to open questions:  **Phase 9 – Sky, Time, Seasons and Weather**  - **Phase 9 Q13 – The seasons' representative days:** on World → Ti |
| 08:51 | the mobile browser version still crashes, on safari I have seen the blue hint box that it's maybe memory related |
| 08:55 | is the a feature in spec file waiting for developement that we could start? |
| 09:24 | do what you recommend: start 2 and 3 together now. They make the world more solid and don't collide with the iPhone work. E4 is the bigger n |
| 09:35 | there is a bug recently intoduced: the trees turn bald (without leaves) all of a sudden when gertting closer. Also there seems a dark big sp |
| 09:36 | i noticed some flickering of the road turn hud, at least in unicorn mode. tuen it there off completely and reenable when riding again |
| 11:06 | show me a foto of the face of the rider |
| 11:15 | what are next steps to be implemented |
| 13:18 | give me one open question |
| 13:22 | show me en example of what you did with Q6 qnd what you did with the creases |
| 13:45 | in the meantime, give ma another open question |
| 13:50 | yes, (a) |
| 13:53 | give me another quest |
| 13:55 | (b), i guess the trainer will cap at somepoint anyway |
| 13:56 | q8 (a) |
| 13:56 | q9 (a) |
| 14:25 | q6: the crease fix of making the road longer and more equal is good. make sure the side road does not stick out of the main road. better smo |
| 17:24 | can you make a rule in woeld building that smoothens the sides, too? |
| 19:45 | give me an open question |
| 19:47 | yes, (a). next question |
| 19:53 | answer: yes, (a) |
| 20:00 | yes, (a) |

## Features

24 spec versions added, 14 landed by a merge; 6 deploys, 0 releases.

| Spec | Feature | Landed | Check (marge) |
|---|---|---|---|
| 5.41 | Season jumps go to the nearest representative day, the calendar keeps setting the day at… | 08:44 `4ad62fdb` | – |
| 5.42 | The Season page checks whether the world's place has seasons | 09:52 `5adfcd42` (merge) | ok at 09:22 (commit) |
| 5.43 | Built: street lamps mapped in OSM stand where they are mapped, and every street lamp's po… | 11:04 `ea3eb92f` (merge) | ok at 11:45, 1 suites, 77 passed, 0 failed (commit) |
| 5.44 | Fixed: trees no longer turn bald when coming closer | 11:30 `06d85426` (merge) | ok at 11:30, 74 suites, 3227 passed, 0 failed (commit) |
| 5.45 | Built: oCW Studio edits model files | 12:36 `078570dc` (merge) | ok at 12:36, 74 suites, 3247 passed, 0 failed (commit) |
| 5.46 | Fixed: the browser app dying on an iPhone in every ride, the test routes too | 13:02 `e8fd6ab4` (merge) | ok at 14:03, 7 suites, 203 passed, 1 failed (commit) |
| 5.47 | Built: the unicorn's wing beat, gallop, flight and landing play in OCW Studio's Models vi… | 13:48 `ab7fb492` (merge) | ok at 13:48, 74 suites, 3258 passed, 0 failed (commit) |
| 5.48 | Plant files are fixed in the generator before their Blender sources are made | 13:50 `a73daf50` | – |
| 5.49 | Off the road after a unicorn landing every slope is ridden at its real gradient, however… | 13:55 `94767ce8` | – |
| 5.50 | The unicorn lands anywhere on land inside the world's tiles | 13:56 `2775d720` | – |
| 5.51 | Riding off the road counts like any riding | 13:56 `d7681321` | – |
| 5.52 | Junction kinks smoothed | 14:27 `a67ff35b` | – |
| 5.53 | Built: riding off the road after a unicorn landing | 15:50 `fc78507a` (merge) | ok at 15:50, 74 suites, 3284 passed, 0 failed (commit) |
| 5.54 | Built: the plant files survive Blender | 16:38 `cb69a327` (merge) | ok at 15:50 (commit) |
| 5.55 | Rule: the sides of a road are as smooth as the road | 17:24 `5eba81ea` | – |
| 5.56 | Built: junction kinks smoothed | 18:08 `7013fc71` (merge) | ok at 18:08, 74 suites, 3302 passed, 0 failed (commit) |
| 5.57 | Off the road every drawn tree is an obstacle | 19:47 `0c952ede` | – |
| 5.58 | A collision proxy col_* may be a modelled mesh or a scaled unit empty | 19:53 `0164808d` | – |
| 5.59 | Plants re-exported with their lowest point at the stem base, held props marked extras.ocw… | 20:00 `fe764355` | – |
| 5.60 | Built: off the road every drawn tree is an obstacle | 21:58 `269e12dd` (merge) | ok at 21:58, 75 suites, 3319 passed, 0 failed (commit) |
| 5.61 | Built: the sides of a road are as smooth as the road | 22:03 `cf7552ac` (merge) | ok at 23:04, 1 suites, 1 passed, 0 failed (commit) |
| 5.62 | Built: every model file survives Blender | 22:47 `55b60864` (merge) | ok at 22:47, 75 suites, 3327 passed, 0 failed (commit) |
| 5.63 | Built: every model file stands on its origin | 22:47 `55b60864` (merge) | ok at 22:47, 75 suites, 3327 passed, 0 failed (commit) |
| 5.64 | Built: street lamp poles are obstacles in the browser too, and a phone's first-ride hints… | 23:57 `7d15976d` (merge) | ok at 22:48 (branch) |

Deploys:

- 12:20 marge: `06d85426` (ok)
- 12:29 leela: `06d85426` (ok)
- 17:22 marge: `5eba81ea` (ok)
- 17:25 leela: `5eba81ea` (ok)
- 23:28 marge: `55b60864` (ok)
- 23:36 leela: `55b60864` (ok)

## Agent jobs

16 jobs (coordinator log agents.jsonl).

| Task | Branch | Start | End | Status | Interrupted | Merged |
|---|---|---|---|---|---|---|
| Day 12 video (2026-11-22) | a825b47a | 00:15 | 00:45 | merged |  |  |
| Season check for worlds without seasons | adb67871 | 08:44 | 09:53 | merged |  |  |
| iPhone: cut browser memory drastically | acbca6f0 | 08:51 | 13:48 | merged |  |  |
| OSM street lamps; lamps and props as obstacles from proxies | a765cbc5 | 09:25 | 11:05 | merged |  |  |
| Fix bald trees on approach, unicorn ground spot | a318b069 | 09:35 | 12:20 | merged |  |  |
| OCW Studio E4: Models workspace editing | a6f5aa9d | 11:06 | 13:22 | merged |  |  |
| Black Forest lamps rebuild; unicorn cycles in Studio viewer | aa8b8382 | 12:20 | 14:21 | merged |  |  |
| Pictures: Q6 side-road mouths and Q7 creases | acb0f792 | 13:23 | 14:27 | merged |  |  |
| Plant files survive Blender (Phase 15 Q11 a) | a11958fe | 13:50 | 17:22 | merged |  |  |
| Phase 13A: ride off the road after a unicorn landing | aecca951 | 14:21 | 16:44 | merged |  |  |
| Junction kinks Q7 (d), terrain smoothing, rebuild all packages | a26ac3f8 | 14:27 | 18:34 | merged |  |  |
| Rule: smooth road sides – junction corners and mouths (J5) | a3769047 | 18:34 | 22:51 | merged |  |  |
| Browser: lamp poles as obstacles, phone layout overlap | aa2305c7 | 19:19 | 23:56 | reported |  |  |
| Unicorn head and rider lip normals survive Blender | a8c5ac48 | 19:19 | 23:28 | merged |  |  |
| Phase 13 Q10: every drawn tree an obstacle off the road | afa3443c | 19:49 | 22:51 | merged |  |  |
| J6: verge V-notch, above-main 0, remaining side faults | adeca704 | 22:04 |  | started |  |  |

## Incidents

44 collected (disk-full 1, janitor-delete 37, machine-offline 2, machine-online 1, runs-failed 1, unit-failed 2), 0 with root-cause notes ([incidents.md](incidents.md)).

| Time | Kind | Machine | What |
|---|---|---|---|
| 00:00 | machine-offline | Weela | Weela unreachable (no route to host) |
| 00:00 | disk-full | Win11Builder | disk C: on Win11Builder at 97 % |
| 09:51 | janitor-delete | leela | janitor delete OCW-worktree-agent-adb67871eba1f1dad/target (12.6 GB) |
| 09:51 | janitor-delete | marge | janitor delete OCW-worktree-agent-adb67871eba1f1dad/target (31.8 GB) |
| 09:51 | janitor-delete | macos | janitor delete OCW-worktree-agent-adb67871eba1f1dad/target (0.0 GB) |
| 11:04 | janitor-delete | marge | janitor delete OCW-worktree-agent-a765cbc595ec59a84/target (43.4 GB) |
| 12:19 | janitor-delete | marge | janitor delete OCW-merge-treelod/target (26.7 GB) |
| 12:19 | janitor-delete | marge | janitor delete OCW-worktree-agent-a318b069771a80073/target (31.6 GB) |
| 12:19 | janitor-delete | leela | janitor delete OCW-worktree-agent-a318b069771a80073/target (3.2 GB) |
| 12:34 | janitor-delete | macos | janitor delete OCW-worktree-agent-a318b069771a80073/target (7.8 GB) |
| 12:45 | janitor-delete | Win11Builder | janitor delete OCW-worktree-agent-a765cbc595ec59a84/target (2.8 GB) |
| 13:01 | janitor-delete | leela | janitor delete OCW-ios-memory-b3/target (16.7 GB) |
| 13:01 | janitor-delete | marge | janitor delete OCW-ios-memory-b3/target (16.1 GB) |
| 13:21 | janitor-delete | marge | janitor delete OCW-merge-e4/target (27.5 GB) |
| 13:21 | janitor-delete | marge | janitor delete OCW-worktree-agent-a6f5aa9dab2456bee/target (32.7 GB) |
| 13:21 | janitor-delete | leela | janitor delete OCW-worktree-agent-a6f5aa9dab2456bee/target (22.1 GB) |
| 13:24 | janitor-delete | macos | janitor delete OCW-worktree-agent-a6f5aa9dab2456bee/target (1.5 GB) |
| 13:46 | janitor-delete | leela | janitor delete OCW-merge-ios/target (32.2 GB) |
| 13:47 | janitor-delete | marge | janitor delete OCW-ios-memory-phone/target (48.2 GB) |
| 14:20 | janitor-delete | marge | janitor delete OCW-merge-unicycles/target (27.0 GB) |
| 14:20 | janitor-delete | marge | janitor delete OCW-worktree-agent-aa8b83829082695f0/target (30.8 GB) |
| 14:45 | janitor-delete | macos | janitor delete OCW-worktree-agent-aa8b83829082695f0/target (6.1 GB) |
| 16:43 | janitor-delete | marge | janitor delete OCW-worktree-agent-aecca951247987cc1/target (28.4 GB) |
| 17:06 | unit-failed | deb | ocw-art-collect.service failed (exit-code) |
| 17:21 | janitor-delete | leela | janitor delete OCW-merge-q11/target (31.2 GB) |
| 17:21 | janitor-delete | marge | janitor delete OCW-merge-13a/target (27.0 GB) |
| 17:21 | janitor-delete | marge | janitor delete OCW-worktree-agent-a11958feda96480f3/target (40.5 GB) |
| 18:33 | janitor-delete | marge | janitor delete OCW-merge-j4/target (27.1 GB) |
| 18:33 | janitor-delete | marge | janitor delete OCW-worktree-agent-a26ac3f82bbda79f8/target (39.7 GB) |
| 18:33 | janitor-delete | marge | janitor delete OCW-worktree-agent-acb0f792245e83954/target (4.2 GB) |
| 19:49 | janitor-delete | macos | janitor delete OCW-worktree-agent-a26ac3f82bbda79f8/target (8.9 GB) |
| 20:00 | janitor-delete | Win11Builder | janitor delete OCW-worktree-agent-aecca951247987cc1/target (2.4 GB) |
| 21:04 | machine-offline | Win11Builder | Win11Builder unreachable (ssh error) |
| 21:05 | machine-online | Win11Builder | Win11Builder back online |
| 22:00 | janitor-delete | marge | janitor delete OCW/target (19.0 GB) |
| 22:49 | janitor-delete | marge | janitor delete OCW-merge-q10/target (27.3 GB) |
| 22:49 | janitor-delete | leela | janitor delete OCW-merge-j5/target (27.4 GB) |
| 22:49 | janitor-delete | marge | janitor delete OCW-worktree-agent-afa3443cd1461751c/target (42.0 GB) |
| 22:49 | janitor-delete | leela | janitor delete OCW-worktree-agent-afa3443cd1461751c/target (20.9 GB) |
| 22:49 | janitor-delete | marge | janitor delete OCW-worktree-agent-a376904757b84bfd9/target (38.6 GB) |
| 23:08 | unit-failed | deb | ocw-art-collect.service failed (exit-code) |
| 23:26 | janitor-delete | marge | janitor delete OCW-merge-batch/target (28.2 GB) |
| 23:26 | janitor-delete | marge | janitor delete OCW-worktree-agent-a8c5ac4818f5d30e5/target (39.7 GB) |
| 23:44 | runs-failed | leela, marge | 5 failed remote.sh runs (leela 2, marge 3) |

## Media

| Time | File |
|---|---|
| 09:08:20 | [090820-web-ios-phone-baseline-loop-local-1min.png](090820-web-ios-phone-baseline-loop-local-1min.png) |
| 09:08:20 | [090820-web-ios-phone-baseline-loop-local-end.png](090820-web-ios-phone-baseline-loop-local-end.png) |
| 09:08:20 | [090820-web-ios-phone-baseline-loop-local-start.png](090820-web-ios-phone-baseline-loop-local-start.png) |
| 09:10:03 | [091003-web-ios-phone-baseline-loop-live-1min.png](091003-web-ios-phone-baseline-loop-live-1min.png) |
| 09:10:03 | [091003-web-ios-phone-baseline-loop-live-end.png](091003-web-ios-phone-baseline-loop-live-end.png) |
| 09:10:03 | [091003-web-ios-phone-baseline-loop-live-start.png](091003-web-ios-phone-baseline-loop-live-start.png) |
| 09:11:18 | [091118-shot-wayland-season-weak-page-tenerife-coast.jpg](091118-shot-wayland-season-weak-page-tenerife-coast.jpg) |
| 09:11:33 | [091133-shot-wayland-season-weak-page-tenerife-canadas.jpg](091133-shot-wayland-season-weak-page-tenerife-canadas.jpg) |
| 09:11:43 | [091143-shot-wayland-season-weak-page-liechtenstein.jpg](091143-shot-wayland-season-weak-page-liechtenstein.jpg) |
| 09:12:03 | [091203-shot-wayland-season-weak-tenerife-coast-november.jpg](091203-shot-wayland-season-weak-tenerife-coast-november.jpg) |
| 09:12:24 | [091224-shot-wayland-season-weak-tenerife-coast-july.jpg](091224-shot-wayland-season-weak-tenerife-coast-july.jpg) |
| 09:51:03 | [095103-shot-ocw.jpg](095103-shot-ocw.jpg) |
| 09:51:12 | [095112-shot-wayland-ocw-wayland.jpg](095112-shot-wayland-ocw-wayland.jpg) |
| 09:52:46 | [095246-web-ios-phone-step-b2-loop-1min.png](095246-web-ios-phone-step-b2-loop-1min.png) |
| 09:52:46 | [095246-web-ios-phone-step-b2-loop-end.png](095246-web-ios-phone-step-b2-loop-end.png) |
| 09:52:46 | [095246-web-ios-phone-step-b2-loop-start.png](095246-web-ios-phone-step-b2-loop-start.png) |
| 09:55:23 | [095523-web-ios-phone-step-b2-hills-1min.png](095523-web-ios-phone-step-b2-hills-1min.png) |
| 09:55:23 | [095523-web-ios-phone-step-b2-hills-2min.png](095523-web-ios-phone-step-b2-hills-2min.png) |
| 09:55:23 | [095523-web-ios-phone-step-b2-hills-3min.png](095523-web-ios-phone-step-b2-hills-3min.png) |
| 09:55:23 | [095523-web-ios-phone-step-b2-hills-4min.png](095523-web-ios-phone-step-b2-hills-4min.png) |
| 09:55:23 | [095523-web-ios-phone-step-b2-hills-5min.png](095523-web-ios-phone-step-b2-hills-5min.png) |
| 09:55:23 | [095523-web-ios-phone-step-b2-hills-context-reloaded.png](095523-web-ios-phone-step-b2-hills-context-reloaded.png) |
| 09:55:23 | [095523-web-ios-phone-step-b2-hills-end.png](095523-web-ios-phone-step-b2-hills-end.png) |
| 09:55:23 | [095523-web-ios-phone-step-b2-hills-start.png](095523-web-ios-phone-step-b2-hills-start.png) |
| 09:55:39 | [095539-tree-lod-ov-east-before.jpg](095539-tree-lod-ov-east-before.jpg) |
| 09:55:52 | [095552-tree-lod-ov-north-before.jpg](095552-tree-lod-ov-north-before.jpg) |
| 09:56:05 | [095605-tree-lod-ov-unicorn-low-before.jpg](095605-tree-lod-ov-unicorn-low-before.jpg) |
| 09:56:18 | [095618-tree-lod-ov-unicorn-high-before.jpg](095618-tree-lod-ov-unicorn-high-before.jpg) |
| 10:01:19 | [100119-web-ios-phone-step-b2-liechtenstein-1min.png](100119-web-ios-phone-step-b2-liechtenstein-1min.png) |
| 10:01:19 | [100119-web-ios-phone-step-b2-liechtenstein-2min.png](100119-web-ios-phone-step-b2-liechtenstein-2min.png) |
| 10:01:19 | [100119-web-ios-phone-step-b2-liechtenstein-3min.png](100119-web-ios-phone-step-b2-liechtenstein-3min.png) |
| 10:01:19 | [100119-web-ios-phone-step-b2-liechtenstein-4min.png](100119-web-ios-phone-step-b2-liechtenstein-4min.png) |
| 10:01:19 | [100119-web-ios-phone-step-b2-liechtenstein-5min.png](100119-web-ios-phone-step-b2-liechtenstein-5min.png) |
| 10:01:19 | [100119-web-ios-phone-step-b2-liechtenstein-context-reloaded.png](100119-web-ios-phone-step-b2-liechtenstein-context-reloaded.png) |
| 10:01:19 | [100119-web-ios-phone-step-b2-liechtenstein-end.png](100119-web-ios-phone-step-b2-liechtenstein-end.png) |
| 10:01:19 | [100119-web-ios-phone-step-b2-liechtenstein-start.png](100119-web-ios-phone-step-b2-liechtenstein-start.png) |
| 10:07:22 | [100722-web-ios-phone-step-b2-tenerife-1min.png](100722-web-ios-phone-step-b2-tenerife-1min.png) |
| 10:07:22 | [100722-web-ios-phone-step-b2-tenerife-2min.png](100722-web-ios-phone-step-b2-tenerife-2min.png) |
| 10:07:22 | [100722-web-ios-phone-step-b2-tenerife-3min.png](100722-web-ios-phone-step-b2-tenerife-3min.png) |
| 10:07:22 | [100722-web-ios-phone-step-b2-tenerife-4min.png](100722-web-ios-phone-step-b2-tenerife-4min.png) |
| 10:07:22 | [100722-web-ios-phone-step-b2-tenerife-5min.png](100722-web-ios-phone-step-b2-tenerife-5min.png) |
| 10:07:22 | [100722-web-ios-phone-step-b2-tenerife-context-reloaded.png](100722-web-ios-phone-step-b2-tenerife-context-reloaded.png) |
| 10:07:22 | [100722-web-ios-phone-step-b2-tenerife-end.png](100722-web-ios-phone-step-b2-tenerife-end.png) |
| 10:07:22 | [100722-web-ios-phone-step-b2-tenerife-start.png](100722-web-ios-phone-step-b2-tenerife-start.png) |
| 10:08:40 | [100840-tree-lod-map-top-before.jpg](100840-tree-lod-map-top-before.jpg) |
| 10:08:52 | [100852-tree-lod-uni-plane-15m-nov-before.jpg](100852-tree-lod-uni-plane-15m-nov-before.jpg) |
| 10:09:05 | [100905-tree-lod-uni-plane-40m-nov-before.jpg](100905-tree-lod-uni-plane-40m-nov-before.jpg) |
| 10:09:18 | [100918-tree-lod-uni-plane-150m-nov-before.jpg](100918-tree-lod-uni-plane-150m-nov-before.jpg) |
| 10:09:31 | [100931-tree-lod-uni-plane-15m-jul-before.jpg](100931-tree-lod-uni-plane-15m-jul-before.jpg) |
| 10:09:43 | [100943-tree-lod-uni-hover-4m-nov-before.jpg](100943-tree-lod-uni-hover-4m-nov-before.jpg) |
| 10:10:20 | [101020-tree-lod-uni-down-10m-before.jpg](101020-tree-lod-uni-down-10m-before.jpg) |
| 10:10:33 | [101033-tree-lod-uni-down-30m-before.jpg](101033-tree-lod-uni-down-30m-before.jpg) |
| 10:10:45 | [101045-tree-lod-uni-down-80m-before.jpg](101045-tree-lod-uni-down-80m-before.jpg) |
| 10:10:58 | [101058-tree-lod-uni-down-200m-before.jpg](101058-tree-lod-uni-down-200m-before.jpg) |
| 10:11:11 | [101111-tree-lod-uni-plane-down-60m-before.jpg](101111-tree-lod-uni-plane-down-60m-before.jpg) |
| 10:12:10 | [101210-tree-lod-uni-low-q-15m-before.jpg](101210-tree-lod-uni-low-q-15m-before.jpg) |
| 10:12:23 | [101223-tree-lod-uni-low-q-40m-before.jpg](101223-tree-lod-uni-low-q-40m-before.jpg) |
| 10:12:35 | [101235-tree-lod-uni-low-q-100m-before.jpg](101235-tree-lod-uni-low-q-100m-before.jpg) |
| 10:12:48 | [101248-tree-lod-uni-med-q-40m-before.jpg](101248-tree-lod-uni-med-q-40m-before.jpg) |
| 10:13:01 | [101301-tree-lod-uni-high-q-40m-before.jpg](101301-tree-lod-uni-high-q-40m-before.jpg) |
| 10:13:36 | [101336-web-ios-phone-step-b2-black-forest-north-1min.png](101336-web-ios-phone-step-b2-black-forest-north-1min.png) |
| 10:13:36 | [101336-web-ios-phone-step-b2-black-forest-north-2min.png](101336-web-ios-phone-step-b2-black-forest-north-2min.png) |
| 10:13:36 | [101336-web-ios-phone-step-b2-black-forest-north-3min.png](101336-web-ios-phone-step-b2-black-forest-north-3min.png) |
| 10:13:36 | [101336-web-ios-phone-step-b2-black-forest-north-4min.png](101336-web-ios-phone-step-b2-black-forest-north-4min.png) |
| 10:13:36 | [101336-web-ios-phone-step-b2-black-forest-north-5min.png](101336-web-ios-phone-step-b2-black-forest-north-5min.png) |
| 10:13:36 | [101336-web-ios-phone-step-b2-black-forest-north-context-reloaded.png](101336-web-ios-phone-step-b2-black-forest-north-context-reloaded.png) |
| 10:13:36 | [101336-web-ios-phone-step-b2-black-forest-north-end.png](101336-web-ios-phone-step-b2-black-forest-north-end.png) |
| 10:13:36 | [101336-web-ios-phone-step-b2-black-forest-north-start.png](101336-web-ios-phone-step-b2-black-forest-north-start.png) |
| 10:13:45 | [101345-tree-lod-uni-gd-nov-30m-before.jpg](101345-tree-lod-uni-gd-nov-30m-before.jpg) |
| 10:13:58 | [101358-tree-lod-uni-gd-nov-30m-gdoff-before.jpg](101358-tree-lod-uni-gd-nov-30m-gdoff-before.jpg) |
| 10:14:11 | [101411-tree-lod-uni-gd-jul-30m-before.jpg](101411-tree-lod-uni-gd-jul-30m-before.jpg) |
| 10:14:24 | [101424-tree-lod-uni-gd-nov-70m-before.jpg](101424-tree-lod-uni-gd-nov-70m-before.jpg) |
| 10:15:29 | [101529-tree-lod-uni-field-jul-120m-before.jpg](101529-tree-lod-uni-field-jul-120m-before.jpg) |
| 10:15:42 | [101542-tree-lod-uni-field-jul-300m-before.jpg](101542-tree-lod-uni-field-jul-300m-before.jpg) |
| 10:15:54 | [101554-tree-lod-uni-field-nov-120m-before.jpg](101554-tree-lod-uni-field-nov-120m-before.jpg) |
| 10:16:07 | [101607-tree-lod-uni-field-nov-40m-before.jpg](101607-tree-lod-uni-field-nov-40m-before.jpg) |
| 10:17:06 | [101706-tree-lod-uni-now-plane-20m-before.jpg](101706-tree-lod-uni-now-plane-20m-before.jpg) |
| 10:17:19 | [101719-tree-lod-uni-now-plane-60m-before.jpg](101719-tree-lod-uni-now-plane-60m-before.jpg) |
| 10:17:31 | [101731-tree-lod-uni-now-hover-25m-before.jpg](101731-tree-lod-uni-now-hover-25m-before.jpg) |
| 10:17:44 | [101744-tree-lod-uni-now-auto-25m-before.jpg](101744-tree-lod-uni-now-auto-25m-before.jpg) |
| 10:19:48 | [101948-tree-lod-li-wood-2026-11-23-600m-before.jpg](101948-tree-lod-li-wood-2026-11-23-600m-before.jpg) |
| 10:20:01 | [102001-tree-lod-li-wood-2026-11-23-330m-before.jpg](102001-tree-lod-li-wood-2026-11-23-330m-before.jpg) |
| 10:20:14 | [102014-tree-lod-li-wood-2026-11-23-250m-before.jpg](102014-tree-lod-li-wood-2026-11-23-250m-before.jpg) |
| 10:20:26 | [102026-tree-lod-li-wood-2026-11-23-150m-before.jpg](102026-tree-lod-li-wood-2026-11-23-150m-before.jpg) |
| 10:20:39 | [102039-tree-lod-li-wood-2026-11-23-60m-before.jpg](102039-tree-lod-li-wood-2026-11-23-60m-before.jpg) |
| 10:21:05 | [102105-osm-lamps-vaduz-night-wide-wayland.jpg](102105-osm-lamps-vaduz-night-wide-wayland.jpg) |
| 10:21:57 | [102157-osm-lamps-santacruz-night-wide-wayland.jpg](102157-osm-lamps-santacruz-night-wide-wayland.jpg) |
| 10:22:11 | [102211-osm-lamps-vaduz-lamp-bump-wayland.jpg](102211-osm-lamps-vaduz-lamp-bump-wayland.jpg) |
| 10:24:01 | [102401-tree-lod-li-wood-2026-11-23-600m-after.jpg](102401-tree-lod-li-wood-2026-11-23-600m-after.jpg) |
| 10:24:14 | [102414-tree-lod-li-wood-2026-11-23-330m-after.jpg](102414-tree-lod-li-wood-2026-11-23-330m-after.jpg) |
| 10:24:27 | [102427-tree-lod-li-wood-2026-11-23-250m-after.jpg](102427-tree-lod-li-wood-2026-11-23-250m-after.jpg) |
| 10:24:41 | [102441-tree-lod-li-wood-2026-11-23-150m-after.jpg](102441-tree-lod-li-wood-2026-11-23-150m-after.jpg) |
| 10:25:20 | [102520-tree-lod-li-wood-2026-07-15-330m-after.jpg](102520-tree-lod-li-wood-2026-07-15-330m-after.jpg) |
| 10:25:46 | [102546-tree-lod-li-wood-2026-07-15-150m-after.jpg](102546-tree-lod-li-wood-2026-07-15-150m-after.jpg) |
| 10:26:12 | [102612-tree-lod-li-wood-2026-10-28-600m-after.jpg](102612-tree-lod-li-wood-2026-10-28-600m-after.jpg) |
| 10:26:25 | [102625-tree-lod-li-wood-2026-10-28-330m-after.jpg](102625-tree-lod-li-wood-2026-10-28-330m-after.jpg) |
| 10:26:38 | [102638-tree-lod-li-wood-2026-10-28-250m-after.jpg](102638-tree-lod-li-wood-2026-10-28-250m-after.jpg) |
| 10:26:51 | [102651-tree-lod-li-wood-2026-10-28-150m-after.jpg](102651-tree-lod-li-wood-2026-10-28-150m-after.jpg) |
| 10:27:04 | [102704-tree-lod-li-wood-2026-10-28-60m-after.jpg](102704-tree-lod-li-wood-2026-10-28-60m-after.jpg) |
| 10:27:17 | [102717-tree-lod-li-wood-2026-05-10-600m-after.jpg](102717-tree-lod-li-wood-2026-05-10-600m-after.jpg) |
| 10:27:30 | [102730-tree-lod-li-wood-2026-05-10-330m-after.jpg](102730-tree-lod-li-wood-2026-05-10-330m-after.jpg) |
| 10:27:44 | [102744-tree-lod-li-wood-2026-05-10-250m-after.jpg](102744-tree-lod-li-wood-2026-05-10-250m-after.jpg) |
| 10:27:57 | [102757-tree-lod-li-wood-2026-05-10-150m-after.jpg](102757-tree-lod-li-wood-2026-05-10-150m-after.jpg) |
| 10:28:10 | [102810-tree-lod-li-wood-2026-05-10-60m-after.jpg](102810-tree-lod-li-wood-2026-05-10-60m-after.jpg) |
| 10:28:26 | [102826-tree-lod-bf-2026-11-23-n-after.jpg](102826-tree-lod-bf-2026-11-23-n-after.jpg) |
| 10:28:42 | [102842-tree-lod-bf-2026-11-23-s-after.jpg](102842-tree-lod-bf-2026-11-23-s-after.jpg) |
| 10:28:58 | [102858-tree-lod-bf-2026-07-15-n-after.jpg](102858-tree-lod-bf-2026-07-15-n-after.jpg) |
| 10:29:15 | [102915-tree-lod-bf-2026-10-28-n-after.jpg](102915-tree-lod-bf-2026-10-28-n-after.jpg) |
| 10:29:31 | [102931-tree-lod-bf-2026-11-23-n-before.jpg](102931-tree-lod-bf-2026-11-23-n-before.jpg) |
| 10:29:47 | [102947-tree-lod-bf-2026-11-23-s-before.jpg](102947-tree-lod-bf-2026-11-23-s-before.jpg) |
| 10:29:58 | [102958-osm-lamps-vaduz-night-wayland.jpg](102958-osm-lamps-vaduz-night-wayland.jpg) |
| 10:30:03 | [103003-tree-lod-bf-2026-07-15-n-before.jpg](103003-tree-lod-bf-2026-07-15-n-before.jpg) |
| 10:30:18 | [103018-tree-lod-bf-2026-10-28-n-before.jpg](103018-tree-lod-bf-2026-10-28-n-before.jpg) |
| 10:30:24 | [103024-osm-lamps-santacruz-night-wayland.jpg](103024-osm-lamps-santacruz-night-wayland.jpg) |
| 10:30:32 | [103032-tree-lod-li-wood-2026-07-15-600m-before.jpg](103032-tree-lod-li-wood-2026-07-15-600m-before.jpg) |
| 10:30:39 | [103039-osm-lamps-schaan-night-wayland.jpg](103039-osm-lamps-schaan-night-wayland.jpg) |
| 10:30:44 | [103044-tree-lod-li-wood-2026-07-15-330m-before.jpg](103044-tree-lod-li-wood-2026-07-15-330m-before.jpg) |
| 10:30:57 | [103057-tree-lod-li-wood-2026-07-15-250m-before.jpg](103057-tree-lod-li-wood-2026-07-15-250m-before.jpg) |
| 10:31:10 | [103110-tree-lod-li-wood-2026-07-15-150m-before.jpg](103110-tree-lod-li-wood-2026-07-15-150m-before.jpg) |
| 10:31:22 | [103122-tree-lod-li-wood-2026-07-15-60m-before.jpg](103122-tree-lod-li-wood-2026-07-15-60m-before.jpg) |
| 10:31:30 | [103130-osm-lamps-santacruz-mapped-night-wayland.jpg](103130-osm-lamps-santacruz-mapped-night-wayland.jpg) |
| 10:31:35 | [103135-tree-lod-li-wood-2026-10-28-600m-before.jpg](103135-tree-lod-li-wood-2026-10-28-600m-before.jpg) |
| 10:31:48 | [103148-tree-lod-li-wood-2026-10-28-330m-before.jpg](103148-tree-lod-li-wood-2026-10-28-330m-before.jpg) |
| 10:32:01 | [103201-tree-lod-li-wood-2026-10-28-250m-before.jpg](103201-tree-lod-li-wood-2026-10-28-250m-before.jpg) |
| 10:32:13 | [103213-tree-lod-li-wood-2026-10-28-150m-before.jpg](103213-tree-lod-li-wood-2026-10-28-150m-before.jpg) |
| 10:32:26 | [103226-tree-lod-li-wood-2026-10-28-60m-before.jpg](103226-tree-lod-li-wood-2026-10-28-60m-before.jpg) |
| 10:32:39 | [103239-tree-lod-li-wood-2026-05-10-600m-before.jpg](103239-tree-lod-li-wood-2026-05-10-600m-before.jpg) |
| 10:32:51 | [103251-tree-lod-li-wood-2026-05-10-330m-before.jpg](103251-tree-lod-li-wood-2026-05-10-330m-before.jpg) |
| 10:33:04 | [103304-tree-lod-li-wood-2026-05-10-250m-before.jpg](103304-tree-lod-li-wood-2026-05-10-250m-before.jpg) |
| 10:33:17 | [103317-tree-lod-li-wood-2026-05-10-150m-before.jpg](103317-tree-lod-li-wood-2026-05-10-150m-before.jpg) |
| 10:33:30 | [103330-tree-lod-li-wood-2026-05-10-60m-before.jpg](103330-tree-lod-li-wood-2026-05-10-60m-before.jpg) |
| 10:54:17 | [105417-tree-lod-li-wood-2026-07-15-600m-after.jpg](105417-tree-lod-li-wood-2026-07-15-600m-after.jpg) |
| 10:54:30 | [105430-tree-lod-li-wood-2026-07-15-250m-after.jpg](105430-tree-lod-li-wood-2026-07-15-250m-after.jpg) |
| 10:54:43 | [105443-tree-lod-li-wood-2026-07-15-60m-after.jpg](105443-tree-lod-li-wood-2026-07-15-60m-after.jpg) |
| 10:54:56 | [105456-tree-lod-li-wood-2026-11-23-60m-after.jpg](105456-tree-lod-li-wood-2026-11-23-60m-after.jpg) |
| 10:55:29 | [105529-tree-lod-uni-forest-jul-12m-before.jpg](105529-tree-lod-uni-forest-jul-12m-before.jpg) |
| 10:55:41 | [105541-tree-lod-uni-forest-jul-plane-15m-before.jpg](105541-tree-lod-uni-forest-jul-plane-15m-before.jpg) |
| 10:55:54 | [105554-tree-lod-uni-forest-nov-12m-before.jpg](105554-tree-lod-uni-forest-nov-12m-before.jpg) |
| 10:57:30 | [105730-tree-lod-uni-forest-jul-12m-after.jpg](105730-tree-lod-uni-forest-jul-12m-after.jpg) |
| 10:57:43 | [105743-tree-lod-uni-forest-jul-plane-15m-after.jpg](105743-tree-lod-uni-forest-jul-plane-15m-after.jpg) |
| 10:57:56 | [105756-tree-lod-uni-forest-nov-12m-after.jpg](105756-tree-lod-uni-forest-nov-12m-after.jpg) |
| 10:58:15 | [105815-junction-fan-fan-unicorn-before.jpg](105815-junction-fan-fan-unicorn-before.jpg) |
| 10:58:16 | [105816-junction-fan-fan-unicorn-before.mp4](105816-junction-fan-fan-unicorn-before.mp4) |
| 10:58:35 | [105835-junction-fan-fan-unicorn-after.jpg](105835-junction-fan-fan-unicorn-after.jpg) |
| 10:58:37 | [105837-junction-fan-fan-unicorn-after.mp4](105837-junction-fan-fan-unicorn-after.mp4) |
| 11:14:36 | [111436-ea3eb92f-shot-wayland-m3-helmet-road-side.jpg](111436-ea3eb92f-shot-wayland-m3-helmet-road-side.jpg) |
| 11:14:46 | [111446-ea3eb92f-shot-wayland-m3-helmet-road-front.jpg](111446-ea3eb92f-shot-wayland-m3-helmet-road-front.jpg) |
| 11:46:14 | [114614-models-e4-bike-node-gizmo-x11.jpg](114614-models-e4-bike-node-gizmo-x11.jpg) |
| 11:46:28 | [114628-models-e4-bike-node-gizmo-wayland.jpg](114628-models-e4-bike-node-gizmo-wayland.jpg) |
| 11:46:41 | [114641-models-e4-bike-rotate-gizmo-x11.jpg](114641-models-e4-bike-rotate-gizmo-x11.jpg) |
| 11:46:55 | [114655-models-e4-bike-rotate-gizmo-wayland.jpg](114655-models-e4-bike-rotate-gizmo-wayland.jpg) |
| 11:47:08 | [114708-models-e4-bike-scale-gizmo-x11.jpg](114708-models-e4-bike-scale-gizmo-x11.jpg) |
| 11:47:22 | [114722-models-e4-bike-scale-gizmo-wayland.jpg](114722-models-e4-bike-scale-gizmo-wayland.jpg) |
| 11:47:36 | [114736-models-e4-anchor-added-x11.jpg](114736-models-e4-anchor-added-x11.jpg) |
| 11:47:50 | [114750-models-e4-anchor-added-wayland.jpg](114750-models-e4-anchor-added-wayland.jpg) |
| 11:48:03 | [114803-models-e4-proxy-mesh-x11.jpg](114803-models-e4-proxy-mesh-x11.jpg) |
| 11:48:17 | [114817-models-e4-proxy-mesh-wayland.jpg](114817-models-e4-proxy-mesh-wayland.jpg) |
| 11:48:30 | [114830-models-e4-proxy-empty-x11.jpg](114830-models-e4-proxy-empty-x11.jpg) |
| 11:48:45 | [114845-models-e4-proxy-empty-wayland.jpg](114845-models-e4-proxy-empty-wayland.jpg) |
| 11:48:59 | [114859-models-e4-slot-picker-x11.jpg](114859-models-e4-slot-picker-x11.jpg) |
| 11:49:13 | [114913-models-e4-slot-picker-wayland.jpg](114913-models-e4-slot-picker-wayland.jpg) |
| 11:49:27 | [114927-models-e4-diff-before-save-x11.jpg](114927-models-e4-diff-before-save-x11.jpg) |
| 11:49:44 | [114944-models-e4-diff-before-save-wayland.jpg](114944-models-e4-diff-before-save-wayland.jpg) |
| 11:52:52 | [115252-models-e4-blender-reimport-x11.jpg](115252-models-e4-blender-reimport-x11.jpg) |
| 11:53:09 | [115309-models-e4-blender-reimport-wayland.jpg](115309-models-e4-blender-reimport-wayland.jpg) |
| 12:29:12 | [122912-web-ios-phone-after-tenerife-1min.png](122912-web-ios-phone-after-tenerife-1min.png) |
| 12:29:12 | [122912-web-ios-phone-after-tenerife-2min.png](122912-web-ios-phone-after-tenerife-2min.png) |
| 12:29:12 | [122912-web-ios-phone-after-tenerife-3min.png](122912-web-ios-phone-after-tenerife-3min.png) |
| 12:29:12 | [122912-web-ios-phone-after-tenerife-4min.png](122912-web-ios-phone-after-tenerife-4min.png) |
| 12:29:12 | [122912-web-ios-phone-after-tenerife-5min.png](122912-web-ios-phone-after-tenerife-5min.png) |
| 12:29:12 | [122912-web-ios-phone-after-tenerife-context-reloaded.png](122912-web-ios-phone-after-tenerife-context-reloaded.png) |
| 12:29:12 | [122912-web-ios-phone-after-tenerife-end.png](122912-web-ios-phone-after-tenerife-end.png) |
| 12:29:12 | [122912-web-ios-phone-after-tenerife-start.png](122912-web-ios-phone-after-tenerife-start.png) |
| 12:35:22 | [123522-web-ios-phone-after-black-forest-north-1min.png](123522-web-ios-phone-after-black-forest-north-1min.png) |
| 12:35:22 | [123522-web-ios-phone-after-black-forest-north-2min.png](123522-web-ios-phone-after-black-forest-north-2min.png) |
| 12:35:22 | [123522-web-ios-phone-after-black-forest-north-3min.png](123522-web-ios-phone-after-black-forest-north-3min.png) |
| 12:35:22 | [123522-web-ios-phone-after-black-forest-north-4min.png](123522-web-ios-phone-after-black-forest-north-4min.png) |
| 12:35:22 | [123522-web-ios-phone-after-black-forest-north-5min.png](123522-web-ios-phone-after-black-forest-north-5min.png) |
| 12:35:22 | [123522-web-ios-phone-after-black-forest-north-context-lost-again.png](123522-web-ios-phone-after-black-forest-north-context-lost-again.png) |
| 12:35:22 | [123522-web-ios-phone-after-black-forest-north-context-reloaded.png](123522-web-ios-phone-after-black-forest-north-context-reloaded.png) |
| 12:35:22 | [123522-web-ios-phone-after-black-forest-north-end.png](123522-web-ios-phone-after-black-forest-north-end.png) |
| 12:35:22 | [123522-web-ios-phone-after-black-forest-north-start.png](123522-web-ios-phone-after-black-forest-north-start.png) |
| 12:40:48 | [124048-web-ios-phone-after-b9-tenerife-1min.png](124048-web-ios-phone-after-b9-tenerife-1min.png) |
| 12:40:48 | [124048-web-ios-phone-after-b9-tenerife-2min.png](124048-web-ios-phone-after-b9-tenerife-2min.png) |
| 12:40:48 | [124048-web-ios-phone-after-b9-tenerife-3min.png](124048-web-ios-phone-after-b9-tenerife-3min.png) |
| 12:40:48 | [124048-web-ios-phone-after-b9-tenerife-4min.png](124048-web-ios-phone-after-b9-tenerife-4min.png) |
| 12:40:48 | [124048-web-ios-phone-after-b9-tenerife-5min.png](124048-web-ios-phone-after-b9-tenerife-5min.png) |
| 12:40:48 | [124048-web-ios-phone-after-b9-tenerife-context-reloaded.png](124048-web-ios-phone-after-b9-tenerife-context-reloaded.png) |
| 12:40:48 | [124048-web-ios-phone-after-b9-tenerife-end.png](124048-web-ios-phone-after-b9-tenerife-end.png) |
| 12:40:48 | [124048-web-ios-phone-after-b9-tenerife-start.png](124048-web-ios-phone-after-b9-tenerife-start.png) |
| 12:41:33 | [124133-web-ios-phone-after-liechtenstein-1min.png](124133-web-ios-phone-after-liechtenstein-1min.png) |
| 12:41:33 | [124133-web-ios-phone-after-liechtenstein-2min.png](124133-web-ios-phone-after-liechtenstein-2min.png) |
| 12:41:33 | [124133-web-ios-phone-after-liechtenstein-3min.png](124133-web-ios-phone-after-liechtenstein-3min.png) |
| 12:41:33 | [124133-web-ios-phone-after-liechtenstein-4min.png](124133-web-ios-phone-after-liechtenstein-4min.png) |
| 12:41:33 | [124133-web-ios-phone-after-liechtenstein-5min.png](124133-web-ios-phone-after-liechtenstein-5min.png) |
| 12:41:33 | [124133-web-ios-phone-after-liechtenstein-context-reloaded.png](124133-web-ios-phone-after-liechtenstein-context-reloaded.png) |
| 12:41:33 | [124133-web-ios-phone-after-liechtenstein-end.png](124133-web-ios-phone-after-liechtenstein-end.png) |
| 12:41:33 | [124133-web-ios-phone-after-liechtenstein-start.png](124133-web-ios-phone-after-liechtenstein-start.png) |
| 12:47:04 | [124704-web-ios-phone-after-b9-black-forest-north-1min.png](124704-web-ios-phone-after-b9-black-forest-north-1min.png) |
| 12:47:04 | [124704-web-ios-phone-after-b9-black-forest-north-2min.png](124704-web-ios-phone-after-b9-black-forest-north-2min.png) |
| 12:47:04 | [124704-web-ios-phone-after-b9-black-forest-north-3min.png](124704-web-ios-phone-after-b9-black-forest-north-3min.png) |
| 12:47:04 | [124704-web-ios-phone-after-b9-black-forest-north-4min.png](124704-web-ios-phone-after-b9-black-forest-north-4min.png) |
| 12:47:04 | [124704-web-ios-phone-after-b9-black-forest-north-5min.png](124704-web-ios-phone-after-b9-black-forest-north-5min.png) |
| 12:47:04 | [124704-web-ios-phone-after-b9-black-forest-north-context-reloaded.png](124704-web-ios-phone-after-b9-black-forest-north-context-reloaded.png) |
| 12:47:04 | [124704-web-ios-phone-after-b9-black-forest-north-end.png](124704-web-ios-phone-after-b9-black-forest-north-end.png) |
| 12:47:04 | [124704-web-ios-phone-after-b9-black-forest-north-start.png](124704-web-ios-phone-after-b9-black-forest-north-start.png) |
| 12:47:43 | [124743-web-ios-phone-after-hills-1min.png](124743-web-ios-phone-after-hills-1min.png) |
| 12:47:43 | [124743-web-ios-phone-after-hills-2min.png](124743-web-ios-phone-after-hills-2min.png) |
| 12:47:43 | [124743-web-ios-phone-after-hills-3min.png](124743-web-ios-phone-after-hills-3min.png) |
| 12:47:43 | [124743-web-ios-phone-after-hills-4min.png](124743-web-ios-phone-after-hills-4min.png) |
| 12:47:43 | [124743-web-ios-phone-after-hills-5min.png](124743-web-ios-phone-after-hills-5min.png) |
| 12:47:43 | [124743-web-ios-phone-after-hills-context-reloaded.png](124743-web-ios-phone-after-hills-context-reloaded.png) |
| 12:47:43 | [124743-web-ios-phone-after-hills-end.png](124743-web-ios-phone-after-hills-end.png) |
| 12:47:43 | [124743-web-ios-phone-after-hills-start.png](124743-web-ios-phone-after-hills-start.png) |
| 12:52:17 | [125217-unicorn-cycles-wing-beat-wayland.jpg](125217-unicorn-cycles-wing-beat-wayland.jpg) |
| 12:52:32 | [125232-unicorn-cycles-gallop-wayland.jpg](125232-unicorn-cycles-gallop-wayland.jpg) |
| 12:52:47 | [125247-unicorn-cycles-wing-beat-x11.jpg](125247-unicorn-cycles-wing-beat-x11.jpg) |
| 12:53:04 | [125304-unicorn-cycles-gallop-x11.jpg](125304-unicorn-cycles-gallop-x11.jpg) |
| 12:53:37 | [125337-web-ios-phone-after-loop-1min.png](125337-web-ios-phone-after-loop-1min.png) |
| 12:53:37 | [125337-web-ios-phone-after-loop-2min.png](125337-web-ios-phone-after-loop-2min.png) |
| 12:53:37 | [125337-web-ios-phone-after-loop-3min.png](125337-web-ios-phone-after-loop-3min.png) |
| 12:53:37 | [125337-web-ios-phone-after-loop-4min.png](125337-web-ios-phone-after-loop-4min.png) |
| 12:53:37 | [125337-web-ios-phone-after-loop-5min.png](125337-web-ios-phone-after-loop-5min.png) |
| 12:53:37 | [125337-web-ios-phone-after-loop-context-reloaded.png](125337-web-ios-phone-after-loop-context-reloaded.png) |
| 12:53:37 | [125337-web-ios-phone-after-loop-died-once.png](125337-web-ios-phone-after-loop-died-once.png) |
| 12:53:37 | [125337-web-ios-phone-after-loop-died-three-times.png](125337-web-ios-phone-after-loop-died-three-times.png) |
| 12:53:37 | [125337-web-ios-phone-after-loop-died-twice.png](125337-web-ios-phone-after-loop-died-twice.png) |
| 12:53:37 | [125337-web-ios-phone-after-loop-end.png](125337-web-ios-phone-after-loop-end.png) |
| 12:53:37 | [125337-web-ios-phone-after-loop-start.png](125337-web-ios-phone-after-loop-start.png) |
| 12:53:51 | [125351-unicorn-cycles-wing-video-end.jpg](125351-unicorn-cycles-wing-video-end.jpg) |
| 12:53:55 | [125355-unicorn-cycles-wing-cycle.mp4](125355-unicorn-cycles-wing-cycle.mp4) |
| 12:54:42 | [125442-unicorn-cycles-landing-video-end.jpg](125442-unicorn-cycles-landing-video-end.jpg) |
| 12:54:44 | [125444-unicorn-cycles-landing-cycle.mp4](125444-unicorn-cycles-landing-cycle.mp4) |
| 13:56:46 | [135646-q6-creases-a-side-live.jpg](135646-q6-creases-a-side-live.jpg) |
| 13:57:00 | [135700-q6-creases-a-side-j2b.jpg](135700-q6-creases-a-side-j2b.jpg) |
| 13:57:15 | [135715-q6-creases-a-side-j3.jpg](135715-q6-creases-a-side-j3.jpg) |
| 13:57:30 | [135730-q6-creases-a-approach-live.jpg](135730-q6-creases-a-approach-live.jpg) |
| 13:57:45 | [135745-q6-creases-a-approach-j2b.jpg](135745-q6-creases-a-approach-j2b.jpg) |
| 13:58:00 | [135800-q6-creases-a-approach-j3.jpg](135800-q6-creases-a-approach-j3.jpg) |
| 13:58:08 | [135808-q6-creases-chart-a-crease.png](135808-q6-creases-chart-a-crease.png) |
| 13:58:08 | [135808-q6-creases-chart-b-blended.png](135808-q6-creases-chart-b-blended.png) |
| 13:58:08 | [135808-q6-creases-chart-c-junction-room.png](135808-q6-creases-chart-c-junction-room.png) |
| 13:58:14 | [135814-q6-creases-a-rider-live.jpg](135814-q6-creases-a-rider-live.jpg) |
| 13:58:29 | [135829-q6-creases-a-rider-j2b.jpg](135829-q6-creases-a-rider-j2b.jpg) |
| 13:58:44 | [135844-q6-creases-a-rider-j3.jpg](135844-q6-creases-a-rider-j3.jpg) |
| 13:58:58 | [135858-q6-creases-c-side-live.jpg](135858-q6-creases-c-side-live.jpg) |
| 13:59:11 | [135911-q6-creases-c-side-j2b.jpg](135911-q6-creases-c-side-j2b.jpg) |
| 13:59:25 | [135925-q6-creases-c-side-j3.jpg](135925-q6-creases-c-side-j3.jpg) |
| 13:59:39 | [135939-q6-creases-c-rider-live.jpg](135939-q6-creases-c-rider-live.jpg) |
| 13:59:53 | [135953-q6-creases-c-rider-j2b.jpg](135953-q6-creases-c-rider-j2b.jpg) |
| 14:00:07 | [140007-q6-creases-c-rider-j3.jpg](140007-q6-creases-c-rider-j3.jpg) |
| 14:00:21 | [140021-q6-creases-c-up-live.jpg](140021-q6-creases-c-up-live.jpg) |
| 14:00:35 | [140035-q6-creases-c-up-j2b.jpg](140035-q6-creases-c-up-j2b.jpg) |
| 14:00:49 | [140049-q6-creases-c-up-j3.jpg](140049-q6-creases-c-up-j3.jpg) |
| 14:01:03 | [140103-q6-creases-b-side-live.jpg](140103-q6-creases-b-side-live.jpg) |
| 14:01:18 | [140118-q6-creases-b-side-j3.jpg](140118-q6-creases-b-side-j3.jpg) |
| 14:01:32 | [140132-q6-creases-b-rider-live.jpg](140132-q6-creases-b-rider-live.jpg) |
| 14:01:46 | [140146-q6-creases-b-rider-j3.jpg](140146-q6-creases-b-rider-j3.jpg) |
| 14:02:02 | [140202-q6-creases-compare-a-approach.jpg](140202-q6-creases-compare-a-approach.jpg) |
| 14:02:02 | [140202-q6-creases-compare-a-rider.jpg](140202-q6-creases-compare-a-rider.jpg) |
| 14:02:02 | [140202-q6-creases-compare-a-side.jpg](140202-q6-creases-compare-a-side.jpg) |
| 14:02:02 | [140202-q6-creases-compare-b-rider.jpg](140202-q6-creases-compare-b-rider.jpg) |
| 14:02:02 | [140202-q6-creases-compare-b-side.jpg](140202-q6-creases-compare-b-side.jpg) |
| 14:02:02 | [140202-q6-creases-compare-c-rider.jpg](140202-q6-creases-compare-c-rider.jpg) |
| 14:02:02 | [140202-q6-creases-compare-c-side.jpg](140202-q6-creases-compare-c-side.jpg) |
| 14:02:02 | [140202-q6-creases-compare-c-up.jpg](140202-q6-creases-compare-c-up.jpg) |
| 14:35:05 | [143505-plant-files-q11-li-forest-2026-07-15-far-before-generator.jpg](143505-plant-files-q11-li-forest-2026-07-15-far-before-generator.jpg) |
| 14:35:21 | [143521-plant-files-q11-li-forest-2026-07-15-near-before-generator.jpg](143521-plant-files-q11-li-forest-2026-07-15-near-before-generator.jpg) |
| 14:35:37 | [143537-plant-files-q11-li-forest-2026-11-23-far-before-generator.jpg](143537-plant-files-q11-li-forest-2026-11-23-far-before-generator.jpg) |
| 14:35:53 | [143553-plant-files-q11-li-forest-2026-11-23-near-before-generator.jpg](143553-plant-files-q11-li-forest-2026-11-23-near-before-generator.jpg) |
| 14:36:14 | [143614-e8fd6ab4-dirty-shot-wayland-bf-conifers-2026-07-15-near-before-generator.jpg](143614-e8fd6ab4-dirty-shot-wayland-bf-conifers-2026-07-15-near-before-generator.jpg) |
| 14:36:33 | [143633-e8fd6ab4-dirty-shot-wayland-bf-conifers-2026-07-15-far-before-generator.jpg](143633-e8fd6ab4-dirty-shot-wayland-bf-conifers-2026-07-15-far-before-generator.jpg) |
| 14:36:53 | [143653-e8fd6ab4-dirty-shot-wayland-bf-conifers-2026-11-23-near-before-generator.jpg](143653-e8fd6ab4-dirty-shot-wayland-bf-conifers-2026-11-23-near-before-generator.jpg) |
| 14:37:15 | [143715-e8fd6ab4-dirty-shot-wayland-bf-conifers-2026-11-23-far-before-generator.jpg](143715-e8fd6ab4-dirty-shot-wayland-bf-conifers-2026-11-23-far-before-generator.jpg) |
| 14:37:37 | [143737-e8fd6ab4-dirty-shot-wayland-tf-palms-2026-07-15-near-before-generator.jpg](143737-e8fd6ab4-dirty-shot-wayland-tf-palms-2026-07-15-near-before-generator.jpg) |
| 14:37:57 | [143757-e8fd6ab4-dirty-shot-wayland-tf-palms-2026-07-15-far-before-generator.jpg](143757-e8fd6ab4-dirty-shot-wayland-tf-palms-2026-07-15-far-before-generator.jpg) |
| 14:38:17 | [143817-e8fd6ab4-dirty-shot-wayland-tf-palms-2026-11-23-near-before-generator.jpg](143817-e8fd6ab4-dirty-shot-wayland-tf-palms-2026-11-23-near-before-generator.jpg) |
| 14:38:38 | [143838-e8fd6ab4-dirty-shot-wayland-tf-palms-2026-11-23-far-before-generator.jpg](143838-e8fd6ab4-dirty-shot-wayland-tf-palms-2026-11-23-far-before-generator.jpg) |
| 14:39:00 | [143900-e8fd6ab4-dirty-shot-wayland-tf-agave-2026-07-15-near-before-generator.jpg](143900-e8fd6ab4-dirty-shot-wayland-tf-agave-2026-07-15-near-before-generator.jpg) |
| 14:39:22 | [143922-e8fd6ab4-dirty-shot-wayland-tf-agave-2026-07-15-far-before-generator.jpg](143922-e8fd6ab4-dirty-shot-wayland-tf-agave-2026-07-15-far-before-generator.jpg) |
| 14:39:44 | [143944-e8fd6ab4-dirty-shot-wayland-tf-agave-2026-11-23-near-before-generator.jpg](143944-e8fd6ab4-dirty-shot-wayland-tf-agave-2026-11-23-near-before-generator.jpg) |
| 14:40:07 | [144007-e8fd6ab4-dirty-shot-wayland-tf-agave-2026-11-23-far-before-generator.jpg](144007-e8fd6ab4-dirty-shot-wayland-tf-agave-2026-11-23-far-before-generator.jpg) |
| 14:40:29 | [144029-plant-files-q11-tf-bananas-2026-07-15-near-before-generator.jpg](144029-plant-files-q11-tf-bananas-2026-07-15-near-before-generator.jpg) |
| 14:40:52 | [144052-plant-files-q11-tf-bananas-2026-11-23-near-before-generator.jpg](144052-plant-files-q11-tf-bananas-2026-11-23-near-before-generator.jpg) |
| 14:41:08 | [144108-plant-files-q11-li-forest-2026-07-15-far-before-files.jpg](144108-plant-files-q11-li-forest-2026-07-15-far-before-files.jpg) |
| 14:41:24 | [144124-plant-files-q11-li-forest-2026-07-15-near-before-files.jpg](144124-plant-files-q11-li-forest-2026-07-15-near-before-files.jpg) |
| 14:41:40 | [144140-plant-files-q11-li-forest-2026-11-23-far-before-files.jpg](144140-plant-files-q11-li-forest-2026-11-23-far-before-files.jpg) |
| 14:41:56 | [144156-plant-files-q11-li-forest-2026-11-23-near-before-files.jpg](144156-plant-files-q11-li-forest-2026-11-23-near-before-files.jpg) |
| 14:42:18 | [144218-e8fd6ab4-dirty-shot-wayland-bf-conifers-2026-07-15-near-before-files.jpg](144218-e8fd6ab4-dirty-shot-wayland-bf-conifers-2026-07-15-near-before-files.jpg) |
| 14:42:38 | [144238-e8fd6ab4-dirty-shot-wayland-bf-conifers-2026-07-15-far-before-files.jpg](144238-e8fd6ab4-dirty-shot-wayland-bf-conifers-2026-07-15-far-before-files.jpg) |
| 14:42:58 | [144258-e8fd6ab4-dirty-shot-wayland-bf-conifers-2026-11-23-near-before-files.jpg](144258-e8fd6ab4-dirty-shot-wayland-bf-conifers-2026-11-23-near-before-files.jpg) |
| 14:43:19 | [144319-e8fd6ab4-dirty-shot-wayland-bf-conifers-2026-11-23-far-before-files.jpg](144319-e8fd6ab4-dirty-shot-wayland-bf-conifers-2026-11-23-far-before-files.jpg) |
| 14:43:39 | [144339-e8fd6ab4-dirty-shot-wayland-tf-palms-2026-07-15-near-before-files.jpg](144339-e8fd6ab4-dirty-shot-wayland-tf-palms-2026-07-15-near-before-files.jpg) |
| 14:43:59 | [144359-e8fd6ab4-dirty-shot-wayland-tf-palms-2026-07-15-far-before-files.jpg](144359-e8fd6ab4-dirty-shot-wayland-tf-palms-2026-07-15-far-before-files.jpg) |
| 14:44:19 | [144419-e8fd6ab4-dirty-shot-wayland-tf-palms-2026-11-23-near-before-files.jpg](144419-e8fd6ab4-dirty-shot-wayland-tf-palms-2026-11-23-near-before-files.jpg) |
| 14:44:38 | [144438-e8fd6ab4-dirty-shot-wayland-tf-palms-2026-11-23-far-before-files.jpg](144438-e8fd6ab4-dirty-shot-wayland-tf-palms-2026-11-23-far-before-files.jpg) |
| 14:44:58 | [144458-e8fd6ab4-dirty-shot-wayland-tf-agave-2026-07-15-near-before-files.jpg](144458-e8fd6ab4-dirty-shot-wayland-tf-agave-2026-07-15-near-before-files.jpg) |
| 14:45:17 | [144517-e8fd6ab4-dirty-shot-wayland-tf-agave-2026-07-15-far-before-files.jpg](144517-e8fd6ab4-dirty-shot-wayland-tf-agave-2026-07-15-far-before-files.jpg) |
| 14:45:37 | [144537-e8fd6ab4-dirty-shot-wayland-tf-agave-2026-11-23-near-before-files.jpg](144537-e8fd6ab4-dirty-shot-wayland-tf-agave-2026-11-23-near-before-files.jpg) |
| 14:45:57 | [144557-e8fd6ab4-dirty-shot-wayland-tf-agave-2026-11-23-far-before-files.jpg](144557-e8fd6ab4-dirty-shot-wayland-tf-agave-2026-11-23-far-before-files.jpg) |
| 14:46:16 | [144616-plant-files-q11-tf-bananas-2026-07-15-near-before-files.jpg](144616-plant-files-q11-tf-bananas-2026-07-15-near-before-files.jpg) |
| 14:46:35 | [144635-plant-files-q11-tf-bananas-2026-11-23-near-before-files.jpg](144635-plant-files-q11-tf-bananas-2026-11-23-near-before-files.jpg) |
| 14:46:52 | [144652-plant-files-q11-li-forest-2026-07-15-far-after-generator.jpg](144652-plant-files-q11-li-forest-2026-07-15-far-after-generator.jpg) |
| 14:47:08 | [144708-plant-files-q11-li-forest-2026-07-15-near-after-generator.jpg](144708-plant-files-q11-li-forest-2026-07-15-near-after-generator.jpg) |
| 14:47:24 | [144724-plant-files-q11-li-forest-2026-11-23-far-after-generator.jpg](144724-plant-files-q11-li-forest-2026-11-23-far-after-generator.jpg) |
| 14:47:40 | [144740-plant-files-q11-li-forest-2026-11-23-near-after-generator.jpg](144740-plant-files-q11-li-forest-2026-11-23-near-after-generator.jpg) |
| 14:48:00 | [144800-e8fd6ab4-dirty-shot-wayland-bf-conifers-2026-07-15-near-after-generator.jpg](144800-e8fd6ab4-dirty-shot-wayland-bf-conifers-2026-07-15-near-after-generator.jpg) |
| 14:48:20 | [144820-e8fd6ab4-dirty-shot-wayland-bf-conifers-2026-07-15-far-after-generator.jpg](144820-e8fd6ab4-dirty-shot-wayland-bf-conifers-2026-07-15-far-after-generator.jpg) |
| 14:48:39 | [144839-e8fd6ab4-dirty-shot-wayland-bf-conifers-2026-11-23-near-after-generator.jpg](144839-e8fd6ab4-dirty-shot-wayland-bf-conifers-2026-11-23-near-after-generator.jpg) |
| 14:48:59 | [144859-e8fd6ab4-dirty-shot-wayland-bf-conifers-2026-11-23-far-after-generator.jpg](144859-e8fd6ab4-dirty-shot-wayland-bf-conifers-2026-11-23-far-after-generator.jpg) |
| 14:49:19 | [144919-e8fd6ab4-dirty-shot-wayland-tf-palms-2026-07-15-near-after-generator.jpg](144919-e8fd6ab4-dirty-shot-wayland-tf-palms-2026-07-15-near-after-generator.jpg) |
| 14:49:39 | [144939-e8fd6ab4-dirty-shot-wayland-tf-palms-2026-07-15-far-after-generator.jpg](144939-e8fd6ab4-dirty-shot-wayland-tf-palms-2026-07-15-far-after-generator.jpg) |
| 14:49:59 | [144959-e8fd6ab4-dirty-shot-wayland-tf-palms-2026-11-23-near-after-generator.jpg](144959-e8fd6ab4-dirty-shot-wayland-tf-palms-2026-11-23-near-after-generator.jpg) |
| 14:50:19 | [145019-e8fd6ab4-dirty-shot-wayland-tf-palms-2026-11-23-far-after-generator.jpg](145019-e8fd6ab4-dirty-shot-wayland-tf-palms-2026-11-23-far-after-generator.jpg) |
| 14:50:39 | [145039-e8fd6ab4-dirty-shot-wayland-tf-agave-2026-07-15-near-after-generator.jpg](145039-e8fd6ab4-dirty-shot-wayland-tf-agave-2026-07-15-near-after-generator.jpg) |
| 14:50:59 | [145059-e8fd6ab4-dirty-shot-wayland-tf-agave-2026-07-15-far-after-generator.jpg](145059-e8fd6ab4-dirty-shot-wayland-tf-agave-2026-07-15-far-after-generator.jpg) |
| 14:51:20 | [145120-e8fd6ab4-dirty-shot-wayland-tf-agave-2026-11-23-near-after-generator.jpg](145120-e8fd6ab4-dirty-shot-wayland-tf-agave-2026-11-23-near-after-generator.jpg) |
| 14:51:41 | [145141-e8fd6ab4-dirty-shot-wayland-tf-agave-2026-11-23-far-after-generator.jpg](145141-e8fd6ab4-dirty-shot-wayland-tf-agave-2026-11-23-far-after-generator.jpg) |
| 14:52:01 | [145201-plant-files-q11-tf-bananas-2026-07-15-near-after-generator.jpg](145201-plant-files-q11-tf-bananas-2026-07-15-near-after-generator.jpg) |
| 14:52:20 | [145220-plant-files-q11-tf-bananas-2026-11-23-near-after-generator.jpg](145220-plant-files-q11-tf-bananas-2026-11-23-near-after-generator.jpg) |
| 14:52:36 | [145236-plant-files-q11-li-forest-2026-07-15-far-after-files.jpg](145236-plant-files-q11-li-forest-2026-07-15-far-after-files.jpg) |
| 14:52:52 | [145252-plant-files-q11-li-forest-2026-07-15-near-after-files.jpg](145252-plant-files-q11-li-forest-2026-07-15-near-after-files.jpg) |
| 14:53:08 | [145308-plant-files-q11-li-forest-2026-11-23-far-after-files.jpg](145308-plant-files-q11-li-forest-2026-11-23-far-after-files.jpg) |
| 14:53:24 | [145324-plant-files-q11-li-forest-2026-11-23-near-after-files.jpg](145324-plant-files-q11-li-forest-2026-11-23-near-after-files.jpg) |
| 14:53:44 | [145344-e8fd6ab4-dirty-shot-wayland-bf-conifers-2026-07-15-near-after-files.jpg](145344-e8fd6ab4-dirty-shot-wayland-bf-conifers-2026-07-15-near-after-files.jpg) |
| 14:54:04 | [145404-e8fd6ab4-dirty-shot-wayland-bf-conifers-2026-07-15-far-after-files.jpg](145404-e8fd6ab4-dirty-shot-wayland-bf-conifers-2026-07-15-far-after-files.jpg) |
| 14:54:26 | [145426-e8fd6ab4-dirty-shot-wayland-bf-conifers-2026-11-23-near-after-files.jpg](145426-e8fd6ab4-dirty-shot-wayland-bf-conifers-2026-11-23-near-after-files.jpg) |
| 14:54:46 | [145446-e8fd6ab4-dirty-shot-wayland-bf-conifers-2026-11-23-far-after-files.jpg](145446-e8fd6ab4-dirty-shot-wayland-bf-conifers-2026-11-23-far-after-files.jpg) |
| 14:55:06 | [145506-e8fd6ab4-dirty-shot-wayland-tf-palms-2026-07-15-near-after-files.jpg](145506-e8fd6ab4-dirty-shot-wayland-tf-palms-2026-07-15-near-after-files.jpg) |
| 14:55:28 | [145528-e8fd6ab4-dirty-shot-wayland-tf-palms-2026-07-15-far-after-files.jpg](145528-e8fd6ab4-dirty-shot-wayland-tf-palms-2026-07-15-far-after-files.jpg) |
| 14:55:49 | [145549-e8fd6ab4-dirty-shot-wayland-tf-palms-2026-11-23-near-after-files.jpg](145549-e8fd6ab4-dirty-shot-wayland-tf-palms-2026-11-23-near-after-files.jpg) |
| 14:56:11 | [145611-e8fd6ab4-dirty-shot-wayland-tf-palms-2026-11-23-far-after-files.jpg](145611-e8fd6ab4-dirty-shot-wayland-tf-palms-2026-11-23-far-after-files.jpg) |
| 14:56:31 | [145631-e8fd6ab4-dirty-shot-wayland-tf-agave-2026-07-15-near-after-files.jpg](145631-e8fd6ab4-dirty-shot-wayland-tf-agave-2026-07-15-near-after-files.jpg) |
| 14:56:52 | [145652-e8fd6ab4-dirty-shot-wayland-tf-agave-2026-07-15-far-after-files.jpg](145652-e8fd6ab4-dirty-shot-wayland-tf-agave-2026-07-15-far-after-files.jpg) |
| 14:57:12 | [145712-e8fd6ab4-dirty-shot-wayland-tf-agave-2026-11-23-near-after-files.jpg](145712-e8fd6ab4-dirty-shot-wayland-tf-agave-2026-11-23-near-after-files.jpg) |
| 14:57:31 | [145731-e8fd6ab4-dirty-shot-wayland-tf-agave-2026-11-23-far-after-files.jpg](145731-e8fd6ab4-dirty-shot-wayland-tf-agave-2026-11-23-far-after-files.jpg) |
| 14:57:51 | [145751-plant-files-q11-tf-bananas-2026-07-15-near-after-files.jpg](145751-plant-files-q11-tf-bananas-2026-07-15-near-after-files.jpg) |
| 14:58:11 | [145811-plant-files-q11-tf-bananas-2026-11-23-near-after-files.jpg](145811-plant-files-q11-tf-bananas-2026-11-23-near-after-files.jpg) |
| 15:00:10 | [150010-e8fd6ab4-dirty-shot-wayland-bf-schauinsland-2026-07-15-far-before-generator.jpg](150010-e8fd6ab4-dirty-shot-wayland-bf-schauinsland-2026-07-15-far-before-generator.jpg) |
| 15:00:34 | [150034-e8fd6ab4-dirty-shot-wayland-bf-schauinsland-2026-07-15-near-before-generator.jpg](150034-e8fd6ab4-dirty-shot-wayland-bf-schauinsland-2026-07-15-near-before-generator.jpg) |
| 15:00:57 | [150057-e8fd6ab4-dirty-shot-wayland-bf-schauinsland-2026-11-23-far-before-generator.jpg](150057-e8fd6ab4-dirty-shot-wayland-bf-schauinsland-2026-11-23-far-before-generator.jpg) |
| 15:01:18 | [150118-e8fd6ab4-dirty-shot-wayland-bf-schauinsland-2026-11-23-near-before-generator.jpg](150118-e8fd6ab4-dirty-shot-wayland-bf-schauinsland-2026-11-23-near-before-generator.jpg) |
| 15:01:39 | [150139-e8fd6ab4-dirty-shot-wayland-bf-schauinsland-2026-07-15-far-before-files.jpg](150139-e8fd6ab4-dirty-shot-wayland-bf-schauinsland-2026-07-15-far-before-files.jpg) |
| 15:02:02 | [150202-e8fd6ab4-dirty-shot-wayland-bf-schauinsland-2026-07-15-near-before-files.jpg](150202-e8fd6ab4-dirty-shot-wayland-bf-schauinsland-2026-07-15-near-before-files.jpg) |
| 15:02:26 | [150226-e8fd6ab4-dirty-shot-wayland-bf-schauinsland-2026-11-23-far-before-files.jpg](150226-e8fd6ab4-dirty-shot-wayland-bf-schauinsland-2026-11-23-far-before-files.jpg) |
| 15:02:49 | [150249-e8fd6ab4-dirty-shot-wayland-bf-schauinsland-2026-11-23-near-before-files.jpg](150249-e8fd6ab4-dirty-shot-wayland-bf-schauinsland-2026-11-23-near-before-files.jpg) |
| 15:03:11 | [150311-e8fd6ab4-dirty-shot-wayland-bf-schauinsland-2026-07-15-far-after-generator.jpg](150311-e8fd6ab4-dirty-shot-wayland-bf-schauinsland-2026-07-15-far-after-generator.jpg) |
| 15:03:32 | [150332-e8fd6ab4-dirty-shot-wayland-bf-schauinsland-2026-07-15-near-after-generator.jpg](150332-e8fd6ab4-dirty-shot-wayland-bf-schauinsland-2026-07-15-near-after-generator.jpg) |
| 15:03:55 | [150355-e8fd6ab4-dirty-shot-wayland-bf-schauinsland-2026-11-23-far-after-generator.jpg](150355-e8fd6ab4-dirty-shot-wayland-bf-schauinsland-2026-11-23-far-after-generator.jpg) |
| 15:04:16 | [150416-e8fd6ab4-dirty-shot-wayland-bf-schauinsland-2026-11-23-near-after-generator.jpg](150416-e8fd6ab4-dirty-shot-wayland-bf-schauinsland-2026-11-23-near-after-generator.jpg) |
| 15:04:38 | [150438-e8fd6ab4-dirty-shot-wayland-bf-schauinsland-2026-07-15-far-after-files.jpg](150438-e8fd6ab4-dirty-shot-wayland-bf-schauinsland-2026-07-15-far-after-files.jpg) |
| 15:04:59 | [150459-e8fd6ab4-dirty-shot-wayland-bf-schauinsland-2026-07-15-near-after-files.jpg](150459-e8fd6ab4-dirty-shot-wayland-bf-schauinsland-2026-07-15-near-after-files.jpg) |
| 15:05:21 | [150521-e8fd6ab4-dirty-shot-wayland-bf-schauinsland-2026-11-23-far-after-files.jpg](150521-e8fd6ab4-dirty-shot-wayland-bf-schauinsland-2026-11-23-far-after-files.jpg) |
| 15:05:45 | [150545-e8fd6ab4-dirty-shot-wayland-bf-schauinsland-2026-11-23-near-after-files.jpg](150545-e8fd6ab4-dirty-shot-wayland-bf-schauinsland-2026-11-23-near-after-files.jpg) |
| 15:06:06 | [150606-e8fd6ab4-dirty-shot-wayland-tf-palms-2026-07-15-far-before-generator.jpg](150606-e8fd6ab4-dirty-shot-wayland-tf-palms-2026-07-15-far-before-generator.jpg) |
| 15:06:29 | [150629-e8fd6ab4-dirty-shot-wayland-tf-palms-2026-07-15-near-before-generator.jpg](150629-e8fd6ab4-dirty-shot-wayland-tf-palms-2026-07-15-near-before-generator.jpg) |
| 15:06:52 | [150652-e8fd6ab4-dirty-shot-wayland-tf-palms-2026-11-23-far-before-generator.jpg](150652-e8fd6ab4-dirty-shot-wayland-tf-palms-2026-11-23-far-before-generator.jpg) |
| 15:07:15 | [150715-e8fd6ab4-dirty-shot-wayland-tf-palms-2026-11-23-near-before-generator.jpg](150715-e8fd6ab4-dirty-shot-wayland-tf-palms-2026-11-23-near-before-generator.jpg) |
| 15:07:38 | [150738-e8fd6ab4-dirty-shot-wayland-tf-palms-above-2026-07-15-near-before-generator.jpg](150738-e8fd6ab4-dirty-shot-wayland-tf-palms-above-2026-07-15-near-before-generator.jpg) |
| 15:08:00 | [150800-e8fd6ab4-dirty-shot-wayland-tf-palms-above-2026-11-23-near-before-generator.jpg](150800-e8fd6ab4-dirty-shot-wayland-tf-palms-above-2026-11-23-near-before-generator.jpg) |
| 15:08:22 | [150822-e8fd6ab4-dirty-shot-wayland-tf-palms-2026-07-15-far-before-files.jpg](150822-e8fd6ab4-dirty-shot-wayland-tf-palms-2026-07-15-far-before-files.jpg) |
| 15:08:44 | [150844-e8fd6ab4-dirty-shot-wayland-tf-palms-2026-07-15-near-before-files.jpg](150844-e8fd6ab4-dirty-shot-wayland-tf-palms-2026-07-15-near-before-files.jpg) |
| 15:09:06 | [150906-e8fd6ab4-dirty-shot-wayland-tf-palms-2026-11-23-far-before-files.jpg](150906-e8fd6ab4-dirty-shot-wayland-tf-palms-2026-11-23-far-before-files.jpg) |
| 15:09:28 | [150928-e8fd6ab4-dirty-shot-wayland-tf-palms-2026-11-23-near-before-files.jpg](150928-e8fd6ab4-dirty-shot-wayland-tf-palms-2026-11-23-near-before-files.jpg) |
| 15:09:51 | [150951-e8fd6ab4-dirty-shot-wayland-tf-palms-above-2026-07-15-near-before-files.jpg](150951-e8fd6ab4-dirty-shot-wayland-tf-palms-above-2026-07-15-near-before-files.jpg) |
| 15:10:13 | [151013-e8fd6ab4-dirty-shot-wayland-tf-palms-above-2026-11-23-near-before-files.jpg](151013-e8fd6ab4-dirty-shot-wayland-tf-palms-above-2026-11-23-near-before-files.jpg) |
| 15:10:37 | [151037-e8fd6ab4-dirty-shot-wayland-tf-palms-2026-07-15-far-after-generator.jpg](151037-e8fd6ab4-dirty-shot-wayland-tf-palms-2026-07-15-far-after-generator.jpg) |
| 15:11:01 | [151101-e8fd6ab4-dirty-shot-wayland-tf-palms-2026-07-15-near-after-generator.jpg](151101-e8fd6ab4-dirty-shot-wayland-tf-palms-2026-07-15-near-after-generator.jpg) |
| 15:11:24 | [151124-e8fd6ab4-dirty-shot-wayland-tf-palms-2026-11-23-far-after-generator.jpg](151124-e8fd6ab4-dirty-shot-wayland-tf-palms-2026-11-23-far-after-generator.jpg) |
| 15:11:47 | [151147-e8fd6ab4-dirty-shot-wayland-tf-palms-2026-11-23-near-after-generator.jpg](151147-e8fd6ab4-dirty-shot-wayland-tf-palms-2026-11-23-near-after-generator.jpg) |
| 15:12:07 | [151207-e8fd6ab4-dirty-shot-wayland-tf-palms-above-2026-07-15-near-after-generator.jpg](151207-e8fd6ab4-dirty-shot-wayland-tf-palms-above-2026-07-15-near-after-generator.jpg) |
| 15:12:28 | [151228-e8fd6ab4-dirty-shot-wayland-tf-palms-above-2026-11-23-near-after-generator.jpg](151228-e8fd6ab4-dirty-shot-wayland-tf-palms-above-2026-11-23-near-after-generator.jpg) |
| 15:12:51 | [151251-e8fd6ab4-dirty-shot-wayland-tf-palms-2026-07-15-far-after-files.jpg](151251-e8fd6ab4-dirty-shot-wayland-tf-palms-2026-07-15-far-after-files.jpg) |
| 15:13:13 | [151313-e8fd6ab4-dirty-shot-wayland-tf-palms-2026-07-15-near-after-files.jpg](151313-e8fd6ab4-dirty-shot-wayland-tf-palms-2026-07-15-near-after-files.jpg) |
| 15:13:35 | [151335-e8fd6ab4-dirty-shot-wayland-tf-palms-2026-11-23-far-after-files.jpg](151335-e8fd6ab4-dirty-shot-wayland-tf-palms-2026-11-23-far-after-files.jpg) |
| 15:13:56 | [151356-e8fd6ab4-dirty-shot-wayland-tf-palms-2026-11-23-near-after-files.jpg](151356-e8fd6ab4-dirty-shot-wayland-tf-palms-2026-11-23-near-after-files.jpg) |
| 15:14:00 | [151400-13a-ring-green-meadow.jpg](151400-13a-ring-green-meadow.jpg) |
| 15:14:16 | [151416-e8fd6ab4-dirty-shot-wayland-tf-palms-above-2026-07-15-near-after-files.jpg](151416-e8fd6ab4-dirty-shot-wayland-tf-palms-above-2026-07-15-near-after-files.jpg) |
| 15:14:37 | [151437-e8fd6ab4-dirty-shot-wayland-tf-palms-above-2026-11-23-near-after-files.jpg](151437-e8fd6ab4-dirty-shot-wayland-tf-palms-above-2026-11-23-near-after-files.jpg) |
| 15:15:02 | [151502-e8fd6ab4-dirty-shot-wayland-tf-agave-2026-07-15-far-before-generator.jpg](151502-e8fd6ab4-dirty-shot-wayland-tf-agave-2026-07-15-far-before-generator.jpg) |
| 15:15:22 | [151522-e8fd6ab4-dirty-shot-wayland-tf-agave-2026-07-15-near-before-generator.jpg](151522-e8fd6ab4-dirty-shot-wayland-tf-agave-2026-07-15-near-before-generator.jpg) |
| 15:15:42 | [151542-e8fd6ab4-dirty-shot-wayland-tf-agave-2026-11-23-far-before-generator.jpg](151542-e8fd6ab4-dirty-shot-wayland-tf-agave-2026-11-23-far-before-generator.jpg) |
| 15:16:04 | [151604-e8fd6ab4-dirty-shot-wayland-tf-agave-2026-11-23-near-before-generator.jpg](151604-e8fd6ab4-dirty-shot-wayland-tf-agave-2026-11-23-near-before-generator.jpg) |
| 15:16:26 | [151626-e8fd6ab4-dirty-shot-wayland-tf-agave-2026-07-15-far-before-files.jpg](151626-e8fd6ab4-dirty-shot-wayland-tf-agave-2026-07-15-far-before-files.jpg) |
| 15:16:37 | [151637-13a-ring-red-water.jpg](151637-13a-ring-red-water.jpg) |
| 15:16:46 | [151646-e8fd6ab4-dirty-shot-wayland-tf-agave-2026-07-15-near-before-files.jpg](151646-e8fd6ab4-dirty-shot-wayland-tf-agave-2026-07-15-near-before-files.jpg) |
| 15:16:52 | [151652-13a-ring-red-house.jpg](151652-13a-ring-red-house.jpg) |
| 15:17:06 | [151706-e8fd6ab4-dirty-shot-wayland-tf-agave-2026-11-23-far-before-files.jpg](151706-e8fd6ab4-dirty-shot-wayland-tf-agave-2026-11-23-far-before-files.jpg) |
| 15:17:26 | [151726-e8fd6ab4-dirty-shot-wayland-tf-agave-2026-11-23-near-before-files.jpg](151726-e8fd6ab4-dirty-shot-wayland-tf-agave-2026-11-23-near-before-files.jpg) |
| 15:17:46 | [151746-e8fd6ab4-dirty-shot-wayland-tf-agave-2026-07-15-far-after-generator.jpg](151746-e8fd6ab4-dirty-shot-wayland-tf-agave-2026-07-15-far-after-generator.jpg) |
| 15:18:03 | [151803-13a-climb-steep-slope.jpg](151803-13a-climb-steep-slope.jpg) |
| 15:18:06 | [151806-13a-climb-steep-slope.mp4](151806-13a-climb-steep-slope.mp4) |
| 15:18:07 | [151807-e8fd6ab4-dirty-shot-wayland-tf-agave-2026-07-15-near-after-generator.jpg](151807-e8fd6ab4-dirty-shot-wayland-tf-agave-2026-07-15-near-after-generator.jpg) |
| 15:18:28 | [151828-e8fd6ab4-dirty-shot-wayland-tf-agave-2026-11-23-far-after-generator.jpg](151828-e8fd6ab4-dirty-shot-wayland-tf-agave-2026-11-23-far-after-generator.jpg) |
| 15:18:48 | [151848-e8fd6ab4-dirty-shot-wayland-tf-agave-2026-11-23-near-after-generator.jpg](151848-e8fd6ab4-dirty-shot-wayland-tf-agave-2026-11-23-near-after-generator.jpg) |
| 15:19:08 | [151908-e8fd6ab4-dirty-shot-wayland-tf-agave-2026-07-15-far-after-files.jpg](151908-e8fd6ab4-dirty-shot-wayland-tf-agave-2026-07-15-far-after-files.jpg) |
| 15:19:30 | [151930-e8fd6ab4-dirty-shot-wayland-tf-agave-2026-07-15-near-after-files.jpg](151930-e8fd6ab4-dirty-shot-wayland-tf-agave-2026-07-15-near-after-files.jpg) |
| 15:19:50 | [151950-e8fd6ab4-dirty-shot-wayland-tf-agave-2026-11-23-far-after-files.jpg](151950-e8fd6ab4-dirty-shot-wayland-tf-agave-2026-11-23-far-after-files.jpg) |
| 15:20:10 | [152010-e8fd6ab4-dirty-shot-wayland-tf-agave-2026-11-23-near-after-files.jpg](152010-e8fd6ab4-dirty-shot-wayland-tf-agave-2026-11-23-near-after-files.jpg) |
| 15:20:43 | [152043-13a-meadow-to-road.jpg](152043-13a-meadow-to-road.jpg) |
| 15:20:53 | [152053-13a-meadow-to-road.mp4](152053-13a-meadow-to-road.mp4) |
| 15:21:16 | [152116-plant-files-q11-bf-schauinsland-2026-07-15-far-before-generator.jpg](152116-plant-files-q11-bf-schauinsland-2026-07-15-far-before-generator.jpg) |
| 15:21:40 | [152140-plant-files-q11-bf-schauinsland-2026-07-15-near-before-generator.jpg](152140-plant-files-q11-bf-schauinsland-2026-07-15-near-before-generator.jpg) |
| 15:22:02 | [152202-plant-files-q11-bf-schauinsland-2026-11-23-far-before-generator.jpg](152202-plant-files-q11-bf-schauinsland-2026-11-23-far-before-generator.jpg) |
| 15:22:26 | [152226-plant-files-q11-bf-schauinsland-2026-11-23-near-before-generator.jpg](152226-plant-files-q11-bf-schauinsland-2026-11-23-near-before-generator.jpg) |
| 15:22:43 | [152243-plant-files-q11-li-forest-2026-07-15-far-before-generator.jpg](152243-plant-files-q11-li-forest-2026-07-15-far-before-generator.jpg) |
| 15:22:59 | [152259-plant-files-q11-li-forest-2026-07-15-near-before-generator.jpg](152259-plant-files-q11-li-forest-2026-07-15-near-before-generator.jpg) |
| 15:23:15 | [152315-plant-files-q11-li-forest-2026-11-23-far-before-generator.jpg](152315-plant-files-q11-li-forest-2026-11-23-far-before-generator.jpg) |
| 15:23:31 | [152331-plant-files-q11-li-forest-2026-11-23-near-before-generator.jpg](152331-plant-files-q11-li-forest-2026-11-23-near-before-generator.jpg) |
| 15:23:52 | [152352-plant-files-q11-tf-agave-2026-07-15-far-before-generator.jpg](152352-plant-files-q11-tf-agave-2026-07-15-far-before-generator.jpg) |
| 15:24:15 | [152415-plant-files-q11-tf-agave-2026-07-15-near-before-generator.jpg](152415-plant-files-q11-tf-agave-2026-07-15-near-before-generator.jpg) |
| 15:24:37 | [152437-plant-files-q11-tf-agave-2026-11-23-far-before-generator.jpg](152437-plant-files-q11-tf-agave-2026-11-23-far-before-generator.jpg) |
| 15:24:59 | [152459-plant-files-q11-tf-agave-2026-11-23-near-before-generator.jpg](152459-plant-files-q11-tf-agave-2026-11-23-near-before-generator.jpg) |
| 15:25:22 | [152522-plant-files-q11-tf-bananas-2026-07-15-near-before-generator.jpg](152522-plant-files-q11-tf-bananas-2026-07-15-near-before-generator.jpg) |
| 15:25:44 | [152544-plant-files-q11-tf-bananas-2026-11-23-near-before-generator.jpg](152544-plant-files-q11-tf-bananas-2026-11-23-near-before-generator.jpg) |
| 15:26:07 | [152607-plant-files-q11-tf-palms-2026-07-15-far-before-generator.jpg](152607-plant-files-q11-tf-palms-2026-07-15-far-before-generator.jpg) |
| 15:26:30 | [152630-plant-files-q11-tf-palms-2026-07-15-near-before-generator.jpg](152630-plant-files-q11-tf-palms-2026-07-15-near-before-generator.jpg) |
| 15:26:53 | [152653-plant-files-q11-tf-palms-2026-11-23-far-before-generator.jpg](152653-plant-files-q11-tf-palms-2026-11-23-far-before-generator.jpg) |
| 15:27:06 | [152706-j4-q7-chart-a-crease.png](152706-j4-q7-chart-a-crease.png) |
| 15:27:06 | [152706-j4-q7-chart-b-blended.png](152706-j4-q7-chart-b-blended.png) |
| 15:27:07 | [152707-j4-q7-chart-c-junction-room.png](152707-j4-q7-chart-c-junction-room.png) |
| 15:27:14 | [152714-plant-files-q11-tf-palms-2026-11-23-near-before-generator.jpg](152714-plant-files-q11-tf-palms-2026-11-23-near-before-generator.jpg) |
| 15:27:36 | [152736-plant-files-q11-tf-palms-above-2026-07-15-near-before-generator.jpg](152736-plant-files-q11-tf-palms-above-2026-07-15-near-before-generator.jpg) |
| 15:27:56 | [152756-plant-files-q11-tf-palms-above-2026-11-23-near-before-generator.jpg](152756-plant-files-q11-tf-palms-above-2026-11-23-near-before-generator.jpg) |
| 15:28:21 | [152821-plant-files-q11-bf-schauinsland-2026-07-15-far-before-files.jpg](152821-plant-files-q11-bf-schauinsland-2026-07-15-far-before-files.jpg) |
| 15:28:44 | [152844-plant-files-q11-bf-schauinsland-2026-07-15-near-before-files.jpg](152844-plant-files-q11-bf-schauinsland-2026-07-15-near-before-files.jpg) |
| 15:29:07 | [152907-plant-files-q11-bf-schauinsland-2026-11-23-far-before-files.jpg](152907-plant-files-q11-bf-schauinsland-2026-11-23-far-before-files.jpg) |
| 15:29:31 | [152931-plant-files-q11-bf-schauinsland-2026-11-23-near-before-files.jpg](152931-plant-files-q11-bf-schauinsland-2026-11-23-near-before-files.jpg) |
| 15:29:48 | [152948-plant-files-q11-li-forest-2026-07-15-far-before-files.jpg](152948-plant-files-q11-li-forest-2026-07-15-far-before-files.jpg) |
| 15:30:05 | [153005-plant-files-q11-li-forest-2026-07-15-near-before-files.jpg](153005-plant-files-q11-li-forest-2026-07-15-near-before-files.jpg) |
| 15:30:21 | [153021-plant-files-q11-li-forest-2026-11-23-far-before-files.jpg](153021-plant-files-q11-li-forest-2026-11-23-far-before-files.jpg) |
| 15:30:37 | [153037-plant-files-q11-li-forest-2026-11-23-near-before-files.jpg](153037-plant-files-q11-li-forest-2026-11-23-near-before-files.jpg) |
| 15:31:00 | [153100-plant-files-q11-tf-agave-2026-07-15-far-before-files.jpg](153100-plant-files-q11-tf-agave-2026-07-15-far-before-files.jpg) |
| 15:31:22 | [153122-plant-files-q11-tf-agave-2026-07-15-near-before-files.jpg](153122-plant-files-q11-tf-agave-2026-07-15-near-before-files.jpg) |
| 15:31:42 | [153142-plant-files-q11-tf-agave-2026-11-23-far-before-files.jpg](153142-plant-files-q11-tf-agave-2026-11-23-far-before-files.jpg) |
| 15:32:04 | [153204-plant-files-q11-tf-agave-2026-11-23-near-before-files.jpg](153204-plant-files-q11-tf-agave-2026-11-23-near-before-files.jpg) |
| 15:32:26 | [153226-plant-files-q11-tf-bananas-2026-07-15-near-before-files.jpg](153226-plant-files-q11-tf-bananas-2026-07-15-near-before-files.jpg) |
| 15:32:47 | [153247-plant-files-q11-tf-bananas-2026-11-23-near-before-files.jpg](153247-plant-files-q11-tf-bananas-2026-11-23-near-before-files.jpg) |
| 15:33:00 | [153300-smoke-d526dc9a-shot-ocw.jpg](153300-smoke-d526dc9a-shot-ocw.jpg) |
| 15:33:07 | [153307-plant-files-q11-tf-palms-2026-07-15-far-before-files.jpg](153307-plant-files-q11-tf-palms-2026-07-15-far-before-files.jpg) |
| 15:33:09 | [153309-smoke-d526dc9a-shot-wayland-ocw-wayland.jpg](153309-smoke-d526dc9a-shot-wayland-ocw-wayland.jpg) |
| 15:33:24 | [153324-j4-q7-a-side-live.jpg](153324-j4-q7-a-side-live.jpg) |
| 15:33:27 | [153327-plant-files-q11-tf-palms-2026-07-15-near-before-files.jpg](153327-plant-files-q11-tf-palms-2026-07-15-near-before-files.jpg) |
| 15:33:39 | [153339-j4-q7-a-side-j3.jpg](153339-j4-q7-a-side-j3.jpg) |
| 15:33:47 | [153347-plant-files-q11-tf-palms-2026-11-23-far-before-files.jpg](153347-plant-files-q11-tf-palms-2026-11-23-far-before-files.jpg) |
| 15:33:53 | [153353-j4-q7-a-side-j4.jpg](153353-j4-q7-a-side-j4.jpg) |
| 15:34:07 | [153407-plant-files-q11-tf-palms-2026-11-23-near-before-files.jpg](153407-plant-files-q11-tf-palms-2026-11-23-near-before-files.jpg) |
| 15:34:28 | [153428-plant-files-q11-tf-palms-above-2026-07-15-near-before-files.jpg](153428-plant-files-q11-tf-palms-above-2026-07-15-near-before-files.jpg) |
| 15:34:48 | [153448-plant-files-q11-tf-palms-above-2026-11-23-near-before-files.jpg](153448-plant-files-q11-tf-palms-above-2026-11-23-near-before-files.jpg) |
| 15:34:50 | [153450-j4-q7-a-rider-live.jpg](153450-j4-q7-a-rider-live.jpg) |
| 15:35:05 | [153505-j4-q7-a-rider-j3.jpg](153505-j4-q7-a-rider-j3.jpg) |
| 15:35:11 | [153511-plant-files-q11-bf-schauinsland-2026-07-15-far-after-generator.jpg](153511-plant-files-q11-bf-schauinsland-2026-07-15-far-after-generator.jpg) |
| 15:35:19 | [153519-j4-q7-a-rider-j4.jpg](153519-j4-q7-a-rider-j4.jpg) |
| 15:35:33 | [153533-j4-q7-b-side-live.jpg](153533-j4-q7-b-side-live.jpg) |
| 15:35:33 | [153533-plant-files-q11-bf-schauinsland-2026-07-15-near-after-generator.jpg](153533-plant-files-q11-bf-schauinsland-2026-07-15-near-after-generator.jpg) |
| 15:35:48 | [153548-j4-q7-b-side-j3.jpg](153548-j4-q7-b-side-j3.jpg) |
| 15:35:56 | [153556-plant-files-q11-bf-schauinsland-2026-11-23-far-after-generator.jpg](153556-plant-files-q11-bf-schauinsland-2026-11-23-far-after-generator.jpg) |
| 15:36:02 | [153602-j4-q7-b-side-j4.jpg](153602-j4-q7-b-side-j4.jpg) |
| 15:36:17 | [153617-j4-q7-b-rider-live.jpg](153617-j4-q7-b-rider-live.jpg) |
| 15:36:18 | [153618-plant-files-q11-bf-schauinsland-2026-11-23-near-after-generator.jpg](153618-plant-files-q11-bf-schauinsland-2026-11-23-near-after-generator.jpg) |
| 15:36:31 | [153631-j4-q7-b-rider-j3.jpg](153631-j4-q7-b-rider-j3.jpg) |
| 15:36:35 | [153635-plant-files-q11-li-forest-2026-07-15-far-after-generator.jpg](153635-plant-files-q11-li-forest-2026-07-15-far-after-generator.jpg) |
| 15:36:45 | [153645-j4-q7-b-rider-j4.jpg](153645-j4-q7-b-rider-j4.jpg) |
| 15:36:51 | [153651-plant-files-q11-li-forest-2026-07-15-near-after-generator.jpg](153651-plant-files-q11-li-forest-2026-07-15-near-after-generator.jpg) |
| 15:37:00 | [153700-j4-q7-c-side-live.jpg](153700-j4-q7-c-side-live.jpg) |
| 15:37:07 | [153707-plant-files-q11-li-forest-2026-11-23-far-after-generator.jpg](153707-plant-files-q11-li-forest-2026-11-23-far-after-generator.jpg) |
| 15:37:14 | [153714-j4-q7-c-side-j3.jpg](153714-j4-q7-c-side-j3.jpg) |
| 15:37:23 | [153723-plant-files-q11-li-forest-2026-11-23-near-after-generator.jpg](153723-plant-files-q11-li-forest-2026-11-23-near-after-generator.jpg) |
| 15:37:28 | [153728-j4-q7-c-side-j4.jpg](153728-j4-q7-c-side-j4.jpg) |
| 15:37:43 | [153743-j4-q7-c-rider-live.jpg](153743-j4-q7-c-rider-live.jpg) |
| 15:37:44 | [153744-plant-files-q11-tf-agave-2026-07-15-far-after-generator.jpg](153744-plant-files-q11-tf-agave-2026-07-15-far-after-generator.jpg) |
| 15:37:57 | [153757-j4-q7-c-rider-j3.jpg](153757-j4-q7-c-rider-j3.jpg) |
| 15:38:05 | [153805-plant-files-q11-tf-agave-2026-07-15-near-after-generator.jpg](153805-plant-files-q11-tf-agave-2026-07-15-near-after-generator.jpg) |
| 15:38:11 | [153811-j4-q7-c-rider-j4.jpg](153811-j4-q7-c-rider-j4.jpg) |
| 15:38:26 | [153826-j4-q7-c-up-live.jpg](153826-j4-q7-c-up-live.jpg) |
| 15:38:26 | [153826-plant-files-q11-tf-agave-2026-11-23-far-after-generator.jpg](153826-plant-files-q11-tf-agave-2026-11-23-far-after-generator.jpg) |
| 15:38:41 | [153841-j4-q7-c-up-j3.jpg](153841-j4-q7-c-up-j3.jpg) |
| 15:38:48 | [153848-plant-files-q11-tf-agave-2026-11-23-near-after-generator.jpg](153848-plant-files-q11-tf-agave-2026-11-23-near-after-generator.jpg) |
| 15:38:56 | [153856-j4-q7-c-up-j4.jpg](153856-j4-q7-c-up-j4.jpg) |
| 15:39:10 | [153910-plant-files-q11-tf-bananas-2026-07-15-near-after-generator.jpg](153910-plant-files-q11-tf-bananas-2026-07-15-near-after-generator.jpg) |
| 15:39:33 | [153933-plant-files-q11-tf-bananas-2026-11-23-near-after-generator.jpg](153933-plant-files-q11-tf-bananas-2026-11-23-near-after-generator.jpg) |
| 15:39:55 | [153955-plant-files-q11-tf-palms-2026-07-15-far-after-generator.jpg](153955-plant-files-q11-tf-palms-2026-07-15-far-after-generator.jpg) |
| 15:40:18 | [154018-plant-files-q11-tf-palms-2026-07-15-near-after-generator.jpg](154018-plant-files-q11-tf-palms-2026-07-15-near-after-generator.jpg) |
| 15:40:42 | [154042-plant-files-q11-tf-palms-2026-11-23-far-after-generator.jpg](154042-plant-files-q11-tf-palms-2026-11-23-far-after-generator.jpg) |
| 15:41:05 | [154105-plant-files-q11-tf-palms-2026-11-23-near-after-generator.jpg](154105-plant-files-q11-tf-palms-2026-11-23-near-after-generator.jpg) |
| 15:41:28 | [154128-plant-files-q11-tf-palms-above-2026-07-15-near-after-generator.jpg](154128-plant-files-q11-tf-palms-above-2026-07-15-near-after-generator.jpg) |
| 15:41:52 | [154152-plant-files-q11-tf-palms-above-2026-11-23-near-after-generator.jpg](154152-plant-files-q11-tf-palms-above-2026-11-23-near-after-generator.jpg) |
| 15:42:18 | [154218-plant-files-q11-bf-schauinsland-2026-07-15-far-after-files.jpg](154218-plant-files-q11-bf-schauinsland-2026-07-15-far-after-files.jpg) |
| 15:42:42 | [154242-plant-files-q11-bf-schauinsland-2026-07-15-near-after-files.jpg](154242-plant-files-q11-bf-schauinsland-2026-07-15-near-after-files.jpg) |
| 15:42:59 | [154259-j4-q7-compare-a-rider.jpg](154259-j4-q7-compare-a-rider.jpg) |
| 15:42:59 | [154259-j4-q7-compare-a-side.jpg](154259-j4-q7-compare-a-side.jpg) |
| 15:42:59 | [154259-j4-q7-compare-b-rider.jpg](154259-j4-q7-compare-b-rider.jpg) |
| 15:42:59 | [154259-j4-q7-compare-b-side.jpg](154259-j4-q7-compare-b-side.jpg) |
| 15:42:59 | [154259-j4-q7-compare-c-rider.jpg](154259-j4-q7-compare-c-rider.jpg) |
| 15:42:59 | [154259-j4-q7-compare-c-side.jpg](154259-j4-q7-compare-c-side.jpg) |
| 15:42:59 | [154259-j4-q7-compare-c-up.jpg](154259-j4-q7-compare-c-up.jpg) |
| 15:43:07 | [154307-plant-files-q11-bf-schauinsland-2026-11-23-far-after-files.jpg](154307-plant-files-q11-bf-schauinsland-2026-11-23-far-after-files.jpg) |
| 15:43:33 | [154333-plant-files-q11-bf-schauinsland-2026-11-23-near-after-files.jpg](154333-plant-files-q11-bf-schauinsland-2026-11-23-near-after-files.jpg) |
| 15:43:51 | [154351-plant-files-q11-li-forest-2026-07-15-far-after-files.jpg](154351-plant-files-q11-li-forest-2026-07-15-far-after-files.jpg) |
| 15:44:08 | [154408-plant-files-q11-li-forest-2026-07-15-near-after-files.jpg](154408-plant-files-q11-li-forest-2026-07-15-near-after-files.jpg) |
| 15:44:25 | [154425-plant-files-q11-li-forest-2026-11-23-far-after-files.jpg](154425-plant-files-q11-li-forest-2026-11-23-far-after-files.jpg) |
| 15:44:42 | [154442-plant-files-q11-li-forest-2026-11-23-near-after-files.jpg](154442-plant-files-q11-li-forest-2026-11-23-near-after-files.jpg) |
| 15:45:05 | [154505-plant-files-q11-tf-agave-2026-07-15-far-after-files.jpg](154505-plant-files-q11-tf-agave-2026-07-15-far-after-files.jpg) |
| 15:45:27 | [154527-plant-files-q11-tf-agave-2026-07-15-near-after-files.jpg](154527-plant-files-q11-tf-agave-2026-07-15-near-after-files.jpg) |
| 15:45:51 | [154551-plant-files-q11-tf-agave-2026-11-23-far-after-files.jpg](154551-plant-files-q11-tf-agave-2026-11-23-far-after-files.jpg) |
| 15:46:15 | [154615-plant-files-q11-tf-agave-2026-11-23-near-after-files.jpg](154615-plant-files-q11-tf-agave-2026-11-23-near-after-files.jpg) |
| 15:46:37 | [154637-plant-files-q11-tf-bananas-2026-07-15-near-after-files.jpg](154637-plant-files-q11-tf-bananas-2026-07-15-near-after-files.jpg) |
| 15:47:00 | [154700-plant-files-q11-tf-bananas-2026-11-23-near-after-files.jpg](154700-plant-files-q11-tf-bananas-2026-11-23-near-after-files.jpg) |
| 15:47:20 | [154720-plant-files-q11-tf-palms-2026-07-15-far-after-files.jpg](154720-plant-files-q11-tf-palms-2026-07-15-far-after-files.jpg) |
| 15:47:40 | [154740-plant-files-q11-tf-palms-2026-07-15-near-after-files.jpg](154740-plant-files-q11-tf-palms-2026-07-15-near-after-files.jpg) |
| 15:48:03 | [154803-plant-files-q11-tf-palms-2026-11-23-far-after-files.jpg](154803-plant-files-q11-tf-palms-2026-11-23-far-after-files.jpg) |
| 15:48:25 | [154825-plant-files-q11-tf-palms-2026-11-23-near-after-files.jpg](154825-plant-files-q11-tf-palms-2026-11-23-near-after-files.jpg) |
| 15:48:46 | [154846-plant-files-q11-tf-palms-above-2026-07-15-near-after-files.jpg](154846-plant-files-q11-tf-palms-above-2026-07-15-near-after-files.jpg) |
| 15:49:06 | [154906-plant-files-q11-tf-palms-above-2026-11-23-near-after-files.jpg](154906-plant-files-q11-tf-palms-above-2026-11-23-near-after-files.jpg) |
| 15:53:58 | [155358-j4-q7-a-approach-live.jpg](155358-j4-q7-a-approach-live.jpg) |
| 15:54:13 | [155413-j4-q7-a-approach-j3.jpg](155413-j4-q7-a-approach-j3.jpg) |
| 15:54:29 | [155429-j4-q7-a-approach-j4.jpg](155429-j4-q7-a-approach-j4.jpg) |
| 15:54:44 | [155444-j4-q7-terrain-edge-j3.jpg](155444-j4-q7-terrain-edge-j3.jpg) |
| 15:54:59 | [155459-j4-q7-terrain-edge-j4.jpg](155459-j4-q7-terrain-edge-j4.jpg) |
| 15:55:13 | [155513-j4-q7-terrain-meadow-j3.jpg](155513-j4-q7-terrain-meadow-j3.jpg) |
| 15:55:29 | [155529-j4-q7-terrain-meadow-j4.jpg](155529-j4-q7-terrain-meadow-j4.jpg) |
| 15:55:40 | [155540-j4-q7-compare-a-approach.jpg](155540-j4-q7-compare-a-approach.jpg) |
| 15:55:40 | [155540-j4-q7-compare-terrain-edge.jpg](155540-j4-q7-compare-terrain-edge.jpg) |
| 15:55:40 | [155540-j4-q7-compare-terrain-meadow.jpg](155540-j4-q7-compare-terrain-meadow.jpg) |
| 16:36:36 | [163636-a17760b0-shot-ocw.jpg](163636-a17760b0-shot-ocw.jpg) |
| 16:36:47 | [163647-a17760b0-shot-wayland-ocw-wayland.jpg](163647-a17760b0-shot-wayland-ocw-wayland.jpg) |
| 17:51:20 | [175120-j4-q7-a-side-live.jpg](175120-j4-q7-a-side-live.jpg) |
| 17:51:35 | [175135-j4-q7-a-side-j3.jpg](175135-j4-q7-a-side-j3.jpg) |
| 17:51:49 | [175149-j4-q7-a-side-j4.jpg](175149-j4-q7-a-side-j4.jpg) |
| 17:52:04 | [175204-j4-q7-a-approach-live.jpg](175204-j4-q7-a-approach-live.jpg) |
| 17:52:18 | [175218-j4-q7-a-approach-j3.jpg](175218-j4-q7-a-approach-j3.jpg) |
| 17:52:33 | [175233-j4-q7-a-approach-j4.jpg](175233-j4-q7-a-approach-j4.jpg) |
| 17:52:47 | [175247-j4-q7-a-rider-live.jpg](175247-j4-q7-a-rider-live.jpg) |
| 17:53:02 | [175302-j4-q7-a-rider-j3.jpg](175302-j4-q7-a-rider-j3.jpg) |
| 17:53:16 | [175316-j4-q7-a-rider-j4.jpg](175316-j4-q7-a-rider-j4.jpg) |
| 17:53:31 | [175331-j4-q7-b-side-live.jpg](175331-j4-q7-b-side-live.jpg) |
| 17:53:46 | [175346-j4-q7-b-side-j3.jpg](175346-j4-q7-b-side-j3.jpg) |
| 17:54:00 | [175400-j4-q7-b-side-j4.jpg](175400-j4-q7-b-side-j4.jpg) |
| 17:54:15 | [175415-j4-q7-b-rider-live.jpg](175415-j4-q7-b-rider-live.jpg) |
| 17:54:29 | [175429-j4-q7-b-rider-j3.jpg](175429-j4-q7-b-rider-j3.jpg) |
| 17:54:44 | [175444-j4-q7-b-rider-j4.jpg](175444-j4-q7-b-rider-j4.jpg) |
| 17:54:58 | [175458-j4-q7-c-side-live.jpg](175458-j4-q7-c-side-live.jpg) |
| 17:55:13 | [175513-j4-q7-c-side-j3.jpg](175513-j4-q7-c-side-j3.jpg) |
| 17:55:27 | [175527-j4-q7-c-side-j4.jpg](175527-j4-q7-c-side-j4.jpg) |
| 17:55:42 | [175542-j4-q7-c-rider-live.jpg](175542-j4-q7-c-rider-live.jpg) |
| 17:55:57 | [175557-j4-q7-c-rider-j3.jpg](175557-j4-q7-c-rider-j3.jpg) |
| 17:56:11 | [175611-j4-q7-c-rider-j4.jpg](175611-j4-q7-c-rider-j4.jpg) |
| 17:56:26 | [175626-j4-q7-c-up-live.jpg](175626-j4-q7-c-up-live.jpg) |
| 17:56:40 | [175640-j4-q7-c-up-j3.jpg](175640-j4-q7-c-up-j3.jpg) |
| 17:56:55 | [175655-j4-q7-c-up-j4.jpg](175655-j4-q7-c-up-j4.jpg) |
| 17:57:09 | [175709-j4-q7-terrain-edge-j3.jpg](175709-j4-q7-terrain-edge-j3.jpg) |
| 17:57:24 | [175724-j4-q7-terrain-edge-j4.jpg](175724-j4-q7-terrain-edge-j4.jpg) |
| 17:57:38 | [175738-j4-q7-terrain-meadow-j3.jpg](175738-j4-q7-terrain-meadow-j3.jpg) |
| 17:57:53 | [175753-j4-q7-terrain-meadow-j4.jpg](175753-j4-q7-terrain-meadow-j4.jpg) |
| 17:58:07 | [175807-j4-q7-a-corner-j4.jpg](175807-j4-q7-a-corner-j4.jpg) |
| 17:58:35 | [175835-j4-q7-chart-a-crease.png](175835-j4-q7-chart-a-crease.png) |
| 17:58:35 | [175835-j4-q7-chart-b-blended.png](175835-j4-q7-chart-b-blended.png) |
| 17:58:44 | [175844-j4-q7-compare-a-approach.jpg](175844-j4-q7-compare-a-approach.jpg) |
| 17:58:44 | [175844-j4-q7-compare-a-rider.jpg](175844-j4-q7-compare-a-rider.jpg) |
| 17:58:44 | [175844-j4-q7-compare-a-side.jpg](175844-j4-q7-compare-a-side.jpg) |
| 17:58:44 | [175844-j4-q7-compare-b-rider.jpg](175844-j4-q7-compare-b-rider.jpg) |
| 17:58:44 | [175844-j4-q7-compare-b-side.jpg](175844-j4-q7-compare-b-side.jpg) |
| 17:58:44 | [175844-j4-q7-compare-c-rider.jpg](175844-j4-q7-compare-c-rider.jpg) |
| 17:58:44 | [175844-j4-q7-compare-c-side.jpg](175844-j4-q7-compare-c-side.jpg) |
| 17:58:44 | [175844-j4-q7-compare-c-up.jpg](175844-j4-q7-compare-c-up.jpg) |
| 17:58:44 | [175844-j4-q7-compare-corner.jpg](175844-j4-q7-compare-corner.jpg) |
| 17:58:44 | [175844-j4-q7-compare-terrain-edge.jpg](175844-j4-q7-compare-terrain-edge.jpg) |
| 17:58:44 | [175844-j4-q7-compare-terrain-meadow.jpg](175844-j4-q7-compare-terrain-meadow.jpg) |
| 17:58:44 | [175844-j4-q7-corner-crop-after.jpg](175844-j4-q7-corner-crop-after.jpg) |
| 17:58:44 | [175844-j4-q7-corner-crop-before.jpg](175844-j4-q7-corner-crop-before.jpg) |
| 17:59:03 | [175903-j4-q7-a-corner-joint-zoom.jpg](175903-j4-q7-a-corner-joint-zoom.jpg) |
| 19:51:37 | [195137-9968b832-dirty-shot-wayland-q11-unicorn-head.jpg](195137-9968b832-dirty-shot-wayland-q11-unicorn-head.jpg) |
| 19:51:47 | [195147-9968b832-dirty-shot-wayland-q11-unicorn-far.jpg](195147-9968b832-dirty-shot-wayland-q11-unicorn-far.jpg) |
| 19:51:59 | [195159-9968b832-dirty-shot-wayland-q11-face-closeup.jpg](195159-9968b832-dirty-shot-wayland-q11-face-closeup.jpg) |
| 19:52:09 | [195209-9968b832-dirty-shot-wayland-lips-speaking.jpg](195209-9968b832-dirty-shot-wayland-lips-speaking.jpg) |
| 19:52:59 | [195259-9968b832-dirty-shot-wayland-q11-unicorn-head.jpg](195259-9968b832-dirty-shot-wayland-q11-unicorn-head.jpg) |
| 19:53:09 | [195309-9968b832-dirty-shot-wayland-q11-unicorn-head-front.jpg](195309-9968b832-dirty-shot-wayland-q11-unicorn-head-front.jpg) |
| 19:53:20 | [195320-9968b832-dirty-shot-wayland-q11-unicorn-far.jpg](195320-9968b832-dirty-shot-wayland-q11-unicorn-far.jpg) |
| 19:53:58 | [195358-9968b832-dirty-shot-wayland-q11-unicorn-head.jpg](195358-9968b832-dirty-shot-wayland-q11-unicorn-head.jpg) |
| 19:54:09 | [195409-9968b832-dirty-shot-wayland-q11-unicorn-head-front.jpg](195409-9968b832-dirty-shot-wayland-q11-unicorn-head-front.jpg) |
| 19:54:20 | [195420-9968b832-dirty-shot-wayland-q11-unicorn-far.jpg](195420-9968b832-dirty-shot-wayland-q11-unicorn-far.jpg) |
| 19:54:30 | [195430-9968b832-dirty-shot-wayland-q11-face-closeup.jpg](195430-9968b832-dirty-shot-wayland-q11-face-closeup.jpg) |
| 19:54:41 | [195441-9968b832-dirty-shot-wayland-lips-speaking.jpg](195441-9968b832-dirty-shot-wayland-lips-speaking.jpg) |
| 19:55:01 | [195501-q11-unicorn-lips-compare-lips-speaking-mouth.jpg](195501-q11-unicorn-lips-compare-lips-speaking-mouth.jpg) |
| 19:55:01 | [195501-q11-unicorn-lips-compare-q11-face-closeup-mouth.jpg](195501-q11-unicorn-lips-compare-q11-face-closeup-mouth.jpg) |
| 19:57:22 | [195722-lamps-layout-2026-11-23-web-ios-before-before-loop-1min.png](195722-lamps-layout-2026-11-23-web-ios-before-before-loop-1min.png) |
| 19:57:22 | [195722-lamps-layout-2026-11-23-web-ios-before-before-loop-2min.png](195722-lamps-layout-2026-11-23-web-ios-before-before-loop-2min.png) |
| 19:57:22 | [195722-lamps-layout-2026-11-23-web-ios-before-before-loop-3min.png](195722-lamps-layout-2026-11-23-web-ios-before-before-loop-3min.png) |
| 19:57:22 | [195722-lamps-layout-2026-11-23-web-ios-before-before-loop-4min.png](195722-lamps-layout-2026-11-23-web-ios-before-before-loop-4min.png) |
| 19:57:22 | [195722-lamps-layout-2026-11-23-web-ios-before-before-loop-5min.png](195722-lamps-layout-2026-11-23-web-ios-before-before-loop-5min.png) |
| 19:57:22 | [195722-lamps-layout-2026-11-23-web-ios-before-before-loop-context-reloaded.png](195722-lamps-layout-2026-11-23-web-ios-before-before-loop-context-reloaded.png) |
| 19:57:22 | [195722-lamps-layout-2026-11-23-web-ios-before-before-loop-end.png](195722-lamps-layout-2026-11-23-web-ios-before-before-loop-end.png) |
| 19:57:22 | [195722-lamps-layout-2026-11-23-web-ios-before-before-loop-start.png](195722-lamps-layout-2026-11-23-web-ios-before-before-loop-start.png) |
| 20:00:20 | [200020-9968b832-dirty-shot-wayland-q11-face-closeup.jpg](200020-9968b832-dirty-shot-wayland-q11-face-closeup.jpg) |
| 20:00:31 | [200031-9968b832-dirty-shot-wayland-lips-speaking.jpg](200031-9968b832-dirty-shot-wayland-lips-speaking.jpg) |
| 20:03:14 | [200314-lamps-layout-2026-11-23-web-ios-before-before-liechtenstein-1min.png](200314-lamps-layout-2026-11-23-web-ios-before-before-liechtenstein-1min.png) |
| 20:03:14 | [200314-lamps-layout-2026-11-23-web-ios-before-before-liechtenstein-2min.png](200314-lamps-layout-2026-11-23-web-ios-before-before-liechtenstein-2min.png) |
| 20:03:14 | [200314-lamps-layout-2026-11-23-web-ios-before-before-liechtenstein-3min.png](200314-lamps-layout-2026-11-23-web-ios-before-before-liechtenstein-3min.png) |
| 20:03:14 | [200314-lamps-layout-2026-11-23-web-ios-before-before-liechtenstein-4min.png](200314-lamps-layout-2026-11-23-web-ios-before-before-liechtenstein-4min.png) |
| 20:03:14 | [200314-lamps-layout-2026-11-23-web-ios-before-before-liechtenstein-5min.png](200314-lamps-layout-2026-11-23-web-ios-before-before-liechtenstein-5min.png) |
| 20:03:14 | [200314-lamps-layout-2026-11-23-web-ios-before-before-liechtenstein-context-lost-again.png](200314-lamps-layout-2026-11-23-web-ios-before-before-liechtenstein-context-lost-again.png) |
| 20:03:14 | [200314-lamps-layout-2026-11-23-web-ios-before-before-liechtenstein-context-reloaded.png](200314-lamps-layout-2026-11-23-web-ios-before-before-liechtenstein-context-reloaded.png) |
| 20:03:14 | [200314-lamps-layout-2026-11-23-web-ios-before-before-liechtenstein-end.png](200314-lamps-layout-2026-11-23-web-ios-before-before-liechtenstein-end.png) |
| 20:03:14 | [200314-lamps-layout-2026-11-23-web-ios-before-before-liechtenstein-start.png](200314-lamps-layout-2026-11-23-web-ios-before-before-liechtenstein-start.png) |
| 20:28:19 | [202819-j5-sides-bf-fork-j4.jpg](202819-j5-sides-bf-fork-j4.jpg) |
| 20:28:19 | [202819-j5-sides-bf-path-j4.jpg](202819-j5-sides-bf-path-j4.jpg) |
| 20:28:19 | [202819-j5-sides-bf-t-j4.jpg](202819-j5-sides-bf-t-j4.jpg) |
| 20:28:19 | [202819-j5-sides-li-fork-j4.jpg](202819-j5-sides-li-fork-j4.jpg) |
| 20:28:19 | [202819-j5-sides-li-letzanaweg-corner-j4.jpg](202819-j5-sides-li-letzanaweg-corner-j4.jpg) |
| 20:28:19 | [202819-j5-sides-li-letzanaweg-side-j4.jpg](202819-j5-sides-li-letzanaweg-side-j4.jpg) |
| 20:28:19 | [202819-j5-sides-li-path-j4.jpg](202819-j5-sides-li-path-j4.jpg) |
| 20:28:19 | [202819-j5-sides-li-t-j4.jpg](202819-j5-sides-li-t-j4.jpg) |
| 20:28:19 | [202819-j5-sides-tf-fork-j4.jpg](202819-j5-sides-tf-fork-j4.jpg) |
| 20:28:19 | [202819-j5-sides-tf-path-j4.jpg](202819-j5-sides-tf-path-j4.jpg) |
| 20:28:19 | [202819-j5-sides-tf-t-j4.jpg](202819-j5-sides-tf-t-j4.jpg) |
| 20:52:51 | [205251-j5-sides-li-letzanaweg-corner-j5.jpg](205251-j5-sides-li-letzanaweg-corner-j5.jpg) |
| 20:53:07 | [205307-j5-sides-li-letzanaweg-side-j5.jpg](205307-j5-sides-li-letzanaweg-side-j5.jpg) |
| 20:53:22 | [205322-j5-sides-li-t-j5.jpg](205322-j5-sides-li-t-j5.jpg) |
| 20:53:37 | [205337-j5-sides-li-fork-j5.jpg](205337-j5-sides-li-fork-j5.jpg) |
| 20:53:52 | [205352-j5-sides-li-path-j5.jpg](205352-j5-sides-li-path-j5.jpg) |
| 21:00:55 | [210055-6320e4bc-dirty-shot-wayland-tf-prickly-pear-before.jpg](210055-6320e4bc-dirty-shot-wayland-tf-prickly-pear-before.jpg) |
| 21:01:17 | [210117-6320e4bc-dirty-shot-wayland-tf-agave-before.jpg](210117-6320e4bc-dirty-shot-wayland-tf-agave-before.jpg) |
| 21:01:40 | [210140-6320e4bc-dirty-shot-wayland-tf-teide-broom-before.jpg](210140-6320e4bc-dirty-shot-wayland-tf-teide-broom-before.jpg) |
| 21:01:54 | [210154-6320e4bc-dirty-shot-wayland-li-green-alder-before.jpg](210154-6320e4bc-dirty-shot-wayland-li-green-alder-before.jpg) |
| 21:05:48 | [210548-lamps-layout-2026-11-23-web-webkit-after-web-webkit-iphone-hints.png](210548-lamps-layout-2026-11-23-web-webkit-after-web-webkit-iphone-hints.png) |
| 21:05:48 | [210548-lamps-layout-2026-11-23-web-webkit-after-web-webkit-iphone-hold.png](210548-lamps-layout-2026-11-23-web-webkit-after-web-webkit-iphone-hold.png) |
| 21:05:48 | [210548-lamps-layout-2026-11-23-web-webkit-after-web-webkit-iphone-landscape-hints.png](210548-lamps-layout-2026-11-23-web-webkit-after-web-webkit-iphone-landscape-hints.png) |
| 21:05:48 | [210548-lamps-layout-2026-11-23-web-webkit-after-web-webkit-iphone-landscape-hold.png](210548-lamps-layout-2026-11-23-web-webkit-after-web-webkit-iphone-landscape-hold.png) |
| 21:05:48 | [210548-lamps-layout-2026-11-23-web-webkit-after-web-webkit-iphone-landscape-riding.png](210548-lamps-layout-2026-11-23-web-webkit-after-web-webkit-iphone-landscape-riding.png) |
| 21:05:48 | [210548-lamps-layout-2026-11-23-web-webkit-after-web-webkit-iphone-landscape-stopped.png](210548-lamps-layout-2026-11-23-web-webkit-after-web-webkit-iphone-landscape-stopped.png) |
| 21:05:48 | [210548-lamps-layout-2026-11-23-web-webkit-after-web-webkit-iphone-landscape.png](210548-lamps-layout-2026-11-23-web-webkit-after-web-webkit-iphone-landscape.png) |
| 21:05:48 | [210548-lamps-layout-2026-11-23-web-webkit-after-web-webkit-iphone-riding.png](210548-lamps-layout-2026-11-23-web-webkit-after-web-webkit-iphone-riding.png) |
| 21:05:48 | [210548-lamps-layout-2026-11-23-web-webkit-after-web-webkit-iphone-start.png](210548-lamps-layout-2026-11-23-web-webkit-after-web-webkit-iphone-start.png) |
| 21:05:48 | [210548-lamps-layout-2026-11-23-web-webkit-after-web-webkit-iphone-stopped.png](210548-lamps-layout-2026-11-23-web-webkit-after-web-webkit-iphone-stopped.png) |
| 21:05:48 | [210548-lamps-layout-2026-11-23-web-webkit-after-web-webkit-iphone.png](210548-lamps-layout-2026-11-23-web-webkit-after-web-webkit-iphone.png) |
| 21:05:48 | [210548-lamps-layout-2026-11-23-web-webkit-after-web-webkit-layout-android-360x640.png](210548-lamps-layout-2026-11-23-web-webkit-after-web-webkit-layout-android-360x640.png) |
| 21:05:48 | [210548-lamps-layout-2026-11-23-web-webkit-after-web-webkit-layout-android-640x360.png](210548-lamps-layout-2026-11-23-web-webkit-after-web-webkit-layout-android-640x360.png) |
| 21:05:48 | [210548-lamps-layout-2026-11-23-web-webkit-after-web-webkit-layout-iphone-390x844.png](210548-lamps-layout-2026-11-23-web-webkit-after-web-webkit-layout-iphone-390x844.png) |
| 21:05:48 | [210548-lamps-layout-2026-11-23-web-webkit-after-web-webkit-layout-iphone-844x390.png](210548-lamps-layout-2026-11-23-web-webkit-after-web-webkit-layout-iphone-844x390.png) |
| 21:05:48 | [210548-lamps-layout-2026-11-23-web-webkit-after-web-webkit-mac.png](210548-lamps-layout-2026-11-23-web-webkit-after-web-webkit-mac.png) |
| 21:08:33 | [210833-lamps-layout-2026-11-23-web-ios-after-lamp-bump-liechtenstein-1min.png](210833-lamps-layout-2026-11-23-web-ios-after-lamp-bump-liechtenstein-1min.png) |
| 21:08:33 | [210833-lamps-layout-2026-11-23-web-ios-after-lamp-bump-liechtenstein-end.png](210833-lamps-layout-2026-11-23-web-ios-after-lamp-bump-liechtenstein-end.png) |
| 21:08:33 | [210833-lamps-layout-2026-11-23-web-ios-after-lamp-bump-liechtenstein-lamp-after.png](210833-lamps-layout-2026-11-23-web-ios-after-lamp-bump-liechtenstein-lamp-after.png) |
| 21:08:33 | [210833-lamps-layout-2026-11-23-web-ios-after-lamp-bump-liechtenstein-lamp-approach.png](210833-lamps-layout-2026-11-23-web-ios-after-lamp-bump-liechtenstein-lamp-approach.png) |
| 21:08:33 | [210833-lamps-layout-2026-11-23-web-ios-after-lamp-bump-liechtenstein-lamp-bump.png](210833-lamps-layout-2026-11-23-web-ios-after-lamp-bump-liechtenstein-lamp-bump.png) |
| 21:08:33 | [210833-lamps-layout-2026-11-23-web-ios-after-lamp-bump-liechtenstein-start.png](210833-lamps-layout-2026-11-23-web-ios-after-lamp-bump-liechtenstein-start.png) |
| 21:09:31 | [210931-0c952ede-dirty-shot-wayland-q10-woods-stop.jpg](210931-0c952ede-dirty-shot-wayland-q10-woods-stop.jpg) |
| 21:09:45 | [210945-lamps-layout-2026-11-23-web-ios-after-after-loop-1min.png](210945-lamps-layout-2026-11-23-web-ios-after-after-loop-1min.png) |
| 21:09:45 | [210945-lamps-layout-2026-11-23-web-ios-after-after-loop-2min.png](210945-lamps-layout-2026-11-23-web-ios-after-after-loop-2min.png) |
| 21:09:45 | [210945-lamps-layout-2026-11-23-web-ios-after-after-loop-3min.png](210945-lamps-layout-2026-11-23-web-ios-after-after-loop-3min.png) |
| 21:09:45 | [210945-lamps-layout-2026-11-23-web-ios-after-after-loop-4min.png](210945-lamps-layout-2026-11-23-web-ios-after-after-loop-4min.png) |
| 21:09:45 | [210945-lamps-layout-2026-11-23-web-ios-after-after-loop-5min.png](210945-lamps-layout-2026-11-23-web-ios-after-after-loop-5min.png) |
| 21:09:45 | [210945-lamps-layout-2026-11-23-web-ios-after-after-loop-context-reloaded.png](210945-lamps-layout-2026-11-23-web-ios-after-after-loop-context-reloaded.png) |
| 21:09:45 | [210945-lamps-layout-2026-11-23-web-ios-after-after-loop-end.png](210945-lamps-layout-2026-11-23-web-ios-after-after-loop-end.png) |
| 21:09:45 | [210945-lamps-layout-2026-11-23-web-ios-after-after-loop-start.png](210945-lamps-layout-2026-11-23-web-ios-after-after-loop-start.png) |
| 21:10:24 | [211024-0c952ede-dirty-video-wayland-q10-woods-crash-video.jpg](211024-0c952ede-dirty-video-wayland-q10-woods-crash-video.jpg) |
| 21:10:24 | [211024-0c952ede-dirty-video-wayland-q10-woods-crash-video.mp4](211024-0c952ede-dirty-video-wayland-q10-woods-crash-video.mp4) |
| 21:15:37 | [211537-lamps-layout-2026-11-23-web-ios-after-after-liechtenstein-1min.png](211537-lamps-layout-2026-11-23-web-ios-after-after-liechtenstein-1min.png) |
| 21:15:37 | [211537-lamps-layout-2026-11-23-web-ios-after-after-liechtenstein-2min.png](211537-lamps-layout-2026-11-23-web-ios-after-after-liechtenstein-2min.png) |
| 21:15:37 | [211537-lamps-layout-2026-11-23-web-ios-after-after-liechtenstein-3min.png](211537-lamps-layout-2026-11-23-web-ios-after-after-liechtenstein-3min.png) |
| 21:15:37 | [211537-lamps-layout-2026-11-23-web-ios-after-after-liechtenstein-4min.png](211537-lamps-layout-2026-11-23-web-ios-after-after-liechtenstein-4min.png) |
| 21:15:37 | [211537-lamps-layout-2026-11-23-web-ios-after-after-liechtenstein-5min.png](211537-lamps-layout-2026-11-23-web-ios-after-after-liechtenstein-5min.png) |
| 21:15:37 | [211537-lamps-layout-2026-11-23-web-ios-after-after-liechtenstein-context-lost-again.png](211537-lamps-layout-2026-11-23-web-ios-after-after-liechtenstein-context-lost-again.png) |
| 21:15:37 | [211537-lamps-layout-2026-11-23-web-ios-after-after-liechtenstein-context-reloaded.png](211537-lamps-layout-2026-11-23-web-ios-after-after-liechtenstein-context-reloaded.png) |
| 21:15:37 | [211537-lamps-layout-2026-11-23-web-ios-after-after-liechtenstein-end.png](211537-lamps-layout-2026-11-23-web-ios-after-after-liechtenstein-end.png) |
| 21:15:37 | [211537-lamps-layout-2026-11-23-web-ios-after-after-liechtenstein-start.png](211537-lamps-layout-2026-11-23-web-ios-after-after-liechtenstein-start.png) |
| 21:23:20 | [212320-j5-sides-li-letzanaweg-corner-j5.jpg](212320-j5-sides-li-letzanaweg-corner-j5.jpg) |
| 21:23:36 | [212336-j5-sides-li-letzanaweg-side-j5.jpg](212336-j5-sides-li-letzanaweg-side-j5.jpg) |
| 21:23:52 | [212352-j5-sides-li-t-j5.jpg](212352-j5-sides-li-t-j5.jpg) |
| 21:24:08 | [212408-j5-sides-li-fork-j5.jpg](212408-j5-sides-li-fork-j5.jpg) |
| 21:24:24 | [212424-j5-sides-li-path-j5.jpg](212424-j5-sides-li-path-j5.jpg) |
| 21:24:56 | [212456-j5-sides-tf-t-j5.jpg](212456-j5-sides-tf-t-j5.jpg) |
| 21:25:29 | [212529-j5-sides-tf-fork-j5.jpg](212529-j5-sides-tf-fork-j5.jpg) |
| 21:26:01 | [212601-j5-sides-tf-path-j5.jpg](212601-j5-sides-tf-path-j5.jpg) |
| 21:26:34 | [212634-j5-sides-bf-t-j5.jpg](212634-j5-sides-bf-t-j5.jpg) |
| 21:27:04 | [212704-j5-sides-bf-fork-j5.jpg](212704-j5-sides-bf-fork-j5.jpg) |
| 21:27:33 | [212733-j5-sides-bf-path-j5.jpg](212733-j5-sides-bf-path-j5.jpg) |
| 21:28:17 | [212817-j5-sides-li-letzanaweg-joint-j4.jpg](212817-j5-sides-li-letzanaweg-joint-j4.jpg) |
| 21:28:17 | [212817-j5-sides-li-letzanaweg-joint-j5.jpg](212817-j5-sides-li-letzanaweg-joint-j5.jpg) |
| 21:28:47 | [212847-j5-sides-chart-a-crease.png](212847-j5-sides-chart-a-crease.png) |
| 21:28:47 | [212847-j5-sides-chart-b-blended.png](212847-j5-sides-chart-b-blended.png) |
| 21:28:48 | [212848-j5-sides-chart-c-junction-room.png](212848-j5-sides-chart-c-junction-room.png) |
| 21:28:48 | [212848-plant-origin-q10-tf-prickly-pear-before.jpg](212848-plant-origin-q10-tf-prickly-pear-before.jpg) |
| 21:29:15 | [212915-plant-origin-q10-tf-agave-before.jpg](212915-plant-origin-q10-tf-agave-before.jpg) |
| 21:29:43 | [212943-6320e4bc-dirty-shot-wayland-tf-teide-broom-before.jpg](212943-6320e4bc-dirty-shot-wayland-tf-teide-broom-before.jpg) |
| 21:29:59 | [212959-6320e4bc-dirty-shot-wayland-li-green-alder-before.jpg](212959-6320e4bc-dirty-shot-wayland-li-green-alder-before.jpg) |
| 21:33:56 | [213356-d797f262-dirty-shot-wayland-q10-woods-stop.jpg](213356-d797f262-dirty-shot-wayland-q10-woods-stop.jpg) |
| 21:35:01 | [213501-d797f262-dirty-video-wayland-q10-woods-crash-video.jpg](213501-d797f262-dirty-video-wayland-q10-woods-crash-video.jpg) |
| 21:35:01 | [213501-d797f262-dirty-video-wayland-q10-woods-crash-video.mp4](213501-d797f262-dirty-video-wayland-q10-woods-crash-video.mp4) |
| 21:35:26 | [213526-d797f262-shot-ocw.jpg](213526-d797f262-shot-ocw.jpg) |
| 21:35:36 | [213536-d797f262-shot-wayland-ocw-wayland.jpg](213536-d797f262-shot-wayland-ocw-wayland.jpg) |
| 21:36:00 | [213600-plant-origin-q10-tf-teide-broom-before.jpg](213600-plant-origin-q10-tf-teide-broom-before.jpg) |
| 21:36:14 | [213614-plant-origin-q10-li-green-alder-before.jpg](213614-plant-origin-q10-li-green-alder-before.jpg) |
| 21:41:09 | [214109-lamps-layout-2026-11-23-web-webkit-final-web-webkit-iphone-hints.png](214109-lamps-layout-2026-11-23-web-webkit-final-web-webkit-iphone-hints.png) |
| 21:41:09 | [214109-lamps-layout-2026-11-23-web-webkit-final-web-webkit-iphone-hold.png](214109-lamps-layout-2026-11-23-web-webkit-final-web-webkit-iphone-hold.png) |
| 21:41:09 | [214109-lamps-layout-2026-11-23-web-webkit-final-web-webkit-iphone-landscape-hints.png](214109-lamps-layout-2026-11-23-web-webkit-final-web-webkit-iphone-landscape-hints.png) |
| 21:41:09 | [214109-lamps-layout-2026-11-23-web-webkit-final-web-webkit-iphone-landscape-hold.png](214109-lamps-layout-2026-11-23-web-webkit-final-web-webkit-iphone-landscape-hold.png) |
| 21:41:09 | [214109-lamps-layout-2026-11-23-web-webkit-final-web-webkit-iphone-landscape-riding.png](214109-lamps-layout-2026-11-23-web-webkit-final-web-webkit-iphone-landscape-riding.png) |
| 21:41:09 | [214109-lamps-layout-2026-11-23-web-webkit-final-web-webkit-iphone-landscape-stopped.png](214109-lamps-layout-2026-11-23-web-webkit-final-web-webkit-iphone-landscape-stopped.png) |
| 21:41:09 | [214109-lamps-layout-2026-11-23-web-webkit-final-web-webkit-iphone-landscape.png](214109-lamps-layout-2026-11-23-web-webkit-final-web-webkit-iphone-landscape.png) |
| 21:41:09 | [214109-lamps-layout-2026-11-23-web-webkit-final-web-webkit-iphone-riding.png](214109-lamps-layout-2026-11-23-web-webkit-final-web-webkit-iphone-riding.png) |
| 21:41:09 | [214109-lamps-layout-2026-11-23-web-webkit-final-web-webkit-iphone-stopped.png](214109-lamps-layout-2026-11-23-web-webkit-final-web-webkit-iphone-stopped.png) |
| 21:41:09 | [214109-lamps-layout-2026-11-23-web-webkit-final-web-webkit-iphone.png](214109-lamps-layout-2026-11-23-web-webkit-final-web-webkit-iphone.png) |
| 21:41:09 | [214109-lamps-layout-2026-11-23-web-webkit-final-web-webkit-layout-android-360x640.png](214109-lamps-layout-2026-11-23-web-webkit-final-web-webkit-layout-android-360x640.png) |
| 21:41:09 | [214109-lamps-layout-2026-11-23-web-webkit-final-web-webkit-layout-android-640x360.png](214109-lamps-layout-2026-11-23-web-webkit-final-web-webkit-layout-android-640x360.png) |
| 21:41:09 | [214109-lamps-layout-2026-11-23-web-webkit-final-web-webkit-layout-iphone-390x844.png](214109-lamps-layout-2026-11-23-web-webkit-final-web-webkit-layout-iphone-390x844.png) |
| 21:41:09 | [214109-lamps-layout-2026-11-23-web-webkit-final-web-webkit-layout-iphone-844x390.png](214109-lamps-layout-2026-11-23-web-webkit-final-web-webkit-layout-iphone-844x390.png) |
| 21:41:09 | [214109-lamps-layout-2026-11-23-web-webkit-final-web-webkit-mac.png](214109-lamps-layout-2026-11-23-web-webkit-final-web-webkit-mac.png) |
| 21:42:08 | [214208-d797f262-dirty-shot-wayland-q10-woods-stop.jpg](214208-d797f262-dirty-shot-wayland-q10-woods-stop.jpg) |
| 21:43:12 | [214312-d797f262-dirty-video-wayland-q10-woods-crash-video.jpg](214312-d797f262-dirty-video-wayland-q10-woods-crash-video.jpg) |
| 21:43:12 | [214312-d797f262-dirty-video-wayland-q10-woods-crash-video.mp4](214312-d797f262-dirty-video-wayland-q10-woods-crash-video.mp4) |
| 21:43:46 | [214346-lamps-layout-2026-11-23-web-ios-final-lamp-bump-liechtenstein-1min.png](214346-lamps-layout-2026-11-23-web-ios-final-lamp-bump-liechtenstein-1min.png) |
| 21:43:46 | [214346-lamps-layout-2026-11-23-web-ios-final-lamp-bump-liechtenstein-end.png](214346-lamps-layout-2026-11-23-web-ios-final-lamp-bump-liechtenstein-end.png) |
| 21:43:46 | [214346-lamps-layout-2026-11-23-web-ios-final-lamp-bump-liechtenstein-lamp-after.png](214346-lamps-layout-2026-11-23-web-ios-final-lamp-bump-liechtenstein-lamp-after.png) |
| 21:43:46 | [214346-lamps-layout-2026-11-23-web-ios-final-lamp-bump-liechtenstein-lamp-approach.png](214346-lamps-layout-2026-11-23-web-ios-final-lamp-bump-liechtenstein-lamp-approach.png) |
| 21:43:46 | [214346-lamps-layout-2026-11-23-web-ios-final-lamp-bump-liechtenstein-lamp-bump.png](214346-lamps-layout-2026-11-23-web-ios-final-lamp-bump-liechtenstein-lamp-bump.png) |
| 21:43:46 | [214346-lamps-layout-2026-11-23-web-ios-final-lamp-bump-liechtenstein-start.png](214346-lamps-layout-2026-11-23-web-ios-final-lamp-bump-liechtenstein-start.png) |
| 21:44:32 | [214432-scenes-q10-woods-crash-video-1280.mp4](214432-scenes-q10-woods-crash-video-1280.mp4) |
| 21:54:41 | [215441-plant-origin-q10-tf-prickly-pear-after.jpg](215441-plant-origin-q10-tf-prickly-pear-after.jpg) |
| 21:55:00 | [215500-2971aee0-shot-ocw.jpg](215500-2971aee0-shot-ocw.jpg) |
| 21:55:10 | [215510-2971aee0-shot-wayland-ocw-wayland.jpg](215510-2971aee0-shot-wayland-ocw-wayland.jpg) |
| 21:55:11 | [215511-plant-origin-q10-tf-agave-after.jpg](215511-plant-origin-q10-tf-agave-after.jpg) |
| 21:55:40 | [215540-plant-origin-q10-tf-teide-broom-after.jpg](215540-plant-origin-q10-tf-teide-broom-after.jpg) |
| 21:55:55 | [215555-plant-origin-q10-li-green-alder-after.jpg](215555-plant-origin-q10-li-green-alder-after.jpg) |
| 21:55:57 | [215557-150c93d8-dirty-shot-wayland-q10-woods-stop.jpg](215557-150c93d8-dirty-shot-wayland-q10-woods-stop.jpg) |
| 21:56:24 | [215624-plant-origin-q10-tf-teide-broom-above-after.jpg](215624-plant-origin-q10-tf-teide-broom-above-after.jpg) |
| 21:56:40 | [215640-plant-origin-q10-li-green-alder-above-after.jpg](215640-plant-origin-q10-li-green-alder-above-after.jpg) |
| 21:57:11 | [215711-plant-origin-q10-tf-prickly-pear-after-files.jpg](215711-plant-origin-q10-tf-prickly-pear-after-files.jpg) |
| 21:57:21 | [215721-150c93d8-dirty-video-wayland-q10-woods-crash-video.jpg](215721-150c93d8-dirty-video-wayland-q10-woods-crash-video.jpg) |
| 21:57:21 | [215721-150c93d8-dirty-video-wayland-q10-woods-crash-video.mp4](215721-150c93d8-dirty-video-wayland-q10-woods-crash-video.mp4) |
| 21:57:39 | [215739-plant-origin-q10-tf-agave-after-files.jpg](215739-plant-origin-q10-tf-agave-after-files.jpg) |
| 21:58:11 | [215811-plant-origin-q10-tf-teide-broom-after-files.jpg](215811-plant-origin-q10-tf-teide-broom-after-files.jpg) |
| 21:58:27 | [215827-plant-origin-q10-li-green-alder-after-files.jpg](215827-plant-origin-q10-li-green-alder-after-files.jpg) |
| 21:58:59 | [215859-plant-origin-q10-tf-teide-broom-above-after-files.jpg](215859-plant-origin-q10-tf-teide-broom-above-after-files.jpg) |
| 21:59:14 | [215914-plant-origin-q10-li-green-alder-above-after-files.jpg](215914-plant-origin-q10-li-green-alder-above-after-files.jpg) |
| 22:05:34 | [220534-6320e4bc-dirty-shot-wayland-tf-teide-broom-above-before.jpg](220534-6320e4bc-dirty-shot-wayland-tf-teide-broom-above-before.jpg) |
| 22:05:50 | [220550-6320e4bc-dirty-shot-wayland-li-green-alder-above-before.jpg](220550-6320e4bc-dirty-shot-wayland-li-green-alder-above-before.jpg) |
| 22:07:23 | [220723-6320e4bc-dirty-shot-wayland-q11-face-closeup.jpg](220723-6320e4bc-dirty-shot-wayland-q11-face-closeup.jpg) |
| 22:07:34 | [220734-6320e4bc-dirty-shot-wayland-lips-speaking.jpg](220734-6320e4bc-dirty-shot-wayland-lips-speaking.jpg) |
| 22:11:29 | [221129-q11-unicorn-lips-compare-lips-speaking-mouth.jpg](221129-q11-unicorn-lips-compare-lips-speaking-mouth.jpg) |
| 22:11:29 | [221129-q11-unicorn-lips-compare-q11-face-closeup-mouth.jpg](221129-q11-unicorn-lips-compare-q11-face-closeup-mouth.jpg) |
| 22:41:24 | [224124-lamps-layout-2026-11-23-web-webkit-final2-web-webkit-iphone-hints.png](224124-lamps-layout-2026-11-23-web-webkit-final2-web-webkit-iphone-hints.png) |
| 22:41:24 | [224124-lamps-layout-2026-11-23-web-webkit-final2-web-webkit-iphone-hold.png](224124-lamps-layout-2026-11-23-web-webkit-final2-web-webkit-iphone-hold.png) |
| 22:41:24 | [224124-lamps-layout-2026-11-23-web-webkit-final2-web-webkit-iphone-landscape-hints.png](224124-lamps-layout-2026-11-23-web-webkit-final2-web-webkit-iphone-landscape-hints.png) |
| 22:41:24 | [224124-lamps-layout-2026-11-23-web-webkit-final2-web-webkit-iphone-landscape-hold.png](224124-lamps-layout-2026-11-23-web-webkit-final2-web-webkit-iphone-landscape-hold.png) |
| 22:41:24 | [224124-lamps-layout-2026-11-23-web-webkit-final2-web-webkit-iphone-landscape-riding.png](224124-lamps-layout-2026-11-23-web-webkit-final2-web-webkit-iphone-landscape-riding.png) |
| 22:41:24 | [224124-lamps-layout-2026-11-23-web-webkit-final2-web-webkit-iphone-landscape-stopped.png](224124-lamps-layout-2026-11-23-web-webkit-final2-web-webkit-iphone-landscape-stopped.png) |
| 22:41:24 | [224124-lamps-layout-2026-11-23-web-webkit-final2-web-webkit-iphone-landscape.png](224124-lamps-layout-2026-11-23-web-webkit-final2-web-webkit-iphone-landscape.png) |
| 22:41:24 | [224124-lamps-layout-2026-11-23-web-webkit-final2-web-webkit-iphone-riding.png](224124-lamps-layout-2026-11-23-web-webkit-final2-web-webkit-iphone-riding.png) |
| 22:41:24 | [224124-lamps-layout-2026-11-23-web-webkit-final2-web-webkit-iphone-stopped.png](224124-lamps-layout-2026-11-23-web-webkit-final2-web-webkit-iphone-stopped.png) |
| 22:41:24 | [224124-lamps-layout-2026-11-23-web-webkit-final2-web-webkit-iphone.png](224124-lamps-layout-2026-11-23-web-webkit-final2-web-webkit-iphone.png) |
| 22:41:24 | [224124-lamps-layout-2026-11-23-web-webkit-final2-web-webkit-layout-android-360x640.png](224124-lamps-layout-2026-11-23-web-webkit-final2-web-webkit-layout-android-360x640.png) |
| 22:41:24 | [224124-lamps-layout-2026-11-23-web-webkit-final2-web-webkit-layout-android-640x360.png](224124-lamps-layout-2026-11-23-web-webkit-final2-web-webkit-layout-android-640x360.png) |
| 22:41:24 | [224124-lamps-layout-2026-11-23-web-webkit-final2-web-webkit-layout-iphone-390x844.png](224124-lamps-layout-2026-11-23-web-webkit-final2-web-webkit-layout-iphone-390x844.png) |
| 22:41:24 | [224124-lamps-layout-2026-11-23-web-webkit-final2-web-webkit-layout-iphone-844x390.png](224124-lamps-layout-2026-11-23-web-webkit-final2-web-webkit-layout-iphone-844x390.png) |
| 22:41:24 | [224124-lamps-layout-2026-11-23-web-webkit-final2-web-webkit-mac.png](224124-lamps-layout-2026-11-23-web-webkit-final2-web-webkit-mac.png) |
| 22:45:03 | [224503-j6-sides-plan-letzanaweg-j5.png](224503-j6-sides-plan-letzanaweg-j5.png) |
| 23:03:13 | [230313-j6-sides-zoom-letzanaweg-j5.png](230313-j6-sides-zoom-letzanaweg-j5.png) |
| 23:05:16 | [230516-j6-sides-plan-letzanaweg-j6.png](230516-j6-sides-plan-letzanaweg-j6.png) |
| 23:05:18 | [230518-j6-sides-zoom-letzanaweg-j6.png](230518-j6-sides-zoom-letzanaweg-j6.png) |
| 23:07:34 | [230734-lamps-layout-2026-11-23-web-webkit-merge-web-webkit-iphone-hints.png](230734-lamps-layout-2026-11-23-web-webkit-merge-web-webkit-iphone-hints.png) |
| 23:07:34 | [230734-lamps-layout-2026-11-23-web-webkit-merge-web-webkit-iphone-hold.png](230734-lamps-layout-2026-11-23-web-webkit-merge-web-webkit-iphone-hold.png) |
| 23:07:34 | [230734-lamps-layout-2026-11-23-web-webkit-merge-web-webkit-iphone-landscape-hints.png](230734-lamps-layout-2026-11-23-web-webkit-merge-web-webkit-iphone-landscape-hints.png) |
| 23:07:34 | [230734-lamps-layout-2026-11-23-web-webkit-merge-web-webkit-iphone-landscape-hold.png](230734-lamps-layout-2026-11-23-web-webkit-merge-web-webkit-iphone-landscape-hold.png) |
| 23:07:34 | [230734-lamps-layout-2026-11-23-web-webkit-merge-web-webkit-iphone-landscape-riding.png](230734-lamps-layout-2026-11-23-web-webkit-merge-web-webkit-iphone-landscape-riding.png) |
| 23:07:34 | [230734-lamps-layout-2026-11-23-web-webkit-merge-web-webkit-iphone-landscape-stopped.png](230734-lamps-layout-2026-11-23-web-webkit-merge-web-webkit-iphone-landscape-stopped.png) |
| 23:07:34 | [230734-lamps-layout-2026-11-23-web-webkit-merge-web-webkit-iphone-landscape.png](230734-lamps-layout-2026-11-23-web-webkit-merge-web-webkit-iphone-landscape.png) |
| 23:07:34 | [230734-lamps-layout-2026-11-23-web-webkit-merge-web-webkit-iphone-riding.png](230734-lamps-layout-2026-11-23-web-webkit-merge-web-webkit-iphone-riding.png) |
| 23:07:34 | [230734-lamps-layout-2026-11-23-web-webkit-merge-web-webkit-iphone-stopped.png](230734-lamps-layout-2026-11-23-web-webkit-merge-web-webkit-iphone-stopped.png) |
| 23:07:34 | [230734-lamps-layout-2026-11-23-web-webkit-merge-web-webkit-iphone.png](230734-lamps-layout-2026-11-23-web-webkit-merge-web-webkit-iphone.png) |
| 23:07:34 | [230734-lamps-layout-2026-11-23-web-webkit-merge-web-webkit-layout-android-360x640.png](230734-lamps-layout-2026-11-23-web-webkit-merge-web-webkit-layout-android-360x640.png) |
| 23:07:34 | [230734-lamps-layout-2026-11-23-web-webkit-merge-web-webkit-layout-android-640x360.png](230734-lamps-layout-2026-11-23-web-webkit-merge-web-webkit-layout-android-640x360.png) |
| 23:07:34 | [230734-lamps-layout-2026-11-23-web-webkit-merge-web-webkit-layout-iphone-390x844.png](230734-lamps-layout-2026-11-23-web-webkit-merge-web-webkit-layout-iphone-390x844.png) |
| 23:07:34 | [230734-lamps-layout-2026-11-23-web-webkit-merge-web-webkit-layout-iphone-844x390.png](230734-lamps-layout-2026-11-23-web-webkit-merge-web-webkit-layout-iphone-844x390.png) |
| 23:07:34 | [230734-lamps-layout-2026-11-23-web-webkit-merge-web-webkit-mac.png](230734-lamps-layout-2026-11-23-web-webkit-merge-web-webkit-mac.png) |
| 23:10:10 | [231010-lamps-layout-2026-11-23-web-ios-merge-lamp-bump-liechtenstein-1min.png](231010-lamps-layout-2026-11-23-web-ios-merge-lamp-bump-liechtenstein-1min.png) |
| 23:10:10 | [231010-lamps-layout-2026-11-23-web-ios-merge-lamp-bump-liechtenstein-end.png](231010-lamps-layout-2026-11-23-web-ios-merge-lamp-bump-liechtenstein-end.png) |
| 23:10:10 | [231010-lamps-layout-2026-11-23-web-ios-merge-lamp-bump-liechtenstein-lamp-after.png](231010-lamps-layout-2026-11-23-web-ios-merge-lamp-bump-liechtenstein-lamp-after.png) |
| 23:10:10 | [231010-lamps-layout-2026-11-23-web-ios-merge-lamp-bump-liechtenstein-lamp-approach.png](231010-lamps-layout-2026-11-23-web-ios-merge-lamp-bump-liechtenstein-lamp-approach.png) |
| 23:10:10 | [231010-lamps-layout-2026-11-23-web-ios-merge-lamp-bump-liechtenstein-lamp-bump.png](231010-lamps-layout-2026-11-23-web-ios-merge-lamp-bump-liechtenstein-lamp-bump.png) |
| 23:10:10 | [231010-lamps-layout-2026-11-23-web-ios-merge-lamp-bump-liechtenstein-start.png](231010-lamps-layout-2026-11-23-web-ios-merge-lamp-bump-liechtenstein-start.png) |
| 23:11:33 | [231133-lamps-layout-2026-11-23-web-ios-merge-merge-liechtenstein-1min.png](231133-lamps-layout-2026-11-23-web-ios-merge-merge-liechtenstein-1min.png) |
| 23:11:33 | [231133-lamps-layout-2026-11-23-web-ios-merge-merge-liechtenstein-2min.png](231133-lamps-layout-2026-11-23-web-ios-merge-merge-liechtenstein-2min.png) |
| 23:11:33 | [231133-lamps-layout-2026-11-23-web-ios-merge-merge-liechtenstein-3min.png](231133-lamps-layout-2026-11-23-web-ios-merge-merge-liechtenstein-3min.png) |
| 23:11:33 | [231133-lamps-layout-2026-11-23-web-ios-merge-merge-liechtenstein-4min.png](231133-lamps-layout-2026-11-23-web-ios-merge-merge-liechtenstein-4min.png) |
| 23:11:33 | [231133-lamps-layout-2026-11-23-web-ios-merge-merge-liechtenstein-5min.png](231133-lamps-layout-2026-11-23-web-ios-merge-merge-liechtenstein-5min.png) |
| 23:11:33 | [231133-lamps-layout-2026-11-23-web-ios-merge-merge-liechtenstein-context-reloaded.png](231133-lamps-layout-2026-11-23-web-ios-merge-merge-liechtenstein-context-reloaded.png) |
| 23:11:33 | [231133-lamps-layout-2026-11-23-web-ios-merge-merge-liechtenstein-end.png](231133-lamps-layout-2026-11-23-web-ios-merge-merge-liechtenstein-end.png) |
| 23:11:33 | [231133-lamps-layout-2026-11-23-web-ios-merge-merge-liechtenstein-start.png](231133-lamps-layout-2026-11-23-web-ios-merge-merge-liechtenstein-start.png) |
| 23:19:19 | [231919-j6-sides-li-letzanaweg-corner-j6.jpg](231919-j6-sides-li-letzanaweg-corner-j6.jpg) |
| 23:19:35 | [231935-j6-sides-li-letzanaweg-side-j6.jpg](231935-j6-sides-li-letzanaweg-side-j6.jpg) |
| 23:23:00 | [232300-j6-sides-li-letzanaweg-joint-j5.jpg](232300-j6-sides-li-letzanaweg-joint-j5.jpg) |
| 23:23:00 | [232300-j6-sides-li-letzanaweg-joint-j6.jpg](232300-j6-sides-li-letzanaweg-joint-j6.jpg) |
| 23:28:31 | [232831-j6-sides-case-cluster9.png](232831-j6-sides-case-cluster9.png) |
| 23:28:36 | [232836-j6-sides-case-short57.png](232836-j6-sides-case-short57.png) |
| 23:28:40 | [232840-j6-sides-case-other291.png](232840-j6-sides-case-other291.png) |
| 23:28:44 | [232844-j6-sides-case-short100.png](232844-j6-sides-case-short100.png) |
| 23:29:49 | [232949-lamps-layout-2026-11-23-web-ios-main-main-liechtenstein-1min.png](232949-lamps-layout-2026-11-23-web-ios-main-main-liechtenstein-1min.png) |
| 23:29:49 | [232949-lamps-layout-2026-11-23-web-ios-main-main-liechtenstein-2min.png](232949-lamps-layout-2026-11-23-web-ios-main-main-liechtenstein-2min.png) |
| 23:29:49 | [232949-lamps-layout-2026-11-23-web-ios-main-main-liechtenstein-3min.png](232949-lamps-layout-2026-11-23-web-ios-main-main-liechtenstein-3min.png) |
| 23:29:49 | [232949-lamps-layout-2026-11-23-web-ios-main-main-liechtenstein-4min.png](232949-lamps-layout-2026-11-23-web-ios-main-main-liechtenstein-4min.png) |
| 23:29:49 | [232949-lamps-layout-2026-11-23-web-ios-main-main-liechtenstein-5min.png](232949-lamps-layout-2026-11-23-web-ios-main-main-liechtenstein-5min.png) |
| 23:29:49 | [232949-lamps-layout-2026-11-23-web-ios-main-main-liechtenstein-context-reloaded.png](232949-lamps-layout-2026-11-23-web-ios-main-main-liechtenstein-context-reloaded.png) |
| 23:29:49 | [232949-lamps-layout-2026-11-23-web-ios-main-main-liechtenstein-end.png](232949-lamps-layout-2026-11-23-web-ios-main-main-liechtenstein-end.png) |
| 23:29:49 | [232949-lamps-layout-2026-11-23-web-ios-main-main-liechtenstein-start.png](232949-lamps-layout-2026-11-23-web-ios-main-main-liechtenstein-start.png) |
| 23:42:22 | [234222-lamps-layout-2026-11-23-web-ios-merge2-merge2-liechtenstein-1min.png](234222-lamps-layout-2026-11-23-web-ios-merge2-merge2-liechtenstein-1min.png) |
| 23:42:22 | [234222-lamps-layout-2026-11-23-web-ios-merge2-merge2-liechtenstein-2min.png](234222-lamps-layout-2026-11-23-web-ios-merge2-merge2-liechtenstein-2min.png) |
| 23:42:22 | [234222-lamps-layout-2026-11-23-web-ios-merge2-merge2-liechtenstein-3min.png](234222-lamps-layout-2026-11-23-web-ios-merge2-merge2-liechtenstein-3min.png) |
| 23:42:22 | [234222-lamps-layout-2026-11-23-web-ios-merge2-merge2-liechtenstein-4min.png](234222-lamps-layout-2026-11-23-web-ios-merge2-merge2-liechtenstein-4min.png) |
| 23:42:22 | [234222-lamps-layout-2026-11-23-web-ios-merge2-merge2-liechtenstein-5min.png](234222-lamps-layout-2026-11-23-web-ios-merge2-merge2-liechtenstein-5min.png) |
| 23:42:22 | [234222-lamps-layout-2026-11-23-web-ios-merge2-merge2-liechtenstein-context-reloaded.png](234222-lamps-layout-2026-11-23-web-ios-merge2-merge2-liechtenstein-context-reloaded.png) |
| 23:42:22 | [234222-lamps-layout-2026-11-23-web-ios-merge2-merge2-liechtenstein-end.png](234222-lamps-layout-2026-11-23-web-ios-merge2-merge2-liechtenstein-end.png) |
| 23:42:22 | [234222-lamps-layout-2026-11-23-web-ios-merge2-merge2-liechtenstein-start.png](234222-lamps-layout-2026-11-23-web-ios-merge2-merge2-liechtenstein-start.png) |
| 23:48:11 | [234811-lamps-layout-2026-11-23-web-ios-merge2-lamp-bump-liechtenstein-end.png](234811-lamps-layout-2026-11-23-web-ios-merge2-lamp-bump-liechtenstein-end.png) |
| 23:48:11 | [234811-lamps-layout-2026-11-23-web-ios-merge2-lamp-bump-liechtenstein-lamp-after.png](234811-lamps-layout-2026-11-23-web-ios-merge2-lamp-bump-liechtenstein-lamp-after.png) |
| 23:48:11 | [234811-lamps-layout-2026-11-23-web-ios-merge2-lamp-bump-liechtenstein-lamp-approach.png](234811-lamps-layout-2026-11-23-web-ios-merge2-lamp-bump-liechtenstein-lamp-approach.png) |
| 23:48:11 | [234811-lamps-layout-2026-11-23-web-ios-merge2-lamp-bump-liechtenstein-lamp-bump.png](234811-lamps-layout-2026-11-23-web-ios-merge2-lamp-bump-liechtenstein-lamp-bump.png) |
| 23:48:11 | [234811-lamps-layout-2026-11-23-web-ios-merge2-lamp-bump-liechtenstein-start.png](234811-lamps-layout-2026-11-23-web-ios-merge2-lamp-bump-liechtenstein-start.png) |
| 23:52:50 | [235250-lamps-layout-2026-11-23-web-webkit-merge2-web-webkit-iphone-hints.png](235250-lamps-layout-2026-11-23-web-webkit-merge2-web-webkit-iphone-hints.png) |
| 23:52:50 | [235250-lamps-layout-2026-11-23-web-webkit-merge2-web-webkit-iphone-hold.png](235250-lamps-layout-2026-11-23-web-webkit-merge2-web-webkit-iphone-hold.png) |
| 23:52:50 | [235250-lamps-layout-2026-11-23-web-webkit-merge2-web-webkit-iphone-landscape-hints.png](235250-lamps-layout-2026-11-23-web-webkit-merge2-web-webkit-iphone-landscape-hints.png) |
| 23:52:50 | [235250-lamps-layout-2026-11-23-web-webkit-merge2-web-webkit-iphone-landscape-hold.png](235250-lamps-layout-2026-11-23-web-webkit-merge2-web-webkit-iphone-landscape-hold.png) |
| 23:52:50 | [235250-lamps-layout-2026-11-23-web-webkit-merge2-web-webkit-iphone-landscape-riding.png](235250-lamps-layout-2026-11-23-web-webkit-merge2-web-webkit-iphone-landscape-riding.png) |
| 23:52:50 | [235250-lamps-layout-2026-11-23-web-webkit-merge2-web-webkit-iphone-landscape-stopped.png](235250-lamps-layout-2026-11-23-web-webkit-merge2-web-webkit-iphone-landscape-stopped.png) |
| 23:52:50 | [235250-lamps-layout-2026-11-23-web-webkit-merge2-web-webkit-iphone-landscape.png](235250-lamps-layout-2026-11-23-web-webkit-merge2-web-webkit-iphone-landscape.png) |
| 23:52:50 | [235250-lamps-layout-2026-11-23-web-webkit-merge2-web-webkit-iphone-riding.png](235250-lamps-layout-2026-11-23-web-webkit-merge2-web-webkit-iphone-riding.png) |
| 23:52:50 | [235250-lamps-layout-2026-11-23-web-webkit-merge2-web-webkit-iphone-stopped.png](235250-lamps-layout-2026-11-23-web-webkit-merge2-web-webkit-iphone-stopped.png) |
| 23:52:50 | [235250-lamps-layout-2026-11-23-web-webkit-merge2-web-webkit-iphone.png](235250-lamps-layout-2026-11-23-web-webkit-merge2-web-webkit-iphone.png) |
| 23:52:50 | [235250-lamps-layout-2026-11-23-web-webkit-merge2-web-webkit-layout-android-360x640.png](235250-lamps-layout-2026-11-23-web-webkit-merge2-web-webkit-layout-android-360x640.png) |
| 23:52:50 | [235250-lamps-layout-2026-11-23-web-webkit-merge2-web-webkit-layout-android-640x360.png](235250-lamps-layout-2026-11-23-web-webkit-merge2-web-webkit-layout-android-640x360.png) |
| 23:52:50 | [235250-lamps-layout-2026-11-23-web-webkit-merge2-web-webkit-layout-iphone-390x844.png](235250-lamps-layout-2026-11-23-web-webkit-merge2-web-webkit-layout-iphone-390x844.png) |
| 23:52:50 | [235250-lamps-layout-2026-11-23-web-webkit-merge2-web-webkit-layout-iphone-844x390.png](235250-lamps-layout-2026-11-23-web-webkit-merge2-web-webkit-layout-iphone-844x390.png) |
| 23:52:50 | [235250-lamps-layout-2026-11-23-web-webkit-merge2-web-webkit-mac.png](235250-lamps-layout-2026-11-23-web-webkit-merge2-web-webkit-mac.png) |
| 23:58:36 | [235836-j6-sides-li-letzanaweg-corner-j6.jpg](235836-j6-sides-li-letzanaweg-corner-j6.jpg) |
| 23:58:51 | [235851-j6-sides-li-letzanaweg-side-j6.jpg](235851-j6-sides-li-letzanaweg-side-j6.jpg) |
| 23:59:06 | [235906-j6-sides-li-t-j6.jpg](235906-j6-sides-li-t-j6.jpg) |
| 23:59:21 | [235921-j6-sides-li-fork-j6.jpg](235921-j6-sides-li-fork-j6.jpg) |
| 23:59:35 | [235935-j6-sides-li-path-j6.jpg](235935-j6-sides-li-path-j6.jpg) |
