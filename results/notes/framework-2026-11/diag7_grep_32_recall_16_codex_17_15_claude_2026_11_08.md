---
name: diag7_grep_32_recall_16_codex_17_15_agent_11_08
description: "Does recall or reading the memory files do the brain's work at 5 calls? Files on Codex (grep 32, recall 16 of 36), neither on Claude (17, 15); Codex bundled symptoms per recall"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T15:28:06+04:00
  status: verified
  evidence: "brain-repo 12_cognitive_architecture/brain_improvement/DIAG7_20261108 (prereg 9bca58d4da, results 052b4ca9e8)"
---

Does recall or reading the memory files do the brain's work at 5 tool calls? On Codex the files, two to one; on Claude neither (8 Nov, DIAG7).

DIAG5's items byte for byte. DIAG6's brain arm split in two at the same 5-call budget: recall (brain.py recall/node only, up to 5) and grep (the memory folder and brain repos with any tool, no brain.py). Codex gpt-6.1-sol high and Claude opus-5-5 high, 3 runs each, hooks off, store brain-graph-full-2026-11-07. Prereg 9bca58d4da before the runs; judged blind.

- Codex: grep 11, 11, 10 = 32 of 36; recall 5, 5, 6 = 16. Grep ahead on 9 plants, recall on none.
- Claude: grep 6, 7, 4 = 17; recall 5, 6, 4 = 15 (reading B; 13.5 scaled with Dr2 void under the recall rule, a false positive on the verdicts text). Recall ahead on COMPACT_WINDOW, DEPTH_SHALLOW, MAIL_ID; grep ahead on COMMA_CUT, IMPORT_REWRITE, QMARK_DROP, ACC_PREFIX.
- Decoys 18 of 18 except grep Claude 17 (the comma-cut look-alike taken once). Claude recall runs took about 100 s, Claude grep about 300 s; Codex both about 140 s.

Why: Codex bundled two or three symptoms into each long recall question; Claude asked one short keyword-like question per symptom, and found plants Codex's recall missed (COMPACT_WINDOW 3 against 0). Grep won on Codex because memory slugs are descriptive: list the folder, match slugs to symptoms, read the hits in one python call.

Next: split a multi-topic recall question into one search per topic inside brain.py and score it on these items; tell agents to ask one symptom per recall.

Rows and scripts: brain-repo 12_cognitive_architecture/brain_improvement/DIAG7_20261108 (last commit 052b4ca9e8). Follows [[diag6_five_calls_brain_27_12_bare_0_2026_11_08]]; harness fault in [[rules_appended_below_main_guard_unseen_by_script_run_2026_11_08]].


Correction (8 Nov 15:31, RECALL6): the bundling explanation above does not hold. Splitting the questions left the surfaced plant sources at 21 of 36 on Codex, more than Claude's 15. The gap is the recall arm seeing only description lines while the grep arm read bodies. See [[recall6_split_bundled_recall_21_to_21_bodies_not_ranking_2026_11_08]].

Correction (15:48): the explanation above does not hold. Most of the recall arm's misses were plants it never asked about (sources beyond rank 60 for every question the run sent: 12 of 20 Codex, 20 of 21 Claude); the limit was questions per call. With recall --each the same arm named 26 and 29 of 36. See [[diag8_recall_each_26_29_of_36_vs_16_15_coverage_not_bodies_2026_11_08]].
