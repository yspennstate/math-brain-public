---
name: mesh_importer_missed_cli_retries_2026_11_12
description: "Mesh importer database is locked although agent_mesh CLI retries; board ingester loses cycles"
metadata:
  type: feedback
  created: 2026-11-12
  created_at: 2026-11-12T15:30:17+02:00
  status: provisional
  evidence: ""
  lesson: true
---

Between 5 and 11 Nov the board ingester lost 25 cycles: 19 at BEGIN IMMEDIATE, 3 at COMMIT, 2 at the open PRAGMA, and 1 at schema repair. Each missed mirror cycle cost 15 minutes. The 12 Nov change passed 23/23 throwaway-database tests, with a row written exactly once after lock release; a live board cycle surviving contention was not yet observed.

CLI main retried refused commands, but scripts importing Mesh constructed it directly and got no CLI retry. Rollback-journal readers and writers can block different stages.

**Why:** Resilience in a command wrapper does not protect callers that import its class.

**How to apply:** Use bounded patient_s for background importers (the ingester asks 30 seconds), leave hook waits short, retry only the safe open/BEGIN/COMMIT boundaries rather than the transaction body, and read mesh_slow.log before choosing a fix; older running processes retain old code.

[[mesh_importing_callers_patient_s_and_the_slow_transaction_log_2026_11_12]]

Drafted by Codex worker W07 of the 12 Nov 04:43 order (H20_1112), screened and filed by an agent. Provisional: the worker read the source, nobody re-measured it.

