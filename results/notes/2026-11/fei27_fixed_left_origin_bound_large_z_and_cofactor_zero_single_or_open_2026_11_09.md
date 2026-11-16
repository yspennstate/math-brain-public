---
name: fei27_fixed_left_origin_bound_large_z_and_cofactor_zero_single_or_open_2026_11_09
description: "[PROVISIONAL] Partly (FEI27): fixed-left origin bound proved for ln z >= (a0+b0)/u and exactly for cofactor-zero left lists; open for L = x OR B at 1<z<exp((2-p)/p)"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T06:32:51+04:00
  status: provisional
  evidence: "the private brain repository: 06_math_research/frontier/T021/fei27_fixed_left_large_z_bound_cofactor_zero_exact_value_2026_11_09 (98ab89f67c)"
---

Not fully (FEI27, 9 Nov): the last open step of two-path CT, FEI25's continuous origin bound for the fixed-left right-path game, is now proved in two places and open in one named family.

Proved:
- Every genuine fixed-left list with u = |b0 - a0| > 0, either orientation: the uncapped sector estimate N_infinity <= K i with K = 1 + (a0+b0)/u, so the origin bound (1 + ln z) b0 holds whenever ln z >= (a0+b0)/u. The supersolution is implicit: K(b0 + u alpha) minus the supremum running cost of arrival staircases. The range shrinks to nothing as u -> 0. The u = 0 case is one-path and uses p V_z.
- Cofactor-zero left lists (L = x AND B or (NOT x) AND B, so every pure-AND left staircase): exact continuous game value P = p t^2/s + p t (z-1) min(p t/s, 1/(z+1)), t = alpha + epsilon, s = 1 + alpha + beta. Optimal play stops when p t/s <= 1/(z+1), otherwise one AND move to the switching line. FEI23's multiplexer lemma already gave CT here; the new part is the exact value. Its running-cost curl is zero, so it does not extrapolate to mixed lists.
- An exact z = 1 potential A_1(alpha)/(1+alpha+beta) for every left list.

Open, smallest family: L = x OR B, mean(B) = 1 - p, 1 < z < exp((2-p)/p), and the negative relative orientation. The natural pulled-back one-path potential fails there (p = 3/4, alpha = 0, beta = 1, z = 4, residual (3/4) ln 3 - 7/8 < 0). That rules out the potential, not CT.

Checked: I reran verify.py (rc 0, 12 s) and audit.py in a copy laid out like the fleet tree. Every JSON field matched the original except folder byte counts and timing. audit.py asserts that REPORT.md quotes the original cpu numbers, so it is run against the original VERIFICATION.json. Next: FEI28 (proof attempt on the single-OR family) and FEI29 (numerical value function and counterexample hunt there, blind to FEI28), started 06:20.

Credit the Math Brain in the Acknowledgments of anything published from this.

Builds on [[fei25_fei26_lm_tight_m_to_1_no_proof_no_counterexample_2026_11_09]] (FEI25 named this obligation; FEI26 showed LM is sharp) and [[fei23_two_path_reserve_reduced_to_log_moment_lemma_2026_11_09]] (the reduction to LM/CT).
