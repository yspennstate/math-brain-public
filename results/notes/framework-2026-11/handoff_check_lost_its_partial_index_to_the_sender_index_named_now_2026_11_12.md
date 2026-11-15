---
name: handoff_check_lost_its_partial_index_to_the_sender_index_named_now_2026_11_12
description: "Mesh release or bye slow while holding the write lock? The pending-handoff check read every row the agent ever sent (34,202 for one broadcaster): a plain index on sender_agent added 11 Nov took the plan from the partial index built for the check on 8 Oct. The statement names it now (INDEXED BY). Before adding an index, EXPLAIN every statement that starts with the same column"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T03:19:45+02:00
  status: verified
  evidence: "agent_run/mesh_lock/test_handoff.txt (13 of 13, the old file against itself fails the bytes line), suites_handoff.txt, live_handoff.txt; ledger row of 12 Nov (o)"
---

`release()` and `bye()` in `agent_mesh.py` check for pending handoffs inside their `BEGIN IMMEDIATE` (`Mesh._pending_handoffs`). On 8 Oct that check was given a partial index, `idx_messages_open_handoffs ON messages(sender_agent, recipient) WHERE kind='handoff' AND acked_at IS NULL`, after a full scan of messages had held the fleet's write lock for half an hour. On 11 Nov I added a plain `idx_messages_sender ON messages(sender_agent)` for other statements ([[desk_agent_mail_query_loaded_every_message_now_index_walks_2026_11_12]], `receipts()`). The mesh file has no planner statistics, and from then on the planner answered the outgoing side from the plain index and the incoming side from `idx_messages_recipient`: every row the agent ever sent and every unacked row it ever received, loaded to look at `kind`, with the write lock held. On the live file that is 34,202 rows for `brain-high`, 464 for a busy session, 5,793 unacked for the desk's inbox; there were 10 open handoffs in all.

Since 12 Nov the statement names the index (`INDEXED BY idx_messages_open_handoffs`, both sides; the incoming side walks the whole partial index, which holds open handoffs only). A file without the index gets the unhinted statement as before; any other error, a locked database included, is raised as before and nothing is sent twice. `agent_run/mesh_lock/test_handoff.py`: 13 of 13 on a throwaway database with the live table and its six indexes (40,000 messages, 60 open handoffs): the same rows in the same order for six agents and four direction pairs; a broadcaster's check reads 0.17 MB of the file against 46.9, an agent with a pile of unacked mail 0.13 against 31.5; the old file against itself fails that line. The folder's five suites give the same result on the old and the new file. Backup `agent_mesh.py.bak_handoffidx_20261112`.

What to carry: a new index can take a plan away from an older, narrower one. Before adding an index, run `EXPLAIN QUERY PLAN` on every statement whose WHERE starts with the same column, on a file with the same statistics as the live one (here: none), and pin the narrow index by name where the statement was built for it. I did not do that on 11 Nov, and the 8 Oct fix was silently undone for a day.

How it was found: the slow log ([[mesh_slow_log_names_who_has_the_file_open_2026_11_12]]) showed a `bye` of the memory mirror with `work=26.12` at 03:07 on 12 Nov, a writer holding the lock while it read. For that agent the handoff check is the small part (it sends nothing and held 52 unacked rows); most of its 26 s is the release of about 150 claims in one transaction with the disk contended, which this change does not touch. So the 03:01-03:08 burst is only partly explained: the commit waits in it are behind readers that the log does not name. The mirror takes its claims one file at a time, about 300 write transactions a run; batching them is a lead, not done.

