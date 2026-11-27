# OCW build diary – day 17, 2026-11-27

82 commits (36 merges), +105872 / −944 lines, 675 images, 43 videos, 0 sounds.

## Commits

| Time | Commit | |
|---|---|---|
| 00:11 | `3a355e94` | Kiosks join the Fly.io game server: OCW_KIOSK_SERVER=remote (spec 11.2, 11.5; v6.65) |
| 00:19 | `7b842cdc` (merge) | Merge the browser's on-page log (?log=1, five taps, Show log on errors) (10G; 6.67) |
| 00:19 | `adb79825` (merge) | Merge the landscape fixes: shores on the OSM outlines, rivers as strips, a water material, far forests in their colour, alpine turf and rock above the tree line, no towers of dismantled power lines, lattice pylons (4.6.3; 6.68) |
| 00:20 | `a7193d0a` (merge) | Merge the kiosks joining a remote server: OCW_KIOSK_SERVER=remote with the Fly join info, fallback to the local server, the join key in join.json (11.2, 11.5; 6.69) |
| 02:45 | `c28f31d9` | Status page shows the names of riders online (11.5 Q1 (b)) |
| 02:46 | `d6ed8601` | VR kiosk built with voice (Phase 11 Q15 (a)) |
| 02:47 | `837f67f6` | deploy-test-windows.sh: header names the vr,voice build |
| 02:57 | `a5baf1d4` | vendor: bevy_render 0.20.1 exactly as published on crates.io |
| 03:48 | `56ae0840` | Status page names the riders on the road: /stats.json riders.online with the names they ride under, bots and Echo marked, time and km this ride, capped at 50 with "+N more"; no IPs or positions; even stat grid (11.5 Q1 (b); 6.73) |
| 04:02 | `0db74fa7` | vendor/bevy_render: the pipeline cache's per-frame compile budget and compile log |
| 04:02 | `6981b672` | Switches in the address find what closes the browser app on a phone; the early page log keeps every line, pipeline compile, frame time and memory sample |
| 04:02 | `3901ed89` (merge) | Merge the phone crash bisect: address switches, early log, pipelines paced on WebGL 2, LiveKit loaded on joining voice (10G; 6.74) |
| 04:58 | `e2afcf56` | Russet alpine grass, no evening glow on the far land (spec 4.6.3 v6.72) |
| 05:05 | `8f30943e` (merge) | Merge the landscape follow-ups: russet dormant grass above the tree line, far land without the low-sun glare (4.6.3, 9I; 6.75) |
| 05:15 | `47a77e4f` | Open question 11.3 Q2: turning the kiosks on again (both off; marge on Fly; marge on Fly + leela local; both on Fly); Appendix C regenerated |
| 06:02 | `ac614c00` (merge) | Merge main (open question 11.3 Q2) into the landscape merge; the landscape row is 6.76 |
| 06:34 | `9320b088` | Built: world packages carry traffic data – TRFC (rules per road edge, signals, bus stops and lines, car parks) and AERO (aerodromes, runways, helipads, nearby airports); world-builder traffic, lint reports roads without speed data (14 Phase 18, 18E T2; v6.76) |
| 06:35 | `1e461443` (merge) | Merge traffic T2: TRFC traffic rules and AERO aerodromes in the world packages, world-builder traffic and lint (18B, 18C, 18E T2; 6.77) |
| 07:15 | `062c9369` | Road traffic core built (Phase 18 T3, ocw-sim::traffic): IDM car following, lanes, junction rules and signals, routes by the rules, spawning around the riders' bubbles by the demand of the hour, plans plus change events (Q3); spec 6.76 |
| 07:16 | `64526a06` (merge) | Merge traffic T3: the road traffic core ocw-sim::traffic – vehicles, IDM, lanes, junctions and signals, bubbles, demand, plans and changes (18E T3; 6.78) |
| 07:28 | `f4f5bbce` | Traffic T1 built: Settings → Traffic in both apps, the session's road traffic decided by the server (traffic_access host / anyone / nobody), the air seed and the traffic command (14 Phase 18, 18E T1; v6.76) |
| 07:29 | `b23d697b` (merge) | Merge traffic T1: the [traffic] settings, Settings → Traffic in both apps, the server's traffic access and the protocol fields; Voice moves under Audio (18E T1; 6.79) |
| 07:31 | `09f36aed` | The traffic's models: a vehicle kind with validator rules and 15 generic low-poly models (18E T6) |
| 07:32 | `8c9ebc25` (merge) | Merge traffic T6: the vehicle model kind, its validator and 15 generated vehicles and aircraft (18E T6, 18G; 6.80) |
| 07:33 | `6930f471` | The public server on Fly.io is the default server of every app, for now: Join a ride and the start choice offer it first, --join public, the browser's fallback, setting net.public_server (spec 6.76, 11.5) |
| 08:16 | `f342f0df` (merge) | Merge the public server as the default: ocw-server.fly.dev in Join a ride, the start choice, --join public, the browser's fallback; net.public_server (11.5, 3.2.1; 6.81) |
| 08:58 | `dc3f1141` | The HUD's heart rate gets a beating heart: pink and pounding while the heart rate rises (v6.77) |
| 09:08 | `8dd35342` | Traffic T8 built: simulated aircraft – airways, approaches and departures, circuits, helicopters, gliders, balloons, contrails, drawn and heard with the delay of sound (14 Phase 18, 18C, 18E T8; 6.81) |
| 09:15 | `fd625698` (merge) | Merge the heart-rate heart: beats with the measured heart rate, pink and pounding while it rises; hr.test (3.2; 6.82) |
| 09:40 | `1bfead9d` | Traffic T5 built: the server runs the road traffic and sends each rider the vehicles near it as plans and changes; the client extrapolates them, debug boxes draw them (14 Phase 18, 18E T5, 18H; Q3 (a); 6.81) |
| 09:42 | `5f3b016a` | Shadows off on iOS WebKit with WebGL 2 by default, iOS starts in the saver memory mode (6.77, 10G) |
| 09:43 | `f7ff92f9` (merge) | Merge the iPhone fix: shadows off on iOS WebKit with WebGL 2, the saver memory profile on iOS, shadowmap / shadowfix test switches, the GPU-memory estimate in the page log (10G; 6.83) |
| 09:44 | `7ae3a992` | A world switch no longer crashes on a background build that finishes after its chunk is gone (spec 3.2.1, v6.77) |
| 09:47 | `2ae1640c` | Aircraft: terrain floors ramp without lifting planned descents, the contrail ribbon as a tested function, thinner trails, the browser test (18E T8) |
| 09:59 | `d016ea00` | Spec 10G: the measured test runs and GPU allocations of v6.77 |
| 10:14 | `17fa33b6` | Aircraft: arrivals land in their slots, apart as by the tower (18E T8) |
| 10:27 | `afdb4d29` | Traffic T4: vehicles pass riders only with the legal distance, a free oncoming lane and the sight distance, else wait; yield at junctions; driver manners and lunatics; contacts with collisions on, the lorry gust, the proximity cue (18E T4; Q4, Q8; 6.81) |
| 10:41 | `08c47fb7` (merge) | Merge traffic T4 into T5: one package adapter (WorldRules), T4's shift in the plans on the wire, contacts and gusts wired into the session (18E T4 / T5; 6.81) |
| 11:01 | `41b590aa` (merge) | Merge remote-tracking branch 'origin/worktree-agent-ad78328f42bb43590' into merge/rel |
| 11:03 | `ede18971` (merge) | Merge the world-switch crash fix: late results of an old scene are dropped (late_insert, SceneGeneration); the desktop's world change in PreUpdate (3.2.1; 6.84) |
| 11:48 | `f99daa2a` | Release 0.2.7 |
| 11:58 | `9787d780` | prepare-world-release: name the traffic sections TRFC and AERO in LICENSE-DATA.md's ODbL note |
| 12:07 | `f668ba4a` (merge) | Merge remote-tracking branch 'origin/traffic-t8-aircraft' into worktree-agent-a1afa9e7262945472 |
| 12:18 | `f874a416` | iPhone results: every shadow variant closes the page, the shadow-free default rides; shadows stay off on iOS WebKit with WebGL 2 (10G) |
| 12:26 | `a0206afc` | vercel.json: no Vercel deployments from git pushes (the servers run on Fly.io; the user, 2026-11-27: disable all deployments on Vercel) |
| 12:40 | `cdf18ef3` (merge) | Merge the release-script fix: TRFC and AERO named in LICENSE-DATA.md's ODbL note |
| 12:43 | `0d489e6c` (merge) | Merge traffic T4 and T5: vehicles around riders (passing distances, manners, lunatic, collisions, gusts) and the road traffic in the server, network and client (18E T4, T5; 6.86, 6.87) |
| 12:43 | `6ba1cb74` (merge) | Merge traffic T8: simulated aircraft – airways, approaches, circuits, helicopters, gliders, balloons, contrails, lights and sound (18C, 18E T8; 6.88) |
| 12:56 | `15426a24` | Fly image: send vendor/bevy_render in the build context |
| 13:17 | `4226c06c` | No ride photos on iOS WebKit with WebGL 2 by default: the first photo closed the page on an iPhone (10G, 6.86) |
| 13:55 | `66e28505` (merge) | Merge the Fly build fix: vendor/bevy_render in the Docker build context (the bevy_render patch since 0db74fa7) |
| 14:09 | `178c4c0a` | ANT+ FE-C smart trainers built: pages 16/25 to power, SIM/ERG as pages 49/50/51/55 one acknowledged message at a time, Use as trainer, a simulated FE-C trainer (14 Phase 17, 17E; 6.86) |
| 14:41 | `0843a715` | test-web-bisect: wait on the log's lines, photofix=all case; clippy and fmt (10G, 6.86) |
| 14:43 | `e8e3387b` | Aircraft flyby: air.follow (a camera and the unicorn flying with one aircraft) and the true-size check of the aircraft models (T8) |
| 14:43 | `f8db40a6` (merge) | Merge remote-tracking branch 'origin/main' into worktree-agent-a1afa9e7262945472 |
| 15:04 | `6a690827` | Spec 10G: the ride-photo tests as measured on marge (6.86) |
| 15:04 | `cbe1992e` | ANT+ in the browser over WebUSB, without hardware (14 Phase 17 A5, 17E The browser; Q3 (a) + (b); 6.85) |
| 15:05 | `0d9e5cbc` (merge) | Merge the iPhone photo fix: ride photos off on iOS WebKit with WebGL 2, photos / photofix switches, an RGBA photo target and fewer frames on WebGL 2 (10G; 6.89) |
| 15:05 | `224a80a8` (merge) | Merge ANT+ FE-C: trainer control over ANT+ (pages 16/25, 49/50/51/55, acknowledged one at a time), the trainer role, Use as trainer, a simulated FE-C trainer (17E; 6.90) |
| 15:05 | `6541b9e4` | Traffic: the permanent queue at Liechtenstein's two main-road junctions fixed – gridlocks around short side-road edges (18H, 18E T3/T5; 6.89) |
| 15:05 | `d65b3534` (merge) | Merge ANT+ over WebUSB in the browser: ant::web on navigator.usb, Add an ANT+ stick, the key kept in this browser only (17A A5, 17E; 6.91) |
| 15:37 | `9e2eaf60` | ANT+ power meters with torque pages and calibration, speed / cadence sensors, FIT device_info for ANT+ sensors (spec 14 Phase 17, 17E, A6; 6.85) |
| 15:38 | `d58861c7` (merge) | Merge the traffic junction fix: no gridlock on short side-road edges, don't block the box, a yielding car doesn't wait for a standing one (18H; 6.92) |
| 15:38 | `ada17a88` (merge) | Merge air.follow: a camera and the unicorn keyed to an aircraft (the flyby videos), aircraft drawn at true size tested, camera.path keeps another guide's camera (T8; 6.93) |
| 15:41 | `9079cec4` | Merge fix: the WebUSB menu test's Entry gets FE-C's trainer field |
| 15:43 | `98ea35a7` | Merge fix: the browser's ANT+ glue knows FE-C trainers (DeviceKind::Trainer) and FE-C's trainer field |
| 15:55 | `b6d084f8` | Traffic T7: road vehicles drawn with their models and heard – instanced by model and level within the quality's budget, regional paint from the look seed, turning wheels, the trailer following the kingpin, headlights / brake lamps / indicators / bus interior, cones and spot lights at night, spray on wet roads, tyre and engine sounds with Doppler (8 voices), pass-by whoosh, honks and the proximity cue (18E T7, 18I; 6.89) |
| 15:58 | `157e2b51` (merge) | Merge the FE-C branch into the power / speed-cadence branch: one StickCore::command, one transfer path (transfer_result) for FE-C control and calibration, FE-C common pages as device_info |
| 15:59 | `0246ad11` (merge) | Merge origin/main (traffic T4/T5/T8, Fly fix) into the ANT+ power / speed-cadence branch; the version row renumbered to 6.89 |
| 16:26 | `410f1cce` (merge) | Merge origin/main (ANT+ FE-C 6.90, WebUSB 6.91, traffic) into the ANT+ power / speed-cadence branch: one StickCore::command and one transfer path for FE-C control and calibration; speed / cadence profiles in the browser's kind map; the version row renumbered to 6.94 |
| 16:27 | `b56d226a` (merge) | Merge traffic T7: road vehicles drawn with their models (instanced, LOD, regional paint), lamps, spray and sound with Doppler, pass-by and proximity cues; headlight spots toned down to 45 000 (18E T7, 18I; 6.94) |
| 17:11 | `894edf69` (merge) | Merge ANT+ power meters and speed/cadence: torque pages, calibration and auto zero, speed/cadence sensors with Use for cadence, FIT device_info for ANT+ sensors, one command and transfer path with FE-C (17E, A6; 6.95) |
| 18:37 | `a8c585bb` | Traffic T9: UFOs and the unicorn – rare sightings on clear nights, on often also at dusk and by day high in the sky, crop circles that stay for the session, a cow lifted by a beam and set down a field away, and the unicorn's curious visitor; the same for every rider from the air seed and the clock, never in events, never near a rider; the hum and the whoosh (18C, 18E T9; Q7; 6.96) |
| 18:38 | `2922c197` (merge) | Merge traffic T9: UFOs – rare night sightings, by day on often, the unicorn's visitor, crop circles, the cow beam (18C, 18E T9; 6.96) |
| 19:22 | `4488f040` | Buses run on their OSM lines and stop at every stop, parked cars stand along the kerbs and in the car parks (18B, 18H; 6.95) |
| 19:24 | `f4334a44` (merge) | Merge buses on their lines and parked cars: OSM bus routes with timetables and stops (doors open), parked cars along the kerbs and in car parks (18B, 18H; 6.97) |
| 19:39 | `00cfba89` | Traffic T10: live aircraft from adsb.lol as an opt-in (Aircraft: live) – the game server fetches for its riders within adsb.lol's limits and shares them without identities, the clients extrapolate and draw them with the credit, the simulated sky when the feed is down; T8's light dots bright (18C, 18D, 18E T10, 18J; Q6 (b); 6.96) |
| 19:48 | `d256d26e` | package tests: wait for in-flight builds by wall time (120 s), not 3000 frames – flaky on a loaded build machine |
| 19:48 | `df124723` (merge) | Merge traffic T10: live aircraft from adsb.lol as an opt-in, server fetch with budget and back-off, no identities, extrapolation, attribution; aircraft light dots bright (18J; 6.98) |
| 21:16 | `86d14255` | Fly fixes: the host's road traffic ends with the last human rider, start.sh passes OCW_ADSB_LOL_KEY / OCW_LIVE_AIR_OFFLINE, the aircraft credit above the elevation profile, the browser follows the server's ride kind (18F Q2, 11.5, 18J; 6.99) |
| 22:21 | `92b118c6` | Browser: the app's module downloads with progress and tries a broken download again – "Downloading the app: 6.2 / 14.8 MB", "The download broke off – trying again (2/3)", then Start failed with Try again; never a partial copy (10G; 6.99) |
| 22:21 | `77eaf670` (merge) | Merge the deploy fixes: road traffic resets when the last human leaves, start.sh passes the adsb.lol key, the aircraft credit above the profile, the browser follows the server's ride, the app download retried with progress (6.99) |

## Builds and build servers

358 build/test runs on the build machines, 75.8 h in total, 17 failed; 1439 server samples; cargo compiled 49480 crates in 14.9 h, 20.2 h waiting for build slots.

| Machine | Runs | Hours | Cargo h | Crates | Waited h | Failed | Online |
|---|---|---|---|---|---|---|---|
| Weela | 0 | 0.0 | 0.0 | 0 | 0.0 | 0 | 0% |
| Win11Builder | 2 | 0.5 | 0.0 | 296 | 0.0 | 1 | 100% |
| leela | 72 | 28.9 | 7.6 | 28511 | 12.4 | 4 | 100% |
| macos | 26 | 1.1 | 0.1 | 84 | 0.0 | 1 | 99% |
| marge | 258 | 45.4 | 7.3 | 20589 | 7.8 | 11 | 100% |

Failed runs:

- 03:05 marge: `cargo fmt --all && cargo check -p ocw-web --target wasm32-unknown-unknown --feat` (exit 129, log `build-log/030522-marge-2177263.log`)
- 06:50 marge: `cargo fmt --all -- --check; cargo clippy -p ocw-render -p ocw-ui -p ocw-client -` (exit 101, log `build-log/065027-marge-2583226.log`)
- 10:26 marge: `target/release/ocw-bot verdict --server-stats target/mp/stats.json --processes 2` (exit 1, log `build-log/102629-marge-2992536.log`)
- 11:49 macos: `OCW_SHA=f99daa2a OCW_FEATURES=ocw-desktop/voice scripts/build-macos-app.sh && OC` (exit 101, log `build-log/114948-macos-3160929.log`)
- 11:49 marge: `scripts/release-linux.sh && scripts/release-web.sh` (exit 101, log `build-log/114948-marge-3160885.log`)
- 11:49 Win11Builder: `cargo build --release -p ocw-desktop -p ocw-server -p world-builder -p ocw-studi` (exit 1, log `build-log/114949-Win11Builder-3160995.log`)
- 12:17 marge: `cargo fmt --all && cargo test -p ocw-client air_follow && cargo test -p ocw-rend` (exit 101, log `build-log/121700-marge-3219105.log`)
- 12:52 marge: `source ~/.cargo/env; cargo fmt --all -- --check && cargo test -p ocw-ui --lib ph` (exit 101, log `build-log/125213-marge-3266544.log`)
- 13:22 leela: `make check` (exit 2, log `build-log/132202-leela-3333934.log`)
- 15:38 leela: `make check && make test-web-build && make test-smoke && echo ALL-CHECKS-OK` (exit 2, log `build-log/153847-leela-3633298.log`)
- 19:24 leela: `make check && make test-web-build && make test-smoke && echo ALL-CHECKS-OK` (exit 2, log `build-log/192419-leela-4122880.log`)
- 20:34 marge: `OCW_APP=/var/tmp/ocw/ocw-desktop OCW_SIZE=1600x900 OCW_SHOT_TIMEOUT=400 .claude/` (exit 1, log `build-log/203411-marge-62821.log`)
- 20:47 marge: `python3 scripts/test-remote-web.py --together --url "https://newkit.github""".io` (exit 2, log `build-log/204744-marge-79977.log`)
- 21:00 marge: `sh -n deploy/fly/ocw-server/start.sh && scripts/test-fly-start.sh` (exit 1, log `build-log/210051-marge-122497.log`)
- 22:02 marge: `make test-web-log` (exit 2, log `build-log/220244-marge-216746.log`)
- 22:11 leela: `make test-web-build && make test-remote` (exit 2, log `build-log/221153-leela-254792.log`)
- 22:14 marge: `make web > /dev/null 2>&1 || { echo web build failed; make web 2>&1 | tail -30; ` (exit 1, log `build-log/221414-marge-257586.log`)

Longest runs:

- 109 min on marge: `df -h ~ | tail -1; free -g | sed -n 2p; make check > /tmp/latefix-check.log 2>&1`
- 101 min on leela: `make check > /tmp/ocw-antweb-check.log 2>&1; echo "check exit $?"; make test-web`
- 94 min on marge: `df -h ~ | tail -1; free -g | head -2; make check > /tmp/t1-check.log 2>&1; echo `
- 78 min on leela: `cargo test -p ocw-devices -p ocw-fit -p ocw-client -p ocw-core -p ocw-bridge -p `
- 77 min on leela: `make check && make test-web-build && make test-smoke && echo ALL-CHECKS-OK`

## Token usage

1.81 B tokens in 6,346 model messages (output 4.3 M, cache reads 1.78 B, cache writes 28.9 M, uncached input 13 k). Full breakdown: [tokens.json](tokens.json).

| Feature | Tokens | Output | Messages |
|---|---|---|---|
| Other | 945.2 M | 2.3 M | 3,235 |
| Build, release & infra | 200.8 M | 262 k | 594 |
| Multiplayer & server | 162.5 M | 289 k | 530 |
| Worlds & terrain | 137.1 M | 367 k | 536 |
| Riders & bikes | 103.5 M | 463 k | 400 |
| UI & menus | 77.8 M | 194 k | 450 |
| Audio & voice | 77.1 M | 163 k | 230 |
| Materials & look | 67.7 M | 127 k | 223 |
| Planning & spec | 41.2 M | 146 k | 148 |

