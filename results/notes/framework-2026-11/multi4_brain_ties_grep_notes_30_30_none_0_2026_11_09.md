---
name: multi4_brain_ties_grep_notes_30_30_none_0_2026_11_09
description: "No (MULTI4): with notes made greppable, Codex BRAIN 30, NOTES 30, NONE 0 of 30 on two-session repairs; brain twice as slow (47 vs 25 s); MULTI3's win was a byte-budget artifact"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T21:04:16+04:00
  status: verified
  evidence: "MULTI4-BUILD runs/multi4_pilot01/codex/grades.json graded 20:57; private-repo d286390908"
---

Does the brain beat a grep over well-formed notes on two-session repairs? No, it ties (MULTI4 pilot01, Codex gpt-6.1-sol high, graded 9 Nov 2026 20:57). BRAIN 30 of 30, NOTES (one JSON line per finding, grep) 30 of 30, NONE 0 of 30. Paired BRAIN vs NOTES: both pass 30, neither alone 0. Both vs NONE: 30 to 0.

Setup: session 1 diagnoses, at least 7,200 s gap per task, session 2 repairs under 8 commands and 8,192 output bytes. Repair prompts in customer language, no task id, opaque dirs, repeated services and customers. t31 note deleted from both memory arms before repairs: no arm recovered it (gate PASS). BRAIN's t31 was invalid, 9,602 bytes from 8 commands spent hunting the deleted note. NOTES stayed within budget.

Time per repair, median: BRAIN 47.3 s, NOTES 24.6 s, NONE 23.2 s (totals 30.8, 13.0, 12.3 min). So the brain was as accurate and about twice as slow.

Graph: diagnoses on brain-graph-full-2026-11-07 (376,111 nodes); every repair on brain-graph-full-2026-11-09 (386,583 node names, 12,351,482 pairs), installed between the sessions; sidecar 244,653 links. The 559 MB unindexed prompts archive was left out of the BRAIN copy for the disk cap.

What it means: MULTI3's 30-to-1 brain win over NOTES was a byte-budget artifact (a flat 120 KB notes file printed whole), not better recall. With notes made greppable, the bank sits at the ceiling for both memory arms and cannot separate them. A test that could would need notes too big or noisy for grep inside the budget, answers that need two notes joined, or questions with no words in common with the note.

Published: private-repo 12_cognitive_architecture/brain_improvement/multi4_codex_pilot01_2026_11_09/ (RESULT.md, grade.json booleans only, summary), commit d286390908. The Claude runtime was not run.

Related: [[multi3_codex_two_session_repair_brain_30_none_0_notes_1_budget_overrun_2026_11_09]], [[multi4_phase_all_runs_three_arms_in_turn_grading_late_harness_frozen_2026_11_09]], [[multi4_codex_client_homes_fill_1gb_folder_cap_run_stopped_moved_aside_2026_11_09]], [[bt4_corrected_grep_false_voids_brainrw_vs_grep_45_24_p0p059_2026_11_09]].

