---
name: stop_checker_rejected_intentional_loop_entries_2026_11_12
description: "hook_liveness Stop order unsafe work_timer not final after wiring loop_keeper or loop_rewake"
metadata:
  type: feedback
  created: 2026-11-12
  created_at: 2026-11-12T15:14:50+02:00
  status: provisional
  evidence: ""
  lesson: true
---

What happened: On 11-12 Nov every wake reported 2 safety failures. One was genuine Codex trust coverage of 44/46 hooks; the other falsely rejected intentional standalone Stop entries. The corrected checker passed 6/6 controls on four runs; the old file passed 0/4 checks moved by the change.

Why it happened: The checker allowed only the older keep-working entries beside the dispatcher. It treated loop_keeper.py and loop_rewake.py as if they could precede the dispatcher's Stop sequence. Settings-level entries run beside it, and an asyncRewake watcher needs that wiring.

**Why:** A stale topology check can turn an intentional installation into a permanent alarm and make real failures harder to notice.

**How to apply:** Preserve the intentional loop entries, update _STANDALONE_STOP_OK alongside any newly authorized standalone entry, and retain a failing control for an unknown entry; do not dismiss the separate 44/46 trust issue.

[[liveness_stop_order_alarm_was_the_loop_keeper_entries_2026_11_12]]

Drafted by Codex worker W05 of the 12 Nov 04:43 order (H20_1112), screened and filed by an agent. Provisional: the worker read the source, nobody re-measured it.

