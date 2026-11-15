---
name: math_prefilter_per_token_sidecar_load_665_to_40_ms_2026_11_11
description: "Math hook slow before ranking (prefilter load ~1 s, 40+ s on a busy box)? Since 11 Nov the index has a per-token sidecar (<index>.lazy.sqlite), stamped with the pickle's signature; load 665 -> 40 ms, same output; stale/missing = old load"
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T19:22:44+02:00
  status: verified
  evidence: "11 Nov 19:15-19:19: live load 40 vs 665 ms; math_sense end-to-end same bytes 2.1/4.5, 3.8/11.2, 2.4/10.1 s; pf/test_lazy.py ALL PASS (157 prompts identical, 5 fallback controls); brain commit b51eb208"
---

Every math prompt loaded the prefilter index (`<store>.prefilter.pkl`, 34 MB) in a fresh process, and unpickling its postings (102,119 tokens, 3.5 million pairs) took 938 of the 962 ms on a warm cache, longer on a busy box. A query reads about twenty tokens. On 11 Nov the two worst math_sense rows of the hour were 48 s and 40 s (`budget_exhausted_before_ranking:46.1s`, `vouch_disagree`), and its served prompts ran 1.5-4 s.

Since 11 Nov 19:15 `math_prefilter.build()` writes `<index>.lazy.sqlite` (45 MB, one row per token, postings packed as uint32 pairs) right after it publishes the pickle. The sidecar is made by reading the published pickle back, stamped with that file's signature (dev, ino, size, mtime_ns), so it can only match the bytes it came from. `load()` opens it only when the stamp matches the pickle on disk now and reads a token's postings when one is asked for (`select()` prefetches the query's tokens in one read). No sidecar, a stale stamp, a corrupt file or `MATHBRAIN_PREFILTER_LAZY=0` is the old load, byte for byte. A fresh sidecar by hand: `python math_prefilter.py lazy <store>` (about 9 s).

Measured: load 40 ms against 665 ms on the live store; load+select in a fresh process 86-142 ms against 751-844 ms. Whole math_sense runs printed the same bytes both ways and took 2.1 against 4.5 s, 3.8 against 11.2 s and 2.4 against 10.1 s. On a copy of the index: 3,000 random tokens' postings, absent tokens, every other field, and select ids, scores, self-score and pinned results on 157 prompts all identical; stale, newer-pickle, corrupt and missing sidecars all fell back.

Caveat: the reader keeps the sidecar open for its process, so on Windows a build's sidecar publish waits for readers like the pickle publish always has (up to 45 s), and if it times out the sidecar goes stale and the old load runs until the next build. The rest of math_sense (ranking, vouch) still runs 2-4 s on a loaded box; that is the next place to look.

Related: [[math_prefilter_publish_waits_out_a_reader_2026_11_11]], [[proof_sense_import_compiled_344_regexes_every_prompt_now_lazy_2026_11_11]].

