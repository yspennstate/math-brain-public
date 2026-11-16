---
name: diag9_mixed_each_plus_files_27_25_no_gain_over_best_single_tool_2026_11_08
description: "[VERIFIED] Should an agent with recall --each also read the memory files at 5 tool calls? It did not help (8 Nov, DIAG9): Codex 27 and Claude 25 of 36 against 32 (grep alone) and 29 (--each alone); arms stopped after --each with calls unused"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T15:58:57+04:00
  status: verified
  evidence: "brain-repo 12_cognitive_architecture/brain_improvement/DIAG9_20261108 (prereg 526a8fd0ba, results e7f7c3f6b2)"
---

Does giving an agent both recall --each and direct reads of the memory files beat the better single tool at 5 tool calls? No (8 Nov, DIAG9): Codex 27 of 36 planted causes (grep alone 32), Claude 25 (--each alone 29).

DIAG5's items byte for byte. One arm, mixed: DIAG6's brain arm prompt (recall/node plus reads of the memory folder and brain repos) with the blinded-test line, up to 5 brain.py calls, and the --each sentence from DIAG8. Codex gpt-6.1-sol high and Claude opus-5-5 high, hooks off, 3 runs each. Store brain-graph-full-2026-11-07, 16,811,666 edges, sidecar 242,841 link rows. Pre-registered (526a8fd0ba); judged blind; 6 of 6 valid, leakcheck clean; decoys 18 of 18 and controls 18 of 18 on both runtimes.

- Codex 8, 9, 10 = 27; Claude 8, 9, 8 = 25. The gaps to the better single tool (5 and 4) are inside the pre-registered no-effect band and inside judging drift between sittings (a regrade moved 6 to 9 verdicts per arm, [[a_regrade_moves_statement_verdicts_compare_arms_within_one_pass_2026_09_29]]).
- Every run asked recall --each first and mostly stopped there: three of six runs ended after 2 recall calls with 3 of 5 calls unused; only two runs read files.
- Against DIAG6's brain arm (same two tools, no --each, 3 recalls of one question): Codex 27 = 27, Claude 25 against 12.

How to apply: --each is the right first move, but do not stop on it. With calls left, read the memory files for the symptoms recall answered weakly; on Codex the whole-file reads are what found the extra plants (COMPACT_WINDOW, DEPTH_SHALLOW, CTIME_REPLACE, COPIED_SIDECAR). The best single tool per runtime is still grep on Codex and --each on Claude.

Files: brain-repo 12_cognitive_architecture/brain_improvement/DIAG9_20261108 (results e7f7c3f6b2). Related: [[diag8_recall_each_26_29_of_36_vs_16_15_coverage_not_bodies_2026_11_08]] (the --each result), [[diag7_grep_32_recall_16_codex_17_15_agent_11_08]], [[diag6_five_calls_brain_27_12_bare_0_2026_11_08]].

