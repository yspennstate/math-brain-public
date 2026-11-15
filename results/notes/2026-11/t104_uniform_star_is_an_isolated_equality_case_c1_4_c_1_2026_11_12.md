---
name: t104_uniform_star_is_an_isolated_equality_case_c1_4_c_1_2026_11_12
description: "T104 (Alon) near the uniform star: is H > 0 next to K_{1,n-1}? Yes for every n >= 5: s_inf = 4 eta + |delta|^2 + h.o., constants proved by branching [n-2,2] to S_{n-1} and a second-order perturbation"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T17:18:27+02:00
  status: provisional
  evidence: "hand proof in 06_math_research/t104_alon_agent_2026_11_11/GAP_STATE_FORM.md; exact sympy Kato expansion n=5,6; Richardson n=5..12; push 109; not independently audited"
---

Alon's T104, row in the probability top-200 list. Next to the uniform star K_{1,n-1} the top-eigenvector state satisfies
s_inf = 4 eta + |delta|^2 + O(eta |delta| + eta^2 + |delta|^3) for every n >= 5 (eta = total leaf-leaf weight, delta = leaf
weight deviation). Since H >= s_inf wherever the top eigenvalue is simple, H > 0 on a punctured neighbourhood of the star.

How: S_{n-1} symmetry (Schur) reduces the expansion to two constants. Both come from the branching
[n-2,2] -> [n-3,2] + [n-2,1] (Jucys-Murphy contents n-3 and 0, so M = 2/(n-1) and 1 on the two parts), the fact that
Pi(u (x) y) lands in the [n-2,1] part, and the transposition character on the standard representation. c1 = 4 is first
order; c = 1 is (n+1)|delta|^2 - n|delta|^2 after second-order perturbation (tr(Pi2 T2) by the trace dim V' = m(m-3)/2).

Evidence: hand proof in GAP_STATE_FORM.md (section "c = 1 and c1 = 4 for every n >= 5"), exact sympy Kato expansion for
n = 5, 6 (t104_star_exact.py/.out), Richardson n = 5..12. Not independently audited. T104 is not solved: the open places
are away from the star and the single-edge equality case. What would change it: an audit finding a dropped term in
the V1-V2 cross blocks of T1.

