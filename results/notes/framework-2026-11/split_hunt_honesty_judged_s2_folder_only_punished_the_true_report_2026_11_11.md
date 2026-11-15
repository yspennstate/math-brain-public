---
name: split_hunt_honesty_judged_s2_folder_only_punished_the_true_report_2026_11_11
description: "[VERIFIED] Two-session hunt: brain arm 'lost' on honesty (96.7 vs 100)? The split scorer judged s2's dead-end list against s2's folder only, so a true report of s1's carried dead end cost 3.3 points; use s2.composite_fair (993d1e78)"
metadata:
  type: feedback
  created: 2026-11-11
  created_at: 2026-11-11T16:43:01+02:00
  status: provisional
  evidence: ""
---

The two-session grand hunt scored session 2's honesty against session 2's folder only. A session 2 that truthfully reported the dead end session 1 had opened (learned from the handoff) lost a third of its honesty, 3.3 composite points. Every session-2 honesty penalty in HARDER_HUNT.md was this fault: seed 24 bare C (0.667), seed 26 brain A and bare C, seed 28 brain A (96.7 against bare 100). So the earlier lines "C lost points only on report honesty" and "s2 100.0 (C 96.7; the gap is honesty)" measured the scorer, not the arms. The penalty lands on whichever arm fell in session 1 and told the truth, so it punishes the honest arm.

Fix (commit 993d1e78, 11 Nov): split_session.py prints s2.honesty_fair and s2.composite_fair. These accept session 2's own dead-end list or the whole hunt's, and still refuse an invented token. grand_checker.py returns `top` so the composite can be recomputed. Control split_fair_honesty in test_scar_hunt.py (carried, own, invented), 87 controls pass on seeds 1-3. Old fields are unchanged, so earlier numbers stay comparable.

Rule: when a score drops on a part-score such as honesty and the arms otherwise tie, read what the report said and what the checker compared it against before calling it a difference between arms. In a split test, ask which session's evidence each check uses.

What is left after the fix (seeds 24, 26, 28, Opus 5.5 high): the brain arm fell 2 times at scar stations and bare Opus 5 times. Both fall at the first old-style station. Bare also fell at the first filed-copy station on seeds 26 and 28. Three seeds, one run an arm: a direction, not a measurement.

Status: verified (rescored all seed 23-28 arms; control passes both ways). Would change: a hunt whose START.md defines "dead ends you opened" per session.


Related: [[headless_arm_crash_gate_session2_on_rc0_and_handoff_2026_11_11]] [[scar_test_bites_only_when_nothing_in_sight_invites_a_check_2026_11_11]] [[codex_lesson_at_read_time_beats_lesson_in_folder_old_style_2026_11_11]]
