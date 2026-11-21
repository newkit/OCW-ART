# OCW build diary – day 10, 2026-11-20

0 commits (0 merges), +0 / −0 lines, 4 images, 1 videos, 0 sounds.

## Commits

| Time | Commit | |
|---|---|---|

## Builds and build servers

0 build/test runs on the build machines, 0.0 h in total, 0 failed; 1440 server samples; cargo compiled 0 crates in 0.0 h, 0.0 h waiting for build slots.

| Machine | Runs | Hours | Cargo h | Crates | Waited h | Failed | Online |
|---|---|---|---|---|---|---|---|
| Weela | 0 | 0.0 | 0.0 | 0 | 0.0 | 0 | 0% |
| Win11Builder | 0 | 0.0 | 0.0 | 0 | 0.0 | 0 | 100% |
| leela | 0 | 0.0 | 0.0 | 0 | 0.0 | 0 | 100% |
| macos | 0 | 0.0 | 0.0 | 0 | 0.0 | 0 | 100% |
| marge | 0 | 0.0 | 0.0 | 0 | 0.0 | 0 | 100% |

## Incidents

4 collected (disk-full 1, machine-offline 2, machine-online 1), 1 with root-cause notes ([incidents.md](incidents.md)).

| Time | Kind | Machine | What |
|---|---|---|---|
| 00:00 | machine-offline | Weela | Weela unreachable (no route to host) |
| 00:00 | disk-full | Win11Builder | disk C: on Win11Builder at 91 % |
| 21:04 | machine-offline | Win11Builder | Win11Builder unreachable (timeout) |
| 21:06 | machine-online | Win11Builder | Win11Builder back online |

### Root-cause notes


Root-cause notes by the coordinator (docs/ART-PROJECT.md §2.6). The collected
entries (journal, build log) are in `logs/build-log/incidents.jsonl` and in
the journal's "Incidents" section.

### 00:00 – No tokens all day: the weekly limit was reached

- **What happened:** nothing was built on 2026-11-20. On the evening of
  2026-11-19 the coordinator's agents stopped with "You've hit your weekly
  limit · resets Nov 21, 9am", and the coordinator could not start new
  ones. The day has no commits, no merges, no build runs, no prompts, no
  tokens and no pictures of the game.
- **Cause:** the account's weekly token limit. 2026-11-19 alone used
  1.59 billion tokens (5,055 model messages, 21 agent jobs); most of them
  were cache reads.
- **Effect:** a day without a build. Two jobs of 19 November stayed open:
  the phone-sized HUD (reported) and the J2 follow-up (grade limits,
  rebuild; started 18:11). The build machines idled; the dashboard kept
  sampling them every minute (1,440 samples).
- **Fix:** wait for the reset on 2026-11-21 at 09:00.
- **Follow-up:** the diary tells the day anyway (a day without media still
  gets its journal and README entry): an ASCII crab turning its pockets out
  (`diary.py crab`, ART-PROJECT §4.1) over a quiet ambient bed. Its clip
  and three stills are the day folder's only pictures.

## Media

| Time | File |
|---|---|
| 12:00:00 | [120000-no-tokens-crab-pockets-0-terminal.jpg](120000-no-tokens-crab-pockets-0-terminal.jpg) |
| 12:00:00 | [120000-no-tokens-crab-pockets-1-limit.jpg](120000-no-tokens-crab-pockets-1-limit.jpg) |
| 12:00:00 | [120000-no-tokens-crab-pockets-2-pockets.jpg](120000-no-tokens-crab-pockets-2-pockets.jpg) |
| 12:00:00 | [120000-no-tokens-crab-pockets-3-moth.jpg](120000-no-tokens-crab-pockets-3-moth.jpg) |
| 12:00:00 | [120000-no-tokens-crab-pockets.mp4](120000-no-tokens-crab-pockets.mp4) |
