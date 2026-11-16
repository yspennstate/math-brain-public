---
name: t222_solver_noise_k_062_flat_vard_exponent_057_2026_11_07
description: "T222 Steele TSP variance: measured solver-noise k (best-of-2 / per-start variance) is 0.62, flat in n=400..1600 and square vs torus; at that k Var(D) ~ n^-0.57 (0.52..0.63), a=1/2 consistent (chi2 7.0/4) but the 800->1600 step is flat"
metadata:
  type: project
  created: 2026-11-07
  created_at: 2026-11-07T03:15:28+02:00
  status: provisional
  evidence: ""
---

T222 (Steele: variance of the random Euclidean TSP). Same points are solved on the square and on the torus, and D = L_sq - L_tor. The square-minus-torus variance excess is Var(D) + 2 Cov(D, L_tor). Solver noise inflates Var(D) by k (s2_sq + s2_tor), where s2 is the per-start variance and k is the best-of-2 variance as a fraction of it. Before 7 Nov, k was only bracketed in [0.5, 1], and the Var(D) exponent ran 0.51 at k=0.5 to 0.82 at k=1, so the solver could not be separated from the geometry.

Measured k (R=8 starts per instance, best-of-2 variance from disjoint start pairs, bootstrap over instances):
- n=400: square 0.642 +- 0.035 (50 instances), torus 0.605 +- 0.043 (50 instances)
- n=1600 (interim, the run is CPU-starved): square 0.607 +- 0.040 (47 instances), torus 0.616 +- 0.077 (26 instances)
- pooled 0.618. k is flat in n and in the boundary condition, so one k serves every size.

Var(D) at the measured k, five sizes n = 100..1600 (650 + 400 instances): the exponent is a = 0.57 (1-sigma 0.52..0.63). The answer barely moves across the k band 0.607..0.644 (a = 0.564..0.583). The boundary-strip prediction a = 1/2 gives chi2 7.0 on 4 dof (p about 0.14), so it is consistent. Cov(D, L_tor) corrected at this k is small and negative (about -0.002 at n >= 800).

Doubt to carry: the fit leans on n = 100..400. The last doubling is flat: corrected Var(D) is 0.00716 at n=800 and 0.00695 at n=1600, with about 20 pct s.e. on the n=800 point, so the local exponent over 800..1600 is roughly 0 +- 0.3. A sixth size (n=3200), or more n=800 instances, is what would separate n^-1/2 from a floor. The final k from the full R=8 run is expected to move by under 0.02, which moves a by under 0.01.

Files: the private repository, 06_math_research/frontier/rows/T222/coupled/calib_k_interim_20261107.out, decompose_measured_k_20261107.out, calib_k.py, calib_k_part.py. Runner: brain_math_loop_1e0a/op/t222/src/coupled_r8.py (out_r8/).
Related: [[t222_five_size_excess_n_minus_0_6_2026_11_07]] [[t222_coupled_square_torus_excess_real_and_decaying_2026_11_06]] [[t222_square_variance_excess_decays_like_n_to_minus_two_thirds_2026_11_06]]



7 Nov 08:0x interim (n=800 at 150 pairs, was 100): Var(D) at 800 stays 0.0117 (se 0.0013), so the flat 800->1600 step (0.0117 vs 0.0121) holds; Var(D) exponent at k=0.6 is 0.575 [0.522,0.630] (was 0.572), a=1/2 at delta-chi2 2.0. Raw Cov(D,L_tor) at 800 moved -0.0041 -> -0.0050 (within 1 se). Nothing moved. File rows/T222/coupled/decompose_n800w150_20261107.out. Pace, measured: the n=800 widening does one 50-instance job per ~1.6 h (5 jobs left, ~16:30); the R=8 n=1600 torus file has 15 of 50 instances after 4.7 h (~19 min each, ~11 h more). The earlier 'interim ~10:00-11:30' guess was off.