| Task | Feature | Tokens | Output |
|---|---|---|---|
| agent: Traffic: buses on lines, parked cars | Other | 153.9 M | 236 k |
| agent: ANT+: power rest, speed/cadence, FIT info | Other | 143.9 M | 253 k |
| agent: Traffic T5: server, network, client | Multiplayer & server | 119.9 M | 191 k |
| coordination: an you disable all deployments on vercel, also the autodeployment when the repo … | Build, release & infra | 105.7 M | 73 k |
| agent: iPhone: real worlds crash while loading | Worlds & terrain | 79.1 M | 162 k |
| agent: Traffic T10: live aircraft | Other | 72.7 M | 168 k |
| agent: Traffic T7: render + sound road traffic | Audio & voice | 71.4 M | 160 k |
| agent: Traffic T9: UFOs and the unicorn | Other | 69.1 M | 167 k |
| agent: Landscape follow-ups: dry grass, evening haze | Other | 67.0 M | 157 k |
| agent: Traffic T8: simulated aircraft | Other | 66.0 M | 215 k |
| agent: Traffic T4: vehicles around riders | Riders & bikes | 53.6 M | 246 k |
| agent: Traffic T2: TRFC/AERO world data | Worlds & terrain | 49.1 M | 176 k |
| agent: iPhone: ride photographer crash | Other | 48.7 M | 107 k |
| agent: HUD: pounding pink HR heart | UI & menus | 47.9 M | 113 k |
| agent: iPhone (iOS 18 WebKit) crash: bisect + fix | Other | 45.6 M | 116 k |
| agent: Traffic T1: settings + protocol | Other | 43.4 M | 121 k |
| coordination: make the hear of the HR pounding in pink whe HR increases | Other | 42.2 M | 53 k |
| agent: Fix crash: ground detail on despawned chunk | Other | 39.2 M | 110 k |
| agent: ANT+ WebUSB in the browser | Planning & spec | 38.1 M | 140 k |
| agent: Fly server as default in all apps | Multiplayer & server | 36.3 M | 88 k |
| coordination: yes build the log option for the browser | Build, release & infra | 36.1 M | 20 k |
| agent: Fixes from the Fly deploy | Build, release & infra | 33.4 M | 92 k |
| agent: Traffic T3: pure traffic core | Other | 32.0 M | 170 k |
| agent: iPhone: shadows off on iOS WebGL 2 | Materials & look | 30.8 M | 95 k |
| agent: Traffic T6: vehicle models | Riders & bikes | 30.4 M | 157 k |
| agent: Day 16 video (2026-11-26) | Other | 30.1 M | 63 k |
| agent: ANT+ FE-C trainer control | Other | 29.2 M | 109 k |
| coordination: there is an error in the web app 1: page log: Open Cycling World – started 2026-… | Materials & look | 23.5 M | 14 k |
| agent: Aircraft flyby video with drone + unicorn | Other | 23.2 M | 84 k |
| agent: Traffic: fix junction queues | Other | 21.2 M | 104 k |
| agent: Release 0.2.7 with Andorra | Build, release & infra | 18.8 M | 51 k |
| agent: Status page: show riders' names | Riders & bikes | 15.8 M | 58 k |
| agent: Rollout 0.2.7 worlds: Fly, kiosks, live page | UI & menus | 14.4 M | 37 k |
| agent: Deploy main to Fly, kiosks, live page | UI & menus | 14.3 M | 40 k |
| coordination: yes | Other | 10.6 M | 16 k |
| agent: Roll out new worlds + Fly + live page | Worlds & terrain | 8.8 M | 29 k |
| agent: Deploy main 77eaf670 to Fly | Build, release & infra | 6.8 M | 26 k |
| coordination: Q15: yes, including voice | Audio & voice | 5.7 M | 3 k |
| coordination: when the landscape check, traffic implementarion and default server tasks are do… | Multiplayer & server | 4.3 M | 7 k |
| coordination: 11.5 Q1: yes, show riders name | Riders & bikes | 3.8 M | 2 k |

## Prompts

28 prompts (full text: [prompts.md](prompts.md)).

