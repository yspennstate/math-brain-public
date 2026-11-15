---
name: mesh_slow_log_names_who_has_the_file_open_2026_11_12
description: "Mesh commits or opens wait 10-20 s and the slow log shows only victims? Since 12 Nov a wait of 5 s (AGENT_MESH_HOLDERS_S) adds a 'holders' line to mesh_slow.log: pid/script/age of every process with the database file open (Windows Restart Manager, no console). The reader is the entry that is not a waiting mesh CLI. First case 01:24 (17 s commit wait) still unnamed; workspace.py report scans all of messages"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T01:42:45+02:00
  status: provisional
  evidence: "agent_run/mesh_lock/test_holders.txt (20 of 20, controls on the old file and with the feature off); ledger row of 12 Nov (h)"
---

The mesh slow log (`~/.agents/coordination/mesh_slow.log`, see [[mesh_importing_callers_patient_s_and_the_slow_transaction_log_2026_11_12]]) showed on its first night what it could not say. At 01:24:05 on 12 Nov a `claim` waited 17.11 s for COMMIT and rolled back, two `release` commands waited 11 and 16 s just to open, and everything cleared at 01:24:12. No writer had long work and no mesh CLI command was slow except the victims. In a rollback journal a commit waits for every reader ([[mesh_lock_convoy_hooks_wait_briefly_and_skip_wal_needs_one_landing_2026_11_11]]), so something read the database for about 24 s, and it was a script that opens the file itself, which the log never sees.

Since 12 Nov `agent_mesh.py` names it. When an open, a BEGIN IMMEDIATE or a COMMIT has waited `AGENT_MESH_HOLDERS_S` seconds (default 5; 0 turns it off) a timer thread asks the Windows Restart Manager which processes have the database file open and appends one line (the shape, with made-up values):

    2026-11-12T01:37:40 pid=9236 tag=cli:claim holders during=commit after=5.0 n=2 24940/some_hook.py/6s,57636/some_service.py/5321s

Each entry is pid/script/age, youngest first. The script is the base name from the process command line (for the mesh CLI also the subcommand, `agent_mesh.py:inbox`); no folder and no argument is written.

How to read it: a holder is any process with the file open, so the other waiting victims are in the list. The reader is the entry that is not a mesh CLI victim with its own `open_wait` or `commit_wait` line at that second. An entry present in every holders line is a long-lived process that keeps a connection open; an entry a few seconds old is a hook or a one-off script.

What it costs: nothing is armed when the call cannot wait as long as the threshold (busy timeout plus `patient_s`), so hooks with 0.3 s waits start no timer. An uncontended write measured 4.50 ms before and 4.81 ms after (median of 300 on a throwaway database).

Tested on throwaway databases with controls (`agent_run/mesh_lock/test_holders.py`, 20 of 20): the old file and the switched-off feature leave no line, a 3 s wait under the default leaves none, an 8 s wait is named at 5 s, and no timer thread survives a refused or failed wait.

Still open: the 01:24 reader itself has not been caught; read the log after the next long wait. One trap found while looking, not shown to be that reader: `global_workspace/workspace.py report` runs `SELECT ... FROM messages WHERE created_at >= ?`, which is a scan of the whole messages table because no index leads with `created_at`.

Two tools worth keeping from this: `EXPLAIN QUERY PLAN` on a read-only connection answers "would this scan the table" without running the query, and Restart Manager (`RmStartSession`, `RmRegisterResources`, `RmGetList` through ctypes) answers "who has this file open" without a console window or a process scan.

