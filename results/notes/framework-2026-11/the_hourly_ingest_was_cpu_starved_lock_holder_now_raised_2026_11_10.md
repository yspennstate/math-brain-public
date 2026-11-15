---
name: the_hourly_ingest_was_cpu_starved_lock_holder_now_raised_2026_11_10
description: "[PROVISIONAL] Hourly project-memory ingest slow / prompt hook waits on 'database is locked'? BelowNormal pass was CPU-starved holding the write lock: A/B 398 vs 906 vs 397 rows/200 s; since 10 Nov the lock holder runs at Normal-equivalent thread priority"
metadata:
  type: project
  created: 2026-11-10
  created_at: 2026-11-10T19:19:22+02:00
  status: provisional
  evidence: ""
---

The hourly project-memory pass (hourly.vbs -> run_bounded.py -> project_memory_cli.py hourly) runs BelowNormal, and on a busy box its ingest was CPU-starved, not slow: each row holds the store's write lock (store.immediate, BEGIN IMMEDIATE) for the whole row, so a starved pass also kept the author's UserPromptSubmit hook waiting on that lock (a priority inversion; the "database is locked" contract brake of the same day).

Measured 2026-11-10 19:07-19:17 on the live 19:00 pass, 200 s per arm, rows = committed ingest_seq:
  A BelowNormal 398 rows, 36.0 CPU-s | B Normal 906 rows, 93.7 CPU-s | C BelowNormal 397 rows, 46.3 CPU-s
Rows per CPU-second were the same (9.7-11.1): the work did not change, the CPU it got did. Earlier probes ruled out cold B-tree reads, the SQLite cache size, classification and _session_prior.

Fix landed 19:2x: store.py gets _lock_scoped_priority(); while the process class is BelowNormal or Idle, the thread holding the write lock runs at THREAD_PRIORITY_HIGHEST (6+2 = 8, a Normal thread) and is restored in finally. Other threads and Normal-class callers are untouched. Controls 7/7 (raised inside, restored after commit and after an exception, rollback kept, Normal untouched, a second thread untouched). Backup store.py.bak_lockraise_20261110 (sha256 be22a68bdbf06bde...). Patch script and controls: lockraise_patch.py / lr_ctl.py (session agent scratchpad).

To check: the 20:00 pass's "project-memory ingest:" line in hourly_bounded.log.child against the 17:00 and 18:00 passes. What would change this: if the 20:00 ingest is no faster, the lock does not cover most of the row's CPU and the raise must move to the whole ingest loop.


Related: [[the_contract_lock_brake_was_the_hourly_ingest_and_harmless_quieted_2026_11_10]] (the prompt-side quieting of the same lock wait).

CORRECTION 20:1x (same session): run_bounded already raises the pass to Normal while compute_state reads owner_away_open (RUN_BOUNDED_NORMAL_PRIORITY=1 in hourly.vbs since 2026-09-17) and opts it out of power throttling every hour. The passes that starve are the author-present ones (17:00 and 18:00 on 10 Nov: "owner present ... the child keeps the caller's class", 60.1 s and 13.9 s a row). The lock-scoped raise therefore matters exactly when the author is at the keyboard, which is when the prompt hook's wait matters; on an owner-away pass it is a no-op.

MY MISTAKE in the A/B: ab_prio.py read the child's class at 19:05:43, before run_bounded raised it to Normal at 19:06:18, then set that stale 0x4000 for arms A and C and "restored" 0x4000 at the end. It left the 19:00 pass at BelowNormal for the rest of its life: its review-row hydrate took 1794 s against 31 s at 18:00, and the 2700 s cap cut the review publication after one project. A priority A/B must re-read the class immediately before each change and restore what it read last, or better, run only when the runner's own log says the child kept the caller's class. The rows-per-arm comparison is unaffected (both priorities ran on the same pass).

Public: the same raise is on yspennstate/brain-framework main as 7ee245d (10 Nov 20:1x), inside the darwin Background try/finally; package controls 7/7 patched, 6/7 unpatched.

SECOND RAISE, THE CONTRACT-CACHE BUILD (11 Nov 02:0x, an agent-loop). The signed hot cache (contract-cache.json, read by every agent's PreToolUse) went 3.6 h stale: the 23:02 and 00:06 passes (owner present, BelowNormal) died at the 2700 s cap inside build_contract_cache. Its child-log marks: sections_key at +222 s and +293 s, then live-brain's contract rows at +1,127 s (1,057 s on an earlier starved pass), against +0 s and 2-17 s on owner-away passes. Two changes in runtime/project_memory/hot_cache.py (backup of the pre-wrapper file in session agent scratchpad, hot_cache.py.bak_20261111_0200):
1. _sections_key reads max(ingest_seq) only. count(*) scanned a covering index of 365k text HMACs; ingest_seq is the AUTOINCREMENT key and nothing deletes prompt_events (grep), so the max moves on every insert. Read-only on the live store: 0.004 s.
2. build_contract_cache wraps the body (now _build_contract_cache) in store._lock_scoped_priority(), so the build's thread runs at a Normal thread's priority on a BelowNormal pass. Checked: imports from hourly_runner and reclassify; under SetPriorityClass BelowNormal the thread reads 0 before, 2 inside, 0 after.
CHECKED 11 Nov 02:28 on the 02:06 owner-present pass (BelowNormal, pid 57784): sections_key at +0 s (was +222 to +293 s), live-brain contract rows at +29 s (was +1,057 to +1,127 s), all 19 projects by +405 s, written at +508 s; hot-contract-cache.json (the real file name; contract-cache.json above is wrong) rewritten 02:28:40, its first write since 10 Nov 22:17. The pass reached the contract_cache phase at 1,302 s of its 2,700 s cap; scan_sources took 595 s against 1,387 s the pass before. Not mirrored to the public brain-framework repo yet. What would change this: an owner-present pass that again dies at the cap inside the build.
