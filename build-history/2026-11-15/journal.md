# OCW build diary – day 5, 2026-11-15

97 commits (30 merges), +33083 / −2643 lines, 523 images, 9 videos, 0 sounds.

## Commits

| Time | Commit | |
|---|---|---|
| 00:00 | `9ea2fd0` | Spec 3.36: public preview of the browser app on GitHub Pages (B8a, stage 1) |
| 00:01 | `8ea61cc` | Art: collector tests never touch the real archive; gather's sources honour OCW_TEST_OUTPUT (no agent worktrees then) |
| 00:01 | `965431b` | Phase 7: cargo fmt |
| 00:16 | `ed4da5f` | Phase 7: clippy (duplicate allow, test-only helpers, a type alias) |
| 00:21 | `098915a` (merge) | Merge branch 'main' into worktree-agent-a43d6ec0bd80728f8 |
| 06:15 | `9212b31` | wip: browser setup |
| 06:15 | `3e6cf9e` | Unicorn mode in the browser (spec §14 Phase 13 G5): god mode shared as ocw_ui::god |
| 06:15 | `ee4ad6f` | Art: more varied music and a style per day (spec 3.37, ART-PROJECT 1.6 §3.2, §4) |
| 06:15 | `00bed8b` (merge) | Merge main (spec 3.36) into the animations / K6 branch; this work becomes spec 3.37 |
| 06:15 | `4e43b82` (merge) | Merge branch 'main' into worktree-agent-ab18479c7c2ff5bd4 |
| 06:15 | `9adc4fd` (merge) | Merge branch 'main' into worktree-agent-ab2216bf39859444d |
| 06:15 | `3fdb5f8` (merge) | Merge main (spec 3.36); unicorn mode in the browser becomes spec 3.37 |
| 06:17 | `b0a7126` | U-turn cue regression test; scene timings; version references 3.37 |
| 06:27 | `8f5f1b3` | Art: incident log (spec 3.38, ART-PROJECT 1.7 §2.6); mask list found from worktrees; dashboard unit memory cap |
| 06:44 | `499b9a2` | Art: incident note 01:05 - correct the publish times |
| 06:44 | `9c2044d` (merge) | Merge art project: hermetic collector tests, varied per-day music (art/music.py, five styles), incident log with root-cause notes, dashboard memory cap (spec 3.37, 3.38) |
| 06:46 | `36d9c9e` | Art: re-masked journals and token counts of days 1–4, today's journals and the first incident notes (00:39 OOM, the masking slip) |
| 06:46 | `a8c519f` | WIP console Tab completion and GPS line |
| 06:46 | `b7b2a7e` (merge) | Merge main into the console completion / GPS branch |
| 07:03 | `d9a9b05` (merge) | Merge Unicorn mode in the browser: god-mode glue shared in ocw-ui (flight, touch, inspection, HUD), Pointer Lock in the browser, test-web-unicorn (spec 3.39) |
| 07:04 | `4dc6f23` (merge) | Merge main (unicorn mode in the browser) into the console completion / GPS branch; spec 3.40 |
| 07:09 | `9cb2372` | Browser app setup: web-serve guard, make web-remote, WEB_BIND, pinned Chromium, README walkthrough test (spec 3.37) |
| 07:15 | `85c04fd` (merge) | Merge branch 'main' into worktree-agent-ab18479c7c2ff5bd4 |
| 07:15 | `6348358` | HUD: the top panel stays clear of the top-right column at every HUD size; bindings for the shared unicorn mode (spec 3.40) |
| 07:22 | `719fe40` | ocw-ui god: cargo fmt |
| 07:27 | `371ffb4` | ocw-ui menu test: unicorn rows on Controls -> Unicorn mode after the merge |
| 07:41 | `a08c638` | Art: features log and agent jobs in the journal, "Today's features" roll (spec 3.40, ART-PROJECT 1.8 §2.7) |
| 07:51 | `559f594` | Helmets (spec §2.6): sculpted road-style shells with vents, rim, retention band and straps, two-tone; TT teardrop with tail and visor; tests |
| 07:51 | `e3364d8` (merge) | Merge main into the helmet rework (spec 3.40) |
| 07:52 | `163da1e` | Helmets: spec references 3.40 |
| 07:52 | `ed821d6` (merge) | Merge browser setup fixes: web-serve stops without a build, make web-remote, WEB_BIND, cargo profile web-release, pinned Chromium 157 for the browser tests, make test-web-readme (spec 3.40) |
| 07:52 | `b28542c` (merge) | Merge art features log: Features and Agent jobs in the journal, agent-event, commit in the build log, deploys log, Today's features roll (spec 3.41) |
| 07:52 | `59f1f44` | Helmets: type aliases (clippy) |
| 07:55 | `1c1aefe` | ocw-ui menu test: cargo fmt |
| 07:55 | `7ccb1ea` | WIP sign-in with Google and Strava (spec §9.1): ocw-auth, ocw-accounts backend, game server token check, Account page (desktop, browser) |
| 07:55 | `3d15557` (merge) | Merge main into the sign-in branch |
| 07:56 | `b64711c` | Spec 3.42: sign-in build note (§9.1.1, Phase 5) |
| 07:56 | `47540c5` | Cargo.lock after the merge |
| 07:57 | `14e09b4` | README: Accounts and sign-in (users, operator setup: Google client, Strava app, config, redirect URIs) |
| 07:58 | `2574052` | Account page screenshots against the fake providers (scripts/test-account-pages.sh); OCW_ACCOUNT_FILE |
| 07:59 | `d5d52b2` | Sign-in: OCW_OPEN_URL (not the browser tests' OCW_BROWSER) names the desktop's browser command |
| 08:00 | `f74e76c` | WIP B8a: web preview (page config, preview root, site assembly, workflow) |
| 08:01 | `bc5df14` | Sign-in: the fake Google's RSA key made at run time (no private key in the repository), axum's get no longer shadowed; make test-web-account |
| 08:02 | `e8f6cdc` | accounts: code redemption without holding the state lock across the match |
| 08:02 | `1c48027` (merge) | Merge main into the B8a web preview branch (profile web-preview-release, pinned test browser) |
| 08:04 | `f883a5b` | Console Tab completion and the GPS line (spec 3.40): hud-gps-route scene rides the package route by its name |
| 08:04 | `94d30e3` | B8a: publish-preview-worlds.sh names the repository for gh (build checkouts have no .git); README profile names |
| 08:05 | `e6dafa2` | accounts: build fixes (Strava client type, borrows) |
| 08:05 | `316a4ec` | WIP vegetation: flora species rules, VEGE section, plantings rows, planted-tree obstacles |
| 08:05 | `1b4cded` (merge) | Merge main into vegetation |
| 08:11 | `1b1dc2b` | Helmets: narrower dark side band, shorter TT visor; models regenerated |
| 08:11 | `9141b51` | Sign-in: clippy fixes (desktop menu pages list, link URL borrow, boxed Welcome in the server test) |
| 08:19 | `8955bf2` | Sign-in: the example config lives in services/accounts (remote.sh never copies config/) |
| 08:25 | `45730a5` | WIP vegetation: species models, tile plants in near/far chunks, VEGE builder, crop share in the colour map |
| 08:30 | `85db4ca` | WIP vegetation: build scripts, spots, VEGE spec, README, far conifer tone |
| 08:41 | `e52ae73` | WIP vegetation: measured crop maps (EUCROPMAP 2022, Mapa de Cultivos de Canarias), tuned tables |
| 08:43 | `e145767` | WIP vegetation: spec §4.6.1 research tables and data sources, version 3.42 |
| 08:45 | `3613063` | ocw-ui test: Display is the fifth Settings item now (Account first) |
| 08:46 | `a96c869` | WIP vegetation: fmt, small fixes |
| 08:46 | `c926016` (merge) | Merge Phase 7: training history (rides, totals, bests, power curve, FIT import/export) and M9 key/button rebinding with accessibility options; HUD panel stays clear of the FPS column (spec 3.42) |
| 08:47 | `5e96eb2` (merge) | Merge console Tab completion and the GPS line restored (route rides kept no geographic origin since fae1547), rider.gps and hud.gps in both apps, browser origin= option (spec 3.43) |
| 08:48 | `9848f41` | WIP vegetation: float-safe flora tests |
| 08:48 | `62eb12a` (merge) | Merge main (Phase 7, shared unicorn mode, browser setup; spec 3.42) into the animations / K6 branch; this work becomes spec 3.44 |
| 08:48 | `06f5768` (merge) | Merge main (spec 3.43 console completion, GPS line) |
| 09:07 | `cfaad72` | B8a: web-preview-release at opt-level z (measured), WEB_WASM_OPT=off, README notes |
| 09:10 | `f8ca730` | Helmets: rustfmt |
| 09:11 | `15f4104` | B8a: spec build note (sizes, trust, worlds, workflow), README sizes |
| 09:12 | `e80662d` | desktop account: clippy (OpenUrl type, userinfo only in tests) |
| 09:21 | `f2d8fef` | WIP vegetation: quality test for the far tree range; drive.sh OCW_APP |
| 09:23 | `35be02d` | WIP vegetation: dragon tree tufts sway with their height |
| 09:28 | `6106e44` | WIP vegetation: clippy |
| 09:29 | `189bada` | WIP vegetation: spec Phase 8 T8 notes |
| 09:46 | `5410232` (merge) | Merge cooler helmets: sculpted road / lightweight / aero road shells with vents, two-tone, retention band and straps; TT teardrop with wrap visor; no clipping with hair, caps and glasses (spec 3.44) |
| 09:47 | `0ff7a70` (merge) | Merge main (spec 3.44 helmets); this work becomes spec 3.45 |
| 10:03 | `a6a05a5` | WIP vegetation: scenes veg-li-*, veg-tf-* |
| 10:08 | `0ca2f20` | B8a: the preview's line in the ride above the height profile (clear of the route label) |
| 10:08 | `ebec766` | B8a: spec and README: site size, test results, open points |
| 10:32 | `d6e843e` | WIP vegetation: scenes veg-bf-* |
| 10:33 | `f085e50` | test-account-pages: open the Account page at the start (software rendering is slow) |
| 10:42 | `8ab9209` (merge) | Merge B8a public preview on GitHub Pages: size-optimised preview build (wasm-opt, fat LTO), preview signing root, page config, start and credits pages, signed Liechtenstein release asset, Pages workflow, README link (spec 3.45) |
| 10:43 | `226d3fe` (merge) | Merge main (spec 3.45 GitHub Pages preview); this work becomes spec 3.46 |
| 10:51 | `96c6062` | WIP vegetation: detail chunks for bananas and vines, lighter banana model, rounded vine canopy, species-relative scale, palms and Canary pines refined |
| 10:55 | `4d33012` | Spec 3.42: the browser sign-in test and the screenshots in §9.1.1 |
| 10:56 | `114666b` | Renumber the animations / K6 version to spec 3.47 |
| 10:56 | `beb5a4e` | Sign-in tests and fakes: fictional names (Ada Rider, Bea Climber, Cleo Sprinter, Dora Tempo) instead of real riders |
| 10:57 | `8796545` (merge) | Merge main (3.45) into the sign-in branch; sign-in is spec 3.46 |
| 11:20 | `594e8c1` (merge) | Merge rider animations (foot down, cornering, U-turn look, finish throw, victory) and Phase 12 K6 organiser rules (aids, chaotic bots, time limit, service wait, DNF reasons) (spec 3.47) |
| 11:21 | `bb11aa0` (merge) | Merge main (3.47) into the sign-in branch; sign-in stays 3.46 below 3.47 |
| 11:37 | `53a853b` | WIP vegetation: bumpy crop stands, varied autumn vines, longer fruit blossom |
| 11:48 | `42b48df` | B8a: the public preview is live on GitHub Pages – live test passed, Pages gzips the wasm (spec B8a note, README) |
| 12:15 | `1f2a0da` | Spec Phase 8 T8: packages, frame rate, renders, tests, open points |
| 12:16 | `bbed3f1` | Spec: Phase 8 heading and §4.6 point to T8 |
| 12:16 | `866a5a2` (merge) | Merge main into vegetation (spec version 3.48) |
| 12:18 | `e2b4bda` (merge) | Merge sign-in with Google and Strava: ocw-auth, the ocw-accounts backend (OIDC-shaped endpoints, device flow, rotation, export/delete), game-server token check, Settings → Account in both apps; fictional test identities (spec 3.46) |
| 12:21 | `a88498c` | Coordinator move nils@deb -> user@deb: checklist (docs/MIGRATE-DEB-USER.md) and root copy script (scripts/migrate-user.sh, dry run by default) |
| 13:14 | `331a29f` | Plan Phase 15 (3D objects as glTF model files in artwork/3dmodels: format comparison, model contract, import/export/loader, migration M1-M6) and Phase 16 (OCW Studio: models, world patches, GPX routes, routing planners with licence check) (spec 3.48) |
| 13:15 | `259934b` (merge) | Merge realistic vegetation (Phase 8 T8): flora species, VEGE crops and plantations, planted trees in OBST, world-builder vegetation, flora/vegetation renderer (spec 3.49) |

## Builds and build servers

131 build/test runs on the build machines, 47.4 h in total, 11 failed; 796 server samples; cargo compiled 2581 crates in 1.8 h, 25.7 h waiting for build slots.

| Machine | Runs | Hours | Cargo h | Crates | Waited h | Failed | Online |
|---|---|---|---|---|---|---|---|
| Win11Builder | 7 | 2.3 | 0.0 | 0 | 1.0 | 0 | 100% |
| leela | 7 | 0.8 | 0.5 | 6 | 0.0 | 2 | 36% |
| macos | 47 | 4.6 | 0.1 | 23 | 2.3 | 5 | 100% |
| marge | 70 | 39.6 | 1.2 | 2552 | 22.4 | 4 | 100% |

Failed runs:

- 00:09 macos: `cargo fmt -p ocw-xr -p ocw-assets && cargo test -p ocw-xr 2>&1 | tail -40 && car` (exit 129, log `build-log/000938-macos-3079424.log`)
- 00:16 macos: `cd vendor && (time CARGO_TARGET_DIR=../target cargo check --workspace --examples` (exit 1, log `build-log/001625-macos-3091403.log`)
- 00:13 marge: `make test-web-readme README_FLAGS="--keep --reuse-target"` (exit 2, log `build-log/001311-marge-3085504.log`)
- 06:15 marge: `make test-web-readme README_FLAGS="--keep --reuse-target"` (exit 2, log `build-log/061555-marge-3409112.log`)
- 06:46 marge: `scripts/render-scenes.sh --out test-output/scenes/2026-11-15-064652 --only conso` (exit 1, log `build-log/064652-marge-3455729.log`)
- 07:57 macos: `bash scripts/vr-check.sh crates` (exit 101, log `build-log/075749-macos-3557578.log`)
- 07:59 macos: `bash scripts/vr-check.sh crates` (exit 101, log `build-log/075923-macos-3559476.log`)
- 08:01 macos: `bash scripts/vr-check.sh crates` (exit 1, log `build-log/080106-macos-3562224.log`)
- 09:20 leela: `   set -e   D=/var/tmp/ocw   put() { install -m $1 "$2" "$D/.$3.new" && mv -f "$` (exit 255, log `build-log/092051-leela-3657912.log`)
- 08:46 marge: `bash scripts/vr-check.sh full` (exit 1, log `build-log/084611-marge-3616020.log`)
- 10:17 leela: `   set -e   D=/var/tmp/ocw   put() { install -m $1 "$2" "$D/.$3.new" && mv -f "$` (exit 255, log `build-log/101718-leela-3713165.log`)

Longest runs:

- 100 min on marge: `df -h ~ | tail -1; mkdir -p test-output/veg; (time scripts/build-liechtenstein.s`
- 74 min on marge: `r(){ n=$1; shift; if "$@" > /tmp/ocw-a61e-$n.log 2>&1; then echo "=== $n OK"; el`
- 71 min on marge: `cargo clippy --workspace --all-targets --keep-going -- -D warnings > /tmp/ocw-a6`
- 69 min on marge: `scripts/render-scenes.sh --out test-output/scenes/helmets-after-x11 --only 'helm`
- 64 min on marge: `bash scripts/tmp-measure-preview.sh`

## Token usage

1.12 B tokens in 2,628 model messages (output 1.8 M, cache reads 1.09 B, cache writes 28.1 M, uncached input 6 k). Full breakdown: [tokens.json](tokens.json).

| Feature | Tokens | Output | Messages |
|---|---|---|---|
| Other | 487.4 M | 908 k | 1,276 |
| Planning & spec | 400.8 M | 652 k | 833 |
| Riders & bikes | 109.9 M | 100 k | 209 |
| Art project | 54.0 M | 116 k | 190 |
| Build, release & infra | 22.1 M | 12 k | 27 |
| Worlds & terrain | 19.1 M | 19 k | 36 |
| UI & menus | 17.1 M | 17 k | 49 |
| Multiplayer & server | 7.1 M | 5 k | 8 |

| Task | Feature | Tokens | Output |
|---|---|---|---|
| agent: Phase 5: Google + Strava sign-in | Planning & spec | 173.5 M | 349 k |
| agent: Realistic vegetation and crops | Other | 148.4 M | 332 k |
| agent: VR X1: OpenXR viewing mode | Planning & spec | 122.7 M | 231 k |
| agent: Animations and K6 organiser rules | Riders & bikes | 105.5 M | 61 k |
| agent: Phase 7: training history, rebinding | Planning & spec | 80.5 M | 51 k |
| agent: B8a: GitHub Pages preview | Other | 70.2 M | 158 k |
| agent: Cooler helmets | Other | 54.3 M | 57 k |
| agent: Art: hourly collector, move history | Other | 48.6 M | 155 k |
| coordination: send me the videos here and to that with future videos as well | Other | 43.6 M | 23 k |
| agent: Research vegetation and data sources | Other | 24.9 M | 109 k |
| coordination: once the helmets are reworked, send images | Other | 24.9 M | 12 k |
| agent: Split art project into OCW-ART | Art project | 17.8 M | 80 k |
| agent: God mode in the browser | Planning & spec | 17.2 M | 14 k |
| agent: Console autocomplete, GPS in HUD | UI & menus | 17.1 M | 17 k |
| agent: Web mode: fix 404, pinned browser, README test | Art project | 15.5 M | 22 k |
| agent: Port bevy_mod_openxr to Bevy 0.20 | Other | 14.8 M | 24 k |
| coordination: are there any smaller buildjobs that could be run on mac/windows? | Build, release & infra | 13.1 M | 6 k |
| coordination: let's prepare the move to the user@deb session | Other | 13.1 M | 13 k |
| coordination: make the other world maps (tenerife and all black forests) also available for we… | Worlds & terrain | 12.8 M | 7 k |
| coordination: i've enabled leela. do one "build all" on leela. | Build, release & infra | 8.1 M | 5 k |
| coordination: yes, and record the definition in art projwct, too. | Other | 8.0 M | 5 k |
| coordination: i've stopped the vms. check the worktrees and resume | Other | 5.7 M | 3 k |
| coordination: the preview works now. | Other | 5.5 M | 2 k |
| coordination: use windows and mac build servers, too | Multiplayer & server | 5.3 M | 3 k |
| coordination: locations will be user@deb:~/src/OCW and OCW-ART | Other | 4.8 M | 2 k |
| coordination: plan: prepare moving all activities from nils@deb to user@deb. let me know if … | Planning & spec | 4.7 M | 6 k |
| coordination: make the trees and vegetation more realistic. get information about the (big) pl… | Worlds & terrain | 4.1 M | 5 k |
| coordination: also move the build-history to the new art project location. | Art project | 3.8 M | 2 k |
| coordination: github is setup for user@deb. continue with move. | Other | 3.8 M | 3 k |
| coordination: i cannot get the browser version of OCW on this url you put in the README "https… | Art project | 3.6 M | 2 k |
| coordination: okay, do the changes and implement the small preview hosting on github. add do r… | Art project | 3.3 M | 6 k |
| coordination: are the art diary video builds running? | Art project | 3.3 M | 1 k |
| coordination: done | Other | 2.9 M | 1 k |
| coordination: Refinement, ... use it for everhing related to the art project. | Art project | 2.9 M | 1 k |
| coordination: why did user crash on deb? | Other | 2.8 M | 2 k |
| coordination: plan a new feature (->spec): after having 3d models, we need an editor where obj… | Riders & bikes | 2.4 M | 18 k |
| coordination: postpone the move for now | Other | 2.4 M | 1 k |
| coordination: art project: are finished build jobs and their status as well as finished featur… | Art project | 2.3 M | 1 k |
| coordination: do you see a second session on deb from the system user named "user" | Other | 2.3 M | 1 k |
| coordination: can you make the black forest and tenarife maps also available in the public web… | Worlds & terrain | 2.2 M | 7 k |

## Prompts

35 prompts (full text: [prompts.md](prompts.md)).

| Time | Prompt |
|---|---|
| 00:09 | the music of day 4 is cool, but a bit monoton. make it a bit more varied. also make different music for different days. record in spec |
| 00:17 | make the trees and vegetation more realistic. get information about the (big) plants and crops that are in the area. analyse them and add th |
| 06:11 | why did user crash on deb? |
| 06:14 | i've stopped the vms. check the worktrees and resume |
| 06:16 | are such crashed and their root cause  already logged in the art project? |
| 06:18 | yes, and record the definition in art projwct, too. |
| 06:51 | make the other world maps (tenerife and all black forests) also available for web usage |
| 07:10 | are there any smaller buildjobs that could be run on mac/windows? |
| 07:24 | do you see a second session on deb from the system user named "user" |
| 07:25 | art project: are finished build jobs and their status as well as finished features and merges logged? |
| 07:26 | yes |
| 07:28 | plan: prepare moving all activities from nils@deb to user@deb. let me know if you need my help with some steps or you can do everything by y |
| 07:50 | postpone the move for now |
| 07:51 | once the helmets are reworked, send images |
| 08:15 | are the art diary video builds running? |
| 08:16 | send me the videos here and to that with future videos as well |
| 11:30 | use windows and mac build servers, too |
| 11:44 | i've enabled leela. do one "build all" on leela. |
| 11:50 | The public view you created at "https://newkit.github.io/OCW/" does not work. IIRC we cannot host the make web-server on github, right? So i |
| 11:51 | design: |
| 11:52 | i cannot get the browser version of OCW on this url you put in the README "https://newkit.github.io/OCW/". It's unclear to me, where the app |
| 12:17 | the preview works now. |
| 12:18 | let's prepare the move to the user@deb session |
| 12:42 | github is setup for user@deb. continue with move. |
| 12:45 | I've created a now home for the artproject. Use this repository https://github.com/newkit/OCW-ART for everything ART related. |
| 12:45 | Refinement, ... use it for everhing related to the art project. |
| 12:46 | also move the build-history to the new art project location. |
| 12:48 | git clone <e-mail>:newkit/OCW.git ~/src/OCW  or would that collide with the building? |
| 12:55 | once the the split is done, prepare moving it to user@deb |
| 12:56 | locations will be  user@deb:~/src/OCW and OCW-ART |
| 12:57 | done |
| 13:01 | wait, i have the split of projects running in the other session. i need to wait till it finishes. |
| 13:06 | plan a new feature (SPECIFICATION.md): Rather than encoding all objects in code, use a standardizes open source 3D model format (make a prop |
| 13:10 | plan a new feature (->spec): after having 3d models, we need an editor where objects can be viewed and edited. also the world files should b |
| 13:15 | can you make the black forest and tenarife maps also available in the public web demo? |

## Features

14 spec versions added, 12 landed by a merge; 10 deploys, 1 releases.

| Spec | Feature | Landed | Check (marge) |
|---|---|---|---|
| 3.36 | Public preview of the browser app on GitHub Pages | 00:00 `9ea2fd0` | – |
| 3.37 | Art project music | 06:44 `9c2044d` (merge) | – |
| 3.38 | Art project incident log | 06:44 `9c2044d` (merge) | – |
| 3.39 | Phase 13 G5's browser part built | 07:03 `d9a9b05` (merge) | – |
| 3.40 | Browser app setup and its test browser | 07:52 `ed821d6` (merge) | ok at 06:25 (branch) |
| 3.41 | Art project features log | 07:52 `b28542c` (merge) | – |
| 3.42 | Phase 7 built in part | 08:46 `c926016` (merge) | – |
| 3.43 | Console Tab completion and the GPS line restored | 08:47 `5e96eb2` (merge) | – |
| 3.44 | Cooler helmets | 09:46 `5410232` (merge) | – |
| 3.45 | Phase 10 B8a built | 10:42 `8ab9209` (merge) | – |
| 3.46 | Sign-in with Google and Strava built | 12:18 `e2b4bda` (merge) | – |
| 3.47 | The remaining rider animations and Phase 12 K6, the organiser's options | 11:20 `594e8c1` (merge) | ok at 06:15, 1 suites, 1 passed, 0 failed (branch) |
| 3.48 | Two new phases planned | 13:14 `331a29f` | – |
| 3.49 | Phase 8 T8 | 13:15 `259934b` (merge) | ok at 08:05 (branch) |

Deploys:

- 08:45 marge: `5e96eb2-dirty` (ok)
- 09:20 leela: `5e96eb2-dirty` (exit 255)
- 09:45 marge: `5410232-dirty` (ok)
- 10:17 leela: `5410232-dirty` (exit 255)
- 10:37 marge: `8ab9209-dirty` (ok)
- 10:57 leela: `8ab9209-dirty` (ok)
- 11:58 marge: `42b48df-dirty` (ok)
- 12:08 leela: `42b48df-dirty` (ok)
- 12:56 marge: `a88498c-dirty` (ok)
- 12:59 leela: `a88498c-dirty` (ok)

Releases:

- 08:03 web-preview-worlds (pre-release)

## Agent jobs

12 jobs (coordinator log agents.jsonl).

| Task | Branch | Start | End | Status | Interrupted | Merged |
|---|---|---|---|---|---|---|
| art project: hermetic collector tests, varied per-day music (art/music.py, five styles), i | merge-9c | 00:01 | 06:44 | merged | 1 | `9c2044d` |
| ocw-ui menu test: unicorn rows on Controls -> Unicorn mode after the merge | ab18479c | 00:01 | 08:47 | merged | 1 | `c926016` |
| wave 2 | a61e5515 | 00:39 | 12:18 | merged | 1 | `e2b4bda` |
| wave 2 | add2bafd | 00:39 | 10:42 | merged | 1 | `8ab9209` |
| wave 2 | aa822ba7 | 00:39 | 12:24 | reported | 1 |  |
| wave 2 | a3b9cf0b | 00:39 | 12:24 | reported | 1 |  |
| Browser app setup: web-serve guard, make web-remote, WEB_BIND, pinned Chromium, README wal | ab2216bf | 06:15 | 07:53 | merged |  | `ed821d6` |
| Unicorn mode in the browser: god-mode glue shared in ocw-ui (flight, touch, inspection, HU | ab69e4b0 | 06:15 | 07:05 | merged |  | `d9a9b05` |
| U-turn cue regression test; scene timings; version references 3.37 | aca12fe4 | 06:15 | 11:20 | merged |  | `594e8c1` |
| WIP console Tab completion and GPS line | a3bffa51 | 06:46 | 08:47 | merged |  | `5e96eb2` |
| Art features log | a43d6ec0 | 07:53 | 07:53 | merged |  | `b28542c` |
| Cooler helmets | a9236ac6 | 07:53 | 09:47 | merged |  | `5410232` |

## Incidents

69 collected (janitor-delete 37, machine-offline 11, machine-online 11, oom-kill 2, runs-failed 1, unit-failed 6, unit-restart 1), 2 with root-cause notes ([incidents.md](incidents.md)).

| Time | Kind | Machine | What |
|---|---|---|---|
| 00:07 | machine-offline | leela | leela unreachable (timeout) |
| 00:39 | oom-kill | deb | OOM killer stopped ocw-build-dashboard.service |
| 00:39 | unit-restart | deb | ocw-build-dashboard.service restarted (restart 1) |
| 00:39 | oom-kill | deb | OOM killer stopped tmux scope (a terminal session) |
| 00:40 | janitor-delete | marge | janitor delete OCW/target (0.2 GB) |
| 00:43 | machine-offline | Win11Builder | Win11Builder unreachable (timeout) |
| 00:44 | machine-online | Win11Builder | Win11Builder back online |
| 00:50 | janitor-delete | marge | janitor delete OCW/target (0.8 GB) |
| 01:00 | janitor-delete | marge | janitor delete OCW/target (0.0 GB) |
| 01:05 | unit-failed | deb | ocw-art-collect.service failed (exit-code) |
| 01:51 | janitor-delete | marge | janitor delete OCW/target (0.0 GB) |
| 02:01 | janitor-delete | marge | janitor delete OCW/target (0.2 GB) |
| 02:01 | unit-failed | deb | ocw-art-collect.service failed (exit-code) |
| 03:02 | unit-failed | deb | ocw-art-collect.service failed (exit-code) |
| 03:22 | janitor-delete | marge | janitor delete OCW/target (0.0 GB) |
| 04:01 | unit-failed | deb | ocw-art-collect.service failed (exit-code) |
| 04:02 | janitor-delete | marge | janitor delete OCW/target (0.0 GB) |
| 05:05 | unit-failed | deb | ocw-art-collect.service failed (exit-code) |
| 06:05 | unit-failed | deb | ocw-art-collect.service failed (exit-code) |
| 06:09 | machine-online | leela | leela back online |
| 06:36 | janitor-delete | marge | janitor delete OCW/target (0.9 GB) |
| 07:08 | janitor-delete | marge | janitor delete OCW-worktree-agent-af13162558b98b473/target (0.0 GB) |
| 07:08 | janitor-delete | marge | janitor delete OCW-worktree-agent-a2e65303b0aed2f1c/target (0.2 GB) |
| 07:08 | janitor-delete | marge | janitor delete OCW-worktree-agent-a7c12806972eb03b7/target (7.4 GB) |
| 07:10 | janitor-delete | macos | janitor delete OCW/target/debug (18.7 GB) |
| 07:18 | janitor-delete | marge | janitor delete OCW-worktree-agent-a1c9a111de4bbfda1/target (20.2 GB) |
| 07:28 | janitor-delete | marge | janitor delete OCW-worktree-agent-a09cdbcff127205c5/target (25.1 GB) |
| 07:54 | janitor-delete | marge | janitor delete OCW-worktree-agent-ab69e4b089e56849c/target (28.1 GB) |
| 07:54 | janitor-delete | macos | janitor delete OCW-worktree-agent-ab69e4b089e56849c/target (5.1 GB) |
| 07:54 | janitor-delete | marge | janitor delete OCW-worktree-agent-ab2216bf39859444d/target (29.7 GB) |
| 07:57 | janitor-delete | macos | janitor delete OCW-worktree-agent-a3b9cf0b40cbf0ccc/target/debug (0.3 GB) |
| 07:59 | janitor-delete | marge | janitor delete OCW/target/debug (54.0 GB) |
| 08:11 | janitor-delete | macos | janitor delete OCW-worktree-agent-add2bafdd6a4b0c43/target/debug (4.6 GB) |
| 08:28 | machine-offline | leela | leela unreachable (timeout) |
| 09:45 | janitor-delete | marge | janitor delete OCW-worktree-agent-aca12fe4f3f6386c9/target/debug (19.2 GB) |
| 10:17 | runs-failed | leela, macos, marge | 11 failed remote.sh runs (leela 2, macos 5, marge 4) |
| 10:17 | janitor-delete | marge | janitor delete OCW-worktree-agent-ab18479c7c2ff5bd4/target (32.3 GB) |
| 10:18 | janitor-delete | macos | janitor delete OCW-worktree-agent-ab18479c7c2ff5bd4/target (4.6 GB) |
| 10:18 | janitor-delete | marge | janitor delete OCW-worktree-agent-a3bffa51d30d0cfa2/target (30.0 GB) |
| 10:18 | janitor-delete | macos | janitor delete OCW-worktree-agent-a3bffa51d30d0cfa2/target (9.3 GB) |
| 10:46 | machine-online | leela | leela back online |
| 10:59 | janitor-delete | marge | janitor delete OCW-worktree-agent-a9236ac646995a021/target (22.5 GB) |
| 10:59 | janitor-delete | macos | janitor delete OCW-worktree-agent-a9236ac646995a021/target (1.4 GB) |
| 11:05 | machine-offline | leela | leela unreachable (timeout) |
| 11:06 | machine-online | leela | leela back online |
| 11:14 | machine-offline | leela | leela unreachable (timeout) |
| 11:14 | janitor-delete | marge | janitor delete OCW-worktree-agent-add2bafdd6a4b0c43/target (29.8 GB) |
| 11:15 | janitor-delete | macos | janitor delete OCW-worktree-agent-add2bafdd6a4b0c43/target (5.4 GB) |
| 11:19 | machine-online | leela | leela back online |
| 11:31 | janitor-delete | macos | janitor delete OCW/target/debug (5.7 GB) |
| 12:10 | janitor-delete | marge | janitor delete OCW-worktree-agent-aca12fe4f3f6386c9/target (32.2 GB) |
| 12:10 | janitor-delete | macos | janitor delete OCW-worktree-agent-aca12fe4f3f6386c9/target (7.8 GB) |
| 12:12 | janitor-delete | marge | janitor delete OCW/target (1.9 GB) |
| 12:14 | machine-offline | leela | leela unreachable (timeout) |
| 12:15 | machine-online | leela | leela back online |
| 12:43 | machine-offline | leela | leela unreachable (ssh error) |
| 12:44 | machine-online | leela | leela back online |
| 12:53 | machine-offline | leela | leela unreachable (timeout) |
| 12:54 | machine-online | leela | leela back online |
| 13:02 | janitor-delete | marge | janitor delete OCW/target (0.0 GB) |

### Root-cause notes


Root-cause notes by the coordinator (art/ART-PROJECT.md §2.6). The collected
entries (journal, build log) are in `logs/build-log/incidents.jsonl` and in
the journal's "Incidents" section.

### 00:39 – deb ran out of memory: the dashboard and the coordinator session were killed

- **What happened:** the OOM killer stopped `ocw-build-dashboard.service`
  (00:39:18) and the coordinator's Claude Code session, its tmux scope
  (00:39:47), on deb. systemd restarted the dashboard 11 s later.
- **Cause:** two QEMU VMs ("windows", "macos") held about 8 GB of deb's 15 GB
  permanently. On top of that ran about 10 parallel agents in one Claude Code
  process (6.8 GB peak), the re-renders of the diary videos (ffmpeg) and the
  art collector. Swap was full (4 of 4 GB).
- **Effect:** the session crashed and 8 running agents were interrupted.
  Their worktrees were intact, and they were resumed at about 06:15. The
  day-4 video rendering at that moment was left truncated and was rendered
  again.
- **Fix:** the user stopped the VMs, and the dashboard was restarted. From now
  on at most about 5 agents run at a time, and renders don't run in parallel
  with many agents. Renders on deb run one day at a time.
- **Follow-up:** the dashboard unit got `Restart=on-failure` and
  `MemoryHigh=768M` / `MemoryMax=1G` (`tools/build-dashboard/ocw-build-dashboard.service`).
  It takes effect after `make dashboard-install`.

### 01:05 – the art collector failed every hour: journals written without the users masked

- **What happened:** `ocw-art-collect.service` failed every hour from 01:05 to
  06:05. Its mask check found 16 unmasked build-machine user names in the
  tracked journals and token files of days 1–4.
- **Cause:** the music agent re-rendered days 1–4 from its agent worktree
  against the main archive (00:24–00:39), and `render` rewrites the day's
  journal. `diary.py` read the machine list from the worktree's
  `config/machines.toml`, which a worktree doesn't have, so the users and
  hosts were left out of the mask. Only the home directory, e-mail and IP
  patterns applied.
- **Effect:** the tracked text files in the main checkout held the build user
  name as a word (not committed). The re-rendered day videos of that run
  could show it in prompt bubbles; they were published at about 06:15 and
  replaced at 06:43.
  No hosts and no IP addresses were affected.
- **Fix:** `check-masked --fix` with the main checkout's tool re-masked the
  files, and the check passes again. `diary.py` now finds `config/machines.toml`
  in the main checkout too, and refuses to mask without a machine list.
  Days 1–4 and the diary were rendered again and re-published.
- **Follow-up:** a regression test (`MachinesConfTest`). The collector's mask
  check did its job; the incident log made the hourly failures visible.

## Media

| Time | File |
|---|---|
| 00:00:04 | [000004-shot-wayland-k6-organiser-rules-menu.jpg](000004-shot-wayland-k6-organiser-rules-menu.jpg) |
| 00:00:55 | [000055-shot-wayland-k6-results-rules.jpg](000055-shot-wayland-k6-results-rules.jpg) |
| 00:01:01 | [000101-shot-wayland-a26-foot-down.jpg](000101-shot-wayland-a26-foot-down.jpg) |
| 00:01:25 | [000125-video-wayland-a26-foot-down-video.jpg](000125-video-wayland-a26-foot-down-video.jpg) |
| 00:01:25 | [000125-video-wayland-a26-foot-down-video.mp4](000125-video-wayland-a26-foot-down-video.mp4) |
| 00:01:37 | [000137-shot-wayland-a26-cornering.jpg](000137-shot-wayland-a26-cornering.jpg) |
| 00:03:30 | [000330-video-wayland-a26-uturn-video.jpg](000330-video-wayland-a26-uturn-video.jpg) |
| 00:03:30 | [000330-video-wayland-a26-uturn-video.mp4](000330-video-wayland-a26-uturn-video.mp4) |
| 00:08:18 | [000818-shot-wayland-a26-uturn-look.jpg](000818-shot-wayland-a26-uturn-look.jpg) |
| 00:12:21 | [001221-shot-wayland-a26-uturn-loop.jpg](001221-shot-wayland-a26-uturn-loop.jpg) |
| 00:13:57 | [001357-video-wayland-a26-victory-video.jpg](001357-video-wayland-a26-victory-video.jpg) |
| 00:13:57 | [001357-video-wayland-a26-victory-video.mp4](001357-video-wayland-a26-victory-video.mp4) |
| 00:14:36 | [001436-shot-wayland-a26-victory.jpg](001436-shot-wayland-a26-victory.jpg) |
| 00:16:12 | [001612-shot-wayland-helmet-road-behind.jpg](001612-shot-wayland-helmet-road-behind.jpg) |
| 00:16:23 | [001623-shot-wayland-helmet-tt-position.jpg](001623-shot-wayland-helmet-tt-position.jpg) |
| 00:16:34 | [001634-shot-wayland-helmet-group-chase.jpg](001634-shot-wayland-helmet-group-chase.jpg) |
| 00:17:13 | [001713-shot-helmet-road-behind.jpg](001713-shot-helmet-road-behind.jpg) |
| 00:17:37 | [001737-frames-v10.jpg](001737-frames-v10.jpg) |
| 00:17:37 | [001737-frames-v12.jpg](001737-frames-v12.jpg) |
| 00:17:37 | [001737-frames-v13.5.jpg](001737-frames-v13.5.jpg) |
| 00:17:38 | [001738-frames-v15.jpg](001738-frames-v15.jpg) |
| 00:17:47 | [001747-shot-helmet-tt-position.jpg](001747-shot-helmet-tt-position.jpg) |
| 00:17:56 | [001756-frames-f1.jpg](001756-frames-f1.jpg) |
| 00:17:57 | [001757-frames-f4.jpg](001757-frames-f4.jpg) |
| 00:17:57 | [001757-frames-f6.5.jpg](001757-frames-f6.5.jpg) |
| 00:17:58 | [001758-frames-u3.jpg](001758-frames-u3.jpg) |
| 00:18:00 | [001800-frames-u6.jpg](001800-frames-u6.jpg) |
| 00:18:01 | [001801-frames-u9.jpg](001801-frames-u9.jpg) |
| 00:18:02 | [001802-frames-u12.jpg](001802-frames-u12.jpg) |
| 00:18:03 | [001803-frames-u15.jpg](001803-frames-u15.jpg) |
| 00:18:18 | [001818-shot-helmet-group-chase.jpg](001818-shot-helmet-group-chase.jpg) |
| 00:27:16 | [002716-shot-wayland-god-unicorn-flight.jpg](002716-shot-wayland-god-unicorn-flight.jpg) |
| 00:32:00 | [003200-shot-wayland-god-inspect-vaduz.jpg](003200-shot-wayland-god-inspect-vaduz.jpg) |
| 00:32:11 | [003211-shot-wayland-god-menu-world.jpg](003211-shot-wayland-god-menu-world.jpg) |
| 06:17:28 | [061728-frames-c1.jpg](061728-frames-c1.jpg) |
| 06:17:29 | [061729-frames-c1.5.jpg](061729-frames-c1.5.jpg) |
| 06:17:30 | [061730-frames-c2.jpg](061730-frames-c2.jpg) |
| 06:17:31 | [061731-frames-c2.5.jpg](061731-frames-c2.5.jpg) |
| 06:17:32 | [061732-frames-c3.5.jpg](061732-frames-c3.5.jpg) |
| 06:17:34 | [061734-frames-c4.jpg](061734-frames-c4.jpg) |
| 06:17:34 | [061734-frames-strip.jpg](061734-frames-strip.jpg) |
| 06:47:43 | [064743-web-web-unicorn-flight.jpg](064743-web-web-unicorn-flight.jpg) |
| 06:47:43 | [064743-web-web-unicorn-inspect.jpg](064743-web-web-unicorn-inspect.jpg) |
| 06:47:43 | [064743-web-web-unicorn-menu.jpg](064743-web-web-unicorn-menu.jpg) |
| 06:57:14 | [065714-scenes-p7-wayland-menu-history-rides.jpg](065714-scenes-p7-wayland-menu-history-rides.jpg) |
| 06:57:24 | [065724-scenes-p7-wayland-menu-history-ride.jpg](065724-scenes-p7-wayland-menu-history-ride.jpg) |
| 06:57:34 | [065734-scenes-p7-wayland-menu-bindings-conflict.jpg](065734-scenes-p7-wayland-menu-bindings-conflict.jpg) |
| 06:57:45 | [065745-scenes-p7-wayland-menu-accessibility.jpg](065745-scenes-p7-wayland-menu-accessibility.jpg) |
| 06:57:52 | [065752-scenes-p7-wayland-access-hud.jpg](065752-scenes-p7-wayland-access-hud.jpg) |
| 06:58:16 | [065816-scenes-p7-x11-menu-history-rides.jpg](065816-scenes-p7-x11-menu-history-rides.jpg) |
| 06:58:40 | [065840-scenes-p7-x11-menu-history-ride.jpg](065840-scenes-p7-x11-menu-history-ride.jpg) |
| 06:59:04 | [065904-scenes-p7-x11-menu-bindings-conflict.jpg](065904-scenes-p7-x11-menu-bindings-conflict.jpg) |
| 06:59:29 | [065929-scenes-p7-x11-menu-accessibility.jpg](065929-scenes-p7-x11-menu-accessibility.jpg) |
| 06:59:48 | [065948-scenes-p7-x11-access-hud.jpg](065948-scenes-p7-x11-access-hud.jpg) |
| 06:59:52 | [065952-web-readme-01-root.jpg](065952-web-readme-01-root.jpg) |
| 06:59:52 | [065952-web-readme-02-root.jpg](065952-web-readme-02-root.jpg) |
| 06:59:52 | [065952-web-readme-03-route-hills.jpg](065952-web-readme-03-route-hills.jpg) |
| 06:59:52 | [065952-web-readme-04-route-hills-bots-5-power-200-start-0-name-ada-ftp-250-qualit.jpg](065952-web-readme-04-route-hills-bots-5-power-200-start-0-name-ada-ftp-250-qualit.jpg) |
| 06:59:52 | [065952-web-readme-05-route-loop-bots-3-power-250-start-1-5-name-ada-ftp-250.jpg](065952-web-readme-05-route-loop-bots-3-power-250-start-1-5-name-ada-ftp-250.jpg) |
| 06:59:52 | [065952-web-readme-06-route-hills-gpu-webgl2-quality-low.jpg](065952-web-readme-06-route-hills-gpu-webgl2-quality-low.jpg) |
| 06:59:52 | [065952-web-readme-07-world-liechtenstein-route-vaduz-malbun-key-first-loading.jpg](065952-web-readme-07-world-liechtenstein-route-vaduz-malbun-key-first-loading.jpg) |
| 06:59:52 | [065952-web-readme-07-world-liechtenstein-route-vaduz-malbun-key.jpg](065952-web-readme-07-world-liechtenstein-route-vaduz-malbun-key.jpg) |
| 06:59:52 | [065952-web-readme-08-world-liechtenstein-route-vaduz-malbun-bots-5-power-250-name-first-loading.jpg](065952-web-readme-08-world-liechtenstein-route-vaduz-malbun-bots-5-power-250-name-first-loading.jpg) |
| 06:59:52 | [065952-web-readme-08-world-liechtenstein-route-vaduz-malbun-bots-5-power-250-name.jpg](065952-web-readme-08-world-liechtenstein-route-vaduz-malbun-bots-5-power-250-name.jpg) |
| 06:59:52 | [065952-web-readme-09-world-liechtenstein-free-1-key-first-loading.jpg](065952-web-readme-09-world-liechtenstein-free-1-key-first-loading.jpg) |
| 06:59:52 | [065952-web-readme-09-world-liechtenstein-free-1-key.jpg](065952-web-readme-09-world-liechtenstein-free-1-key.jpg) |
| 06:59:52 | [065952-web-readme-10-world-liechtenstein-key-first-loading.jpg](065952-web-readme-10-world-liechtenstein-key-first-loading.jpg) |
| 06:59:52 | [065952-web-readme-10-world-liechtenstein-key.jpg](065952-web-readme-10-world-liechtenstein-key.jpg) |
| 06:59:52 | [065952-web-readme-11-route-hills.jpg](065952-web-readme-11-route-hills.jpg) |
| 07:01:29 | [070129-web-web-world-unicorn-flight.jpg](070129-web-web-world-unicorn-flight.jpg) |
| 07:01:29 | [070129-web-web-world-unicorn-inspect.jpg](070129-web-web-world-unicorn-inspect.jpg) |
| 07:01:29 | [070129-web-web-world-unicorn-menu.jpg](070129-web-web-world-unicorn-menu.jpg) |
| 07:09:44 | [070944-scenes-p7-x11b-menu-history-rides.jpg](070944-scenes-p7-x11b-menu-history-rides.jpg) |
| 07:10:16 | [071016-scenes-p7-x11b-menu-history-ride.jpg](071016-scenes-p7-x11b-menu-history-ride.jpg) |
| 07:10:50 | [071050-scenes-p7-x11b-menu-bindings-conflict.jpg](071050-scenes-p7-x11b-menu-bindings-conflict.jpg) |
| 07:11:17 | [071117-scenes-p7-x11b-menu-accessibility.jpg](071117-scenes-p7-x11b-menu-accessibility.jpg) |
| 07:11:50 | [071150-scenes-p7-x11b-access-hud.jpg](071150-scenes-p7-x11b-access-hud.jpg) |
| 07:15:44 | [071544-shot-wayland-console-completion-cycle.jpg](071544-shot-wayland-console-completion-cycle.jpg) |
| 07:16:17 | [071617-shot-wayland-k6-event-rules.jpg](071617-shot-wayland-k6-event-rules.jpg) |
| 07:16:24 | [071624-shot-wayland-k6-organiser-rules-menu.jpg](071624-shot-wayland-k6-organiser-rules-menu.jpg) |
| 07:17:16 | [071716-shot-wayland-k6-results-rules.jpg](071716-shot-wayland-k6-results-rules.jpg) |
| 07:17:23 | [071723-shot-wayland-a26-foot-down.jpg](071723-shot-wayland-a26-foot-down.jpg) |
| 07:17:52 | [071752-video-wayland-a26-foot-down-video.jpg](071752-video-wayland-a26-foot-down-video.jpg) |
| 07:17:52 | [071752-video-wayland-a26-foot-down-video.mp4](071752-video-wayland-a26-foot-down-video.mp4) |
| 07:18:06 | [071806-shot-wayland-a26-cornering.jpg](071806-shot-wayland-a26-cornering.jpg) |
| 07:19:35 | [071935-video-wayland-a26-uturn-video.jpg](071935-video-wayland-a26-uturn-video.jpg) |
| 07:19:35 | [071935-video-wayland-a26-uturn-video.mp4](071935-video-wayland-a26-uturn-video.mp4) |
| 07:19:44 | [071944-shot-wayland-a26-uturn-look.jpg](071944-shot-wayland-a26-uturn-look.jpg) |
| 07:19:59 | [071959-shot-wayland-a26-uturn-loop.jpg](071959-shot-wayland-a26-uturn-loop.jpg) |
| 07:21:34 | [072134-video-wayland-a26-victory-video.jpg](072134-video-wayland-a26-victory-video.jpg) |
| 07:21:34 | [072134-video-wayland-a26-victory-video.mp4](072134-video-wayland-a26-victory-video.mp4) |
| 07:22:21 | [072221-shot-wayland-a26-victory.jpg](072221-shot-wayland-a26-victory.jpg) |
| 07:30:36 | [073036-shot-wayland-console-completion.jpg](073036-shot-wayland-console-completion.jpg) |
| 07:30:51 | [073051-shot-wayland-hud-gps-route.jpg](073051-shot-wayland-hud-gps-route.jpg) |
| 07:31:27 | [073127-shot-k6-event-rules.jpg](073127-shot-k6-event-rules.jpg) |
| 07:32:03 | [073203-shot-k6-organiser-rules-menu.jpg](073203-shot-k6-organiser-rules-menu.jpg) |
| 07:33:04 | [073304-shot-k6-results-rules.jpg](073304-shot-k6-results-rules.jpg) |
| 07:33:39 | [073339-shot-a26-foot-down.jpg](073339-shot-a26-foot-down.jpg) |
| 07:37:31 | [073731-video-a26-foot-down-video.jpg](073731-video-a26-foot-down-video.jpg) |
| 07:37:31 | [073731-video-a26-foot-down-video.mp4](073731-video-a26-foot-down-video.mp4) |
| 07:37:57 | [073757-shot-a26-cornering.jpg](073757-shot-a26-cornering.jpg) |
| 07:45:21 | [074521-scenes-p7-hudfit-access-hud.jpg](074521-scenes-p7-hudfit-access-hud.jpg) |
| 07:47:12 | [074712-video-a26-uturn-video.jpg](074712-video-a26-uturn-video.jpg) |
| 07:47:12 | [074712-video-a26-uturn-video.mp4](074712-video-a26-uturn-video.mp4) |
| 07:47:42 | [074742-web-web-console.jpg](074742-web-web-console.jpg) |
| 07:47:42 | [074742-web-web-gps.jpg](074742-web-web-gps.jpg) |
| 07:47:42 | [074742-web-web-hud.jpg](074742-web-web-hud.jpg) |
| 07:48:03 | [074803-shot-a26-uturn-look.jpg](074803-shot-a26-uturn-look.jpg) |
| 07:48:56 | [074856-shot-a26-uturn-loop.jpg](074856-shot-a26-uturn-loop.jpg) |
| 07:56:33 | [075633-shot-wayland-helmet-mirror-road.jpg](075633-shot-wayland-helmet-mirror-road.jpg) |
| 07:57:01 | [075701-shot-wayland-helmet-mirror-road-side.jpg](075701-shot-wayland-helmet-mirror-road-side.jpg) |
| 07:57:27 | [075727-shot-wayland-helmet-mirror-light.jpg](075727-shot-wayland-helmet-mirror-light.jpg) |
| 07:57:55 | [075755-shot-wayland-helmet-mirror-light-side.jpg](075755-shot-wayland-helmet-mirror-light-side.jpg) |
| 07:58:21 | [075821-shot-wayland-helmet-mirror-aero-road.jpg](075821-shot-wayland-helmet-mirror-aero-road.jpg) |
| 07:58:49 | [075849-shot-wayland-helmet-mirror-aero-road-side.jpg](075849-shot-wayland-helmet-mirror-aero-road-side.jpg) |
| 07:59:03 | [075903-video-a26-victory-video.jpg](075903-video-a26-victory-video.jpg) |
| 07:59:03 | [075903-video-a26-victory-video.mp4](075903-video-a26-victory-video.mp4) |
| 07:59:15 | [075915-shot-wayland-helmet-mirror-tt.jpg](075915-shot-wayland-helmet-mirror-tt.jpg) |
| 07:59:42 | [075942-shot-wayland-helmet-mirror-tt-side.jpg](075942-shot-wayland-helmet-mirror-tt-side.jpg) |
| 07:59:51 | [075951-shot-a26-victory.jpg](075951-shot-a26-victory.jpg) |
| 08:00:10 | [080010-shot-wayland-helmet-mirror-cap.jpg](080010-shot-wayland-helmet-mirror-cap.jpg) |
| 08:00:21 | [080021-shot-wayland-helmet-road-behind.jpg](080021-shot-wayland-helmet-road-behind.jpg) |
| 08:00:32 | [080032-shot-wayland-helmet-tt-position.jpg](080032-shot-wayland-helmet-tt-position.jpg) |
| 08:00:43 | [080043-shot-wayland-helmet-group-chase.jpg](080043-shot-wayland-helmet-group-chase.jpg) |
| 08:01:06 | [080106-scenes-helmets-before-wayland-helmet-mirror-aero-road-closeup-back.jpg](080106-scenes-helmets-before-wayland-helmet-mirror-aero-road-closeup-back.jpg) |
| 08:01:06 | [080106-scenes-helmets-before-wayland-helmet-mirror-light-closeup-back.jpg](080106-scenes-helmets-before-wayland-helmet-mirror-light-closeup-back.jpg) |
| 08:01:06 | [080106-scenes-helmets-before-wayland-helmet-mirror-light-closeup-mirror.jpg](080106-scenes-helmets-before-wayland-helmet-mirror-light-closeup-mirror.jpg) |
| 08:01:06 | [080106-scenes-helmets-before-wayland-helmet-mirror-road-closeup-back.jpg](080106-scenes-helmets-before-wayland-helmet-mirror-road-closeup-back.jpg) |
| 08:01:06 | [080106-scenes-helmets-before-wayland-helmet-mirror-road-closeup-mirror.jpg](080106-scenes-helmets-before-wayland-helmet-mirror-road-closeup-mirror.jpg) |
| 08:01:07 | [080107-scenes-helmets-before-wayland-helmet-mirror-aero-road-closeup-mirror.jpg](080107-scenes-helmets-before-wayland-helmet-mirror-aero-road-closeup-mirror.jpg) |
| 08:01:07 | [080107-scenes-helmets-before-wayland-helmet-mirror-aero-road-side-closeup-back.jpg](080107-scenes-helmets-before-wayland-helmet-mirror-aero-road-side-closeup-back.jpg) |
| 08:01:07 | [080107-scenes-helmets-before-wayland-helmet-mirror-aero-road-side-closeup-mirror.jpg](080107-scenes-helmets-before-wayland-helmet-mirror-aero-road-side-closeup-mirror.jpg) |
| 08:01:07 | [080107-scenes-helmets-before-wayland-helmet-mirror-cap-closeup-back.jpg](080107-scenes-helmets-before-wayland-helmet-mirror-cap-closeup-back.jpg) |
| 08:01:07 | [080107-scenes-helmets-before-wayland-helmet-mirror-cap-closeup-mirror.jpg](080107-scenes-helmets-before-wayland-helmet-mirror-cap-closeup-mirror.jpg) |
| 08:01:07 | [080107-scenes-helmets-before-wayland-helmet-mirror-light-side-closeup-back.jpg](080107-scenes-helmets-before-wayland-helmet-mirror-light-side-closeup-back.jpg) |
| 08:01:07 | [080107-scenes-helmets-before-wayland-helmet-mirror-light-side-closeup-mirror.jpg](080107-scenes-helmets-before-wayland-helmet-mirror-light-side-closeup-mirror.jpg) |
| 08:01:07 | [080107-scenes-helmets-before-wayland-helmet-mirror-road-side-closeup-back.jpg](080107-scenes-helmets-before-wayland-helmet-mirror-road-side-closeup-back.jpg) |
| 08:01:07 | [080107-scenes-helmets-before-wayland-helmet-mirror-road-side-closeup-mirror.jpg](080107-scenes-helmets-before-wayland-helmet-mirror-road-side-closeup-mirror.jpg) |
| 08:01:07 | [080107-scenes-helmets-before-wayland-helmet-mirror-tt-closeup-back.jpg](080107-scenes-helmets-before-wayland-helmet-mirror-tt-closeup-back.jpg) |
| 08:01:07 | [080107-scenes-helmets-before-wayland-helmet-mirror-tt-closeup-mirror.jpg](080107-scenes-helmets-before-wayland-helmet-mirror-tt-closeup-mirror.jpg) |
| 08:01:07 | [080107-scenes-helmets-before-wayland-helmet-mirror-tt-side-closeup-back.jpg](080107-scenes-helmets-before-wayland-helmet-mirror-tt-side-closeup-back.jpg) |
| 08:01:08 | [080108-scenes-helmets-after1-wayland-helmet-mirror-light-closeup-back.jpg](080108-scenes-helmets-after1-wayland-helmet-mirror-light-closeup-back.jpg) |
| 08:01:08 | [080108-scenes-helmets-after1-wayland-helmet-mirror-light-closeup-mirror.jpg](080108-scenes-helmets-after1-wayland-helmet-mirror-light-closeup-mirror.jpg) |
| 08:01:08 | [080108-scenes-helmets-after1-wayland-helmet-mirror-road-closeup-back.jpg](080108-scenes-helmets-after1-wayland-helmet-mirror-road-closeup-back.jpg) |
| 08:01:08 | [080108-scenes-helmets-after1-wayland-helmet-mirror-road-closeup-mirror.jpg](080108-scenes-helmets-after1-wayland-helmet-mirror-road-closeup-mirror.jpg) |
| 08:01:08 | [080108-scenes-helmets-before-wayland-helmet-group-chase-closeup.jpg](080108-scenes-helmets-before-wayland-helmet-group-chase-closeup.jpg) |
| 08:01:08 | [080108-scenes-helmets-before-wayland-helmet-mirror-tt-side-closeup-mirror.jpg](080108-scenes-helmets-before-wayland-helmet-mirror-tt-side-closeup-mirror.jpg) |
| 08:01:08 | [080108-scenes-helmets-before-wayland-helmet-road-behind-closeup.jpg](080108-scenes-helmets-before-wayland-helmet-road-behind-closeup.jpg) |
| 08:01:08 | [080108-scenes-helmets-before-wayland-helmet-tt-position-closeup.jpg](080108-scenes-helmets-before-wayland-helmet-tt-position-closeup.jpg) |
| 08:01:08 | [080108-scenes-helmets-before2-wayland-helmet-group-chase-closeup.jpg](080108-scenes-helmets-before2-wayland-helmet-group-chase-closeup.jpg) |
| 08:01:08 | [080108-scenes-helmets-before2-wayland-helmet-road-behind-closeup.jpg](080108-scenes-helmets-before2-wayland-helmet-road-behind-closeup.jpg) |
| 08:01:08 | [080108-scenes-helmets-before2-wayland-helmet-tt-position-closeup.jpg](080108-scenes-helmets-before2-wayland-helmet-tt-position-closeup.jpg) |
| 08:01:09 | [080109-scenes-helmets-after1-wayland-helmet-mirror-aero-road-closeup-back.jpg](080109-scenes-helmets-after1-wayland-helmet-mirror-aero-road-closeup-back.jpg) |
| 08:01:09 | [080109-scenes-helmets-after1-wayland-helmet-mirror-aero-road-closeup-mirror.jpg](080109-scenes-helmets-after1-wayland-helmet-mirror-aero-road-closeup-mirror.jpg) |
| 08:01:09 | [080109-scenes-helmets-after1-wayland-helmet-mirror-aero-road-side-closeup-back.jpg](080109-scenes-helmets-after1-wayland-helmet-mirror-aero-road-side-closeup-back.jpg) |
| 08:01:09 | [080109-scenes-helmets-after1-wayland-helmet-mirror-aero-road-side-closeup-mirror.jpg](080109-scenes-helmets-after1-wayland-helmet-mirror-aero-road-side-closeup-mirror.jpg) |
| 08:01:09 | [080109-scenes-helmets-after1-wayland-helmet-mirror-cap-closeup-back.jpg](080109-scenes-helmets-after1-wayland-helmet-mirror-cap-closeup-back.jpg) |
| 08:01:09 | [080109-scenes-helmets-after1-wayland-helmet-mirror-cap-closeup-mirror.jpg](080109-scenes-helmets-after1-wayland-helmet-mirror-cap-closeup-mirror.jpg) |
| 08:01:09 | [080109-scenes-helmets-after1-wayland-helmet-mirror-light-side-closeup-back.jpg](080109-scenes-helmets-after1-wayland-helmet-mirror-light-side-closeup-back.jpg) |
| 08:01:09 | [080109-scenes-helmets-after1-wayland-helmet-mirror-light-side-closeup-mirror.jpg](080109-scenes-helmets-after1-wayland-helmet-mirror-light-side-closeup-mirror.jpg) |
| 08:01:09 | [080109-scenes-helmets-after1-wayland-helmet-mirror-road-side-closeup-back.jpg](080109-scenes-helmets-after1-wayland-helmet-mirror-road-side-closeup-back.jpg) |
| 08:01:09 | [080109-scenes-helmets-after1-wayland-helmet-mirror-road-side-closeup-mirror.jpg](080109-scenes-helmets-after1-wayland-helmet-mirror-road-side-closeup-mirror.jpg) |
| 08:01:09 | [080109-scenes-helmets-after1-wayland-helmet-mirror-tt-closeup-back.jpg](080109-scenes-helmets-after1-wayland-helmet-mirror-tt-closeup-back.jpg) |
| 08:01:09 | [080109-scenes-helmets-after1-wayland-helmet-mirror-tt-closeup-mirror.jpg](080109-scenes-helmets-after1-wayland-helmet-mirror-tt-closeup-mirror.jpg) |
| 08:01:10 | [080110-scenes-helmets-after1-wayland-helmet-group-chase-closeup.jpg](080110-scenes-helmets-after1-wayland-helmet-group-chase-closeup.jpg) |
| 08:01:10 | [080110-scenes-helmets-after1-wayland-helmet-mirror-tt-side-closeup-back.jpg](080110-scenes-helmets-after1-wayland-helmet-mirror-tt-side-closeup-back.jpg) |
| 08:01:10 | [080110-scenes-helmets-after1-wayland-helmet-mirror-tt-side-closeup-mirror.jpg](080110-scenes-helmets-after1-wayland-helmet-mirror-tt-side-closeup-mirror.jpg) |
| 08:01:10 | [080110-scenes-helmets-after1-wayland-helmet-road-behind-closeup.jpg](080110-scenes-helmets-after1-wayland-helmet-road-behind-closeup.jpg) |
| 08:01:10 | [080110-scenes-helmets-after1-wayland-helmet-tt-position-closeup.jpg](080110-scenes-helmets-after1-wayland-helmet-tt-position-closeup.jpg) |
| 08:03:06 | [080306-web-web-world-unicorn-inspect.jpg](080306-web-web-world-unicorn-inspect.jpg) |
| 08:03:06 | [080306-web-web-world.jpg](080306-web-web-world.jpg) |
| 09:03:31 | [090331-web-preview-fps-wp-s-web.jpg](090331-web-preview-fps-wp-s-web.jpg) |
| 09:04:00 | [090400-web-preview-fps-wp-z-web.jpg](090400-web-preview-fps-wp-z-web.jpg) |
| 09:04:26 | [090426-web-preview-fps-wp-s-O3-web.jpg](090426-web-preview-fps-wp-s-O3-web.jpg) |
| 09:04:52 | [090452-web-preview-fps-wp-z-O3-web.jpg](090452-web-preview-fps-wp-z-O3-web.jpg) |
| 09:05:19 | [090519-web-preview-fps-wp-s-web.jpg](090519-web-preview-fps-wp-s-web.jpg) |
| 09:05:38 | [090538-shot-wayland-helmet-mirror-road.jpg](090538-shot-wayland-helmet-mirror-road.jpg) |
| 09:05:45 | [090545-web-preview-fps-wp-z-web.jpg](090545-web-preview-fps-wp-z-web.jpg) |
| 09:06:12 | [090612-web-preview-fps-wp-s-O3-web.jpg](090612-web-preview-fps-wp-s-O3-web.jpg) |
| 09:06:40 | [090640-web-preview-fps-wp-z-O3-web.jpg](090640-web-preview-fps-wp-z-O3-web.jpg) |
| 09:09:30 | [090930-shot-wayland-helmet-mirror-road-side.jpg](090930-shot-wayland-helmet-mirror-road-side.jpg) |
| 09:09:51 | [090951-shot-helmet-mirror-road.jpg](090951-shot-helmet-mirror-road.jpg) |
| 09:09:56 | [090956-shot-wayland-helmet-mirror-light.jpg](090956-shot-wayland-helmet-mirror-light.jpg) |
| 09:10:24 | [091024-shot-wayland-helmet-mirror-light-side.jpg](091024-shot-wayland-helmet-mirror-light-side.jpg) |
| 09:10:46 | [091046-shot-helmet-mirror-road-side.jpg](091046-shot-helmet-mirror-road-side.jpg) |
| 09:10:50 | [091050-shot-wayland-helmet-mirror-aero-road.jpg](091050-shot-wayland-helmet-mirror-aero-road.jpg) |
| 09:11:18 | [091118-shot-wayland-helmet-mirror-aero-road-side.jpg](091118-shot-wayland-helmet-mirror-aero-road-side.jpg) |
| 09:11:44 | [091144-shot-wayland-helmet-mirror-tt.jpg](091144-shot-wayland-helmet-mirror-tt.jpg) |
| 09:11:46 | [091146-shot-helmet-mirror-light.jpg](091146-shot-helmet-mirror-light.jpg) |
| 09:12:12 | [091212-shot-wayland-helmet-mirror-tt-side.jpg](091212-shot-wayland-helmet-mirror-tt-side.jpg) |
| 09:12:40 | [091240-shot-wayland-helmet-mirror-cap.jpg](091240-shot-wayland-helmet-mirror-cap.jpg) |
| 09:12:49 | [091249-shot-helmet-mirror-light-side.jpg](091249-shot-helmet-mirror-light-side.jpg) |
| 09:12:51 | [091251-shot-wayland-helmet-road-behind.jpg](091251-shot-wayland-helmet-road-behind.jpg) |
| 09:13:02 | [091302-shot-wayland-helmet-tt-position.jpg](091302-shot-wayland-helmet-tt-position.jpg) |
| 09:13:13 | [091313-shot-wayland-helmet-group-chase.jpg](091313-shot-wayland-helmet-group-chase.jpg) |
| 09:13:20 | [091320-scenes-helmets-after-wayland-helmet-mirror-aero-road-closeup-back.jpg](091320-scenes-helmets-after-wayland-helmet-mirror-aero-road-closeup-back.jpg) |
| 09:13:20 | [091320-scenes-helmets-after-wayland-helmet-mirror-aero-road-closeup-mirror.jpg](091320-scenes-helmets-after-wayland-helmet-mirror-aero-road-closeup-mirror.jpg) |
| 09:13:20 | [091320-scenes-helmets-after-wayland-helmet-mirror-light-closeup-back.jpg](091320-scenes-helmets-after-wayland-helmet-mirror-light-closeup-back.jpg) |
| 09:13:20 | [091320-scenes-helmets-after-wayland-helmet-mirror-light-closeup-mirror.jpg](091320-scenes-helmets-after-wayland-helmet-mirror-light-closeup-mirror.jpg) |
| 09:13:20 | [091320-scenes-helmets-after-wayland-helmet-mirror-road-closeup-back.jpg](091320-scenes-helmets-after-wayland-helmet-mirror-road-closeup-back.jpg) |
| 09:13:20 | [091320-scenes-helmets-after-wayland-helmet-mirror-road-closeup-mirror.jpg](091320-scenes-helmets-after-wayland-helmet-mirror-road-closeup-mirror.jpg) |
| 09:13:20 | [091320-scenes-helmets-after-wayland-helmet-mirror-tt-closeup-back.jpg](091320-scenes-helmets-after-wayland-helmet-mirror-tt-closeup-back.jpg) |
| 09:13:21 | [091321-scenes-helmets-after-wayland-helmet-mirror-aero-road-side-closeup-back.jpg](091321-scenes-helmets-after-wayland-helmet-mirror-aero-road-side-closeup-back.jpg) |
| 09:13:21 | [091321-scenes-helmets-after-wayland-helmet-mirror-aero-road-side-closeup-mirror.jpg](091321-scenes-helmets-after-wayland-helmet-mirror-aero-road-side-closeup-mirror.jpg) |
| 09:13:21 | [091321-scenes-helmets-after-wayland-helmet-mirror-cap-closeup-back.jpg](091321-scenes-helmets-after-wayland-helmet-mirror-cap-closeup-back.jpg) |
| 09:13:21 | [091321-scenes-helmets-after-wayland-helmet-mirror-cap-closeup-mirror.jpg](091321-scenes-helmets-after-wayland-helmet-mirror-cap-closeup-mirror.jpg) |
| 09:13:21 | [091321-scenes-helmets-after-wayland-helmet-mirror-light-side-closeup-back.jpg](091321-scenes-helmets-after-wayland-helmet-mirror-light-side-closeup-back.jpg) |
| 09:13:21 | [091321-scenes-helmets-after-wayland-helmet-mirror-light-side-closeup-mirror.jpg](091321-scenes-helmets-after-wayland-helmet-mirror-light-side-closeup-mirror.jpg) |
| 09:13:21 | [091321-scenes-helmets-after-wayland-helmet-mirror-road-side-closeup-back.jpg](091321-scenes-helmets-after-wayland-helmet-mirror-road-side-closeup-back.jpg) |
| 09:13:21 | [091321-scenes-helmets-after-wayland-helmet-mirror-road-side-closeup-mirror.jpg](091321-scenes-helmets-after-wayland-helmet-mirror-road-side-closeup-mirror.jpg) |
| 09:13:21 | [091321-scenes-helmets-after-wayland-helmet-mirror-tt-closeup-mirror.jpg](091321-scenes-helmets-after-wayland-helmet-mirror-tt-closeup-mirror.jpg) |
| 09:13:21 | [091321-scenes-helmets-after-wayland-helmet-mirror-tt-side-closeup-back.jpg](091321-scenes-helmets-after-wayland-helmet-mirror-tt-side-closeup-back.jpg) |
| 09:13:21 | [091321-scenes-helmets-after-wayland-helmet-mirror-tt-side-closeup-mirror.jpg](091321-scenes-helmets-after-wayland-helmet-mirror-tt-side-closeup-mirror.jpg) |
| 09:13:21 | [091321-scenes-helmets-after-wayland-helmet-road-behind-closeup.jpg](091321-scenes-helmets-after-wayland-helmet-road-behind-closeup.jpg) |
| 09:13:22 | [091322-scenes-helmets-after-wayland-helmet-group-chase-closeup.jpg](091322-scenes-helmets-after-wayland-helmet-group-chase-closeup.jpg) |
| 09:13:22 | [091322-scenes-helmets-after-wayland-helmet-tt-position-closeup.jpg](091322-scenes-helmets-after-wayland-helmet-tt-position-closeup.jpg) |
| 09:13:22 | [091322-scenes-helmets-compare-wayland-helmet-compare-group-chase-closeup.jpg](091322-scenes-helmets-compare-wayland-helmet-compare-group-chase-closeup.jpg) |
| 09:13:22 | [091322-scenes-helmets-compare-wayland-helmet-compare-group-chase.jpg](091322-scenes-helmets-compare-wayland-helmet-compare-group-chase.jpg) |
| 09:13:22 | [091322-scenes-helmets-compare-wayland-helmet-compare-mirror-aero-road-closeup-back.jpg](091322-scenes-helmets-compare-wayland-helmet-compare-mirror-aero-road-closeup-back.jpg) |
| 09:13:22 | [091322-scenes-helmets-compare-wayland-helmet-compare-mirror-aero-road-closeup-mirror.jpg](091322-scenes-helmets-compare-wayland-helmet-compare-mirror-aero-road-closeup-mirror.jpg) |
| 09:13:22 | [091322-scenes-helmets-compare-wayland-helmet-compare-mirror-aero-road-side-closeup-back.jpg](091322-scenes-helmets-compare-wayland-helmet-compare-mirror-aero-road-side-closeup-back.jpg) |
| 09:13:22 | [091322-scenes-helmets-compare-wayland-helmet-compare-mirror-aero-road-side-closeup-mirror.jpg](091322-scenes-helmets-compare-wayland-helmet-compare-mirror-aero-road-side-closeup-mirror.jpg) |
| 09:13:22 | [091322-scenes-helmets-compare-wayland-helmet-compare-mirror-aero-road-side.jpg](091322-scenes-helmets-compare-wayland-helmet-compare-mirror-aero-road-side.jpg) |
| 09:13:22 | [091322-scenes-helmets-compare-wayland-helmet-compare-mirror-aero-road.jpg](091322-scenes-helmets-compare-wayland-helmet-compare-mirror-aero-road.jpg) |
| 09:13:23 | [091323-scenes-helmets-compare-wayland-helmet-compare-mirror-cap-closeup-back.jpg](091323-scenes-helmets-compare-wayland-helmet-compare-mirror-cap-closeup-back.jpg) |
| 09:13:23 | [091323-scenes-helmets-compare-wayland-helmet-compare-mirror-cap-closeup-mirror.jpg](091323-scenes-helmets-compare-wayland-helmet-compare-mirror-cap-closeup-mirror.jpg) |
| 09:13:23 | [091323-scenes-helmets-compare-wayland-helmet-compare-mirror-cap.jpg](091323-scenes-helmets-compare-wayland-helmet-compare-mirror-cap.jpg) |
| 09:13:23 | [091323-scenes-helmets-compare-wayland-helmet-compare-mirror-light-closeup-back.jpg](091323-scenes-helmets-compare-wayland-helmet-compare-mirror-light-closeup-back.jpg) |
| 09:13:23 | [091323-scenes-helmets-compare-wayland-helmet-compare-mirror-light-closeup-mirror.jpg](091323-scenes-helmets-compare-wayland-helmet-compare-mirror-light-closeup-mirror.jpg) |
| 09:13:23 | [091323-scenes-helmets-compare-wayland-helmet-compare-mirror-light-side-closeup-back.jpg](091323-scenes-helmets-compare-wayland-helmet-compare-mirror-light-side-closeup-back.jpg) |
| 09:13:23 | [091323-scenes-helmets-compare-wayland-helmet-compare-mirror-light-side-closeup-mirror.jpg](091323-scenes-helmets-compare-wayland-helmet-compare-mirror-light-side-closeup-mirror.jpg) |
| 09:13:23 | [091323-scenes-helmets-compare-wayland-helmet-compare-mirror-light-side.jpg](091323-scenes-helmets-compare-wayland-helmet-compare-mirror-light-side.jpg) |
| 09:13:23 | [091323-scenes-helmets-compare-wayland-helmet-compare-mirror-light.jpg](091323-scenes-helmets-compare-wayland-helmet-compare-mirror-light.jpg) |
| 09:13:23 | [091323-scenes-helmets-compare-wayland-helmet-compare-mirror-road-closeup-back.jpg](091323-scenes-helmets-compare-wayland-helmet-compare-mirror-road-closeup-back.jpg) |
| 09:13:23 | [091323-scenes-helmets-compare-wayland-helmet-compare-mirror-road-closeup-mirror.jpg](091323-scenes-helmets-compare-wayland-helmet-compare-mirror-road-closeup-mirror.jpg) |
| 09:13:24 | [091324-scenes-helmets-compare-wayland-helmet-compare-mirror-road-side-closeup-back.jpg](091324-scenes-helmets-compare-wayland-helmet-compare-mirror-road-side-closeup-back.jpg) |
| 09:13:24 | [091324-scenes-helmets-compare-wayland-helmet-compare-mirror-road-side-closeup-mirror.jpg](091324-scenes-helmets-compare-wayland-helmet-compare-mirror-road-side-closeup-mirror.jpg) |
| 09:13:24 | [091324-scenes-helmets-compare-wayland-helmet-compare-mirror-road-side.jpg](091324-scenes-helmets-compare-wayland-helmet-compare-mirror-road-side.jpg) |
| 09:13:24 | [091324-scenes-helmets-compare-wayland-helmet-compare-mirror-road.jpg](091324-scenes-helmets-compare-wayland-helmet-compare-mirror-road.jpg) |
| 09:13:24 | [091324-scenes-helmets-compare-wayland-helmet-compare-mirror-tt-closeup-back.jpg](091324-scenes-helmets-compare-wayland-helmet-compare-mirror-tt-closeup-back.jpg) |
| 09:13:24 | [091324-scenes-helmets-compare-wayland-helmet-compare-mirror-tt-closeup-mirror.jpg](091324-scenes-helmets-compare-wayland-helmet-compare-mirror-tt-closeup-mirror.jpg) |
| 09:13:24 | [091324-scenes-helmets-compare-wayland-helmet-compare-mirror-tt-side-closeup-back.jpg](091324-scenes-helmets-compare-wayland-helmet-compare-mirror-tt-side-closeup-back.jpg) |
| 09:13:24 | [091324-scenes-helmets-compare-wayland-helmet-compare-mirror-tt-side-closeup-mirror.jpg](091324-scenes-helmets-compare-wayland-helmet-compare-mirror-tt-side-closeup-mirror.jpg) |
| 09:13:24 | [091324-scenes-helmets-compare-wayland-helmet-compare-mirror-tt-side.jpg](091324-scenes-helmets-compare-wayland-helmet-compare-mirror-tt-side.jpg) |
| 09:13:24 | [091324-scenes-helmets-compare-wayland-helmet-compare-mirror-tt.jpg](091324-scenes-helmets-compare-wayland-helmet-compare-mirror-tt.jpg) |
| 09:13:24 | [091324-scenes-helmets-compare-wayland-helmet-compare-road-behind-closeup.jpg](091324-scenes-helmets-compare-wayland-helmet-compare-road-behind-closeup.jpg) |
| 09:13:25 | [091325-scenes-helmets-compare-wayland-helmet-compare-road-behind.jpg](091325-scenes-helmets-compare-wayland-helmet-compare-road-behind.jpg) |
| 09:13:25 | [091325-scenes-helmets-compare-wayland-helmet-compare-tt-position-closeup.jpg](091325-scenes-helmets-compare-wayland-helmet-compare-tt-position-closeup.jpg) |
| 09:13:25 | [091325-scenes-helmets-compare-wayland-helmet-compare-tt-position.jpg](091325-scenes-helmets-compare-wayland-helmet-compare-tt-position.jpg) |
| 09:13:59 | [091359-shot-helmet-mirror-aero-road.jpg](091359-shot-helmet-mirror-aero-road.jpg) |
| 09:15:09 | [091509-shot-helmet-mirror-aero-road-side.jpg](091509-shot-helmet-mirror-aero-road-side.jpg) |
| 09:16:18 | [091618-shot-helmet-mirror-tt.jpg](091618-shot-helmet-mirror-tt.jpg) |
| 09:17:22 | [091722-shot-helmet-mirror-tt-side.jpg](091722-shot-helmet-mirror-tt-side.jpg) |
| 09:18:26 | [091826-shot-helmet-mirror-cap.jpg](091826-shot-helmet-mirror-cap.jpg) |
| 09:19:09 | [091909-shot-helmet-road-behind.jpg](091909-shot-helmet-road-behind.jpg) |
| 09:19:47 | [091947-shot-helmet-tt-position.jpg](091947-shot-helmet-tt-position.jpg) |
| 09:20:21 | [092021-shot-helmet-group-chase.jpg](092021-shot-helmet-group-chase.jpg) |
| 09:20:26 | [092026-scenes-helmets-before-x11-helmet-mirror-road-closeup-back.jpg](092026-scenes-helmets-before-x11-helmet-mirror-road-closeup-back.jpg) |
| 09:20:26 | [092026-scenes-helmets-before-x11-helmet-mirror-road-closeup-mirror.jpg](092026-scenes-helmets-before-x11-helmet-mirror-road-closeup-mirror.jpg) |
| 09:20:27 | [092027-scenes-helmets-before-x11-helmet-mirror-aero-road-closeup-back.jpg](092027-scenes-helmets-before-x11-helmet-mirror-aero-road-closeup-back.jpg) |
| 09:20:27 | [092027-scenes-helmets-before-x11-helmet-mirror-aero-road-closeup-mirror.jpg](092027-scenes-helmets-before-x11-helmet-mirror-aero-road-closeup-mirror.jpg) |
| 09:20:27 | [092027-scenes-helmets-before-x11-helmet-mirror-aero-road-side-closeup-back.jpg](092027-scenes-helmets-before-x11-helmet-mirror-aero-road-side-closeup-back.jpg) |
| 09:20:27 | [092027-scenes-helmets-before-x11-helmet-mirror-cap-closeup-back.jpg](092027-scenes-helmets-before-x11-helmet-mirror-cap-closeup-back.jpg) |
| 09:20:27 | [092027-scenes-helmets-before-x11-helmet-mirror-light-closeup-back.jpg](092027-scenes-helmets-before-x11-helmet-mirror-light-closeup-back.jpg) |
| 09:20:27 | [092027-scenes-helmets-before-x11-helmet-mirror-light-closeup-mirror.jpg](092027-scenes-helmets-before-x11-helmet-mirror-light-closeup-mirror.jpg) |
| 09:20:27 | [092027-scenes-helmets-before-x11-helmet-mirror-light-side-closeup-back.jpg](092027-scenes-helmets-before-x11-helmet-mirror-light-side-closeup-back.jpg) |
| 09:20:27 | [092027-scenes-helmets-before-x11-helmet-mirror-light-side-closeup-mirror.jpg](092027-scenes-helmets-before-x11-helmet-mirror-light-side-closeup-mirror.jpg) |
| 09:20:27 | [092027-scenes-helmets-before-x11-helmet-mirror-road-side-closeup-back.jpg](092027-scenes-helmets-before-x11-helmet-mirror-road-side-closeup-back.jpg) |
| 09:20:27 | [092027-scenes-helmets-before-x11-helmet-mirror-road-side-closeup-mirror.jpg](092027-scenes-helmets-before-x11-helmet-mirror-road-side-closeup-mirror.jpg) |
| 09:20:27 | [092027-scenes-helmets-before-x11-helmet-mirror-tt-closeup-back.jpg](092027-scenes-helmets-before-x11-helmet-mirror-tt-closeup-back.jpg) |
| 09:20:27 | [092027-scenes-helmets-before-x11-helmet-mirror-tt-closeup-mirror.jpg](092027-scenes-helmets-before-x11-helmet-mirror-tt-closeup-mirror.jpg) |
| 09:20:28 | [092028-scenes-helmets-after-x11-helmet-mirror-road-closeup-back.jpg](092028-scenes-helmets-after-x11-helmet-mirror-road-closeup-back.jpg) |
| 09:20:28 | [092028-scenes-helmets-after-x11-helmet-mirror-road-closeup-mirror.jpg](092028-scenes-helmets-after-x11-helmet-mirror-road-closeup-mirror.jpg) |
| 09:20:28 | [092028-scenes-helmets-before-x11-helmet-group-chase-closeup.jpg](092028-scenes-helmets-before-x11-helmet-group-chase-closeup.jpg) |
| 09:20:28 | [092028-scenes-helmets-before-x11-helmet-mirror-aero-road-side-closeup-mirror.jpg](092028-scenes-helmets-before-x11-helmet-mirror-aero-road-side-closeup-mirror.jpg) |
| 09:20:28 | [092028-scenes-helmets-before-x11-helmet-mirror-tt-side-closeup-back.jpg](092028-scenes-helmets-before-x11-helmet-mirror-tt-side-closeup-back.jpg) |
| 09:20:28 | [092028-scenes-helmets-before-x11-helmet-mirror-tt-side-closeup-mirror.jpg](092028-scenes-helmets-before-x11-helmet-mirror-tt-side-closeup-mirror.jpg) |
| 09:20:28 | [092028-scenes-helmets-before-x11-helmet-road-behind-closeup.jpg](092028-scenes-helmets-before-x11-helmet-road-behind-closeup.jpg) |
| 09:20:28 | [092028-scenes-helmets-before-x11-helmet-tt-position-closeup.jpg](092028-scenes-helmets-before-x11-helmet-tt-position-closeup.jpg) |
| 09:20:28 | [092028-scenes-helmets-before2-x11-helmet-group-chase-closeup.jpg](092028-scenes-helmets-before2-x11-helmet-group-chase-closeup.jpg) |
| 09:20:28 | [092028-scenes-helmets-before2-x11-helmet-road-behind-closeup.jpg](092028-scenes-helmets-before2-x11-helmet-road-behind-closeup.jpg) |
| 09:20:28 | [092028-scenes-helmets-before2-x11-helmet-tt-position-closeup.jpg](092028-scenes-helmets-before2-x11-helmet-tt-position-closeup.jpg) |
| 09:20:29 | [092029-scenes-helmets-after-x11-helmet-mirror-aero-road-closeup-back.jpg](092029-scenes-helmets-after-x11-helmet-mirror-aero-road-closeup-back.jpg) |
| 09:20:29 | [092029-scenes-helmets-after-x11-helmet-mirror-aero-road-closeup-mirror.jpg](092029-scenes-helmets-after-x11-helmet-mirror-aero-road-closeup-mirror.jpg) |
| 09:20:29 | [092029-scenes-helmets-after-x11-helmet-mirror-cap-closeup-back.jpg](092029-scenes-helmets-after-x11-helmet-mirror-cap-closeup-back.jpg) |
| 09:20:29 | [092029-scenes-helmets-after-x11-helmet-mirror-cap-closeup-mirror.jpg](092029-scenes-helmets-after-x11-helmet-mirror-cap-closeup-mirror.jpg) |
| 09:20:29 | [092029-scenes-helmets-after-x11-helmet-mirror-light-closeup-back.jpg](092029-scenes-helmets-after-x11-helmet-mirror-light-closeup-back.jpg) |
| 09:20:29 | [092029-scenes-helmets-after-x11-helmet-mirror-light-closeup-mirror.jpg](092029-scenes-helmets-after-x11-helmet-mirror-light-closeup-mirror.jpg) |
| 09:20:29 | [092029-scenes-helmets-after-x11-helmet-mirror-light-side-closeup-back.jpg](092029-scenes-helmets-after-x11-helmet-mirror-light-side-closeup-back.jpg) |
| 09:20:29 | [092029-scenes-helmets-after-x11-helmet-mirror-light-side-closeup-mirror.jpg](092029-scenes-helmets-after-x11-helmet-mirror-light-side-closeup-mirror.jpg) |
| 09:20:29 | [092029-scenes-helmets-after-x11-helmet-mirror-road-side-closeup-back.jpg](092029-scenes-helmets-after-x11-helmet-mirror-road-side-closeup-back.jpg) |
| 09:20:29 | [092029-scenes-helmets-after-x11-helmet-mirror-road-side-closeup-mirror.jpg](092029-scenes-helmets-after-x11-helmet-mirror-road-side-closeup-mirror.jpg) |
| 09:20:29 | [092029-scenes-helmets-after-x11-helmet-mirror-tt-closeup-back.jpg](092029-scenes-helmets-after-x11-helmet-mirror-tt-closeup-back.jpg) |
| 09:20:29 | [092029-scenes-helmets-after-x11-helmet-mirror-tt-closeup-mirror.jpg](092029-scenes-helmets-after-x11-helmet-mirror-tt-closeup-mirror.jpg) |
| 09:20:30 | [092030-scenes-helmets-after-x11-helmet-group-chase-closeup.jpg](092030-scenes-helmets-after-x11-helmet-group-chase-closeup.jpg) |
| 09:20:30 | [092030-scenes-helmets-after-x11-helmet-mirror-aero-road-side-closeup-back.jpg](092030-scenes-helmets-after-x11-helmet-mirror-aero-road-side-closeup-back.jpg) |
| 09:20:30 | [092030-scenes-helmets-after-x11-helmet-mirror-aero-road-side-closeup-mirror.jpg](092030-scenes-helmets-after-x11-helmet-mirror-aero-road-side-closeup-mirror.jpg) |
| 09:20:30 | [092030-scenes-helmets-after-x11-helmet-mirror-tt-side-closeup-back.jpg](092030-scenes-helmets-after-x11-helmet-mirror-tt-side-closeup-back.jpg) |
| 09:20:30 | [092030-scenes-helmets-after-x11-helmet-mirror-tt-side-closeup-mirror.jpg](092030-scenes-helmets-after-x11-helmet-mirror-tt-side-closeup-mirror.jpg) |
| 09:20:30 | [092030-scenes-helmets-after-x11-helmet-road-behind-closeup.jpg](092030-scenes-helmets-after-x11-helmet-road-behind-closeup.jpg) |
| 09:20:30 | [092030-scenes-helmets-after-x11-helmet-tt-position-closeup.jpg](092030-scenes-helmets-after-x11-helmet-tt-position-closeup.jpg) |
| 09:20:30 | [092030-scenes-helmets-compare-x11-helmet-compare-group-chase-closeup.jpg](092030-scenes-helmets-compare-x11-helmet-compare-group-chase-closeup.jpg) |
| 09:20:30 | [092030-scenes-helmets-compare-x11-helmet-compare-group-chase.jpg](092030-scenes-helmets-compare-x11-helmet-compare-group-chase.jpg) |
| 09:20:30 | [092030-scenes-helmets-compare-x11-helmet-compare-mirror-aero-road-closeup-back.jpg](092030-scenes-helmets-compare-x11-helmet-compare-mirror-aero-road-closeup-back.jpg) |
| 09:20:30 | [092030-scenes-helmets-compare-x11-helmet-compare-mirror-aero-road-closeup-mirror.jpg](092030-scenes-helmets-compare-x11-helmet-compare-mirror-aero-road-closeup-mirror.jpg) |
| 09:20:31 | [092031-scenes-helmets-compare-x11-helmet-compare-mirror-aero-road-side-closeup-back.jpg](092031-scenes-helmets-compare-x11-helmet-compare-mirror-aero-road-side-closeup-back.jpg) |
| 09:20:31 | [092031-scenes-helmets-compare-x11-helmet-compare-mirror-aero-road-side-closeup-mirror.jpg](092031-scenes-helmets-compare-x11-helmet-compare-mirror-aero-road-side-closeup-mirror.jpg) |
| 09:20:31 | [092031-scenes-helmets-compare-x11-helmet-compare-mirror-aero-road-side.jpg](092031-scenes-helmets-compare-x11-helmet-compare-mirror-aero-road-side.jpg) |
| 09:20:31 | [092031-scenes-helmets-compare-x11-helmet-compare-mirror-aero-road.jpg](092031-scenes-helmets-compare-x11-helmet-compare-mirror-aero-road.jpg) |
| 09:20:31 | [092031-scenes-helmets-compare-x11-helmet-compare-mirror-cap-closeup-back.jpg](092031-scenes-helmets-compare-x11-helmet-compare-mirror-cap-closeup-back.jpg) |
| 09:20:31 | [092031-scenes-helmets-compare-x11-helmet-compare-mirror-cap-closeup-mirror.jpg](092031-scenes-helmets-compare-x11-helmet-compare-mirror-cap-closeup-mirror.jpg) |
| 09:20:31 | [092031-scenes-helmets-compare-x11-helmet-compare-mirror-cap.jpg](092031-scenes-helmets-compare-x11-helmet-compare-mirror-cap.jpg) |
| 09:20:31 | [092031-scenes-helmets-compare-x11-helmet-compare-mirror-light-closeup-back.jpg](092031-scenes-helmets-compare-x11-helmet-compare-mirror-light-closeup-back.jpg) |
| 09:20:31 | [092031-scenes-helmets-compare-x11-helmet-compare-mirror-light-closeup-mirror.jpg](092031-scenes-helmets-compare-x11-helmet-compare-mirror-light-closeup-mirror.jpg) |
| 09:20:31 | [092031-scenes-helmets-compare-x11-helmet-compare-mirror-light-side-closeup-back.jpg](092031-scenes-helmets-compare-x11-helmet-compare-mirror-light-side-closeup-back.jpg) |
| 09:20:31 | [092031-scenes-helmets-compare-x11-helmet-compare-mirror-light.jpg](092031-scenes-helmets-compare-x11-helmet-compare-mirror-light.jpg) |
| 09:20:32 | [092032-scenes-helmets-compare-x11-helmet-compare-mirror-light-side-closeup-mirror.jpg](092032-scenes-helmets-compare-x11-helmet-compare-mirror-light-side-closeup-mirror.jpg) |
| 09:20:32 | [092032-scenes-helmets-compare-x11-helmet-compare-mirror-light-side.jpg](092032-scenes-helmets-compare-x11-helmet-compare-mirror-light-side.jpg) |
| 09:20:32 | [092032-scenes-helmets-compare-x11-helmet-compare-mirror-road-closeup-back.jpg](092032-scenes-helmets-compare-x11-helmet-compare-mirror-road-closeup-back.jpg) |
| 09:20:32 | [092032-scenes-helmets-compare-x11-helmet-compare-mirror-road-closeup-mirror.jpg](092032-scenes-helmets-compare-x11-helmet-compare-mirror-road-closeup-mirror.jpg) |
| 09:20:32 | [092032-scenes-helmets-compare-x11-helmet-compare-mirror-road-side-closeup-back.jpg](092032-scenes-helmets-compare-x11-helmet-compare-mirror-road-side-closeup-back.jpg) |
| 09:20:32 | [092032-scenes-helmets-compare-x11-helmet-compare-mirror-road-side-closeup-mirror.jpg](092032-scenes-helmets-compare-x11-helmet-compare-mirror-road-side-closeup-mirror.jpg) |
| 09:20:32 | [092032-scenes-helmets-compare-x11-helmet-compare-mirror-road-side.jpg](092032-scenes-helmets-compare-x11-helmet-compare-mirror-road-side.jpg) |
| 09:20:32 | [092032-scenes-helmets-compare-x11-helmet-compare-mirror-road.jpg](092032-scenes-helmets-compare-x11-helmet-compare-mirror-road.jpg) |
| 09:20:32 | [092032-scenes-helmets-compare-x11-helmet-compare-mirror-tt-closeup-back.jpg](092032-scenes-helmets-compare-x11-helmet-compare-mirror-tt-closeup-back.jpg) |
| 09:20:32 | [092032-scenes-helmets-compare-x11-helmet-compare-mirror-tt-closeup-mirror.jpg](092032-scenes-helmets-compare-x11-helmet-compare-mirror-tt-closeup-mirror.jpg) |
| 09:20:32 | [092032-scenes-helmets-compare-x11-helmet-compare-mirror-tt.jpg](092032-scenes-helmets-compare-x11-helmet-compare-mirror-tt.jpg) |
| 09:20:33 | [092033-scenes-helmets-compare-x11-helmet-compare-mirror-tt-side-closeup-back.jpg](092033-scenes-helmets-compare-x11-helmet-compare-mirror-tt-side-closeup-back.jpg) |
| 09:20:33 | [092033-scenes-helmets-compare-x11-helmet-compare-mirror-tt-side-closeup-mirror.jpg](092033-scenes-helmets-compare-x11-helmet-compare-mirror-tt-side-closeup-mirror.jpg) |
| 09:20:33 | [092033-scenes-helmets-compare-x11-helmet-compare-mirror-tt-side.jpg](092033-scenes-helmets-compare-x11-helmet-compare-mirror-tt-side.jpg) |
| 09:20:33 | [092033-scenes-helmets-compare-x11-helmet-compare-road-behind-closeup.jpg](092033-scenes-helmets-compare-x11-helmet-compare-road-behind-closeup.jpg) |
| 09:20:33 | [092033-scenes-helmets-compare-x11-helmet-compare-road-behind.jpg](092033-scenes-helmets-compare-x11-helmet-compare-road-behind.jpg) |
| 09:20:33 | [092033-scenes-helmets-compare-x11-helmet-compare-tt-position-closeup.jpg](092033-scenes-helmets-compare-x11-helmet-compare-tt-position-closeup.jpg) |
| 09:20:33 | [092033-scenes-helmets-compare-x11-helmet-compare-tt-position.jpg](092033-scenes-helmets-compare-x11-helmet-compare-tt-position.jpg) |
| 09:30:50 | [093050-vr-vr-sim-both-eyes.jpg](093050-vr-vr-sim-both-eyes.jpg) |
| 09:35:44 | [093544-vr-vr-sim-one-eye.jpg](093544-vr-vr-sim-one-eye.jpg) |
| 09:37:08 | [093708-vr-vr-sim-chase-mirror.jpg](093708-vr-vr-sim-chase-mirror.jpg) |
| 09:41:54 | [094154-vr-vr-sim-blackforest.jpg](094154-vr-vr-sim-blackforest.jpg) |
| 09:45:44 | [094544-vr-vr-no-runtime.jpg](094544-vr-vr-no-runtime.jpg) |
| 10:00:36 | [100036-web-preview-preview-credits.jpg](100036-web-preview-preview-credits.jpg) |
| 10:00:36 | [100036-web-preview-preview-hills.jpg](100036-web-preview-preview-hills.jpg) |
| 10:00:36 | [100036-web-preview-preview-start.jpg](100036-web-preview-preview-start.jpg) |
| 10:00:36 | [100036-web-preview-preview-untrusted.jpg](100036-web-preview-preview-untrusted.jpg) |
| 10:00:36 | [100036-web-preview-preview-webgl2.jpg](100036-web-preview-preview-webgl2.jpg) |
| 10:00:36 | [100036-web-preview-preview-world-world-loading.jpg](100036-web-preview-preview-world-world-loading.jpg) |
| 10:00:36 | [100036-web-preview-preview-world-world.jpg](100036-web-preview-preview-world-world.jpg) |
| 10:00:36 | [100036-web-preview-preview-world.jpg](100036-web-preview-preview-world.jpg) |
| 10:25:33 | [102533-web-web-account-linked.jpg](102533-web-web-account-linked.jpg) |
| 10:25:33 | [102533-web-web-account-signed-in.jpg](102533-web-web-account-signed-in.jpg) |
| 10:38:15 | [103815-web-preview-preview-hills.jpg](103815-web-preview-preview-hills.jpg) |
| 10:38:15 | [103815-web-preview-preview-world-world-loading.jpg](103815-web-preview-preview-world-world-loading.jpg) |
| 10:38:15 | [103815-web-preview-preview-world-world.jpg](103815-web-preview-preview-world-world.jpg) |
| 10:38:15 | [103815-web-preview-preview-world.jpg](103815-web-preview-preview-world.jpg) |
| 10:38:25 | [103825-scenes-veg-before-wayland-veg-li-vaduz-vineyards.jpg](103825-scenes-veg-before-wayland-veg-li-vaduz-vineyards.jpg) |
| 10:38:36 | [103836-scenes-veg-before-wayland-veg-li-vaduz-vineyards-autumn.jpg](103836-scenes-veg-before-wayland-veg-li-vaduz-vineyards-autumn.jpg) |
| 10:38:48 | [103848-scenes-veg-before-wayland-veg-li-vaduz-orchard.jpg](103848-scenes-veg-before-wayland-veg-li-vaduz-orchard.jpg) |
| 10:38:59 | [103859-scenes-veg-before-wayland-veg-li-triesenberg-forest.jpg](103859-scenes-veg-before-wayland-veg-li-triesenberg-forest.jpg) |
| 10:39:10 | [103910-scenes-veg-before-wayland-veg-li-malbun-treeline.jpg](103910-scenes-veg-before-wayland-veg-li-malbun-treeline.jpg) |
| 10:39:22 | [103922-scenes-veg-before-wayland-veg-li-fields-summer.jpg](103922-scenes-veg-before-wayland-veg-li-fields-summer.jpg) |
| 10:39:33 | [103933-scenes-veg-before-wayland-veg-li-fields-harvest.jpg](103933-scenes-veg-before-wayland-veg-li-fields-harvest.jpg) |
| 10:39:49 | [103949-scenes-veg-before-wayland-veg-tf-bananas.jpg](103949-scenes-veg-before-wayland-veg-tf-bananas.jpg) |
| 10:40:04 | [104004-scenes-veg-before-wayland-veg-tf-canary-pine.jpg](104004-scenes-veg-before-wayland-veg-tf-canary-pine.jpg) |
| 10:40:20 | [104020-scenes-veg-before-wayland-veg-tf-laurel-anaga.jpg](104020-scenes-veg-before-wayland-veg-tf-laurel-anaga.jpg) |
| 10:40:35 | [104035-scenes-veg-before-wayland-veg-tf-laurel-teno.jpg](104035-scenes-veg-before-wayland-veg-tf-laurel-teno.jpg) |
| 10:40:51 | [104051-scenes-veg-before-wayland-veg-tf-palms.jpg](104051-scenes-veg-before-wayland-veg-tf-palms.jpg) |
| 10:41:07 | [104107-scenes-veg-before-wayland-veg-tf-broom.jpg](104107-scenes-veg-before-wayland-veg-tf-broom.jpg) |
| 10:41:22 | [104122-scenes-veg-before-wayland-veg-tf-succulents.jpg](104122-scenes-veg-before-wayland-veg-tf-succulents.jpg) |
| 10:41:38 | [104138-scenes-veg-before-x11-veg-li-vaduz-vineyards.jpg](104138-scenes-veg-before-x11-veg-li-vaduz-vineyards.jpg) |
| 10:41:44 | [104144-scenes-veg-after-wayland-veg-li-vaduz-vineyards.jpg](104144-scenes-veg-after-wayland-veg-li-vaduz-vineyards.jpg) |
| 10:41:56 | [104156-scenes-veg-after-wayland-veg-li-vaduz-vineyards-autumn.jpg](104156-scenes-veg-after-wayland-veg-li-vaduz-vineyards-autumn.jpg) |
| 10:42:03 | [104203-scenes-veg-before-x11-veg-li-vaduz-vineyards-autumn.jpg](104203-scenes-veg-before-x11-veg-li-vaduz-vineyards-autumn.jpg) |
| 10:42:08 | [104208-scenes-veg-after-wayland-veg-li-vaduz-orchard.jpg](104208-scenes-veg-after-wayland-veg-li-vaduz-orchard.jpg) |
| 10:42:19 | [104219-scenes-veg-after-wayland-veg-li-triesenberg-forest.jpg](104219-scenes-veg-after-wayland-veg-li-triesenberg-forest.jpg) |
| 10:42:26 | [104226-scenes-veg-before-x11-veg-li-vaduz-orchard.jpg](104226-scenes-veg-before-x11-veg-li-vaduz-orchard.jpg) |
| 10:42:31 | [104231-scenes-veg-after-wayland-veg-li-malbun-treeline.jpg](104231-scenes-veg-after-wayland-veg-li-malbun-treeline.jpg) |
| 10:42:43 | [104243-scenes-veg-after-wayland-veg-li-fields-summer.jpg](104243-scenes-veg-after-wayland-veg-li-fields-summer.jpg) |
| 10:42:53 | [104253-scenes-veg-before-x11-veg-li-triesenberg-forest.jpg](104253-scenes-veg-before-x11-veg-li-triesenberg-forest.jpg) |
| 10:42:55 | [104255-scenes-veg-after-wayland-veg-li-fields-harvest.jpg](104255-scenes-veg-after-wayland-veg-li-fields-harvest.jpg) |
| 10:43:12 | [104312-scenes-veg-after-wayland-veg-tf-bananas.jpg](104312-scenes-veg-after-wayland-veg-tf-bananas.jpg) |
| 10:43:22 | [104322-scenes-veg-before-x11-veg-li-malbun-treeline.jpg](104322-scenes-veg-before-x11-veg-li-malbun-treeline.jpg) |
| 10:43:31 | [104331-scenes-veg-after-wayland-veg-tf-canary-pine.jpg](104331-scenes-veg-after-wayland-veg-tf-canary-pine.jpg) |
| 10:43:46 | [104346-scenes-veg-before-x11-veg-li-fields-summer.jpg](104346-scenes-veg-before-x11-veg-li-fields-summer.jpg) |
| 10:43:47 | [104347-scenes-veg-after-wayland-veg-tf-laurel-anaga.jpg](104347-scenes-veg-after-wayland-veg-tf-laurel-anaga.jpg) |
| 10:44:04 | [104404-scenes-veg-after-wayland-veg-tf-laurel-teno.jpg](104404-scenes-veg-after-wayland-veg-tf-laurel-teno.jpg) |
| 10:44:05 | [104405-scenes-veg-before-x11-veg-li-fields-harvest.jpg](104405-scenes-veg-before-x11-veg-li-fields-harvest.jpg) |
| 10:44:20 | [104420-scenes-veg-after-wayland-veg-tf-palms.jpg](104420-scenes-veg-after-wayland-veg-tf-palms.jpg) |
| 10:44:29 | [104429-scenes-veg-before-x11-veg-tf-bananas.jpg](104429-scenes-veg-before-x11-veg-tf-bananas.jpg) |
| 10:44:37 | [104437-scenes-veg-after-wayland-veg-tf-broom.jpg](104437-scenes-veg-after-wayland-veg-tf-broom.jpg) |
| 10:44:58 | [104458-scenes-veg-before-x11-veg-tf-canary-pine.jpg](104458-scenes-veg-before-x11-veg-tf-canary-pine.jpg) |
| 10:45:31 | [104531-scenes-veg-before-x11-veg-tf-laurel-anaga.jpg](104531-scenes-veg-before-x11-veg-tf-laurel-anaga.jpg) |
| 10:46:01 | [104601-scenes-veg-before-x11-veg-tf-laurel-teno.jpg](104601-scenes-veg-before-x11-veg-tf-laurel-teno.jpg) |
| 10:46:36 | [104636-scenes-veg-before-x11-veg-tf-palms.jpg](104636-scenes-veg-before-x11-veg-tf-palms.jpg) |
| 10:47:07 | [104707-scenes-veg-before-x11-veg-tf-broom.jpg](104707-scenes-veg-before-x11-veg-tf-broom.jpg) |
| 10:47:36 | [104736-scenes-veg-before-x11-veg-tf-succulents.jpg](104736-scenes-veg-before-x11-veg-tf-succulents.jpg) |
| 10:53:46 | [105346-account-account-signed-out.jpg](105346-account-account-signed-out.jpg) |
| 10:54:07 | [105407-account-account-signed-in.jpg](105407-account-account-signed-in.jpg) |
| 10:54:27 | [105427-account-account-code.jpg](105427-account-account-code.jpg) |
| 10:54:55 | [105455-account-device-page.png](105455-account-device-page.png) |
| 10:57:51 | [105751-vr-vr-sim-both-eyes.jpg](105751-vr-vr-sim-both-eyes.jpg) |
| 10:58:23 | [105823-vr-vr-sim-one-eye.jpg](105823-vr-vr-sim-one-eye.jpg) |
| 10:59:06 | [105906-vr-vr-sim-chase-mirror.jpg](105906-vr-vr-sim-chase-mirror.jpg) |
| 10:59:38 | [105938-vr-vr-sim-blackforest.jpg](105938-vr-vr-sim-blackforest.jpg) |
| 11:00:13 | [110013-vr-vr-no-runtime.jpg](110013-vr-vr-no-runtime.jpg) |
| 11:02:50 | [110250-scenes-veg2-after-wayland-veg-li-vaduz-vineyards.jpg](110250-scenes-veg2-after-wayland-veg-li-vaduz-vineyards.jpg) |
| 11:03:02 | [110302-scenes-veg2-after-wayland-veg-li-vaduz-vineyards-autumn.jpg](110302-scenes-veg2-after-wayland-veg-li-vaduz-vineyards-autumn.jpg) |
| 11:03:13 | [110313-scenes-veg2-after-wayland-veg-li-vaduz-orchard.jpg](110313-scenes-veg2-after-wayland-veg-li-vaduz-orchard.jpg) |
| 11:03:24 | [110324-scenes-veg2-after-wayland-veg-li-triesenberg-forest.jpg](110324-scenes-veg2-after-wayland-veg-li-triesenberg-forest.jpg) |
| 11:03:36 | [110336-scenes-veg2-after-wayland-veg-li-malbun-treeline.jpg](110336-scenes-veg2-after-wayland-veg-li-malbun-treeline.jpg) |
| 11:03:47 | [110347-scenes-veg2-after-wayland-veg-li-fields-summer.jpg](110347-scenes-veg2-after-wayland-veg-li-fields-summer.jpg) |
| 11:03:59 | [110359-scenes-veg2-after-wayland-veg-li-fields-harvest.jpg](110359-scenes-veg2-after-wayland-veg-li-fields-harvest.jpg) |
| 11:04:14 | [110414-scenes-veg2-after-wayland-veg-tf-bananas.jpg](110414-scenes-veg2-after-wayland-veg-tf-bananas.jpg) |
| 11:04:31 | [110431-scenes-veg2-after-wayland-veg-tf-canary-pine.jpg](110431-scenes-veg2-after-wayland-veg-tf-canary-pine.jpg) |
| 11:04:47 | [110447-scenes-veg2-after-wayland-veg-tf-laurel-anaga.jpg](110447-scenes-veg2-after-wayland-veg-tf-laurel-anaga.jpg) |
| 11:05:03 | [110503-scenes-veg2-after-wayland-veg-tf-laurel-teno.jpg](110503-scenes-veg2-after-wayland-veg-tf-laurel-teno.jpg) |
| 11:05:20 | [110520-scenes-veg2-after-wayland-veg-tf-palms.jpg](110520-scenes-veg2-after-wayland-veg-tf-palms.jpg) |
| 11:05:36 | [110536-scenes-veg2-after-wayland-veg-tf-broom.jpg](110536-scenes-veg2-after-wayland-veg-tf-broom.jpg) |
| 11:05:53 | [110553-scenes-veg2-after-wayland-veg-tf-succulents.jpg](110553-scenes-veg2-after-wayland-veg-tf-succulents.jpg) |
| 11:06:12 | [110612-scenes-veg2-after-wayland-veg-bf-spruce-fir-meadows.jpg](110612-scenes-veg2-after-wayland-veg-bf-spruce-fir-meadows.jpg) |
| 11:06:29 | [110629-scenes-veg2-after-wayland-veg-bf-schauinsland-forest.jpg](110629-scenes-veg2-after-wayland-veg-bf-schauinsland-forest.jpg) |
| 11:06:47 | [110647-scenes-veg2-after-wayland-veg-bf-kaiserstuhl-vineyards.jpg](110647-scenes-veg2-after-wayland-veg-bf-kaiserstuhl-vineyards.jpg) |
| 11:07:04 | [110704-scenes-veg2-after-wayland-veg-bf-ortenau-vineyards.jpg](110704-scenes-veg2-after-wayland-veg-bf-ortenau-vineyards.jpg) |
| 11:07:19 | [110719-scenes-veg2-after-wayland-veg-bf-ortenau-orchards.jpg](110719-scenes-veg2-after-wayland-veg-bf-ortenau-orchards.jpg) |
| 11:07:37 | [110737-scenes-veg2-after-wayland-veg-bf-fields-summer.jpg](110737-scenes-veg2-after-wayland-veg-bf-fields-summer.jpg) |
| 11:07:53 | [110753-scenes-veg2-after-wayland-veg-bf-fields-harvest.jpg](110753-scenes-veg2-after-wayland-veg-bf-fields-harvest.jpg) |
| 11:08:10 | [110810-scenes-veg2-after-wayland-veg-bf-fields-autumn.jpg](110810-scenes-veg2-after-wayland-veg-bf-fields-autumn.jpg) |
| 11:08:24 | [110824-scenes-veg2-after-x11-veg-li-vaduz-vineyards.jpg](110824-scenes-veg2-after-x11-veg-li-vaduz-vineyards.jpg) |
| 11:08:46 | [110846-scenes-veg2-after-x11-veg-li-vaduz-vineyards-autumn.jpg](110846-scenes-veg2-after-x11-veg-li-vaduz-vineyards-autumn.jpg) |
| 11:09:09 | [110909-scenes-veg2-after-x11-veg-li-vaduz-orchard.jpg](110909-scenes-veg2-after-x11-veg-li-vaduz-orchard.jpg) |
| 11:09:36 | [110936-scenes-veg2-after-x11-veg-li-triesenberg-forest.jpg](110936-scenes-veg2-after-x11-veg-li-triesenberg-forest.jpg) |
| 11:10:08 | [111008-scenes-veg2-after-x11-veg-li-malbun-treeline.jpg](111008-scenes-veg2-after-x11-veg-li-malbun-treeline.jpg) |
| 11:10:39 | [111039-scenes-veg2-after-x11-veg-li-fields-summer.jpg](111039-scenes-veg2-after-x11-veg-li-fields-summer.jpg) |
| 11:11:05 | [111105-scenes-veg2-after-x11-veg-li-fields-harvest.jpg](111105-scenes-veg2-after-x11-veg-li-fields-harvest.jpg) |
| 11:11:34 | [111134-scenes-veg2-after-x11-veg-tf-bananas.jpg](111134-scenes-veg2-after-x11-veg-tf-bananas.jpg) |
| 11:12:10 | [111210-scenes-veg2-after-x11-veg-tf-canary-pine.jpg](111210-scenes-veg2-after-x11-veg-tf-canary-pine.jpg) |
| 11:12:46 | [111246-scenes-veg2-after-x11-veg-tf-laurel-anaga.jpg](111246-scenes-veg2-after-x11-veg-tf-laurel-anaga.jpg) |
| 11:13:18 | [111318-scenes-veg2-after-x11-veg-tf-laurel-teno.jpg](111318-scenes-veg2-after-x11-veg-tf-laurel-teno.jpg) |
| 11:13:44 | [111344-scenes-veg2-after-x11-veg-tf-palms.jpg](111344-scenes-veg2-after-x11-veg-tf-palms.jpg) |
| 11:14:08 | [111408-scenes-veg2-after-x11-veg-tf-broom.jpg](111408-scenes-veg2-after-x11-veg-tf-broom.jpg) |
| 11:14:32 | [111432-scenes-veg2-after-x11-veg-tf-succulents.jpg](111432-scenes-veg2-after-x11-veg-tf-succulents.jpg) |
| 11:15:04 | [111504-scenes-veg2-after-x11-veg-bf-spruce-fir-meadows.jpg](111504-scenes-veg2-after-x11-veg-bf-spruce-fir-meadows.jpg) |
| 11:15:40 | [111540-scenes-veg2-after-x11-veg-bf-schauinsland-forest.jpg](111540-scenes-veg2-after-x11-veg-bf-schauinsland-forest.jpg) |
| 11:16:17 | [111617-scenes-veg2-after-x11-veg-bf-kaiserstuhl-vineyards.jpg](111617-scenes-veg2-after-x11-veg-bf-kaiserstuhl-vineyards.jpg) |
| 11:16:49 | [111649-scenes-veg2-after-x11-veg-bf-ortenau-vineyards.jpg](111649-scenes-veg2-after-x11-veg-bf-ortenau-vineyards.jpg) |
| 11:17:29 | [111729-scenes-veg2-after-x11-veg-bf-ortenau-orchards.jpg](111729-scenes-veg2-after-x11-veg-bf-ortenau-orchards.jpg) |
| 11:18:12 | [111812-scenes-veg2-after-x11-veg-bf-fields-summer.jpg](111812-scenes-veg2-after-x11-veg-bf-fields-summer.jpg) |
| 11:18:49 | [111849-scenes-veg2-after-x11-veg-bf-fields-harvest.jpg](111849-scenes-veg2-after-x11-veg-bf-fields-harvest.jpg) |
| 11:19:26 | [111926-scenes-veg2-after-x11-veg-bf-fields-autumn.jpg](111926-scenes-veg2-after-x11-veg-bf-fields-autumn.jpg) |
| 11:20:01 | [112001-scenes-veg2-before-wayland-veg-bf-spruce-fir-meadows.jpg](112001-scenes-veg2-before-wayland-veg-bf-spruce-fir-meadows.jpg) |
| 11:20:18 | [112018-scenes-veg2-before-wayland-veg-bf-schauinsland-forest.jpg](112018-scenes-veg2-before-wayland-veg-bf-schauinsland-forest.jpg) |
| 11:20:35 | [112035-scenes-veg2-before-wayland-veg-bf-kaiserstuhl-vineyards.jpg](112035-scenes-veg2-before-wayland-veg-bf-kaiserstuhl-vineyards.jpg) |
| 11:20:52 | [112052-scenes-veg2-before-wayland-veg-bf-ortenau-vineyards.jpg](112052-scenes-veg2-before-wayland-veg-bf-ortenau-vineyards.jpg) |
| 11:21:09 | [112109-scenes-veg2-before-wayland-veg-bf-ortenau-orchards.jpg](112109-scenes-veg2-before-wayland-veg-bf-ortenau-orchards.jpg) |
| 11:21:28 | [112128-scenes-veg2-before-wayland-veg-bf-fields-summer.jpg](112128-scenes-veg2-before-wayland-veg-bf-fields-summer.jpg) |
| 11:21:47 | [112147-scenes-veg2-before-wayland-veg-bf-fields-harvest.jpg](112147-scenes-veg2-before-wayland-veg-bf-fields-harvest.jpg) |
| 11:22:05 | [112205-scenes-veg2-before-wayland-veg-bf-fields-autumn.jpg](112205-scenes-veg2-before-wayland-veg-bf-fields-autumn.jpg) |
| 11:22:32 | [112232-scenes-veg2-before-x11-veg-bf-spruce-fir-meadows.jpg](112232-scenes-veg2-before-x11-veg-bf-spruce-fir-meadows.jpg) |
| 11:23:18 | [112318-scenes-veg2-before-x11-veg-bf-schauinsland-forest.jpg](112318-scenes-veg2-before-x11-veg-bf-schauinsland-forest.jpg) |
| 11:24:01 | [112401-scenes-veg2-before-x11-veg-bf-kaiserstuhl-vineyards.jpg](112401-scenes-veg2-before-x11-veg-bf-kaiserstuhl-vineyards.jpg) |
| 11:24:40 | [112440-scenes-veg2-before-x11-veg-bf-ortenau-vineyards.jpg](112440-scenes-veg2-before-x11-veg-bf-ortenau-vineyards.jpg) |
| 11:25:18 | [112518-scenes-veg2-before-x11-veg-bf-ortenau-orchards.jpg](112518-scenes-veg2-before-x11-veg-bf-ortenau-orchards.jpg) |
| 11:25:43 | [112543-scenes-veg2-before-x11-veg-bf-fields-summer.jpg](112543-scenes-veg2-before-x11-veg-bf-fields-summer.jpg) |
| 11:26:08 | [112608-scenes-veg2-before-x11-veg-bf-fields-harvest.jpg](112608-scenes-veg2-before-x11-veg-bf-fields-harvest.jpg) |
| 11:26:36 | [112636-scenes-veg2-before-x11-veg-bf-fields-autumn.jpg](112636-scenes-veg2-before-x11-veg-bf-fields-autumn.jpg) |
| 11:26:48 | [112648-vr-vr-sim-both-eyes.jpg](112648-vr-vr-sim-both-eyes.jpg) |
| 11:27:08 | [112708-vr-vr-sim-one-eye.jpg](112708-vr-vr-sim-one-eye.jpg) |
| 11:27:51 | [112751-vr-vr-sim-chase-mirror.jpg](112751-vr-vr-sim-chase-mirror.jpg) |
| 11:28:27 | [112827-vr-vr-sim-blackforest.jpg](112827-vr-vr-sim-blackforest.jpg) |
| 11:29:01 | [112901-vr-vr-no-runtime.jpg](112901-vr-vr-no-runtime.jpg) |
| 11:41:08 | [114108-web-preview-preview-hills.jpg](114108-web-preview-preview-hills.jpg) |
| 11:41:08 | [114108-web-preview-preview-untrusted.jpg](114108-web-preview-preview-untrusted.jpg) |
| 11:41:08 | [114108-web-preview-preview-webgl2.jpg](114108-web-preview-preview-webgl2.jpg) |
| 11:41:08 | [114108-web-preview-preview-world-world-loading.jpg](114108-web-preview-preview-world-world-loading.jpg) |
| 11:41:08 | [114108-web-preview-preview-world-world.jpg](114108-web-preview-preview-world-world.jpg) |
| 11:41:08 | [114108-web-preview-preview-world.jpg](114108-web-preview-preview-world.jpg) |
| 11:48:46 | [114846-scenes-veg3-after-wayland-veg-li-vaduz-vineyards.jpg](114846-scenes-veg3-after-wayland-veg-li-vaduz-vineyards.jpg) |
| 11:48:57 | [114857-scenes-veg3-after-wayland-veg-li-vaduz-vineyards-autumn.jpg](114857-scenes-veg3-after-wayland-veg-li-vaduz-vineyards-autumn.jpg) |
| 11:49:09 | [114909-scenes-veg3-after-wayland-veg-li-vaduz-orchard.jpg](114909-scenes-veg3-after-wayland-veg-li-vaduz-orchard.jpg) |
| 11:49:21 | [114921-scenes-veg3-after-wayland-veg-li-triesenberg-forest.jpg](114921-scenes-veg3-after-wayland-veg-li-triesenberg-forest.jpg) |
| 11:49:32 | [114932-scenes-veg3-after-wayland-veg-li-malbun-treeline.jpg](114932-scenes-veg3-after-wayland-veg-li-malbun-treeline.jpg) |
| 11:49:43 | [114943-scenes-veg3-after-wayland-veg-li-fields-summer.jpg](114943-scenes-veg3-after-wayland-veg-li-fields-summer.jpg) |
| 11:49:55 | [114955-scenes-veg3-after-wayland-veg-li-fields-harvest.jpg](114955-scenes-veg3-after-wayland-veg-li-fields-harvest.jpg) |
| 11:50:10 | [115010-scenes-veg3-after-wayland-veg-tf-bananas.jpg](115010-scenes-veg3-after-wayland-veg-tf-bananas.jpg) |
| 11:50:27 | [115027-scenes-veg3-after-wayland-veg-tf-canary-pine.jpg](115027-scenes-veg3-after-wayland-veg-tf-canary-pine.jpg) |
| 11:50:43 | [115043-scenes-veg3-after-wayland-veg-tf-laurel-anaga.jpg](115043-scenes-veg3-after-wayland-veg-tf-laurel-anaga.jpg) |
| 11:50:59 | [115059-scenes-veg3-after-wayland-veg-tf-laurel-teno.jpg](115059-scenes-veg3-after-wayland-veg-tf-laurel-teno.jpg) |
| 11:51:15 | [115115-scenes-veg3-after-wayland-veg-tf-palms.jpg](115115-scenes-veg3-after-wayland-veg-tf-palms.jpg) |
| 11:51:31 | [115131-scenes-veg3-after-wayland-veg-tf-broom.jpg](115131-scenes-veg3-after-wayland-veg-tf-broom.jpg) |
| 11:51:46 | [115146-scenes-veg3-after-wayland-veg-tf-succulents.jpg](115146-scenes-veg3-after-wayland-veg-tf-succulents.jpg) |
| 11:52:03 | [115203-scenes-veg3-after-wayland-veg-bf-spruce-fir-meadows.jpg](115203-scenes-veg3-after-wayland-veg-bf-spruce-fir-meadows.jpg) |
| 11:52:20 | [115220-scenes-veg3-after-wayland-veg-bf-schauinsland-forest.jpg](115220-scenes-veg3-after-wayland-veg-bf-schauinsland-forest.jpg) |
| 11:52:36 | [115236-scenes-veg3-after-wayland-veg-bf-kaiserstuhl-vineyards.jpg](115236-scenes-veg3-after-wayland-veg-bf-kaiserstuhl-vineyards.jpg) |
| 11:52:52 | [115252-scenes-veg3-after-wayland-veg-bf-ortenau-vineyards.jpg](115252-scenes-veg3-after-wayland-veg-bf-ortenau-vineyards.jpg) |
| 11:53:07 | [115307-scenes-veg3-after-wayland-veg-bf-ortenau-orchards.jpg](115307-scenes-veg3-after-wayland-veg-bf-ortenau-orchards.jpg) |
| 11:53:24 | [115324-scenes-veg3-after-wayland-veg-bf-fields-summer.jpg](115324-scenes-veg3-after-wayland-veg-bf-fields-summer.jpg) |
| 11:53:40 | [115340-scenes-veg3-after-wayland-veg-bf-fields-harvest.jpg](115340-scenes-veg3-after-wayland-veg-bf-fields-harvest.jpg) |
| 11:53:56 | [115356-scenes-veg3-after-wayland-veg-bf-fields-autumn.jpg](115356-scenes-veg3-after-wayland-veg-bf-fields-autumn.jpg) |
| 11:54:11 | [115411-scenes-veg3-after-x11-veg-li-vaduz-vineyards.jpg](115411-scenes-veg3-after-x11-veg-li-vaduz-vineyards.jpg) |
| 11:54:31 | [115431-scenes-veg3-after-x11-veg-li-vaduz-vineyards-autumn.jpg](115431-scenes-veg3-after-x11-veg-li-vaduz-vineyards-autumn.jpg) |
| 11:54:52 | [115452-scenes-veg3-after-x11-veg-li-vaduz-orchard.jpg](115452-scenes-veg3-after-x11-veg-li-vaduz-orchard.jpg) |
| 11:55:14 | [115514-scenes-veg3-after-x11-veg-li-triesenberg-forest.jpg](115514-scenes-veg3-after-x11-veg-li-triesenberg-forest.jpg) |
| 11:55:35 | [115535-scenes-veg3-after-x11-veg-li-malbun-treeline.jpg](115535-scenes-veg3-after-x11-veg-li-malbun-treeline.jpg) |
| 11:55:54 | [115554-scenes-veg3-after-x11-veg-li-fields-summer.jpg](115554-scenes-veg3-after-x11-veg-li-fields-summer.jpg) |
| 11:56:12 | [115612-scenes-veg3-after-x11-veg-li-fields-harvest.jpg](115612-scenes-veg3-after-x11-veg-li-fields-harvest.jpg) |
| 11:56:34 | [115634-scenes-veg3-after-x11-veg-tf-bananas.jpg](115634-scenes-veg3-after-x11-veg-tf-bananas.jpg) |
| 11:57:02 | [115702-scenes-veg3-after-x11-veg-tf-canary-pine.jpg](115702-scenes-veg3-after-x11-veg-tf-canary-pine.jpg) |
| 11:57:31 | [115731-scenes-veg3-after-x11-veg-tf-laurel-anaga.jpg](115731-scenes-veg3-after-x11-veg-tf-laurel-anaga.jpg) |
| 11:57:57 | [115757-scenes-veg3-after-x11-veg-tf-laurel-teno.jpg](115757-scenes-veg3-after-x11-veg-tf-laurel-teno.jpg) |
| 11:58:24 | [115824-scenes-veg3-after-x11-veg-tf-palms.jpg](115824-scenes-veg3-after-x11-veg-tf-palms.jpg) |
| 11:58:47 | [115847-scenes-veg3-after-x11-veg-tf-broom.jpg](115847-scenes-veg3-after-x11-veg-tf-broom.jpg) |
| 11:59:11 | [115911-scenes-veg3-after-x11-veg-tf-succulents.jpg](115911-scenes-veg3-after-x11-veg-tf-succulents.jpg) |
| 11:59:42 | [115942-scenes-veg3-after-x11-veg-bf-spruce-fir-meadows.jpg](115942-scenes-veg3-after-x11-veg-bf-spruce-fir-meadows.jpg) |
| 12:00:13 | [120013-scenes-veg3-after-x11-veg-bf-schauinsland-forest.jpg](120013-scenes-veg3-after-x11-veg-bf-schauinsland-forest.jpg) |
| 12:00:42 | [120042-scenes-veg3-after-x11-veg-bf-kaiserstuhl-vineyards.jpg](120042-scenes-veg3-after-x11-veg-bf-kaiserstuhl-vineyards.jpg) |
| 12:01:09 | [120109-scenes-veg3-after-x11-veg-bf-ortenau-vineyards.jpg](120109-scenes-veg3-after-x11-veg-bf-ortenau-vineyards.jpg) |
| 12:01:36 | [120136-scenes-veg3-after-x11-veg-bf-ortenau-orchards.jpg](120136-scenes-veg3-after-x11-veg-bf-ortenau-orchards.jpg) |
| 12:02:06 | [120206-scenes-veg3-after-x11-veg-bf-fields-summer.jpg](120206-scenes-veg3-after-x11-veg-bf-fields-summer.jpg) |
| 12:02:30 | [120230-scenes-veg3-after-x11-veg-bf-fields-harvest.jpg](120230-scenes-veg3-after-x11-veg-bf-fields-harvest.jpg) |
| 12:02:59 | [120259-scenes-veg3-after-x11-veg-bf-fields-autumn.jpg](120259-scenes-veg3-after-x11-veg-bf-fields-autumn.jpg) |
| 12:03:05 | [120305-web-web-account-linked.jpg](120305-web-web-account-linked.jpg) |
| 12:03:05 | [120305-web-web-account-signed-in.jpg](120305-web-web-account-signed-in.jpg) |
| 12:03:05 | [120305-web-web-account-signed-out.jpg](120305-web-web-account-signed-out.jpg) |
| 12:03:29 | [120329-scenes-veg3-before-wayland-veg-li-triesenberg-forest.jpg](120329-scenes-veg3-before-wayland-veg-li-triesenberg-forest.jpg) |
| 12:03:43 | [120343-scenes-veg3-before-x11-veg-li-triesenberg-forest.jpg](120343-scenes-veg3-before-x11-veg-li-triesenberg-forest.jpg) |
| 12:04:59 | [120459-vr-vr-sim-both-eyes.jpg](120459-vr-vr-sim-both-eyes.jpg) |
| 12:05:04 | [120504-account-account-signed-out.jpg](120504-account-account-signed-out.jpg) |
| 12:05:21 | [120521-vr-vr-sim-one-eye.jpg](120521-vr-vr-sim-one-eye.jpg) |
| 12:05:24 | [120524-account-account-signed-in.jpg](120524-account-account-signed-in.jpg) |
| 12:05:45 | [120545-account-account-code.jpg](120545-account-account-code.jpg) |
| 12:06:01 | [120601-vr-vr-sim-chase-mirror.jpg](120601-vr-vr-sim-chase-mirror.jpg) |
| 12:06:12 | [120612-account-device-page.png](120612-account-device-page.png) |
| 12:06:35 | [120635-vr-vr-sim-blackforest.jpg](120635-vr-vr-sim-blackforest.jpg) |
| 12:07:10 | [120710-vr-vr-no-runtime.jpg](120710-vr-vr-no-runtime.jpg) |
