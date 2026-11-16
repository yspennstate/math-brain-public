---
name: monotone_fei_per_coordinate_ratio_stays_near_0_7_at_small_influence_2026_11_08
description: "FEI T021 8 Nov 03:4x: monotone DNF climbs reach R_i/(I ln 1/I) = 0.788 at I=3/128, 0.713 at 1/128, 0.706 at 7/2048; symmetric thresholds fall to 0.25 by n=401. Monotone lim sup still open in [0.396,1]."
metadata:
  node_type: memory
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T03:49:10-05:00
  status: superseded
  superseded_by: monotone_fei_per_coordinate_constant_is_also_1_2026_11_08
  evidence: climb_mono_summary.out in the private brain repository: 06_math_research/frontier/T021/fei4_agent_2026_11_08; 3/128 point rechecked by direct Fourier sums
  modified: 2026-11-08T09:05:46.387Z
---

Search over arbitrary monotone DNFs (climb_mono.py, read count and width unrestricted, only coordinates with I_i under a cap scored) at n = 10..13. Best points:
- 0.7879 at I = 3/128 (8 variables; the same function found at n = 10 and at n = 12; rechecked by direct Fourier sums to 1e-12)
- 0.7758 at I = 7/128
- 0.7127 at I = 1/128
- 0.7061 at I = 7/2048

Symmetric thresholds, computed exactly by levels up to n = 401 (sym_threshold.py), are much worse: the best is 0.391 at n = 41 and 0.252 at n = 401.

These are single functions at a fixed I, so they bound nothing about the limit. They do show the monotone ratio does not fall toward the G(c,1) value 0.396 as I shrinks to about 0.003. The next question is whether the 8-variable optimum extends to a family.

Over all Boolean f the constant is 1: [[per_coordinate_fei_bound_is_sharp_2026_11_08]]. The upper bound: [[per_coordinate_fei_cost_is_at_most_i_ln_e_over_i_for_every_boolean_f_2026_11_08]].
