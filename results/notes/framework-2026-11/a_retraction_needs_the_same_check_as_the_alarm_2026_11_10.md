---
name: a_retraction_needs_the_same_check_as_the_alarm_2026_11_10
description: "[PROVISIONAL] Retracting a 'service dead' alarm because a process is up now? Tie it to the launch first (start time, parent, launcher log or owner); 10 Nov Mini 2: the server I saw was hand-started, the scripted launch had died on a busy port"
metadata:
  type: feedback
  created: 2026-11-10
  created_at: 2026-11-10T21:52:10+02:00
  status: provisional
  evidence: ""
---

A retraction is a claim too. Check it as hard as the alarm it cancels.

10 Nov 23:46-23:50 Mini 2 time. A nice-0 restart of mlx-serve left no server running. I reported it to the script's owner (true). One minute later a widened probe showed mlx-serve up at nice 0, and I retracted. That was false. The scripted launch had died on "port 11240 already in use", because the old server was still in graceful shutdown and the script waited on HTTP rather than the old pid. The process I saw was the one its owner had started by hand seconds earlier. GPU idle was about 2.5 min.

**Why:** "something is running now" does not show that the launch I reported on succeeded. The fresh sighting matched my wish that my alarm was noise, so I did not check who started it.

**How to apply:** before retracting a "dead" or "failed" report on another agent's job, tie the live process to the launch in question. Compare start time with the launch line, check the parent pid, and read the launcher's own log or ask its owner. If you cannot tie them, send "up now, cause unknown", not "nothing was wrong". When restarting a server on a fixed port, wait for the old pid to exit, not for HTTP to go quiet. See [[gpu_feeder_process_must_not_sit_below_cpu_lanes_in_priority_2026_11_10]] and [[mini2_ltx_swap_thrash_fix_is_placement_not_a_flag_2026_11_10]].

