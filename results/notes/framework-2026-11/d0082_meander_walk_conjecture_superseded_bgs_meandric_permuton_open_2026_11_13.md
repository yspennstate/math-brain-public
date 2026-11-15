---
name: d0082_meander_walk_conjecture_superseded_bgs_meandric_permuton_open_2026_11_13
description: "D0082 (Gwynne-Holden-Sun mating-of-trees survey Problem 6.3: the meander lattice walk converges to a correlated 2D Brownian motion, correlation -cos(pi gamma^2/4)) is superseded by its own source's UPDATE: the uniform meander is expected to converge to gamma-LQG with c=-4, gamma = sqrt((17 - sqrt 145)/3) ~ 1.2856, decorated by two INDEPENDENT SLE_8 (Borga-Gwynne-Sun arXiv 2207.02319, meandric permuton conjecture). That replacement is open on 13 Nov 2026, as is the Di Francesco-Golinelli-Guitter meander exponent alpha = (29 + sqrt 145)/12. Nearby: Borga-Gwynne 2409.15494 (the permuton determines the LQG surface and curves), Wei 2610.03730 (numerics on meandric systems)"
metadata:
  node_type: memory
  status: provisional
  type: project
  originSessionId: agent-66b6-4575-b3c4-a8807fd17369
  modified: 2026-11-13T16:29:41.507Z
---

D0082, rank 42 on the 200 list. Source: Gwynne, Holden and Sun, "Mating of trees for random planar maps and Liouville
quantum gravity: a survey", arXiv 1910.04713, Problem 6.3 (PDF p.55). As stated, it asks to prove that a lattice walk
encoding meanders converges to a 2D Brownian motion with correlation -cos(pi gamma^2/4). Via a Gwynne-Sun-type argument,
that would give the exponent alpha in the enumeration of meanders.

Status 13 Nov 2026: the stated conjecture is withdrawn by its source, and its replacement is open.
- The survey's own UPDATE says the uniform meander should instead converge to LQG with central charge c = -4, decorated
  by two independent SLE_8 curves. Here kappa = 8 differs from 16/gamma^2, so mating of trees does not apply directly and
  the Brownian-walk statement is not expected to hold as written.
- The replacement is Borga, Gwynne and Sun, "Permutons, meanders, and SLE-decorated Liouville quantum gravity", arXiv
  2207.02319. It conjectures that uniform meandric permutations converge to the meandric permuton: two independent
  SLE_8 on gamma-LQG with gamma = sqrt((17 - sqrt 145)/3). Rechecked 13 Nov: sqrt 145 = 12.0416, so gamma^2 = 1.6528 and
  gamma = 1.2856, matching our 8 Sep first pass D0082-A001 (c = -4 gives Q = sqrt(29/6)). The meander exponent
  alpha = (29 + sqrt 145)/12, about 3.42 (Di Francesco-Golinelli-Guitter 2000), is still a conjecture.
- My arXiv check on 13 Nov: meander with Liouville, exponent, mating of trees, and "meandric" in math.PR. Nothing proves
  the meander scaling limit or the exponent. Nearby work:
  - Borga and Gwynne, arXiv 2409.15494 (Sep 2024): the meandric permuton, if it is the limit, uniquely determines the
    LQG surface and the two SLE_8 curves up to symmetries. This is a reconstruction result, not a convergence result.
  - David Wei, arXiv 2610.03730 (Sep 2026): numerics on uniform meandric systems, a different model (many loops) read as
    percolation on planar maps. It gives conjectures on box crossings and a law-preserving flip dynamics.
  - Duplantier and Guitter, arXiv 2507.12203 (Jul 2025): LQG duality relations for block-weighted maps, meandric
    systems included. These are physics-level enumerative relations.
  - Borga, Gwynne and Wang, arXiv 2609.22514 (Sep 2026): directed distances in the sqrt 2-LQG class. Not meanders.
- What A001 recorded as the wall still stands: the meander walk pairs two independent arch systems nonlocally, and no
  invariance principle for that pairing is known. A001's "correlation 0 under the corrected picture" is a heuristic and
  was not checked against BGS.
- There is no Codex report for D0082. If the item is worked again, the target is the BGS meandric permuton conjecture,
  not the survey's walk statement.

Related: [[e0031_euclidean_matching_fluctuation_lower_bound_open_feng_upper_2026_11_13]] (previous item in this loop).
