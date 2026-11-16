---
name: diag18b_query_advice_six_runs_not_confirmed_2026_11_09
description: "[VERIFIED] No (DIAG18B): pooled 6 runs Claude eachkw-each +8.0/108, Codex each-eachkw +9.6, bar 18; runs 4-6 alone +0.0 and +1.5 of 54"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T04:45:15+04:00
  status: provisional
  evidence: "the private brain repository 132eb5e1b0 12_cognitive_architecture/brain_improvement/DIAG18_20261109/README_B.md"
---

Does the query advice (keyword-style questions for Claude, plain each-questions for Codex) hold up with six runs per cell? No (9 Nov, DIAG18B, DIAG18 Addendum B, prereg c548f3c700, results 132eb5e1b0). Pooled with DIAG18's runs 1-3, Claude eachkw - each is +8.0 of 108 and Codex each - eachkw +9.6, bar 18. Runs 4-6 alone: Claude +0.0 of 54, Codex +1.5 (+3.0 with the one leak-voided run counted back in). The DIAG18 lift came almost entirely from its first three runs.

What moved with the lift: Claude's eachkw arm asked more questions in DIAG18 (42-52 a run against 27-38) and surfaced more planted notes (43 vs 35 of 54). In runs 4-6 both Claude arms asked exactly 100 questions in total and surfaced 36 and 34, and they scored the same. The advice text did not reliably change how much Claude asks; the question count did the work when it changed. Codex keyword questions are shorter (4.6-6.1 words vs 6.9-10.5) and surface fewer planted notes every time (32 vs 42, 36 vs 44 of 54), but in runs 4-6 that barely reached the points.

Validity: 12 of 12 passed reaudit. each_codex_Dr4 is void in the primary score because the leak check hit `.verify_gate_turns`, which appeared in a recall row quoting an older scar memory's description; the run never opened that file. That marker is a substring of a readable memory's slug, so any recall that surfaces that scar trips it. Before the next test, change the marker to the file path (`dreaming/.verify_gate_turns`) or exempt recall rows. Controls: C on every control line, both runtimes.

**Why:** a +8 on three runs with a bar of 9 looked like "same direction, half size". Three more runs put that half at zero for Claude. A three-run cell cannot size an effect this small.

**How to apply:** do not ship the query advice as a default for either runtime on this evidence. If it is tested again, fix the question count (or measure it as the mediator) and give each cell at least six runs before reading a difference under 10 of 54. Harness: ~/.claude/compute/keys_private/diag18b (private). Related: [[diag18_query_advice_fresh_items_not_confirmed_2026_11_09]], [[diag17c_query_advice_lifts_claude_recall_29_43_hurts_codex_40_29_2026_11_09]], [[follow_up_test_harness_must_deny_prior_run_results_2026_11_09]].

