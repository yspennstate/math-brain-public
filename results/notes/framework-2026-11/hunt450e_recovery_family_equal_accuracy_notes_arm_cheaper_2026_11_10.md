---
name: hunt450e_recovery_family_equal_accuracy_notes_arm_cheaper_2026_11_10
description: "[PROVISIONAL] hunt450E recovery family (10 Nov): brain and notes both 72/72; notes 75 s / 140k tokens vs brain 86 s / 207k; 2 notes runs BRUTE; families still too easy to separate"
metadata:
  type: project
  created: 2026-11-10
  created_at: 2026-11-10T07:11:30+02:00
  status: provisional
  evidence: ""
---

hunt450E (recovery family: damaged, moved or stale files, plus one note found from a sorted bag of its description words, plus one computation), 36 hunts, two Codex gpt-6.1-sol high runs per arm, harness v0.8f, 144 rows scored by hunt_checker.py against KEY_450 on 10 Nov 2026 07:10.
- brain arm: 72/72 complete, depth 216/216, median 86 s, median 207k tokens (mean 217k).
- notes arm: 72/72 complete, depth 216/216, median 75 s, median 140k tokens (mean 157k). Two runs (E023, E025) are flagged BRUTE, meaning they enumerated instead of recovering.

**Why:** accuracy is equal again, as on hunt450D ([[hunt450d_brain_equal_accuracy_faster_notes_arm_greps_live_memory_2026_11_10]]). The brain arm pays about 50 pct more tokens, mostly for its one long recall output. A sorted word bag still gives the notes arm literal words to grep for.

**How to apply:** do not quote E as a brain win. To separate the arms, the next family must take away the grep: answers reached only through links between notes, or a note renamed since the clue was written. Count BRUTE flags as a separate failure line. Board page: brain-tasks-board coordination/tasks/AGENTIC-RECALL-HUNT-20261105.md (commit cf873a32).

