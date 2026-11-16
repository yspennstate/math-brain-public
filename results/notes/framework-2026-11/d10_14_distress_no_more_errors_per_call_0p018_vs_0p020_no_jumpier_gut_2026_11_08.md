---
name: d10_14_distress_no_more_errors_per_call_0p018_vs_0p020_no_jumpier_gut_2026_11_08
description: "Does distress on the laptop raise the error rate per tool call? No: D10 #14 jumpier reflexes under stress has no premise on the Mac: errors per tool call 0.018 in distress vs 0.020 ok (CIs overlap), fires per call flat; 2 distress episodes"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T03:41:27+04:00
  status: provisional
  evidence: "hook_dispatch.log calls x body_history.tsv tier x outcomes.jsonl, 3-5 Nov; 8 Nov 03:41"
---

1000-ways D10 #14 ("gut-brain coupling") asks that a stressed body lower the reflex firing thresholds, making the brain jumpier, and measures reflex fire rate against tier. Checked by an agent on 8 Nov about 03:41. Not built: the premise fails on the Mac's own data.

Each tool call was tagged with the governor status in force (the last body_history.tsv reading in the 7 min before it), over 3 Nov 19:32 to 5 Nov 06:24:
- ok: 5,329 calls, 105 error signals (0.020 a call, 95% 0.016-0.024), 0.11 reflex fires a call
- warn: 4,034 calls, 63 errors (0.016, 0.012-0.020), 0.11 fires
- distress: 1,747 calls, 32 errors (0.018, 0.013-0.026), 0.09 fires

Under distress, agents make no more mistakes per call, and reflexes fire at the same rate. A lower threshold would add fires where nothing extra goes wrong.

Sources: calls are PreToolUse lines in ~/.claude/compute/hook_dispatch.log, errors are outcomes.jsonl rows with a signal, fires are instinct_fires.tsv. Script: d10_14_errors_by_body_tier.py.

Size of doubt:
- Distress comes from two episodes (see [[d10_1_live_body_reread_already_the_case_status_stale_35pct_at_1h_2026_11_08]]), so the distress row is two stretches of work, not 1,747 independent calls.
- The call log has no session id, so it cannot be split by session class. Headless runners and interactive sessions are mixed.
- outcomes.jsonl counts error signals (non-zero exits, tracebacks), not wrong claims. A stressed agent that errs in what it says would not show here.

How to apply: leave reflex thresholds alone under machine stress. What stress does change is the machine (swap, panics); those are handled by the compute governor and the heavy-lock gate, not the gut. Related: [[scar_load_no_next_hour_error_feedback_rho_0p21_is_activity_d6_63_2026_11_03]] (error load tracks activity, not stress).

