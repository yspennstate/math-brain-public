---
name: t261_ridgeless_rf_smin_bounded_off_n_eq_p_2026_11_02
description: T261 gap (a) ridgeless RF at k1=k2=2 (softplus, d 16-48): feature-matrix smin/sqrt(max) bounded off n=p (limits ~0.025 at n/p .5, 0.006 at 2), collapses at n=p; ridgeless error stable in d; ridge->ridgeless uniform in lam*n not lam
metadata:
  type: project
  created: 2026-11-02
  created_at: 2026-11-02T03:08:10+04:00
  status: provisional
  evidence: "frontier/rows/T261 move m261a, moves.jsonl 604558c4"
  originSessionId: 5f945141-4948-4871-89cc-b3d6b9f2d2b9
---

T261 (random-features ridge regression in polynomial scaling), frontier row 06_math_research/frontier/rows/T261, move m261a by an agent on 2 Nov 2026 (moves.jsonl blob 604558c4; files smin.py, herm.py, smin_run1.txt, smin_run2.txt in the row folder). It is on gap (a) of an agent's 18 Oct restatement: ridgeless lambda = 0 at finite size with k1 = k2 = 2, the case 2403.08160 leaves open because it needs lambda > 0. The same gap is T260's Target 2; T260's own ridgeless test was proportional only.

Setup: softplus activation (mu_0, mu_1, mu_2 nonzero), p = d^2/2, d from 16 to 48, 4 seeds.

Results:
- Off the diagonal, the smallest singular value of the feature matrix over sqrt(max(n, p)) stays bounded away from 0. From d = 24 to 48 it moves 0.0301 -> 0.0274 at n/p = 0.5 and 0.0094 -> 0.0079 at n/p = 2, flattening; c + a/d fits give c about 0.025 and 0.006. The degree-0 and degree-1 spikes do not carry it.
- At n = p it collapses, from 9.1e-5 to 3.5e-5.
- The ridgeless test error has a stable profile in d (1.14-1.22 at n/p = 2) and blows up at n = p (up to 8,232).
- Ridge with penalty lam n |a|^2 tends to the ridgeless error, within 0.1% by lam = 1e-9, but the lam needed shrinks like 1/n. So convergence is uniform in lam n / smin^2, not in lam.

PREREG70: (a) and (b) passed; (c) missed for exactly that scaling reason.

How to apply: before testing "the limits commute", fix the ridge normalization against the paper's, or compare in lam n / smin^2. Evidence only: one activation, and no bound is proved.


Related: [[t260_deep_random_features_match_gaussian_model_to_noise_floor_2026_10_30]] (the same ridgeless gap in the proportional regime, where its n = p peak gap turned out to be seed noise).
