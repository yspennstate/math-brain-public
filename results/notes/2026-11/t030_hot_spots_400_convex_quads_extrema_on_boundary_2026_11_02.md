---
name: t030_hot_spots_400_convex_quads_extrema_on_boundary_2026_11_02
description: T030 hot spots: P1 FEM Neumann on 400 random convex quadrilaterals (aspects 1-8): u2 extrema on boundary in 400/400, margins positive and shrinking ~h^2 under refinement; hot/cold separation >= 0.935 diam for aspect >= 2, 0.804 on near-squares; PREREG97 4/5
metadata:
  type: project
  created: 2026-11-02
  created_at: 2026-11-02T08:22:07+04:00
  status: provisional
  evidence: "rows/T030/moves.jsonl 4dea9c1a"
---

T030 (hot spots, convex planar domains), first frontier move, 2 Nov 2026, an agent. m030a is in rows/T030/moves.jsonl (4dea9c1a); the code is t030_hs.py and t030_refine.py in 06_math_research/frontier/rows/T030.

- Setup: P1 FEM Neumann, checked on a 2x1 rectangle (lambda2 error O(h^2), 3.2e-5 at N 80).
- In 400 random convex quadrilaterals (aspects 1/2/4/8, nonsmooth, usually no symmetry axis), the max and min of u2 are on the boundary in all 400, and lambda2 is always simple.
- The 10 smallest margins stay positive at N 120 and 180, shrinking like h^2: the signature of a boundary extremum.
- The hot and cold spots are at least 0.935 diam apart at aspects 2-8 but only 0.804 apart on near-squares (PREREG97 (c) MISS; 4/5 overall).
- METHOD NOTE: a node-based strictness margin goes to 0 like h^2 for a true boundary extremum, so a tiny margin is not a warning sign. Judge from its trend under refinement.
- eigsh's sign is arbitrary, so the max and min labels swap between meshes; compare them as a pair.
- Interior critical points were not searched.
- Related: [[t028_ising_interface_rough_k0p30_to_0p40_smooth_0p45_2026_11_02]].

