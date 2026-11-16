---
name: t319_secant_width_grows_sqrt_depth_2026_11_01
description: [PROVISIONAL] T319: random expansive ReLU net secant Gaussian width grows like sqrt(d) (width^2 ~ 0.87 k d, k=4, d<=6); earlier plateau was a sample artifact
metadata:
  type: project
  created: 2026-11-01
  created_at: 2026-11-01T00:40:18+04:00
  status: superseded
  superseded_by: t319_fixed_width_depth_growth_stops_2026_11_01
  evidence: ""
---



T319 (1 Nov, an agent), pushed a57d67c to research-repo (research_pushes/2026-11-01-loop-T319-secant-width), card claim_80a47a49a7f34523a1f19b90954bcd36.

Lower estimates at k=4 with 24 draws: 1.965, 3.298, 3.766, 4.114, 4.551 at d = 1, 3, 4, 5, 6. The d=1 control is E chi_4 = 1.88. width^2/d is 3.4-3.9. So O(sqrt k) uniformly in depth fails on this family. Depth and log n are confounded because n = 2^d k.

Trap worth remembering: a sup estimated over a sample of directions plateaus once the number of linear pieces met approaches the sample size. Check that the estimate does not move when the sample is quadrupled before calling it flat. Here the first pass looked flat at d=4-6, and that was the artifact.

Related: [[t324_two_cluster_merger_tracking_w3_2026_11_01]], [[t254_collapse_rate_identity_2026_11_01]].

Superseded the same day by [[t319_fixed_width_depth_growth_stops_2026_11_01]]: at fixed layer width the growth stops by d = 4, so the sqrt(d) reading does not hold as a depth effect.
