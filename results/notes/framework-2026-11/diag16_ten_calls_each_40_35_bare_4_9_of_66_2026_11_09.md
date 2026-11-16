---
name: diag16_ten_calls_each_40_35_bare_4_9_of_66_2026_11_09
description: "Yes (DIAG16): with 10 tool calls and no rewrites, brain arms beat bare on two-memory faults, each 40/35 vs bare 4/9 of 66, two blind judges agree"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T01:30:56+04:00
  status: verified
  evidence: "brain-repo 12_cognitive_architecture/brain_improvement/DIAG16_20261109 0384f056d9"
---

Does the brain beat no brain on two-memory faults once the arms get ten tool calls? Yes, by a wide margin (DIAG16, 9 Nov 01:2x, an agent on the a second machine). Points of 66 (11 pairs x 3 runs x 2 causes): Codex bare 4, each 40, grep 28.5; Claude bare 9, each 35, grep 23. The pre-registered bar was beating bare by 11; every brain arm clears it on both runtimes. Runs naming both causes: bare 0 of 33 on both, each 11 and 8 of 33. Controls 18 of 18 in every arm.

The same setup as DIAG15 (which sat at the floor, brain arms 6-9 of 66, bare 0), with two changes only: 10 tool calls instead of 5, and pairs flagged by the clue check dropped instead of rewritten (24 written, 11 clear). New items from a fresh draw of 64 scars (pool 647, seed 20261117).

How sure: judged blind by line id with rulings written before the runmaps were opened. A strict re-mark that takes back all 41 lenient marks still leaves each +32 (Codex) and +27 (Claude), grep +24 and +13. A second blind judge (Codex gpt-6.1-sol high, base rules only, none of my rulings) agreed on 277 of 306 lines, always stricter where it differed, and scored Codex 0 / 35 / 25.5 and Claude 3 / 29 / 18. Pair by pair, each beats bare on 10 of 11 pairs on both runtimes and loses on none. One Codex grep run is void (it read one of my compaction notes); scored back in, that arm gets 27, not more.

What it says: the join is limited by the budget for lookups, not by recall alone. Part A (plain recall on the symptom text, top 40) held both memories for 0 of 11 pairs, yet the agents got there by writing their own queries from the log, one cause at a time. The each arm (several queries per recall call) beat grep on both runtimes. DIAG16 cannot say which of the two changes did it; the clean next test is these 11 pairs at 5 calls.

Graph: brain-graph-full-2026-11-07, manifest 11,982,982 directed + 4,828,684 co = 16,811,666 edges; sidecar 243,298 link rows; BRAIN_RECALL_LOG=0, BRAIN_RECALL_REFRESH=0. Models Codex gpt-6.1-sol high and Claude opus-5-5 high, hooks off, 3 runs per arm.

Files: brain-repo 12_cognitive_architecture/brain_improvement/DIAG16_20261109/ (PREREG c89801e405, Addendum A b39253c36c, results 0384f056d9). Items and keys stay private in keys_private/diag16.

Related: [[diag15_two_memory_joins_brain_6_9_of_66_bare_0_below_bar_2026_11_08]] (the floor this lifts), [[diag15_pairs_not_linked_in_graph_3_of_11_walk_cannot_join_2026_11_09]], [[diag_regrade_drift_0_of_57_with_written_rulings_run_spread_sd_2_2026_11_08]] (the noise band: about 4 points of 12 there; here the gaps are 14 to 36 points of 66).