| Time | Prompt |
|---|---|
| 02:45 | 11.5 Q1: yes, show riders name |
| 02:46 | Q15: yes, including voice |
| 02:48 | here is the log of the crashing browser app:  Whats the RC?  page log: Open Cycling World – started 2026-11-27T01:47:36.337Z, now +   8.592  |
| 02:49 | Landscape follow-ups: yes, rust-brown dry grass, weaker evening haze. |
| 02:52 | yes |
| 05:14 | update the lpen question section |
| 05:15 | start implementing traffic |
| 05:17 | insert the url of the fly.io server as default for all apps for now |
| 05:45 | which are the running tasks? |
| 05:47 | when the landscape check, traffic implementarion and default server tasks are done and tested successfully, bump bersion and do a release. d |
| 06:34 | 1.  page log: Open Cycling World – started 2026-11-27T05:34:12.952Z, now +  21.179 s page build: ac614c0 (2026-11-27), channel preview app b |
| 06:35 | 2. Since this does not work i stop here, or do you want me to runt he other tests, too?  page log: Open Cycling World – started 2026-11-27T0 |
| 06:37 | 9. rides  page log: Open Cycling World – started 2026-11-27T05:36:48.210Z, now +   8.912 s page build: ac614c0 (2026-11-27), channel preview |
| 06:38 | 11. rides  page log: Open Cycling World – started 2026-11-27T05:37:29.656Z, now +   9.457 s page build: ac614c0 (2026-11-27), channel previe |
| 06:39 | 7. closed  page log: Open Cycling World – started 2026-11-27T05:39:07.315Z, now +   7.522 s page build: ac614c0 (2026-11-27), channel previe |
| 06:39 | 8. closed  page log: Open Cycling World – started 2026-11-27T05:39:48.826Z, now +   1.956 s page build: ac614c0 (2026-11-27), channel previe |
| 06:45 | status ant? |
| 06:46 | make the hear of the HR pounding  in pink whe HR increases |
| 12:05 | yes, start points 2 |
| 12:06 | planes are pretty small in the images i've seen. create a flyby with a drone and the unicorn |
| 12:07 | 1 rides, but crashed when clicked above left arrow  page log: Open Cycling World – started 2026-11-27T11:06:46.517Z, now +   5.076 s page bu |
| 12:07 | 2. crashes  page log: Open Cycling World – started 2026-11-27T11:07:31.534Z, now +   2.173 s page build: 41b590a (2026-11-27), channel previ |
| 12:08 | 3. crashes  page log: Open Cycling World – started 2026-11-27T11:08:03.521Z, now +   0.719 s page build: 41b590a (2026-11-27), channel previ |
| 12:17 | 4 crashes  page log: Open Cycling World – started 2026-11-27T11:17:12.196Z, now +   2.609 s page build: 41b590a (2026-11-27), channel previe |
| 12:18 | 5 crashes  page log: Open Cycling World – started 2026-11-27T11:17:44.881Z, now +   2.127 s page build: 41b590a (2026-11-27), channel previe |
| 12:19 | no, 1 wirh no aufo still crashes when tapped  page log: Open Cycling World – started 2026-11-27T11:18:51.617Z, now +   2.094 s page build: 4 |
| 12:25 | an you disable all deployments on vercel, also the autodeployment when the repo changes |
| 21:44 | there is an error in the web app 1:  page log: Open Cycling World – started 2026-11-27T20:43:15.386Z, now +  24.804 s page build: df12472 (2 |

## Features

32 spec versions added, 28 landed by a merge; 8 deploys, 1 releases.

| Spec | Feature | Landed | Check (marge) |
|---|---|---|---|
| 6.67 | The browser app keeps an on-page log a rider can open on a phone and send | 00:19 `7b842cdc` (merge) | – |
| 6.68 | Fixed, for every world | 00:19 `adb79825` (merge) | – |
| 6.69 | The Linux kiosks join the game server on Fly.io | 00:20 `a7193d0a` (merge) | ok at 00:20, 88 suites, 3785 passed, 0 failed (commit) |
| 6.70 | Decided: 5 Q1 – the Fly server's status page names the riders online now, still without I… | 02:45 `c28f31d9` | – |
| 6.71 | Decided: Phase 11 Q15 – the Windows VR kiosk is built with voice, so riders who join it c… | 02:46 `d6ed8601` | – |
| 6.73 | The Fly server's status page names the riders on the road now | 03:48 `56ae0840` | – |
| 6.74 | Switches in the address find what closes the browser app on a phone | 04:02 `3901ed89` (merge) | ok at 04:03, 88 suites, 3799 passed, 0 failed (commit) |
| 6.75 | New open question 11.3 Q2 | 06:02 `ac614c00` (merge) | ok at 09:29, 1 suites, 3 passed, 0 failed (commit) |
| 6.76 | Dormant and dry grass above the tree line is a darker russet in every world, and the far… | 06:02 `ac614c00` (merge) | ok at 09:29, 1 suites, 3 passed, 0 failed (commit) |
| 6.77 | Built: the world packages carry the traffic data | 06:35 `1e461443` (merge) | – |
| 6.78 | Road traffic core built | 07:16 `64526a06` (merge) | – |
| 6.79 | Traffic T1 built | 07:29 `b23d697b` (merge) | – |
| 6.80 | The traffic's models | 07:32 `8c9ebc25` (merge) | ok at 09:36 (commit) |
| 6.81 | The public server on Fly.io is the default server of every app, for now | 08:16 `f342f0df` (merge) | – |
| 6.82 | The heart rate in the HUD has a beating heart | 09:15 `fd625698` (merge) | – |
| 6.83 | The browser app rides without shadows on iPhones and iPads with WebGL 2 by default, and s… | 09:43 `f7ff92f9` (merge) | – |
| 6.84 | A world switch no longer crashes on a background build that finishes after its chunk is g… | 11:03 `ede18971` (merge) | ok at 09:44 (commit) |
| 6.85 | On the iPhone every shadow variant closes the page, the shadow-free default rides | 12:18 `f874a416` | – |
| 6.86 | Traffic T4 built | 12:43 `0d489e6c` (merge) | ok at 10:41 (commit) |
| 6.87 | Traffic T5 built | 12:43 `0d489e6c` (merge) | ok at 10:41 (commit) |
| 6.88 | Traffic T8 built | 12:43 `6ba1cb74` (merge) | ok at 15:24 (commit) |
| 6.89 | The browser app takes no ride photos on iPhones and iPads with WebGL 2 by default | 15:05 `0d9e5cbc` (merge) | – |
| 6.90 | ANT+ FE-C smart trainers are built for the desktop app, without hardware | 15:05 `224a80a8` (merge) | – |
| 6.91 | ANT+ in the browser over WebUSB is built, without hardware | 15:05 `d65b3534` (merge) | – |
| 6.92 | The permanent queue at Liechtenstein's two main-road junctions is fixed | 15:38 `d58861c7` (merge) | – |
| 6.93 | Close-up aircraft flybys | 15:38 `ada17a88` (merge) | – |
| 6.94 | Traffic T7 built | 16:27 `b56d226a` (merge) | ok at 19:12, 20 suites, 1574 passed, 0 failed (commit) |
| 6.95 | Built: ANT+ power meters that send only torque pages and their calibration, ANT+ speed /… | 17:11 `894edf69` (merge) | ok at 19:24 (commit) |
| 6.96 | Traffic T9 built | 18:38 `2922c197` (merge) | – |
| 6.97 | Buses run on their OSM lines and stop at every stop, parked cars stand along the kerbs an… | 19:24 `f4334a44` (merge) | – |
| 6.98 | Traffic T10 built | 19:48 `df124723` (merge) | ok at 23:00, 7 suites, 581 passed, 0 failed (commit) |
| 6.99 | Fixes from deploying main to the Fly server | 22:21 `77eaf670` (merge) | – |

Deploys:

- 01:11 marge: `a7193d0a` (ok)
- 01:11 leela: `a7193d0a` (ok)
- 06:05 marge: `ac614c00` (ok)
- 06:25 leela: `ac614c00` (ok)
- 12:47 marge: `15426a24` (ok)
- 12:47 leela: `15426a24` (ok)
- 20:25 marge: `df124723` (ok)
- 20:33 leela: `df124723` (ok)

Releases:

- 12:35 v0.2.7 (pre-release)

## Agent jobs

37 jobs (coordinator log agents.jsonl).

| Task | Branch | Start | End | Status | Interrupted | Merged |
|---|---|---|---|---|---|---|
| Day 16 video (2026-11-26) | ababc78b | 00:11 | 00:44 | reported |  |  |
| Kiosks join the Fly server (remote mode) | a5e80efc | 00:11 | 01:05 | merged |  |  |
| Fly server: a public status and statistics page | a17e3f1a | 00:19 | 00:19 | merged |  |  |
| ANT+: Garmin's driver on Windows, the udev helper on Linux (Phase 17 Q7 d, Q8 b) | a4ff3c8a | 00:19 | 00:19 | merged |  |  |
| Browser app: an on-page log for phones (?log=1) | abd1e924 | 01:05 | 01:05 | merged |  |  |
| Landscape: smooth lakes and rivers, far terrain, high slopes, tall objects (all worlds) | a0d2648e | 01:05 | 01:05 | merged |  |  |
| Rollout: new worlds on marge/leela, Fly and the live page | a6340195 | 01:06 | 01:50 | reported |  |  |
| Status page: the names of riders online (11.5 Q1 b) | add68355 | 02:46 | 03:51 | merged |  |  |
| Landscape follow-ups: rust-brown dry grass, weaker evening haze | a44fa409 | 02:50 | 06:04 | merged |  |  |
| iPhone (iOS 18 WebKit) crash: bisect switches, early log, fixes | a04fbda1 | 02:52 | 05:05 | merged |  |  |
| Traffic T1: settings and protocol | aa001639 | 05:16 | 08:16 | merged |  |  |
| Traffic T2: world data TRFC / AERO | a71ca960 | 05:16 | 08:15 | merged |  |  |
| Traffic T3: the traffic core (ocw-sim::traffic) | adaba21b | 05:16 | 08:16 | merged |  |  |
| Traffic T6: vehicle and aircraft models | adc38938 | 05:16 | 08:16 | merged |  |  |
| The Fly server as the default server in all apps | a6c9978c | 05:17 | 09:15 | merged |  |  |
| iPhone: shadows off on iOS WebKit with WebGL 2, shadow-map switches | ad78328f | 06:37 | 11:03 | merged |  |  |
| HUD: the heart-rate heart beats, pink and pounding while HR rises | a7dfbacf | 06:46 | 11:02 | merged |  |  |
| Fix: late ground-detail meshes on despawned chunks after a world switch | a83ded9f | 07:34 | 11:47 | merged |  |  |
| Traffic T4: vehicles around riders (overtaking, manners, lunatic, collisions, gusts) | a4381619 | 08:17 | 13:45 | merged |  |  |
| Traffic T5: road traffic in the server, network and client | a8c371fe | 08:17 | 13:46 | merged |  |  |
| Traffic T8: simulated aircraft | a74c4eb5 | 08:17 | 13:46 | merged |  |  |
| Release 0.2.7 with Andorra | a2afc89e | 11:48 | 12:39 | reported |  |  |
| ANT+: torque power meters, calibration, speed/cadence sensors, FIT device_info | a9ea3efb | 12:06 | 17:23 | merged |  |  |
| ANT+: FE-C trainer control | a33440e4 | 12:06 | 16:26 | merged |  |  |
| ANT+: WebUSB stick in the browser | a55ba273 | 12:06 | 16:26 | merged |  |  |
| Aircraft flyby video: drone camera and the unicorn alongside an airliner | a1afa9e7 | 12:06 | 16:27 | merged |  |  |
| iPhone: the ride photographer closes the page (photos off on iOS WebGL 2, test switches) | a5b38082 | 12:19 | 16:26 | merged |  |  |
| Rollout of the 0.2.7 worlds: marge/leela, Fly, live page | adc9703b | 12:40 | 13:57 | merged |  |  |
| Traffic T7: rendering and sound of road traffic | a09570e8 | 13:47 | 17:13 | merged |  |  |
| Traffic: junction queues on the Liechtenstein main road | a2d44626 | 13:47 | 16:27 | merged |  |  |
| Traffic T9: UFOs and the unicorn | a0f4835a | 17:14 | 19:23 | merged |  |  |
| Traffic: buses on their lines, parked cars | a5515092 | 17:14 | 20:22 | merged |  |  |
| Traffic T10: live aircraft (adsb.lol) | a85482d4 | 18:15 | 20:22 | merged |  |  |
| Deploy main (traffic, aircraft, UFOs, live air, ANT+) to Fly, marge/leela, live page | a628fdb6 | 20:23 | 20:54 | merged |  |  |
| Fixes from the Fly deploy: traffic resets when empty, start.sh env, credit overlap, browse | ab5a47bc | 20:54 | 23:11 | merged |  |  |
| iPhone: real worlds close the page while loading (base sections, TRFC, memory per stage) | a25ad283 | 22:03 |  | started |  |  |
| Deploy main 77eaf670 to Fly (traffic reset, start.sh env) | a823e49f | 23:11 | 23:34 | merged |  |  |

## Incidents

87 collected (disk-full 1, janitor-delete 68, machine-offline 5, machine-online 4, runs-failed 1, unit-failed 8), 0 with root-cause notes ([incidents.md](incidents.md)).

| Time | Kind | Machine | What |
|---|---|---|---|
| 00:00 | machine-offline | Weela | Weela unreachable (no route to host) |
| 00:00 | disk-full | Win11Builder | disk C: on Win11Builder at 98 % |
| 00:19 | janitor-delete | marge | janitor delete OCW-worktree-agent-a4ff3c8abd356f67f/target (44.1 GB) |
| 00:19 | janitor-delete | marge | janitor delete OCW-merge-pair/target (35.1 GB) |
| 01:05 | janitor-delete | marge | janitor delete OCW-feature-web-page-log/target (4.8 GB) |
| 01:05 | janitor-delete | leela | janitor delete OCW-feature-web-page-log/target (35.0 GB) |
| 01:05 | janitor-delete | marge | janitor delete OCW-worktree-agent-a5e80efcdf1cc0fcd/target (30.1 GB) |
| 01:05 | janitor-delete | marge | janitor delete OCW-merge-trio2/target (40.7 GB) |
| 01:30 | janitor-delete | Win11Builder | janitor delete OCW-worktree-agent-a4ff3c8abd356f67f/target (20.1 GB) |
| 03:51 | janitor-delete | marge | janitor delete OCW-worktree-agent-add68355f3c7c137b/target (37.7 GB) |
| 05:05 | janitor-delete | marge | janitor delete OCW-worktree-agent-a04fbda1b56757da6/target (20.6 GB) |
| 05:05 | janitor-delete | leela | janitor delete OCW-worktree-agent-a04fbda1b56757da6/target (37.1 GB) |
| 05:05 | janitor-delete | marge | janitor delete OCW-merge-iphone/target (42.0 GB) |
| 06:04 | janitor-delete | marge | janitor delete OCW-worktree-agent-a44fa4098d6540f7b/target (47.6 GB) |
| 06:04 | janitor-delete | leela | janitor delete OCW-worktree-agent-a44fa4098d6540f7b/target (7.7 GB) |
| 06:04 | janitor-delete | marge | janitor delete OCW-merge-land/target (42.0 GB) |
| 08:15 | janitor-delete | marge | janitor delete OCW-worktree-agent-a71ca960ff9e89875/target (3.5 GB) |
| 08:16 | janitor-delete | leela | janitor delete OCW-worktree-agent-a71ca960ff9e89875/target (37.3 GB) |
| 08:16 | janitor-delete | marge | janitor delete OCW-worktree-agent-adaba21b1ef39507a/target (33.4 GB) |
| 08:16 | janitor-delete | marge | janitor delete OCW-worktree-agent-aa001639530a21eb0/target (49.6 GB) |
| 08:16 | janitor-delete | marge | janitor delete OCW-worktree-agent-adc38938cfd9ffe37/target (38.8 GB) |
| 08:16 | janitor-delete | leela | janitor delete OCW-worktree-agent-adc38938cfd9ffe37/target (0.5 GB) |
| 08:16 | janitor-delete | leela | janitor delete OCW-merge-t2/target (42.3 GB) |
| 08:21 | janitor-delete | macos | janitor delete OCW-worktree-agent-adaba21b1ef39507a/target (0.4 GB) |
| 08:21 | janitor-delete | macos | janitor delete OCW-worktree-agent-adc38938cfd9ffe37/target (0.9 GB) |
| 09:12 | machine-offline | macos | macos unreachable (timeout) |
| 09:15 | janitor-delete | leela | janitor delete OCW-merge-pub/target (37.7 GB) |
| 09:27 | machine-online | macos | macos back online |
| 10:43 | janitor-delete | marge | janitor delete OCW-worktree-agent-a0d2648e3477afb9f/target (51.3 GB) |
| 10:43 | janitor-delete | marge | janitor delete OCW-worktree-agent-a17e3f1a7b680b441/target (3.9 GB) |
| 10:43 | janitor-delete | marge | janitor delete OCW-worktree-agent-a6c9978cf1e4f6ba9/target (37.6 GB) |
| 10:43 | janitor-delete | marge | janitor delete OCW/target (2.2 GB) |
| 11:03 | janitor-delete | marge | janitor delete OCW-worktree-agent-a7dfbacf196603f86/target (47.7 GB) |
| 11:03 | janitor-delete | leela | janitor delete OCW-worktree-agent-a7dfbacf196603f86/target (20.4 GB) |
| 11:03 | janitor-delete | marge | janitor delete OCW-worktree-agent-ad78328f42bb43590/target (56.5 GB) |
| 11:03 | janitor-delete | leela | janitor delete OCW-worktree-agent-ad78328f42bb43590/target (4.8 GB) |
| 11:03 | janitor-delete | leela | janitor delete OCW-merge-rel/target (39.5 GB) |
| 11:47 | janitor-delete | marge | janitor delete OCW-worktree-agent-a83ded9fc90e9e68c/target (47.1 GB) |
| 11:47 | janitor-delete | leela | janitor delete OCW-worktree-agent-a83ded9fc90e9e68c/target (4.8 GB) |
| 11:48 | janitor-delete | leela | janitor delete OCW-merge-fix/target (37.8 GB) |
| 11:54 | janitor-delete | macos | janitor delete OCW-worktree-agent-a83ded9fc90e9e68c/target (3.8 GB) |
| 13:46 | janitor-delete | marge | janitor delete OCW-worktree-agent-a4381619ca70aa029/target (34.6 GB) |
| 13:46 | janitor-delete | marge | janitor delete OCW-worktree-agent-a8c371fe3b825be88/target (52.8 GB) |
| 13:46 | janitor-delete | leela | janitor delete OCW-worktree-agent-a8c371fe3b825be88/target (38.0 GB) |
| 13:46 | janitor-delete | leela | janitor delete OCW-merge-traf2/target (38.4 GB) |
| 13:54 | janitor-delete | macos | janitor delete OCW-worktree-agent-a74c4eb55332fe563/target (0.4 GB) |
| 13:54 | janitor-delete | macos | janitor delete OCW-worktree-agent-a8c371fe3b825be88/target (3.6 GB) |
| 15:04 | unit-failed | deb | ocw-art-collect.service failed (exit-code) |
| 16:04 | unit-failed | deb | ocw-art-collect.service failed (exit-code) |
| 16:26 | janitor-delete | marge | janitor delete OCW-worktree-agent-a5b38082302de2735/target (51.6 GB) |
| 16:26 | janitor-delete | marge | janitor delete OCW-worktree-agent-a33440e4325704bbb/target (7.1 GB) |
| 16:26 | janitor-delete | leela | janitor delete OCW-worktree-agent-a33440e4325704bbb/target (46.0 GB) |
| 16:27 | janitor-delete | marge | janitor delete OCW-worktree-agent-a55ba27310844f480/target (17.6 GB) |
| 16:27 | janitor-delete | leela | janitor delete OCW-worktree-agent-a55ba27310844f480/target (37.9 GB) |
| 16:27 | janitor-delete | marge | janitor delete OCW-worktree-agent-a2d44626d33ace963/target (35.1 GB) |
| 16:27 | janitor-delete | marge | janitor delete OCW-worktree-agent-a1afa9e7262945472/target (27.1 GB) |
| 16:27 | janitor-delete | leela | janitor delete OCW-worktree-agent-a1afa9e7262945472/target (33.6 GB) |
| 16:27 | janitor-delete | leela | janitor delete OCW-merge-photo/target (41.7 GB) |
| 16:38 | machine-offline | Win11Builder | Win11Builder unreachable (ssh error) |
| 16:40 | machine-online | Win11Builder | Win11Builder back online |

## Media

| Time | File |
|---|---|
| 01:46:29 | [014629-rollout-water-remote-web-end.jpg](014629-rollout-water-remote-web-end.jpg) |
| 01:46:29 | [014629-rollout-water-remote-web-joined.jpg](014629-rollout-water-remote-web-joined.jpg) |
| 01:46:29 | [014629-rollout-water-remote-web-riding.jpg](014629-rollout-water-remote-web-riding.jpg) |
| 02:56:33 | [025633-statuspage-names-statuspage-names-desktop-dark.png](025633-statuspage-names-statuspage-names-desktop-dark.png) |
| 02:56:33 | [025633-statuspage-names-statuspage-names-desktop.png](025633-statuspage-names-statuspage-names-desktop.png) |
| 02:56:33 | [025633-statuspage-names-statuspage-names-phone.png](025633-statuspage-names-statuspage-names-phone.png) |
| 03:04:25 | [030425-scenes-landscape-before-readme-sunset.jpg](030425-scenes-landscape-before-readme-sunset.jpg) |
| 03:04:57 | [030457-scenes-landscape-before-readme-rain.jpg](030457-scenes-landscape-before-readme-rain.jpg) |
| 03:05:14 | [030514-scenes-landscape-before-readme-andorra-envalira.jpg](030514-scenes-landscape-before-readme-andorra-envalira.jpg) |
| 03:05:31 | [030531-scenes-landscape-before-readme-andorra-dawn.jpg](030531-scenes-landscape-before-readme-andorra-dawn.jpg) |
| 03:05:43 | [030543-scenes-landscape-before-sky-sunrise.jpg](030543-scenes-landscape-before-sky-sunrise.jpg) |
| 03:06:06 | [030606-scenes-landscape-before-wg-hornisgrinde-far.jpg](030606-scenes-landscape-before-wg-hornisgrinde-far.jpg) |
| 03:06:18 | [030618-scenes-landscape-before-wg-envalira-pass.jpg](030618-scenes-landscape-before-wg-envalira-pass.jpg) |
| 03:06:40 | [030640-scenes-landscape-before-wg-teide-high.jpg](030640-scenes-landscape-before-wg-teide-high.jpg) |
| 03:07:03 | [030703-scenes-landscape-before-wg-hornisgrinde-far-noon.jpg](030703-scenes-landscape-before-wg-hornisgrinde-far-noon.jpg) |
| 03:07:26 | [030726-scenes-landscape-before-unicorn-hornisgrinde-sunset.jpg](030726-scenes-landscape-before-unicorn-hornisgrinde-sunset.jpg) |
| 03:07:49 | [030749-scenes-landscape-before-lh-hornisgrinde-sunset-simple.jpg](030749-scenes-landscape-before-lh-hornisgrinde-sunset-simple.jpg) |
| 03:08:12 | [030812-scenes-landscape-before-lh-hornisgrinde-sunset-medium.jpg](030812-scenes-landscape-before-lh-hornisgrinde-sunset-medium.jpg) |
| 03:08:35 | [030835-scenes-landscape-before-lh-hornisgrinde-morning.jpg](030835-scenes-landscape-before-lh-hornisgrinde-morning.jpg) |
| 03:08:47 | [030847-scenes-landscape-before-lh-envalira-pass-july.jpg](030847-scenes-landscape-before-lh-envalira-pass-july.jpg) |
| 03:09:10 | [030910-scenes-landscape-before-lh-teide-high-august.jpg](030910-scenes-landscape-before-lh-teide-high-august.jpg) |
| 03:09:24 | [030924-scenes-landscape-before-lh-malbun-alps.jpg](030924-scenes-landscape-before-lh-malbun-alps.jpg) |
| 03:09:52 | [030952-scenes-landscape-before-lh-feldberg-october.jpg](030952-scenes-landscape-before-lh-feldberg-october.jpg) |
| 03:40:09 | [034009-smoke-c28f31d9-dirty-shot-ocw.jpg](034009-smoke-c28f31d9-dirty-shot-ocw.jpg) |
| 03:40:19 | [034019-smoke-c28f31d9-dirty-shot-wayland-ocw-wayland.jpg](034019-smoke-c28f31d9-dirty-shot-wayland-ocw-wayland.jpg) |
| 03:40:38 | [034038-web-bisect-web-bisect-android-base.png](034038-web-bisect-web-bisect-android-base.png) |
| 03:40:38 | [034038-web-bisect-web-bisect-android-ios-safe.png](034038-web-bisect-web-bisect-android-ios-safe.png) |
| 03:40:38 | [034038-web-bisect-web-bisect-android-noegui.png](034038-web-bisect-web-bisect-android-noegui.png) |
| 03:40:38 | [034038-web-bisect-web-bisect-android-nosee.png](034038-web-bisect-web-bisect-android-nosee.png) |
| 03:40:38 | [034038-web-bisect-web-bisect-android-pipelines-serial.png](034038-web-bisect-web-bisect-android-pipelines-serial.png) |
| 03:40:38 | [034038-web-bisect-web-bisect-iphone-base.png](034038-web-bisect-web-bisect-iphone-base.png) |
| 03:40:38 | [034038-web-bisect-web-bisect-iphone-frames-0.png](034038-web-bisect-web-bisect-iphone-frames-0.png) |
| 03:40:38 | [034038-web-bisect-web-bisect-iphone-frames-30.png](034038-web-bisect-web-bisect-iphone-frames-30.png) |
| 03:40:38 | [034038-web-bisect-web-bisect-iphone-ios-safe.png](034038-web-bisect-web-bisect-iphone-ios-safe.png) |
| 03:40:38 | [034038-web-bisect-web-bisect-iphone-killed.png](034038-web-bisect-web-bisect-iphone-killed.png) |
| 03:40:38 | [034038-web-bisect-web-bisect-iphone-noarrays.png](034038-web-bisect-web-bisect-iphone-noarrays.png) |
| 03:40:38 | [034038-web-bisect-web-bisect-iphone-noaudio.png](034038-web-bisect-web-bisect-iphone-noaudio.png) |
| 03:40:38 | [034038-web-bisect-web-bisect-iphone-noegui.png](034038-web-bisect-web-bisect-iphone-noegui.png) |
| 03:40:38 | [034038-web-bisect-web-bisect-iphone-nomsaa.png](034038-web-bisect-web-bisect-iphone-nomsaa.png) |
| 03:40:38 | [034038-web-bisect-web-bisect-iphone-nosee.png](034038-web-bisect-web-bisect-iphone-nosee.png) |
| 03:40:38 | [034038-web-bisect-web-bisect-iphone-noshadow.png](034038-web-bisect-web-bisect-iphone-noshadow.png) |
| 03:40:38 | [034038-web-bisect-web-bisect-iphone-nosky.png](034038-web-bisect-web-bisect-iphone-nosky.png) |
| 03:40:38 | [034038-web-bisect-web-bisect-iphone-novoice.png](034038-web-bisect-web-bisect-iphone-novoice.png) |
| 03:40:38 | [034038-web-bisect-web-bisect-iphone-pipelines-serial.png](034038-web-bisect-web-bisect-iphone-pipelines-serial.png) |
| 03:40:38 | [034038-web-bisect-web-bisect-iphone-plain.png](034038-web-bisect-web-bisect-iphone-plain.png) |
| 03:43:53 | [034353-statuspage-live-join-remote-web-end.jpg](034353-statuspage-live-join-remote-web-end.jpg) |
| 03:43:53 | [034353-statuspage-live-join-remote-web-joined.jpg](034353-statuspage-live-join-remote-web-joined.jpg) |
| 03:43:53 | [034353-statuspage-live-join-remote-web-riding.jpg](034353-statuspage-live-join-remote-web-riding.jpg) |
| 03:44:46 | [034446-statuspage-names-statuspage-live-phone.png](034446-statuspage-names-statuspage-live-phone.png) |
| 03:45:12 | [034512-statuspage-names-statuspage-live-desktop.png](034512-statuspage-names-statuspage-live-desktop.png) |
| 03:51:02 | [035102-web-bisect-web-bisect-iphone-base-early-log.png](035102-web-bisect-web-bisect-iphone-base-early-log.png) |
| 03:51:02 | [035102-web-bisect-web-bisect-iphone-base.png](035102-web-bisect-web-bisect-iphone-base.png) |
| 03:51:02 | [035102-web-bisect-web-bisect-iphone-frames-0-early-log.png](035102-web-bisect-web-bisect-iphone-frames-0-early-log.png) |
| 03:51:02 | [035102-web-bisect-web-bisect-iphone-frames-0.png](035102-web-bisect-web-bisect-iphone-frames-0.png) |
| 03:51:02 | [035102-web-bisect-web-bisect-iphone-ios-safe-early-log.png](035102-web-bisect-web-bisect-iphone-ios-safe-early-log.png) |
| 03:51:02 | [035102-web-bisect-web-bisect-iphone-ios-safe.png](035102-web-bisect-web-bisect-iphone-ios-safe.png) |
| 03:51:02 | [035102-web-bisect-web-bisect-iphone-killed-early-log.png](035102-web-bisect-web-bisect-iphone-killed-early-log.png) |
| 03:51:02 | [035102-web-bisect-web-bisect-iphone-killed.png](035102-web-bisect-web-bisect-iphone-killed.png) |
| 03:51:02 | [035102-web-bisect-web-bisect-iphone-nosee-early-log.png](035102-web-bisect-web-bisect-iphone-nosee-early-log.png) |
| 03:51:02 | [035102-web-bisect-web-bisect-iphone-nosee.png](035102-web-bisect-web-bisect-iphone-nosee.png) |
| 03:51:02 | [035102-web-bisect-web-bisect-iphone-pipelines-serial-early-log.png](035102-web-bisect-web-bisect-iphone-pipelines-serial-early-log.png) |
| 03:51:02 | [035102-web-bisect-web-bisect-iphone-pipelines-serial.png](035102-web-bisect-web-bisect-iphone-pipelines-serial.png) |
| 03:52:53 | [035253-web-bisect-web-bisect-android-base-early-log.png](035253-web-bisect-web-bisect-android-base-early-log.png) |
| 03:52:53 | [035253-web-bisect-web-bisect-android-base.png](035253-web-bisect-web-bisect-android-base.png) |
| 03:52:53 | [035253-web-bisect-web-bisect-android-ios-safe-early-log.png](035253-web-bisect-web-bisect-android-ios-safe-early-log.png) |
| 03:52:53 | [035253-web-bisect-web-bisect-android-ios-safe.png](035253-web-bisect-web-bisect-android-ios-safe.png) |
| 04:01:30 | [040130-a5baf1d4-dirty-shot-ocw.jpg](040130-a5baf1d4-dirty-shot-ocw.jpg) |
| 04:01:41 | [040141-a5baf1d4-dirty-shot-wayland-ocw-wayland.jpg](040141-a5baf1d4-dirty-shot-wayland-ocw-wayland.jpg) |
| 04:36:23 | [043623-scenes-landscape-after-readme-sunset.jpg](043623-scenes-landscape-after-readme-sunset.jpg) |
| 04:36:54 | [043654-scenes-landscape-after-readme-rain.jpg](043654-scenes-landscape-after-readme-rain.jpg) |
| 04:37:11 | [043711-scenes-landscape-after-readme-andorra-envalira.jpg](043711-scenes-landscape-after-readme-andorra-envalira.jpg) |
| 04:37:28 | [043728-scenes-landscape-after-readme-andorra-dawn.jpg](043728-scenes-landscape-after-readme-andorra-dawn.jpg) |
| 04:37:40 | [043740-scenes-landscape-after-sky-sunrise.jpg](043740-scenes-landscape-after-sky-sunrise.jpg) |
| 04:38:02 | [043802-scenes-landscape-after-wg-hornisgrinde-far.jpg](043802-scenes-landscape-after-wg-hornisgrinde-far.jpg) |
| 04:38:14 | [043814-scenes-landscape-after-wg-envalira-pass.jpg](043814-scenes-landscape-after-wg-envalira-pass.jpg) |
| 04:38:37 | [043837-scenes-landscape-after-wg-teide-high.jpg](043837-scenes-landscape-after-wg-teide-high.jpg) |
| 04:38:59 | [043859-scenes-landscape-after-wg-hornisgrinde-far-noon.jpg](043859-scenes-landscape-after-wg-hornisgrinde-far-noon.jpg) |
| 04:39:22 | [043922-scenes-landscape-after-unicorn-hornisgrinde-sunset.jpg](043922-scenes-landscape-after-unicorn-hornisgrinde-sunset.jpg) |
| 04:39:45 | [043945-scenes-landscape-after-lh-hornisgrinde-sunset-simple.jpg](043945-scenes-landscape-after-lh-hornisgrinde-sunset-simple.jpg) |
| 04:40:08 | [044008-scenes-landscape-after-lh-hornisgrinde-sunset-medium.jpg](044008-scenes-landscape-after-lh-hornisgrinde-sunset-medium.jpg) |
| 04:40:31 | [044031-scenes-landscape-after-lh-hornisgrinde-morning.jpg](044031-scenes-landscape-after-lh-hornisgrinde-morning.jpg) |
| 04:40:43 | [044043-scenes-landscape-after-lh-envalira-pass-july.jpg](044043-scenes-landscape-after-lh-envalira-pass-july.jpg) |
| 04:41:06 | [044106-scenes-landscape-after-lh-teide-high-august.jpg](044106-scenes-landscape-after-lh-teide-high-august.jpg) |
| 04:41:20 | [044120-scenes-landscape-after-lh-malbun-alps.jpg](044120-scenes-landscape-after-lh-malbun-alps.jpg) |
| 04:41:48 | [044148-scenes-landscape-after-lh-feldberg-october.jpg](044148-scenes-landscape-after-lh-feldberg-october.jpg) |
| 04:44:08 | [044408-scenes-landscape-compare-lh-envalira-pass-july.jpg](044408-scenes-landscape-compare-lh-envalira-pass-july.jpg) |
| 04:44:08 | [044408-scenes-landscape-compare-lh-feldberg-october.jpg](044408-scenes-landscape-compare-lh-feldberg-october.jpg) |
| 04:44:08 | [044408-scenes-landscape-compare-lh-hornisgrinde-morning.jpg](044408-scenes-landscape-compare-lh-hornisgrinde-morning.jpg) |
| 04:44:09 | [044409-scenes-landscape-compare-lh-hornisgrinde-sunset-medium.jpg](044409-scenes-landscape-compare-lh-hornisgrinde-sunset-medium.jpg) |
| 04:44:09 | [044409-scenes-landscape-compare-lh-hornisgrinde-sunset-simple.jpg](044409-scenes-landscape-compare-lh-hornisgrinde-sunset-simple.jpg) |
| 04:44:09 | [044409-scenes-landscape-compare-lh-malbun-alps.jpg](044409-scenes-landscape-compare-lh-malbun-alps.jpg) |
| 04:44:09 | [044409-scenes-landscape-compare-lh-teide-high-august.jpg](044409-scenes-landscape-compare-lh-teide-high-august.jpg) |
| 04:44:09 | [044409-scenes-landscape-compare-readme-andorra-dawn.jpg](044409-scenes-landscape-compare-readme-andorra-dawn.jpg) |
| 04:44:09 | [044409-scenes-landscape-compare-readme-andorra-envalira.jpg](044409-scenes-landscape-compare-readme-andorra-envalira.jpg) |
| 04:44:09 | [044409-scenes-landscape-compare-readme-rain.jpg](044409-scenes-landscape-compare-readme-rain.jpg) |
| 04:44:10 | [044410-scenes-landscape-compare-readme-sunset.jpg](044410-scenes-landscape-compare-readme-sunset.jpg) |
| 04:44:10 | [044410-scenes-landscape-compare-sky-sunrise.jpg](044410-scenes-landscape-compare-sky-sunrise.jpg) |
| 04:44:10 | [044410-scenes-landscape-compare-unicorn-hornisgrinde-sunset.jpg](044410-scenes-landscape-compare-unicorn-hornisgrinde-sunset.jpg) |
| 04:44:10 | [044410-scenes-landscape-compare-wg-envalira-pass.jpg](044410-scenes-landscape-compare-wg-envalira-pass.jpg) |
| 04:44:10 | [044410-scenes-landscape-compare-wg-hornisgrinde-far-noon.jpg](044410-scenes-landscape-compare-wg-hornisgrinde-far-noon.jpg) |
| 04:44:10 | [044410-scenes-landscape-compare-wg-hornisgrinde-far.jpg](044410-scenes-landscape-compare-wg-hornisgrinde-far.jpg) |
| 04:44:10 | [044410-scenes-landscape-compare-wg-teide-high.jpg](044410-scenes-landscape-compare-wg-teide-high.jpg) |
| 04:58:12 | [045812-837f67f6-dirty-shot-ocw.jpg](045812-837f67f6-dirty-shot-ocw.jpg) |
| 04:58:22 | [045822-837f67f6-dirty-shot-wayland-ocw-wayland.jpg](045822-837f67f6-dirty-shot-wayland-ocw-wayland.jpg) |
| 05:55:42 | [055542-vehicles-t6-airliner-twinjet-day-wayland.jpg](055542-vehicles-t6-airliner-twinjet-day-wayland.jpg) |
| 05:55:53 | [055553-vehicles-t6-balloon-hot-air-day-wayland.jpg](055553-vehicles-t6-balloon-hot-air-day-wayland.jpg) |
| 05:56:05 | [055605-vehicles-t6-bus-city-day-wayland.jpg](055605-vehicles-t6-bus-city-day-wayland.jpg) |
| 05:56:16 | [055616-vehicles-t6-car-hatchback-day-wayland.jpg](055616-vehicles-t6-car-hatchback-day-wayland.jpg) |
| 05:56:28 | [055628-vehicles-t6-car-saloon-day-wayland.jpg](055628-vehicles-t6-car-saloon-day-wayland.jpg) |
| 05:56:32 | [055632-2026-11-27-traffic-t3-liechtenstein-hour.png](055632-2026-11-27-traffic-t3-liechtenstein-hour.png) |
| 05:56:32 | [055632-2026-11-27-traffic-t3-ring-jam-wave.png](055632-2026-11-27-traffic-t3-ring-jam-wave.png) |
| 05:56:39 | [055639-vehicles-t6-car-suv-day-wayland.jpg](055639-vehicles-t6-car-suv-day-wayland.jpg) |
| 05:56:51 | [055651-vehicles-t6-glider-sailplane-day-wayland.jpg](055651-vehicles-t6-glider-sailplane-day-wayland.jpg) |
| 05:57:03 | [055703-vehicles-t6-helicopter-light-day-wayland.jpg](055703-vehicles-t6-helicopter-light-day-wayland.jpg) |
| 05:57:14 | [055714-vehicles-t6-lorry-articulated-box-day-wayland.jpg](055714-vehicles-t6-lorry-articulated-box-day-wayland.jpg) |
| 05:57:26 | [055726-vehicles-t6-lorry-rigid-box-day-wayland.jpg](055726-vehicles-t6-lorry-rigid-box-day-wayland.jpg) |
| 05:57:38 | [055738-vehicles-t6-motorbike-touring-day-wayland.jpg](055738-vehicles-t6-motorbike-touring-day-wayland.jpg) |
| 05:57:49 | [055749-vehicles-t6-plane-high-wing-day-wayland.jpg](055749-vehicles-t6-plane-high-wing-day-wayland.jpg) |
| 05:58:01 | [055801-vehicles-t6-tractor-farm-day-wayland.jpg](055801-vehicles-t6-tractor-farm-day-wayland.jpg) |
| 05:58:12 | [055812-vehicles-t6-ufo-saucer-day-wayland.jpg](055812-vehicles-t6-ufo-saucer-day-wayland.jpg) |
| 05:58:24 | [055824-vehicles-t6-van-panel-day-wayland.jpg](055824-vehicles-t6-van-panel-day-wayland.jpg) |
| 06:34:03 | [063403-2026-11-27-t2-smoke-leela-smoke-wayland.jpg](063403-2026-11-27-t2-smoke-leela-smoke-wayland.jpg) |
| 06:34:03 | [063403-2026-11-27-t2-smoke-leela-smoke-x11.jpg](063403-2026-11-27-t2-smoke-leela-smoke-x11.jpg) |
| 07:04:09 | [070409-t1-scenes-menu-audio-voice.jpg](070409-t1-scenes-menu-audio-voice.jpg) |
| 07:04:48 | [070448-t1-scenes-menu-traffic.jpg](070448-t1-scenes-menu-traffic.jpg) |
| 07:05:26 | [070526-t1-scenes-menu-traffic-more.jpg](070526-t1-scenes-menu-traffic-more.jpg) |
| 07:27:40 | [072740-t1-web-web-traffic-traffic-more.jpg](072740-t1-web-web-traffic-traffic-more.jpg) |
| 07:27:40 | [072740-t1-web-web-traffic-traffic.jpg](072740-t1-web-web-traffic-traffic.jpg) |
| 07:32:54 | [073254-desktop-join-public-fly-liechtenstein.jpg](073254-desktop-join-public-fly-liechtenstein.jpg) |
| 07:39:05 | [073905-heart-heart-normal.jpg](073905-heart-heart-normal.jpg) |
| 07:39:28 | [073928-heart-heart-pink.jpg](073928-heart-heart-pink.jpg) |
| 07:54:33 | [075433-latefix-before-1.jpg](075433-latefix-before-1.jpg) |
| 07:55:47 | [075547-latefix-before-2.jpg](075547-latefix-before-2.jpg) |
| 07:57:00 | [075700-latefix-before-3.jpg](075700-latefix-before-3.jpg) |
| 08:03:23 | [080323-heart-web-web-webgl2-normal-zoom.png](080323-heart-web-web-webgl2-normal-zoom.png) |
| 08:03:23 | [080323-heart-web-web-webgl2-normal.jpg](080323-heart-web-web-webgl2-normal.jpg) |
| 08:03:23 | [080323-heart-web-web-webgl2-pink-zoom.png](080323-heart-web-web-webgl2-pink-zoom.png) |
| 08:03:23 | [080323-heart-web-web-webgl2-pink.jpg](080323-heart-web-web-webgl2-pink.jpg) |
| 08:03:23 | [080323-heart-web-web-webgl2.jpg](080323-heart-web-web-webgl2.jpg) |
| 08:04:04 | [080404-heart-web-web-normal-zoom.png](080404-heart-web-web-normal-zoom.png) |
| 08:04:04 | [080404-heart-web-web-normal.jpg](080404-heart-web-web-normal.jpg) |
| 08:04:04 | [080404-heart-web-web-pink-zoom.png](080404-heart-web-web-pink-zoom.png) |
| 08:04:04 | [080404-heart-web-web-pink.jpg](080404-heart-web-web-pink.jpg) |
| 08:04:04 | [080404-heart-web-web.jpg](080404-heart-web-web.jpg) |
| 08:20:45 | [082045-c6b25317-shot-heart-normal.jpg](082045-c6b25317-shot-heart-normal.jpg) |
| 08:31:48 | [083148-c6b25317-shot-heart-pink.jpg](083148-c6b25317-shot-heart-pink.jpg) |
| 08:33:32 | [083332-2026-11-27-smoke-ac614c00-dirty-shot-ocw.jpg](083332-2026-11-27-smoke-ac614c00-dirty-shot-ocw.jpg) |
| 08:33:43 | [083343-2026-11-27-smoke-ac614c00-dirty-shot-wayland-ocw-wayland.jpg](083343-2026-11-27-smoke-ac614c00-dirty-shot-wayland-ocw-wayland.jpg) |
| 08:40:42 | [084042-c6b25317-video-heart-ride.jpg](084042-c6b25317-video-heart-ride.jpg) |
| 08:40:42 | [084042-c6b25317-video-heart-ride.mp4](084042-c6b25317-video-heart-ride.mp4) |
| 08:40:46 | [084046-heart-heart-normal-zoom.jpg](084046-heart-heart-normal-zoom.jpg) |
| 08:40:46 | [084046-heart-heart-pink-zoom.jpg](084046-heart-heart-pink-zoom.jpg) |
| 08:40:46 | [084046-heart-heart-ride-zoom.mp4](084046-heart-heart-ride-zoom.mp4) |
| 08:57:58 | [085758-c6b25317-shot-ocw.jpg](085758-c6b25317-shot-ocw.jpg) |
| 08:58:07 | [085807-c6b25317-shot-wayland-ocw-wayland.jpg](085807-c6b25317-shot-wayland-ocw-wayland.jpg) |
| 09:17:08 | [091708-2026-11-27-ios-shadows-web-webkit-iphone-hints.png](091708-2026-11-27-ios-shadows-web-webkit-iphone-hints.png) |
| 09:17:08 | [091708-2026-11-27-ios-shadows-web-webkit-iphone-hold.png](091708-2026-11-27-ios-shadows-web-webkit-iphone-hold.png) |
| 09:17:08 | [091708-2026-11-27-ios-shadows-web-webkit-iphone-landscape-hints.png](091708-2026-11-27-ios-shadows-web-webkit-iphone-landscape-hints.png) |
| 09:17:08 | [091708-2026-11-27-ios-shadows-web-webkit-iphone-landscape-hold.png](091708-2026-11-27-ios-shadows-web-webkit-iphone-landscape-hold.png) |
| 09:17:08 | [091708-2026-11-27-ios-shadows-web-webkit-iphone-landscape-riding.png](091708-2026-11-27-ios-shadows-web-webkit-iphone-landscape-riding.png) |
| 09:17:08 | [091708-2026-11-27-ios-shadows-web-webkit-iphone-landscape-stopped.png](091708-2026-11-27-ios-shadows-web-webkit-iphone-landscape-stopped.png) |
| 09:17:08 | [091708-2026-11-27-ios-shadows-web-webkit-iphone-landscape.png](091708-2026-11-27-ios-shadows-web-webkit-iphone-landscape.png) |
| 09:17:08 | [091708-2026-11-27-ios-shadows-web-webkit-iphone-riding.png](091708-2026-11-27-ios-shadows-web-webkit-iphone-riding.png) |
| 09:17:08 | [091708-2026-11-27-ios-shadows-web-webkit-iphone-start.png](091708-2026-11-27-ios-shadows-web-webkit-iphone-start.png) |
| 09:17:08 | [091708-2026-11-27-ios-shadows-web-webkit-iphone-stopped.png](091708-2026-11-27-ios-shadows-web-webkit-iphone-stopped.png) |
| 09:17:08 | [091708-2026-11-27-ios-shadows-web-webkit-iphone.png](091708-2026-11-27-ios-shadows-web-webkit-iphone.png) |
| 09:17:08 | [091708-2026-11-27-ios-shadows-web-webkit-layout-android-360x640.png](091708-2026-11-27-ios-shadows-web-webkit-layout-android-360x640.png) |
| 09:17:08 | [091708-2026-11-27-ios-shadows-web-webkit-layout-android-640x360.png](091708-2026-11-27-ios-shadows-web-webkit-layout-android-640x360.png) |
| 09:17:08 | [091708-2026-11-27-ios-shadows-web-webkit-layout-iphone-390x844.png](091708-2026-11-27-ios-shadows-web-webkit-layout-iphone-390x844.png) |
| 09:17:08 | [091708-2026-11-27-ios-shadows-web-webkit-layout-iphone-844x390.png](091708-2026-11-27-ios-shadows-web-webkit-layout-iphone-844x390.png) |
| 09:17:08 | [091708-2026-11-27-ios-shadows-web-webkit-mac.png](091708-2026-11-27-ios-shadows-web-webkit-mac.png) |
| 09:29:06 | [092906-scenes-traffic-boxes-video-1280.mp4](092906-scenes-traffic-boxes-video-1280.mp4) |
| 09:31:53 | [093153-scenes-t8-air-air-tfn-approach.jpg](093153-scenes-t8-air-air-tfn-approach.jpg) |
| 09:32:13 | [093213-scenes-t8-air-air-tfn-approach.mp4](093213-scenes-t8-air-air-tfn-approach.mp4) |
| 09:33:00 | [093300-scenes-t8-air-air-contrails-blackforest.jpg](093300-scenes-t8-air-air-contrails-blackforest.jpg) |
| 09:33:47 | [093347-scenes-t8-air-air-contrails-dry.jpg](093347-scenes-t8-air-air-contrails-dry.jpg) |
| 09:34:24 | [093424-scenes-t8-air-air-dusk-lights.jpg](093424-scenes-t8-air-air-dusk-lights.jpg) |
| 09:36:02 | [093602-2026-11-27-traffic-t4-t4plots-overtake-lunatic.png](093602-2026-11-27-traffic-t4-t4plots-overtake-lunatic.png) |
| 09:36:02 | [093602-2026-11-27-traffic-t4-t4plots-overtake-mostly-polite.png](093602-2026-11-27-traffic-t4-t4plots-overtake-mostly-polite.png) |
| 09:36:02 | [093602-2026-11-27-traffic-t4-t4plots-overtake-polite.png](093602-2026-11-27-traffic-t4-t4plots-overtake-polite.png) |
| 09:36:02 | [093602-2026-11-27-traffic-t4-t4plots-overtake-some-realism.png](093602-2026-11-27-traffic-t4-t4plots-overtake-some-realism.png) |
| 09:36:02 | [093602-2026-11-27-traffic-t4-t4plots-passes-lunatic.png](093602-2026-11-27-traffic-t4-t4plots-passes-lunatic.png) |
| 09:36:02 | [093602-2026-11-27-traffic-t4-t4plots-passes-mostly-polite.png](093602-2026-11-27-traffic-t4-t4plots-passes-mostly-polite.png) |
| 09:36:02 | [093602-2026-11-27-traffic-t4-t4plots-passes-polite.png](093602-2026-11-27-traffic-t4-t4plots-passes-polite.png) |
| 09:36:02 | [093602-2026-11-27-traffic-t4-t4plots-passes-some-realism.png](093602-2026-11-27-traffic-t4-t4plots-passes-some-realism.png) |
| 09:38:09 | [093809-8c9ebc25-dirty-shot-wayland-traffic-boxes-vaduz.jpg](093809-8c9ebc25-dirty-shot-wayland-traffic-boxes-vaduz.jpg) |
| 09:38:27 | [093827-8c9ebc25-dirty-shot-wayland-traffic-boxes-top.jpg](093827-8c9ebc25-dirty-shot-wayland-traffic-boxes-top.jpg) |
| 09:39:12 | [093912-8c9ebc25-dirty-video-wayland-traffic-boxes-video.jpg](093912-8c9ebc25-dirty-video-wayland-traffic-boxes-video.jpg) |
| 09:39:12 | [093912-8c9ebc25-dirty-video-wayland-traffic-boxes-video.mp4](093912-8c9ebc25-dirty-video-wayland-traffic-boxes-video.mp4) |
| 09:39:51 | [093951-2026-11-27-ios-shadows-web-bisect-android-base-early-log.png](093951-2026-11-27-ios-shadows-web-bisect-android-base-early-log.png) |
| 09:39:51 | [093951-2026-11-27-ios-shadows-web-bisect-android-base.png](093951-2026-11-27-ios-shadows-web-bisect-android-base.png) |
| 09:39:51 | [093951-2026-11-27-ios-shadows-web-bisect-android-ios-safe-early-log.png](093951-2026-11-27-ios-shadows-web-bisect-android-ios-safe-early-log.png) |
| 09:39:51 | [093951-2026-11-27-ios-shadows-web-bisect-android-ios-safe.png](093951-2026-11-27-ios-shadows-web-bisect-android-ios-safe.png) |
| 09:39:51 | [093951-2026-11-27-ios-shadows-web-bisect-android-noegui-early-log.png](093951-2026-11-27-ios-shadows-web-bisect-android-noegui-early-log.png) |
| 09:39:51 | [093951-2026-11-27-ios-shadows-web-bisect-android-noegui.png](093951-2026-11-27-ios-shadows-web-bisect-android-noegui.png) |
| 09:39:51 | [093951-2026-11-27-ios-shadows-web-bisect-android-nosee-early-log.png](093951-2026-11-27-ios-shadows-web-bisect-android-nosee-early-log.png) |
| 09:39:51 | [093951-2026-11-27-ios-shadows-web-bisect-android-nosee.png](093951-2026-11-27-ios-shadows-web-bisect-android-nosee.png) |
| 09:39:51 | [093951-2026-11-27-ios-shadows-web-bisect-android-pipelines-serial-early-log.png](093951-2026-11-27-ios-shadows-web-bisect-android-pipelines-serial-early-log.png) |
| 09:39:51 | [093951-2026-11-27-ios-shadows-web-bisect-android-pipelines-serial.png](093951-2026-11-27-ios-shadows-web-bisect-android-pipelines-serial.png) |
| 09:39:51 | [093951-2026-11-27-ios-shadows-web-bisect-iphone-base-early-log.png](093951-2026-11-27-ios-shadows-web-bisect-iphone-base-early-log.png) |
| 09:39:51 | [093951-2026-11-27-ios-shadows-web-bisect-iphone-base.png](093951-2026-11-27-ios-shadows-web-bisect-iphone-base.png) |
| 09:39:51 | [093951-2026-11-27-ios-shadows-web-bisect-iphone-frames-0-early-log.png](093951-2026-11-27-ios-shadows-web-bisect-iphone-frames-0-early-log.png) |
| 09:39:51 | [093951-2026-11-27-ios-shadows-web-bisect-iphone-frames-0.png](093951-2026-11-27-ios-shadows-web-bisect-iphone-frames-0.png) |
| 09:39:51 | [093951-2026-11-27-ios-shadows-web-bisect-iphone-frames-30-early-log.png](093951-2026-11-27-ios-shadows-web-bisect-iphone-frames-30-early-log.png) |
| 09:39:51 | [093951-2026-11-27-ios-shadows-web-bisect-iphone-frames-30.png](093951-2026-11-27-ios-shadows-web-bisect-iphone-frames-30.png) |
| 09:39:51 | [093951-2026-11-27-ios-shadows-web-bisect-iphone-ios-safe-early-log.png](093951-2026-11-27-ios-shadows-web-bisect-iphone-ios-safe-early-log.png) |
| 09:39:51 | [093951-2026-11-27-ios-shadows-web-bisect-iphone-ios-safe.png](093951-2026-11-27-ios-shadows-web-bisect-iphone-ios-safe.png) |
| 09:39:51 | [093951-2026-11-27-ios-shadows-web-bisect-iphone-killed-early-log.png](093951-2026-11-27-ios-shadows-web-bisect-iphone-killed-early-log.png) |
| 09:39:51 | [093951-2026-11-27-ios-shadows-web-bisect-iphone-killed.png](093951-2026-11-27-ios-shadows-web-bisect-iphone-killed.png) |
| 09:39:51 | [093951-2026-11-27-ios-shadows-web-bisect-iphone-noarrays-early-log.png](093951-2026-11-27-ios-shadows-web-bisect-iphone-noarrays-early-log.png) |
| 09:39:51 | [093951-2026-11-27-ios-shadows-web-bisect-iphone-noarrays.png](093951-2026-11-27-ios-shadows-web-bisect-iphone-noarrays.png) |
| 09:39:51 | [093951-2026-11-27-ios-shadows-web-bisect-iphone-noaudio-early-log.png](093951-2026-11-27-ios-shadows-web-bisect-iphone-noaudio-early-log.png) |
| 09:39:51 | [093951-2026-11-27-ios-shadows-web-bisect-iphone-noaudio.png](093951-2026-11-27-ios-shadows-web-bisect-iphone-noaudio.png) |
| 09:39:51 | [093951-2026-11-27-ios-shadows-web-bisect-iphone-noegui-early-log.png](093951-2026-11-27-ios-shadows-web-bisect-iphone-noegui-early-log.png) |
| 09:39:51 | [093951-2026-11-27-ios-shadows-web-bisect-iphone-noegui.png](093951-2026-11-27-ios-shadows-web-bisect-iphone-noegui.png) |
| 09:39:51 | [093951-2026-11-27-ios-shadows-web-bisect-iphone-nomsaa-early-log.png](093951-2026-11-27-ios-shadows-web-bisect-iphone-nomsaa-early-log.png) |
| 09:39:51 | [093951-2026-11-27-ios-shadows-web-bisect-iphone-nomsaa.png](093951-2026-11-27-ios-shadows-web-bisect-iphone-nomsaa.png) |
| 09:39:51 | [093951-2026-11-27-ios-shadows-web-bisect-iphone-nosee-early-log.png](093951-2026-11-27-ios-shadows-web-bisect-iphone-nosee-early-log.png) |
| 09:39:51 | [093951-2026-11-27-ios-shadows-web-bisect-iphone-nosee.png](093951-2026-11-27-ios-shadows-web-bisect-iphone-nosee.png) |
| 09:39:51 | [093951-2026-11-27-ios-shadows-web-bisect-iphone-noshadow-0-early-log.png](093951-2026-11-27-ios-shadows-web-bisect-iphone-noshadow-0-early-log.png) |
| 09:39:51 | [093951-2026-11-27-ios-shadows-web-bisect-iphone-noshadow-0.png](093951-2026-11-27-ios-shadows-web-bisect-iphone-noshadow-0.png) |
| 09:39:51 | [093951-2026-11-27-ios-shadows-web-bisect-iphone-noshadow-early-log.png](093951-2026-11-27-ios-shadows-web-bisect-iphone-noshadow-early-log.png) |
| 09:39:51 | [093951-2026-11-27-ios-shadows-web-bisect-iphone-noshadow.png](093951-2026-11-27-ios-shadows-web-bisect-iphone-noshadow.png) |
| 09:39:51 | [093951-2026-11-27-ios-shadows-web-bisect-iphone-nosky-early-log.png](093951-2026-11-27-ios-shadows-web-bisect-iphone-nosky-early-log.png) |
| 09:39:51 | [093951-2026-11-27-ios-shadows-web-bisect-iphone-nosky.png](093951-2026-11-27-ios-shadows-web-bisect-iphone-nosky.png) |
| 09:39:51 | [093951-2026-11-27-ios-shadows-web-bisect-iphone-novoice-early-log.png](093951-2026-11-27-ios-shadows-web-bisect-iphone-novoice-early-log.png) |
| 09:39:51 | [093951-2026-11-27-ios-shadows-web-bisect-iphone-novoice.png](093951-2026-11-27-ios-shadows-web-bisect-iphone-novoice.png) |
| 09:39:51 | [093951-2026-11-27-ios-shadows-web-bisect-iphone-pipelines-serial-early-log.png](093951-2026-11-27-ios-shadows-web-bisect-iphone-pipelines-serial-early-log.png) |
| 09:39:51 | [093951-2026-11-27-ios-shadows-web-bisect-iphone-pipelines-serial.png](093951-2026-11-27-ios-shadows-web-bisect-iphone-pipelines-serial.png) |
| 09:39:51 | [093951-2026-11-27-ios-shadows-web-bisect-iphone-plain-early-log.png](093951-2026-11-27-ios-shadows-web-bisect-iphone-plain-early-log.png) |
| 09:39:51 | [093951-2026-11-27-ios-shadows-web-bisect-iphone-plain.png](093951-2026-11-27-ios-shadows-web-bisect-iphone-plain.png) |
| 09:39:51 | [093951-2026-11-27-ios-shadows-web-bisect-iphone-shadowfix-hw2x2+near-noshadow-0-early-log.png](093951-2026-11-27-ios-shadows-web-bisect-iphone-shadowfix-hw2x2+near-noshadow-0-early-log.png) |
| 09:39:51 | [093951-2026-11-27-ios-shadows-web-bisect-iphone-shadowfix-hw2x2+near-noshadow-0.png](093951-2026-11-27-ios-shadows-web-bisect-iphone-shadowfix-hw2x2+near-noshadow-0.png) |
| 09:39:51 | [093951-2026-11-27-ios-shadows-web-bisect-iphone-shadowmap-1024-early-log.png](093951-2026-11-27-ios-shadows-web-bisect-iphone-shadowmap-1024-early-log.png) |
| 09:39:51 | [093951-2026-11-27-ios-shadows-web-bisect-iphone-shadowmap-1024.png](093951-2026-11-27-ios-shadows-web-bisect-iphone-shadowmap-1024.png) |
| 09:39:51 | [093951-2026-11-27-ios-shadows-web-bisect-iphone-shadowmap-512-noshadow-0-early-log.png](093951-2026-11-27-ios-shadows-web-bisect-iphone-shadowmap-512-noshadow-0-early-log.png) |
| 09:39:51 | [093951-2026-11-27-ios-shadows-web-bisect-iphone-shadowmap-512-noshadow-0.png](093951-2026-11-27-ios-shadows-web-bisect-iphone-shadowmap-512-noshadow-0.png) |
| 09:43:12 | [094312-scenes-t8-air2-air-tfn-approach.jpg](094312-scenes-t8-air2-air-tfn-approach.jpg) |
| 09:43:30 | [094330-scenes-t8-air2-air-tfn-approach.mp4](094330-scenes-t8-air2-air-tfn-approach.mp4) |
| 09:44:13 | [094413-scenes-t8-air2-air-contrails-blackforest.jpg](094413-scenes-t8-air2-air-contrails-blackforest.jpg) |
| 09:44:59 | [094459-scenes-t8-air2-air-contrails-dry.jpg](094459-scenes-t8-air2-air-contrails-dry.jpg) |
| 09:45:36 | [094536-scenes-t8-air2-air-dusk-lights.jpg](094536-scenes-t8-air2-air-dusk-lights.jpg) |
| 09:46:38 | [094638-scenes-t8-air2-air-contrails-timelapse.jpg](094638-scenes-t8-air2-air-contrails-timelapse.jpg) |
| 09:46:52 | [094652-scenes-t8-air2-air-contrails-timelapse.mp4](094652-scenes-t8-air2-air-contrails-timelapse.mp4) |
| 09:57:06 | [095706-2026-11-27-ios-shadows-web-log-android-copy.png](095706-2026-11-27-ios-shadows-web-log-android-copy.png) |
| 09:57:06 | [095706-2026-11-27-ios-shadows-web-log-android-killed.png](095706-2026-11-27-ios-shadows-web-log-android-killed.png) |
| 09:57:06 | [095706-2026-11-27-ios-shadows-web-log-android-no-gpu-log.png](095706-2026-11-27-ios-shadows-web-log-android-no-gpu-log.png) |
| 09:57:06 | [095706-2026-11-27-ios-shadows-web-log-android-no-gpu.png](095706-2026-11-27-ios-shadows-web-log-android-no-gpu.png) |
| 09:57:06 | [095706-2026-11-27-ios-shadows-web-log-android-no-wasm-log.png](095706-2026-11-27-ios-shadows-web-log-android-no-wasm-log.png) |
| 09:57:06 | [095706-2026-11-27-ios-shadows-web-log-android-no-wasm.png](095706-2026-11-27-ios-shadows-web-log-android-no-wasm.png) |
| 09:57:06 | [095706-2026-11-27-ios-shadows-web-log-android-reload.png](095706-2026-11-27-ios-shadows-web-log-android-reload.png) |
| 09:57:06 | [095706-2026-11-27-ios-shadows-web-log-android-ride.png](095706-2026-11-27-ios-shadows-web-log-android-ride.png) |
| 09:57:06 | [095706-2026-11-27-ios-shadows-web-log-android-taps.png](095706-2026-11-27-ios-shadows-web-log-android-taps.png) |
| 09:57:06 | [095706-2026-11-27-ios-shadows-web-log-android-too-old-log.png](095706-2026-11-27-ios-shadows-web-log-android-too-old-log.png) |
| 09:57:06 | [095706-2026-11-27-ios-shadows-web-log-android-too-old.png](095706-2026-11-27-ios-shadows-web-log-android-too-old.png) |
| 09:57:06 | [095706-2026-11-27-ios-shadows-web-log-iphone-copy.png](095706-2026-11-27-ios-shadows-web-log-iphone-copy.png) |
| 09:57:06 | [095706-2026-11-27-ios-shadows-web-log-iphone-killed.png](095706-2026-11-27-ios-shadows-web-log-iphone-killed.png) |
| 09:57:06 | [095706-2026-11-27-ios-shadows-web-log-iphone-no-wasm-log.png](095706-2026-11-27-ios-shadows-web-log-iphone-no-wasm-log.png) |
| 09:57:06 | [095706-2026-11-27-ios-shadows-web-log-iphone-no-wasm.png](095706-2026-11-27-ios-shadows-web-log-iphone-no-wasm.png) |
| 09:57:06 | [095706-2026-11-27-ios-shadows-web-log-iphone-reload.png](095706-2026-11-27-ios-shadows-web-log-iphone-reload.png) |
| 09:57:06 | [095706-2026-11-27-ios-shadows-web-log-iphone-ride.png](095706-2026-11-27-ios-shadows-web-log-iphone-ride.png) |
| 09:57:06 | [095706-2026-11-27-ios-shadows-web-log-iphone-taps.png](095706-2026-11-27-ios-shadows-web-log-iphone-taps.png) |
| 09:57:06 | [095706-2026-11-27-ios-shadows-web-log-iphone-too-old-log.png](095706-2026-11-27-ios-shadows-web-log-iphone-too-old-log.png) |
| 09:57:06 | [095706-2026-11-27-ios-shadows-web-log-iphone-too-old.png](095706-2026-11-27-ios-shadows-web-log-iphone-too-old.png) |
| 10:07:39 | [100739-web-air-web-air-webgpu-contrails.jpg](100739-web-air-web-air-webgpu-contrails.jpg) |
| 10:07:39 | [100739-web-air-web-air-webgpu-off.jpg](100739-web-air-web-air-webgpu-off.jpg) |
| 10:08:01 | [100801-web-air-web-air-webgl2-contrails.jpg](100801-web-air-web-air-webgl2-contrails.jpg) |
| 10:08:01 | [100801-web-air-web-air-webgl2-off.jpg](100801-web-air-web-air-webgl2-off.jpg) |
| 10:12:20 | [101220-scenes-t8-air3-air-tfn-approach.jpg](101220-scenes-t8-air3-air-tfn-approach.jpg) |
| 10:12:47 | [101247-scenes-t8-air3-air-tfn-approach.mp4](101247-scenes-t8-air3-air-tfn-approach.mp4) |
| 10:13:28 | [101328-scenes-t8-air3-air-dusk-lights.jpg](101328-scenes-t8-air3-air-dusk-lights.jpg) |
| 10:26:31 | [102631-8c9ebc25-dirty-multiplayer-camera-camera.mp4](102631-8c9ebc25-dirty-multiplayer-camera-camera.mp4) |
| 10:26:31 | [102631-8c9ebc25-dirty-multiplayer-camera-final.jpg](102631-8c9ebc25-dirty-multiplayer-camera-final.jpg) |
| 10:26:31 | [102631-8c9ebc25-dirty-multiplayer-camera-still-30.jpg](102631-8c9ebc25-dirty-multiplayer-camera-still-30.jpg) |
| 10:26:31 | [102631-8c9ebc25-dirty-multiplayer-camera-still-50.jpg](102631-8c9ebc25-dirty-multiplayer-camera-still-50.jpg) |
| 10:26:31 | [102631-8c9ebc25-dirty-multiplayer-camera-still-65.jpg](102631-8c9ebc25-dirty-multiplayer-camera-still-65.jpg) |
| 10:29:04 | [102904-1bfead9d-multiplayer-camera-camera.mp4](102904-1bfead9d-multiplayer-camera-camera.mp4) |
| 10:29:04 | [102904-1bfead9d-multiplayer-camera-final.jpg](102904-1bfead9d-multiplayer-camera-final.jpg) |
| 10:29:04 | [102904-1bfead9d-multiplayer-camera-still-30.jpg](102904-1bfead9d-multiplayer-camera-still-30.jpg) |
| 10:29:04 | [102904-1bfead9d-multiplayer-camera-still-50.jpg](102904-1bfead9d-multiplayer-camera-still-50.jpg) |
| 10:29:04 | [102904-1bfead9d-multiplayer-camera-still-65.jpg](102904-1bfead9d-multiplayer-camera-still-65.jpg) |
| 11:32:37 | [113237-latefix-after-1.jpg](113237-latefix-after-1.jpg) |
| 11:33:33 | [113333-latefix-after-2.jpg](113333-latefix-after-2.jpg) |
| 12:11:05 | [121105-2026-11-27-release-0.2.7-web-webgpu-web-calendar-select.jpg](121105-2026-11-27-release-0.2.7-web-webgpu-web-calendar-select.jpg) |
| 12:11:05 | [121105-2026-11-27-release-0.2.7-web-webgpu-web-calendar.jpg](121105-2026-11-27-release-0.2.7-web-webgpu-web-calendar.jpg) |
| 12:11:05 | [121105-2026-11-27-release-0.2.7-web-webgpu-web-console.jpg](121105-2026-11-27-release-0.2.7-web-webgpu-web-console.jpg) |
| 12:11:05 | [121105-2026-11-27-release-0.2.7-web-webgpu-web-damage-crash.jpg](121105-2026-11-27-release-0.2.7-web-webgpu-web-damage-crash.jpg) |
| 12:11:05 | [121105-2026-11-27-release-0.2.7-web-webgpu-web-damage-fresh.jpg](121105-2026-11-27-release-0.2.7-web-webgpu-web-damage-fresh.jpg) |
| 12:11:05 | [121105-2026-11-27-release-0.2.7-web-webgpu-web-devices-collapsed.jpg](121105-2026-11-27-release-0.2.7-web-webgpu-web-devices-collapsed.jpg) |
| 12:11:05 | [121105-2026-11-27-release-0.2.7-web-webgpu-web-devices-expanded.jpg](121105-2026-11-27-release-0.2.7-web-webgpu-web-devices-expanded.jpg) |
| 12:11:05 | [121105-2026-11-27-release-0.2.7-web-webgpu-web-gamepad.jpg](121105-2026-11-27-release-0.2.7-web-webgpu-web-gamepad.jpg) |
| 12:11:05 | [121105-2026-11-27-release-0.2.7-web-webgpu-web-gps.jpg](121105-2026-11-27-release-0.2.7-web-webgpu-web-gps.jpg) |
| 12:11:05 | [121105-2026-11-27-release-0.2.7-web-webgpu-web-history-delete.jpg](121105-2026-11-27-release-0.2.7-web-webgpu-web-history-delete.jpg) |
| 12:11:05 | [121105-2026-11-27-release-0.2.7-web-webgpu-web-history-ride-file.jpg](121105-2026-11-27-release-0.2.7-web-webgpu-web-history-ride-file.jpg) |
| 12:11:05 | [121105-2026-11-27-release-0.2.7-web-webgpu-web-history-ride-map.jpg](121105-2026-11-27-release-0.2.7-web-webgpu-web-history-ride-map.jpg) |
| 12:11:05 | [121105-2026-11-27-release-0.2.7-web-webgpu-web-hud.jpg](121105-2026-11-27-release-0.2.7-web-webgpu-web-hud.jpg) |
| 12:11:05 | [121105-2026-11-27-release-0.2.7-web-webgpu-web-input-mapping-capture.jpg](121105-2026-11-27-release-0.2.7-web-webgpu-web-input-mapping-capture.jpg) |
| 12:11:05 | [121105-2026-11-27-release-0.2.7-web-webgpu-web-input-mapping-junctions.jpg](121105-2026-11-27-release-0.2.7-web-webgpu-web-input-mapping-junctions.jpg) |
| 12:11:05 | [121105-2026-11-27-release-0.2.7-web-webgpu-web-input-mapping-swapped.jpg](121105-2026-11-27-release-0.2.7-web-webgpu-web-input-mapping-swapped.jpg) |
| 12:11:05 | [121105-2026-11-27-release-0.2.7-web-webgpu-web-input-mapping.jpg](121105-2026-11-27-release-0.2.7-web-webgpu-web-input-mapping.jpg) |
| 12:11:05 | [121105-2026-11-27-release-0.2.7-web-webgpu-web-join.jpg](121105-2026-11-27-release-0.2.7-web-webgpu-web-join.jpg) |
| 12:11:05 | [121105-2026-11-27-release-0.2.7-web-webgpu-web-menu.jpg](121105-2026-11-27-release-0.2.7-web-webgpu-web-menu.jpg) |
| 12:11:05 | [121105-2026-11-27-release-0.2.7-web-webgpu-web-photo-preview.jpg](121105-2026-11-27-release-0.2.7-web-webgpu-web-photo-preview.jpg) |
| 12:11:05 | [121105-2026-11-27-release-0.2.7-web-webgpu-web-ride.jpg](121105-2026-11-27-release-0.2.7-web-webgpu-web-ride.jpg) |
| 12:11:05 | [121105-2026-11-27-release-0.2.7-web-webgpu-web-riders.jpg](121105-2026-11-27-release-0.2.7-web-webgpu-web-riders.jpg) |
| 12:11:05 | [121105-2026-11-27-release-0.2.7-web-webgpu-web-settings.jpg](121105-2026-11-27-release-0.2.7-web-webgpu-web-settings.jpg) |
| 12:11:05 | [121105-2026-11-27-release-0.2.7-web-webgpu-web-strava-recording-downloaded.jpg](121105-2026-11-27-release-0.2.7-web-webgpu-web-strava-recording-downloaded.jpg) |
| 12:11:05 | [121105-2026-11-27-release-0.2.7-web-webgpu-web-strava-recording-saved-to-folder.jpg](121105-2026-11-27-release-0.2.7-web-webgpu-web-strava-recording-saved-to-folder.jpg) |
| 12:11:05 | [121105-2026-11-27-release-0.2.7-web-webgpu-web-strava-recording.jpg](121105-2026-11-27-release-0.2.7-web-webgpu-web-strava-recording.jpg) |
| 12:11:05 | [121105-2026-11-27-release-0.2.7-web-webgpu-web-strava-row.jpg](121105-2026-11-27-release-0.2.7-web-webgpu-web-strava-row.jpg) |
| 12:11:05 | [121105-2026-11-27-release-0.2.7-web-webgpu-web-strava-steps.jpg](121105-2026-11-27-release-0.2.7-web-webgpu-web-strava-steps.jpg) |
| 12:11:05 | [121105-2026-11-27-release-0.2.7-web-webgpu-web-touch-hints.jpg](121105-2026-11-27-release-0.2.7-web-webgpu-web-touch-hints.jpg) |
| 12:11:05 | [121105-2026-11-27-release-0.2.7-web-webgpu-web-touch-hold.jpg](121105-2026-11-27-release-0.2.7-web-webgpu-web-touch-hold.jpg) |
| 12:11:05 | [121105-2026-11-27-release-0.2.7-web-webgpu-web-unicorn-flight.jpg](121105-2026-11-27-release-0.2.7-web-webgpu-web-unicorn-flight.jpg) |
| 12:11:05 | [121105-2026-11-27-release-0.2.7-web-webgpu-web-unicorn-inspect.jpg](121105-2026-11-27-release-0.2.7-web-webgpu-web-unicorn-inspect.jpg) |
| 12:11:05 | [121105-2026-11-27-release-0.2.7-web-webgpu-web-unicorn-menu.jpg](121105-2026-11-27-release-0.2.7-web-webgpu-web-unicorn-menu.jpg) |
| 12:11:05 | [121105-2026-11-27-release-0.2.7-web-webgpu-web-weather.jpg](121105-2026-11-27-release-0.2.7-web-webgpu-web-weather.jpg) |
| 12:11:05 | [121105-2026-11-27-release-0.2.7-web-webgpu-web-workout-map.jpg](121105-2026-11-27-release-0.2.7-web-webgpu-web-workout-map.jpg) |
| 12:11:05 | [121105-2026-11-27-release-0.2.7-web-webgpu-web.jpg](121105-2026-11-27-release-0.2.7-web-webgpu-web.jpg) |
| 12:13:27 | [121327-2026-11-27-release-0.2.7-web-webgl2-web-webgl2-calendar-select.jpg](121327-2026-11-27-release-0.2.7-web-webgl2-web-webgl2-calendar-select.jpg) |
| 12:13:27 | [121327-2026-11-27-release-0.2.7-web-webgl2-web-webgl2-calendar.jpg](121327-2026-11-27-release-0.2.7-web-webgl2-web-webgl2-calendar.jpg) |
| 12:13:27 | [121327-2026-11-27-release-0.2.7-web-webgl2-web-webgl2-console.jpg](121327-2026-11-27-release-0.2.7-web-webgl2-web-webgl2-console.jpg) |
| 12:13:27 | [121327-2026-11-27-release-0.2.7-web-webgl2-web-webgl2-damage-crash.jpg](121327-2026-11-27-release-0.2.7-web-webgl2-web-webgl2-damage-crash.jpg) |
| 12:13:27 | [121327-2026-11-27-release-0.2.7-web-webgl2-web-webgl2-damage-fresh.jpg](121327-2026-11-27-release-0.2.7-web-webgl2-web-webgl2-damage-fresh.jpg) |
| 12:13:27 | [121327-2026-11-27-release-0.2.7-web-webgl2-web-webgl2-devices-collapsed.jpg](121327-2026-11-27-release-0.2.7-web-webgl2-web-webgl2-devices-collapsed.jpg) |
| 12:13:27 | [121327-2026-11-27-release-0.2.7-web-webgl2-web-webgl2-devices-expanded.jpg](121327-2026-11-27-release-0.2.7-web-webgl2-web-webgl2-devices-expanded.jpg) |
| 12:13:27 | [121327-2026-11-27-release-0.2.7-web-webgl2-web-webgl2-gamepad.jpg](121327-2026-11-27-release-0.2.7-web-webgl2-web-webgl2-gamepad.jpg) |
| 12:13:27 | [121327-2026-11-27-release-0.2.7-web-webgl2-web-webgl2-gps.jpg](121327-2026-11-27-release-0.2.7-web-webgl2-web-webgl2-gps.jpg) |
| 12:13:27 | [121327-2026-11-27-release-0.2.7-web-webgl2-web-webgl2-history-delete.jpg](121327-2026-11-27-release-0.2.7-web-webgl2-web-webgl2-history-delete.jpg) |
| 12:13:27 | [121327-2026-11-27-release-0.2.7-web-webgl2-web-webgl2-history-ride-file.jpg](121327-2026-11-27-release-0.2.7-web-webgl2-web-webgl2-history-ride-file.jpg) |
| 12:13:27 | [121327-2026-11-27-release-0.2.7-web-webgl2-web-webgl2-history-ride-map.jpg](121327-2026-11-27-release-0.2.7-web-webgl2-web-webgl2-history-ride-map.jpg) |
| 12:13:27 | [121327-2026-11-27-release-0.2.7-web-webgl2-web-webgl2-hud.jpg](121327-2026-11-27-release-0.2.7-web-webgl2-web-webgl2-hud.jpg) |
| 12:13:27 | [121327-2026-11-27-release-0.2.7-web-webgl2-web-webgl2-input-mapping-capture.jpg](121327-2026-11-27-release-0.2.7-web-webgl2-web-webgl2-input-mapping-capture.jpg) |
| 12:13:27 | [121327-2026-11-27-release-0.2.7-web-webgl2-web-webgl2-input-mapping-junctions.jpg](121327-2026-11-27-release-0.2.7-web-webgl2-web-webgl2-input-mapping-junctions.jpg) |
| 12:13:27 | [121327-2026-11-27-release-0.2.7-web-webgl2-web-webgl2-input-mapping-swapped.jpg](121327-2026-11-27-release-0.2.7-web-webgl2-web-webgl2-input-mapping-swapped.jpg) |
| 12:13:27 | [121327-2026-11-27-release-0.2.7-web-webgl2-web-webgl2-input-mapping.jpg](121327-2026-11-27-release-0.2.7-web-webgl2-web-webgl2-input-mapping.jpg) |
| 12:13:27 | [121327-2026-11-27-release-0.2.7-web-webgl2-web-webgl2-join.jpg](121327-2026-11-27-release-0.2.7-web-webgl2-web-webgl2-join.jpg) |
| 12:13:27 | [121327-2026-11-27-release-0.2.7-web-webgl2-web-webgl2-menu.jpg](121327-2026-11-27-release-0.2.7-web-webgl2-web-webgl2-menu.jpg) |
| 12:13:27 | [121327-2026-11-27-release-0.2.7-web-webgl2-web-webgl2-photo-preview.jpg](121327-2026-11-27-release-0.2.7-web-webgl2-web-webgl2-photo-preview.jpg) |
| 12:13:27 | [121327-2026-11-27-release-0.2.7-web-webgl2-web-webgl2-ride.jpg](121327-2026-11-27-release-0.2.7-web-webgl2-web-webgl2-ride.jpg) |
| 12:13:27 | [121327-2026-11-27-release-0.2.7-web-webgl2-web-webgl2-riders.jpg](121327-2026-11-27-release-0.2.7-web-webgl2-web-webgl2-riders.jpg) |
| 12:13:27 | [121327-2026-11-27-release-0.2.7-web-webgl2-web-webgl2-settings.jpg](121327-2026-11-27-release-0.2.7-web-webgl2-web-webgl2-settings.jpg) |
| 12:13:27 | [121327-2026-11-27-release-0.2.7-web-webgl2-web-webgl2-strava-recording-downloaded.jpg](121327-2026-11-27-release-0.2.7-web-webgl2-web-webgl2-strava-recording-downloaded.jpg) |
| 12:13:27 | [121327-2026-11-27-release-0.2.7-web-webgl2-web-webgl2-strava-recording-saved-to-folder.jpg](121327-2026-11-27-release-0.2.7-web-webgl2-web-webgl2-strava-recording-saved-to-folder.jpg) |
| 12:13:27 | [121327-2026-11-27-release-0.2.7-web-webgl2-web-webgl2-strava-recording.jpg](121327-2026-11-27-release-0.2.7-web-webgl2-web-webgl2-strava-recording.jpg) |
| 12:13:27 | [121327-2026-11-27-release-0.2.7-web-webgl2-web-webgl2-strava-row.jpg](121327-2026-11-27-release-0.2.7-web-webgl2-web-webgl2-strava-row.jpg) |
| 12:13:27 | [121327-2026-11-27-release-0.2.7-web-webgl2-web-webgl2-strava-steps.jpg](121327-2026-11-27-release-0.2.7-web-webgl2-web-webgl2-strava-steps.jpg) |
| 12:13:27 | [121327-2026-11-27-release-0.2.7-web-webgl2-web-webgl2-touch-hints.jpg](121327-2026-11-27-release-0.2.7-web-webgl2-web-webgl2-touch-hints.jpg) |
| 12:13:27 | [121327-2026-11-27-release-0.2.7-web-webgl2-web-webgl2-touch-hold.jpg](121327-2026-11-27-release-0.2.7-web-webgl2-web-webgl2-touch-hold.jpg) |
| 12:13:27 | [121327-2026-11-27-release-0.2.7-web-webgl2-web-webgl2-unicorn-flight.jpg](121327-2026-11-27-release-0.2.7-web-webgl2-web-webgl2-unicorn-flight.jpg) |
| 12:13:27 | [121327-2026-11-27-release-0.2.7-web-webgl2-web-webgl2-unicorn-inspect.jpg](121327-2026-11-27-release-0.2.7-web-webgl2-web-webgl2-unicorn-inspect.jpg) |
| 12:13:27 | [121327-2026-11-27-release-0.2.7-web-webgl2-web-webgl2-unicorn-menu.jpg](121327-2026-11-27-release-0.2.7-web-webgl2-web-webgl2-unicorn-menu.jpg) |
| 12:13:27 | [121327-2026-11-27-release-0.2.7-web-webgl2-web-webgl2-weather.jpg](121327-2026-11-27-release-0.2.7-web-webgl2-web-webgl2-weather.jpg) |
| 12:13:27 | [121327-2026-11-27-release-0.2.7-web-webgl2-web-webgl2-workout-map.jpg](121327-2026-11-27-release-0.2.7-web-webgl2-web-webgl2-workout-map.jpg) |
| 12:13:27 | [121327-2026-11-27-release-0.2.7-web-webgl2-web-webgl2.jpg](121327-2026-11-27-release-0.2.7-web-webgl2-web-webgl2.jpg) |
| 12:16:12 | [121612-2026-11-27-release-0.2.7-web-world-webgpu-web-world-cached-loading.jpg](121612-2026-11-27-release-0.2.7-web-world-webgpu-web-world-cached-loading.jpg) |
| 12:16:12 | [121612-2026-11-27-release-0.2.7-web-world-webgpu-web-world-cached.jpg](121612-2026-11-27-release-0.2.7-web-world-webgpu-web-world-cached.jpg) |
| 12:16:12 | [121612-2026-11-27-release-0.2.7-web-world-webgpu-web-world-first-loading.jpg](121612-2026-11-27-release-0.2.7-web-world-webgpu-web-world-first-loading.jpg) |
| 12:16:12 | [121612-2026-11-27-release-0.2.7-web-world-webgpu-web-world-teleport.jpg](121612-2026-11-27-release-0.2.7-web-world-webgpu-web-world-teleport.jpg) |
| 12:16:12 | [121612-2026-11-27-release-0.2.7-web-world-webgpu-web-world.jpg](121612-2026-11-27-release-0.2.7-web-world-webgpu-web-world.jpg) |
| 12:17:23 | [121723-2026-11-27-release-0.2.7-web-world-webgl2-web-world-webgl2-cached-loading.jpg](121723-2026-11-27-release-0.2.7-web-world-webgl2-web-world-webgl2-cached-loading.jpg) |
| 12:17:23 | [121723-2026-11-27-release-0.2.7-web-world-webgl2-web-world-webgl2-cached.jpg](121723-2026-11-27-release-0.2.7-web-world-webgl2-web-world-webgl2-cached.jpg) |
| 12:17:23 | [121723-2026-11-27-release-0.2.7-web-world-webgl2-web-world-webgl2-first-loading.jpg](121723-2026-11-27-release-0.2.7-web-world-webgl2-web-world-webgl2-first-loading.jpg) |
| 12:17:23 | [121723-2026-11-27-release-0.2.7-web-world-webgl2-web-world-webgl2-teleport.jpg](121723-2026-11-27-release-0.2.7-web-world-webgl2-web-world-webgl2-teleport.jpg) |
| 12:17:23 | [121723-2026-11-27-release-0.2.7-web-world-webgl2-web-world-webgl2.jpg](121723-2026-11-27-release-0.2.7-web-world-webgl2-web-world-webgl2.jpg) |
| 12:20:56 | [122056-2026-11-27-release-0.2.7-web-world2-webgpu-web-world-cached-loading.jpg](122056-2026-11-27-release-0.2.7-web-world2-webgpu-web-world-cached-loading.jpg) |
| 12:20:56 | [122056-2026-11-27-release-0.2.7-web-world2-webgpu-web-world-cached.jpg](122056-2026-11-27-release-0.2.7-web-world2-webgpu-web-world-cached.jpg) |
| 12:20:56 | [122056-2026-11-27-release-0.2.7-web-world2-webgpu-web-world-first-loading.jpg](122056-2026-11-27-release-0.2.7-web-world2-webgpu-web-world-first-loading.jpg) |
| 12:20:56 | [122056-2026-11-27-release-0.2.7-web-world2-webgpu-web-world-teleport.jpg](122056-2026-11-27-release-0.2.7-web-world2-webgpu-web-world-teleport.jpg) |
| 12:20:56 | [122056-2026-11-27-release-0.2.7-web-world2-webgpu-web-world.jpg](122056-2026-11-27-release-0.2.7-web-world2-webgpu-web-world.jpg) |
| 12:22:33 | [122233-2026-11-27-release-0.2.7-web-world2-webgl2-web-world-webgl2-cached-loading.jpg](122233-2026-11-27-release-0.2.7-web-world2-webgl2-web-world-webgl2-cached-loading.jpg) |
| 12:22:33 | [122233-2026-11-27-release-0.2.7-web-world2-webgl2-web-world-webgl2-cached.jpg](122233-2026-11-27-release-0.2.7-web-world2-webgl2-web-world-webgl2-cached.jpg) |
| 12:22:33 | [122233-2026-11-27-release-0.2.7-web-world2-webgl2-web-world-webgl2-first-loading.jpg](122233-2026-11-27-release-0.2.7-web-world2-webgl2-web-world-webgl2-first-loading.jpg) |
| 12:22:33 | [122233-2026-11-27-release-0.2.7-web-world2-webgl2-web-world-webgl2-teleport.jpg](122233-2026-11-27-release-0.2.7-web-world2-webgl2-web-world-webgl2-teleport.jpg) |
| 12:22:33 | [122233-2026-11-27-release-0.2.7-web-world2-webgl2-web-world-webgl2.jpg](122233-2026-11-27-release-0.2.7-web-world2-webgl2-web-world-webgl2.jpg) |
| 12:24:22 | [122422-2026-11-27-release-0.2.7-windows-icon-ocw-desktop-128.png](122422-2026-11-27-release-0.2.7-windows-icon-ocw-desktop-128.png) |
| 12:24:22 | [122422-2026-11-27-release-0.2.7-windows-icon-ocw-desktop-16.png](122422-2026-11-27-release-0.2.7-windows-icon-ocw-desktop-16.png) |
| 12:24:22 | [122422-2026-11-27-release-0.2.7-windows-icon-ocw-desktop-24.png](122422-2026-11-27-release-0.2.7-windows-icon-ocw-desktop-24.png) |
| 12:24:22 | [122422-2026-11-27-release-0.2.7-windows-icon-ocw-desktop-256.png](122422-2026-11-27-release-0.2.7-windows-icon-ocw-desktop-256.png) |
| 12:24:22 | [122422-2026-11-27-release-0.2.7-windows-icon-ocw-desktop-32.png](122422-2026-11-27-release-0.2.7-windows-icon-ocw-desktop-32.png) |
| 12:24:22 | [122422-2026-11-27-release-0.2.7-windows-icon-ocw-desktop-48.png](122422-2026-11-27-release-0.2.7-windows-icon-ocw-desktop-48.png) |
| 12:24:22 | [122422-2026-11-27-release-0.2.7-windows-icon-ocw-desktop-64.png](122422-2026-11-27-release-0.2.7-windows-icon-ocw-desktop-64.png) |
| 12:24:22 | [122422-2026-11-27-release-0.2.7-windows-icon-ocw-studio-128.png](122422-2026-11-27-release-0.2.7-windows-icon-ocw-studio-128.png) |
| 12:24:22 | [122422-2026-11-27-release-0.2.7-windows-icon-ocw-studio-16.png](122422-2026-11-27-release-0.2.7-windows-icon-ocw-studio-16.png) |
| 12:24:22 | [122422-2026-11-27-release-0.2.7-windows-icon-ocw-studio-24.png](122422-2026-11-27-release-0.2.7-windows-icon-ocw-studio-24.png) |
| 12:24:22 | [122422-2026-11-27-release-0.2.7-windows-icon-ocw-studio-256.png](122422-2026-11-27-release-0.2.7-windows-icon-ocw-studio-256.png) |
| 12:24:22 | [122422-2026-11-27-release-0.2.7-windows-icon-ocw-studio-32.png](122422-2026-11-27-release-0.2.7-windows-icon-ocw-studio-32.png) |
| 12:24:22 | [122422-2026-11-27-release-0.2.7-windows-icon-ocw-studio-48.png](122422-2026-11-27-release-0.2.7-windows-icon-ocw-studio-48.png) |
| 12:24:22 | [122422-2026-11-27-release-0.2.7-windows-icon-ocw-studio-64.png](122422-2026-11-27-release-0.2.7-windows-icon-ocw-studio-64.png) |
| 12:59:56 | [125956-smoke-leela-f99daa2a-dirty-shot-ocw.jpg](125956-smoke-leela-f99daa2a-dirty-shot-ocw.jpg) |
| 13:00:06 | [130006-smoke-leela-f99daa2a-dirty-shot-wayland-ocw-wayland.jpg](130006-smoke-leela-f99daa2a-dirty-shot-wayland-ocw-wayland.jpg) |
| 13:01:16 | [130116-ant-fec-A-end.jpg](130116-ant-fec-A-end.jpg) |
| 13:04:31 | [130431-ant-fec-B-ride-erg.jpg](130431-ant-fec-B-ride-erg.jpg) |
| 13:04:36 | [130436-ant-fec-B-ride-erg.mp4](130436-ant-fec-B-ride-erg.mp4) |
| 13:09:05 | [130905-ant-fec-A-1-devices-fe-c-trainer.png](130905-ant-fec-A-1-devices-fe-c-trainer.png) |
| 13:09:14 | [130914-ant-fec-A-2-ride-erg-240w.png](130914-ant-fec-A-2-ride-erg-240w.png) |
| 13:09:41 | [130941-ant-fec-A-end.jpg](130941-ant-fec-A-end.jpg) |
| 13:11:32 | [131132-rollout-0.2.7-desktop-release-join-public.jpg](131132-rollout-0.2.7-desktop-release-join-public.jpg) |
| 13:19:21 | [131921-f668ba4a-dirty-video-wayland-air-flyby-tfn-airliner-video.jpg](131921-f668ba4a-dirty-video-wayland-air-flyby-tfn-airliner-video.jpg) |
| 13:19:21 | [131921-f668ba4a-dirty-video-wayland-air-flyby-tfn-airliner-video.mp4](131921-f668ba4a-dirty-video-wayland-air-flyby-tfn-airliner-video.mp4) |
| 13:20:23 | [132023-2026-11-27-ant-webusb-web-ant-webkit-ant.png](132023-2026-11-27-ant-webusb-web-ant-webkit-ant.png) |
| 13:20:23 | [132023-2026-11-27-ant-webusb-web-ant-webkit-devices.png](132023-2026-11-27-ant-webusb-web-ant-webkit-devices.png) |
| 13:20:41 | [132041-f668ba4a-dirty-video-wayland-air-flyby-tenerife-helicopter-video.jpg](132041-f668ba4a-dirty-video-wayland-air-flyby-tenerife-helicopter-video.jpg) |
| 13:20:41 | [132041-f668ba4a-dirty-video-wayland-air-flyby-tenerife-helicopter-video.mp4](132041-f668ba4a-dirty-video-wayland-air-flyby-tenerife-helicopter-video.mp4) |
| 13:21:53 | [132153-2026-11-27-ant-webusb-web-ant-chromium-ant-page.jpg](132153-2026-11-27-ant-webusb-web-ant-chromium-ant-page.jpg) |
| 13:21:53 | [132153-2026-11-27-ant-webusb-web-ant-chromium-connected.jpg](132153-2026-11-27-ant-webusb-web-ant-chromium-connected.jpg) |
| 13:21:53 | [132153-2026-11-27-ant-webusb-web-ant-chromium-devices.jpg](132153-2026-11-27-ant-webusb-web-ant-chromium-devices.jpg) |
| 13:21:53 | [132153-2026-11-27-ant-webusb-web-ant-chromium-found-2.jpg](132153-2026-11-27-ant-webusb-web-ant-chromium-found-2.jpg) |
| 13:21:53 | [132153-2026-11-27-ant-webusb-web-ant-chromium-found.jpg](132153-2026-11-27-ant-webusb-web-ant-chromium-found.jpg) |
| 13:21:53 | [132153-2026-11-27-ant-webusb-web-ant-chromium-key-typing.jpg](132153-2026-11-27-ant-webusb-web-ant-chromium-key-typing.jpg) |
| 13:21:53 | [132153-2026-11-27-ant-webusb-web-ant-chromium-nousb-ant.jpg](132153-2026-11-27-ant-webusb-web-ant-chromium-nousb-ant.jpg) |
| 13:21:53 | [132153-2026-11-27-ant-webusb-web-ant-chromium-nousb-devices.jpg](132153-2026-11-27-ant-webusb-web-ant-chromium-nousb-devices.jpg) |
| 13:21:53 | [132153-2026-11-27-ant-webusb-web-ant-chromium-reload.jpg](132153-2026-11-27-ant-webusb-web-ant-chromium-reload.jpg) |
| 13:21:53 | [132153-2026-11-27-ant-webusb-web-ant-chromium-ride.jpg](132153-2026-11-27-ant-webusb-web-ant-chromium-ride.jpg) |
| 13:24:20 | [132420-f668ba4a-dirty-video-wayland-air-flyby-tfn-airliner-video.jpg](132420-f668ba4a-dirty-video-wayland-air-flyby-tfn-airliner-video.jpg) |
| 13:24:20 | [132420-f668ba4a-dirty-video-wayland-air-flyby-tfn-airliner-video.mp4](132420-f668ba4a-dirty-video-wayland-air-flyby-tfn-airliner-video.mp4) |
| 13:25:31 | [132531-f668ba4a-dirty-video-wayland-air-flyby-tenerife-helicopter-video.jpg](132531-f668ba4a-dirty-video-wayland-air-flyby-tenerife-helicopter-video.jpg) |
| 13:25:31 | [132531-f668ba4a-dirty-video-wayland-air-flyby-tenerife-helicopter-video.mp4](132531-f668ba4a-dirty-video-wayland-air-flyby-tenerife-helicopter-video.mp4) |
| 13:26:17 | [132617-2026-11-27-aircraft-flyby-airliner-flyby-1280.mp4](132617-2026-11-27-aircraft-flyby-airliner-flyby-1280.mp4) |
| 13:26:21 | [132621-2026-11-27-aircraft-flyby-airliner-still-1-s.jpg](132621-2026-11-27-aircraft-flyby-airliner-still-1-s.jpg) |
| 13:26:21 | [132621-2026-11-27-aircraft-flyby-airliner-still-7-s.jpg](132621-2026-11-27-aircraft-flyby-airliner-still-7-s.jpg) |
| 13:26:21 | [132621-2026-11-27-aircraft-flyby-helicopter-flyby-1280.mp4](132621-2026-11-27-aircraft-flyby-helicopter-flyby-1280.mp4) |
| 13:26:22 | [132622-2026-11-27-aircraft-flyby-airliner-still-17-s.jpg](132622-2026-11-27-aircraft-flyby-airliner-still-17-s.jpg) |
| 13:26:22 | [132622-2026-11-27-aircraft-flyby-airliner-still-22-s.jpg](132622-2026-11-27-aircraft-flyby-airliner-still-22-s.jpg) |
| 13:26:22 | [132622-2026-11-27-aircraft-flyby-airliner-still-31-s.jpg](132622-2026-11-27-aircraft-flyby-airliner-still-31-s.jpg) |
| 13:26:22 | [132622-2026-11-27-aircraft-flyby-helicopter-still-9-s.jpg](132622-2026-11-27-aircraft-flyby-helicopter-still-9-s.jpg) |
| 13:30:26 | [133026-rollout-0.2.7-remote-web-end.jpg](133026-rollout-0.2.7-remote-web-end.jpg) |
| 13:30:26 | [133026-rollout-0.2.7-remote-web-joined.jpg](133026-rollout-0.2.7-remote-web-joined.jpg) |
| 13:30:26 | [133026-rollout-0.2.7-remote-web-riding.jpg](133026-rollout-0.2.7-remote-web-riding.jpg) |
| 13:35:19 | [133519-web-bisect-web-bisect-android-base-early-log.png](133519-web-bisect-web-bisect-android-base-early-log.png) |
| 13:35:19 | [133519-web-bisect-web-bisect-android-base-photo-1.jpg](133519-web-bisect-web-bisect-android-base-photo-1.jpg) |
| 13:35:19 | [133519-web-bisect-web-bisect-android-base.png](133519-web-bisect-web-bisect-android-base.png) |
| 13:35:19 | [133519-web-bisect-web-bisect-android-ios-safe-early-log.png](133519-web-bisect-web-bisect-android-ios-safe-early-log.png) |
| 13:35:19 | [133519-web-bisect-web-bisect-android-ios-safe.png](133519-web-bisect-web-bisect-android-ios-safe.png) |
| 13:35:19 | [133519-web-bisect-web-bisect-android-noegui-early-log.png](133519-web-bisect-web-bisect-android-noegui-early-log.png) |
| 13:35:19 | [133519-web-bisect-web-bisect-android-noegui-photo-1.jpg](133519-web-bisect-web-bisect-android-noegui-photo-1.jpg) |
| 13:35:19 | [133519-web-bisect-web-bisect-android-noegui.png](133519-web-bisect-web-bisect-android-noegui.png) |
| 13:35:19 | [133519-web-bisect-web-bisect-android-nosee-early-log.png](133519-web-bisect-web-bisect-android-nosee-early-log.png) |
| 13:35:19 | [133519-web-bisect-web-bisect-android-nosee-photo-1.jpg](133519-web-bisect-web-bisect-android-nosee-photo-1.jpg) |
| 13:35:19 | [133519-web-bisect-web-bisect-android-nosee.png](133519-web-bisect-web-bisect-android-nosee.png) |
| 13:35:19 | [133519-web-bisect-web-bisect-android-pipelines-serial-early-log.png](133519-web-bisect-web-bisect-android-pipelines-serial-early-log.png) |
| 13:35:19 | [133519-web-bisect-web-bisect-android-pipelines-serial-photo-1.jpg](133519-web-bisect-web-bisect-android-pipelines-serial-photo-1.jpg) |
| 13:35:19 | [133519-web-bisect-web-bisect-android-pipelines-serial.png](133519-web-bisect-web-bisect-android-pipelines-serial.png) |
| 13:35:19 | [133519-web-bisect-web-bisect-iphone-base-early-log.png](133519-web-bisect-web-bisect-iphone-base-early-log.png) |
| 13:35:19 | [133519-web-bisect-web-bisect-iphone-base.png](133519-web-bisect-web-bisect-iphone-base.png) |
| 13:35:19 | [133519-web-bisect-web-bisect-iphone-frames-0-early-log.png](133519-web-bisect-web-bisect-iphone-frames-0-early-log.png) |
| 13:35:19 | [133519-web-bisect-web-bisect-iphone-frames-0.png](133519-web-bisect-web-bisect-iphone-frames-0.png) |
| 13:35:19 | [133519-web-bisect-web-bisect-iphone-frames-30-early-log.png](133519-web-bisect-web-bisect-iphone-frames-30-early-log.png) |
| 13:35:19 | [133519-web-bisect-web-bisect-iphone-frames-30.png](133519-web-bisect-web-bisect-iphone-frames-30.png) |
| 13:35:19 | [133519-web-bisect-web-bisect-iphone-ios-safe-early-log.png](133519-web-bisect-web-bisect-iphone-ios-safe-early-log.png) |
| 13:35:19 | [133519-web-bisect-web-bisect-iphone-ios-safe.png](133519-web-bisect-web-bisect-iphone-ios-safe.png) |
| 13:35:19 | [133519-web-bisect-web-bisect-iphone-killed-early-log.png](133519-web-bisect-web-bisect-iphone-killed-early-log.png) |
| 13:35:19 | [133519-web-bisect-web-bisect-iphone-killed.png](133519-web-bisect-web-bisect-iphone-killed.png) |
| 13:35:19 | [133519-web-bisect-web-bisect-iphone-noarrays-early-log.png](133519-web-bisect-web-bisect-iphone-noarrays-early-log.png) |
| 13:35:19 | [133519-web-bisect-web-bisect-iphone-noarrays.png](133519-web-bisect-web-bisect-iphone-noarrays.png) |
| 13:35:19 | [133519-web-bisect-web-bisect-iphone-noaudio-early-log.png](133519-web-bisect-web-bisect-iphone-noaudio-early-log.png) |
| 13:35:19 | [133519-web-bisect-web-bisect-iphone-noaudio.png](133519-web-bisect-web-bisect-iphone-noaudio.png) |
| 13:35:19 | [133519-web-bisect-web-bisect-iphone-noegui-early-log.png](133519-web-bisect-web-bisect-iphone-noegui-early-log.png) |
| 13:35:19 | [133519-web-bisect-web-bisect-iphone-noegui.png](133519-web-bisect-web-bisect-iphone-noegui.png) |
| 13:35:19 | [133519-web-bisect-web-bisect-iphone-nomsaa-early-log.png](133519-web-bisect-web-bisect-iphone-nomsaa-early-log.png) |
| 13:35:19 | [133519-web-bisect-web-bisect-iphone-nomsaa.png](133519-web-bisect-web-bisect-iphone-nomsaa.png) |
| 13:35:19 | [133519-web-bisect-web-bisect-iphone-nosee-early-log.png](133519-web-bisect-web-bisect-iphone-nosee-early-log.png) |
| 13:35:19 | [133519-web-bisect-web-bisect-iphone-nosee.png](133519-web-bisect-web-bisect-iphone-nosee.png) |
| 13:35:19 | [133519-web-bisect-web-bisect-iphone-noshadow-0-early-log.png](133519-web-bisect-web-bisect-iphone-noshadow-0-early-log.png) |
| 13:35:19 | [133519-web-bisect-web-bisect-iphone-noshadow-0.png](133519-web-bisect-web-bisect-iphone-noshadow-0.png) |
| 13:35:19 | [133519-web-bisect-web-bisect-iphone-noshadow-early-log.png](133519-web-bisect-web-bisect-iphone-noshadow-early-log.png) |
| 13:35:19 | [133519-web-bisect-web-bisect-iphone-noshadow.png](133519-web-bisect-web-bisect-iphone-noshadow.png) |
| 13:35:19 | [133519-web-bisect-web-bisect-iphone-nosky-early-log.png](133519-web-bisect-web-bisect-iphone-nosky-early-log.png) |
| 13:35:19 | [133519-web-bisect-web-bisect-iphone-nosky.png](133519-web-bisect-web-bisect-iphone-nosky.png) |
| 13:35:19 | [133519-web-bisect-web-bisect-iphone-novoice-early-log.png](133519-web-bisect-web-bisect-iphone-novoice-early-log.png) |
| 13:35:19 | [133519-web-bisect-web-bisect-iphone-novoice.png](133519-web-bisect-web-bisect-iphone-novoice.png) |
| 13:35:19 | [133519-web-bisect-web-bisect-iphone-photos-1-early-log.png](133519-web-bisect-web-bisect-iphone-photos-1-early-log.png) |
| 13:35:19 | [133519-web-bisect-web-bisect-iphone-photos-1-photofix-once+nosave-early-log.png](133519-web-bisect-web-bisect-iphone-photos-1-photofix-once+nosave-early-log.png) |
| 13:35:19 | [133519-web-bisect-web-bisect-iphone-photos-1-photofix-once+nosave.png](133519-web-bisect-web-bisect-iphone-photos-1-photofix-once+nosave.png) |
| 13:35:19 | [133519-web-bisect-web-bisect-iphone-photos-1-photofix-screen-early-log.png](133519-web-bisect-web-bisect-iphone-photos-1-photofix-screen-early-log.png) |
| 13:35:19 | [133519-web-bisect-web-bisect-iphone-photos-1-photofix-screen.png](133519-web-bisect-web-bisect-iphone-photos-1-photofix-screen.png) |
| 13:35:19 | [133519-web-bisect-web-bisect-iphone-photos-1-photofix-small-early-log.png](133519-web-bisect-web-bisect-iphone-photos-1-photofix-small-early-log.png) |
| 13:35:19 | [133519-web-bisect-web-bisect-iphone-photos-1-photofix-small.png](133519-web-bisect-web-bisect-iphone-photos-1-photofix-small.png) |
| 13:35:19 | [133519-web-bisect-web-bisect-iphone-photos-1.png](133519-web-bisect-web-bisect-iphone-photos-1.png) |
| 13:35:19 | [133519-web-bisect-web-bisect-iphone-pipelines-serial-early-log.png](133519-web-bisect-web-bisect-iphone-pipelines-serial-early-log.png) |
| 13:35:19 | [133519-web-bisect-web-bisect-iphone-pipelines-serial.png](133519-web-bisect-web-bisect-iphone-pipelines-serial.png) |
| 13:35:19 | [133519-web-bisect-web-bisect-iphone-plain-early-log.png](133519-web-bisect-web-bisect-iphone-plain-early-log.png) |
| 13:35:19 | [133519-web-bisect-web-bisect-iphone-plain.png](133519-web-bisect-web-bisect-iphone-plain.png) |
| 13:35:19 | [133519-web-bisect-web-bisect-iphone-shadowfix-hw2x2+near-noshadow-0-early-log.png](133519-web-bisect-web-bisect-iphone-shadowfix-hw2x2+near-noshadow-0-early-log.png) |
| 13:35:19 | [133519-web-bisect-web-bisect-iphone-shadowfix-hw2x2+near-noshadow-0.png](133519-web-bisect-web-bisect-iphone-shadowfix-hw2x2+near-noshadow-0.png) |
| 13:35:19 | [133519-web-bisect-web-bisect-iphone-shadowmap-1024-early-log.png](133519-web-bisect-web-bisect-iphone-shadowmap-1024-early-log.png) |
| 13:35:19 | [133519-web-bisect-web-bisect-iphone-shadowmap-1024.png](133519-web-bisect-web-bisect-iphone-shadowmap-1024.png) |
| 13:35:19 | [133519-web-bisect-web-bisect-iphone-shadowmap-512-noshadow-0-early-log.png](133519-web-bisect-web-bisect-iphone-shadowmap-512-noshadow-0-early-log.png) |
| 13:35:19 | [133519-web-bisect-web-bisect-iphone-shadowmap-512-noshadow-0.png](133519-web-bisect-web-bisect-iphone-shadowmap-512-noshadow-0.png) |
| 13:47:51 | [134751-web-web-webkit-iphone-hints.png](134751-web-web-webkit-iphone-hints.png) |
| 13:47:51 | [134751-web-web-webkit-iphone-hold.png](134751-web-web-webkit-iphone-hold.png) |
| 13:47:51 | [134751-web-web-webkit-iphone-landscape-hints.png](134751-web-web-webkit-iphone-landscape-hints.png) |
| 13:47:51 | [134751-web-web-webkit-iphone-landscape-hold.png](134751-web-web-webkit-iphone-landscape-hold.png) |
| 13:47:51 | [134751-web-web-webkit-iphone-landscape-riding.png](134751-web-web-webkit-iphone-landscape-riding.png) |
| 13:47:51 | [134751-web-web-webkit-iphone-landscape-stopped.png](134751-web-web-webkit-iphone-landscape-stopped.png) |
| 13:47:51 | [134751-web-web-webkit-iphone-landscape.png](134751-web-web-webkit-iphone-landscape.png) |
| 13:47:51 | [134751-web-web-webkit-iphone-riding.png](134751-web-web-webkit-iphone-riding.png) |
| 13:47:51 | [134751-web-web-webkit-iphone-stopped.png](134751-web-web-webkit-iphone-stopped.png) |
| 13:47:51 | [134751-web-web-webkit-iphone.png](134751-web-web-webkit-iphone.png) |
| 13:47:51 | [134751-web-web-webkit-layout-android-360x640.png](134751-web-web-webkit-layout-android-360x640.png) |
| 13:47:51 | [134751-web-web-webkit-layout-android-640x360.png](134751-web-web-webkit-layout-android-640x360.png) |
| 13:47:51 | [134751-web-web-webkit-layout-iphone-390x844.png](134751-web-web-webkit-layout-iphone-390x844.png) |
| 13:47:51 | [134751-web-web-webkit-layout-iphone-844x390.png](134751-web-web-webkit-layout-iphone-844x390.png) |
| 13:47:51 | [134751-web-web-webkit-mac.png](134751-web-web-webkit-mac.png) |
| 13:56:38 | [135638-web-log-web-log-android-copy.png](135638-web-log-web-log-android-copy.png) |
| 13:56:38 | [135638-web-log-web-log-android-killed.png](135638-web-log-web-log-android-killed.png) |
| 13:56:38 | [135638-web-log-web-log-android-no-gpu-log.png](135638-web-log-web-log-android-no-gpu-log.png) |
| 13:56:38 | [135638-web-log-web-log-android-no-wasm-log.png](135638-web-log-web-log-android-no-wasm-log.png) |
| 13:56:38 | [135638-web-log-web-log-android-reload.png](135638-web-log-web-log-android-reload.png) |
| 13:56:38 | [135638-web-log-web-log-android-ride.png](135638-web-log-web-log-android-ride.png) |
| 13:56:38 | [135638-web-log-web-log-android-taps.png](135638-web-log-web-log-android-taps.png) |
| 13:56:38 | [135638-web-log-web-log-android-too-old-log.png](135638-web-log-web-log-android-too-old-log.png) |
| 13:56:38 | [135638-web-log-web-log-iphone-copy.png](135638-web-log-web-log-iphone-copy.png) |
| 13:56:38 | [135638-web-log-web-log-iphone-killed.png](135638-web-log-web-log-iphone-killed.png) |
| 13:56:38 | [135638-web-log-web-log-iphone-no-wasm-log.png](135638-web-log-web-log-iphone-no-wasm-log.png) |
| 13:56:38 | [135638-web-log-web-log-iphone-reload.png](135638-web-log-web-log-iphone-reload.png) |
| 13:56:38 | [135638-web-log-web-log-iphone-ride.png](135638-web-log-web-log-iphone-ride.png) |
| 13:56:38 | [135638-web-log-web-log-iphone-taps.png](135638-web-log-web-log-iphone-taps.png) |
| 13:56:38 | [135638-web-log-web-log-iphone-too-old-log.png](135638-web-log-web-log-iphone-too-old-log.png) |
| 14:03:34 | [140334-f874a416-dirty-shot-ocw.jpg](140334-f874a416-dirty-shot-ocw.jpg) |
| 14:03:43 | [140343-f874a416-dirty-shot-wayland-ocw-wayland.jpg](140343-f874a416-dirty-shot-wayland-ocw-wayland.jpg) |
| 14:09:37 | [140937-web-bisect-web-bisect-android-base-early-log.png](140937-web-bisect-web-bisect-android-base-early-log.png) |
| 14:09:37 | [140937-web-bisect-web-bisect-android-base-photo-1.jpg](140937-web-bisect-web-bisect-android-base-photo-1.jpg) |
| 14:09:37 | [140937-web-bisect-web-bisect-android-base.png](140937-web-bisect-web-bisect-android-base.png) |
| 14:09:37 | [140937-web-bisect-web-bisect-android-ios-safe-early-log.png](140937-web-bisect-web-bisect-android-ios-safe-early-log.png) |
| 14:09:37 | [140937-web-bisect-web-bisect-android-ios-safe.png](140937-web-bisect-web-bisect-android-ios-safe.png) |
| 14:09:37 | [140937-web-bisect-web-bisect-android-noegui-early-log.png](140937-web-bisect-web-bisect-android-noegui-early-log.png) |
| 14:09:37 | [140937-web-bisect-web-bisect-android-noegui-photo-1.jpg](140937-web-bisect-web-bisect-android-noegui-photo-1.jpg) |
| 14:09:37 | [140937-web-bisect-web-bisect-android-noegui.png](140937-web-bisect-web-bisect-android-noegui.png) |
| 14:09:37 | [140937-web-bisect-web-bisect-android-nosee-early-log.png](140937-web-bisect-web-bisect-android-nosee-early-log.png) |
| 14:09:37 | [140937-web-bisect-web-bisect-android-nosee-photo-1.jpg](140937-web-bisect-web-bisect-android-nosee-photo-1.jpg) |
| 14:09:37 | [140937-web-bisect-web-bisect-android-nosee.png](140937-web-bisect-web-bisect-android-nosee.png) |
| 14:09:37 | [140937-web-bisect-web-bisect-android-pipelines-serial-early-log.png](140937-web-bisect-web-bisect-android-pipelines-serial-early-log.png) |
| 14:09:37 | [140937-web-bisect-web-bisect-android-pipelines-serial-photo-1.jpg](140937-web-bisect-web-bisect-android-pipelines-serial-photo-1.jpg) |
| 14:09:37 | [140937-web-bisect-web-bisect-android-pipelines-serial.png](140937-web-bisect-web-bisect-android-pipelines-serial.png) |
| 14:09:37 | [140937-web-bisect-web-bisect-iphone-base-early-log.png](140937-web-bisect-web-bisect-iphone-base-early-log.png) |
| 14:09:37 | [140937-web-bisect-web-bisect-iphone-base.png](140937-web-bisect-web-bisect-iphone-base.png) |
| 14:09:37 | [140937-web-bisect-web-bisect-iphone-frames-0-early-log.png](140937-web-bisect-web-bisect-iphone-frames-0-early-log.png) |
| 14:09:37 | [140937-web-bisect-web-bisect-iphone-frames-0.png](140937-web-bisect-web-bisect-iphone-frames-0.png) |
| 14:09:37 | [140937-web-bisect-web-bisect-iphone-frames-30-early-log.png](140937-web-bisect-web-bisect-iphone-frames-30-early-log.png) |
| 14:09:37 | [140937-web-bisect-web-bisect-iphone-frames-30.png](140937-web-bisect-web-bisect-iphone-frames-30.png) |
| 14:09:37 | [140937-web-bisect-web-bisect-iphone-ios-safe-early-log.png](140937-web-bisect-web-bisect-iphone-ios-safe-early-log.png) |
| 14:09:37 | [140937-web-bisect-web-bisect-iphone-ios-safe.png](140937-web-bisect-web-bisect-iphone-ios-safe.png) |
| 14:09:37 | [140937-web-bisect-web-bisect-iphone-killed-early-log.png](140937-web-bisect-web-bisect-iphone-killed-early-log.png) |
| 14:09:37 | [140937-web-bisect-web-bisect-iphone-killed.png](140937-web-bisect-web-bisect-iphone-killed.png) |
| 14:09:37 | [140937-web-bisect-web-bisect-iphone-noarrays-early-log.png](140937-web-bisect-web-bisect-iphone-noarrays-early-log.png) |
| 14:09:37 | [140937-web-bisect-web-bisect-iphone-noarrays.png](140937-web-bisect-web-bisect-iphone-noarrays.png) |
| 14:09:37 | [140937-web-bisect-web-bisect-iphone-noaudio-early-log.png](140937-web-bisect-web-bisect-iphone-noaudio-early-log.png) |
| 14:09:37 | [140937-web-bisect-web-bisect-iphone-noaudio.png](140937-web-bisect-web-bisect-iphone-noaudio.png) |
| 14:09:37 | [140937-web-bisect-web-bisect-iphone-noegui-early-log.png](140937-web-bisect-web-bisect-iphone-noegui-early-log.png) |
| 14:09:37 | [140937-web-bisect-web-bisect-iphone-noegui.png](140937-web-bisect-web-bisect-iphone-noegui.png) |
| 14:09:37 | [140937-web-bisect-web-bisect-iphone-nomsaa-early-log.png](140937-web-bisect-web-bisect-iphone-nomsaa-early-log.png) |
| 14:09:37 | [140937-web-bisect-web-bisect-iphone-nomsaa.png](140937-web-bisect-web-bisect-iphone-nomsaa.png) |
| 14:09:37 | [140937-web-bisect-web-bisect-iphone-nosee-early-log.png](140937-web-bisect-web-bisect-iphone-nosee-early-log.png) |
| 14:09:37 | [140937-web-bisect-web-bisect-iphone-nosee.png](140937-web-bisect-web-bisect-iphone-nosee.png) |
| 14:09:37 | [140937-web-bisect-web-bisect-iphone-noshadow-0-early-log.png](140937-web-bisect-web-bisect-iphone-noshadow-0-early-log.png) |
| 14:09:37 | [140937-web-bisect-web-bisect-iphone-noshadow-0.png](140937-web-bisect-web-bisect-iphone-noshadow-0.png) |
| 14:09:37 | [140937-web-bisect-web-bisect-iphone-noshadow-early-log.png](140937-web-bisect-web-bisect-iphone-noshadow-early-log.png) |
| 14:09:37 | [140937-web-bisect-web-bisect-iphone-noshadow.png](140937-web-bisect-web-bisect-iphone-noshadow.png) |
| 14:09:37 | [140937-web-bisect-web-bisect-iphone-nosky-early-log.png](140937-web-bisect-web-bisect-iphone-nosky-early-log.png) |
| 14:09:37 | [140937-web-bisect-web-bisect-iphone-nosky.png](140937-web-bisect-web-bisect-iphone-nosky.png) |
| 14:09:37 | [140937-web-bisect-web-bisect-iphone-novoice-early-log.png](140937-web-bisect-web-bisect-iphone-novoice-early-log.png) |
| 14:09:37 | [140937-web-bisect-web-bisect-iphone-novoice.png](140937-web-bisect-web-bisect-iphone-novoice.png) |
| 14:09:37 | [140937-web-bisect-web-bisect-iphone-photos-1-early-log.png](140937-web-bisect-web-bisect-iphone-photos-1-early-log.png) |
| 14:09:37 | [140937-web-bisect-web-bisect-iphone-photos-1-photo-1.jpg](140937-web-bisect-web-bisect-iphone-photos-1-photo-1.jpg) |
| 14:09:37 | [140937-web-bisect-web-bisect-iphone-photos-1-photofix-all-early-log.png](140937-web-bisect-web-bisect-iphone-photos-1-photofix-all-early-log.png) |
| 14:09:37 | [140937-web-bisect-web-bisect-iphone-photos-1-photofix-all.png](140937-web-bisect-web-bisect-iphone-photos-1-photofix-all.png) |
| 14:09:37 | [140937-web-bisect-web-bisect-iphone-photos-1-photofix-screen-early-log.png](140937-web-bisect-web-bisect-iphone-photos-1-photofix-screen-early-log.png) |
| 14:09:37 | [140937-web-bisect-web-bisect-iphone-photos-1-photofix-screen-photo-1.jpg](140937-web-bisect-web-bisect-iphone-photos-1-photofix-screen-photo-1.jpg) |
| 14:09:37 | [140937-web-bisect-web-bisect-iphone-photos-1-photofix-screen.png](140937-web-bisect-web-bisect-iphone-photos-1-photofix-screen.png) |
| 14:09:37 | [140937-web-bisect-web-bisect-iphone-photos-1-photofix-small-early-log.png](140937-web-bisect-web-bisect-iphone-photos-1-photofix-small-early-log.png) |
| 14:09:37 | [140937-web-bisect-web-bisect-iphone-photos-1-photofix-small-photo-1.jpg](140937-web-bisect-web-bisect-iphone-photos-1-photofix-small-photo-1.jpg) |
| 14:09:37 | [140937-web-bisect-web-bisect-iphone-photos-1-photofix-small.png](140937-web-bisect-web-bisect-iphone-photos-1-photofix-small.png) |
| 14:09:37 | [140937-web-bisect-web-bisect-iphone-photos-1.png](140937-web-bisect-web-bisect-iphone-photos-1.png) |
| 14:09:37 | [140937-web-bisect-web-bisect-iphone-pipelines-serial-early-log.png](140937-web-bisect-web-bisect-iphone-pipelines-serial-early-log.png) |
| 14:09:37 | [140937-web-bisect-web-bisect-iphone-pipelines-serial.png](140937-web-bisect-web-bisect-iphone-pipelines-serial.png) |
| 14:09:37 | [140937-web-bisect-web-bisect-iphone-plain-early-log.png](140937-web-bisect-web-bisect-iphone-plain-early-log.png) |
| 14:09:37 | [140937-web-bisect-web-bisect-iphone-plain.png](140937-web-bisect-web-bisect-iphone-plain.png) |
| 14:09:37 | [140937-web-bisect-web-bisect-iphone-shadowfix-hw2x2+near-noshadow-0-early-log.png](140937-web-bisect-web-bisect-iphone-shadowfix-hw2x2+near-noshadow-0-early-log.png) |
| 14:09:37 | [140937-web-bisect-web-bisect-iphone-shadowfix-hw2x2+near-noshadow-0.png](140937-web-bisect-web-bisect-iphone-shadowfix-hw2x2+near-noshadow-0.png) |
| 14:09:37 | [140937-web-bisect-web-bisect-iphone-shadowmap-1024-early-log.png](140937-web-bisect-web-bisect-iphone-shadowmap-1024-early-log.png) |
| 14:09:37 | [140937-web-bisect-web-bisect-iphone-shadowmap-1024.png](140937-web-bisect-web-bisect-iphone-shadowmap-1024.png) |
| 14:09:37 | [140937-web-bisect-web-bisect-iphone-shadowmap-512-noshadow-0-early-log.png](140937-web-bisect-web-bisect-iphone-shadowmap-512-noshadow-0-early-log.png) |
| 14:09:37 | [140937-web-bisect-web-bisect-iphone-shadowmap-512-noshadow-0.png](140937-web-bisect-web-bisect-iphone-shadowmap-512-noshadow-0.png) |
| 14:11:24 | [141124-traffic-junctions-after-10min.png](141124-traffic-junctions-after-10min.png) |
| 14:11:24 | [141124-traffic-junctions-before-10min.png](141124-traffic-junctions-before-10min.png) |
| 14:11:25 | [141125-traffic-junctions-after-60min.png](141125-traffic-junctions-after-60min.png) |
| 14:11:25 | [141125-traffic-junctions-before-60min.png](141125-traffic-junctions-before-60min.png) |
| 14:11:26 | [141126-traffic-junctions-compare-10min.png](141126-traffic-junctions-compare-10min.png) |
| 14:11:26 | [141126-traffic-junctions-compare-60min.png](141126-traffic-junctions-compare-60min.png) |
| 14:56:48 | [145648-ant-power-A-1-devices-list.png](145648-ant-power-A-1-devices-list.png) |
| 14:56:54 | [145654-ant-power-A-2-power-meter-page.png](145654-ant-power-A-2-power-meter-page.png) |
| 14:56:58 | [145658-ant-power-A-3-speed-cadence-page.png](145658-ant-power-A-3-speed-cadence-page.png) |
| 14:57:03 | [145703-ant-power-A-4-ride-hud.png](145703-ant-power-A-4-ride-hud.png) |
| 14:57:08 | [145708-ant-power-A-end.jpg](145708-ant-power-A-end.jpg) |
| 14:57:16 | [145716-ant-power-B-1-scan.png](145716-ant-power-B-1-scan.png) |
| 14:57:24 | [145724-ant-power-B-2-connected.png](145724-ant-power-B-2-connected.png) |
| 14:57:28 | [145728-ant-power-B-end.jpg](145728-ant-power-B-end.jpg) |
| 15:05:56 | [150556-6ba1cb74-dirty-shot-traffic-day-x11.jpg](150556-6ba1cb74-dirty-shot-traffic-day-x11.jpg) |
| 15:06:45 | [150645-6ba1cb74-dirty-shot-wayland-traffic-day-wayland.jpg](150645-6ba1cb74-dirty-shot-wayland-traffic-day-wayland.jpg) |
| 15:07:46 | [150746-6ba1cb74-dirty-shot-traffic-night-x11.jpg](150746-6ba1cb74-dirty-shot-traffic-night-x11.jpg) |
| 15:08:36 | [150836-6ba1cb74-dirty-shot-wayland-traffic-night-wayland.jpg](150836-6ba1cb74-dirty-shot-wayland-traffic-night-wayland.jpg) |
| 15:09:39 | [150939-6ba1cb74-dirty-shot-traffic-rain-x11.jpg](150939-6ba1cb74-dirty-shot-traffic-rain-x11.jpg) |
| 15:10:29 | [151029-6ba1cb74-dirty-shot-wayland-traffic-rain-wayland.jpg](151029-6ba1cb74-dirty-shot-wayland-traffic-rain-wayland.jpg) |
| 15:15:53 | [151553-6ba1cb74-dirty-video-traffic-dusk-rain-x11.jpg](151553-6ba1cb74-dirty-video-traffic-dusk-rain-x11.jpg) |
| 15:15:53 | [151553-6ba1cb74-dirty-video-traffic-dusk-rain-x11.mp4](151553-6ba1cb74-dirty-video-traffic-dusk-rain-x11.mp4) |
| 15:16:14 | [151614-6ba1cb74-dirty-video-wayland-traffic-day-wayland.jpg](151614-6ba1cb74-dirty-video-wayland-traffic-day-wayland.jpg) |
| 15:16:14 | [151614-6ba1cb74-dirty-video-wayland-traffic-day-wayland.mp4](151614-6ba1cb74-dirty-video-wayland-traffic-day-wayland.mp4) |
| 15:37:25 | [153725-f99daa2a-dirty-shot-ocw.jpg](153725-f99daa2a-dirty-shot-ocw.jpg) |
| 15:37:35 | [153735-f99daa2a-dirty-shot-wayland-ocw-wayland.jpg](153735-f99daa2a-dirty-shot-wayland-ocw-wayland.jpg) |
| 16:38:30 | [163830-after-merge-ant-power-A-1-devices-list.png](163830-after-merge-ant-power-A-1-devices-list.png) |
| 16:38:36 | [163836-after-merge-ant-power-A-2-power-meter-page.png](163836-after-merge-ant-power-A-2-power-meter-page.png) |
| 16:38:40 | [163840-after-merge-ant-power-A-3-speed-cadence-page.png](163840-after-merge-ant-power-A-3-speed-cadence-page.png) |
| 16:38:45 | [163845-after-merge-ant-power-A-4-ride-hud.png](163845-after-merge-ant-power-A-4-ride-hud.png) |
| 16:38:50 | [163850-after-merge-ant-power-A-end.jpg](163850-after-merge-ant-power-A-end.jpg) |
| 16:38:57 | [163857-after-merge-ant-power-B-1-scan.png](163857-after-merge-ant-power-B-1-scan.png) |
| 16:39:05 | [163905-after-merge-ant-power-B-2-connected.png](163905-after-merge-ant-power-B-2-connected.png) |
| 16:39:09 | [163909-after-merge-ant-power-B-end.jpg](163909-after-merge-ant-power-B-end.jpg) |
| 16:39:26 | [163926-after-merge-ant-fec-A-1-devices-fe-c-trainer.png](163926-after-merge-ant-fec-A-1-devices-fe-c-trainer.png) |
| 16:39:33 | [163933-after-merge-ant-fec-A-2-ride-erg-240w.png](163933-after-merge-ant-fec-A-2-ride-erg-240w.png) |
| 16:40:26 | [164026-after-merge-ant-fec-A-end.jpg](164026-after-merge-ant-fec-A-end.jpg) |
| 16:41:17 | [164117-after-merge-ant-fec-B-ride-erg.jpg](164117-after-merge-ant-fec-B-ride-erg.jpg) |
| 16:41:19 | [164119-after-merge-ant-fec-B-ride-erg.mp4](164119-after-merge-ant-fec-B-ride-erg.mp4) |
| 17:52:33 | [175233-b56d226a-dirty-video-wayland-ufo-unicorn-dusk-video.jpg](175233-b56d226a-dirty-video-wayland-ufo-unicorn-dusk-video.jpg) |
| 17:52:33 | [175233-b56d226a-dirty-video-wayland-ufo-unicorn-dusk-video.mp4](175233-b56d226a-dirty-video-wayland-ufo-unicorn-dusk-video.mp4) |
| 17:53:54 | [175354-b56d226a-dirty-video-wayland-ufo-crop-circle-video.jpg](175354-b56d226a-dirty-video-wayland-ufo-crop-circle-video.jpg) |
| 17:53:54 | [175354-b56d226a-dirty-video-wayland-ufo-crop-circle-video.mp4](175354-b56d226a-dirty-video-wayland-ufo-crop-circle-video.mp4) |
| 17:55:02 | [175502-b56d226a-dirty-video-wayland-ufo-crop-circle-morning.jpg](175502-b56d226a-dirty-video-wayland-ufo-crop-circle-morning.jpg) |
| 17:55:02 | [175502-b56d226a-dirty-video-wayland-ufo-crop-circle-morning.mp4](175502-b56d226a-dirty-video-wayland-ufo-crop-circle-morning.mp4) |
| 17:57:27 | [175727-b56d226a-dirty-video-wayland-ufo-cow-beam-video.jpg](175727-b56d226a-dirty-video-wayland-ufo-cow-beam-video.jpg) |
| 17:57:27 | [175727-b56d226a-dirty-video-wayland-ufo-cow-beam-video.mp4](175727-b56d226a-dirty-video-wayland-ufo-cow-beam-video.mp4) |
| 17:57:52 | [175752-b56d226a-dirty-video-wayland-ufo-night-sighting.jpg](175752-b56d226a-dirty-video-wayland-ufo-night-sighting.jpg) |
| 17:57:52 | [175752-b56d226a-dirty-video-wayland-ufo-night-sighting.mp4](175752-b56d226a-dirty-video-wayland-ufo-night-sighting.mp4) |
| 18:00:22 | [180022-b56d226a-dirty-video-wayland-ufo-unicorn-dusk-video.jpg](180022-b56d226a-dirty-video-wayland-ufo-unicorn-dusk-video.jpg) |
| 18:00:22 | [180022-b56d226a-dirty-video-wayland-ufo-unicorn-dusk-video.mp4](180022-b56d226a-dirty-video-wayland-ufo-unicorn-dusk-video.mp4) |
| 18:02:37 | [180237-b56d226a-dirty-video-wayland-ufo-crop-circle-video.jpg](180237-b56d226a-dirty-video-wayland-ufo-crop-circle-video.jpg) |
| 18:02:37 | [180237-b56d226a-dirty-video-wayland-ufo-crop-circle-video.mp4](180237-b56d226a-dirty-video-wayland-ufo-crop-circle-video.mp4) |
| 18:03:50 | [180350-b56d226a-dirty-video-wayland-ufo-crop-circle-morning.jpg](180350-b56d226a-dirty-video-wayland-ufo-crop-circle-morning.jpg) |
| 18:03:50 | [180350-b56d226a-dirty-video-wayland-ufo-crop-circle-morning.mp4](180350-b56d226a-dirty-video-wayland-ufo-crop-circle-morning.mp4) |
| 18:05:45 | [180545-b56d226a-dirty-video-wayland-ufo-cow-beam-video.jpg](180545-b56d226a-dirty-video-wayland-ufo-cow-beam-video.jpg) |
| 18:05:45 | [180545-b56d226a-dirty-video-wayland-ufo-cow-beam-video.mp4](180545-b56d226a-dirty-video-wayland-ufo-cow-beam-video.mp4) |
| 18:06:06 | [180606-b56d226a-dirty-video-wayland-ufo-night-sighting.jpg](180606-b56d226a-dirty-video-wayland-ufo-night-sighting.jpg) |
| 18:06:06 | [180606-b56d226a-dirty-video-wayland-ufo-night-sighting.mp4](180606-b56d226a-dirty-video-wayland-ufo-night-sighting.mp4) |
| 18:07:56 | [180756-b56d226a-dirty-video-wayland-ufo-unicorn-dusk-video.jpg](180756-b56d226a-dirty-video-wayland-ufo-unicorn-dusk-video.jpg) |
| 18:07:56 | [180756-b56d226a-dirty-video-wayland-ufo-unicorn-dusk-video.mp4](180756-b56d226a-dirty-video-wayland-ufo-unicorn-dusk-video.mp4) |
| 18:09:33 | [180933-b56d226a-dirty-video-wayland-ufo-crop-circle-video.jpg](180933-b56d226a-dirty-video-wayland-ufo-crop-circle-video.jpg) |
| 18:09:33 | [180933-b56d226a-dirty-video-wayland-ufo-crop-circle-video.mp4](180933-b56d226a-dirty-video-wayland-ufo-crop-circle-video.mp4) |
| 18:10:35 | [181035-b56d226a-dirty-video-wayland-ufo-crop-circle-morning.jpg](181035-b56d226a-dirty-video-wayland-ufo-crop-circle-morning.jpg) |
| 18:10:35 | [181035-b56d226a-dirty-video-wayland-ufo-crop-circle-morning.mp4](181035-b56d226a-dirty-video-wayland-ufo-crop-circle-morning.mp4) |
| 18:12:46 | [181246-b56d226a-dirty-video-wayland-ufo-cow-beam-video.jpg](181246-b56d226a-dirty-video-wayland-ufo-cow-beam-video.jpg) |
| 18:12:46 | [181246-b56d226a-dirty-video-wayland-ufo-cow-beam-video.mp4](181246-b56d226a-dirty-video-wayland-ufo-cow-beam-video.mp4) |
| 18:16:54 | [181654-b56d226a-dirty-video-wayland-ufo-unicorn-dusk-video.jpg](181654-b56d226a-dirty-video-wayland-ufo-unicorn-dusk-video.jpg) |
| 18:16:54 | [181654-b56d226a-dirty-video-wayland-ufo-unicorn-dusk-video.mp4](181654-b56d226a-dirty-video-wayland-ufo-unicorn-dusk-video.mp4) |
| 18:18:37 | [181837-b56d226a-dirty-video-wayland-ufo-crop-circle-video.mp4](181837-b56d226a-dirty-video-wayland-ufo-crop-circle-video.mp4) |
| 18:18:51 | [181851-b56d226a-dirty-video-wayland-ufo-unicorn-dusk-video.jpg](181851-b56d226a-dirty-video-wayland-ufo-unicorn-dusk-video.jpg) |
| 18:18:51 | [181851-b56d226a-dirty-video-wayland-ufo-unicorn-dusk-video.mp4](181851-b56d226a-dirty-video-wayland-ufo-unicorn-dusk-video.mp4) |
| 18:19:44 | [181944-b56d226a-dirty-video-wayland-ufo-crop-circle-morning.jpg](181944-b56d226a-dirty-video-wayland-ufo-crop-circle-morning.jpg) |
| 18:19:44 | [181944-b56d226a-dirty-video-wayland-ufo-crop-circle-morning.mp4](181944-b56d226a-dirty-video-wayland-ufo-crop-circle-morning.mp4) |
| 18:22:05 | [182205-b56d226a-dirty-video-wayland-ufo-cow-beam-video.jpg](182205-b56d226a-dirty-video-wayland-ufo-cow-beam-video.jpg) |
| 18:22:05 | [182205-b56d226a-dirty-video-wayland-ufo-cow-beam-video.mp4](182205-b56d226a-dirty-video-wayland-ufo-cow-beam-video.mp4) |
| 18:23:00 | [182300-t9-ufo-ufo-cow-beam.jpg](182300-t9-ufo-ufo-cow-beam.jpg) |
| 18:23:00 | [182300-t9-ufo-ufo-crop-circle-night.jpg](182300-t9-ufo-ufo-crop-circle-night.jpg) |
| 18:25:17 | [182517-b56d226a-dirty-video-wayland-ufo-unicorn-dusk-video.jpg](182517-b56d226a-dirty-video-wayland-ufo-unicorn-dusk-video.jpg) |
| 18:25:17 | [182517-b56d226a-dirty-video-wayland-ufo-unicorn-dusk-video.mp4](182517-b56d226a-dirty-video-wayland-ufo-unicorn-dusk-video.mp4) |
| 18:28:30 | [182830-bus18b-bus-stop-doors-day-wayland.jpg](182830-bus18b-bus-stop-doors-day-wayland.jpg) |
| 18:28:30 | [182830-bus18b-bus-stop-doors-day-x11.jpg](182830-bus18b-bus-stop-doors-day-x11.jpg) |
| 18:28:30 | [182830-bus18b-parked-cars-street-day-wayland.jpg](182830-bus18b-parked-cars-street-day-wayland.jpg) |
| 18:28:30 | [182830-bus18b-parked-cars-street-day-x11.jpg](182830-bus18b-parked-cars-street-day-x11.jpg) |
| 18:31:24 | [183124-b56d226a-dirty-video-wayland-ufo-unicorn-dusk-video.jpg](183124-b56d226a-dirty-video-wayland-ufo-unicorn-dusk-video.jpg) |
| 18:31:24 | [183124-b56d226a-dirty-video-wayland-ufo-unicorn-dusk-video.mp4](183124-b56d226a-dirty-video-wayland-ufo-unicorn-dusk-video.mp4) |
| 18:31:52 | [183152-b56d226a-dirty-video-wayland-ufo-night-sighting.jpg](183152-b56d226a-dirty-video-wayland-ufo-night-sighting.jpg) |
| 18:31:52 | [183152-b56d226a-dirty-video-wayland-ufo-night-sighting.mp4](183152-b56d226a-dirty-video-wayland-ufo-night-sighting.mp4) |
| 18:33:10 | [183310-t9-ufo-ufo-unicorn-dusk.jpg](183310-t9-ufo-ufo-unicorn-dusk.jpg) |
| 19:09:19 | [190919-894edf69-dirty-shot-wayland-air-live-tenerife.jpg](190919-894edf69-dirty-shot-wayland-air-live-tenerife.jpg) |
| 19:10:05 | [191005-894edf69-dirty-shot-wayland-air-live-blackforest.jpg](191005-894edf69-dirty-shot-wayland-air-live-blackforest.jpg) |
| 19:10:36 | [191036-894edf69-dirty-shot-wayland-air-dusk-lights-close.jpg](191036-894edf69-dirty-shot-wayland-air-dusk-lights-close.jpg) |
| 19:12:58 | [191258-894edf69-dirty-shot-wayland-air-live-tenerife.jpg](191258-894edf69-dirty-shot-wayland-air-live-tenerife.jpg) |
| 19:13:52 | [191352-bus18b-bus-stop-video-wayland.mp4](191352-bus18b-bus-stop-video-wayland.mp4) |
| 19:14:49 | [191449-894edf69-dirty-shot-wayland-air-live-blackforest.jpg](191449-894edf69-dirty-shot-wayland-air-live-blackforest.jpg) |
| 19:22:22 | [192222-894edf69-dirty-shot-wayland-air-dusk-lights-close.jpg](192222-894edf69-dirty-shot-wayland-air-dusk-lights-close.jpg) |
| 19:23:27 | [192327-894edf69-dirty-shot-wayland-air-live-tenerife.jpg](192327-894edf69-dirty-shot-wayland-air-live-tenerife.jpg) |
| 19:24:03 | [192403-894edf69-dirty-shot-wayland-air-live-blackforest.jpg](192403-894edf69-dirty-shot-wayland-air-live-blackforest.jpg) |
| 19:24:31 | [192431-894edf69-dirty-shot-wayland-air-dusk-lights-close.jpg](192431-894edf69-dirty-shot-wayland-air-dusk-lights-close.jpg) |
| 21:22:20 | [212220-86d14255-shot-wayland-air-live-credit-hud.jpg](212220-86d14255-shot-wayland-air-live-credit-hud.jpg) |
| 21:22:47 | [212247-86d14255-shot-wayland-air-live-credit-small.jpg](212247-86d14255-shot-wayland-air-live-credit-small.jpg) |
| 21:24:31 | [212431-86d14255-dirty-shot-wayland-air-live-credit-hud.jpg](212431-86d14255-dirty-shot-wayland-air-live-credit-hud.jpg) |
| 21:24:59 | [212459-86d14255-dirty-shot-wayland-air-live-credit-small.jpg](212459-86d14255-dirty-shot-wayland-air-live-credit-small.jpg) |
| 22:17:45 | [221745-web-log-web-log-android-copy.png](221745-web-log-web-log-android-copy.png) |
| 22:17:45 | [221745-web-log-web-log-android-killed.png](221745-web-log-web-log-android-killed.png) |
| 22:17:45 | [221745-web-log-web-log-android-no-gpu-log.png](221745-web-log-web-log-android-no-gpu-log.png) |
| 22:17:45 | [221745-web-log-web-log-android-no-wasm-log.png](221745-web-log-web-log-android-no-wasm-log.png) |
| 22:17:45 | [221745-web-log-web-log-android-no-wasm.png](221745-web-log-web-log-android-no-wasm.png) |
| 22:17:45 | [221745-web-log-web-log-android-reload.png](221745-web-log-web-log-android-reload.png) |
| 22:17:45 | [221745-web-log-web-log-android-retry-abort.png](221745-web-log-web-log-android-retry-abort.png) |
| 22:17:45 | [221745-web-log-web-log-android-retry-half.png](221745-web-log-web-log-android-retry-half.png) |
| 22:17:45 | [221745-web-log-web-log-android-ride.png](221745-web-log-web-log-android-ride.png) |
| 22:17:45 | [221745-web-log-web-log-android-taps.png](221745-web-log-web-log-android-taps.png) |
| 22:17:45 | [221745-web-log-web-log-android-too-old-log.png](221745-web-log-web-log-android-too-old-log.png) |
| 22:17:45 | [221745-web-log-web-log-iphone-copy.png](221745-web-log-web-log-iphone-copy.png) |
| 22:17:45 | [221745-web-log-web-log-iphone-killed.png](221745-web-log-web-log-iphone-killed.png) |
| 22:17:45 | [221745-web-log-web-log-iphone-no-wasm-log.png](221745-web-log-web-log-iphone-no-wasm-log.png) |
| 22:17:45 | [221745-web-log-web-log-iphone-no-wasm.png](221745-web-log-web-log-iphone-no-wasm.png) |
| 22:17:45 | [221745-web-log-web-log-iphone-reload.png](221745-web-log-web-log-iphone-reload.png) |
| 22:17:45 | [221745-web-log-web-log-iphone-retry-abort.png](221745-web-log-web-log-iphone-retry-abort.png) |
| 22:17:45 | [221745-web-log-web-log-iphone-retry-half.png](221745-web-log-web-log-iphone-retry-half.png) |
| 22:17:45 | [221745-web-log-web-log-iphone-ride.png](221745-web-log-web-log-iphone-ride.png) |
| 22:17:45 | [221745-web-log-web-log-iphone-taps.png](221745-web-log-web-log-iphone-taps.png) |
| 22:17:45 | [221745-web-log-web-log-iphone-too-old-log.png](221745-web-log-web-log-iphone-too-old-log.png) |
| 23:16:10 | [231610-web-load-2026-11-28-web-webkit-world-liechtenstein.png](231610-web-load-2026-11-28-web-webkit-world-liechtenstein.png) |
| 23:21:30 | [232130-fly-traffic-reset-first.jpg](232130-fly-traffic-reset-first.jpg) |
| 23:21:30 | [232130-fly-traffic-reset-second.jpg](232130-fly-traffic-reset-second.jpg) |
| 23:25:30 | [232530-fly-traffic-reset-rejoin-second.jpg](232530-fly-traffic-reset-rejoin-second.jpg) |
| 23:27:23 | [232723-fly-traffic-reset-first.jpg](232723-fly-traffic-reset-first.jpg) |
| 23:27:23 | [232723-fly-traffic-reset-second.jpg](232723-fly-traffic-reset-second.jpg) |
| 23:53:51 | [235351-web-load-2026-11-28-andorra-new4-end.png](235351-web-load-2026-11-28-andorra-new4-end.png) |
| 23:53:51 | [235351-web-load-2026-11-28-andorra-new4-start.png](235351-web-load-2026-11-28-andorra-new4-start.png) |
| 23:54:18 | [235418-web-load-2026-11-28-tenerife-new4-end.png](235418-web-load-2026-11-28-tenerife-new4-end.png) |
| 23:54:18 | [235418-web-load-2026-11-28-tenerife-new4-start.png](235418-web-load-2026-11-28-tenerife-new4-start.png) |
