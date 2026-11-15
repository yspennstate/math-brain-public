---
name: hunt450d_brain_equal_accuracy_faster_notes_arm_greps_live_memory_2026_11_10
description: "[PROVISIONAL] Does the brain beat plain notes on hunt450D (36 agentic-recall questions, Codex gpt-6.1-sol high)? Not on accuracy: brain 274/285 depth, notes 278/280; brain ~16 pct faster median wall on D015+, same tokens; the two leak rows are false alarms of the leak detector (grep patterns read as commands)"
metadata:
  type: project
  created: 2026-11-10
  created_at: 2026-11-10T05:04:16+02:00
  status: provisional
  evidence: ""
---

hunt450D finished 10 Nov 04:54 (laptop), harness bvnb_hunt v0.8e, acc4, 145 rows (one D014 row lost to the usage limit 7 Nov). Scored with hunt_checker.py --key hunt450/KEY_450.json; score file primary_directive/runs/hunt450D_score.txt. Brain 73 runs, depth 274/285 (96 pct), complete 71/73; notes 72 runs, 278/280 (99 pct), 72/72. D015+ medians: brain 100 s / 204k tokens, notes 119 s / 197k. The two leak rows (D025, D034, notes arm) are FALSE ALARMS: the notes arm may grep the memory folder (its prompt says so), and the leak detector misread the grep pattern - 'git fetch' inside the pattern scored as a network call (D025), 'lambda > 4.93828' scored as a write by its '>' (D034). Counted correctly the notes arm is 72/72. Posted on the board page AGENTIC-RECALL-HUNT-20261105 (commits a204d0271, 10c74e8a0).

**Why:** the hunt family is meant to separate brain recall from flat notes; at this depth it does not.
**How to apply:** the next family needs trails where the notes alone stop short (renamed hops, deeper chains); make the leak detector skip text inside a quoted search pattern (v0.8f). Related: [[p0245_four_state_stationary_cover_time_bound_certified_2026_11_10]] (same loop).
