---
name: p0363_frozen_percolation_3regular_finite_graph_limit_open_list_entry_says_endogeny_wrongly_2026_11_13
description: "P0363 (Rath-Swart-Terpai arXiv 1910.09213, Problem 2: show Aldous' frozen percolation on the 3-regular tree is the local weak limit of frozen percolation on suitable finite graphs) is open on 13 Nov 2026. arXiv has no finite-graph or random-regular-graph result; the newest frozen-percolation paper (Rath-Szoke-Yeo 2610.37320, Oct 2026) is mean-field on K_n. The 200-list entry's 'endogeny of the tree model is known' is wrong: the source proves NONendogeny, which is why the finite-graph question is hard. Our only attempt (6 Sep codex_20h A001, partial): local lightning in a fixed ball vanishes, so all freezing in the limit must be transmitted from outside every ball"
metadata:
  node_type: memory
  status: provisional
  type: project
  modified: 2026-11-13T18:36:07.904Z
---

P0363, rank 56 on the 200 list. Source: Rath, Swart and Terpai, "Frozen percolation on the binary tree is
nonendogenous", arXiv 1910.09213 (Ann. Probab. 2021), Problem 2, PDF p.15. Aldous (2000) built frozen percolation on the
3-regular tree (an edge opens at its uniform activation time unless an endpoint is already in an infinite open cluster,
in which case it freezes). The problem: show this process is the local weak limit of frozen-percolation-type processes on
a suitable sequence of finite graphs. The list's caveat stands: the known growing-threshold approximation on the
infinite tree does not count.

Status 13 Nov 2026: open.
- Correction to the list entry: its "where it stands" says endogeny of the tree model is known. The source proves the
  opposite: the recursive tree process is nonendogenous (whether an edge freezes is not a function of the activation
  times). Rath, Swart and Szoke, arXiv 2103.14408, find a phase transition between endogeny and nonendogeny for a
  discretised-freezing variant on the marked binary branching tree. Nonendogeny means a finite-graph limit must carry
  extra randomness, which is what makes the question delicate.
- My arXiv check on 13 Nov ("frozen percolation" in all fields; with regular, local, random regular, forest fire, local
  weak; nonendogenous): nothing on finite graphs converging locally to the 3-regular tree model. Nearby, other models:
  - Rath, Szoke and Yeo, arXiv 2610.37320 (Oct 2026): window process of slightly subcritical mean-field frozen percolation
    on K_n, lightning rate lambda_n with (ln n)^{4/3} n^{-1/3} << lambda_n << 1; OU fluctuations and a tempered stable
    Levy limit for the increments.
  - Yeo, arXiv 1810.02750: mean-field frozen percolation on inhomogeneous random graphs, hydrodynamic limit through
    multitype branching processes.
  - Rath, arXiv 0812.2750 (mean-field frozen percolation); Crane 1809.03462 (Rath-Toth forest fire).
  - van den Berg, Kiss, Nolin 1105.1977 (binary tree, large finite clusters frozen) and the 2D work of van den Berg,
    Kiss, Nolin, Lam: finite-threshold versions, not finite graphs.
- There is no Codex report for P0363 in referee_reports/2026-11-13.
- Our earlier work: open-problems-repo probability_campaign_2026_09/codex_20h_20260906 P0363-A001 (7 Sep, partial,
  author-checked). On finite graphs with lightning rate lambda_n -> 0, a fixed ball B sees a strike by time t with chance
  at most |B| lambda_n t -> 0, so any freezing in the limit is transmitted from clusters leaving every fixed ball. The
  obstruction is quantitative control of mesoscopic cluster growth and transmitted freeze times.
- Where an attempt could start: mean-field frozen percolation on random 3-regular graphs, with lambda_n -> 0 and
  n lambda_n -> infinity. Show its local limit is a frozen percolation on the 3-regular tree. Then use the Rath-Swart-Terpai
  uniqueness or characterisation of the canonical law to identify which one. The Rath-Szoke-Yeo window process on K_n is
  the closest finite-graph SOC machinery.

Related: [[d0097_arw_z2_critical_density_small_lambda_solved_forien_gaudilliere_afg_2026_11_13]] (previous item in this
loop).
