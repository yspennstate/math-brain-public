---
name: checklist_loop_reopen_written_with_the_next_save_2026_11_11
description: "Checklist hook slow on loop ticks (each reopen of a done entry loaded and saved 15 MB)? Since 11 Nov the reopen waits in a small file and the next locked save folds it in: 3.2 s -> 91 ms, same entry and ledger"
metadata:
  node_type: memory
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T18:06:44+02:00
  status: verified
  evidence: "scen_test.py old vs new: entry, ledger rows, printed lines identical; in-process on a 15 MB copy reopen median 3158 -> 91 ms; selftest pass; live md5 89cfb91c; brain main de354977"
  modified: 2026-11-11T16:22:33.765Z
---

A loop session closes its checklist entry every round, and the next tick of the same words reopened it with a whole-state load and save of the 15 MB state.json under the lock: 73 such reopens between 17:00 and 17:47 on 11 Nov. The checklist hook's median prompt was 35 ms and its mean 277 ms; 51 of 174 prompts ran over 300 ms and carried 92 pct of its time (measured by an agent).

Fixed 11 Nov (an agent, live md5 89cfb91c, brain main de354977). The session sidecar (session_latest.json) now also names each session's newest entry from the last three days, its ask key and its count of "asked again" notes. When the sidecar is current, the session has no open entry and its newest entry is this ask, the prompt writes the reopen to a small file in .stop_pending/ (<session>.<ns>.reopen), prints the same two lines as before and returns. A second tick while that file waits is a silent no-op, the same as a tick on an open entry.

Every locked load_state folds pending reopens in before anything else changes, so an agent's done, a closing-line Stop or the flush child writes the reopen first and then its own change. state.json keeps the newest reopen applied per session (reopens_applied), so a load that is never saved cannot apply one twice. The folded ledger rows are written ahead of the next ledger row, so the order stays the same. Reopen files are deleted after the replace and before the sidecar is rewritten, so a reader in between sees a stale stamp and takes the full path. A Stop with a reopen pending takes the full path. The feature follows Stop coalescing: off with TASK_CHECKLIST_STOP_COALESCE=0 (the selftest's store) and with TASK_CHECKLIST_NO_FAST=1.

Checked before landing: one loop round run through the old and new hooks on temp stores (register, done, reopen, same tick, plain Stop, note, closing-line Stop, reopen, flush child) gave the same entry, the same ledger rows in the same order, the same printed lines, and no files left behind. In-process on a copy of the live 15 MB store, five reopen ticks took a median of 3,158 ms on the old hook against 91 ms on the new one (the box was loaded: commit near 95 pct), with the same five "asked again (time 2..6)" notes. The selftest passes. Rollback: task_checklist_hook.py.bak_reopen_20261111 (md5 d71c55c1).

Second case, fixed the same evening (live md5 28cdafa4, brain main 9de1668f, rollback .bak_alt_20261111 = 89cfb91c). In the first 20 minutes after landing, the prompt mean got worse (433 ms, 18 of 59 over 300 ms). The slow ticks came from loop sessions that alternate between two asks (agent, agent, agent, agent, 600-3,100 ms each). Both of those entries stay open, and each tick names the one that is not the session's latest. The full path then only adds "asked again" and moves latest, but the sidecar held only the newest entry, so these ticks missed the deferral. The sidecar now keeps, per session, the newest entry for each ask key from the last three days (map "k"), and the deferral takes any of them. While reopens are pending for a session, the newest pending entry counts as its latest, and the plain same-ask fast path steps aside. Without that, the second ask of an alternating pair was dropped silently (caught by the test, not live). Checked: an alternating A/B loop (ticks, a done, reopen, note, repeats with a reopen pending) and the single-ask round, both run through the original full-path hook, give the same entries, ledger rows in the same order and printed lines; selftest 0 failed. Known and left alone: the count in "asked again (time N)" stops rising near 42 because updates are trimmed to 40. Both paths do this.

How to apply elsewhere: when a write can wait for the next writer, leave it beside the store and fold it in at every locked load, with a marker in the store that makes it apply once. Related: [[checklist_stop_bursts_written_once_by_a_flush_child_2026_11_11]], [[checklist_view_temp_files_leaked_470_mb_now_swept_2026_11_11]].

