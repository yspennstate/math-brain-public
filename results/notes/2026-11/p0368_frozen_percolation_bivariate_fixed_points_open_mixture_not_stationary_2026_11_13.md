---
name: p0368_frozen_percolation_bivariate_fixed_points_open_mixture_not_stationary_2026_11_13
description: "P0368 (Rath-Swart-Terpai arXiv 1910.09213, Problem 7: classify every fixed point and domain of attraction of d mu_h/dh = T2(mu_h) - mu_h, the bivariate evolution for frozen percolation on the oriented binary tree) is open on 13 Nov 2026. Only the two scale-invariant fixed points (diagonal and the nonendogeny witness) are known; arXiv has nothing since. Ours (7 Sep codex_20h A001, partial, exact identity): a convex mixture of the two known fixed points is NOT stationary, its derivative along the mixture line is 2p(1-p)(C - (nu_diag+nu_min)/2), so an apparent line of equilibria in a plot is spurious"
metadata:
  node_type: memory
  status: provisional
  type: project
  modified: 2026-11-13T18:43:22.228Z
---

P0368, rank 57 on the 200 list. Source: Rath, Swart and Terpai, "Frozen percolation on the binary tree is
nonendogenous", arXiv 1910.09213 (Ann. Probab. 2021), Problem 7, PDF p.16. In the source, nonendogeny is proved by
studying the bivariate (pair-coupling) version of the recursive distributional equation. A law mu_h on pairs evolves by
d mu_h/dh = T2(mu_h) - mu_h, where T2 is the two-child bivariate map. The two scale-invariant fixed points are known: the
diagonal coupling, and the off-diagonal one whose existence witnesses nonendogeny. Problem 7 asks for all fixed points,
nonscale-invariant ones included, and the domain of attraction of each.

Status 13 Nov 2026: open.
- My arXiv check on 13 Nov: "recursive tree process" with endogeny; Swart as author with recursive tree; "bivariate
  uniqueness"; Szoke as author with percolation. Nothing on this classification. Background only:
  - Mach, Sturm and Swart, arXiv 1801.05253 (a new characterization of endogeny via the n-variate map) and 1812.10787
    (RTPs as mean-field limits of stochastic flows). These are the general framework for T2 and its fixed points.
  - Bandyopadhyay, math/0511203 and math/0407175 (bivariate uniqueness and tail triviality).
  - Rath, Swart and Szoke, arXiv 2103.14408: the theta^n discretised-freezing variant has an endogeny threshold theta*.
    It is a different model, but the nearest result on the fixed-point structure.
  - Rath, Szoke and Yeo, arXiv 2610.37320 (Oct 2026): mean-field frozen percolation on K_n, not this equation.
- There is no Codex report for P0368 in referee_reports/2026-11-13.
- Our earlier work:
  - open-problems-repo probability_campaign_2026_09/codex_20h_20260906 P0368-A001 (7 Sep, partial, author-checked, an
    exact signed-measure identity, not a simulation). Start at the mixture p nu_diag + (1-p) nu_min of the two known
    fixed points. T2 has a cross term of weight 2p(1-p), so the derivative along the mixture line is
    2p(1-p)(C - (nu_diag + nu_min)/2). Mixtures are not stationary; an interpolation plot can show a false line of
    equilibria.
  - proofnet24/NM13-08 (18-19 Sep) screened P0368 repeatedly and kept it "HARD-shaped". No result.
- The source suggests time-split couplings, which share the lightning up to a fixed time and are independent after it.
  The missing step: an invariant family containing those couplings, or a Lyapunov function giving a basin decomposition.

Related: [[p0363_frozen_percolation_3regular_finite_graph_limit_open_list_entry_says_endogeny_wrongly_2026_11_13]] (same
source, previous item in this loop).
