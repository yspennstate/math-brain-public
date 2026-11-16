---
name: recall_sem_realpath_gil_wait_on_side_thread_2026_11_13
description: "[PROVISIONAL] A profiling harness can invent a lock-wait lever: realpath(mem_dir) memo cut stage:sem 1.7 s -> 0.23 s UNDER cProfile, but live served sem.full was already 0 ms p50 (max 318); check calls.jsonl first (bfa540cb)"
metadata:
  type: project
  created: 2026-11-13
  created_at: 2026-11-13T07:43:21+02:00
  status: provisional
  evidence: ""
---

CORRECTION, same morning (07:5x, from the live calls.jsonl): the numbers below are from a cProfile harness, not from served calls. Live, before the fix, 48 served calls had sub:sem.full p50 0 ms, p90 0, max 318 ms, and stage:sem p50 98 ms. The live server did not pay the 1.3 s; cProfile's overhead stretched the main thread's lock holds and made the side thread wait. The memo is harmless and may trim a rare outlier, but it did NOT take served recall from 3.4 to 2.5 s. The live levers at 06:10-07:44 (n 68): stage:bm25_block p50 367 ms, lex.score ~290, stage:collapse 254 (co.superseded_known 180, p90 440).

Lesson that stands: before acting on a profile, check the same stage's arm in the live calls.jsonl. A lever that is big under the profiler and absent in the live arms is the profiler's.

(Original text, profiled numbers:) In the profiled recall server, stage:sem cost 1.7 s a call, and 1.3 s of that was four os.path.realpath(mem_dir) calls in embedding_artifact's verify-cache helpers. Each one took 340 ms (median 49 ms, max 1.1 s, side-thread probe), against under 1 ms when the process was idle.

Mechanism: the semantic lane runs on a side thread. realpath releases the interpreter lock for its syscall (_getfinalpathname), and getting the lock back waits while the main thread scores. Any lock-releasing call on that thread pays this price. The ~750 per-row os.stat calls paid it too: 9.3 s across 12 calls, falling to 0.67 s once the realpath waits were gone.

Fix (13 Nov 2026, an agent): _real_mem_dir memoizes realpath per process per spelling. Commit bfa540cb on the private repository main; the live file matches it byte for byte.

Measured with a server-shaped profile: build brain_recall_server.Brain() (all memos, resident listing, embeddings, link lists), make 6 warm calls, then cProfile 12 calls through b.call. Same questions before and after: stage:sem 1669 -> 225 ms, stage:total 3439 -> 2495 ms. Scripts: scratch area server_prof.py and rp_server.py.

Lessons:
- A cold CLI profile, or a warm one without the server memos, points at the wrong lever. Profile through brain_recall_server.Brain.
- Time a syscall twice, idle and while a recall runs. A 0 ms idle reading says nothing about the served cost.
- brain.py main() sets BRAIN_EMB_LAZY=1 for every recall, the server's included. Code in the non-lazy branch of _semantic_scores never runs when served. My 13 Nov partition speedup sits there; the lazy branch's Python sort costs only 50-85 ms, so it is not a lever.
- sed -i on this machine turns CRLF files into LF (whole-file churn in the diff). Check `file X` after a sed edit.
- Doubt to carry: one A/B pair on a loaded box. co.superseded_known read 126 -> 683 ms in the second run with no CPU behind it in the profile. Confirm on the live calls.jsonl.

Same family as graph_lane_generation_realpath_on_the_sidecar_stalled_recall_2026_10_30 (realpath on a hot path) and [[belownormal_parent_starves_recall_cli_2026_11_13]] (wait time, not CPU).

