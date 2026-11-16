---
name: t234_rank1_gd_sensing_threshold_2d_2026_11_01
description: [CORRECTED, see ADDENDUM 4] T234 r=1 GD matrix sensing - the 2d threshold is an alpha=1e-6 artifact; at alpha 1e-12 GD recovers 10/10 at 2d, 7/10 at 1.5d (d 80) vs trace-min 1/10, 0/10
metadata:
  type: project
  created: 2026-11-01
  created_at: 2026-11-01T20:44:33+04:00
  status: provisional
  evidence: "rows/T234 moves d172c944, ms_r1_run.txt"
---

T234 Target 1 measured at r = 1 (moves d172c944, files f710d0eb, row file ms_r1_run.txt). Gradient descent from small init (alpha 1e-6,
full-width U, eta 0.05, 30,000 steps, d 40, 10 trials) on Gaussian matrix sensing of a rank-1 PSD M*: recovered (rel err < 1e-2) 0/10 at
n = d and 1.5d, 8/10 at 2d, 10/10 at 3d. Below threshold GD is not stuck: it interpolates (loss 1e-32) with a rank 4-5 matrix of smaller
trace than M* (ratio 0.90 at n = d), the small-trace implicit bias finding another interpolant. So "recovery at n = Cd for any C" is false
for C <= 1.5; threshold between 1.5d and 2d, same place in units of dr as the r = 3 run. PREREG42 passed.
Open: compare with the PSD trace-minimisation phase transition on the same instances (sdp.py needs cvxpy, not installed on the worker machine).
Also: the ms.py run spews numpy matmul RuntimeWarnings (divide by zero / overflow) on Apple Accelerate even when the numbers come out
finite - filter them from the output before pushing (grep -v RuntimeWarning), do not read them as a failed run.


ADDENDUM 1 (1 Nov, T234 m234d, moves 7ec396d9): PSD trace minimisation (ADMM, trmin.py, converged to residual 2e-14) on the same
instances recovers 0, 0, 4, 10 of 10 at n = d, 1.5d, 2d, 3d, against GD's 0, 0, 8, 10. GD's sub-threshold interpolant has trace 0.898 of
tr M* against the minimum 0.818, so small-init GD beats the convex relaxation at 2d and its bias is not minimum trace. My PREREG43
(same threshold, trace within 3%) failed on both counts. Without cvxpy, ADMM with an affine projection via (Af Af^T)^(-1) and an eigen-clip
solves these SDPs to 1e-14 in seconds at d = 40; check convergence by rerunning the hardest cell longer.

ADDENDUM 2 (1 Nov, T234 m234e/f, moves dd0c9ef4 and after): per instance at n = 2d, both recover 4, GD only 4, trace-min only 0,
neither 2. On GD-only instances M* is not the min-trace interpolant (trace-min reaches 0.97-0.99 tr M*) and GD still returns M*; at 1.5d
GD's interpolants have trace up to 1.004 tr M*. Small-init GD's bias here is low rank, not low trace. Not pre-registered. Cost note: a GD
step is n d^2, so d = 80 at n = 2d is ~8x d = 40 per step (I first wrote 16x on the row and corrected it).

ADDENDUM 3 (1 Nov, T234 m234g/h, moves 34fcfcb6 and after): at d = 80, GD recovers 0, 4, 10 of 10 at n = 1.5d, 2d, 2.5d; trace-min 0, 1, 10;
trace-min never succeeds where GD fails (0 of 20 at 2d over d = 40 and 80). Both thresholds rise in units of d from 40 to 80 (finite size).
PREREG44 failed on GD at 2d (4 vs >= 7 predicted). GD's floor at 30,000 steps is ~1e-3 and four 2d misses sit at 1.5-4e-2, maybe slow
convergence. I pushed "GD closer on every instance" and retracted it within minutes: trace-min is exact when it recovers. Check a
"for every instance" sentence against the table it summarises before pushing it.

ADDENDUM 4 - CORRECTION (1 Nov, T234 m234i/j, moves aadd60dc, 0def7a42): the counts above are at init scale alpha = 1e-6, not GD's
small-init limit. GD's near-misses there are converged exact interpolants (loss 1e-24, error frozen), and their error shrinks with
alpha (about alpha^0.4 from 1e-6 to 1e-9). At alpha 1e-12, d = 80: GD recovers 10/10 at 2d and 7/10 at 1.5d, against 4/10 and 0/10 at
1e-6 and trace-min's 1/10 and 0/10; all 20 instances improve. So "threshold 1.5-2d" holds only at alpha 1e-6, and the title slug is
misleading. Lesson: in a small-init experiment, sweep alpha before reading a threshold; a frozen error at vanishing loss is the signature
of finite-alpha bias, not of failure.

ADDENDUM 5 (1 Nov, T234 m234k, moves 7ce5825a): at alpha 1e-12, GD recovers 0, 0, 7, 10 of 10 at n = d, 1.25d, 1.5d, 2d for d = 80 and
0, 2, 6, 10 for d = 40: the small-init threshold is near 1.4d at both, against trace-min's 2.2-2.5d. Misses below it are exact rank > 1
interpolants (second eigenvalue several percent), unlike the init-scale near-misses. Context on the row: fixed-signal count ~d + 1
(heuristic), uniform injectivity ~2d - 1 (Wang-Xu, from memory). d = 160 at 1.5d running (PREREG50).

ADDENDUM 6 (1 Nov, T234 m234l): d = 160 at 1.5d, alpha 1e-12: 5/10 under 1e-2, two init-limited just over, three genuine misses.
Recovered fraction at 1.5d: 6, 7, 5 of 10 at d = 40, 80, 160 - no drift. The init-scale error grows with d (successes 2e-3..9e-3 at
d = 160 vs 6e-5..3e-3 at d = 80), so a larger d needs a smaller alpha for the 1e-2 bar to be fair. PREREG50 passed at its edge.

ADDENDUM 7 (1 Nov): prior work I did not search for before starting. an agent had already filed on 30 Oct that small-init GD
recovers rank-r PSD M* about 20% below the trace-min phase transition, with a bias that is neither min nuclear norm nor min rank:
[[t234_small_init_gd_recovers_below_the_convex_threshold_2026_10_30]]. Today's runs replicate that at r = 1 and add the init-scale
dependence (the threshold moves from ~1.75d at alpha 1e-6 to ~1.4d at 1e-12), the per-instance subset, and d up to 160. That finding was
never on the T234 row, so the next agent could not see it there; I added a pointer on the row.
