---
name: diag22_grep_name_listing_not_claudes_gap_brain_beats_grepls_10_and_19_2026_11_09
description: "[PROVISIONAL] No (DIAG22): listing names moved Claude grep 23->27, brain still +10; the sentence cut Codex grep 42->30, brain +19 over grepls"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T07:10:12+04:00
  status: provisional
  evidence: "the private repository b1ec45f9a9 DIAG22_20261109/score22.txt"
---

No (DIAG22, 9 Nov 2026, pushed b1ec45f9a9 to the private repository, 12_cognitive_architecture/brain_improvement/DIAG22_20261109; prereg ce3c82236a).

Telling Claude's grep arm to list every file name first moved it 23 -> 27 of 72 (+4, inside the bar of 9); the brain arm (eachhi, 48+ questions) still beat it 37 to 27 (+10, items 5 up / 1 down / 6 tied). On Codex the same sentence hurt: grepls 30 against plain grep 42 (-12, 2 up / 6 down), although Codex's plain grep already listed every name in 3 of 3 runs. Brain vs grepls: Codex 49 to 30 (+19, 9/0/3). Brain vs plain grep replicated DIAG21: Claude +14 (was +13), Codex +7 (was +1, still inside the bar).

Same 18 items as DIAG21 (12 plants, 6 controls), 10 tool calls, 1200 s, brain-graph-full-2026-11-07 (16,811,666 edges), Codex gpt-6.1-sol high, Claude claude-opus-5-5 high, 3 runs per cell. 18/18 valid; one name-only leak hit kept (strict line drops it, no conclusion changes). Marks hashed 07:08 before runmaps; mark sums match the scorer (Codex 121, Claude 87).

What it means:
- The listing habit does not explain Claude's DIAG21 loss. Asked to list, Claude listed a filtered or truncated set in 2 of 3 runs (grep -v, head -500); the one full-listing run scored no better (per-protocol grepls 24).
- "Pick files from the names before searching inside them" costs Codex content search. Don't add that sentence to a grep arm; the plain grep rule is the stronger baseline.
- My prereg prediction was wrong on all four hypotheses.
- For DIAG23 (does grep's score come from the descriptive file names?), compare plain grep to grep over the hashed-name copy, not grepls.

Recall surfaced the planted notes 12-13 of 24 per Claude run and 18 of 24 per Codex run (qstyle22).


Follows [[diag21_brain_48q_beats_grep_claude_13_codex_ties_1_of_72_2026_11_09]] (the gap this tested), uses the 48+ question advice from [[diag20_asking_48_plus_beats_default_claude_5_codex_3p5_of_54_below_bar_2026_11_09]], and the surfacing split matches [[brain_arm_misses_are_surfacing_misses_seen_426_of_479_unseen_23_of_331_2026_11_09]].

Why Codex fell (07:2x, regex count over the six Codex grep transcripts, heuristic classes): plain grep runs searched inside files 5, 5 and 6 times (rg/grep with a pattern or a python body match) of 10 calls; grepls runs 0, 0 and 1, spending the rest on python name filters and reading files picked by name (9, 9, 6). The sentence turned Codex into a name-only searcher, which is why it scored lower although both arms listed every name.
