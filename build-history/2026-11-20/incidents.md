# Incidents – 2026-11-20

Root-cause notes by the coordinator (docs/ART-PROJECT.md §2.6). The collected
entries (journal, build log) are in `logs/build-log/incidents.jsonl` and in
the journal's "Incidents" section.

## 00:00 – No tokens all day: the weekly limit was reached

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
