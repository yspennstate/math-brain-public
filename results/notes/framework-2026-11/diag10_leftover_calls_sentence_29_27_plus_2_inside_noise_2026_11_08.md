---
name: diag10_leftover_calls_sentence_29_27_plus_2_inside_noise_2026_11_08
description: "Does telling the mixed brain arm to spend leftover calls reading memory files help? Not measurably (DIAG10): Codex 29, Claude 27 of 36 vs 27, 25 without; runs used their calls; misses are mechanism-wording gaps"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T16:09:17+04:00
  status: verified
  evidence: "the private brain repository 12_cognitive_architecture/brain_improvement/DIAG10_20261108 ef58c8be80"
---

Does telling the mixed arm (recall --each plus memory-file reads, 5 tool calls) to spend its leftover calls reading the memory files help? Not measurably (8 Nov, DIAG10): Codex 29 and Claude 27 of 36 planted causes, against 27 and 25 without the sentence (DIAG9). +2 each, short of the pre-registered gain of 6.

Same items, key, store (brain-graph-full-2026-11-07, 16,811,666 edges, sidecar 242,841 link rows), caps and judging rule as DIAG9; one sentence added to the prompt. Codex gpt-6.1-sol high and Claude opus-5-5 high, hooks off, 3 runs each. Pre-registered (1103706788); judged blind; 6 of 6 valid, leakcheck clean, decoys and controls 18 of 18 on both runtimes.

- The sentence changed behaviour: no run stopped early (DIAG9: three of six left 3 calls unused). Codex made one --each call with all 24 questions, then 4 reads or greps of the memory folder; Claude made 2 recalls and a node read, then 1 or 2 reads.
- The better single tool still leads: grep 32 on Codex (3 ahead), --each 29 on Claude (2 ahead). Gaps this small sit inside judging drift between sittings ([[a_regrade_moves_statement_verdicts_compare_arms_within_one_pass_2026_09_29]]).
- Misses left: DEPTH_SHALLOW on every Codex run (all said damaged refs), CTIME_REPLACE and COPIED_SIDECAR on every Claude run (named the sidecar binding, never ctime on rename or the copy's new identity).

How to apply: more reading is not the lever. The leftover misses are memories that name the mechanism in words the symptom does not use, so the next thing to test is recall, not the prompt: aliases or symptom phrasing on those memories, or a recall step that pulls a memory's mechanism line into the brief.

Scar from the run: the leak marker bt2_arms/DIAG1 is a prefix of bt2_arms/DIAG10, so every DIAG10 run first read as a leak; mask the run's own folder before matching (leakcheck.py now does).

Files: brain-repo 12_cognitive_architecture/brain_improvement/DIAG10_20261108 (results ef58c8be80). Related: [[diag9_mixed_each_plus_files_27_25_no_gain_over_best_single_tool_2026_11_08]], [[diag8_recall_each_26_29_of_36_vs_16_15_coverage_not_bodies_2026_11_08]], [[diag7_grep_32_recall_16_codex_17_15_agent_11_08]].

Addendum (8 Nov 16:2x): in DIAG10 every recall call carried 7 or 8 questions because the prompt said 'up to 8'; Claude's 2 recall calls left items unasked (CTIME_REPLACE's memory was in no Claude run's context). DIAG11 lifted the cap to 24 and Claude still asked 14 to 18, so the cap was not the cause; see [[diag11_each_cap_24_claude_still_asks_15_codex_30_claude_29_2026_11_08]].
