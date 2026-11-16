---
name: diag17c_query_advice_lifts_claude_recall_29_43_hurts_codex_40_29_2026_11_09
description: "Does one paragraph of query advice help brain recall? Claude 29 -> 43 of 66, Codex 40 -> 29: the advice is runtime-specific (DIAG17C)"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T03:23:34+04:00
  status: provisional
  evidence: "brain-repo brain_improvement/DIAG17_20261109 252219d878"
---

Does one paragraph of query advice make brain recall work better? For Claude yes, for Codex it hurt (DIAG17
Addendum C, 9 Nov 2026, exploratory).

The advice, added to the each arm's prompt (arm eachkw): ask with a few distinctive words copied from the item (error
text, tool and file names, numbers), not a sentence carrying your guess; read the names that come back and open a
close one with node; sharpen the next question from what you read. Same items, tools and budget as DIAG17's each arm
(brain.py recall/node, 10 calls, 1200 s), 3 runs per runtime, all valid, leak clean, full brain
brain-graph-full-2026-11-07.

Judged blind with the 3 registered each runs shuffled into the same sheet, so each was re-judged too. Points of 66:
- Claude: each 29 (28 in the primary), eachkw 43. Both causes right 5 -> 11 of 33. eachkw higher on 7 items, lower on 2.
  43 is above Claude's clean-copy grep arm (37).
- Codex: each 40 (same per-item sums as the primary), eachkw 29. Both right 9 -> 1. eachkw higher on 1 item, lower on 6.
- Three rulings written mid-sheet (runmap still closed) moved Claude by 1 and 2; without them 28 vs 41.

Why, from the transcripts (qstyle17.py): the advice pushed each runtime toward the other's habit. Claude went from
30-51 questions of 11-13 words to 53-70 of 8-10 and surfaced planted notes in 41 of 66 cause-runs instead of 30.
Codex, already asking 56-72 short questions, took "open it with node" to heart (3-4 node reads), asked 32-48 and
surfaced 29 instead of 52. The score followed the surfaced count both ways.

How to apply: do not ship one query-advice paragraph to every runtime. For Claude agents using recall, "ask more,
shorter questions in the item's own words" is worth about 14 points of 66 here; for Codex, leave the prompt alone or
add nothing that spends calls. Caveats: 3 runs per arm, later time slot than the compared runs, run spread unmeasured.
A registered rerun (more runs, both arms in one wave) would settle it.

Files: brain-repo 12_cognitive_architecture/brain_improvement/DIAG17_20261109/ (252219d878;
PREREG Addendum C bdb7b545d1). Items, key and rulings stay private.
Related: [[diag17_fresh_draw_recall_beats_bare_loses_to_clean_grep_50_40_37_28_2026_11_09]],
[[diag16_ten_calls_each_40_35_bare_4_9_of_66_2026_11_09]], [[symlead1_symptom_lines_lift_recall_replicated_2026_11_08]].

Follow-up (9 Nov 04:07): on fresh items (DIAG18) the same direction at about half the size, Claude +8 and Codex -7 of 54, below the pre-registered bar of 9: [[diag18_query_advice_fresh_items_not_confirmed_2026_11_09]].
