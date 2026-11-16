---
name: p0434_two_atom_finite_load_sup_is_s2_by_a_resultant_2026_11_08
description: "[PROVISIONAL] P0434 8 Nov: on {1,K}, 2<K<=9/4, the finite-load sup of E T_MS/E T_G is S2(K); resultant of the two partials has fixed sign, so no interior max; branch formula still numerical"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T04:57:55-05:00
  status: provisional
  evidence: ""
---

P0434 (M-SERPT vs Gittins, mean response time ratio R on laws supported in [1, K]). On two-atom laws {1, K} the
finite-load sup is S2(K), the tie-mass value from route item 22, for 2 < K <= 9/4, and the proof is a resultant, not a grid.

How it goes (route_agent.md item 25, the private repository main 727647c1, 06_math_research/frontier/P0434/route_agent_2026_11_08/):
- Coordinates h = K - 2, s = p/tie, eps = 1 - load. R = 1 on three edges of the box (eps = 0, eps = 1, s = 0); the fourth
  edge (s = 1) is R_tie(eps), with one interior critical point, giving S2.
- dR/dp ~ P and dR/deps ~ -G, both quadratic in eps with positive leading coefficients. Res_eps(P, G) =
  -2hs(1+h)(1+hs)^2 F(h, s), and F >= 1 - 9707/131072 > 0 for h <= 1/4 (exact sum of the negative terms). So R has no
  interior critical point and the max is on the s = 1 edge.
- A plain "R rises in p" proof fails: dR/dp < 0 at small eps (R there <= 1.031). And "R rises in eps below eps1" fails at
  small s. The resultant sidesteps both. That is the reusable move: when two partials have explicit low-degree numerators,
  check their resultant's sign before trying monotonicity along paths.
- Consistency: F first vanishes near K = 4.85, the same K where the envelope max_eps R(p, eps) stopped being monotone in p.

Open: the branch formula itself (one SOAP ordering for all p below the tie; M-SERPT = Gittins above it) is checked to
8.9e-16 against soap.ratio at K = 2.05..6, not proved. Four-atom laws on (2, K*) are untested. The refined conjecture
sup R = max(S2(K), 2u/(1+u)) for K > 2 (u = sqrt(K-1)), and 1 for K <= 2, is in own_p0434/NOTE.md.

Related: [[a_finite_load_search_skipped_the_k_range_where_the_bound_fails_2026_11_08]],
[[p0434_heavy_traffic_reduces_to_a_staircase_hull_inequality_2026_11_08]],
[[p0434_heavy_traffic_upper_bound_passed_an_independent_read_2026_11_08]].


Update 8 Nov 11:0x: the branch lemma is now proved by hand (route item 26, the private repository main b82e3c22). The three rank
comparisons that fix the SOAP structure (M-SERPT's jump at age 1, Gittins' start 1/(1-p) against K-1, and which term of
Gittins' min is active) all switch at the same p = (K-2)/(K-1). Above it both policies are FCFS in mean, so R = 1; below it
the structure is fixed, so R(p, eps) is one rational function. The two-atom result now rests only on the SOAP mean formula
and on soapsym implementing it.

Update 8 Nov 05:2x: route item 27 (08c1b993) - a small third atom at any m in (1, K) stays below S2 (w = 1e-4, 13 pairs at K = 2.1, 2.2); the margin goes to 0 only as m -> K, so a three-atom proof should start there.
Update 8 Nov 05:3x: route item 28 (32c5ce28) - the three-atom branch ends where E X = e(1) (closed-form tie shift); the first-order slope of the sup in w is negative for all 24 (K, m) checked and ~ -0.28 (K - m) near the merge at K = 2.25.
Update 8 Nov 05:3x: route item 29 (8c6ebec5) - first-order three-atom lemma: for 2 < K <= 9/4 the slope of the sup in a small third atom is T = eps(eps-1)(m-K)Q/(positive), Q linear in m, and two end resultants against e2 show T < 0 on [1, K). Rests on one numerically matched branch rational.
