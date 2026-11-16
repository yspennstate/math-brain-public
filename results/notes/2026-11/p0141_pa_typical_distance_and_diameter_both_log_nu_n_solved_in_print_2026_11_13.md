---
name: p0141_pa_typical_distance_and_diameter_both_log_nu_n_solved_in_print_2026_11_13
description: "P0141 (van der Hofstad Saint-Flour 2017 OP 2.3, distance constants in PA with m>=2, delta>0) is solved in print 2025 - typical distance AND diameter are both (1+o(1)) log_nu n with explicit nu, so a = b; our list's \"a<b\" target is wrong"
metadata:
  node_type: memory
  status: provisional
  type: project
  modified: 2026-11-13T14:17:07.969Z
---

P0141, rank 20 on the 200 list: "for affine preferential attachment with m>=2 and delta>0, prove typical distance/log n and
diameter/log n converge to explicit constants a<b". Source: van der Hofstad, Saint-Flour 2017 notes, Open Problem 2.3.

Status: SOLVED IN PRINT (arXiv 2025), and the answer is a = b, not a < b.
- van der Hofstad and Zhu, "Logarithmic typical distances in preferential attachment models", arXiv 2502.07961
  (submitted to AAP). Theorem 1.2: for m>=2, delta>0 and uniform o1, o2, dist(o1,o2)/log_nu n -> 1 in probability, with
  nu = 2( m(m+delta) + sqrt(m(m-1)(m+delta)(m+1+delta)) ) / delta > 1.
  nu is the spectral radius of the offspring operator of the Polya point tree, i.e. 1/pi_c from Hazra, van der Hofstad
  and Ray, arXiv 2312.14085 (same closed form).
- Du, Gong, Li and Zhu, "Asymptotic diameter of preferential attachment model", arXiv 2504.21741: the diameter is
  (1+o(1)) log_nu n whp for m>=2, delta>0, confirming the VZ25 conjecture.
So a = b = 1/log nu. That is the configuration-model picture: minimum degree m >= 2 leaves no long dangling paths, so the
diameter carries no extra term beyond the typical distance.

Sanity values (computed 13 Nov): m=2, delta=1: nu = 21.80, 1/log nu = 0.3245; m=2, delta=10: 8.33; m=3, delta=1: 45.91;
delta -> infinity: nu -> 2(m + sqrt(m(m-1))) (6.83 for m=2), finite as it should be.

What is left: second-order terms (fluctuations of dist - log_nu n, an additive diameter correction), and m=1 is a tree
with different behaviour. The 200-list statement "explicit positive constants a<b" should be corrected to a = b. Our only
prior work was the 6 Sep codex_20h first pass (P0141-A001, weak ordering a <= b only), and that pass was right not to
claim strictness. Same failure as [[an_open_problem_corpus_inherits_its_sources_dates_2026_09_14]]: a 2017 source,
resolved in 2025.

Related: [[c0068_torus_giant_above_window_slow_eps_solved_brn_2025_general_open_2026_11_13]] (another 200-list item checked the same day).
Would change this: a referee finding a gap in 2504.21741 (it is an arXiv preprint; not checked line by line here).
