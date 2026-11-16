---
name: fleet_sampler_lost_freeze_fix_in_a_sync_and_starved_at_below_normal_2026_11_13
description: "Laptop STALE or thin in the fleet resource table (HOURLY.md), GPU a dash? The sampler lost its 9 Nov freeze fix in an 11 Nov sync and starved at BelowNormal; merged back, task priority 7 -> 4, full hour seen (111 samples, 55 min, GPU 65)"
metadata:
  type: project
  created: 2026-11-13
  created_at: 2026-11-13T05:06:13+02:00
  status: verified
  evidence: "hourly.jsonl row 2026-11-13T02: 111 samples, 55 minutes, gpu_avg 65.1; rows T00 and T01: 1 and 9 samples, gpu null"
---

The workstation showed STALE in the fleet resource table (the coordination board's hourly resource file)
from the 23:00 UTC row of 12 Nov, and its rows had a dash under GPU. Two causes, both fixed 13 Nov 03:57-04:05 by
an agent under a standing request (rank 4 of the task list, resource reports).

1. A sync dropped a fix. The live sampler ~/.claude/dreaming/fleet_resources.py (sha e8fd5b26a45c, written 11 Nov 02:13
   by session agent) carried the newer report text but had lost the 9 Nov freeze fix that the copy
   .bak_daygap_20261111 (sha 7847cb12b7f9) still held: the process scan in a child with a 240 s timeout, the 420 s
   stall watchdog, the single-instance lock, covered minutes counted from sample times. Without it the sampler sat
   ninety minutes (02:13 to 03:43) inside an in-process psutil scan while RAM stood at 99.5 per cent, and the 00 UTC
   row went out with one sample. Repair: git merge-file with the board copy (commit 4e45f89fe) as base, ours the live
   report half, theirs the .bak sampler half; clean merge.
2. BelowNormal starvation. Task Scheduler started the sampler at priority 7 (BelowNormal). On this saturated box that
   process got 0.7 s of CPU in 150 s, took minutes to reach its first line, its board post hung past 80 s, and the
   nvidia-smi read (5 s timeout) came back empty, which is the dash under GPU. A _normal_priority() call at the top of
   run_sampler was not enough: the interpreter starved before reaching it. What worked: scheduled task
   FleetResourcesSampler Settings.Priority 7 -> 4 (action unchanged, pythonw, no console).

Live file now sha 174530f21cd2; brain-tree mirror 12_cognitive_architecture/dreaming/fleet_resources.py same bytes
(commit f8020d2807c). Rollback: copy fleet_resources.py.bak_freezefix_20261113 over the live file and restart the task
by its exact name.

Measured after the fix: the 02 UTC hour (04:00-05:00 local, 13 Nov) has 111 samples, 55 minutes covered, GPU average
65.1, max 100. The two hours before had 1 sample / 0 minutes and 9 samples / 6 minutes, GPU empty.
Not yet confirmed when this was written: the row on the board and the workstation leaving STALE in HOURLY.md (rewritten
at :12 past by the worker machine). The board's own copy tools/fleet_board/fleet_resources.py (365 lines, 8 Nov) is older
than both halves and still to be replaced.

How to apply: when one file is synced between a live folder and a mirror, diff both directions before overwriting; a
newer date does not mean it holds every fix. A scheduled task on this workstation that must report on time runs at task
priority 4, not the default 7. A thin hourly row (few samples, minutes_covered far under 60) or an empty GPU field
is the sign.

Related: [[gist_belownormal_starvation_on_a_saturated_box_2026_11_13]],
[[transport_write_lock_held_at_below_normal_starved_two_hours_2026_11_12]],
[[humanness_check_starved_at_below_normal_2026_11_13]], [[belownormal_parent_starves_recall_cli_2026_11_13]].

