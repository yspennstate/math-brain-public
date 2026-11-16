---
name: p0010_biased_random_orientations_z2_infinite_path_open_dp_comparison_only_2026_11_13
description: "P0010 (Grimmett, Selected problems in probability theory, arXiv 2205.07318, Question 5.1: in the biased random orientation of Z^2, does every bias p != 1/2 give positive probability of an infinite directed path from the origin?) is open on 13 Nov 2026; arXiv has nothing new (the 2026 randomly-oriented-lattice papers are about random walks on Manhattan lattices). Known: p = 1/2 has no such path (Grimmett 2000), and p above the north-east directed-percolation threshold (or its reflection) has one by subgraph comparison. Our 6 Sep codex_20h A001 gives only the symmetry p <-> 1-p and that comparison; the window (1/2, p_c^dir) is the open part"
metadata:
  node_type: memory
  status: provisional
  type: project
  modified: 2026-11-13T18:48:37.552Z
---

P0010, rank 58 on the 200 list. Source: Geoffrey Grimmett, "Selected problems in probability theory", arXiv
2205.07318, Question 5.1, PDF p.9. Orient each edge of Z^2 at random with a bias p, independently: horizontal edges point
east with probability p, vertical edges north with probability p (the source fixes the exact convention). Is there,
for every p != 1/2, positive probability of an infinite directed path from the origin?

Status 13 Nov 2026: open.
- Known: at p = 1/2 there is a.s. no infinite directed path from the origin (Grimmett, "Infinite paths in randomly
  oriented lattices", Random Structures Algorithms 2001; cited in the source). The north-east edges form oriented
  percolation with parameter p, so p > p_c of oriented site/bond percolation gives an infinite path, and by reflection so
  does p < 1 - p_c. The question is the window between 1/2 and the oriented threshold, where monotonicity in p is not
  obvious because paths may use edges against the bias.
- My arXiv check on 13 Nov: "randomly oriented" with lattice, in the title, "random orientation" with infinite path,
  oriented percolation with random orientations. Nothing on this question. The 2026 hits concern random walk on the
  randomly oriented Manhattan lattice (Bou-Rabee and Peres 2609.07621, transient in 2D; Nguyen 2608.21701, 3D
  superdiffusive), another model. Older and near: Zhelezov 1205.5873 (a property of random-oriented percolation in a
  quadrant), before the source.
- There is no Codex report for P0010 in referee_reports/2026-11-13.
- Our earlier work: open-problems-repo probability_campaign_2026_09/codex_20h_20260906 P0010-A001 (6 Sep, limited
  argument): the p <-> 1-p symmetry and the oriented-percolation subgraph comparison. Nothing inside the window.
- Where an attempt could start: show theta(p) > 0 just above 1/2 via an essential enhancement over the p = 1/2 model
  (Aizenman-Grimmett style). The difficulty: p = 1/2 is itself subcritical-like for the origin's forward set, not
  critical in a standard monotone family, and the forward set is not increasing in the orientation bias.

Related: [[p0368_frozen_percolation_bivariate_fixed_points_open_mixture_not_stationary_2026_11_13]] (previous item in this
loop).
