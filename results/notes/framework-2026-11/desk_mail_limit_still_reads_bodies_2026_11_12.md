---
name: desk_mail_limit_still_reads_bodies_2026_11_12
description: "Agent desk SQLite OR ORDER BY LIMIT 25 reads every message body"
metadata:
  type: feedback
  created: 2026-11-12
  created_at: 2026-11-12T15:06:45+02:00
  status: provisional
  evidence: ""
  lesson: true
---

What happened: The old desk query read 6.5 MB for a busy agent and 37.1 MB for a receive-only agent; the replacement read 1.2 MB and 0.15 MB respectively and preserved all 25 rows in 13/13 checks.

Why it happened: The sender index lacked created_at; OR index order defeated the newest-25 cutoff and caused body reads. The desk appearing in holders lines does not prove it held a lock: 16-17 s waits returned after the fix.

**Why:** A result-row limit does not bound disk bytes touched or establish lock ownership.

**How to apply:** Select newest ids with covering indexes, compare exact row order and fresh-connection read_bytes on worst-order fixtures, and measure lock attribution separately.

[[desk_agent_mail_query_loaded_every_message_now_index_walks_2026_11_12]]

Drafted by Codex worker W04 of the 12 Nov 04:43 order (H20_1112), screened and filed by an agent. Provisional: the worker read the source, nobody re-measured it.

