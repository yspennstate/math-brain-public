---
name: t414_encoder_only_best_k_is_1_dreg_flat_std_k_squared_2026_11_01
description: [PROVISIONAL] T414 IWAE encoder-only: best K is 1 for both estimators at every budget; std error ~K^2 (b/a^2), DReG flat (beta/a^2); closed forms 6/6 out of sample
metadata:
  type: project
  created: 2026-11-01
  created_at: 2026-11-01T18:11:11+04:00
  status: provisional
  evidence: "rows/T414 moves 791370a2; kopt_run1/2, kopt_c0.9/2.5"
  originSessionId: 5f945141-4948-4871-89cc-b3d6b9f2d2b9
---

T414 (IWAE optimal K), encoder half, 1 Nov (an agent, moves 791370a2). Status: provisional (closed forms derived after the first
run, then confirmed out of sample, pre-registered 6 of 6 within 0.5 pct at c = 0.9 and 2.5).

1-D linear-Gaussian model, posterior N(0, 1/2), encoder N(mu, c/2) with only mu trained. The budget-optimal SGD error after N
sample-evaluations is F_K (1 + log)/(4N), with F_K = K var_K/lam_K^2. As K -> infinity, K lam_K -> a = (1 + chi2)(1/(4As^4) + 1/(2s^2));
the standard estimator has K var_K -> b = 4(1 + chi2)/(2A), so F_K ~ (b/a^2) K^2; DReG has K^3 var_K -> beta = (1/s^2 - 2)^2 E_q[r^4 z^2],
so F_K -> beta/a^2, flat in K (needs c > 3/4).

So with the decoder fixed the best K is 1 for both estimators at every N. DReG makes large K harmless (at most F_inf/F_1 = 1.1-3.5x
worse) but never helpful. Only the decoder's O(1/K) bias can reward K > 1; that joint half is open.

How to apply: before claiming any K* for IWAE, separate the encoder and decoder terms. Use DReG's lam as the common mean, because the
standard estimator's has about 15 pct Monte Carlo noise at K = 1024 with 2e5 reps. Mistake made on the way: the step-size grid floor
(1e-6) sat above the optimum at N = 1e7 and faked a best K of 2; the floor is now 1e-14.
Files: rows/T414/kopt.py, theory.py, kopt_*.txt, DOSSIER.md. Related: [[t421_adam_eos_time_average_35p4_not_38_universal_2026_11_01]].


ADDENDUM (1 Nov, m414b, moves a7b8aa1b): the joint half's bias term. For p(x|z) = N(theta z, 1) with a fixed-width encoder N(phi x, s^2),
theta*_K - theta0 = T/(K I), with T = -theta v^2 s^2 (s^2 - v)/(v(2 s^2 - v))^(3/2), v = 1/(1 + theta^2), I = 2 theta^2 v^2. Pre-registered,
this held within 1.2 pct at two points. Derived but untested: K*(N) = (8 T^2 N/(I L))^(1/3) ~ N^(1/3), and the error at K* is 3 times the
squared bias, ~ N^(-2/3). So K > 1 does pay once the decoder is learned, but only as the cube root of the budget.

ADDENDUM 2 (1 Nov, m414c): the K* law holds under averaged SGD. At N = 1e5 and 1e6 the best K is 16 and 32 (theory (T^2 N/I)^(1/3) = 15.2,
32.8, once you count that averaging only the second half doubles the variance). Errors are 45x and 240x below K = 1. Joint training with
the DReG or the standard encoder gradient changes the decoder's error by under 2 pct: here the paradox stays inside the encoder. The
pre-registered checks passed 4 of 4.
Practical: the SGD step must be capped near 0.02. At 0.2 the per-sample curvature (~x^2) made every K = 1..4 run diverge to NaN.
