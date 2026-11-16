---
name: t222_coupled_square_torus_excess_real_and_decaying_2026_11_06
description: "[PROVISIONAL] T222 Steele TSP variance: same points solved in square and torus metric; square excess real (chi2 29.7/4 vs 0) and decays n^-0.71 (0.43-1.12), shared limit holds with no torus prior"
metadata:
  type: project
  created: 2026-11-06
  created_at: 2026-11-06T21:13:03+02:00
  status: provisional
  evidence: ""
---

T222 (Steele's variance-limit conjecture, random Euclidean TSP). 6 Nov 21:1x, an agent. Status: provisional (heuristic tours, n <= 800).

FIRE WHEN T222, the square-vs-torus variance limit, or the boundary decay rate p comes up.

Why: the 17:58 control showed the square table alone cannot test the shared limit; the 06:42 p = 0.67 needed the torus plateau as an input ([[t222_square_variance_excess_decays_like_n_to_minus_two_thirds_2026_11_06]]). Fix: a coupled estimator - tsp.c solves each random point set twice, unit-square metric and flat torus, so the instance noise is shared.

Result (paired bootstrap s.e.): excess Var(L_sq)-Var(L_tor) = 0.0170+-0.0037 (n100, 300 inst), 0.0131+-0.0053 (n200, 200), 0.0058+-0.0045 (n400, 150), 0.0034+-0.0037 (n800, 100). Zero excess: chi2 29.7 on 4 dof. Fit C n^-a: a = 0.71, 1 sigma 0.43..1.12; chi2 (3 dof) 0.80 at 1/2, 0.30 at 2/3, 0.84 at 1, 3.26 at 1/4 (dchi2 3.0, ~1.7 sigma). So the excess goes to zero and p ~ 2/3 is reproduced without the torus prior; p = 1/4 is disfavoured, not excluded.

Size of the doubt: corr(L_sq, L_tor) was only 0.64-0.83, so pairing cut the s.e. about 2x, not 10x (the point sets match but the optimal tours rearrange near the boundary). The preview at 20:40 (without n100) resolved nothing - n100 carries most of the signal. What would change it: coupled n = 1600 at ~100 instances, or exact tours.

Files: the private repository, 06_math_research/frontier/rows/T222/coupled/ (tsp.c, coupled2.py, analyse_coupled.py, fit_excess.py and outputs); move appended to rows/T222/moves.jsonl 21:11. Side lesson from the run: on a saturated box EcoQoS opt-out is inside the noise ([[gist_belownormal_starvation_on_a_busy_box_2026_10_20]]).
