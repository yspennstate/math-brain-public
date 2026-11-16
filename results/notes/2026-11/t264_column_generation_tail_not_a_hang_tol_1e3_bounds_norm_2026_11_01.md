---
name: t264_column_generation_tail_not_a_hang_tol_1e3_bounds_norm_2026_11_01
description: [CORRECTED, see CORRECTION - one LP also hangs near round 426] T264 stalled solve is the column-generation tail (price 1.01-1.10 for 400+ rounds), not a hang; tol 1e-3 bounds the norm to 0.1%
metadata:
  type: project
  created: 2026-11-01
  created_at: 2026-11-01T22:20:08+04:00
  status: provisional
  evidence: "grid5g_log.txt, grid5f 35 CPU-h no output"
---

T264's grid5f.py (min-norm ReLU interpolation in d = 2 by column generation over HiGHS, mvn4.py solve(), tol 1e-6, up to 3000 rounds,
60 units a round) ran 45 h / 35 CPU-h without finishing its first solve. A round log (t264/grid5g_log.txt in an agent's
scratchpad) shows why: +120 columns a round, max reduced price oscillating 1.01-1.10 for hundreds of rounds (1.19 at round 75, 1.01 at
425), never near 1 + 1e-6 - the usual column-generation tail, worsened by the fine angle refinement around the top directions. 50 rounds
take 3 s, so it is not slow rounds; one silent stretch was CPU starvation on a loaded box (2.6 CPU-min in 20 min), not an LP hang.
Fix: the column-generation bound obj / max_price <= OPT <= obj means tol 1e-3 already gives the norm to 0.1%; grid5g.py takes TOL and
ITMAX from the environment and prints the final price, rounds and time. Lesson: before waiting days on a column-generation solve, log the
max price per round; a price stuck a few percent above 1 is the tail, and the tolerance, not the hardware, sets the run time.


Related: [[t264_min_norm_relu_interpolant_d2_l2_near_1p8_1d_solve_ill_conditioned_2026_10_30]] - the same row's solver, whose d = 2 runs this stall blocked.

CORRECTION (1 Nov, 22:3x): the sentence "one silent stretch was CPU starvation on a loaded box, not an LP hang" is wrong. A second run at
TOL 1e-3 follows the same deterministic path (identical max prices round by round) and also went silent right after round 425, after
500+ CPU-s there. So the 45 h stall is the tail PLUS one LP that does not finish: 83 rows, 52k columns, almost surely simplex degeneracy
in HiGHS's warm-started re-solve. The tolerance fix alone does not cure it. Under test: the same run with HiGHS solver=ipm (grid5h.py,
env LPSOLVER); its prices match simplex round for round, at about 4x the time a round.

ADDENDUM 1 (01 Nov 22:48): fixed and verified. grid5i.py = tol 1e-3 + each simplex LP capped at 30 s (time_limit set as
getRunTime() + 30, see [[highs_time_limit_is_cumulative_set_runtime_plus_budget_2026_11_01]]) + an interior-point re-solve of a capped LP.
At round 433 the simplex hit the cap and ipm finished the LP in 9 s; R 0.06 converged in 166 s, norm 138.07 vs 138.05 from the earlier
converged run (0.014%). The 45 h run never got past that LP. On the row as move m264o (files bcee1744, moves a3a58c68). Pure ipm also
works, at about 4x the time a round.
