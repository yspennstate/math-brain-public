---
name: the_governor_restarts_itself_at_logon_now_2026_11_10
description: "[VERIFIED] Governor dead after a reboot? Since 10 Nov ComputeGovernorAliveCheck is enabled with an AtLogOn trigger and matches the pid's command line; it relaunches only a dead governor"
metadata:
  type: project
  created: 2026-11-10
  created_at: 2026-11-10T17:18:50+02:00
  status: provisional
  evidence: ""
---

﻿The compute governor died with the workstation's reboot at 16:33 on 10 Nov and stayed down 45 minutes; it is the third time (2 Nov crash, 31 Oct wedge) because both its scheduled tasks had been Disabled since 13 and 17 Sep and nothing started it at logon.

Fixed 10 Nov 17:1x (an agent, claim topic:compute-governor):
- relaunched via launch_compute_governor.vbs: one governor, pid 15088, state ok.
- ComputeGovernorAliveCheck re-enabled, with a second trigger AtLogOn (2 min delay) beside the 30-min repeat. Its script never kills and only relaunches a governor whose pid is dead, so it cannot start a second one beside a live one.
- governor_alive_check.ps1 now tests the pid's command line for compute_governor.ps1, not just a process named powershell: after a reboot the old pid can belong to an unrelated powershell, which read as a live governor.
- a missing state file set age to Infinity; [int] of it threw under SilentlyContinue and ate the DOWN log line. Now 999999.
Controls on a copy with the launch replaced by a log line: real governor pid -> no launch; decoy powershell pid -> launch; no state file -> DOWN line plus launch. Live run against pid 15088: exit 0, governor count stayed 1.
ComputeGovernor (the governor task itself) stays Disabled: the alive-check is the only starter, so there is one path and no race.

Related: [[the_compute_governor_stayed_dead_after_the_crash_and_starved_the_dream_2026_11_03]] (its still-open question is answered here), [[stale_heartbeat_is_not_a_dead_watchdog_2026_07_15]].

