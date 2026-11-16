---
name: belownormal_recall_eval_cpu_starved_not_slow_code_2026_11_08
description: "[VERIFIED] Is the recall code slow, or is the low-priority eval process starved of CPU? Brain recall eval taking 400-800 s per call on 8 Nov: CPU-starved BelowNormal process (thread Ready, 10 s CPU per recall, box 100 pct on Normal math workers), not slow code (raised to Normal under the same 100 pct load: median 549 s -> 16 s a call); measure cpu/wall and thread state before profiling"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T06:06:15+02:00
  status: verified
  evidence: ""
---

On 8 Nov 05:4x the paired semantic-rescue recall test (semantic_rescue_paired_2026_11_08/semr_paired.py, an agent's run, pid 53900, BelowNormal) took 390-800 s per brain.recall() call. Three episodes (six recalls) took 76 minutes on 62 s of CPU in total, about 10 s of CPU per recall. The math-brain regression gate timed out the same night (rc 124).

It looked like slow code. It was not. The evidence:
- Thread states sampled five times: the main thread was Ready (runnable, waiting for a core) four times and Running once.
- Over a 20 s window the process used 0.36 s of CPU, read nothing and took 85 page faults. So it was not doing I/O and not paging.
- I/O priority was 2 (normal) and memory priority 5 (normal), read with NtQueryInformationProcess class 33 and GetProcessInformation. The process was not in background mode.
- py-spy dumps moved through ordinary recall code: _fast_listing, brain_node_documents manifest reads and open(). A cold read of the same 190 attachment files (1.7 MB) in a fresh process took 0.08-0.35 s.
- The box was at 100 pct load on 16 logical cores. The top consumers were Normal-priority math workers (rank10_t228_iv_*_piece.py, climb_18w.py).

How to tell next time: when a BelowNormal job is slow, its CPU time is a small fraction of its wall time and its threads show Ready, the job is losing the scheduler to Normal-priority work. It is not a regression in its code. Measure CPU and wall time and sample the thread states before you profile the code. Under the no-shedding law (18 Sep) you do not kill the Normal workers. Either the author of the job raises it to Normal, which is fair for a light job like this one at about 10 s of CPU per recall, or the job waits for a quieter window. Recall timings taken in such a window measure the CPU queue, not recall. Never quote them as recall speed.

Status: provisional. It rests on one night's samples. A run raised to Normal during the same kind of load would confirm it if its wall time fell to within a few times its CPU time.


**Confirmed 8 Nov 06:2x (status verified).** an agent raised pid 53900 to Normal priority at about 06:2x. Nothing else changed: same code, same run, and the box was still at 100 pct CPU at 06:29 on the same Normal math workers. Before the raise, the 12 recall calls (episodes 0-5, both arms) took 375-800 s each, median 549 s. After it, the next 8 calls (episodes 6-9) took 12-25 s each, median 16 s. That is about 33 times faster, close to the roughly 10 s of CPU each call needs. A BelowNormal process on a saturated box runs at the scheduler's leftovers, and the wall time measured its wait in the queue, not the code. Rows: out_20261108.jsonl, i 0-9.
