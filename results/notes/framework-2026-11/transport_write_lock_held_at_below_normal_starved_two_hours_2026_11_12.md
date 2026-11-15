---
name: transport_write_lock_held_at_below_normal_starved_two_hours_2026_11_12
description: "Transport ingest refused 'write lock busy 120 s' for two hours, pass looks hung? Lock holder starved at BelowNormal (Task Scheduler default), thread Ready, 0.3 pct of a core; fix: lock is held at Normal (c43b9f5d)"
metadata:
  node_type: memory
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T23:58:06+02:00
  status: verified
  evidence: "test_math_transport_lock_priority.py 11/11 patched, 9/11 original; brain commit c43b9f5d23524f25c52a9f28e97b6c00b2a16ebb"
  originSessionId: agent-1cb4-4f2b-ad55-8141bfd8fb70
  modified: 2026-11-13T00:07:19.317Z
---

Question this answers: `math_transport.py ingest` / `ingest-many` / `revise` says "refused: the transport write lock
was busy for 120 s; try again" again and again, the queue ages, and the scheduled pass looks hung. What is it?

What happened (12 Nov 2026, laptop). The 15-minute pass (`math_transport.py run`, task BrainMathTransport15m, started
21:53) took the write lock for its last step (the prefilter rebuild, because two store nodes were newer than the index)
and was still holding it at 23:48. It was not hung: its one thread was in state Ready, but it had used 47.6 s of CPU in
1 h 55 min, about 0.3 pct of a core. Task Scheduler starts a task at BelowNormal by default, and every core was busy
with Normal-priority work, so the job that held the lock was the last job the box would run. Two `ingest-many` calls of
29 queued results were refused meanwhile, and the 15-minute task could not start again (no overlap), so nothing was
carried into the math store for two hours.

How it was told apart from a hang: `Get-Process -Id <pid>` twice a few minutes apart (CPU moved 46.2 -> 47.5 s), and
`.Threads | Select ThreadState, WaitReason` (Ready, no wait reason). A blocked process shows Wait and a reason; a
starved one shows Ready with a crawling CPU count.

Proof of cause: setting that one process to Normal gave it 5.8 s of CPU in the next 20 s (against 1.3 s in the eight
minutes before), and 130 s in the nine minutes after.

Fix (an agent): `_write_lock` in `math_transport.py` now lifts the process to Normal while the lock is held when
it runs at Idle or BelowNormal, and puts the old class back on release (`_lift_priority`, `_drop_priority`, Windows
only, ctypes, no new dependency). A Normal or higher process is left alone; a refused lock changes nothing. Test
`test_math_transport_lock_priority.py`: 11 of 11 on the patched file, 9 of 11 on the original (the two lifts fail, as
they must). `test_math_transport_hold_race.py` and `test_math_transport_wal_copy.py` still pass. Original kept as
`math_transport.py.bak_lockprio_20261112`. Live file sha256 29e124cd979b2d93..., mirror pushed as brain commit
c43b9f5d23524f25c52a9f28e97b6c00b2a16ebb.

Not yet seen: a scheduled pass taking the lock under the new code on a saturated box. The pass that was running kept
the old code in memory. Check the next time the queue is refused: the pass should be at Normal while it writes.

How to apply. A job that holds a lock others wait on must not be the lowest-priority job on the machine. Any scheduled
task here starts at BelowNormal, so every script that takes a shared lock from a scheduled task has this exposure
(the bm25 refresh, the dream's persist, the vector build). Lift for the locked section only, never for the whole run:
the author's rule that background work stays polite still holds outside the lock. Lifting a starved lock holder is not
shedding load; stopping or suspending the jobs ahead of it would be.

The other lock sites, measured on 13 Nov 02:06 and left alone (measured: a count of each refusal message over the 332
files in `~/.claude/dreaming/logs`). `brain.py` `_memory_write_lock` (20 s): 5 refusals, in two dream logs (22 Oct,
2 Nov). `embedding_artifact.py` `file_lock` (30 s): 6, in two dream logs (25 and 30 Oct). `compact_index.py`,
`math_claim_vecs.py`, `math_recall_prebuild.py`: none. Nothing since 2 Nov. These locks are held for seconds, not for
a long rebuild, so a starved holder costs a retry and no queue backs up behind it. Lift one of them only when its
refusal shows up again with a holder in state Ready and a crawling CPU count. A third case of the same starvation
without a lock: the weekly humanness check, a headless session started at BelowNormal by Task Scheduler, needed 530 s
and was killed by an 8 minute timer three weeks running (an agent's fix, 13 Nov; `hook_liveness.py` now reports
a run that ends with no result).

Related: [[s500_music_render_starves_at_below_normal_2026_11_12]] (same starvation, no lock),
[[claim_vector_backups_never_rotated_keep_three_prune_stale_tmp_2026_11_12]] (the vector write this pass was about to make).



Consolidated 13 Nov 2026 (SWS dream) with five sibling cases into [[gist_belownormal_starvation_on_a_saturated_box_2026_11_13]] - the one mechanism under all of them.
