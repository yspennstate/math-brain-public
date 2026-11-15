---
name: t371_concave_cube_radius_0p42_to_0p45_not_half_2026_11_01
description: [PROVISIONAL] T371 below threshold: at tau 0.1 the soft value is numerically concave on max|z|<=0.4 (margin -0.0025), not on the half cube (corner eig +0.033); scale-0.4 features give the convex-route bound at every sigma, exp(1.6G/sigma^2)
metadata:
  type: project
  created: 2026-11-01
  created_at: 2026-11-01T14:11:02+04:00
  status: provisional
  evidence: ""
  originSessionId: b9a49845-179c-4e8f-8401-adcc0c5c2952
---



Finer scan 1 Nov (t371_halfcube.py, 17^4 grid + 20,000 random points per cube): r 0.35 grid max -0.0456, margin -0.0325; r 0.4 grid max -0.0179, margin -0.0025; r 0.5 grid max +0.0331 at (-0.5, 0.5, 0.5, -0.5), 18 positive random points. Corners alone: -0.0072 at r 0.42, +0.0085 at r 0.45. The margin uses an estimated Lipschitz constant (largest neighbour change), not a certified one. The first scan (step 0.25) put its first positive points at max|z| = 0.5, which I read as concave below 0.5. Pushed 8801bc7.

Related: supersedes [[t371_convex_route_fails_full_box_holds_half_scale_2026_11_01]] on the radius; same row as [[t371_critic_adds_eps_once_2026_11_01]]

Update 1 Nov 14:32: measured particle error (t371_scale.py, dcf2042): with c 0.4 and c 1, sigma 0.5/0.2/0.1, N 40-640, to t 40, error x sqrt N stays 0.23-0.43 and 0.46-0.85 with no growth in 16 of 18 rows. At c 1 the logits reach 0.71, outside the concave cube, and the error still does not grow. So the non-concavity is a gap in the proof, not in the behaviour, on this MDP.

Folder: research-repo research_pushes/2026-11-01-loop-T371-scale
