---
name: w10_mesh_report_reads_block_writers_2026_11_12
description: "Mesh claims waiting while the desk or workspace report reads the whole messages table"
metadata:
  type: feedback
  created: 2026-11-12
  created_at: 2026-11-12T15:50:52+02:00
  status: provisional
  evidence: ""
  lesson: true
---

What happened: A report read the 416 MB message table in one transaction; waits reached 17 s. A separate desk query loaded message bodies to keep 25 rows; its replacement passed 13/13 checks, while the report replacement passed 9/9 plus 50 existing tests.

Why it happened: The report time predicate had no leading index. The desk OR query could load many bodies despite LIMIT 25. On a rollback-journal database a long reader delays commits; the later source update says 16-17 s waits returned and does not identify their holder.

**Why:** A small result set does not imply a small read or prove which query caused a live lock.

**How to apply:** Inspect EXPLAIN QUERY PLAN, use bounded indexed transactions, compare answers and read bytes on worst-order data, and measure live waits independently.

Input evidence: item 291 (2026-11-12 01:30, [an agent]), item 235 (2026-11-12 01:51, [an agent]), item 196 (2026-11-12 02:05, [an agent]), item 016 (2026-11-12 03:02, [an agent]).

Source memories: [[workspace_report_reads_mesh_messages_newest_first_in_chunks_2026_11_12]] [[desk_agent_mail_query_loaded_every_message_now_index_walks_2026_11_12]]

Drafted by Codex worker W10 of the 12 Nov 04:43 order (H20_1112), screened and filed by an agent. Provisional: the worker read the source, nobody re-measured it.

