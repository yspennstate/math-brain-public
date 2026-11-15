---
name: mesh_command_retries_a_locked_database_when_nothing_was_written_2026_11_11
description: "agent_mesh.py exit 2 'database is locked'? Since 11 Nov 06:27 the command retries by itself (4 attempts inside 27 s) when nothing it wrote stayed; exit 2 now means the lock outlasted that; AGENT_MESH_BUSY_BUDGET_S=60 waits longer. 17 controls pass. Stalls not fixed: 95 in 72 h on the 597 MB DELETE-mode store"
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T06:42:36+02:00
  status: verified
  evidence: "brain_improvement/agent_run/mesh_busy_retry/patch_mesh_busy_retry.py, test_mesh_busy_retry.py; ledger_rows_20261111_l.jsonl"
---

**Symptom.** A mesh command (`claim`, `release`, `send`, `pulse`, `hello`) prints `agent mesh database error: database is
locked` and exits 2, usually after about 15 s. Nothing was refused; the tool failed.

**What changed (landed 11 Nov 06:27).** `agent_mesh.py` now retries by itself. `main()` runs the command up to four times
inside 27 s of wall clock when SQLite says locked or busy and this process wrote nothing that stayed: no transaction
committed, none open, and every row change sits inside a transaction that was rolled back. So a retry cannot apply a write
twice, and a command whose first transaction landed is never run again. Each retry prints one line on stderr
(`agent mesh: database busy (...); nothing was written, attempt 2 of 4`). Exit codes are the same: 2 is a database error
(now only after the attempts or the budget are spent), 3 is a refusal.

**Dials.** `AGENT_MESH_BUSY_BUDGET_S` (default 27, chosen to stay under the 30 s subprocess timeout `brain.py` gives the
command; a script that can wait sets 60 or more), `AGENT_MESH_BUSY_ATTEMPTS` (default 4; 1 is the old single attempt),
`AGENT_MESH_BUSY_TIMEOUT_MS` (default 15000).

**What a caller should still do.** Gate the write on the claim's exit code as before. A script's own retry loop around
exit 2 is still right for stalls longer than the budget. Callers with a subprocess timeout shorter than about 28 s
(`fleet.py` 10 and 15 s, `conditioning_guard.py` 20 s) are not helped. Hooks that use the `Mesh` class directly are unchanged.

**Measured.** Old file: a 20 s write lock gives exit 2 after 19.7 s. New file, 17 controls on a temp database, all pass:
the 20 s lock is waited out and the claim lands once; a retried `send` leaves exactly one message and one event; a reader
that blocks the COMMIT ends in one claim and one event; a lock longer than the budget still ends in exit 2 with no row
left. The folder's unit suite passes 48 of 48.

**Not fixed: the stalls themselves.** The event log of 8-11 Nov has 95 moments with no event for 8 s or more and then
three or more agents inside one second (17 to 31 a day; 40 of them 15 s or longer, longest 64 s). The store is 597 MB in
DELETE journal mode with 795k events never pruned; there a COMMIT waits for every reader and every other writer and new
reader waits behind it, so one slow read stalls the fleet. A command that fails leaves no event, so the number of exit-2
failures a day before the change is not known. Next: find the slow readers, then decide between pruning and WAL
(the code comment at the `journal_mode` line records why DELETE was chosen; measure before reversing it).

Same family, different causes: [[agent_mesh_open_took_the_write_lock_three_times_2026_11_05]],
[[the_mesh_database_grew_to_416_mb_and_locks_the_fleet_2026_10_08]],
[[mesh_rc_2_is_a_locked_database_not_a_refusal_2026_10_04]],
[[the_mesh_store_is_235mb_in_delete_mode_and_exit_2_is_the_tool_failing_2026_09_12]],
[[a_push_script_stopped_on_a_locked_mesh_database_at_hello_2026_11_01]].

