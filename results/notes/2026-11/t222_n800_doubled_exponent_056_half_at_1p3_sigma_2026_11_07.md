---
name: t222_n800_doubled_exponent_056_half_at_1p3_sigma_2026_11_07
description: "[PROVISIONAL] T222 Steele TSP variance: n=800 doubled to 300 coupled pairs; corrected Var_D exponent at k=0.62 is 0.565 [0.515, 0.616], 1/2 at 1.3 sigma; k decides it"
metadata:
  type: project
  created: 2026-11-07
  created_at: 2026-11-07T15:16:33+02:00
  status: provisional
  evidence: ""
---

T222 (Steele TSP variance, square vs torus on the same points). The n=800 row was the thin one: 150 coupled pairs, and its Var_D sat low against the 800 -> 1600 step. coupled4.py ran three more seeds (78003-78005, 50 instances each, finished 7 Nov 14:27), so n=800 now has 300 pairs. decompose.py rerun at 15:1x, output rows/T222/coupled/decompose_n800w300_20261107.out.

What moved:
- n=800 raw Var_D 0.0117 +- 0.0013 (150 pairs) -> 0.0127 +- 0.0010 (300 pairs), inside one standard error. Cov(D, L_tor) unchanged at -0.0050.
- Solver-noise-corrected fit Var_D ~ C n^-a, five sizes 100-1600:
  k=0.62 (the measured solver-noise factor): a 0.575 [0.522, 0.630] -> 0.565 [0.515, 0.616], chi2 4.12 on 4 dof; a=1/2 gives chi2 5.75, so 1/2 sits about 1.3 sigma out.
  k=0.6: a 0.556 [0.506, 0.606]; k=0.5: a 0.511 [0.464, 0.559] with a=1/2 inside; k=0 (no correction) 0.345; k=1 0.796.
- The 800 -> 1600 step of the corrected Var_D (k=0.62) is a ratio of 0.85 where n^-1/2 predicts 0.71: still the flattest step, now less flat than before.

Reading: the boundary-strip heuristic (Var_D ~ n^-1/2) survives the doubling; the exponent leans a little above 1/2 at the measured k but does not exclude it. The answer is held by k: the fit runs from 0.35 to 0.80 as k goes from 0 to 1, so the open question is k, not more seeds at 800.

Note on the printout: decompose.py formats k with one decimal, so k=0.62 prints as "k=0.6"; the first of the two k=0.6 lines is 0.62.

How far to trust it: one solver (tsp.exe best of 2 starts), one decomposition, the k factor from calib_k_interim (no ALLDONE_R8 marker yet). What would change it: calib_k.py on the full calibration set moving k outside 0.5-0.7, or n=3200 pairs.

Earlier record: [[t222_solver_noise_k_062_flat_vard_exponent_057_2026_11_07]], [[t222_five_size_excess_n_minus_0_6_2026_11_07]], [[t222_coupled_square_torus_excess_real_and_decaying_2026_11_06]].

