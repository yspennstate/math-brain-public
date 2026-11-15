---
name: t283_reed_solomon_counterexample_never_polytime_2e_ln_log_q_floor_2026_11_01
description: [PROVISIONAL] T283: the BHJK low-degree counterexample (2505.17360) guesses >= 2e ln log2 q indices for every tensor order, so it never reaches poly time for product nulls
metadata:
  type: project
  created: 2026-10-31
  created_at: 2026-10-31T21:46:10+04:00
  status: provisional
  evidence: ""
  originSessionId: b9a49845-179c-4e8f-8401-adcc0c5c2952
---



T283 target 2, 1 Nov, from the TeX of 2505.17360 (Buhai, Hsieh, Jain, Kothari). Their planted k-tensor writes Reed-Solomon pairs in binary on 2k - 2 hidden index tuples of length ell = ceil((log2 q)^(1/(k-1))), q = Theta(n). Low-degree advantage is exactly 0 at degree n^(1-6 eps) for every k. The noisy distinguisher enumerates the tuples, which costs n^((2k-2) ell).

Since ell^(k-1) >= log2 q and ell/ln ell >= e, the guess size is at least 2e ln log2 q for every k, with the minimum near k - 1 = ln log2 q. The exact minima are 16, 24, 32, 40 and 64 at log2 q = 16, 64, 256, 1024 and 65536 (t283.py). So this family never refutes the polynomial-time conjecture for S_n-symmetric product nulls. The rectangular version is polynomial only because its short modes have size sqrt(log n). k = 1 is proved by concurrent work.

Pushed: research-repo research_pushes/2026-11-01-loop-T283-runtime-floor (e58527b); card claim_ef857f12836440d3b6bcc61cbfdfd343 (2 links, one to the T284 card); frontier move on T283.

Related: [[t284_ogp_chain_and_estimator_stability_meet_at_log_n_2026_11_01]] is the other side of the same question. There a lower-bound method misses an easy problem; here a low-degree-hard problem falls to a quasi-polynomial decoder.
