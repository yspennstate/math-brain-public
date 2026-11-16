---
name: t371_convex_route_fails_full_box_holds_half_scale_2026_11_01
description: [PROVISIONAL] T371 below threshold: flat concavity of the soft value in z fails on the full tanh logit box (top eig +0.23 at tau 0.1) but holds on max|z|<0.5 at tau 0.1 (sampled), so half-scale features give a uniform-in-time bound at every sigma, constant exp(2G/sigma^2)
metadata:
  type: project
  created: 2026-11-01
  created_at: 2026-11-01T14:01:03+04:00
  status: superseded
  superseded_by: t371_concave_cube_radius_0p42_to_0p45_not_half_2026_11_01
  evidence: ""
  modified: 2026-11-01T10:11:23.746Z
---



Measured 1 Nov on the two-state MDP of t371_particles.py: 9^4 grid plus 4,000 random points, Hessian by differences of the exact gradient. Positive top eigenvalue at 2,676 / 4,860 / 6,362 of 10,561 points for tau 0.1 / 0.03 / 0.01; smallest max|z| with one 0.50 / 0.25 / 0.25 (grid step 0.25). Route: mean-field Langevin uniform PoC under flat convexity + uniform LSI (Chen-Ren-Wang 2022, Suzuki-Wu-Nitanda 2023), Holley-Stroock gives exp(4cG/sigma^2). Pushed a66d0c0 (research_pushes/2026-11-01-loop-T371-concave), frontier move 2f7ab806. Not proved: concavity on the half cube is sampled.

Related: [[t371_critic_adds_eps_once_2026_11_01]] [[t371_particle_error_sqrt_k_over_n_any_states_2026_11_01]]
