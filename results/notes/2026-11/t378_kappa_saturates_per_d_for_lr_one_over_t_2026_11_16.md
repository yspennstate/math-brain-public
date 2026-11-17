---
name: t378_kappa_saturates_per_d_for_lr_one_over_t_2026_11_16
description: "[PROVISIONAL] T378 one-pass mean-field SGD path-norm drift kappa: with lr~1/t it settles at every d 8..64 (limits ~9.2/14.5/15.5/16.1, slow growth in d); with lr~t^-0.6 it is still accelerating at d32 at n=1e8, so d16's 'halving' was not saturation. Proof route: martingale noise sums (a>1/2) + finite length of the drift via Lojasiewicz on the analytic population loss (Tadic arXiv:0907.1020); gaps: iterate boundedness, Tadic's step condition, degenerate set."
metadata:
  type: project
  created: 2026-11-16
  created_at: 2026-11-16T22:46:31+02:00
  status: provisional
  evidence: ""
---

Runs and tables: 06_math_research/frontier/rows/T378/DOSSIER.md sections of 16 Nov 22:0x-22:38, files runs/long/out_b_* and out_c_*. Seeds agree to 0.08. What would change it: d32 a=0.6 to 1e9 (running on Mac 1) still accelerating would mean slow-decay steps need n >> 1e9 or diverge.

16 Nov 23:0x: Tadic arXiv:0907.1020 Thm 2.1 read: with martingale SGD noise the condition is sum alpha_n^2 gamma_n^{2r} < inf for some r>1, i.e. a > 3/4 for alpha_n = n^-a. Candidate lemma: on the event E_K (iterates stay in a compact away from dead/parallel neurons) kappa_n converges a.s. for a in (3/4,1]. Only P(E_K) is open. DOSSIER section 16 Nov 23:0x.

16 Nov 23:2x CORRECTION: with lr~1/t the flow time grows like log n (about 8 units of n0/B steps at 1e8), so the a=1 limits 9.2/14.5/15.5/16.1 are lower bounds, not limits; the const run at d32 reaches 19.13 at flow time 1000 and is still rising. The log d conjecture is withdrawn until a const-step d sweep reaches flow time 1e3 or more. d32 to 1e9: a=0.6 21.54 (slowing), a=0.75 19.13 (not slowing).
