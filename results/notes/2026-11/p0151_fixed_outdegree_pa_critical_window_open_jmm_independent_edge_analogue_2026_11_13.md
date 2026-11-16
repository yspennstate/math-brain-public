---
name: p0151_fixed_outdegree_pa_critical_window_open_jmm_independent_edge_analogue_2026_11_13
description: "P0151 (vdH Saint-Flour 2017 OP 4.4, percolation window for fixed-outdegree PA, m>=2, delta>0) is still open per vdH's Dec 2025 survey; threshold known (HvdHR 2312.14085), and the independent-edge analogue (Jorritsma-Maillard-Morters 2512.18937) gives the predicted answer - window (log n)^-2, largest component sqrt(n)/log n"
metadata:
  node_type: memory
  status: provisional
  type: project
  modified: 2026-11-13T14:20:54.367Z
---

P0151, rank 22 on the 200 list: for affine PA with a fixed m>=2 edges per new vertex and delta>0, identify the
percolation scaling window and the largest critical component sizes. Source: van der Hofstad, Saint-Flour 2017, Open Problem 4.4.

Status: OPEN (checked 13 Nov 2026).
- Threshold known: Hazra, van der Hofstad, Ray, arXiv 2312.14085: pi_c = delta / (2(m(m+delta) + sqrt(m(m-1)(m+delta)(m+1+delta)))),
  the inverse spectral radius of the Polya point tree's offspring operator (the same nu as P0141's distance constant).
- Window for the INDEPENDENT-edge class: Jorritsma, Maillard, Morters, "The critical percolation window in growing random
  graphs", arXiv 2512.18937 (Dec 2025). Vertices connect independently to earlier v with probability ~ a power of v's arrival
  time; includes inhomogeneous random graphs of PA type. When the threshold is positive: window width (log n)^{-2}, largest
  component of order sqrt(n)/log n, finite susceptibility independent of the position in the window, and a secondary
  transition at the window's upper edge. Proof: explorations coupled to branching random walks killed outside an interval of
  length log n.
- Fixed out-degree still open: van der Hofstad, "Percolation on random graphs", arXiv 2512.15673 (Dec 2025 SIAM survey)
  says the subcritical results "can be expected" to extend to PA "with major technical adjustments" and that this "is
  ongoing"; the infinite-order (barely supercritical) transition is known for the m-out graph (Riordan) "but not yet for
  preferential attachment models with fixed out-degrees".
- Infinite variance (delta<0, tau in (2,3)), a different regime: Morters and Schatze, arXiv 2606.27844, moving window
  p_c ~ beta n^{(tau-3)/(2tau-2)} for the PA-type inhomogeneous graph.

Conjectured answer to aim at: the JMM exponents, (log n)^{-2} and sqrt(n)/log n. The difficulty is the dependence among each
vertex's m edges (Polya urn representation) breaking the independent killed-BRW coupling. Prior work: 6 Sep first pass
(P0151-A001) and HARD7-04 on 18 Sep (PARTIAL, a quadratic gain law, no closure).

Related: [[p0141_pa_typical_distance_and_diameter_both_log_nu_n_solved_in_print_2026_11_13]] (same nu, same day).
