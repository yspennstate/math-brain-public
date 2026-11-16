---
name: recall_server_started_a_thread_inside_every_call_2026_11_12
description: "Recall calls that skip the walk slow (20 ms and tails of seconds) on the loaded workstation? The server started a thread inside every call; Thread.start waits for the new thread to run (33 ms median, p90 136). One resident thread woken by an event since 12 Nov 08:25: 2.2 ms median, max 8.6 on 20 live rows"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T08:58:31+02:00
  status: verified
  evidence: "12_cognitive_architecture/brain_improvement/agent_run/recall_rise/runidx/test_fs_out.txt"
  lesson: true
---

**What was wrong (found 12 Nov 2026 08:14, an agent).** `spread_server.py` started one `FaultSampler` thread
inside the timed part of every recall call. Python's `Thread.start()` returns only when the new thread has run, and on
this workstation with every core busy a new thread waits in the run queue: 33 ms median to start one at 08:14 (p90 136,
max 219), 18 ms median at 08:29 (p75 220, max 507), measured from a fresh Normal-class process. Waking a thread that
already exists from an event wait cost the caller 0.02 ms in the same minutes. So every per-prompt recall call of
every Claude session paid a thread start, and the calls that skip the walk (which should take 2 ms) showed it most.

**Fix, landed 08:25:12.** The sampler is one resident thread woken by an event; the per-call object only hands it the
job. Live `~/.claude/dreaming/spread_server.py` sha c5a7544c8b87b5c7, backup `spread_server.py.bak_sampler_20261112`,
brain main a8fabf3333cd. Off switch `SPREAD_SERVER_FAULT_RESIDENT=0`.

**Measured.** On copies (test_fs.py, six parts pass): start() for the caller 0.045 ms median against 21.5 ms with the
old class, and the old class fails the same under-2-ms check; samples still name the busy function; 100 calls leave
the thread count at 2. Live, calls that skip the walk since 08:25:33 (the first 20 rows, 0 errors): 2.2 ms median, p90
8.6, max 8.6. Before, 05:15 to 08:25: 268 rows, 4.8 ms median, p90 32.2, max 2,487; on the server of 07:41 to 08:25
alone the median was 11 to 24 ms as the load moved. The rule set beforehand was under 8 ms median on 20 rows.

**The 07:33:31 stall is not a count against the Normal-priority fix** ([[recall_server_inherits_belownormal_from_its_spawner_2026_11_12]]):
that one 2,467 ms call at Normal class had 0 file opens, 0 samples and 6 page faults, and fell inside my own priority
test (07:31:12 to 07:35:51), whose part C ran busy AboveNormal and High class children. No such children on this box
while sessions are live.

**The rule.** Nothing that creates a thread or a process belongs inside a per-call timed path on a loaded machine;
keep one resident worker and wake it. To find such a cost, time the primitive itself from a fresh process in the same
minutes (thread start, stat, event set) before blaming the code around it.

**Size of the doubt.** 20 live rows over 30 minutes; the before-figure moves with the box's load, which is why the
comparison is paired with the thread-start timing of the same minutes (recall_rise/runidx/stl1.txt, stl2.txt).

