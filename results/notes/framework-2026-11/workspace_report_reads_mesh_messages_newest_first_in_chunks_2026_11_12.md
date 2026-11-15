---
name: workspace_report_reads_mesh_messages_newest_first_in_chunks_2026_11_12
description: "A reader of the mesh messages table by time (workspace.py report: WHERE created_at >= ?) scans the whole table, no index leads with created_at, and every mesh commit waits behind it. Fixed 12 Nov: read newest first by rowid, 2,000 rows a query, stop after 1,000 rows older than the window. Check any such reader with EXPLAIN QUERY PLAN first; same answers old against new"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T01:51:17+02:00
  status: verified
  evidence: "agent_run/mesh_lock/test_ws.txt (9 of 9, old file against new); ledger row of 12 Nov (i)"
---

`global_workspace/workspace.py report` counted mesh traffic with `SELECT sender_agent, recipient, kind FROM messages WHERE created_at >= ?`. No index on the mesh's messages table leads with `created_at`, so the plan is `SCAN messages`: the whole table (416 MB on 12 Nov 2026) in one read transaction. The mesh runs a rollback journal, where every commit waits for every reader ([[mesh_lock_convoy_hooks_wait_briefly_and_skip_wal_needs_one_landing_2026_11_11]]), so one report could hold up every agent's claim and release for as long as the scan ran. Nothing scheduled runs the report; it was found while looking for the reader behind a 17 s commit wait ([[mesh_slow_log_names_who_has_the_file_open_2026_11_12]]) and is not shown to be that reader.

Since 12 Nov `_recent_messages` reads the window newest first: 2,000 rows a query by rowid (`ORDER BY rowid DESC LIMIT ?`, then `WHERE rowid < ?`), each chunk its own short read so commits get in between, and it stops after 1,000 rows older than the window minus an hour of slack. Messages are appended, so the newest sit at the highest rowids; the slack is there because a message's stamp is taken before it is written and a sender can wait.

Measured old against new on throwaway databases (`agent_run/mesh_lock/test_ws.py`, 9 of 9): the same answer at seven window positions with stamps up to 30 s out of table order and again with 30 minutes; a table without a rowid falls back to the old query; on an 83 MB table with the window on the newest 2 per cent, one statement over 40,000 rows became three over 6,000 (84 ms against 26 ms, file in the cache). Not measured on the live mesh file.

The pattern for any reader of an append-only table on a shared SQLite file: ask `EXPLAIN QUERY PLAN` first (it does not run the query); if it says SCAN, read backwards by rowid in chunks and stop on age, instead of adding an index to someone else's table. What it gives up: stamps more than an hour out of table order, or a block of 1,000 old-stamped rows above newer ones, are undercounted.

