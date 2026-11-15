---
name: mesh_messages_full_scan_read_lock_2026_11_12
description: "workspace.py report scans mesh messages by created_at and blocks shared SQLite commits"
metadata:
  type: feedback
  created: 2026-11-12
  created_at: 2026-11-12T15:17:49+02:00
  status: provisional
  evidence: ""
  lesson: true
---

What happened: The old report queried messages WHERE created_at >= ? without an index leading with created_at, producing SCAN messages over a 416 MB table. It could hold a rollback-journal reader open across the scan. On an 83 MB throwaway table, the replacement changed 40000 rows in one statement at 84 ms to 6000 rows in three statements at 26 ms.

Why it happened: A time-window predicate looked selective but the available indexes could not use its leading column. One long read transaction delayed writers.

**Why:** Returning few recent rows does not imply that SQLite reads few rows or releases the read lock quickly.
**How to apply:** Inspect EXPLAIN QUERY PLAN first and preserve short newest-first rowid reads; test out-of-order timestamps and disclose that more than an hour of disorder or 1000 old-stamped rows can undercount.

The source reports 9 of 9 scratch controls, not live timing. This report was not proved to cause the separate 17-second live stall.

[[workspace_report_reads_mesh_messages_newest_first_in_chunks_2026_11_12]]
[[mesh_slow_log_names_who_has_the_file_open_2026_11_12]]

Drafted by Codex worker W06 of the 12 Nov 04:43 order (H20_1112), screened and filed by an agent. Provisional: the worker read the source, nobody re-measured it.

