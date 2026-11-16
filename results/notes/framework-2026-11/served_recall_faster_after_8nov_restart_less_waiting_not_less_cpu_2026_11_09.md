---
name: served_recall_faster_after_8nov_restart_less_waiting_not_less_cpu_2026_11_09
description: "Served recall faster since 8 Nov? Yes, 3.4 -> 2.1 s median over 24 h, but from the 06:53 AboveNormal self-priority (row 28), not the 01:45 restart; held 19 h incl. a loaded evening, CPU per call unchanged"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T02:43:32+02:00
  status: provisional
  evidence: ""
---

Over 24 hours, served recall (brain_recall_server, calls.jsonl) got faster: median 3,358 -> 2,115 ms, p90 5,894 -> 3,784 ms (958 vs 1,207 calls). The 8 Nov 01:45:23 restart onto graph_lane a641c98c did not cause it. The server raising its own priority to AboveNormal from 06:53 on 8 Nov did, which is ledger row 28 in [[recall_server_sets_its_own_priority_outside_set_dies_on_restart_2026_11_08]]. This note confirms that row 28 held for 19 hours.

These numbers leave out calls with no session id and calls that rebuilt a cache (miss_s set). Medians by window:

| window | calls | wall median | p90 | CPU median |
|---|---|---|---|---|
| 7 Nov 01:45 - 8 Nov 01:45 (before) | 958 | 3,358 | 5,894 | 2,609 (last 80 calls only; cpu_ms was first logged 7 Nov 23:45) |
| 8 Nov 01:45-04:00 (restarted, quiet hours) | 90 | 2,275 | 4,381 | 2,562 |
| 8 Nov 04:00-06:33 (restarted, loaded box, Normal priority) | 77 | 4,521 | 9,060 | 3,015 |
| 8 Nov 06:53-12:00 (AboveNormal) | 443 | 1,956 | 3,028 | 2,515 |
| 8 Nov 12:00-18:00 | 227 | 1,984 | 3,454 | 2,609 |
| 8 Nov 18:00 - 9 Nov 01:45 (evening dream and renders) | 367 | 2,183 | 3,352 | 2,843 |

- CPU per call stayed between 2.5 and 3.0 s throughout, so the code did no less work. What fell was waiting for a core. From 06:53 on, the wall-clock median is about 0.6 s below the CPU median: the call runs on several threads, and the 4.5 s loaded stretch was queueing.
- A check that the change wasn't just a different mix of sessions: the 22 sessions that recalled in both 24 h windows were each faster, with a median per-session ratio of 0.68. These are not 22 confirmations. All 22 ran on one box in the same two windows, so together they make one before/after observation.
- How to apply: if served recall slows again, compare the server's priority class and wall-minus-CPU in calls.jsonl before touching the code. A restart only looks like a speedup if it lands in quiet hours.

Why provisional: box load is uncontrolled. The evidence that the fix holds under load is one evening, 18:00-01:45 on 8 Nov, when the box was starved (RAM 2-7 GB free, commit 91-92 pct). Related: [[recall_time_follows_the_machines_load_not_rebuilds_2026_11_06]], [[belownormal_recall_eval_cpu_starved_not_slow_code_2026_11_08]].

Scripts: prepost24.py, matched_nomiss.py, split653.py (task, an agent).
