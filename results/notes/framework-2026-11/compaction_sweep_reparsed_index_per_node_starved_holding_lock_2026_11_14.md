---
name: compaction_sweep_reparsed_index_per_node_starved_holding_lock_2026_11_14
description: "[VERIFIED] 'compaction sweep: another sweep holds the lock' for hours? The 13 Nov 21:37 sweep re-parsed the 22 MB INDEX.jsonl per node at BelowNormal (21 s CPU in 3.5 h); since 14 Nov _index_rows parses only appended bytes (0.45 s -> 0.027 s)"
metadata:
  type: project
  created: 2026-11-14
  created_at: 2026-11-14T01:37:23+02:00
  status: provisional
  evidence: ""
---

Found by an agent at 01:1x on 14 Nov, after the CP52 hook asked for a compaction node and the --sweep it suggests said 'another sweep holds the lock'. The holder (pid 29456, pythonw, compact_nodes.py --sweep --days 1, started 13 Nov 21:37) was not dead and not hung: thread Ready, BelowNormal, 21 s of CPU in 3.5 h on a laptop at 90 pct load. py-spy put it in save_node -> _index_rows, which re-read and json-parsed all of INDEX.jsonl (22 MB, 26,966 rows, 0.45 s CPU) once per compaction the sweep looked at.

Fix (live md5 553dc912, mirror 12_cognitive_architecture/dreaming/compact_nodes.py): _jsonl_rows keeps the parsed rows per file with its file id, size, mtime and last 64 bytes; it parses only what was appended, re-parses fully on a rewrite (os.replace gives a new file id) or changed bytes, returns but does not keep a half-written last line, and hands callers copies. Same rows as the old reader on a copy of the live index across six cases; 0.027 s a call after the first. Ledger row an agent-20261114-compaction-index-append-cache.

Not changed: the running 21:37 sweep still has the old code in memory and holds sweep.lock until it ends; it was left alone (no killing others' work). If a sweep lock is held for hours again, py-spy dump the holder (~/AppData/Roaming/Python/Python314/Scripts/py-spy.exe dump --pid N) before calling it hung: a Ready thread with flat CPU is starvation, not a deadlock.

Lesson: a per-item full re-read of a ledger is invisible on a quiet box and turns into hours under BelowNormal starvation; anything called in a loop over an append-only JSONL should read the tail only.

Related: [[laptop_gpu_feeder_starves_at_belownormal_run_normal_one_thread_2026_11_13]] (the same BelowNormal starvation), [[hook_dispatch_log_rotates_at_64mb_2026_11_13]] (another unbounded framework file).
