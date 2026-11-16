---
name: psutil_proc_scan_holds_the_gil_froze_sampler_and_watchdog_2026_11_09
description: "[VERIFIED] Fleet resource sampler (fleet_resources.py) silent / hourly rows stale / watchdog never fired: psutil per-process cpu_times blocked while holding the GIL on a starved box, so a scan THREAD froze the main loop and the watchdog thread together; fix = scan in a child process (topscan) with a subprocess timeout"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T03:44:26+02:00
  status: provisional
  evidence: ""
---

9 Nov 2026 01:00-03:34 local: the first machine posted no hourly resource row (the second machine's hourly email listed it STALE from 23 UTC). stall.log showed the main thread stuck in pure-python summarize() while a _scan_once thread sat in psutil _pswindows _proc_info/cpu_times; one process (03:14 start) wrote nothing for 12+ minutes and its 420 s watchdog thread never fired, because a C call that keeps the GIL stops every Python thread. Moving the scan to a thread (the 9 Nov 00:43 fix) did not help for that reason. Fix (an agent, 03:3x): top_procs_child() runs 'fleet_resources.py topscan' via _run (CREATE_NO_WINDOW, timeout 240 s, child killed on timeout); the parent waits in subprocess with the GIL released; _beat is also set before summarize. Backup fleet_resources.py.bak_gil_20261109. Missing hours T21-T00 UTC posted from samples on disk by flow_agent/off/fr_backfill.py. Rule: on Windows under memory pressure, any per-process psutil walk belongs in a child process, never a thread, if something else in the process must stay alive. Related [[fleet_resources_sampler_dash_s_hides_psutil_on_windows_2026_11_08]].
