---
name: w09_mesh_fix_claim_preceded_live_evidence_2026_11_12
description: "Agent desk mesh waits returned after fix query scans and wall clock stalls"
metadata:
  type: feedback
  created: 2026-11-12
  created_at: 2026-11-12T15:42:22+02:00
  status: provisional
  evidence: ""
  lesson: true
---

The claim that a desk fix ended 16-second mesh waits was withdrawn at 03:20 after waits returned at 03:01-03:08. A displaced index made a release check read 34,202 messages to keep 10. Later desk work fell from 0.6 to 0.006 seconds per tick, but a 0.003-second task query still stalled; six later stalls used only 0.0-0.3 CPU seconds, with a longest wall time of 48.6 seconds and peer commit waits of 19.7 and 12.0 seconds.

An improved query and a quiet observation window were treated as proof of a system-wide fix; live lock holding, query plans and scheduler stalls were different mechanisms.

**Why:** An improved query and a quiet observation window were treated as proof of a system-wide fix; live lock holding, query plans and scheduler stalls were different mechanisms.

**How to apply:** Inspect EXPLAIN after index edits, use CPU plus wall time and real holder evidence, and retain provisional status until the symptom is measured under comparable load.

Sources: [[desk_agent_mail_query_loaded_every_message_now_index_walks_2026_11_12]], [[desk_read_all_mesh_agents_every_tick_now_whole_once_in_five_minutes_2026_11_12]].
Input notes: N010, N124, N131, N134, N257 in input/agent_notes.txt.

Drafted by Codex worker W09 of the 12 Nov 04:43 order (H20_1112), screened and filed by an agent. Provisional: the worker read the source, nobody re-measured it.

