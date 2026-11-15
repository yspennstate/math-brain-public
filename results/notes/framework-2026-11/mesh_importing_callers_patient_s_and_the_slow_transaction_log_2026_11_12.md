---
name: mesh_importing_callers_patient_s_and_the_slow_transaction_log_2026_11_12
description: "Script that imports agent_mesh.py dies with 'database is locked' (board ingester, 25 cycles 5-11 Nov)? Only the CLI retried. Mesh(db, patient_s=N) now tries the open, BEGIN IMMEDIATE and COMMIT again for N s (default 0); the ingester asks 30. mesh_slow.log beside the database names waits and slow writers: begin_wait = behind a writer, commit_wait = behind a reader, work = the slow writer"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T00:56:05+02:00
  status: verified
  evidence: "agent_run/mesh_lock/test_patient.txt (23 of 23, controls on the old file); ledger row of 12 Nov (d)"
---

A script that imports `agent_mesh.py` and builds `Mesh()` itself gets none of the command line's retry. `main()` re-runs a refused command up to four times; an importing caller got one try per statement at its busy timeout and then `sqlite3.OperationalError: database is locked`. The board's report ingester (`scheduled_tasks/ingest_repository_reports.py`, run by `publish_board.py` every 15 minutes) lost 25 cycles that way between 5 and 11 Nov: 19 at `BEGIN IMMEDIATE`, 3 at `COMMIT`, 2 at the open's `PRAGMA journal_mode=DELETE`, 1 in the schema repair. Each cost the board mirror 15 minutes. The lock spans behind them are the rollback-journal convoy: [[mesh_lock_convoy_hooks_wait_briefly_and_skip_wal_needs_one_landing_2026_11_11]].

Since 12 Nov 2026 `Mesh(db, busy_timeout_ms=..., patient_s=N)` tries a locked database again every quarter second until N seconds have passed, at three places that are safe to repeat: the open (connect, PRAGMAs, schema check), `BEGIN IMMEDIATE` (nothing of the transaction exists yet) and `COMMIT` (SQLite keeps the transaction open when COMMIT is refused as busy, so the same transaction commits once the reader leaves). Default 0: hooks keep their short waits and skip. The ingester asks for 30 s, with a `TypeError` fallback to plain `Mesh(db)` so a rollback of the mesh file does not break it. Other importing callers that have no retry: `team_comm.py` (busy 3 s) and `bridge/mesh_bridge.py` (15 s); not changed, not measured.

The same landing added `mesh_slow.log` next to the database (`~/.agents/coordination/`). One line when a write transaction's parts add up to 2 s or more (`AGENT_MESH_SLOW_S`), one for a slow open, one for a slow CLI command:

    2026-11-12T00:49:22 pid=34112 tag=cli:claim write_tx begin_wait=0.00 work=0.02 commit_wait=4.99 outcome=committed

The stamp is the end of the span. How to read it: a long `begin_wait` waited on another writer; a long `commit_wait` waited on a reader; a long `work` is the writer the others waited on; a slow `command` line with no `write_tx` line from the same pid is a slow reader. `outcome=begin_refused` is a caller that gave up. The tag is `cli:<command>` or the importing script's file name. No statement text, no agent names. The file rotates to `.1` at 2 MB. Callers that open the database with their own `sqlite3.connect` write nothing, and a long-lived process keeps the old code until it restarts.

Tested on throwaway databases with a second process holding the lock (`agent_run/mesh_lock/test_patient.py`, 23 of 23): each of the three places is refused on the old file and on the new file without patience, and succeeds about 5 s later with `patient_s=20`, the row written exactly once. `patient_s=3` behind a 12 s writer is refused after 3.3 s with nothing written. A non-lock error and the caller's own exception are raised at once. The mesh folder's suites give the same result on both files. Not proven: a live board cycle that met a lock and got through; read PUBLISH.log and the slow log for that.

Method worth keeping: to test lock handling, hold the lock from a second process in the exact state that matters (`BEGIN EXCLUSIVE` blocks the open, `BEGIN IMMEDIATE` blocks another writer's BEGIN, an open read blocks only the COMMIT), and write a ready file so the test does not race the holder.

