---
name: desk_unindexed_filter_keeps_scan_2026_11_12
description: "Slow Agent desk mesh read last_seen WHERE filter still scans agents"
metadata:
  type: feedback
  created: 2026-11-12
  created_at: 2026-11-12T14:44:32+02:00
  status: provisional
  evidence: ""
  lesson: true
---

What happened: On 2026-11-12 the desk read 11,366 agent rows every 3 seconds with a viewer or 30 seconds without one. Three slow reads took 4.5, 5.4 and 3.1 seconds in 29.5 minutes. The replacement passed 13/13 cases and used 30 SQLite steps versus 1,954.

Why it happened: link_mesh discarded old rows in Python after reading them. EXPLAIN showed SCAN agents even with last_seen filtering; the usable partial index was on lease_until. The new path uses that index, catches departed agents by primary key and refreshes all rows every 300 seconds; done/offline edits can lag five minutes. The overall reduction in live lock waits remains unmeasured.

**Why:** Filtering an unindexed column can reduce returned rows while reading the same pages.

**How to apply:** Run EXPLAIN QUERY PLAN, reuse idx_agents_live, preserve departure and fallback behavior, then measure live read and commit waits.

[[desk_read_all_mesh_agents_every_tick_now_whole_once_in_five_minutes_2026_11_12]]

Drafted by Codex worker W02 of the 12 Nov 04:43 order (H20_1112), screened and filed by an agent. Provisional: the worker read the source, nobody re-measured it.

