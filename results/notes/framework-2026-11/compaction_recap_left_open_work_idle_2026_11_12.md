---
name: compaction_recap_left_open_work_idle_2026_11_12
description: "Agent stops after compaction although a timed task and open work remain"
metadata:
  type: feedback
  created: 2026-11-12
  created_at: 2026-11-12T16:21:47+02:00
  status: provisional
  evidence: ""
  lesson: true
---

What happened: On 16 Oct 02:13 the author requested a continuation hook; the linked record identifies one 02:11 recap stop with 3 simulations open. He reported another post-compact stop on 17 Oct 19:36 while asking for 20 hours of work. Do not count loop echoes as separate stalls.

Why it happened: A compaction recap became an end-of-turn response. Context-only hooks could remind the agent but could not themselves force the next turn; the documented fix was Claude-only at that date.

**Why:** A recap can erase the practical obligation to continue a timed task.

**How to apply:** Restore the checkpoint, open task and deadline, then perform the next authorized action; verify the relevant runtime continuation mechanism.

Input lines: 234, 256, 281, 285, 289.

[[w14_prompt_evidence_2026_11_12]] [[after_a_compaction_agents_stopped_on_a_recap_stop_hook_sends_them_back_2026_10_16]]

Drafted by Codex worker W14 of the 12 Nov 04:43 order (H20_1112), screened and filed by an agent. Provisional: the worker read the source, nobody re-measured it.

