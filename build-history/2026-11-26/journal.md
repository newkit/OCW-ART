# OCW build diary – day 16, 2026-11-26

113 commits (36 merges), +38985 / −1517 lines, 247 images, 6 videos, 1 sounds.

## Commits

| Time | Commit | |
|---|---|---|
| 04:40 | `5e482567` | Studio asks before loading the patch next to a package (16H Q16 (b)) |
| 04:41 | `e949f664` | Build package: patched/ next to the package, a build recipe with each official package for the full chain (16H Q17 (a)) |
| 04:42 | `f8a8c25f` | Road edits act on the whole OSM way by default, the edge as the switch (16H Q18 (a)) |
| 04:44 | `01f783f4` | The game lists the studio's saved routes next to the package and in the data dir; documented in the README (16H Q19 (a)) |
| 04:54 | `56870075` | Fixed: OCW Studio's 2D map draws the land use again – its texture is made in the egui context that draws the map (16A Fixed; spec 6.03) |
| 05:41 | `19694296` (merge) | Merge the land-use fix for the studio's 2D map: the texture is made again in the egui context that draws it, never above the largest texture side (6.07) |
| 05:47 | `3997a6d7` | Built: the game's route list offers the studio's routes next to the package and in the data dir, marked yours; Save route falls back to the data dir; README documents it (16H Q19 (a), v6.07) |
| 06:11 | `72db9890` (merge) | Merge the user's routes in the game's list: next to the package and in the data dir, marked yours; the studio's save fallback; README (16H Q19 (a); 6.08) |
| 07:16 | `b49743e8` | OCW Studio asks before loading the patch next to a package, Build package runs the package's build recipe, road edits act on the whole OSM way by default (16H Q16 (b), Q17 (a), Q18 (a); spec 6.09) |
| 07:40 | `73941c84` | Planner settings stay separate: the studio's planner.json, the game's own later (16H Q20 (b)) |
| 07:43 | `34b1dab5` | BRouter consent remembered per server (16H Q21 (a)) |
| 07:44 | `03e4f45d` | Own BRouter on marge for the planner tests, data from our extracts (16H Q22 (a)) |
| 07:45 | `5c74de2f` (merge) | Merge the studio's patch question, build recipes and whole-way road edits (16H Q16 (b), Q17 (a), Q18 (a); 6.12) |
| 07:51 | `fc80aa9f` | Imported tracks keep a via-point every kilometre, as built (16H Q23 (a)) |
| 08:46 | `9943c7af` | BRouter consent asked once per server and remembered; planner tests on our own BRouter built from our extract (16H Q21 (a), Q22 (a); 6.14) |
| 08:59 | `1d001b90` | Base parts included with accounts (Phase 4 Q18 (a)) |
| 09:01 | `08e67ac1` | Hearts: signed servers credit directly, other rides via the checked ride summary (Phase 4 Q19 (a)) |
| 09:02 | `3d17a923` | Offline riding with the last synced bikes and kit, read-only, ride credited later (Phase 4 Q20 (a)) |
| 09:03 | `f62c5492` | Accounts start fresh with 5,000 hearts, local test wallets not imported (Phase 4 Q21 (a)) |
| 09:16 | `2372e833` | Prepared: ocw-server with its bundled voice server on Fly.io, one always-on machine in fra (11.5; 6.18) |
| 09:22 | `8c4ec441` (merge) | Merge BRouter: the via-point question remembered per server, our own BRouter on marge for the planner tests (16H Q21 (a), Q22 (a); 6.18) |
| 09:24 | `ba5e986c` (merge) | Merge the Fly.io hosting setup for ocw-server with its bundled voice server: Dockerfile, fly.toml, start script, README and spec 11.5 (not deployed yet: Fly needs a card for the dedicated IPv4; 6.19) |
| 09:57 | `5cde9248` | Built: accounts backend on PostgreSQL with the workshop, hearts ledger and ride credits (14 Phase 4, 4O; Q18-Q21 backend; 6.19) |
| 10:12 | `d04fe46e` | Fly.io budget: at most $10 a month for the hosted server (11.5; 6.20) |
| 10:36 | `3193fd15` | Official builds fail on a vanished patch target (--strict-patch), users' builds warn (16H Q7 (a)) |
| 10:39 | `f5c0612b` | Studio camera views stored in the world patch file (16H Q13 (b)) |
| 10:42 | `3505028f` | A road closed for bikes stays drawn and rideable, with warning signs at its ends (16H Q6) |
| 10:52 | `b911da34` | Spec Phase 10 Q11 elaborated: why the bridge matters on Apple devices, who is affected, group rides need WebTransport too, an example |
| 10:56 | `bcd7c4f7` (merge) | Merge the accounts backend on PostgreSQL: inventory, the hearts ledger, purchases and sales, signed-server credits and checked ride summaries (4O part 1; Phase 4 Q18-Q21 in the backend; 6.23) |
| 10:57 | `f18e1d4b` | WIP: the desktop's workshop on the account, offline queue, server ride credits (4O part 2) |
| 10:57 | `225de8e7` (merge) | Merge remote-tracking branch 'origin/main' into worktree-agent-ae9ce66a8776a5e06 |
| 11:01 | `2f80984f` | Sensor bridge on iOS before 26.4: ask to update, for now (Phase 10 Q11 (a)) |
| 11:10 | `661719a4` | WIP: studio signing, strict patch, views in patch, closed-for-bikes signs, binding filter |
| 11:10 | `52d0d9bc` (merge) | Merge origin/main |
| 11:10 | `d6f92474` | WIP: virtual brake at most 5 m/s², client tests on a fixed clock and seed |
| 11:10 | `c37c17f8` (merge) | Merge origin/main |
| 11:17 | `d3c1cea8` | Plan traffic as a Settings switch: simulated road traffic, aircraft and UFOs; live aircraft from adsb.lol, no live road data (14 Phase 18, 6.25) |
| 11:18 | `280f8620` (merge) | Merge the traffic plan: Phase 18 – cars, lorries, motorbikes, aircraft and UFOs; live data sources researched; 10 open questions (6.25) |
| 11:38 | `cf128e15` | Traffic: defaults, group-ride choice, car plans; cars can hit riders, and a lunatic mode (Phase 18 Q1-Q4) |
| 11:39 | `b09100db` | Live road data: a switch now, data once a suitable source exists; research continues (Phase 18 Q5) |
| 11:41 | `2d783aff` | Live aircraft from adsb.lol as an opt-in, OpenSky as fallback (Phase 18 Q6) |
| 11:42 | `14a7943c` | UFOs around the unicorn and rare night sightings (Phase 18 Q7 (b)) |
| 11:42 | `53f0ce28` | UFOs with all three: the unicorn, night sightings, crop circles and the cow (Phase 18 Q7 (c)) |
| 11:44 | `4750e5dd` | Driver manners selectable in the traffic settings (Phase 18 Q8) |
| 11:45 | `59b2051e` | Traffic on every device, fewer vehicles by quality level (Phase 18 Q9 (a)) |
| 11:46 | `5ee57d5d` | Road traffic only on the desktop, aircraft everywhere (Phase 18 Q9 (b), corrected) |
| 11:47 | `5024a6c1` | Traffic priority: after the work in progress, simulated road traffic and aircraft first (Phase 18 Q10 (a)) |
| 11:51 | `de06f5e4` | Fixed: the virtual brake of autodrive sheds speed at most 5 m/s², so prediction error no longer brakes the own rider 3-4 m/s on the client; group bump test deterministic (6.25) |
| 11:51 | `6ba7b19b` | ANT+ key entered by the user, not shipped, for now (Phase 17 Q1 (b)) |
| 11:52 | `a8c27d55` | Live road data: the DGT incident feed suits Tenerife now; live density only behind a registration (Phase 18 Q5 research, new Q11) |
| 11:52 | `73181477` | ANT+: build without hardware, the stick test postponed (Phase 17 Q2) |
| 11:52 | `df4e9f4b` | Built: signed in, the desktop's workshop is the account's; rides queued offline and credited once; certified game servers credit hearts at a ride's end (4O part 2; Q19 (a), Q20 (a); 6.24) |
| 11:53 | `372aad1f` (merge) | Merge remote-tracking branch 'origin/main' into worktree-agent-ae9ce66a8776a5e06 |
| 11:53 | `f6bebe49` (merge) | Merge the live road-data research: the DGT incident feed suits Tenerife now; Swiss and German live counts need registration (Phase 18 18D, new Q11; 6.37) |
| 11:54 | `460d2aca` | ANT+ on the desktop first, in the browser via the bridge and WebUSB (Phase 17 Q3) |
| 11:57 | `a21f17df` | Live road data: register for opentransportdata.swiss and Mobilithek too (Phase 18 Q11 (b), (c)) |
| 12:01 | `27eab829` | Fixed: the chin-strap beard lies on the jaw line from ear to ear, and the stubble beards leave the lips free, also while speaking (4N Fixed) |
| 12:02 | `6402f53f` (merge) | Merge origin/main (the beard fix renumbered 6.40) |
| 12:42 | `fcf55f13` (merge) | Merge the fix of the flaky prediction test: the virtual brake sheds speed at a hard stop's rate (5 m/s²) on server and client alike; client tests on a fixed clock and weather seed (6.40) |
| 12:52 | `98c46a0a` | ANT+ now; heart rate first, power and FE-C planned too; straps picked by hand (Phase 17 Q4 (b), Q5, Q6 (c)) |
| 13:03 | `77fff69b` | Fixed: no white panels on the bikes – deep rims, disc wheel and down tube show rim colour and paint (6.40) |
| 13:18 | `6b4be99c` | Built: the browser app has the desktop's workshop on the signed-in rider's account, purchases without blocking the page, the workshop kept for offline, rides queued for the account; anonymous riders stay locked (4O part 3, W5c in the browser, B6 parity; 6.38) |
| 13:21 | `e281a2a2` (merge) | Merge remote-tracking branch 'origin/main' into worktree-agent-ae9ce66a8776a5e06 |
| 13:28 | `197286d3` | Built: repairs on the account at the local garage's prices with the ride's damage kept there, and game servers that count only the parts a signed-in rider owns (4O part 4: W5d's BikeChange ownership check, W6 with accounts; 6.44) |
| 13:40 | `3b8daab1` | Built: the rider is the account's – name, weight, height, FTP, bike profile, character and kit look kept with the account, the same on every computer and in the browser, its name unique on the backend (4O part 5, W5b; 6.45) |
| 13:45 | `394f5ff4` (merge) | Merge accounts part 2: signed in, the desktop's workshop is the account's; rides queued offline and credited once; certified game servers credit hearts at a ride's end (4O part 2; Q19 (a), Q20 (a); 6.42) |
| 13:45 | `0243bd91` (merge) | Merge accounts parts 3 and 4: the browser's workshop on the account (the workshop moved into ocw-ui), repairs with accounts and the game server's ownership check (4O; 6.43, 6.44) |
| 13:47 | `6b811538` | remote.sh: delete files removed or moved away here in the machines' checkouts too |
| 13:50 | `b415979d` | OCW Studio signs its builds with the user's own key; strict patches for official builds; views in the patch; closed-for-bikes roads stay rideable with warning signs; N / Z in the studio (4.21 item, 16H Q6, Q7 (a), Q13 (b); 6.25) |
| 14:03 | `826a7174` | Deployed: ocw-server with its voice server on Fly.io, voice from https pages over wss://ocw-server.fly.dev, Fly.io budget at most $16 a month (11.5; 6.25) |
| 14:03 | `59a7da04` (merge) | Merge origin/main into the Fly.io deployment branch (the version row renumbered to 6.43) |
| 14:09 | `4cdea4f1` | Fly.io (11.5; 6.43): Chromium's WebTransport handshake to the Fly server fails 3 of 4 times, recorded as open |
| 14:10 | `fdd25b8c` (merge) | Merge: no white label panels on rims and down tubes – removed from the bike generator, all six bike files re-exported (6.45) |
| 14:10 | `40385e02` (merge) | Merge: the chin-strap beard lies on the jaw line, the stubble beards leave the lips free (4N; 6.46) |
| 14:11 | `a471203b` (merge) | Merge OCW Studio: built packages signed with the user's own key, N/Z without console noise, --strict-patch, camera views in the patch, roads closed for bikes stay rideable with warning signs (4.21, 16H Q6, Q7, Q13; 6.47) |
| 14:28 | `51a7d006` (merge) | Merge remote-tracking branch 'origin/main' into worktree-agent-ae9ce66a8776a5e06 |
| 14:55 | `1f9ba6da` | Spec 6.43, CLAUDE.md: remote.sh deletes stale files on the build machines (11.2 Stale files) |
| 15:09 | `31585b16` (merge) | Merge main (accounts parts 3 and 4) into the combined merge |
| 15:22 | `aed18ae0` (merge) | Merge the remote.sh fix: the build machines' checkouts drop files git no longer tracks, on Linux, macOS and Windows (11.2; 6.48) |
| 15:41 | `8b650fed` | ANT+ heart rate for the desktop app, built without hardware (spec 14 Phase 17 A1-A3, 6.42) |
| 16:05 | `fa289dcd` (merge) | Merge origin/main into the Fly.io deployment branch (the Fly row renumbered to 6.48) |
| 16:38 | `e8bdb186` | Fifth world: Andorra – the whole country in one package with four climbs and Andorra's own estimates (6.42) |
| 16:46 | `f3f2d963` (merge) | Merge agent/vr-x1 onto main: PC VR in the desktop app (OpenXR, --vr, --vr-sim, vr command, quality vr) sharing the bike computer, controller mapping, eye projection and camera look with WebXR (spec 6.48, 14 Phase 11 X1, 11J) |
| 16:47 | `2482a3fe` (merge) | Merge accounts part 5: the rider is the account's – name, weight, height, FTP, bike and look kept with the account, unique names, both apps riding it when signed in (4O W5b; 6.49) |
| 16:47 | `6365e44f` (merge) | Merge ANT+ heart rate for the desktop app, built without hardware: decoding, the stick service with a simulated stick, the Devices page with the key entry (Phase 17 A1-A3; 6.50) |
| 16:47 | `df7f8b67` (merge) | Merge the fifth world, Andorra: built like the others with all estimates, four climbs (Envalira, Arcalís, Coll d'Ordino, Coll de la Gallina) (6.51) |
| 16:48 | `21e22b82` (merge) | Merge PC VR onto main: OpenXR in the desktop app (the agent/vr-x1 branch), sharing the session, bike computer, controllers and eye projection with WebXR (Phase 11 X1; 6.52) |
| 17:12 | `ffb61848` | Fixed: browsers join the Fly.io server reliably – a WebTransport handshake without an answer is tried again on a new connection (a new UDP flow), up to 3 more times (11.5 Lost UDP flows; 6.49) |
| 17:13 | `affc26c0` (merge) | Merge origin/main into the Fly.io branch (the Fly rows renumbered to 6.49 and 6.50) |
| 17:24 | `ba69b807` (merge) | Merge the Fly.io server: ocw-server with its voice server deployed (--no-gso, --no-mtu-discovery, wss:// on 443), and browsers retrying a lost WebTransport handshake on a new UDP flow (11.5; 6.53, 6.54) |
| 18:15 | `d491f70d` | Andorra within its border for now; Andorra on the live page (4.7 Q1) |
| 19:02 | `50e0ac45` | README: Andorra in the Worlds gallery – the Port d'Envalira in January snow and Andorra la Vella; scenes readme-andorra-* to render them again |
| 19:03 | `bdb142fc` (merge) | Merge the Andorra artwork: README Worlds with five regions and an Andorra row (Envalira in winter, Andorra la Vella), credits for Sentinel-2 and the forest layers; eight readme-andorra scenes |
| 19:05 | `6850ec17` | Riding together on the public page: the preview joins the Fly.io server with voice, learning its certificate hashes at runtime (11.5 Join info; 6.56) |
| 19:12 | `de4139f4` | Preview start page: the lead names riding together on the public server (11.5 Join info) |
| 19:13 | `c11db780` (merge) | Merge riding together on the public page: the Fly server's join info (/join.json with the current and next certificate hashes), voice over wss, the start page's Ride together (11.5, B8a; 6.56) |
| 20:34 | `84d86b07` | The public server keeps logging joins with name and IP (decision) |
| 21:02 | `fd113570` | ANT stick on Linux: a pkexec helper installs the udev rule (Phase 17 Q8 (b)) |
| 21:08 | `516c26d1` | No COM-port route for ANT sticks on Windows; proposed: drive Garmin's libusb-win32 driver (Phase 17 Q7 research) |
| 21:29 | `59244c25` | ANT stick on Windows through Garmin's libusb-win32 driver, Zadig as fallback (Phase 17 Q7 (d)) |
| 21:29 | `562b6ebb` | Spec: the Q7 decision row is 6.60 (6.59 was taken by the research row) |
| 21:43 | `324b5d71` | PC VR menu: the WebXR panel, shared (Phase 11 Q11 (a)) |
| 21:44 | `e62294d6` | VR bike computer between the TT extensions (Phase 11 Q12 (c)) |
| 21:45 | `34eac71b` | VR: the fitted computer part becomes the VR bike computer (Phase 11 Q13 (b)) |
| 21:52 | `fedfa78b` | ANT stick on Windows through Garmin's libusb-win32 driver; Linux access rule through pkexec (Phase 17 Q7 (d), Q8 (b)) |
| 21:59 | `42e87345` | VR kiosk: local server for now, ocw-server with bots once it runs again (Phase 11 Q14) |
| 22:42 | `3174ba08` | ANT+ driver / access pages: in the desktop page list, notes short enough for a 16:9 page |
| 22:53 | `bdb1f14b` | Lakes and rivers follow their OSM outlines, water material, far forests, alpine ground, no phantom pylons (spec 4.6.3, v6.58) |
| 23:05 | `1b560575` | Status page for the Fly.io server: / for browsers, /stats.json, counts only (spec 11.5) |
| 23:23 | `1dde18f3` | Status page deployed on Fly (release v6): checks recorded (spec 11.5) |
| 23:29 | `733ca32d` (merge) | Merge the Fly server's public status page (/ and /stats.json, counts only) (11.5; 6.65) |
| 23:29 | `22d76884` (merge) | Merge ANT+ access: Garmin's libusb-win32 driver on Windows (WinUSB first, then libusb0), the pkexec udev helper on Linux (Phase 17 Q7 (d), Q8 (b); 6.66) |
| 23:54 | `78acd165` | Browser app: an on-page log a rider can open on a phone and send (spec 14 Phase 10, 10G, v6.65) |

## Builds and build servers

283 build/test runs on the build machines, 55.1 h in total, 51 failed; 1440 server samples; cargo compiled 67863 crates in 18.9 h, 13.2 h waiting for build slots.

| Machine | Runs | Hours | Cargo h | Crates | Waited h | Failed | Online |
|---|---|---|---|---|---|---|---|
| Weela | 0 | 0.0 | 0.0 | 0 | 0.0 | 0 | 0% |
| Win11Builder | 9 | 3.7 | 1.7 | 2119 | 1.1 | 2 | 99% |
| leela | 54 | 20.0 | 4.4 | 17137 | 9.1 | 13 | 100% |
| macos | 22 | 1.0 | 0.4 | 240 | 0.1 | 2 | 100% |
| marge | 198 | 30.5 | 12.4 | 48367 | 2.8 | 34 | 100% |

Failed runs:

- 05:11 leela: `make check && make test-web-build && make test-smoke` (exit 2, log `build-log/051119-leela-3880287.log`)
- 09:12 marge: `bash test-output/fly/mem-measure.sh` (exit 127, log `build-log/091226-marge-160770.log`)
- 09:30 leela: `make test-accounts && make check && make test-web-build && echo ALL-GREEN` (exit 2, log `build-log/093024-leela-207338.log`)
- 09:33 leela: `make test-accounts && make check && make test-web-build && echo ALL-GREEN` (exit 2, log `build-log/093307-leela-210544.log`)
- 09:40 leela: `make test-accounts && make check && make test-web-build && echo ALL-GREEN` (exit 2, log `build-log/094001-leela-218307.log`)
- 10:45 marge: `OCW_REMOTE_HOST=213.188.222.85 OCW_REMOTE_CERT=0ae1fb51a5eacb8fb1beb577b107b5fa5` (exit 1, log `build-log/104504-marge-345637.log`)
- 10:49 marge: `python3 scripts/test-remote-web.py --query "server=https://213.188.222.85:47801&` (exit 1, log `build-log/104943-marge-352715.log`)
- 10:51 marge: `make check` (exit 2, log `build-log/105126-marge-356012.log`)
- 10:45 leela: `make check && make test-web-build && make test-smoke && echo CHECKS-OK` (exit 2, log `build-log/104514-leela-346024.log`)
- 11:10 leela: `cargo fmt --all --check; cargo clippy --workspace --all-targets -- -D warnings &` (exit 101, log `build-log/111037-leela-404620.log`)
- 11:11 marge: `make check && make test-web-build && make test-smoke` (exit 2, log `build-log/111144-marge-406918.log`)
- 11:16 leela: `cargo fmt --all --check; cargo clippy --workspace --all-targets -- -D warnings &` (exit 101, log `build-log/111634-leela-412770.log`)
- 11:33 leela: `cargo fmt --all --check && cargo clippy -p ocw-desktop --all-targets -- -D warni` (exit 101, log `build-log/113331-leela-431365.log`)
- 11:36 leela: `make test-accounts && make check && make test-web-build && make test-smoke` (exit 2, log `build-log/113646-leela-435063.log`)
- 11:36 marge: `scripts/workshop-account-shot.sh test-output/workshop-account/workshop-account.j` (exit 1, log `build-log/113646-marge-435109.log`)
- 11:46 marge: `bash target/a38/phase-a.sh && bash target/a38/phase-b.sh` (exit 1, log `build-log/114641-marge-447076.log`)
- 12:03 marge: `make web && make web-worlds && OCW_REMOTE_HOST=213.188.222.85 OCW_REMOTE_CERT=0a` (exit 1, log `build-log/120338-marge-475116.log`)
- 12:18 marge: `python3 scripts/test-remote-web.py --query "server=https%3A%2F%2F213.188.222.85%` (exit 1, log `build-log/121853-marge-513802.log`)
- 12:26 marge: `OCW_REMOTE_HOST=213.188.222.85 OCW_REMOTE_CERT=0ae1fb51a5eacb8fb1beb577b107b5fa5` (exit 1, log `build-log/122611-marge-522295.log`)
- 12:33 marge: `OCW_REMOTE_HOST=213.188.222.85 OCW_REMOTE_CERT=0ae1fb51a5eacb8fb1beb577b107b5fa5` (exit 1, log `build-log/123324-marge-529994.log`)
- 12:36 macos: `rm -rf apps/desktop/src/workshop; cargo fmt --all --check && cargo test -p ocw-u` (exit 101, log `build-log/123652-macos-533593.log`)
- 12:50 marge: `make check && make test-web-build && make test-smoke` (exit 2, log `build-log/125012-marge-574316.log`)
- 13:24 marge: `OCW_REMOTE_HOST=213.188.222.85 OCW_REMOTE_CERT=0ae1fb51a5eacb8fb1beb577b107b5fa5` (exit 1, log `build-log/132417-marge-637239.log`)
- 13:31 macos: `cargo fmt --all -- --check && cargo test -q -p ocw-sky 2>&1 | tail -5 && cargo t` (exit 1, log `build-log/133128-macos-645357.log`)
- 13:32 marge: `OCW_REMOTE_HOST=213.188.222.85 OCW_REMOTE_CERT=0ae1fb51a5eacb8fb1beb577b107b5fa5` (exit 1, log `build-log/133217-marge-646554.log`)
- 13:40 marge: `free -g | head -2; rm -rf apps/desktop/src/workshop; make test-accounts && make ` (exit 2, log `build-log/134046-marge-657543.log`)
- 13:55 marge: `OCW_REMOTE_HOST=213.188.222.85 OCW_REMOTE_CERT=0ae1fb51a5eacb8fb1beb577b107b5fa5` (exit 1, log `build-log/135534-marge-700019.log`)
- 14:03 marge: `OCW_REMOTE_HOST=213.188.222.85 OCW_REMOTE_CERT=0ae1fb51a5eacb8fb1beb577b107b5fa5` (exit 1, log `build-log/140323-marge-733854.log`)
- 14:06 marge: `free -g | head -2; make check && make test-web-build && make test-smoke` (exit 2, log `build-log/140615-marge-736921.log`)
- 14:06 leela: `{ [ -L data/andorra ] || ln -s ~/src/OCW/data/andorra data/andorra; } && scripts` (exit 1, log `build-log/140604-leela-736679.log`)
- 14:58 marge: `scripts/fetch-imagery.sh andorra && du -sh data/andorra/imagery && tail -8 data/` (exit 135, log `build-log/145856-marge-791487.log`)
- 14:12 marge: `make check && make test-web-build && make test-smoke` (exit 2, log `build-log/141225-marge-743593.log`)
- 14:11 marge: `make check && make test-web-build && make test-smoke && echo ALL-CHECKS-OK` (exit 2, log `build-log/141107-marge-742351.log`)
- 15:09 marge: `make check && make test-web-build && make test-smoke && echo ALL-CHECKS-OK` (exit 2, log `build-log/150931-marge-828752.log`)
- 14:58 leela: `{ [ -L data/andorra ] || ln -s ~/src/OCW/data/andorra data/andorra; } && scripts` (exit 1, log `build-log/145856-leela-791511.log`)
- 15:03 leela: `{ [ -L data/andorra ] || ln -s ~/src/OCW/data/andorra data/andorra; } && { [ -x ` (exit 1, log `build-log/150357-leela-796589.log`)
- 15:51 Win11Builder: `cargo clippy --workspace --all-targets -- -D warnings 2>&1 | Select-String -Patt` (exit 1, log `build-log/155150-Win11Builder-901989.log`)
- 17:55 marge: `   set -e   D=/var/tmp/ocw   put() { install -m $1 "$2" "$D/.$3.new" && mv -f "$` (exit 101, log `build-log/175509-marge-1131160.log`)
- 17:58 leela: `   set -e   D=/var/tmp/ocw   put() { install -m $1 "$2" "$D/.$3.new" && mv -f "$` (exit 101, log `build-log/175851-leela-1134582.log`)
- 18:26 marge: `cargo fmt --all -- --check; cargo test -p ocw-server --lib -- join_http tls:: &&` (exit 101, log `build-log/182649-marge-1185963.log`)
- 18:29 marge: `cargo fmt --all -- --check && cargo test -p ocw-server --lib -- join_http tls:: ` (exit 101, log `build-log/182905-marge-1188182.log`)
- 18:29 marge: `cargo fmt --all -- --check && cargo test -p ocw-server --lib -- join_http tls:: ` (exit 2, log `build-log/182948-marge-1188998.log`)
- 18:34 marge: `cargo fmt --all -- --check && make check && make test-web-build && make test-smo` (exit 2, log `build-log/183451-marge-1193687.log`)
- 19:10 marge: `O=test-output/together-$(date +%Y%m%d); S=target/together/site; python3 scripts/` (exit 1, log `build-log/191006-marge-1255682.log`)
- 21:52 marge: `make check && make test-web-build && make test-smoke` (exit 2, log `build-log/215234-marge-1486382.log`)
- 21:56 marge: `make check && make test-web-build && make test-smoke` (exit 2, log `build-log/215618-marge-1490603.log`)
- 22:05 marge: `make check && make test-web-build && make test-smoke` (exit 2, log `build-log/220512-marge-1525636.log`)
- 21:49 Win11Builder: `cargo clippy -p ocw-desktop -p ocw-client -p ocw-ui --all-targets -- -D warnings` (exit 1, log `build-log/214947-Win11Builder-1483297.log`)
- 22:06 marge: `cargo test -p ocw-desktop --bin ocw-desktop menu::tests && make check && make te` (exit 101, log `build-log/220623-marge-1527533.log`)
- 22:14 marge: `bash scripts/test-kiosk.sh` (exit 143, log `build-log/221447-marge-1538095.log`)
- 22:27 marge: `c=$(mktemp -d /var/tmp/ocw-joincfg.XXXX); XDG_CONFIG_HOME=$c OCW_APP=/var/tmp/oc` (exit 1, log `build-log/222754-marge-1553020.log`)

Longest runs:

- 95 min on leela: `make check && make test-web-build && make test-smoke; echo CHECKS_EXIT $?`
- 76 min on Win11Builder: `cargo clippy --workspace --all-targets -- -D warnings; if ($LASTEXITCODE -ne 0) `
- 72 min on leela: `rm -rf apps/desktop/src/workshop && make test-accounts && make check && make tes`
- 72 min on leela: `make check && make test-web-build && make test-smoke && cargo run -q -p ocw-asse`
- 70 min on leela: `bash scripts/tmp-andorra-tests.sh`

## Token usage

1.71 B tokens in 5,960 model messages (output 3.5 M, cache reads 1.68 B, cache writes 22.2 M, uncached input 13 k). Full breakdown: [tokens.json](tokens.json).

| Feature | Tokens | Output | Messages |
|---|---|---|---|
| Other | 884.4 M | 1.8 M | 2,978 |
| Worlds & terrain | 252.7 M | 306 k | 608 |
| Planning & spec | 167.8 M | 353 k | 697 |
| Build, release & infra | 164.8 M | 379 k | 524 |
| Art project | 77.5 M | 163 k | 359 |
| Multiplayer & server | 69.3 M | 194 k | 345 |
| Audio & voice | 46.7 M | 118 k | 231 |
| UI & menus | 27.1 M | 94 k | 121 |
| Riders & bikes | 17.3 M | 104 k | 97 |

| Task | Feature | Tokens | Output |
|---|---|---|---|
| agent: Landscape: water, far hills, slopes, obelisks | Other | 178.6 M | 325 k |
| agent: New world: Andorra | Worlds & terrain | 171.5 M | 173 k |
| agent: Accounts part 2: desktop client | Other | 150.8 M | 232 k |
| agent: Accounts: inventory + hearts on Postgres | Other | 97.4 M | 252 k |
| agent: Build ANT+ heart rate (no hardware) | Build, release & infra | 78.2 M | 239 k |
| agent: Bring PC VR (agent/vr-x1) onto main | Planning & spec | 62.2 M | 103 k |
| agent: Studio: patch prompt, recipe, way edits | Other | 54.5 M | 156 k |
| coordination: yes | Other | 53.2 M | 35 k |
| coordination: add and build a world map for andorra. do all the estimations as for the other w… | Worlds & terrain | 51.6 M | 32 k |
| agent: Studio: signing, keys, strict, views, closed | Other | 50.4 M | 82 k |
| agent: Fly: finish deploy tests + wss | Build, release & infra | 49.6 M | 120 k |
| agent: Fly: browser WebTransport to Fly | Planning & spec | 49.0 M | 95 k |
| agent: Deploy ocw-server + voice on Fly.io | Audio & voice | 42.3 M | 113 k |
| agent: Fly server: public status/statistics page | Multiplayer & server | 35.8 M | 101 k |
| agent: Studio: sign with own key, N/Z keys | Other | 34.1 M | 116 k |
| coordination: yes build the log option for the browser | Build, release & infra | 31.4 M | 15 k |
| agent: Live page joins the Fly server | Multiplayer & server | 31.0 M | 92 k |
| agent: BRouter consent + own BRouter on marge | Worlds & terrain | 29.7 M | 101 k |
| agent: ANT+: Garmin driver (Win) + udev helper (Linux) | Other | 29.2 M | 104 k |
| agent: Browser app: on-page log (?log=1) | Planning & spec | 25.5 M | 86 k |
| coordination: create some artwork of Andorra, put it here and also put it in the readme | Art project | 24.9 M | 12 k |
| agent: Fix missing land use on studio 2D map | Other | 22.8 M | 50 k |
| agent: Kiosks join the Fly server | UI & menus | 22.7 M | 90 k |
| agent: Game lists studio routes + README | Art project | 21.7 M | 70 k |
| agent: Andorra artwork + README | Art project | 16.0 M | 47 k |
| agent: Day 15 video (2026-11-25) | Other | 14.1 M | 36 k |
| agent: Faces: chin-strap beard, stubble | Other | 12.8 M | 41 k |
| coordination: is there a description on how to do the echo voice test, is it in readme? | Art project | 12.7 M | 13 k |
| agent: Rider faces: chin-strap beard, stubble | Riders & bikes | 12.5 M | 94 k |
| coordination: gibe me the open questions | Planning & spec | 12.4 M | 8 k |
| agent: Remove white squares on frames and rims | Other | 11.3 M | 38 k |
| agent: Research live road-traffic data sources | Other | 11.1 M | 45 k |
| agent: Fix flaky client prediction test | Other | 10.3 M | 45 k |
| coordination: yes, include border | Other | 8.4 M | 10 k |
| agent: remote.sh: drop files git stopped tracking | Other | 7.5 M | 47 k |
| coordination: 2: yes | Other | 7.5 M | 4 k |
| agent: Render unicorn over Hornisgrinde | Other | 7.4 M | 27 k |
| coordination: yes, a | Other | 7.4 M | 6 k |
| coordination: yes, q7 d | Other | 6.6 M | 5 k |
| coordination: i disnt mean to stop anything, continue everything | Other | 6.4 M | 13 k |

## Prompts

88 prompts (full text: [prompts.md](prompts.md)).

| Time | Prompt |
|---|---|
| 04:32 | The missing land use on OCW Studio's 2D map: should I start an agent to fix it? yes |
| 04:38 | next question |
| 04:40 | b |
| 04:41 | a |
| 04:42 | a |
| 04:43 | a, add to documentation |
| 04:45 | is there a description on how to do the echo voice test, is it in readme? |
| 07:18 | next question |
| 07:40 | b |
| 07:43 | a |
| 07:44 | a |
| 07:51 | q23 a |
| 07:52 | yes |
| 08:40 | I wan to host the ocw-server and the voice server on vercel. I created an api key: <token> and started the import of OCW and the deploy of o |
| 08:46 | the team is newkit. okay then lets only put the accounts with psql and the bike / hearts / parts thing there. |
| 08:54 | stop with vercel for now |
| 08:55 | i created a fly.io account <token> |
| 08:59 | q18 (a) |
| 09:01 | q19 a |
| 09:02 | q20 a |
| 09:02 | q21 a |
| 09:04 | yes |
| 10:10 | okay, added a payment option to fly.io |
| 10:11 | 10$ budget per month is authorizes |
| 10:14 | whats the user secret? where did it come from? |
| 10:18 | i have created that secret but its not used. it can be safely removed |
| 10:20 | what would be the costs for the psql on fly as well? |
| 10:24 | lets keep it simple for now and put the psql on fly, too. increase budget authorization to 16$. |
| 10:25 | yes, a |
| 10:31 | what else can be developed? |
| 10:32 | okay, develop 1.-8. |
| 10:33 | give me the next open question |
| 10:36 | okay, a |
| 10:39 | b |
| 10:41 | put warning signs, but let it be ridable |
| 10:51 | planning: make a switch in settings for turning on traffic. this are cars, lorries, motobikes planes, helicopters, ufos and such. investigat |
| 10:52 | elaborate p10q11 |
| 10:57 | a for now |
| 11:01 | open questions? |
| 11:07 | i disnt mean to stop anything, continue everything |
| 11:38 | q1-3: yes, as proposed. q4: yes, cars can hit riders. add a lunatic mode, where cares drive like crazy and overtake in stupid and dangerous  |
| 11:39 | q5: ivestigate where to get data and add a switch for that. implement when there are datasources available that suit us |
| 11:41 | q6: yes |
| 11:41 | q7: yes |
| 11:42 | q7: a,b,c |
| 11:43 | q8: make options a,b,c selectalble in traffic settings in game menu |
| 11:44 | q9: yes |
| 11:45 | q9: b |
| 11:46 | yes, change q9, i made a mistake |
| 11:47 | q10: a |
| 11:50 | what are the ant+ questions? |
| 11:51 | q1: b for now |
| 11:52 | q2: postpone the hw test, just prepare and build |
| 11:54 | q3: a, but also b |
| 11:57 | 18q11: b,c |
| 12:17 | gibe me the open questions |
| 12:51 | q4 b , q5: a,b, q6: c |
| 13:14 | add and build a world map for andorra. do all the estimations as for the other worlds |
| 15:26 | yes, do the fly agent |
| 15:27 | would i need the marge vr build output |
| 15:28 | yes and yes |
| 15:32 | yes, a |
| 16:07 | render me a nice image of the unicorn flying over hornisgrinde |
| 16:09 | also make a short video clip of the unicorn, have the drown swirl around so that unicorn and landscape is visible |
| 16:10 | is everything clear for the ant plus HR snsor connction and recording? |
| 16:16 | retrieve the ant key and tell me here |
| 16:19 | yes |
| 18:14 | 1: yea |
| 18:14 | 2: yes |
| 18:36 | create some artwork of Andorra, put it here and also put it in the readme |
| 20:34 | 1: yes 2: show an image 3: whats the question |
| 20:53 | 2: yes fix that but in a general way. for instance i noticed all lakes and rivers have that zig zag pattern. fix it for all similar cases |
| 21:01 | q7 investigate b |
| 21:02 | q8:b |
| 21:28 | yes, q7 d |
| 21:41 | Envalira pass on an October evening - i think the poles dont belomg there. i spoke to some locals and they say there is nothing like that. |
| 21:42 | give me a vr question |
| 21:43 | yes, a |
| 21:44 | c |
| 21:45 | b |
| 21:47 | is the fly.io seever up and running? does is have a website? |
| 21:56 | yes, build the statistic page for the server |
| 21:58 | q14, as proposed |
| 21:59 | can i do the voice echo test from my fone? the webapp does not run on my phone (still). can u fix that, too? |
| 22:03 | q15? |
| 22:04 | would it help to watch the browser console? how to open? |
| 22:05 | have the kiosks connect to the new fly.io server |
| 22:06 | yes build the log option for the browser |

## Features

64 spec versions added, 25 landed by a merge; 6 deploys, 0 releases.

| Spec | Feature | Landed | Check (marge) |
|---|---|---|---|
| 6.03 | Decided: 16H Q16 – when OCW Studio opens a package with a patch file <package>.ocwpatch n… | 04:40 `5e482567` | – |
| 6.04 | Decided: 16H Q17 – OCW Studio's *Build package* keeps writing patched/<name>.ocwpkg next… | 04:41 `e949f664` | – |
| 6.05 | Decided: 16H Q18 – a road edit in OCW Studio acts on the whole OSM way by default | 04:42 `f8a8c25f` | – |
| 6.06 | Decided: 16H Q19 – the game's route list offers the package's own routes, every routes/*.… | 04:44 `01f783f4` | – |
| 6.07 | Fixed: OCW Studio's 2D map draws the open package's land use again | 05:41 `19694296` (merge) | ok at 06:52, 81 suites, 3572 passed, 0 failed (commit) |
| 6.08 | Built: the game's route list offers the package's own routes, then the user's, marked "yo… | 06:11 `72db9890` (merge) | – |
| 6.09 | Decided: 16H Q20 – the route planner's settings stay separate | 07:40 `73941c84` | – |
| 6.10 | Decided: 16H Q21 – sending the via-points to a BRouter server is asked once per server an… | 07:43 `34b1dab5` | – |
| 6.11 | Decided: 16H Q22 – the planner tests use our own BRouter on marge | 07:44 `03e4f45d` | – |
| 6.12 | Built: OCW Studio asks before loading the patch next to a package, *Build package* runs t… | 07:45 `5c74de2f` (merge) | – |
| 6.13 | Decided: 16H Q23 – an imported GPX track keeps a via-point every kilometre, so dragging o… | 07:51 `fc80aa9f` | – |
| 6.14 | Decided: Phase 4 Q18 – with accounts, every rider's base parts are included | 08:59 `1d001b90` | – |
| 6.15 | Decided: Phase 4 Q19 – hearts are credited directly only by game servers whose key is sig… | 09:01 `08e67ac1` | – |
| 6.16 | Decided: Phase 4 Q20 – a signed-in rider without internet, or with the server down, rides… | 09:02 `3d17a923` | – |
| 6.17 | Decided: Phase 4 Q21 – with accounts every rider starts fresh with 5,000 ♥ and nothing ow… | 09:03 `f62c5492` | – |
| 6.18 | Built: sending the via-points to a BRouter server is asked once per server and the answer… | 09:22 `8c4ec441` (merge) | – |
| 6.19 | Prepared: ocw-server with its bundled voice server on Fly.io | 09:24 `ba5e986c` (merge) | exit 2 at 10:51 (commit) |
| 6.20 | Decided: 16H Q7 – a world patch whose target road is gone in a newer OSM build fails our… | 10:36 `3193fd15` | – |
| 6.21 | Decided: 16H Q13 – OCW Studio's saved camera views are stored in the world patch file, so… | 10:39 `f5c0612b` | – |
| 6.22 | Decided: 16H Q6 – a road marked *closed for bikes* in a world patch stays drawn and ridea… | 10:42 `3505028f` | – |
| 6.23 | Built: the accounts backend keeps every account's hearts, bikes, parts and kit in Postgre… | 10:56 `bcd7c4f7` (merge) | – |
| 6.24 | Decided: Phase 10 Q11 – on iPhones and iPads before iOS / iPadOS 26.4 the sensor bridge s… | 11:01 `2f80984f` | – |
| 6.25 | Planned: traffic as a switch in Settings | 11:18 `280f8620` (merge) | – |
| 6.26 | Decided: Phase 18 Q1 – traffic decisions | 11:38 `cf128e15` | – |
| 6.27 | Decided: Phase 18 Q5 – live road-traffic data | 11:39 `b09100db` | – |
| 6.28 | Decided: Phase 18 Q6 – live aircraft come from adsb.lol as an opt-in | 11:41 `2d783aff` | – |
| 6.29 | Decided: Phase 18 Q7 – UFOs come to the unicorn in god mode | 11:42 `14a7943c` | – |
| 6.30 | Decided: Phase 18 Q7 – UFOs get the scenes too | 11:42 `53f0ce28` | – |
| 6.31 | Decided: Phase 18 Q8 – drivers' manners are a setting in Settings → Traffic | 11:44 `4750e5dd` | – |
| 6.32 | Decided: Phase 18 Q9 – traffic is available on every device | 11:45 `59b2051e` | – |
| 6.33 | Road traffic only in the desktop app | 11:46 `5ee57d5d` | – |
| 6.34 | Decided: Phase 18 Q10 – traffic comes after the open work of the phases in progress | 11:47 `5024a6c1` | – |
| 6.35 | Decided: Phase 17 Q1 – the ANT+ network key is not shipped | 11:51 `6ba7b19b` | – |
| 6.36 | Decided: Phase 17 Q2 – ANT+ heart rate is prepared and built without hardware | 11:52 `73181477` | – |
| 6.37 | Live road data sources researched again | 11:53 `f6bebe49` (merge) | – |
| 6.38 | Decided: Phase 17 Q3 – ANT+ comes to the desktop app first and to the browser both ways | 11:54 `460d2aca` | – |
| 6.39 | Decided: Phase 18 Q11 – live road data for all three worlds | 11:57 `a21f17df` | – |
| 6.40 | Fixed: the virtual brake of autodrive sheds speed at most 5 m/s², no longer all at once,… | 12:42 `fcf55f13` (merge) | – |
| 6.41 | Decided: Phase 17 Q4 – ANT+ starts now, without hardware | 12:52 `98c46a0a` | – |
| 6.42 | Built: signed in, the desktop's workshop is the account's | 13:45 `394f5ff4` (merge) | ok at 12:42 (commit) |
| 6.43 | Built: the browser app has the desktop's workshop | 15:09 `31585b16` (merge) | ok at 16:16 (commit) |
| 6.44 | Built: repairs on the account | 15:09 `31585b16` (merge) | ok at 16:16 (commit) |
| 6.45 | Fixed: no white panels on the bikes | 14:10 `fdd25b8c` (merge) | – |
| 6.46 | Fixed: the chin-strap beard lies on the jaw line from ear to ear, and the stubble beards… | 14:10 `40385e02` (merge) | – |
| 6.47 | Built: OCW Studio signs the packages it builds with the user's own key, made on the first… | 14:11 `a471203b` (merge) | ok at 15:04, 86 suites, 3650 passed, 0 failed (commit) |
| 6.48 | Fixed: remote.sh deletes on the build machines the files removed or moved away here, so a… | 15:22 `aed18ae0` (merge) | ok at 16:10, 86 suites, 3654 passed, 0 failed (commit) |
| 6.49 | Built: the rider is the account's | 16:47 `2482a3fe` (merge) | – |
| 6.50 | ANT+ heart rate is built for the desktop app, without hardware | 16:47 `6365e44f` (merge) | – |
| 6.51 | Fifth world | 16:47 `df7f8b67` (merge) | – |
| 6.52 | Built: PC VR merged onto main | 16:48 `21e22b82` (merge) | ok at 16:48, 95 suites, 3800 passed, 0 failed (commit) |
| 6.53 | Deployed: ocw-server with its bundled voice server runs on Fly.io | 17:24 `ba69b807` (merge) | exit 101 at 18:26 (commit) |
| 6.54 | Fixed: browsers join the Fly.io server reliably | 17:24 `ba69b807` (merge) | exit 101 at 18:26 (commit) |
| 6.55 | Decided: 7 Q1 – andorra stays within its border for now | 18:15 `d491f70d` | – |
| 6.56 | Riding together on the public page | 19:13 `c11db780` (merge) | ok at 19:13, 88 suites, 3741 passed, 0 failed (commit) |
| 6.57 | Decided: the public Fly server keeps logging joins with the rider's name and IP address,… | 20:34 `84d86b07` | – |
| 6.58 | Decided: Phase 17 Q8 – on Linux the ANT stick's access rule is installed by a helper, ocw… | 21:02 `fd113570` | – |
| 6.59 | No COM-port route for ANT sticks on Windows | 21:08 `516c26d1` | – |
| 6.60 | Decided: Phase 17 Q7 – on Windows the desktop app talks to the ANT stick through Garmin's… | 21:29 `562b6ebb` | – |
| 6.61 | Decided: Phase 11 Q11 – in the PC headset the in-game menu opens as the same panel as in… | 21:43 `324b5d71` | – |
| 6.62 | Decided: Phase 11 Q12 – in VR on the time-trial bike the bike computer moves between the… | 21:44 `e62294d6` | – |
| 6.63 | Decided: Phase 11 Q13 – in VR a bike computer part fitted in the workshop becomes the VR… | 21:45 `34eac71b` | – |
| 6.64 | Decided: Phase 11 Q14 – the Windows VR kiosk keeps the app's local server while it is sto… | 21:59 `42e87345` | – |
| 6.65 | A public status page for the Fly.io server | 23:29 `733ca32d` (merge) | – |
| 6.66 | Built: the ANT stick works on Windows through Garmin's own libusb-win32 driver, and on Li… | 23:29 `22d76884` (merge) | ok at 23:29, 86 suites, 3769 passed, 0 failed (commit) |

Deploys:

- 06:53 marge: `72db9890` (ok)
- 06:55 leela: `72db9890` (ok)
- 17:55 marge: `ba69b807` (exit 101)
- 17:58 leela: `ba69b807` (exit 101)
- 18:02 marge: `ba69b807` (ok)
- 18:03 leela: `ba69b807` (ok)

## Agent jobs

33 jobs (coordinator log agents.jsonl).

| Task | Branch | Start | End | Status | Interrupted | Merged |
|---|---|---|---|---|---|---|
| Fix the missing land use on the studio's 2D map | a219c9b5 | 04:32 | 06:11 | merged |  |  |
| The game lists the studio's saved routes; README (16H Q19 a) | ad266d1e | 04:44 | 06:53 | merged |  |  |
| Studio: ask before loading a patch, build recipes, whole-way road edits (16H Q16-Q18) | a8045880 | 06:12 | 07:47 | merged |  |  |
| BRouter: consent per server, own BRouter on marge for the planner tests (16H Q21, Q22) | ac80ed3b | 07:52 | 09:24 | merged |  |  |
| Host ocw-server and the voice server on Fly.io | af97cd2d | 08:56 | 09:16 | reported |  |  |
| Accounts backend: inventory and hearts on Postgres (4O, Phase 4 Q18-Q21) | ae9ce66a | 09:05 | 10:13 | reported |  |  |
| Fix the flaky client prediction test | a52ff800 | 10:33 |  | started |  |  |
| Studio: sign built worlds with the user's own key; N/Z keys | a38bf8cc | 10:33 |  | started |  |  |
| Rider faces: chin-strap beard on the jaw, stubble clear of the lips | ad6678d7 | 10:33 |  | started |  |  |
| Art README: the evolution strip to day 15 | acd594c7 | 10:33 | 10:39 | merged |  |  |
| Planning: traffic (cars, lorries, motorbikes, aircraft, UFOs) and real-time data | aa7e3fb0 | 10:51 |  | started |  |  |
| Fly: ocw-server deploy tests and wss:// (continued) | aefaf1b3 | 11:09 | 14:42 | reported |  |  |
| Accounts part 2: the desktop client (continued) | ab18f006 | 11:09 | 17:22 | merged |  |  |
| Studio: own-key signing, N/Z, --strict-patch, views in the patch, closed roads (continued) | ad8dfd66 | 11:09 | 15:21 | merged |  |  |
| Rider faces: chin-strap beard, stubble (continued) | a8912406 | 11:09 | 15:21 | merged |  |  |
| Fix the flaky client prediction test (continued) | a8812bf5 | 11:09 | 12:44 | merged |  |  |
| Planning: traffic and real-time data (restarted) | a3e11a1a | 11:09 | 11:18 | merged |  |  |
| Research: live road-traffic data sources (Phase 18 Q5) | aa3a4bee | 11:40 | 11:53 | merged |  |  |
| Remove the white squares on frames and rims (all models) | a14a9b86 | 12:05 | 15:21 | merged |  |  |
| ANT+ heart rate on the desktop, without hardware (Phase 17 A1-A3) | a5c74980 | 12:52 | 17:23 | merged |  |  |
| New world: Andorra, built like the others with all estimates | a5e3f990 | 13:15 | 17:23 | merged |  |  |
| remote.sh: drop files git no longer tracks on the build machines | a8422046 | 13:41 | 16:46 | merged |  |  |
| Fly: the browser's WebTransport connection to the Fly server | aa3c6429 | 15:27 | 17:54 | merged |  |  |
| Bring PC VR (agent/vr-x1, OpenXR via Link) onto main | a0839f55 | 15:33 | 17:23 | merged |  |  |
| Render: the unicorn flying over the Hornisgrinde | a635a78a | 16:08 | 16:56 | reported |  |  |
| The live page rides and talks on the Fly server | a5aa4517 | 18:14 | 19:43 | merged |  |  |
| Andorra artwork for the README | a334c6ab | 18:36 | 19:03 | merged |  |  |
| Landscape: smooth lakes and rivers, far terrain, high slopes, tall objects (all worlds) | a0d2648e | 20:54 | 23:43 | reported |  |  |
| Research: the ANT stick over a COM port on Windows (Phase 17 Q7 b) | a30a6ccf | 21:01 | 21:09 | merged |  |  |
| ANT+: Garmin's driver on Windows, the udev helper on Linux (Phase 17 Q7 d, Q8 b) | a4ff3c8a | 21:29 | 23:28 | reported |  |  |
| Fly server: a public status and statistics page | a17e3f1a | 21:57 | 23:23 | reported |  |  |
| Kiosks join the Fly server (remote mode) | a5e80efc | 22:06 |  | started |  |  |
| Browser app: an on-page log for phones (?log=1) | abd1e924 | 22:07 | 23:55 | reported |  |  |

## Incidents

70 collected (disk-full 2, janitor-delete 62, machine-offline 3, machine-online 2, runs-failed 1), 0 with root-cause notes ([incidents.md](incidents.md)).

| Time | Kind | Machine | What |
|---|---|---|---|
| 00:00 | machine-offline | Weela | Weela unreachable (no route to host) |
| 00:00 | disk-full | Win11Builder | disk C: on Win11Builder at 97 % |
| 06:10 | janitor-delete | marge | janitor delete OCW-merge-landuse/target (32.8 GB) |
| 06:10 | janitor-delete | marge | janitor delete OCW-worktree-agent-a219c9b503ec94ccf/target (38.8 GB) |
| 06:10 | janitor-delete | leela | janitor delete OCW-worktree-agent-a219c9b503ec94ccf/target (3.1 GB) |
| 06:51 | janitor-delete | leela | janitor delete OCW-merge-routes/target (32.8 GB) |
| 06:52 | janitor-delete | leela | janitor delete OCW-worktree-agent-ad266d1e347afb128/target (40.7 GB) |
| 06:52 | janitor-delete | marge | janitor delete OCW-worktree-agent-ad266d1e347afb128/target (7.6 GB) |
| 07:46 | janitor-delete | marge | janitor delete OCW-merge-q16/target (32.9 GB) |
| 07:46 | janitor-delete | marge | janitor delete OCW-worktree-agent-a8045880f0c5689dc/target (46.3 GB) |
| 07:46 | janitor-delete | leela | janitor delete OCW-worktree-agent-a8045880f0c5689dc/target (0.4 GB) |
| 09:22 | janitor-delete | marge | janitor delete OCW-merge-brouter/target (32.9 GB) |
| 09:22 | janitor-delete | marge | janitor delete OCW-worktree-agent-ac80ed3b3b3781bb1/target (41.2 GB) |
| 09:51 | janitor-delete | marge | janitor delete OCW-merge-fly/target (28.2 GB) |
| 10:37 | machine-offline | Win11Builder | Win11Builder unreachable (timeout) |
| 10:40 | machine-online | Win11Builder | Win11Builder back online |
| 10:57 | janitor-delete | leela | janitor delete OCW-merge-accounts/target (35.3 GB) |
| 12:24 | janitor-delete | marge | janitor delete OCW/target (3.2 GB) |
| 12:34 | janitor-delete | marge | janitor delete OCW/target (0.5 GB) |
| 12:43 | janitor-delete | leela | janitor delete OCW-merge-flaky/target (33.7 GB) |
| 12:43 | janitor-delete | leela | janitor delete OCW-worktree-agent-a52ff8004742f6ccd/target (6.1 GB) |
| 12:43 | janitor-delete | marge | janitor delete OCW-worktree-agent-a52ff8004742f6ccd/target (35.8 GB) |
| 13:53 | disk-full | marge | disk home on marge at 90 % |
| 14:17 | janitor-delete | marge | janitor alert  (0.0 GB) |
| 14:27 | janitor-delete | marge | janitor alert  (0.0 GB) |
| 14:38 | janitor-delete | marge | janitor alert  (0.0 GB) |
| 14:48 | janitor-delete | marge | janitor alert  (0.0 GB) |
| 14:58 | janitor-delete | marge | janitor alert  (0.0 GB) |
| 15:04 | janitor-delete | marge | janitor delete OCW-merge-studio-logo/target (20.0 GB) |
| 15:04 | janitor-delete | marge | janitor delete OCW-merge-fps/target (20.9 GB) |
| 15:04 | janitor-delete | marge | janitor delete OCW-merge-models-e3/target (20.7 GB) |
| 15:04 | janitor-delete | marge | janitor delete OCW-merge-activities/target (25.4 GB) |
| 15:04 | janitor-delete | marge | janitor delete OCW-j8-sides/target (39.5 GB) |
| 15:04 | janitor-delete | marge | janitor delete OCW-worktree-agent-ad6678d7086339e61/target (9.1 GB) |
| 15:04 | janitor-delete | marge | janitor delete OCW-worktree-agent-a14a9b861052bbda3/target (35.5 GB) |
| 15:04 | janitor-delete | marge | janitor delete OCW-worktree-agent-a38bf8cc98eb9bbc7/target (41.9 GB) |
| 15:04 | janitor-delete | marge | janitor delete OCW-merge-acc2/target (35.5 GB) |
| 15:09 | janitor-delete | macos | janitor delete OCW-worktree-agent-a367743c92249633c/target (7.4 GB) |
| 15:09 | janitor-delete | macos | janitor delete OCW-worktree-agent-a35b38f26955e38d0/target (2.0 GB) |
| 15:21 | janitor-delete | leela | janitor delete OCW-worktree-agent-ad6678d7086339e61/target (35.6 GB) |
| 15:21 | janitor-delete | leela | janitor delete OCW-worktree-agent-a38bf8cc98eb9bbc7/target (13.4 GB) |
| 15:21 | janitor-delete | marge | janitor delete OCW-merge-trio/target (47.1 GB) |
| 15:29 | janitor-delete | macos | janitor delete OCW-worktree-agent-ad6678d7086339e61/target (0.8 GB) |
| 15:59 | janitor-delete | macos | janitor delete OCW-worktree-agent-ab692ee78e235e3a6/target (6.3 GB) |
| 16:46 | janitor-delete | marge | janitor delete OCW-merge-sync/target (29.6 GB) |
| 17:22 | janitor-delete | marge | janitor delete OCW-worktree-agent-ae9ce66a8776a5e06/target (50.0 GB) |
| 17:23 | janitor-delete | leela | janitor delete OCW-worktree-agent-ae9ce66a8776a5e06/target (72.2 GB) |
| 17:23 | janitor-delete | marge | janitor delete OCW-worktree-agent-a5c7498037cda739c/target (34.0 GB) |
| 17:23 | janitor-delete | leela | janitor delete OCW-worktree-agent-a5c7498037cda739c/target (16.0 GB) |
| 17:23 | janitor-delete | marge | janitor delete OCW-worktree-agent-a5e3f9902d7341373/target (0.5 GB) |
| 17:23 | janitor-delete | leela | janitor delete OCW-worktree-agent-a5e3f9902d7341373/target (21.2 GB) |
| 17:23 | janitor-delete | marge | janitor delete OCW-merge-three/target (39.2 GB) |
| 17:23 | janitor-delete | marge | janitor delete OCW-merge-vr-x1/target (39.2 GB) |
| 17:23 | janitor-delete | leela | janitor delete OCW-merge-acc2/target (39.6 GB) |
| 17:30 | janitor-delete | macos | janitor delete OCW-worktree-agent-a5e3f9902d7341373/target (3.4 GB) |
| 17:30 | janitor-delete | macos | janitor delete OCW-worktree-agent-ae9ce66a8776a5e06/target (29.9 GB) |
| 17:54 | janitor-delete | marge | janitor delete OCW-merge-fly2/target (35.0 GB) |
| 17:54 | janitor-delete | marge | janitor delete OCW-worktree-agent-af97cd2d46c527ce9/target (89.0 GB) |
| 19:03 | janitor-delete | leela | janitor delete OCW-worktree-agent-a334c6ab7508061fd/target (3.6 GB) |
| 19:44 | janitor-delete | marge | janitor delete OCW-merge-join/target (35.0 GB) |

## Media

| Time | File |
|---|---|
| 04:38:59 | [043859-landuse-before-1600x900-bf-middle-neighbours.jpg](043859-landuse-before-1600x900-bf-middle-neighbours.jpg) |
| 04:39:20 | [043920-landuse-before-1600x900-bf-middle-border.jpg](043920-landuse-before-1600x900-bf-middle-border.jpg) |
| 04:39:42 | [043942-landuse-before-1600x900-bf-middle-aerial-off.jpg](043942-landuse-before-1600x900-bf-middle-aerial-off.jpg) |
| 04:40:03 | [044003-landuse-before-1600x900-bf-middle-aerial-on.jpg](044003-landuse-before-1600x900-bf-middle-aerial-on.jpg) |
| 04:40:19 | [044019-landuse-before-1600x900-li-border.jpg](044019-landuse-before-1600x900-li-border.jpg) |
| 04:40:35 | [044035-landuse-before-1600x900-li-aerial-off.jpg](044035-landuse-before-1600x900-li-aerial-off.jpg) |
| 04:40:50 | [044050-landuse-before-1600x900-li-aerial-on.jpg](044050-landuse-before-1600x900-li-aerial-on.jpg) |
| 04:41:12 | [044112-landuse-before-2560x1440-bf-middle-neighbours.jpg](044112-landuse-before-2560x1440-bf-middle-neighbours.jpg) |
| 04:41:33 | [044133-landuse-before-2560x1440-bf-middle-border.jpg](044133-landuse-before-2560x1440-bf-middle-border.jpg) |
| 04:41:54 | [044154-landuse-before-2560x1440-bf-middle-aerial-off.jpg](044154-landuse-before-2560x1440-bf-middle-aerial-off.jpg) |
| 04:42:16 | [044216-landuse-before-2560x1440-bf-middle-aerial-on.jpg](044216-landuse-before-2560x1440-bf-middle-aerial-on.jpg) |
| 04:42:32 | [044232-landuse-before-2560x1440-li-border.jpg](044232-landuse-before-2560x1440-li-border.jpg) |
| 04:42:47 | [044247-landuse-before-2560x1440-li-aerial-off.jpg](044247-landuse-before-2560x1440-li-aerial-off.jpg) |
| 04:43:03 | [044303-landuse-before-2560x1440-li-aerial-on.jpg](044303-landuse-before-2560x1440-li-aerial-on.jpg) |
| 04:56:24 | [045624-landuse-after-1600x900-bf-middle-neighbours.jpg](045624-landuse-after-1600x900-bf-middle-neighbours.jpg) |
| 04:56:45 | [045645-landuse-after-1600x900-bf-middle-border.jpg](045645-landuse-after-1600x900-bf-middle-border.jpg) |
| 04:57:07 | [045707-landuse-after-1600x900-bf-middle-aerial-off.jpg](045707-landuse-after-1600x900-bf-middle-aerial-off.jpg) |
| 04:57:28 | [045728-landuse-after-1600x900-bf-middle-aerial-on.jpg](045728-landuse-after-1600x900-bf-middle-aerial-on.jpg) |
| 04:57:44 | [045744-landuse-after-1600x900-li-border.jpg](045744-landuse-after-1600x900-li-border.jpg) |
| 04:58:00 | [045800-landuse-after-1600x900-li-aerial-off.jpg](045800-landuse-after-1600x900-li-aerial-off.jpg) |
| 04:58:15 | [045815-landuse-after-1600x900-li-aerial-on.jpg](045815-landuse-after-1600x900-li-aerial-on.jpg) |
| 04:58:36 | [045836-landuse-after-2560x1440-bf-middle-neighbours.jpg](045836-landuse-after-2560x1440-bf-middle-neighbours.jpg) |
| 04:58:58 | [045858-landuse-after-2560x1440-bf-middle-border.jpg](045858-landuse-after-2560x1440-bf-middle-border.jpg) |
| 04:59:19 | [045919-landuse-after-2560x1440-bf-middle-aerial-off.jpg](045919-landuse-after-2560x1440-bf-middle-aerial-off.jpg) |
| 04:59:41 | [045941-landuse-after-2560x1440-bf-middle-aerial-on.jpg](045941-landuse-after-2560x1440-bf-middle-aerial-on.jpg) |
| 04:59:57 | [045957-landuse-after-2560x1440-li-border.jpg](045957-landuse-after-2560x1440-li-border.jpg) |
| 05:00:12 | [050012-landuse-after-2560x1440-li-aerial-off.jpg](050012-landuse-after-2560x1440-li-aerial-off.jpg) |
| 05:00:28 | [050028-landuse-after-2560x1440-li-aerial-on.jpg](050028-landuse-after-2560x1440-li-aerial-on.jpg) |
| 05:00:46 | [050046-landuse-compare-bf-middle-neighbours-before-after.jpg](050046-landuse-compare-bf-middle-neighbours-before-after.jpg) |
| 05:00:46 | [050046-landuse-compare-li-border-before-after.jpg](050046-landuse-compare-li-border-before-after.jpg) |
| 05:27:17 | [052717-q19-q19-routes.jpg](052717-q19-q19-routes.jpg) |
| 06:49:00 | [064900-studio-q16-q18-patch-question.jpg](064900-studio-q16-q18-patch-question.jpg) |
| 06:50:48 | [065048-studio-q16-q18-whole-way-selected.jpg](065048-studio-q16-q18-whole-way-selected.jpg) |
| 06:51:04 | [065104-studio-q16-q18-edge-only-selected.jpg](065104-studio-q16-q18-edge-only-selected.jpg) |
| 08:20:33 | [082033-fc80aa9f-dirty-shot-wayland-brouter-consent.jpg](082033-fc80aa9f-dirty-shot-wayland-brouter-consent.jpg) |
| 08:20:51 | [082051-fc80aa9f-dirty-shot-wayland-brouter-vaduz-malbun.jpg](082051-fc80aa9f-dirty-shot-wayland-brouter-vaduz-malbun.jpg) |
| 08:46:03 | [084603-fc80aa9f-dirty-shot-ocw.jpg](084603-fc80aa9f-dirty-shot-ocw.jpg) |
| 08:46:12 | [084612-fc80aa9f-dirty-shot-wayland-ocw-wayland.jpg](084612-fc80aa9f-dirty-shot-wayland-ocw-wayland.jpg) |
| 10:45:05 | [104505-remote-server-desktop.jpg](104505-remote-server-desktop.jpg) |
| 10:45:26 | [104526-remote-server-remote-web-.mic.wav](104526-remote-server-remote-web-.mic.wav) |
| 10:45:26 | [104526-remote-server-remote-web-end.jpg](104526-remote-server-remote-web-end.jpg) |
| 10:45:26 | [104526-remote-server-remote-web-joined.jpg](104526-remote-server-remote-web-joined.jpg) |
| 10:45:26 | [104526-remote-server-remote-web-riding.jpg](104526-remote-server-remote-web-riding.jpg) |
| 10:55:34 | [105534-ba5e986c-dirty-shot-wayland-beard-fix-a-front.jpg](105534-ba5e986c-dirty-shot-wayland-beard-fix-a-front.jpg) |
| 10:55:45 | [105545-ba5e986c-dirty-shot-wayland-beard-fix-a-side.jpg](105545-ba5e986c-dirty-shot-wayland-beard-fix-a-side.jpg) |
| 10:55:57 | [105557-ba5e986c-dirty-shot-wayland-beard-fix-a-below.jpg](105557-ba5e986c-dirty-shot-wayland-beard-fix-a-below.jpg) |
| 10:56:07 | [105607-ba5e986c-dirty-shot-wayland-beard-fix-b-front.jpg](105607-ba5e986c-dirty-shot-wayland-beard-fix-b-front.jpg) |
| 10:56:19 | [105619-ba5e986c-dirty-shot-wayland-beard-fix-b-speaking.jpg](105619-ba5e986c-dirty-shot-wayland-beard-fix-b-speaking.jpg) |
| 10:56:30 | [105630-ba5e986c-dirty-shot-wayland-beard-fix-b-below.jpg](105630-ba5e986c-dirty-shot-wayland-beard-fix-b-below.jpg) |
| 10:56:41 | [105641-ba5e986c-dirty-shot-wayland-beard-fix-c-chinstrap-70-side.jpg](105641-ba5e986c-dirty-shot-wayland-beard-fix-c-chinstrap-70-side.jpg) |
| 10:56:52 | [105652-ba5e986c-dirty-shot-wayland-beard-fix-d-chinstrap-20-below.jpg](105652-ba5e986c-dirty-shot-wayland-beard-fix-d-chinstrap-20-below.jpg) |
| 10:57:03 | [105703-ba5e986c-dirty-shot-wayland-beard-fix-e-stubble-60-speaking.jpg](105703-ba5e986c-dirty-shot-wayland-beard-fix-e-stubble-60-speaking.jpg) |
| 10:57:14 | [105714-ba5e986c-dirty-shot-wayland-beard-fix-f-shortstubble-bare.jpg](105714-ba5e986c-dirty-shot-wayland-beard-fix-f-shortstubble-bare.jpg) |
| 11:52:08 | [115208-workshop-account-workshop-account.jpg](115208-workshop-account-workshop-account.jpg) |
| 11:52:39 | [115239-smoke-leela-smoke-wayland.jpg](115239-smoke-leela-smoke-wayland.jpg) |
| 11:52:39 | [115239-smoke-leela-smoke-x11.jpg](115239-smoke-leela-smoke-x11.jpg) |
| 11:54:12 | [115412-15757bc7-shot-wayland-beard-fix-a-front.jpg](115412-15757bc7-shot-wayland-beard-fix-a-front.jpg) |
| 11:54:23 | [115423-15757bc7-shot-wayland-beard-fix-a-side.jpg](115423-15757bc7-shot-wayland-beard-fix-a-side.jpg) |
| 11:54:34 | [115434-15757bc7-shot-wayland-beard-fix-a-below.jpg](115434-15757bc7-shot-wayland-beard-fix-a-below.jpg) |
| 11:54:44 | [115444-15757bc7-shot-wayland-beard-fix-b-front.jpg](115444-15757bc7-shot-wayland-beard-fix-b-front.jpg) |
| 11:54:54 | [115454-15757bc7-shot-wayland-beard-fix-b-speaking.jpg](115454-15757bc7-shot-wayland-beard-fix-b-speaking.jpg) |
| 11:55:05 | [115505-15757bc7-shot-wayland-beard-fix-b-below.jpg](115505-15757bc7-shot-wayland-beard-fix-b-below.jpg) |
| 11:55:16 | [115516-15757bc7-shot-wayland-beard-fix-c-chinstrap-70-side.jpg](115516-15757bc7-shot-wayland-beard-fix-c-chinstrap-70-side.jpg) |
| 11:55:27 | [115527-15757bc7-shot-wayland-beard-fix-d-chinstrap-20-below.jpg](115527-15757bc7-shot-wayland-beard-fix-d-chinstrap-20-below.jpg) |
| 11:55:37 | [115537-15757bc7-shot-wayland-beard-fix-e-stubble-60-speaking.jpg](115537-15757bc7-shot-wayland-beard-fix-e-stubble-60-speaking.jpg) |
| 11:55:48 | [115548-15757bc7-shot-wayland-beard-fix-f-shortstubble-bare.jpg](115548-15757bc7-shot-wayland-beard-fix-f-shortstubble-bare.jpg) |
| 11:55:58 | [115558-15757bc7-shot-wayland-beard-fix-g-chinstrap-bare.jpg](115558-15757bc7-shot-wayland-beard-fix-g-chinstrap-bare.jpg) |
| 11:56:09 | [115609-15757bc7-shot-wayland-beard-fix-h-far.jpg](115609-15757bc7-shot-wayland-beard-fix-h-far.jpg) |
| 12:01:16 | [120116-beard-fix-beard-fix-a-below-before.jpg](120116-beard-fix-beard-fix-a-below-before.jpg) |
| 12:01:16 | [120116-beard-fix-beard-fix-a-front-before.jpg](120116-beard-fix-beard-fix-a-front-before.jpg) |
| 12:01:16 | [120116-beard-fix-beard-fix-a-side-before.jpg](120116-beard-fix-beard-fix-a-side-before.jpg) |
| 12:01:16 | [120116-beard-fix-beard-fix-b-below-before.jpg](120116-beard-fix-beard-fix-b-below-before.jpg) |
| 12:01:16 | [120116-beard-fix-beard-fix-b-front-before.jpg](120116-beard-fix-beard-fix-b-front-before.jpg) |
| 12:01:16 | [120116-beard-fix-beard-fix-b-speaking-before.jpg](120116-beard-fix-beard-fix-b-speaking-before.jpg) |
| 12:17:46 | [121746-a21f17df-dirty-shot-wayland-white-panels-stand-aero.jpg](121746-a21f17df-dirty-shot-wayland-white-panels-stand-aero.jpg) |
| 12:17:57 | [121757-a21f17df-dirty-shot-wayland-white-panels-road-aero.jpg](121757-a21f17df-dirty-shot-wayland-white-panels-road-aero.jpg) |
| 12:18:11 | [121811-a21f17df-dirty-shot-wayland-white-panels-stand-tt.jpg](121811-a21f17df-dirty-shot-wayland-white-panels-stand-tt.jpg) |
| 12:18:22 | [121822-a21f17df-dirty-shot-wayland-white-panels-road-tt.jpg](121822-a21f17df-dirty-shot-wayland-white-panels-road-tt.jpg) |
| 12:21:38 | [122138-a21f17df-dirty-shot-wayland-white-panels-stand-aero.jpg](122138-a21f17df-dirty-shot-wayland-white-panels-stand-aero.jpg) |
| 12:22:05 | [122205-a21f17df-dirty-shot-wayland-white-panels-road-aero.jpg](122205-a21f17df-dirty-shot-wayland-white-panels-road-aero.jpg) |
| 12:22:19 | [122219-a21f17df-dirty-shot-wayland-white-panels-stand-tt.jpg](122219-a21f17df-dirty-shot-wayland-white-panels-stand-tt.jpg) |
| 12:22:30 | [122230-a21f17df-dirty-shot-wayland-white-panels-road-tt.jpg](122230-a21f17df-dirty-shot-wayland-white-panels-road-tt.jpg) |
| 12:22:46 | [122246-a21f17df-dirty-shot-wayland-white-panels-stand-endurance-carbon.jpg](122246-a21f17df-dirty-shot-wayland-white-panels-stand-endurance-carbon.jpg) |
| 12:22:59 | [122259-a21f17df-dirty-shot-wayland-white-panels-stand-gravel.jpg](122259-a21f17df-dirty-shot-wayland-white-panels-stand-gravel.jpg) |
| 12:23:13 | [122313-a21f17df-dirty-shot-wayland-white-panels-stand-mtb.jpg](122313-a21f17df-dirty-shot-wayland-white-panels-stand-mtb.jpg) |
| 12:54:52 | [125452-studio-signing-closed-roads-game-closed-road-sign-near.jpg](125452-studio-signing-closed-roads-game-closed-road-sign-near.jpg) |
| 12:54:52 | [125452-studio-signing-closed-roads-game-closed-road-sign.jpg](125452-studio-signing-closed-roads-game-closed-road-sign.jpg) |
| 12:54:52 | [125452-studio-signing-closed-roads-game-trust-dialog.jpg](125452-studio-signing-closed-roads-game-trust-dialog.jpg) |
| 12:54:52 | [125452-studio-signing-closed-roads-game-world-menu.jpg](125452-studio-signing-closed-roads-game-world-menu.jpg) |
| 12:54:52 | [125452-studio-signing-closed-roads-studio-built-signed.jpg](125452-studio-signing-closed-roads-studio-built-signed.jpg) |
| 12:54:52 | [125452-studio-signing-closed-roads-studio-sign-dialog.jpg](125452-studio-signing-closed-roads-studio-sign-dialog.jpg) |
| 13:04:11 | [130411-studio-signing-closed-roads-game-world-menu.jpg](130411-studio-signing-closed-roads-game-world-menu.jpg) |
| 13:14:13 | [131413-beard-fix-smoke-wayland-leela.jpg](131413-beard-fix-smoke-wayland-leela.jpg) |
| 13:14:13 | [131413-beard-fix-smoke-x11-leela.jpg](131413-beard-fix-smoke-x11-leela.jpg) |
| 13:17:46 | [131746-web-web-account-linked.jpg](131746-web-web-account-linked.jpg) |
| 13:17:46 | [131746-web-web-account-signed-in.jpg](131746-web-web-account-signed-in.jpg) |
| 13:17:46 | [131746-web-web-account-signed-out.jpg](131746-web-web-account-signed-out.jpg) |
| 13:17:46 | [131746-web-web-account-workshop.jpg](131746-web-web-account-workshop.jpg) |
| 13:55:35 | [135535-remote-server-desktop.jpg](135535-remote-server-desktop.jpg) |
| 13:55:56 | [135556-remote-server-remote-web-end.jpg](135556-remote-server-remote-web-end.jpg) |
| 13:55:56 | [135556-remote-server-remote-web-joined.jpg](135556-remote-server-remote-web-joined.jpg) |
| 13:55:56 | [135556-remote-server-remote-web-riding.jpg](135556-remote-server-remote-web-riding.jpg) |
| 15:26:02 | [152602-ant-devices-A-1-scan.png](152602-ant-devices-A-1-scan.png) |
| 15:26:11 | [152611-ant-devices-A-2-paired.png](152611-ant-devices-A-2-paired.png) |
| 15:26:12 | [152612-ant-devices-A-3-ant.png](152612-ant-devices-A-3-ant.png) |
| 15:26:16 | [152616-ant-devices-A-4-strap-page.png](152616-ant-devices-A-4-strap-page.png) |
| 15:26:18 | [152618-ant-devices-A-5-use-for-heart-rate.png](152618-ant-devices-A-5-use-for-heart-rate.png) |
| 15:26:22 | [152622-ant-devices-A-6-ride-hud.png](152622-ant-devices-A-6-ride-hud.png) |
| 15:26:32 | [152632-ant-devices-A-end.jpg](152632-ant-devices-A-end.jpg) |
| 15:26:49 | [152649-ant-devices-B-1-key-needed.png](152649-ant-devices-B-1-key-needed.png) |
| 15:26:50 | [152650-ant-devices-B-end.jpg](152650-ant-devices-B-end.jpg) |
| 15:26:51 | [152651-ant-devices-B-2-typing-the-key.png](152651-ant-devices-B-2-typing-the-key.png) |
| 15:27:16 | [152716-ant-devices-C-end.jpg](152716-ant-devices-C-end.jpg) |
| 15:35:25 | [153525-2026-11-26-andorra-envalira-pass.jpg](153525-2026-11-26-andorra-envalira-pass.jpg) |
| 15:35:50 | [153550-2026-11-26-andorra-arcalis.jpg](153550-2026-11-26-andorra-arcalis.jpg) |
| 15:46:11 | [154611-2026-11-26-andorra-gallina.jpg](154611-2026-11-26-andorra-gallina.jpg) |
| 15:46:16 | [154616-2026-11-26-andorra-gallina.mp4](154616-2026-11-26-andorra-gallina.mp4) |
| 15:46:43 | [154643-2026-11-26-andorra-andorra-la-vella.jpg](154643-2026-11-26-andorra-andorra-la-vella.jpg) |
| 15:51:15 | [155115-2026-11-26-andorra-studio.jpg](155115-2026-11-26-andorra-studio.jpg) |
| 16:01:07 | [160107-2026-11-26-andorra-web-web-world-cached-loading.jpg](160107-2026-11-26-andorra-web-web-world-cached-loading.jpg) |
| 16:01:07 | [160107-2026-11-26-andorra-web-web-world-cached.jpg](160107-2026-11-26-andorra-web-web-world-cached.jpg) |
| 16:01:07 | [160107-2026-11-26-andorra-web-web-world-first-loading.jpg](160107-2026-11-26-andorra-web-web-world-first-loading.jpg) |
| 16:01:07 | [160107-2026-11-26-andorra-web-web-world-teleport.jpg](160107-2026-11-26-andorra-web-web-world-teleport.jpg) |
| 16:01:07 | [160107-2026-11-26-andorra-web-web-world.jpg](160107-2026-11-26-andorra-web-web-world.jpg) |
| 16:02:01 | [160201-2026-11-26-andorra-web-memory-andorra-webgpu-web-world-first-loading.jpg](160201-2026-11-26-andorra-web-memory-andorra-webgpu-web-world-first-loading.jpg) |
| 16:02:01 | [160201-2026-11-26-andorra-web-memory-andorra-webgpu-web-world-teleport.jpg](160201-2026-11-26-andorra-web-memory-andorra-webgpu-web-world-teleport.jpg) |
| 16:02:01 | [160201-2026-11-26-andorra-web-memory-andorra-webgpu-web-world.jpg](160201-2026-11-26-andorra-web-memory-andorra-webgpu-web-world.jpg) |
| 16:02:49 | [160249-2026-11-26-andorra-web-memory-andorra-webgl2-web-world-webgl2-first-loading.jpg](160249-2026-11-26-andorra-web-memory-andorra-webgl2-web-world-webgl2-first-loading.jpg) |
| 16:02:49 | [160249-2026-11-26-andorra-web-memory-andorra-webgl2-web-world-webgl2-teleport.jpg](160249-2026-11-26-andorra-web-memory-andorra-webgl2-web-world-webgl2-teleport.jpg) |
| 16:02:49 | [160249-2026-11-26-andorra-web-memory-andorra-webgl2-web-world-webgl2.jpg](160249-2026-11-26-andorra-web-memory-andorra-webgl2-web-world-webgl2.jpg) |
| 16:04:10 | [160410-vr-merge-2026-11-26-00-monado-left-eye.jpg](160410-vr-merge-2026-11-26-00-monado-left-eye.jpg) |
| 16:13:53 | [161353-98c46a0a-dirty-shot-ocw.jpg](161353-98c46a0a-dirty-shot-ocw.jpg) |
| 16:14:03 | [161403-98c46a0a-dirty-shot-wayland-ocw-wayland.jpg](161403-98c46a0a-dirty-shot-wayland-ocw-wayland.jpg) |
| 16:31:25 | [163125-vr-merge-2026-11-26-01-bike-computer-left-eye.jpg](163125-vr-merge-2026-11-26-01-bike-computer-left-eye.jpg) |
| 16:31:43 | [163143-vr-merge-2026-11-26-02-controls-hint-left-eye.jpg](163143-vr-merge-2026-11-26-02-controls-hint-left-eye.jpg) |
| 16:32:06 | [163206-vr-merge-2026-11-26-03-both-eyes.jpg](163206-vr-merge-2026-11-26-03-both-eyes.jpg) |
| 16:32:45 | [163245-vr-merge-2026-11-26-04-chase-mirror.jpg](163245-vr-merge-2026-11-26-04-chase-mirror.jpg) |
| 16:37:32 | [163732-remote-server-desktop.jpg](163732-remote-server-desktop.jpg) |
| 16:37:44 | [163744-98c46a0a-dirty-shot-wayland-final-envalira-soldeu.jpg](163744-98c46a0a-dirty-shot-wayland-final-envalira-soldeu.jpg) |
| 16:40:07 | [164007-remote-server-remote-web-end.jpg](164007-remote-server-remote-web-end.jpg) |
| 16:40:07 | [164007-remote-server-remote-web-joined.jpg](164007-remote-server-remote-web-joined.jpg) |
| 16:40:07 | [164007-remote-server-remote-web-riding.jpg](164007-remote-server-remote-web-riding.jpg) |
| 16:40:12 | [164012-remote-server-remote-web-end.jpg](164012-remote-server-remote-web-end.jpg) |
| 16:40:12 | [164012-remote-server-remote-web-joined.jpg](164012-remote-server-remote-web-joined.jpg) |
| 16:40:12 | [164012-remote-server-remote-web-riding.jpg](164012-remote-server-remote-web-riding.jpg) |
| 16:43:42 | [164342-remote-server-joins-remote-web-joined.jpg](164342-remote-server-joins-remote-web-joined.jpg) |
| 16:47:01 | [164701-remote-server-joins-remote-web-joined.jpg](164701-remote-server-joins-remote-web-joined.jpg) |
| 16:47:27 | [164727-scenes-uh-probe1-uh-a-west.jpg](164727-scenes-uh-probe1-uh-a-west.jpg) |
| 16:47:53 | [164753-scenes-uh-probe1-uh-b-east.jpg](164753-scenes-uh-probe1-uh-b-east.jpg) |
| 16:48:19 | [164819-scenes-uh-probe1-uh-c-north.jpg](164819-scenes-uh-probe1-uh-c-north.jpg) |
| 16:48:42 | [164842-scenes-uh-probe1-uh-d-plane.jpg](164842-scenes-uh-probe1-uh-d-plane.jpg) |
| 16:49:58 | [164958-scenes-uh-probe2-uh-e-slope.jpg](164958-scenes-uh-probe2-uh-e-slope.jpg) |
| 16:50:07 | [165007-remote-server-joins-remote-web-joined.jpg](165007-remote-server-joins-remote-web-joined.jpg) |
| 16:50:21 | [165021-scenes-uh-probe2-uh-f-front.jpg](165021-scenes-uh-probe2-uh-f-front.jpg) |
| 16:50:44 | [165044-scenes-uh-probe2-uh-g-mummelsee.jpg](165044-scenes-uh-probe2-uh-g-mummelsee.jpg) |
| 16:51:07 | [165107-scenes-uh-probe2-uh-h-sunset.jpg](165107-scenes-uh-probe2-uh-h-sunset.jpg) |
| 16:52:00 | [165200-scenes-uh-probe2-uh-v-circle.jpg](165200-scenes-uh-probe2-uh-v-circle.jpg) |
| 16:52:15 | [165215-scenes-uh-probe2-uh-v-circle.mp4](165215-scenes-uh-probe2-uh-v-circle.mp4) |
| 16:53:17 | [165317-remote-server-joins-remote-web-joined.jpg](165317-remote-server-joins-remote-web-joined.jpg) |
| 16:53:47 | [165347-scenes-unicorn-hornisgrinde-final-unicorn-hornisgrinde-tower.jpg](165347-scenes-unicorn-hornisgrinde-final-unicorn-hornisgrinde-tower.jpg) |
| 16:54:10 | [165410-scenes-unicorn-hornisgrinde-final-unicorn-hornisgrinde-plateau.jpg](165410-scenes-unicorn-hornisgrinde-final-unicorn-hornisgrinde-plateau.jpg) |
| 16:54:33 | [165433-scenes-unicorn-hornisgrinde-final-unicorn-hornisgrinde-sunset.jpg](165433-scenes-unicorn-hornisgrinde-final-unicorn-hornisgrinde-sunset.jpg) |
| 16:55:27 | [165527-scenes-unicorn-hornisgrinde-final-unicorn-hornisgrinde-orbit-video.jpg](165527-scenes-unicorn-hornisgrinde-final-unicorn-hornisgrinde-orbit-video.jpg) |
| 16:55:41 | [165541-scenes-unicorn-hornisgrinde-final-unicorn-hornisgrinde-orbit-video.mp4](165541-scenes-unicorn-hornisgrinde-final-unicorn-hornisgrinde-orbit-video.mp4) |
| 16:56:10 | [165610-unicorn-hornisgrinde-unicorn-hornisgrinde-orbit-720p.mp4](165610-unicorn-hornisgrinde-unicorn-hornisgrinde-orbit-720p.mp4) |
| 16:56:39 | [165639-remote-server-joins-remote-web-joined.jpg](165639-remote-server-joins-remote-web-joined.jpg) |
| 17:00:00 | [170000-remote-server-joins-remote-web-joined.jpg](170000-remote-server-joins-remote-web-joined.jpg) |
| 17:03:06 | [170306-remote-server-joins-remote-web-joined.jpg](170306-remote-server-joins-remote-web-joined.jpg) |
| 17:06:26 | [170626-remote-server-joins-remote-web-joined.jpg](170626-remote-server-joins-remote-web-joined.jpg) |
| 17:09:51 | [170951-remote-server-desktop.jpg](170951-remote-server-desktop.jpg) |
| 17:09:53 | [170953-remote-server-remote-web-end.jpg](170953-remote-server-remote-web-end.jpg) |
| 17:09:53 | [170953-remote-server-remote-web-joined.jpg](170953-remote-server-remote-web-joined.jpg) |
| 17:09:53 | [170953-remote-server-remote-web-riding.jpg](170953-remote-server-remote-web-riding.jpg) |
| 17:09:58 | [170958-remote-server-remote-web-end.jpg](170958-remote-server-remote-web-end.jpg) |
| 17:09:58 | [170958-remote-server-remote-web-joined.jpg](170958-remote-server-remote-web-joined.jpg) |
| 17:09:58 | [170958-remote-server-remote-web-riding.jpg](170958-remote-server-remote-web-riding.jpg) |
| 18:54:19 | [185419-scenes-andorra-r1-readme-andorra-envalira.jpg](185419-scenes-andorra-r1-readme-andorra-envalira.jpg) |
| 18:54:36 | [185436-scenes-andorra-r1-readme-andorra-envalira-winter.jpg](185436-scenes-andorra-r1-readme-andorra-envalira-winter.jpg) |
| 18:54:53 | [185453-scenes-andorra-r1-readme-andorra-gallina.jpg](185453-scenes-andorra-r1-readme-andorra-gallina.jpg) |
| 18:55:10 | [185510-scenes-andorra-r1-readme-andorra-vella.jpg](185510-scenes-andorra-r1-readme-andorra-vella.jpg) |
| 18:55:27 | [185527-scenes-andorra-r1-readme-andorra-arcalis.jpg](185527-scenes-andorra-r1-readme-andorra-arcalis.jpg) |
| 18:55:40 | [185540-scenes-andorra-r1-readme-andorra-unicorn.jpg](185540-scenes-andorra-r1-readme-andorra-unicorn.jpg) |
| 18:55:57 | [185557-scenes-andorra-r1-readme-andorra-dawn.jpg](185557-scenes-andorra-r1-readme-andorra-dawn.jpg) |
| 18:57:04 | [185704-scenes-andorra-r2-readme-andorra-envalira.jpg](185704-scenes-andorra-r2-readme-andorra-envalira.jpg) |
| 18:57:21 | [185721-scenes-andorra-r2-readme-andorra-envalira-winter.jpg](185721-scenes-andorra-r2-readme-andorra-envalira-winter.jpg) |
| 18:57:38 | [185738-scenes-andorra-r2-readme-andorra-gallina.jpg](185738-scenes-andorra-r2-readme-andorra-gallina.jpg) |
| 18:57:55 | [185755-scenes-andorra-r2-readme-andorra-vella.jpg](185755-scenes-andorra-r2-readme-andorra-vella.jpg) |
| 18:58:12 | [185812-scenes-andorra-r2-readme-andorra-arcalis.jpg](185812-scenes-andorra-r2-readme-andorra-arcalis.jpg) |
| 18:58:29 | [185829-scenes-andorra-r2-readme-andorra-dawn.jpg](185829-scenes-andorra-r2-readme-andorra-dawn.jpg) |
| 18:58:57 | [185857-scenes-andorra-r2-readme-andorra-envalira-video.jpg](185857-scenes-andorra-r2-readme-andorra-envalira-video.jpg) |
| 18:59:09 | [185909-scenes-andorra-r2-readme-andorra-envalira-video.mp4](185909-scenes-andorra-r2-readme-andorra-envalira-video.mp4) |
| 18:59:58 | [185958-scenes-andorra-r2-readme-andorra-envalira-video-small.mp4](185958-scenes-andorra-r2-readme-andorra-envalira-video-small.mp4) |
| 19:00:10 | [190010-scenes-andorra-r3-readme-andorra-envalira.jpg](190010-scenes-andorra-r3-readme-andorra-envalira.jpg) |
| 19:00:27 | [190027-scenes-andorra-r3-readme-andorra-envalira-winter.jpg](190027-scenes-andorra-r3-readme-andorra-envalira-winter.jpg) |
| 19:00:44 | [190044-scenes-andorra-r3-readme-andorra-vella.jpg](190044-scenes-andorra-r3-readme-andorra-vella.jpg) |
| 19:01:01 | [190101-scenes-andorra-r3-readme-andorra-dawn.jpg](190101-scenes-andorra-r3-readme-andorra-dawn.jpg) |
| 19:10:07 | [191007-together-20261126-remote-web-end.jpg](191007-together-20261126-remote-web-end.jpg) |
| 19:10:07 | [191007-together-20261126-remote-web-joined.jpg](191007-together-20261126-remote-web-joined.jpg) |
| 19:10:07 | [191007-together-20261126-remote-web-riding.jpg](191007-together-20261126-remote-web-riding.jpg) |
| 19:10:15 | [191015-together-20261126-remote-web-end.jpg](191015-together-20261126-remote-web-end.jpg) |
| 19:10:15 | [191015-together-20261126-remote-web-joined.jpg](191015-together-20261126-remote-web-joined.jpg) |
| 19:10:15 | [191015-together-20261126-remote-web-riding.jpg](191015-together-20261126-remote-web-riding.jpg) |
| 19:11:47 | [191147-together-20261126-preview-credits.jpg](191147-together-20261126-preview-credits.jpg) |
| 19:12:05 | [191205-together-20261126-preview-start.jpg](191205-together-20261126-preview-start.jpg) |
| 21:53:14 | [215314-water-ground-before-readme-andorra-envalira.jpg](215314-water-ground-before-readme-andorra-envalira.jpg) |
| 21:53:32 | [215332-water-ground-before-readme-andorra-envalira-winter.jpg](215332-water-ground-before-readme-andorra-envalira-winter.jpg) |
| 21:53:46 | [215346-water-ground-before-readme-andorra-unicorn.jpg](215346-water-ground-before-readme-andorra-unicorn.jpg) |
| 21:54:18 | [215418-water-ground-before-wg-mummelsee-above.jpg](215418-water-ground-before-wg-mummelsee-above.jpg) |
| 21:54:55 | [215455-water-ground-before-wg-titisee.jpg](215455-water-ground-before-wg-titisee.jpg) |
| 21:55:11 | [215511-water-ground-before-wg-rhine.jpg](215511-water-ground-before-wg-rhine.jpg) |
| 21:55:26 | [215526-water-ground-before-wg-valira.jpg](215526-water-ground-before-wg-valira.jpg) |
| 21:55:51 | [215551-water-ground-before-wg-hornisgrinde-far.jpg](215551-water-ground-before-wg-hornisgrinde-far.jpg) |
| 21:56:03 | [215603-water-ground-before-wg-envalira-pass.jpg](215603-water-ground-before-wg-envalira-pass.jpg) |
| 21:56:30 | [215630-water-ground-before-wg-teide-high.jpg](215630-water-ground-before-wg-teide-high.jpg) |
| 22:15:02 | [221502-status-page-local-phone.png](221502-status-page-local-phone.png) |
| 22:34:49 | [223449-42e87345-dirty-shot-fly-join.jpg](223449-42e87345-dirty-shot-fly-join.jpg) |
| 22:49:32 | [224932-web-log-web-log-iphone-no-wasm.png](224932-web-log-web-log-iphone-no-wasm.png) |
| 22:49:32 | [224932-web-log-web-log-iphone-too-old.png](224932-web-log-web-log-iphone-too-old.png) |
| 22:50:02 | [225002-water-ground-after-readme-andorra-arcalis.jpg](225002-water-ground-after-readme-andorra-arcalis.jpg) |
| 22:50:02 | [225002-water-ground-after-readme-andorra-envalira-winter.jpg](225002-water-ground-after-readme-andorra-envalira-winter.jpg) |
| 22:50:02 | [225002-water-ground-after-readme-andorra-envalira.jpg](225002-water-ground-after-readme-andorra-envalira.jpg) |
| 22:50:02 | [225002-water-ground-after-readme-andorra-unicorn.jpg](225002-water-ground-after-readme-andorra-unicorn.jpg) |
| 22:50:02 | [225002-water-ground-after-readme-teide.jpg](225002-water-ground-after-readme-teide.jpg) |
| 22:50:02 | [225002-water-ground-after-showcase-mummelsee.jpg](225002-water-ground-after-showcase-mummelsee.jpg) |
| 22:50:02 | [225002-water-ground-after-showcase-schluchsee.jpg](225002-water-ground-after-showcase-schluchsee.jpg) |
| 22:50:02 | [225002-water-ground-after-wg-envalira-pass.jpg](225002-water-ground-after-wg-envalira-pass.jpg) |
| 22:50:02 | [225002-water-ground-after-wg-hornisgrinde-far-noon.jpg](225002-water-ground-after-wg-hornisgrinde-far-noon.jpg) |
| 22:50:02 | [225002-water-ground-after-wg-hornisgrinde-far.jpg](225002-water-ground-after-wg-hornisgrinde-far.jpg) |
| 22:50:02 | [225002-water-ground-after-wg-mummelsee-above.jpg](225002-water-ground-after-wg-mummelsee-above.jpg) |
| 22:50:02 | [225002-water-ground-after-wg-rhine.jpg](225002-water-ground-after-wg-rhine.jpg) |
| 22:50:02 | [225002-water-ground-after-wg-teide-high.jpg](225002-water-ground-after-wg-teide-high.jpg) |
| 22:50:02 | [225002-water-ground-after-wg-titisee.jpg](225002-water-ground-after-wg-titisee.jpg) |
| 22:50:02 | [225002-water-ground-after-wg-valira.jpg](225002-water-ground-after-wg-valira.jpg) |
| 23:12:24 | [231224-34eac71b-dirty-shot-ocw.jpg](231224-34eac71b-dirty-shot-ocw.jpg) |
| 23:12:34 | [231234-34eac71b-dirty-shot-wayland-ocw-wayland.jpg](231234-34eac71b-dirty-shot-wayland-ocw-wayland.jpg) |
| 23:16:59 | [231659-status-page-live-phone.png](231659-status-page-live-phone.png) |
| 23:17:24 | [231724-status-page-live-desktop.png](231724-status-page-live-desktop.png) |
| 23:17:50 | [231750-status-page-live-phone-dark.png](231750-status-page-live-phone-dark.png) |
| 23:17:51 | [231751-status-page-voice-remote-web-end.jpg](231751-status-page-voice-remote-web-end.jpg) |
| 23:17:51 | [231751-status-page-voice-remote-web-joined.jpg](231751-status-page-voice-remote-web-joined.jpg) |
| 23:17:51 | [231751-status-page-voice-remote-web-riding.jpg](231751-status-page-voice-remote-web-riding.jpg) |
| 23:21:11 | [232111-status-page-voice2-remote-web-end.jpg](232111-status-page-voice2-remote-web-end.jpg) |
| 23:21:11 | [232111-status-page-voice2-remote-web-joined.jpg](232111-status-page-voice2-remote-web-joined.jpg) |
| 23:21:11 | [232111-status-page-voice2-remote-web-riding.jpg](232111-status-page-voice2-remote-web-riding.jpg) |
| 23:21:20 | [232120-status-page-voice2-remote-web-end.jpg](232120-status-page-voice2-remote-web-end.jpg) |
| 23:21:20 | [232120-status-page-voice2-remote-web-joined.jpg](232120-status-page-voice2-remote-web-joined.jpg) |
| 23:21:20 | [232120-status-page-voice2-remote-web-riding.jpg](232120-status-page-voice2-remote-web-riding.jpg) |
| 23:24:34 | [232434-web-log-web-log-iphone-no-wasm.png](232434-web-log-web-log-iphone-no-wasm.png) |
| 23:24:34 | [232434-web-log-web-log-iphone-too-old.png](232434-web-log-web-log-iphone-too-old.png) |
| 23:26:27 | [232627-web-log-web-log-android-no-gpu.png](232627-web-log-web-log-android-no-gpu.png) |
| 23:26:27 | [232627-web-log-web-log-android-no-wasm.png](232627-web-log-web-log-android-no-wasm.png) |
| 23:26:27 | [232627-web-log-web-log-android-too-old.png](232627-web-log-web-log-android-too-old.png) |
| 23:54:19 | [235419-42e87345-dirty-shot-ocw.jpg](235419-42e87345-dirty-shot-ocw.jpg) |
| 23:54:30 | [235430-42e87345-dirty-shot-wayland-ocw-wayland.jpg](235430-42e87345-dirty-shot-wayland-ocw-wayland.jpg) |
