---
name: laptop_memory_push_every_10_min_halves_the_lag_2026_11_08
description: "Laptop memories reach GitHub slowly / BrainMemoryMirror every 30 min: changed to PT10M 8 Nov; runs 6-8 min fire-to-land under load, lag p90 ~38 -> ~18 min"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T01:46:01+02:00
  status: provisional
  evidence: ""
---

The workstation's memory push (task BrainMemoryMirror, wscript -> launch_mirror.vbs -> memory_mirror.py, MultipleInstances IgnoreNew) fired every 30 minutes until 8 Nov 2026. The run itself is short (about 20 s, max 208 s over four days, 191 runs, never a plan with more missing than one batch), so the wait was the schedule, not the work: workstation-to-GitHub lag measured p50 18.7 min, p90 37.7 min (mtime of the newest file to its landing, n 335).

Change, 8 Nov ~01:07 local time, an agent (recall loop): Triggers[0].Repetition.Interval PT30M -> PT10M, nothing else. Backup of the task XML: BrainMemoryMirror_before_20261108.xml (restore with schtasks /Create /XML ... /TN BrainMemoryMirror /F).

Measured on the first three PT10M runs, under heavy memory pressure (RAM ~2-3 GB free, commit 92-94 pct, PowerShell starts 24-38 s):
- fired 01:11:53, python start logged 01:18:22, 2 landed 01:19:59 (8.1 min fire to land)
- fired 01:21:52, start 01:27:11, 2 landed 01:28:05 (6.2 min)
- start 01:38:27, 1 landed 01:39:22 (commit ba00b91e79e2)
Most of each run is interpreter start-up under load (4.5-6.5 min from fire to the first log line); the push itself is 6-11 s. Landings now come about every 10 min, so the worst-case lag falls from ~38 min to ~18 min; on a quiet machine it would be nearer 10.

Cost: one API commit per run only when something is missing (most runs land 1-2 files); a run with nothing to push does a head compare. No GitHub Actions on the brain repo, so no billing.

What would change it: if two runs overlap (start-up longer than 10 min) IgnoreNew drops the second fire, harmless; if the API's secondary rate limit starts refusing (403), go back to PT15M. Owner of the task: an agent (told on the mesh).

