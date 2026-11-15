---
name: mirror_waited_on_offline_editor_2026_11_12
description: "Waiting for memory mirror peer reply from offline session agent status last_seen"
metadata:
  type: feedback
  created: 2026-11-12
  created_at: 2026-11-12T14:45:14+02:00
  status: provisional
  evidence: ""
  lesson: true
---

What happened: A 2026-11-12 03:23 request to an agent was never delivered: the session had been offline since 10 Nov. The source records the batch fix landing at 04:19, but does not measure how much of that interval was waiting.

Why it happened: The request named the old editor without checking whether the agents-table row still described a live session.

**Why:** A message to an offline session cannot produce the peer response the plan depends on.

**How to apply:** Check peer status and last_seen before waiting, choose a live handoff, and still honor claims and write authority.

[[memory_mirror_claims_in_batches_six_mesh_calls_for_sixty_files_2026_11_12]]

Drafted by Codex worker W02 of the 12 Nov 04:43 order (H20_1112), screened and filed by an agent. Provisional: the worker read the source, nobody re-measured it.

