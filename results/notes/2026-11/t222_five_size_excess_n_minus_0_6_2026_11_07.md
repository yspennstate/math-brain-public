---
name: t222_five_size_excess_n_minus_0_6_2026_11_07
description: "[PROVISIONAL] T222 Steele TSP variance, five sizes to n=1600: square-minus-torus variance excess real (chi2 33/5 vs zero), decays n^-0.6 (0.41-0.85), solver noise ruled out; exponent 1/2 vs 2/3 open"
metadata:
  type: project
  created: 2026-11-07
  created_at: 2026-11-07T00:42:51+02:00
  status: provisional
  evidence: ""
---

T222 (Steele TSP variance), coupled square/torus estimator, now at five sizes n = 100, 200, 400, 800, 1600 (1600: 400 instances, seeds 86000-86015).

Excess Var(L_sq) - Var(L_tor), paired bootstrap s.e.: 0.0170 +- 0.0037, 0.0131 +- 0.0053, 0.0058 +- 0.0045, 0.0034 +- 0.0037, 0.0041 +- 0.0022.
Fit C n^-a: a = 0.595, 1 sigma [0.41, 0.85], chi2 0.57 / 3 dof. Zero excess rejected: chi2 33.2 / 5 dof.
Fixed exponents (4 dof): 1/4 4.27, 1/3 2.61, 1/2 0.80, 2/3 0.68, 1 2.63. So 1/2 and 2/3 both fit; 1 is about 1.4 sigma off, 1/4 about 1.9 sigma.
Solver-noise control (control both ways): d = s2_sq - s2_tor from the two heuristic starts is mixed in sign and at most a quarter of the excess s.e. Refitting excess - k d for k = 0, 0.5, 1 gives a = 0.60, 0.56, 0.53; the zero-excess chi2 stays 33-35.

Reading: the square's extra variance is real and dies with n, so square and torus share the variance limit in this range; the solver's own noise does not make the excess. The exponent is NOT pinned (four-size value 0.71 moved to 0.60 when n=1600 came in a little high). What would change it: n = 3200 coupled, or an exact solver on a subsample.

Evidence: 06_math_research/frontier/rows/T222/coupled/ (coupled_result.txt, fit_excess.out, heur_noise.out, fit_corrected.out, scripts); move appended to rows/T222/moves.jsonl 2026-11-07 00:41. Updates [[t222_coupled_square_torus_excess_real_and_decaying_2026_11_06]] (four sizes) and [[t222_square_variance_excess_decays_like_n_to_minus_two_thirds_2026_11_06]].
