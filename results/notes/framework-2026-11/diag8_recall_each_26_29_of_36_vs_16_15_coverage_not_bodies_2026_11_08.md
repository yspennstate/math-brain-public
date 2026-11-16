---
name: diag8_recall_each_26_29_of_36_vs_16_15_coverage_not_bodies_2026_11_08
description: "[VERIFIED] Several symptoms to look up with recall? Send them in one call with --each (8 Nov, DIAG8): Codex 26 and Claude 29 of 36 planted causes against 16 and 15 for one question a call; the misses were questions never asked"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T15:48:38+04:00
  status: verified
  evidence: "brain-repo 12_cognitive_architecture/brain_improvement/DIAG8_20261108 (prereg d32de44aca, results 400ccaefd9)"
---

Does recall --each (several questions in one call) close the recall-only gap at 5 tool calls? Yes (8 Nov, DIAG8): Codex 26 of 36 planted causes against DIAG7 recall's 16, Claude 29 against 15.

DIAG5's 24 items (12 plants, 6 decoys, 6 controls) byte for byte, DIAG7's recall arm prompt with the one-question sentence replaced by one teaching `brain.py recall "<q1>" --each "<q2>" --each "<q3>"` (-n per question, default 3). Same deny rules, 5 tool calls, no --or. Codex gpt-6.1-sol high and Claude opus-5-5 high, hooks off, 3 runs each. Store brain-graph-full-2026-11-07, 16,811,666 edges, sidecar 242,841 link rows. Pre-registered (d32de44aca) before any run; judged blind.

- Codex: 9, 9, 8 = 26 (DIAG7 recall 16, grep 32). Ahead of recall on 10 plant-runs, behind on none; behind grep by 6.
- Claude: 9, 10, 10 = 29 (DIAG7 recall 15, grep 17). Ahead of both.
- Decoys 18 of 18 and controls 18 of 18 on each runtime. 6 of 6 runs valid, leakcheck 6 of 6 clean.
- Every run sent all its questions in 3 recall calls: Codex 24 (one per item), Claude 20, at -n 2 or 3.

Why it works: DIAG7's recall arm missed plants it never asked about. Their sources ranked beyond 60 for every question the run sent (12 of 20 Codex misses, 20 of 21 Claude). Each symptom asked alone puts 11 of 12 sources in a top 8. With 12 symptoms and 5 calls, one question a call cannot cover the items; grep covered them by reading every matching file in one call. Two earlier explanations were wrong: bundled questions (RECALL6, splitting changed nothing) and description-only output (bodies could have added at most 5 and 1).

How to apply: when a task has several separate symptoms or questions, send them to recall in ONE call with --each, not one call each and not bundled into one sentence. On Codex, reading the memory files whole still finds 6 more (the plants whose source ranks low for the symptom's own words: DEPTH_SHALLOW, CTIME_REPLACE, COPIED_SIDECAR).

Caveats: DIAG7 is a same-day, not concurrent, comparison judged in a separate sitting; the memory index has grown since DIAG7.

Files: brain-repo 12_cognitive_architecture/brain_improvement/DIAG8_20261108 (results 400ccaefd9), with the coverage analysis in DIAG7_20261108/split (depth.py, ceiling.py, ceiling_each.py). Related: [[diag7_grep_32_recall_16_codex_17_15_agent_11_08]], [[recall6_split_bundled_recall_21_to_21_bodies_not_ranking_2026_11_08]], [[diag6_five_calls_brain_27_12_bare_0_2026_11_08]].

