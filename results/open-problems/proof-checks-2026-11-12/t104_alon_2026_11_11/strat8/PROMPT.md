You are working on one case of a graph inequality. Work in this folder only and write as you go: keep LOG.md current
after every step, and put the final write-up in RESULT.md. Label every statement PROVED (with an exact certificate and a
replay script), NUMERICAL (floating point evidence) or OPEN. Never present a numerical finding as a proof.

READ FIRST (read-only, do not modify): ~/agent_run/STRAT6/
- RESULT.md: the latest n = 5, D = 2 result. It proves the radial reduction (R1): on a fixed frame (u, w) and ratio r,
  T(a, ar) = a(1 - a/a_end)L(r) + (a/a_end)^2 T(a_end, r a_end), so T >= 0 on a ray iff T >= 0 at its far end a_end.
  It proves T >= 0 for a <= 103/200 (176 rational cells), for equal gaps up to G ~ 0.551713, and on 47 rational boxes of the
  zero-weight face (zero_face.py, zero_face_boxes.json, the 6-coordinate chart (t, v1, z1, v2, z2, z)). Its section
  "What remains" states the residual region exactly. Its scripts and JSON files are the tools to build on.
- ~/agent_run/STRAT7/terms.py: a numerical reference for T (function terms(W)); use it to test, never as a proof.
Copied here: far_end_frames.json - numerical least-T frames found by a GPU search near the far end, one per ratio r
(34 ratios), each with the frame u (5x2), the weights, the smallest weight (at a 1e-6 floor: these are on the zero-weight
face), T and q. The least values are q ~ 0.032 at r ~ 0.791 and ~0.037-0.05 for r in 0.72-0.83. These are the hard spots.

THE QUANTITY (as in STRAT6): n = 5, u, w orthonormal in the zero-sum subspace, b = ar with 0 < r <= 1,
lambda = (2 + a + b)/4, edge weights omega_ij = lambda/5 + a u_i u_j + b w_i w_j, and T = X1 + X2 + X3 - 2 S5 with the
definitions in STRAT6/RESULT.md.

TASK
Prove T >= 0 on the residual region of STRAT6: connected far endpoints with at least one zero weight, 3/25 < r <= 1,
a_end between the proved ceilings and 2/(3 - r). By (R1) it suffices to prove it on the zero-weight face itself.
Suggested routes, in order:
1. Reproduce the face polynomial (F2)/Cface from STRAT6 and evaluate it at the 34 frames in far_end_frames.json to see how
   much room there is (q ~ 0.03 is small but positive).
2. Cover the whole face (all charts: choose the zero edge as {4,5}, the symmetries in STRAT6) by rational boxes with exact
   interval or Bernstein bounds, refining adaptively near the hard spots. Record every box; a replay script must recheck
   all of them in exact rational arithmetic. Prove that the boxes cover the face (state the domain of each chart variable
   with a proof of its bounds).
3. If a full cover is too large, prove as much of the face as possible and state the remaining set exactly.
4. Faces with two or more zero weights are lower-dimensional; treat them as boundary cases of the same cover or separately.
Keep memory under 4 GB and use at most 4 processes. No network and no language-model workers. Write only in this folder.
