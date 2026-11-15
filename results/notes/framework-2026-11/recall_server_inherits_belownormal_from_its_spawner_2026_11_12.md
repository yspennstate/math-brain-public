---
name: recall_server_inherits_belownormal_from_its_spawner_2026_11_12
description: "Recall hook calls of 2 ms waiting 0.2-2.5 s with 0 ms CPU right after the recall server restarted? The server inherited BelowNormal from the hook that spawned it (12 Nov 07:15, pid 32280; 7 such rows in 3 min vs 0 in 10 h). spread_server.py now raises itself to Normal at start and logs it; test with teeth in agent_run/recall_rise/runidx. A hook-spawned helper on Windows must set its own class."
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T07:46:23+02:00
  status: provisional
  evidence: "agent_run/recall_rise/runidx/test_srv_out.txt; wait1.txt; wait3.txt; brain main ec957eb727bd"
  lesson: true
---

Recall hook calls that normally take 2 ms wait 0.2 to 2.5 s with 0 ms of process CPU and no file reads, starting right after the recall server restarted? Look at the server's priority class before anything else.

What happened (12 Nov 2026). A landing of spread_recall.py at 07:15:19 made the resident recall server (spread_server.py) exit on its code-file check and respawn, as designed. The new server (pid 32280) was at BelowNormal. Windows hands a child its parent's priority class when the parent is Idle or BelowNormal; spread_client._spawn passes no class; the hook that happened to start the server ran in a BelowNormal session. The box was at 78 to 87 pct CPU.

Measured in calls.jsonl: rows with ms >= 200, cpu_ms <= 16 and rd 0 numbered 0 in every quarter hour of the ten hours before, and 7 in the first three minutes of the BelowNormal server (240 to 2,487 ms). After the class was set to Normal by exact pid at 07:22:44: 1 such row in 19 minutes, and that one fell inside a test of mine that started High-priority children. So the class explains most of it; the busy run queue can still produce one now and then.

Not the cause: the compute governor ($RelaxPriorities is true since 9 Sep 2026, observe only; governor.log never names the server).

The fix, live since 07:39:33: spread_server.py runs _normal_priority() beside _unthrottle() at start. Idle or BelowNormal is raised to Normal, a higher class is left alone, SPREAD_SERVER_NORMAL=0 turns it off, and server.log gets one line "priority class 0x.. -> 0x..". Live sha 944d2cd7788b, backup spread_server.py.bak_prio_20261112 (sha d597a32b1692).

The test with teeth: brain_improvement/agent_run/recall_rise/runidx/test_srv_prio.py. Without the fix a child of a BelowNormal starter reports 0x4000; with it 0x20; AboveNormal and High are kept; the switch off leaves BelowNormal.

How to apply. Any resident helper that a hook spawns on Windows (a server, a warm cache, a daemon) inherits Idle or BelowNormal from whichever session spawned it, and many of our sessions and keepers run BelowNormal on purpose. A helper on the per-prompt path must set its own class at start and log it. When a latency change follows a restart, compare the process's class before and after the restart, not only the code that changed: this stall arrived with my own landing and looked at first like a fault in the landed code.

What would change this: waited rows that keep coming at Normal priority mean the run queue itself, and then the question is who holds the cores.

Also learned: a test that starts an Idle-class python on a saturated box can hang for minutes (the child is never scheduled). Give such a child a timeout with a kill and do not count its timeout as a failure of the thing under test.

