---
name: hourly_session_map_query_driven_from_pairs_2026_11_11
description: "Hourly project-memory pass session-to-project map slow (60-200 s)? Since 11 Nov 04:07 PAIRED_SESSION_SQL starts from the 57k paired events, not all 366k: same 6,508 rows, 30.7 s vs 60.5 s; 04:04 pass whole in 705 s"
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T04:21:59+02:00
  status: verified
  evidence: "session_alt.py equality check + 04:04 pass log"
---

The hourly project-memory pass builds a session-to-project map in contract_cache (PAIRED_SESSION_SQL in `~/.brain-framework/runtime/project_memory/hot_cache.py`). The query started from prompt_events (366k rows) through idx_prompt_session and joined the pairs table onto every authoritative event. Only about 57k events carry a project pair (99,345 pairs in event_project_cache.sqlite3), so most of the scan was wasted. On 11 Nov 03:05 it was still running after 200 s when the pass hit its 2700 s cap.

Fix (11 Nov 04:07, an agent): the query now starts from temp.event_project_pairs and joins prompt_events by its unique event_id index (`FROM temp.event_project_pairs ep CROSS JOIN prompt_events p ON p.event_id=ep.event_id`), with the same WHERE clause (AUTHORITATIVE_EVENT_SQL), GROUP BY, ORDER BY and LIMIT 20000.

Checks, read-only on the live store (scratch session_alt.py): 6,508 rows each way, the same multiset, the same newest-first order, and the same session-to-project sets. Timing: 30.7 s against 60.5 s warm, and the old plan took 95.3 s on its first run. The consumers (hot_cache.py:389, project_memory_hot_hook.py:333) use the result as a set of projects per session. runtime/test_project_memory_hot_hook.py passes 24 of 24. Backup: scratch area hot_cache.py.bak_20261111_0410 (session agent).

In production: the 04:04 pass on 11 Nov (owner away, Normal priority) ran contract_cache to "sections done" at +44 s, with the session map included. Contract rows took 2 s for live-brain and 6 s for shared-brain, against 239 s and 341 s at 03:05. The scan took 32 s, against 1616 s. The whole pass finished in 705 s and exited 3, which means "backfill pending": the 600 MB read budget left 46 files for a later pass, as designed.

Caveat: the cache was warm from my test queries. The contract-row speedup belongs to Normal I/O priority and that warm cache, not to this change. The slow phase is now ingest: 2,504 new rows in 480 s (0.19 s each, one IMMEDIATE transaction per row, WAL with synchronous=FULL). That is the next lead.

Related: [[hourly_store_open_binding_check_partial_index_2026_11_11]], [[run_bounded_restores_io_priority_for_owner_present_scheduled_jobs_2026_11_11]], [[hourly_hydrate_replay_walk_cached_by_git_tree_2026_11_11]].

