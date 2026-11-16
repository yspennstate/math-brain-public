---
name: desk_agent_mail_query_loaded_every_message_now_index_walks_2026_11_12
description: "Who held the mesh database during the 16 s commit waits? The slow log's holders lines named the Agent desk (agent_desk_service.py): its mail query for the selected agent loaded every message that agent sent or received, with bodies, to keep 25. Fixed 12 Nov with covering-index walks, same 25 rows; measure such a query by the process read-byte counter and test the worst index order"
metadata:
  node_type: memory
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T02:05:01+02:00
  status: provisional
  evidence: "agent_run/mesh_lock/test_desk.txt (13 of 13, control old against old fails), holders_first_live_20261112.txt; ledger row of 12 Nov (j)"
  modified: 2026-11-12T01:04:51.006Z
---

The first live "holders" lines of the mesh slow log ([[mesh_slow_log_names_who_has_the_file_open_2026_11_12]]) came at 01:54:03-01:54:10 on 12 Nov 2026, during a 16.2 s commit wait: the only process with the mesh database open that was not itself a waiting mesh command was `agent_desk_service.py` (the Agent desk, `~/agent-desk`, [[agent_desk_live_interactive_view_of_every_agent_2026_09_09]]).

Its `mesh_snapshot(detail_agent=...)` ran, for the agent selected in the desk, `... from messages where sender_agent=? or recipient=? or recipient='all' order by created_at desc limit 25`. The plan is MULTI-INDEX OR with a temp b-tree. What that costs is not obvious from the plan: SQLite reads the sort key first and loads the rest of a row only if the key can still make the newest 25. The sender index carries no `created_at`, so every row the agent sent is loaded with its body; received rows are loaded only when newer than the 25th newest seen so far. An agent that sends a lot pays for its sent rows; an agent that never sends gets no cut-off and all of its mail is loaded, oldest first. The live table holds no `recipient='all'` rows (a broadcast is one row per recipient), so that branch found nothing.

Since 12 Nov the newest 25 row ids of each kind (sent by rowid; received unacked and received acked by `created_at`) come from covering indexes without touching a body, and only those rows (at most 125) are read and sorted. Measured old file against new on throwaway databases with the mesh's own table and indexes (`agent_run/mesh_lock/test_desk.py`, 13 of 13, the control old against old fails): the same 25 messages in the same order; file bytes read 6.5 MB against 1.2 for a busy agent, 37.1 against 0.15 for an agent that only receives.

Two things to carry. A read counter (`psutil.Process().io_counters().read_bytes` around a query on a fresh connection) measures how much of a SQLite file a query touches, which step counts and warm timings hide; it showed the same query reading 7 MB on one test database and 40 MB on another, and that difference is what explained the mechanism. And `ORDER BY ... LIMIT` over an OR of indexes is cheap or ruinous depending on the order the index hands rows over, so test it with the worst order, not a random one. Not timed on the live file: the 16 s is tied to the desk process by the holders lines, not to this query by a measurement ([[workspace_report_reads_mesh_messages_newest_first_in_chunks_2026_11_12]] is the sibling fix).

Watched after the fix (12 Nov): from the desk's restart at 02:04:34 to 03:01 the mesh slow log holds one line, a release that took 2.0 s at 02:09:57, and no holders line. Then from 03:01:26 to at least 03:03:43 the waits came back: commits waiting 16 to 17 s and rolled back (a send at 03:02:09, an ack at 03:03:17, a claim at 03:03:36), opens waiting 9 to 14 s, one begin refused after 25 s. The desk is on every holders line of that burst, but it keeps the file open all the time (its age on the line is the time since its restart), so being named there does not show it held the lock; at 03:01:59 it was the only live process named beside the waiting send. `memory_mirror.py` (one process issuing hello, claim and assert) and about ten CLI calls at once were in the same two minutes, and the slow-sense probe had reported disk contention at 02:56. So the query fix stands on its own test (same 25 rows, far fewer bytes read), and whether it removed the 16 s waits is NOT shown: status stays provisional until the burst's holder is found.
