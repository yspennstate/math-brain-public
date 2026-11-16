---
name: multi4_phase_all_runs_three_arms_in_turn_grading_late_harness_frozen_2026_11_09
description: "[VERIFIED] No (MULTI4, 9 Nov): phase all diagnoses BRAIN, NOTES, NONE in turn (183 each, ~3.3 h an arm) then 93 repairs, so grading ~22-23:00 not after the first arm's 15:22 gap; the harness is hash-frozen per step, so no mid-run patch"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T14:26:27+04:00
  status: verified
  evidence: "tools/launch_scored.py:6,18; harness/run_step.py:108-118; FREEZE.json lists run_step.py, brain_env.py; BRAIN batch step1 181/183 at 14:21"
---

When does a MULTI4-style scored run (launch_scored.py --phase all --wait-gap) finish, and can its harness be patched mid-run? It finishes long after the first arm's cold gap, and no, it cannot be patched (checked 9 Nov 2026, an agent).

Timing: phase all runs every diagnosis first, arm by arm (ARMS = BRAIN, NOTES, NONE, tools/launch_scored.py:6 and :18), and only then the repairs. multi4_pilot01 began at 11:07. BRAIN's 183 diagnoses took about 3 h 18 min, to ~14:25. NOTES and NONE each take about as long, and then come 93 repairs, so grading lands around 22:00-23:00. For three hours I told the author "grading after ~15:30". That came from reading BRAIN's 7,200 s cold-gap window (13:11-15:22) as the end of the run. Read the arm loop and count arms × tasks before giving a finish time.

Patching: every model step verifies the freeze (harness/run_step.py:108-118), and FREEZE.json hashes run_step.py and brain_env.py among 20 harness files. Editing any of them mid-run, even for a security fix such as the clean_env token scrub ([[codex_child_inherits_claude_session_env_token_leak_2026_11_09]]), voids every later attempt. Apply the fix after the run, refreeze, then launch.

How to apply: before quoting when a frozen test ends, or before changing its code, read its launcher's loop and its FREEZE list.


Related: [[multi3_codex_two_session_repair_brain_30_none_0_notes_1_budget_overrun_2026_11_09]] - the predecessor run with the same two-session design.
