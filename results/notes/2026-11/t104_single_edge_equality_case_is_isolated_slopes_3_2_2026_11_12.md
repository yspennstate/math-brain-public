---
name: t104_single_edge_equality_case_is_isolated_slopes_3_2_2026_11_12
description: "T104 (Alon) near the single edge: is H > 0 next to one edge of weight 1? Yes for every n >= 5: s_inf = (3/2) A + ((4n-10)/(n-3)) B to first order, by S_2 x S_{n-2} symmetry; both equality cases of H are isolated"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T17:25:11+02:00
  status: provisional
  evidence: "hand proof in 06_math_research/t104_alon_agent_2026_11_11/GAP_STATE_FORM.md; measured slopes n=5..8 in t104_edge_local.out; push 110; not independently audited"
---

T104 (Alon), the second equality case. At the single edge (one edge of weight 1) the top eigenvalue 2 is simple, and to
first order s_inf = (3/2) A + ((4n-10)/(n-3)) B, where A is the weight added on edges touching the edge's ends and B the
weight on the other edges (renormalised). Both slopes are positive, so s_inf > 0 and H > 0 on a punctured neighbourhood,
for every n >= 5. Together with the star (s_inf = 4 eta + |delta|^2), both equality cases of H are isolated.

How: S_2 x S_{n-2} symmetry makes the first-order form constant on the two edge orbits. T0 = 4 sum |Z(y)><Z(y)| with
Z(y) = sym(u y^T), y sum-zero on the other n-2 vertices; the slopes are (n-2)(-1 - <K_f>) - (n-1) lam1, with
<K_23> = (n-5)/(n-3) (transposition on the standard representation of S_{n-2}) and <K_02> = 1/2 (entry count).

Evidence: hand proof in GAP_STATE_FORM.md, measured slopes n = 5..8 match (t104_edge_local.out). Not independently
audited. T104 not solved: what is left is global (away from both cases, and where the top eigenvalue is not simple).

