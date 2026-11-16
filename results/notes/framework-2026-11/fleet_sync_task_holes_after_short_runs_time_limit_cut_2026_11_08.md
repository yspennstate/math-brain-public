---
name: fleet_sync_task_holes_after_short_runs_time_limit_cut_2026_11_08
description: "Task export (FleetBoardSyncTasks) missed 68/126 min after short clean runs on 7 Nov; machine awake, scheduler log disabled; ExecutionTimeLimit cut PT72H->PT1H 8 Nov"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T18:50:18+02:00
  status: provisional
  evidence: ""
---

FleetBoardSyncTasks (the first machine task export to the private task board, every 20 min, IgnoreNew) twice skipped several starts right after a SHORT clean run: 7 Nov 02:55 (5 min run, next start 68 min later) and 7 Nov 21:37 (run 21:37:03-21:39:59 rc 0, next start 23:43:20, 126 min). Of 445 runs in run.log, every other gap over 30 min follows a long run (20-40 min, the 3-4 Nov runs), which IgnoreNew skipping explains.

What the evidence rules out: the machine was awake and Task Scheduler was firing - BrainTasksBoardPublish logged every 15 min through 04:40-06:43 JST 8 Nov (= 21:40-23:43 +0200). fleet_board.py writes its "--- <time> sync-tasks" header line-buffered as the first thing under pythonw, so no python reached main during the hole.

Not provable: Microsoft-Windows-TaskScheduler/Operational is DISABLED on this workstation (wevtutil gl: enabled false), so there is no record of triggers fired or ignored. Leading hypothesis: the previous instance did not exit after printing "rc 0" (the rc line is printed before sys.exit; wscript waits on pythonw), and IgnoreNew skipped triggers while it hung. fleet_board.py starts no threads.

Hardening done 8 Nov 18:4x (before 18:51 JST) (an agent, mesh claim topic:schtask/FleetBoardSyncTasks): ExecutionTimeLimit PT72H -> PT1H (read back; action, IgnoreNew and Interactive logon unchanged). A stuck instance now blocks at most two cycles instead of up to three days. The longest real run seen was 39 min (3 Nov). If holes recur after short runs, enable the scheduler's Operational log (admin) or add os._exit(rc) after the rc line.

