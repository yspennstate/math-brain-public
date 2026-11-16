---
name: the_contract_lock_brake_was_the_hourly_ingest_and_harmless_quieted_2026_11_10
description: "[VERIFIED] Prompt hook says 'Contract processing failed closed (database is locked), avoid irreversible work' on the workstation? It was the hourly project-memory ingest holding the write lock 13-97 s a row (92 of 94 on 10 Nov in minutes 0-14). Harmless: prompts are re-read from transcripts, enforcement reads the hot cache file. Since 10 Nov 18:1x the lock case is logged, not injected"
metadata:
  type: project
  created: 2026-11-10
  created_at: 2026-11-10T18:18:13+02:00
  status: provisional
  evidence: ""
---

Why did agents on the workstation keep seeing "[prompt-contract] Contract processing failed closed for awareness (OperationalError: database is locked). Avoid irreversible work"? Measured 10 Nov 18:0x-18:1x, an agent-loop.

- The hook (~/.brain-framework/runtime/project_memory/hook.py) logs every failure to ~/.brain-framework/state/project_memory/contract-failures.jsonl. 4,321 rows since 18 Sep; 4,280 are "database is locked" (35 disk I/O, 2 disk full, 4 JSON escapes). 420-465 a day on 3-4 Nov, 94 on 10 Nov.
- On 10 Nov, 92 of the 94 fell in minutes 0-14 of the hour. The hourly pass (hourly.vbs -> run_bounded -> project_memory_cli.py hourly, started 18:00:39) logs its ingest as "new 49 in 680.8 s (13.893 s each) ... slowest rows 97.5 s": one write transaction per new row on the 46 GB store, held 13-97 s. The prompt hook waits 3 s (busy_timeout_ms=3000) and gives up.
- Nothing was being lost or weakened: the hourly pass re-reads every prompt from the transcripts (scan_sources: "8 grown transcripts parsed from their cursor"), and PreToolUse enforcement in the same hook reads the signed hot cache file (load_contract_cache), never the store. So the brake sentence told every agent to stop irreversible work about a hundred times a day for nothing.
- A retry (the worker machine fix of 1 Nov, [[prompt_contract_fail_closed_is_the_hourly_runner_holding_the_lock_6s_2026_11_01]]) cannot cover holds of 13-97 s, so the workstation got a different fix.

Fix, live 10 Nov 18:1x: in hook.py's exception branch, when the event is UserPromptSubmit and the detail is "database is locked", the failure row is still written but no line is injected. Every other error, and any PreToolUse failure, still prints the brake. Controls 4/4 (scratch hooklock_test.py: lock on prompt quiet; disk I/O on prompt, ValueError on prompt, lock on PreToolUse all still print). Backup hook.py.bak_lockquiet_20261110. The test wrote 4 rows into the live log; they were removed (the log is LF-terminated since, appends unaffected).

Still open, the root: 13.9 s per ingested row is slow. ingest_prompt does its classification reads inside BEGIN IMMEDIATE (store.py immediate()); moving the reads before the lock, as the 1 Nov note suggests, would shrink the window for everyone, the hot-hook writers included. Count the effect from contract-failures.jsonl: it should keep recording the locks, and agents should no longer see them.

Related: [[the_contract_hooks_failure_had_no_counter_2026_09_18]] [[the_brake_could_not_say_why_it_engaged_2026_09_18]] [[the_contract_cache_was_starved_by_the_ingest_deadline_2026_11_06]]

