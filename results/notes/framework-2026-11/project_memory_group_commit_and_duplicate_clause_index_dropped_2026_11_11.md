---
name: project_memory_group_commit_and_duplicate_clause_index_dropped_2026_11_11
description: "[VERIFIED] Project-memory hourly ingest slow per row? Group commit tried 11 Nov and ROLLED BACK (no gain: under WAL synchronous=NORMAL a commit costs page writes, not fsync); the duplicate idx_clause_event drop stays (268 s lock; drop schema line first)"
metadata:
  node_type: memory
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T10:26:57+02:00
  updated_at: 2026-11-11T16:20:00+02:00
  status: verified
  evidence: py-spy of the 09:00 (per-row) and 11:00 (grouped) hourly passes; hourly_bounded.log.child timing lines
  modified: 2026-11-11T14:15:48.608Z
---

Hourly project-memory pass, ingest of new prompts (0.13-0.31 s a row on the 47 GB store). Two changes tried 11 Nov 2026; one stays.

1. Group commit: ROLLED BACK 16:1x. store.group_commit(0.25) wrapped the hourly ingest loop from 09:15 (one transaction per ~0.25 s of rows, a savepoint per row; identical output proven on 25 tables). On a fresh test store it cut 0.34-0.44 s to 0.12-0.14 s a row. Live it bought nothing:
   - per new row 0.175 s at 09:00 (per-row commits) against 0.233 s at 10:00 and 0.240 s at 11:00 (grouped);
   - py-spy: commit time per row about 0.072 s ungrouped, about 0.069 s grouped (41 pct of ingest_prompt became 29 pct, but the inserts grew);
   - the hook gauge said the box was no busier at 11:00 (median 0.052 against 0.056).
   Why: the hourly pass runs synchronous=NORMAL under WAL (hourly_runner.py, since 14 Oct), so a commit does not fsync; its cost is writing the dirty pages, and the store's random HMAC keys put each row's inserts on different pages, so batching rows shares almost no pages. The test store won because it was small and its default sync did fsync. Grouping also holds the write lock longer while the prompt hook waits. Restored from the scratch area backups .bak_20261111_0920 (copy, compile, os.replace), files verified unchanged since the patch first.

2. Duplicate index dropped (10:22-10:26), STAYS: idx_clause_event(event_id, ordinal) duplicated UNIQUE(event_id, ordinal) on clauses (19.3M rows); a sweep of every index in the store found no other duplicate. The CREATE line left schema.sql FIRST (schema.sql runs on every store open, so an open between the drop and the edit would rebuild a 19M-row index inside the prompt hook). The drop held the write lock 268 s, so hook saves skipped for those 4.5 min; the hourly pass reingests them. Other machines keep the old index harmlessly; schema.sql carries no DROP on purpose.

Hint for the next speed attempt here: batching commits is a dead lead on this store. What the 11:00 profile left: inserts into coverage_spans, clauses, obligation_progress and coverage_dispositions (the bulk of ingest), then publish 30 pct and contract_cache 23 pct of the pass (_contract_rows, hot_cache.py:140).
What would change this: the pass moving to synchronous=FULL, or a key scheme that clusters a row's inserts on shared pages.

Related: [[merged_line_reads_of_a_sparse_prompt_window_read_15x_the_bytes_2026_11_11]] (the other speedup that lost, same pass), [[runtime_module_imported_by_the_prompt_hook_edit_a_copy_then_replace_2026_11_11]] (how store.py was replaced), [[checklist_task_20261110_092]].

1. Group commit (09:15): store.group_commit(0.25) around the hourly ingest loop. Rows written through immediate() share one transaction, a SAVEPOINT each, committed every ~0.25 s and at the end; a row that raises rolls back only itself. Only the hourly loop opens a group; the prompt hook is unchanged. The timing line now prints "group commit R row writes in C commits". Proven identical output first (25 tables, three hold modes, the error path). 10:00 pass: 3451 row writes in 604 commits, no error. Test store, same 92 rows: 0.34-0.44 s committing per row, 0.12-0.14 s grouped. Live per-row time went 0.175 -> 0.233 s while the hook's own one-row save doubled (0.056 -> 0.113 s median), so the live gain is NOT shown yet; read the 11:00+ passes, or py-spy the ingest and compare the commit share with 41 pct at 09:00.
Backups: scratch area store.py/hourly_runner.py .bak_20261111_0920, schema.sql.bak_20261111_1021. Rollback of 1 = os.replace the backups; rollback of 2 = restore the line (the next open rebuilds the index, minutes under lock, so outside a pass).
What would change this: a pass where grouped ingest is slower per row than the same-hour hook gauge predicts.
