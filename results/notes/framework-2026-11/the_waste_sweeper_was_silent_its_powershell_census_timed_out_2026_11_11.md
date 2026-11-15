---
name: the_waste_sweeper_was_silent_its_powershell_census_timed_out_2026_11_11
description: "Waste sweeper (hook_reaper, BrainWasteSweeper20m) log silent? 11 Nov 00:57-02:2x its PowerShell census timed out (>240 s) on the starved box and died unlogged; its pipe list also skipped find/head/sort. Now psutil census 11 s, full FRAGMENTS list, ERROR lines, VBS starts python directly."
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T02:32:05+02:00
  status: verified
  evidence: "hook_reaper.log: no line 00:57->02:23; live process 58048 (02:13) still in its Get-CimInstance child at 02:18; new census timed 11 s (scratchpad time_reaper.py); first live run logged 02:31 candidates=1 spared_msys=17"
---

The 20-minute waste sweeper (task BrainWasteSweeper20m -> hook_reaper.vbs -> hook_reaper.py) wrote no log line from 00:57 to 02:2x on 11 Nov 2026, while the box was in ui_freeze and the slow probe was telling every session to reap orphans by hand.

Two causes, both fixed 11 Nov 02:2x by an agent:
- The census was a PowerShell `Get-CimInstance Win32_Process` subprocess with a 240 s timeout. A bare PowerShell start took 23-32 s that night, and the launcher added its own PowerShell hop (the 02:10 fire reached python at 02:13). The census timed out, `main()` raised, and the top-level `except` printed an error to a hidden console and exited 0 with no log line, so a silent log looked like "nothing to reap". The census now reads one psutil process snapshot (through `_usersite`, because the task runs `python -s`) and reads a command line only for an orphaned python or powershell: 11 s against more than 240 s. The PowerShell census stays as the fallback if psutil fails to import. Any failure now writes an `ERROR` line to hook_reaper.log, and the VBS starts python directly.
- `DEAD_PIPE` named only sleep, tail and grep, while waste_sense's FRAGMENTS also names find, head, sort, du, wc, cat, uniq, sed, awk, xargs and cut. An orphaned `find ... | grep | head` from a dead agent shell walked the repos for 10 minutes at 107 s of CPU and was never swept. `DEAD_PIPE` now matches FRAGMENTS. The MSYS-parent test still spares every fragment of live work: the dry run spared 22 and flagged 0.

How to apply: when a periodic sweeper's log goes quiet, read the gap as a failure until a fresh line proves otherwise. A guard that exits 0 on error must leave a line. Keep a guard's name list identical to the list that names its victims to agents (waste_sense FRAGMENTS here); a fix at one site is only a note ([[a_fix_at_one_site_is_a_note_not_a_fix_2026_08_24]]). Backups of the old files are in the session scratchpad as hook_reaper_before.py/.vbs. Related: [[waste_sense_msys_verdicts_shared_two_minutes_2026_11_10]].


Third cause, found 02:4x the same night: the task's own limit. BrainWasteSweeper20m stops a run after 10 minutes, and the 02:28 fire ended with result 267014 (terminated). Task Scheduler stops wscript only; the python it started lives on as an orphan (pid 53996, started 02:30, still alive at 02:53 holding a console, killed by pid). So a slow run leaves no log line AND a leaked process. The task now runs at priority 4 instead of the default 7 ([[hidden_scheduled_task_slow_start_priority_4_and_early_opt_out_2026_11_11]]). The 02:48 fire then logged at 02:53:12 and ended normally (killed one 24-minute orphaned bash), so a sweep currently takes about 5 minutes of wall time and 35 s of CPU on an 870-process box: well inside the limit, but not the 11 s measured by hand.

Fourth fix, 03:0x: the psutil census was itself the slow part. psutil.process_iter asking each process for its name and start time took 223 s wall and 35 s CPU on 921 processes (one OpenProcess per process on a full run queue); one Toolhelp snapshot (CreateToolhelp32Snapshot) gives pid, parent and exe name for all of them in 0.06 s. The census now takes the snapshot and calls psutil only for an orphan in the watched names (its start time, and a command line for python/powershell). Whole sweep, dry run: 0.9 s, same three candidates as the old census. For any census on this box: snapshot first, per-process calls only for the few rows you judge.
