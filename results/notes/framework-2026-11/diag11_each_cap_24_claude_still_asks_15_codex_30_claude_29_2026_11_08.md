---
name: diag11_each_cap_24_claude_still_asks_15_codex_30_claude_29_2026_11_08
description: "Does lifting the 8-question cap on recall --each make the mixed brain arm cover more and score more? No (DIAG11): Claude still asked 14-18 of 24, named 29 (27 capped); Codex 30 (29); mixed now within 2 of the better single tool on both"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T16:18:57+04:00
  status: verified
  evidence: "the private brain repository 12_cognitive_architecture/brain_improvement/DIAG11_20261108 ffa621b2c8"
---

Does lifting the "up to 8 questions" cap on recall --each make the mixed brain arm ask about every item and name more planted causes? No (8 Nov, DIAG11): with room for 24, Claude's runs asked 18, 15 and 14 questions and named 29 of 36 (27 under the cap, DIAG10); Codex asked 20, 12, 20 and named 30 (29). Both gains are inside judging drift.

DIAG10's harness byte for byte, one word changed in the prompt (8 to 24). Store brain-graph-full-2026-11-07, 16,811,666 edges, sidecar 242,841 link rows. Codex gpt-6.1-sol high and Claude opus-5-5 high, hooks off, 3 runs each. Pre-registered (41be4bff64), judged blind, 6 of 6 valid, leakcheck clean. Decoys: Codex 18 of 18, Claude 17 of 18 (one run named the comma cut for the Tenerife row); controls 18 of 18.

- Claude picks about 15 of the 24 items to ask about whatever the cap allows, so in DIAG10 the cap was not what held Claude's coverage down.
- The mixed arm across DIAG9, DIAG10 and DIAG11: Claude 25, 27, 29; Codex 27, 29, 30. It now sits at the better single tool on Claude (--each 29) and 2 under grep on Codex (32).

How to apply: give agents one prompt, recall --each first and then file reads with the calls left; it comes within 2 plants of the better single tool on both runtimes. Do not spend more test rounds on the prompt; what is still missed (DEPTH_SHALLOW on Codex, CTIME_REPLACE and COPIED_SIDECAR on Claude) is in how the memories are worded.

Files: the private repository, 12_cognitive_architecture/brain_improvement/DIAG11_20261108 (results ffa621b2c8). Related: [[diag10_leftover_calls_sentence_29_27_plus_2_inside_noise_2026_11_08]] (the cap guess it tests), [[diag9_mixed_each_plus_files_27_25_no_gain_over_best_single_tool_2026_11_08]], [[diag8_recall_each_26_29_of_36_vs_16_15_coverage_not_bodies_2026_11_08]].

