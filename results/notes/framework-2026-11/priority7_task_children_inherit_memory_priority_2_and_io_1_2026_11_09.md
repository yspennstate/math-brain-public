---
name: priority7_task_children_inherit_memory_priority_2_and_io_1_2026_11_09
description: "[VERIFIED] Scheduled task slow only under memory pressure / git under board publisher 300-420 s: Priority-7 task starts at memory priority 2 + I/O 1, children inherit both, 0x20 resets CPU only; board_sync sets 5/2 at import, fetch 292 -> 21-41 s; run_bounded NORMAL raise now sets 5/2 too"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T07:09:20+02:00
  status: verified
  evidence: ""
---

A Windows scheduled task at Priority 7 (the default when the XML has no Priority element) starts its process at BelowNormal CPU, memory priority 2 and I/O priority 1. Every child inherits the memory and I/O priority at creation, and the NORMAL_PRIORITY_CLASS creation flag (0x20) resets only the CPU class. Tested 9 Nov: a child of a 2/1 parent started with 0x20 comes up (memory 2, Normal, I/O 1). With commit at 95 pct, Windows trims priority-2 pages first, so that job pages heavily.

Where it bit. BrainTasksBoardPublish (wscript -> publish_board.py -> board_sync.py -> git). Board_sync already set 0x20 on git and opted the tree out of power throttling, but the live publisher read 2/BelowNormal/1 and its git child 2/Normal/1. Each run took over 15 minutes, so every second run skipped on the single-run lock. Task Scheduler's 14-minute limit killed only the wscript, and the python child kept running. git read-tree hit 180 s, and the control fetch ran 292-420 s while the same fetch from a console took 21-38 s.

Fix (9 Nov 06:3x). board_sync.py calls _normal_memory_and_io_priority() at import: SetProcessInformation(ProcessMemoryPriority=0, 5) and NtSetInformationProcess(ProcessIoPriority=33, 2) on itself. publish_board.py imports board_sync first thing in main, so both processes and every git child run at 5/2. CPU class is unchanged.

| control fetch | s |
|---|---|
| 9 Nov before (03:13 .. 06:11) | 372, 44, 217, 67, 420 refused, 348, 292 |
| 06:52, first run after | 21 |

How to apply. When a scheduled or windowless job is slow only under memory pressure, read its memory and I/O priority (GetProcessInformation class 0, NtQueryInformationProcess class 33), not just its CPU class. Raise them on the job itself, early, so the children inherit them. Do not raise other agents' work (his 18 Sep law); this changes only our own task.

Why provisional: one run measured so far. The next runs in SYNC.log are the check. Related: [[partial_clone_fetch_recopied_59mb_unmarked_pack_in_midx_2026_11_09]], [[board_publish_fetch_timeouts_and_tmp_packs_2026_11_08]], [[a_belownormal_render_stalls_on_ecoqos_opt_out_keeps_the_priority_2026_09_24]]. Task, an agent.

Held over three runs (9 Nov): control fetch 21, 41 and 23 s after the fix, against 44-420 s (median about 290 s) on the seven runs before it the same morning.

The same trap was inside run_bounded.py's NORMAL raise (RUN_BOUNDED_NORMAL_PRIORITY=1, the dream's corpus-walking steps, owner-away only). It calls SetPriorityClass, which moves the CPU class and nothing else, so a raised dream step ran at (memory 2, Normal, I/O 1): its disk reads still waited behind every other process. The live memory_twoway_sync and memory_mirror processes read (2, Normal, 1) for the same reason. Fixed 9 Nov 07:4x: _raise_to_normal also sets memory 5 and I/O 2 on the child. Test from a (2, BelowNormal, 1) parent: no raise -> child (2, BelowNormal, 1); raise -> child (5, Normal, 2). The fleet_board sync-tasks job (FleetBoardSyncTasks) got the same 5/2 in _unattended(); its before/after runtimes are still being measured.

Check for any slow background job: read the process's memory and I/O priority (GetProcessInformation class 0, NtQueryInformationProcess class 33), not just its CPU class. Of the enabled brain tasks at the root of Task Scheduler on 9 Nov, none had a Priority element, so all start at 2/1.
