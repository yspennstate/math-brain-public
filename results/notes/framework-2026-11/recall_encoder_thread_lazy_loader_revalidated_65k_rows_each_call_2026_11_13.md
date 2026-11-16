---
name: recall_encoder_thread_lazy_loader_revalidated_65k_rows_each_call_2026_11_13
description: "[VERIFIED] Served recall seeds/lex slow beside the query-encoder thread? The worker's lazy load_verified_embeddings redid set(slugs), isfinite on 65k x 384, two slug dicts, the hash dict and the mean every call (135-518 ms warm, GIL-bound). Memoized per resident parse 13 Nov: 9-23 ms; served seeds med 225 -> 101 ms, call p90 3230 -> 2044, answers 7/7 same"
metadata:
  type: project
  created: 2026-11-13
  created_at: 2026-11-13T17:56:29+02:00
  status: provisional
  evidence: ""
---

status: verified

Symptom: in brain_recall_server, stage:seeds carried 50-170 ms nobody could find inside it; BM25.score ran 8-45 ms instead of 4-17.
Test: the same served calls with BRAIN_RECALL_QUERY_EMBED=0 dropped seeds warm median 84 -> 61 ms, so the encoder thread (_qemb_start in brain.py) was competing for the GIL.
Cause: the thread calls _full_embeddings -> embedding_artifact.load_verified_embeddings. With BRAIN_EMB_LAZY=1 and RESIDENT the sidecar parse is cached, but the checks and maps built from it were not: len(set(slugs)), np.isfinite(vecs).all(), {slug: i} twice, dict(zip(slugs, hashes)), vecs.mean - about 200 ms of Python per recall on 65,299 rows.
Fix (embedding_artifact.py, commit 521073c81730): compute them once per parse object, kept in _RES['derived'] next to _RES['sidecar'] and cleared with it; every call still gets its own dict copies.
Check: old vs new loader equal on index, bias, text_hashes, row_of, verify_key, built_ns, verify_cache and matrix, for lazy/eager x resident/not; copy isolation tested. Served A/B, one process, alternating loaders, 21 calls each on a loaded workstation: seeds median 225 -> 101 ms (p90 538 -> 206), call median 1744 -> 1420 ms (p90 3230 -> 2044), same top lines 7 of 7.
Lesson: a resident cache of the raw data is half the job when the per-call code still rebuilds everything derived from it; profile what runs AFTER the cache hit. A side thread's Python work shows up as slowness in whatever the main thread is doing at that moment.
Related: [[recall_sem_realpath_gil_wait_on_side_thread_2026_11_13]], [[recall_server_housekeeping_belongs_in_the_idle_tick_2026_11_13]]

Live check (13 Nov 18:12, server successor pid 59484 reloaded at 17:53 on the code change): 16 live calls after vs 100 calls
15:00-17:47 before - stage:seeds median 144 -> 134 ms, p90 240 -> 189; call median 1033 -> 938 ms. Real but about a third of
the in-process A/B gain: the harness's old arm paid more contention than live traffic does. Quote the live figure.
