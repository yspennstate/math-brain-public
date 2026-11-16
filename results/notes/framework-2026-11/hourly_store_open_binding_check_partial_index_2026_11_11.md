---
name: hourly_store_open_binding_check_partial_index_2026_11_11
description: "[VERIFIED] Hourly project-memory pass sat 13 min at store open (_install_schema integrity COUNT over 365k prompt_events, I/O priority 1)? Since 11 Nov 03:19 a partial index idx_prompt_binding_broken holds only broken-binding rows (none), so the check is exact and instant (0.005 s open)"
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T03:21:38+02:00
  status: provisional
  evidence: ""
---

The hourly project-memory pass (pid 41312, started 03:05:10 on 11 Nov) spent 03:05 to about 03:18 in ProjectMemoryStore._install_schema at store.py:221: the source-binding integrity check, SELECT COUNT(*) FROM prompt_events WHERE <binding broken>, a full scan of 365,691 rows. The prompt hook skips it since 00:42 (verify_bindings=False, memory project_memory_hook_open_scan_and_two_copies_2026_11_11), but the hourly pass keeps it, and its children run at I/O priority 1 behind the renders. The same scan from a Normal shell, read-only: 21.8 s cold, 6.4 s warm, 0.6 s hot. So about 13 of the pass's 45-minute cap went to one COUNT that has returned 0 every time.

Fix (11 Nov 03:19, an agent-loop): a partial index that holds only the broken rows, CREATE INDEX idx_prompt_binding_broken ON prompt_events(ingest_seq) WHERE <the same expression as the COUNT>. SQLite's planner answers the COUNT from the index (EXPLAIN QUERY PLAN: SCAN prompt_events USING INDEX idx_prompt_binding_broken), and the check stays exact: in a 200k-row test a bad UPDATE and a bad INSERT were both counted (2) in 0.0000 s. Built on the live 47 GB store after a hot read: the write lock was held 0.5 s, and contract-failures.jsonl has no row after 02:19. A store open with the full check now takes 0.005 s (0.004 without). Added to runtime/project_memory/schema.sql (backup schema.sql.bak_20261111_0320 in the agent scratch area). The nested stale copy runtime/project_memory/project_memory/ was not touched.

Rule: the index's WHERE must stay the same expression as the COUNT in store._install_schema. Change one and you must change the other, or the planner silently goes back to the full scan. How to check: EXPLAIN QUERY PLAN must name the index.

What would change this: a pass whose store open is still slow. The 04:0x pass's first progress line should come within seconds of its start. Related: [[hourly_hydrate_replay_walk_cached_by_git_tree_2026_11_11]], [[the_hourly_ingest_was_cpu_starved_lock_holder_now_raised_2026_11_10]].
