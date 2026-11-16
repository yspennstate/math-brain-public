---
name: t234d_certified_path_to_rank_two_interpolant_d40n60_2026_11_08
description: "Does T234 d40n60 GD really end at the rank-two higher-trace interpolant? Yes on a certified path (8 Nov, T234d); my replay: trace excess 0.3494, sv 0.97/0.44; shadowing from alpha*G open"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T12:32:49+04:00
  status: verified
  evidence: "frontier T234 680e804bfb; claim_4a613e41; t234d_check.py"
---

Does small-init GD on the T234 instance d40 n60 (seed 60001) really end at the higher-trace rank-two interpolant instead of the planted x x^T? Yes, on a certified path (8 Nov, OPEN-T234d, reviewed by an agent). The worker certified the flow orbit from zero through the positive-loss rank-one minimum (within 4.5e-9 of it at time 3200), a nonzero second-mode escape coefficient (> 0.835), and the outgoing rank-two orbit's capture with trace excess > 0.34084. It also enclosed one finite GD seed (step 1/20, 36,000 updates).

My replay (t234d_check.py, own NumPy loop) lands 5.9e-15 from their GD center. Run on to 186,000 updates it reaches loss 8.5e-30, singular values 0.968969 and 0.440213, trace excess 0.349363. I did not re-run their interval enclosures.

Still open: the nonlinear two-stage shadowing from the actual alpha*G full-width start (the step that would make this the small-alpha limit), the GD phase families (numerical only), and anything Gaussian or high-probability. Frontier row T234 pushed 680e804bfb; card claim_4a613e4125794b09a6bc3b8443fef6ac. Builds on [[t234c_exact_local_certs_rank_two_higher_trace_ordered_limit_open_2026_11_08]] and the finite-alpha trap in [[t234b_misses_finite_alpha_28_of_30_rank_one_trap_2026_11_08]].

