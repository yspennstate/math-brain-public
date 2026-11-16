---
name: t030_lambda2_high_sharp_corners_extrema_hold_2026_11_03
description: [VERIFIED] T030 review: quad survey's hot-spot findings hold on 39 reruns (73/78 extrema at corners, 0 interior), but lambda2 runs high at sharp corners; row 202 needle 0.562 vs 0.462 (1D limit agrees)
metadata:
  type: project
  created: 2026-11-03
  created_at: 2026-11-03T04:18:43+04:00
  status: provisional
  evidence: "06_math_research/frontier/rows/T030/reviews_agent/REVIEW_T030_QUAD_SURVEY.md"
---

T030 review, 3 Nov 04:17 (an agent), of an agent's 2 Nov survey of 400 convex quadrilaterals
(hot spots). A second P1 solver on an unstructured Delaunay mesh, run on the same vertices for 39 shapes, agrees
on every qualitative point: both extrema of u2 on the boundary in 39 of 39, 73 of 78 exactly at a corner, no
interior node a strict local extremum, separations within 0.005 (the 0.8041 aspect-1 miss is real).

What it caught: the survey's structured bilinear grid overestimates lambda2 on sharp-cornered shapes, which are 115
of the 400 (corner under 15 degrees). The error is 0.05-2.5% on most of them. Row 202 is a 0.11-degree needle
(area 0.032, diameter 5.67): it reads 0.56173 with lambda3/lambda2 392.8, against 0.46245 and 3.35 from both my 2D
mesh (n 150/300/600) and the 1D thin-domain limit -(w u')' = lambda w u.

Reusable checks:
- Two conforming solvers both give upper bounds on Neumann eigenvalues, so the lower converged one is closer.
- Any needle shape has a 1D limit whose error is about (width/length)^2. Use it.
- A lambda3/lambda2 far above about 4 on a thin shape is a solver artefact.
- A margin that shrinks 4x per mesh doubling is what a corner extremum gives, because grad u = 0 at a convex
  Neumann corner. It is not evidence against an interior extremum near the boundary. Count interior local extrema
  instead.

Files: 06_math_research/frontier/rows/T030/reviews_agent/ on the private repository main, and a move appended to
T030/moves.jsonl.


Related: [[t030_hot_spots_400_convex_quads_extrema_on_boundary_2026_11_02]] - the survey this review checks; its lambda2 values for sharp-cornered shapes need this correction.
