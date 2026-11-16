---
name: t226f_depth_four_edge_window_limit_0_fifteen_branches_2026_11_08
description: "Depth four edge window limit 0? Yes (8 Nov, T226f): 15 branches, beta 4353823/4404960<99/100, H9 cert; my check clean, LP witnesses unchecked"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T12:15:44+04:00
  status: verified
  evidence: "frontier T226 e3166b7c5d; claim_d2775bb8; t226f_check.py"
---

Does the depth-three edge-of-stability result (T226e) hold at depth four? Yes, as a limit (8 Nov, OPEN-T226f, worker-proved, reviewed by an agent, not refereed). For GD on (u1 u2 u3 u4 - 1)^2/2 with Gaussian init of sd eta^(-1/6), P(converge with |lambda - 2/eta| <= C) -> 0 for every fixed C.

What changed from depth three: 15 inverse branches instead of 7, det DT_0 = 1-e1-3e2-5e3-7e4, a degree-nine nonnegative-coefficient certificate for q<4 invariance (degrees 7 and 8 fail: 8 and 4 negative coefficients), and the reciprocal weighted Jacobians sum to 4353823/4404960 < 99/100 (depth three had 23/24). The old branch table does not carry over. That is the real work at each new depth.

My check (scratch t226f_check.py, pushed with the row as review_check_agent.py): all symbolic identities, H9 rebuilt (630 terms, 0 negative), beta summed exactly, 20,000 seeded targets with all fifteen preimages solved, 0 branch-bound violations (tightest: branch 1, 3.0226 vs 3; branch 134, 99.07 vs 96), max inverse sum 0.584. Not checked by me: the 13 LP witness polynomials and the two 35-interval covers.

Still open: any rate in eta, general depth (2^L - 1 branches, needs a uniform Jacobian bound), nonlinear networks. Frontier row T226 pushed e3166b7c5d; math card claim_d2775bb8d66242458a0b3fd2bebf2b3e. Builds on [[t226e_depth_three_edge_window_probability_tends_to_0_null_survivors_2026_11_08]].

