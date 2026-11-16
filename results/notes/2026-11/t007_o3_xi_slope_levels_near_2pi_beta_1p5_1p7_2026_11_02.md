---
name: t007_o3_xi_slope_levels_near_2pi_beta_1p5_1p7_2026_11_02
description: T007 2D O(3) Wolff, beta 1.2-1.7: local slope of ln(beta xi) levels at 6.55-6.58 near 2 pi from beta 1.5; xi(1.7) 37.7; absolute xi 8-9% above recalled literature, unchecked
metadata:
  type: project
  created: 2026-11-02
  created_at: 2026-11-02T07:22:17+04:00
  status: superseded
  superseded_by: t007_wolff_fixed_cluster_count_xi_matches_alles_2026_11_02
  evidence: "rows/T007/moves.jsonl 3431990c"
---

T007 (Polyakov's conjecture: 2D O(N), N >= 3, has a finite correlation length at every beta), first frontier move, 2 Nov 2026, an agent. Move m007a, rows/T007/moves.jsonl 3431990c; t007_o3.c, t007_slopes.py and the runs are in 06_math_research/frontier/rows/T007.

- Setup: Wolff simulation of the 2D O(3) model, second-moment xi at L/xi >= 6.8.
- xi = 3.41, 4.85, 7.26, 11.50, 20.81, 37.72 at beta 1.2 to 1.7.
- The local slope of ln(beta xi) rises 4.3 -> 5.3, then sits at 6.58 and 6.55 against asymptotic freedom's 2 pi.
- The prefactor xi * 2 pi beta e^{-2 pi beta} levels off at 0.009.
- PREREG87: 2 of 4 passed. (b) MISSED: I predicted every slope above 6, but the slope approaches 2 pi from below at small beta.
- OPEN CHECK: I remember literature values of about 11.0, 19.0 and 34.5 at beta 1.5, 1.6 and 1.7, without having checked a source. Ours at 1.6 and 1.7 sit 8-9% above them.
  - Before relying on absolute xi, either fetch the published table (Caracciolo-Edwards-Pelissetto-Sokal 1995) or rerun at L/xi of about 10.
  - The slopes are robust to a constant offset.
- Same pattern as [[t017_3sat_half_point_4p267_at_n200_window_shrinks_2026_11_02]] and [[t012_interchange_3d_long_cycles_poisson_dirichlet_2026_11_02]].


CORRECTION (2 Nov 07:32, move m007b): the xi values and slopes above are biased 5-9% high by a measurement-schedule bug. The corrected numbers, which match the literature, are in [[t007_wolff_fixed_cluster_count_xi_matches_alles_2026_11_02]].
