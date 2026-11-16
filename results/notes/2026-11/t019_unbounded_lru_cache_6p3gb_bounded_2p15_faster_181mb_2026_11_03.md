---
name: t019_unbounded_lru_cache_6p3gb_bounded_2p15_faster_181mb_2026_11_03
description: Scar 3 Nov: T019 5-unpinned certifier with lru_cache(maxsize=None) per graph reached 6.3 GB and swapped for 45 min with no group done; maxsize 2^15 ran 30k tuples in 32.8 s at 181 MB (2^17: 61.5 s, 586 MB), same values
metadata:
  type: project
  created: 2026-11-03
  created_at: 2026-11-03T13:13:44+04:00
  status: verified
  evidence: "frontier/t019_seq_probe5_30000.out and _c15.out in session 5f945141; peer warning msg-3e7e2e1032"
---

What happened: t019_seq_run.py 4 7 5 (Delta 4, q 7, all five block vertices unpinned) shares count_c and w_c caches across every problem on one graph. The first group (bare star, about 250k tuples) grew them without bound to 6.3 GB resident; the process fell into swap at about 15-20% of a core, finished no group in 45 minutes, and pushed swap to 7.2 of 8 GB with disk free falling (an agent flagged it on the mesh).

Measured fix (t019_seq_probe5.py, first 30,000 tuples of that group): maxsize 2^17 took 61.5 s and peaked at 586 MB; maxsize 2^15 took 32.8 s and peaked at 181 MB, with the same worst value 0.3789. Smaller was faster, because the hit rate barely moves while a smaller table thrashes memory less.

How to apply: any memoised recursion that is shared across millions of subproblems gets a bounded cache from the start, and a probe of the first few thousand items, with peak RSS, before the full run. Eviction only costs recomputation. Related: [[t019_delta3_q5_glauber_open_bdg_is_block_chain_hamming_fails_2026_11_03]].
