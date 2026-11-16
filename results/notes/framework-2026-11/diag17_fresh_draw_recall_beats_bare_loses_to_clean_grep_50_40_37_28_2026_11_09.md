---
name: diag17_fresh_draw_recall_beats_bare_loses_to_clean_grep_50_40_37_28_2026_11_09
description: "Does brain recall beat no brain and grep on a fresh draw? Beats bare (Codex 40 vs 0, Claude 28 vs 3 of 66) but loses to grep on a clean memory copy (50, 37) (DIAG17)"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T03:08:09+04:00
  status: provisional
  evidence: "the private repository, brain_improvement/DIAG17_20261109 b923489ea4"
---

Does brain recall beat no brain, and beat grep over the same memories, on a fresh draw? Beats no brain by a mile;
loses to grep on a clean copy (DIAG17, 9 Nov 2026).

Design as DIAG16: 11 planted two-cause failures plus 6 clean controls, drawn fresh; Codex gpt-6.1-sol high and Claude
opus-5-5 high, 3 runs per arm, 10 tool calls, 1200 s, blind judging by shuffled run label, points out of 66.
Full brain: brain-graph-full-2026-11-07, 11,982,982 directed + 4,828,684 co pairs, sidecar 243,298 links.

Primary points /66 (Codex | Claude):
- bare 0 | 3 (Claude's 3 all on one item)
- each, brain recall 40 | 28
- grep on the first memory copy, 2 valid runs each, scaled: 37.5 | 25.5
- grep2 on the clean copy (supplementary, PREREG Addendum B): 50 | 37
- controls 144 of 144 lines right; 22 of 24 runs valid; leakcheck 24 of 24 clean.
- paired by item, each vs grep2: Codex 2 / 8 / 1 tied, Claude 2 / 6 / 3 tied.
- sensitivity: the voided Codex grep run scored back in gives 43; all runs gives Claude grep 27.

What it means: the memories carry the answers (no access, almost nothing found), but the recall tool is not the best
door to them; a model reading the files with grep did as well or better. Same shape as BVNB139 and AUDIT1. Recall
also served Codex far better than Claude (40 vs 28; Claude's recall runs scored 0 on two pairs in all three runs).
The grep -> grep2 gain mixes a cleaner copy with run spread; do not read it as the copy's effect alone.

Two traps found on the way, worth keeping:
- A grep corpus copied from the memory folder still teaches test vocabulary: 555 "Symptom as an agent meets it"
  header lines and 62 files naming earlier test series. One grep run typed a series name it read there and voided.
  Strip the header prefix and drop files naming test series before a grep arm runs (build_memsnap2.py).
- Part A's low ranks were real, not a broken index: a positive control found 48 of 48 notes by node and in the top 10
  when recalled by their own description; the contexts were simply worded far from the notes.

Judging limits: one judge, who also drew the items; item rulings written before any runmap was opened (private file
JUDGING_DIAG17.txt), marks hashed before unblinding. Items, key, sheets and rulings stay private.
Files: the private repository, 12_cognitive_architecture/brain_improvement/DIAG17_20261109/ (b923489ea4).
Related: [[diag16_ten_calls_each_40_35_bare_4_9_of_66_2026_11_09]], [[diag16b_five_calls_each_28_32_items_carry_lift_2026_11_09]],
[[bvnb139_brain_recall_ties_grep_on_the_memory_a_session_needed_2026_11_08]], [[audit1_script_audit_brain_ties_bare_2026_11_09]].

Follow-up: one paragraph of query advice in the recall prompt lifted Claude 29 -> 43 and dropped Codex 40 -> 29 on these items (exploratory) - [[diag17c_query_advice_lifts_claude_recall_29_43_hurts_codex_40_29_2026_11_09]]; DIAG18 repeats it on a fresh draw (prereg e2472268a5).
