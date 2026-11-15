---
name: f0073_pinned_positive_2d_growing_box_ratio_to_gaussian_2026_11_14
description: "[PROVISIONAL] F0073 (Velenik 2006 OP6, 2d field pinned at 0, positive, convex V): does the mean next to the pin stay bounded (estimate A)? Open; growing-box numerics N=8..128: convex/Gaussian ratio 0.60-0.63, r=1 increments shrink ~0.8 per doubling"
metadata:
  type: project
  created: 2026-11-14
  created_at: 2026-11-14T11:21:58+02:00
  status: provisional
  evidence: ""
---

status: provisional. Folder 12_cognitive_architecture/math/trio_1011/op/F0073. The 12 Oct ATTEMPT.md already proves monotonicity in N, the c log|i| lower bound (Deuschel-Giacomin) and reduces existence to estimate A: sup_N E_N^+(phi_e) < infinity at a neighbour e; it corrected the intake attempt's reversed halves. Do not re-derive those. 14 Nov added pin2d.c (exact slice sampler, V = x^2/2 + a log cosh x) on Mac mini 1: a=0 (Gaussian) N=8..128, a=2 N=8..64 (N=128 pending in ~/f0073_20af/res_a2.txt). r=1 means: Gaussian 0.972 1.071 1.139 1.203 1.240; a=2 0.594 0.658 0.710 0.751. Ratio a2/a0 0.605-0.625 at every r, N; at r=1 it creeps 0.611->0.625. Even the Gaussian, whose limit is finite, still rises at fixed r with N, so these boxes cannot settle A or the uniform log upper bound. Route suggested: a comparison of MEANS under positivity (Brascamp-Lieb compares variances of the unconstrained field only). What would change this: a=2 N=128 r=1 ratio above 0.63, or a proof of a mean comparison. Related [[f0072_continuous_sos_entropic_repulsion_log_n_over_d_prediction_2026_11_14]].
