---
name: t238_quadratic_student_is_matrix_sensing_lazy_edge_c_0p3_2026_11_01
description: [PROVISIONAL] T238: quadratic student with +- pairs is exactly PSD-difference matrix sensing from cI; window fixed in c = alpha/d over d = 8..32 (centre ~1e-2, lazy by 0.1-0.3)
metadata:
  type: project
  created: 2026-10-31
  created_at: 2026-10-31T23:12:54+04:00
  status: provisional
  evidence: ""
---

T238 (lazy-rich window). Quadratic activation student, +- pairs, m -> inf: each w_j obeys w' = -/+ G w with G = (1/n) sum r_i x_i x_i^T, so the predictor is x^T(P - Q)x with P' = -(GP+PG), Q' = +(GQ+QG), P0 = Q0 = cI, c ~ alpha/d. Lazy limit = minimum-Frobenius interpolant; commuting case is the spectral hypentropy bias (matrix Woodworth 2002.09277). Numerics n = d^2/4, rank-one teacher: distance to lazy < 3% of max at c = 0.3 for d = 8, 12, 16; a first one-seed pass read a rich end moving down with d (0.92/0.78-0.95/0.71 at c = 1e-3); a second pass with two seeds per d up to d = 32 (2026-10-31 23:2x) shows seed spread as large as any trend, so over d = 8..32 the window is fixed in c: centre ~1e-2, lazy by 0.1-0.3, rich by 1e-3 (correction move on the row). The lazy interpolant bulk eigenvalues stay at 0.06-0.12, so no shrinking bulk scale sets it. One-seed d-trends here were noise, as in [[overlapping_windows_inflate_significance_2026_08_07]]. Note research_pushes/2026-11-01-t238-quadratic-window, move 32a96d00. Same multiplicative-flow structure as [[t259_quadratic_mean_field_needs_cavity_tilt_shape_changes_at_p_d2_2026_11_01]] (quadratic nets reduce to matrix problems).
