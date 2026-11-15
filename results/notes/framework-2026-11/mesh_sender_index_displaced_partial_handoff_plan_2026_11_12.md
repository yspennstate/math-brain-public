---
name: mesh_sender_index_displaced_partial_handoff_plan_2026_11_12
description: "agent_mesh pending handoffs release bye slow after adding sender_agent index; EXPLAIN partial-index plan"
metadata:
  type: feedback
  created: 2026-11-12
  created_at: 2026-11-12T14:52:19+02:00
  status: provisional
  evidence: ""
  lesson: true
---

What happened: The 11 Nov sender_agent index displaced the 8 Oct partial handoff index for about one day. On 12 Nov, the check could read 34,202 sent rows and 5,793 unacked inbox rows although only 10 handoffs were open, while holding BEGIN IMMEDIATE. The throwaway comparison measured 46.9 versus 0.17 MB for a broadcaster and 31.5 versus 0.13 MB for a busy inbox. Thirteen of thirteen controls passed after naming the narrow index.

Why it happened: An additional broad index changed SQLite's plan on a database with no planner statistics. The original change checked its intended queries without checking the older queries sharing sender_agent. The observed 26.12-second bye is not entirely explained: about 150 claim releases and disk contention remain, and batching about 300 transactions was a lead only.

**Why:** Adding an index can silently undo an earlier query fix.

**How to apply:** EXPLAIN every query sharing the new index's leading column on a copy with live-equivalent statistics, preserve the intended partial-index plan and fallback, and propagate unrelated database errors.

[[handoff_check_lost_its_partial_index_to_the_sender_index_named_now_2026_11_12]]

Drafted by Codex worker W03 of the 12 Nov 04:43 order (H20_1112), screened and filed by an agent. Provisional: the worker read the source, nobody re-measured it.

