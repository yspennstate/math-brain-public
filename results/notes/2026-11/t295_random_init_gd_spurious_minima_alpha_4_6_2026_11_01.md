---
name: t295_random_init_gd_spurious_minima_alpha_4_6_2026_11_01
description: [PROVISIONAL] T295 random-init GD phase retrieval at m=4d-6d, eta 0.5/log d: every failure (72) is a strict spurious local min; trapping at alpha 4 rises 58%->80% from d 100 to 400
metadata:
  type: project
  created: 2026-11-02
  created_at: 2026-11-02T00:03:17+04:00
  status: provisional
  evidence: "rows/T295 moves 71c835a3"
---

T295 (random-init GD for real phase retrieval, quartic loss, m = alpha d), 1-2 Nov, step eta = 0.5/log d, cap 20000 iterations.

Exact recovery: d = 100 gives 17/40, 26/40, 33/40 at alpha 4, 5, 6; d = 400 gives 4/20, 11/20, 17/20.

Every failure is a strict spurious local minimum. That covers all 44 at d = 100 and all 28 at d = 400. Each ends with gradient about 1e-16, a positive definite Hessian (smallest eigenvalue 0.013-0.138) and loss 0.10-0.32. At those points |x| is about 1 and the overlap ranges from 0.01 to 0.74. None of the failures is slow progress or local instability (that mode shows only at larger fixed steps, per the 16 Oct gd_pr_fail runs).

Trapping at alpha 4 rises with d (58% at d 100, 80% at d 400); at alpha 6 it stays flat (17%, 15%). So the finite-d threshold is not moving down toward the AMP value at these sizes, and an escape theorem near alpha 4-6 would have to fail with positive probability.

Pushed as a T295 move (rows/T295/gd_pr2*.py/txt, moves 71c835a3). d = 1600 (10 trials per alpha) was still running at push time. PREREG58 is scored in the scratch NEXT once it finishes.


ADDENDUM 1 (2 Nov): 2006.06997 (Sarao Mannelli et al., NeurIPS 2020) studies the same quartic loss and predicts a threshold near alpha 13.8, with strong finite-size shifts. Our success at fixed alpha 4-5 falling from d 100 to 400 is that shift, with the threshold moving up toward 13.8. The traps flatten with d (median smallest Hessian eigenvalue 0.06-0.08 at d 100, 0.02-0.04 at d 400, loss unchanged), which fits their marginal threshold states. Moves d663ea0e. Do not expect an escape theorem below about 13.8.

ADDENDUM 2 (2 Nov): the high-alpha side. Success is 39/40 then 40/40 at alpha 8, 10, 12, 14 (d 100), and 19/20 then 20/20 (d 400); the single alpha-8 failure is again a stationary trap. At these sizes the trapping edge sits near alpha 8-10, below the 13.8 theory, as 2006.06997 also saw. PREREG59 held on all three parts. Move m295c was queued while GitHub quota was out.

ADDENDUM 3 (2 Nov): d = 1600 recovers 0/10, 3/10, 7/10 at alpha 4, 5, 6. Across d 100, 400, 1600: alpha 4 0.43, 0.20, 0.00; alpha 5 0.65, 0.55, 0.30; alpha 6 0.83, 0.85, 0.70. Success falls with d at every alpha below 8, so the edge moves up toward the 13.8 of 2006.06997. Traps at d 1600 settle more slowly (gradient up to 1e-5 at the cap), and every failure ends far from x*. PREREG58: part 1 missed (exactly 0.25 lower), part 2 held. Moves 85fb03c1 (high alpha), a90b04cf (d 1600).

ADDENDUM 4 (2 Nov): Hessians of the 20 d = 1600 failures: 19 strict minima, median smallest eigenvalue 0.019, 0.016, 0.007 at alpha 4, 5, 6 (d 400: 0.037, 0.026, 0.023; d 100: 0.062, 0.070, 0.076), so the traps flatten roughly like d^-0.4 to d^-0.7. One alpha-6 failure is a saddle (eigenvalue -0.047, gradient 6.6e-3 at the cap), so at d 1600 some failures are slow saddle escapes, and the "every failure is a strict minimum" line holds only at d 100 and 400. Move m295e.

ADDENDUM 5 (2 Nov, target 2 local part): from x* + r h at alpha 8, eta 0.5/log d, random h converges 10/10 up to r 0.7 at d 100, 400, 1600. h along one sample vector diverges past r_c = sqrt(4 alpha log d / d) (1.21, 0.69, 0.38), from the cubic overshoot on z = a_1.x; the d 1600 prediction (0.5 and 0.7 fail, 0.3 succeeds) was registered first and held. Near x* the only obstruction is coherence with one sample, and it diverges rather than traps. The open step at m = alpha d is an incoherence bound for the iterates. Move m295f (b631870b).
