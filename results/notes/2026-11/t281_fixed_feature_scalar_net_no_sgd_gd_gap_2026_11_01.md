---
name: t281_fixed_feature_scalar_net_no_sgd_gd_gap_2026_11_01
description: [PROVISIONAL] T281: scalar-output random-features net with Lipschitz convex loss on a ball has width-free uniform convergence, so no SCO SGD-vs-GD statistical gap; needs k >~ n outputs or first-layer training
metadata:
  type: project
  created: 2026-10-31
  created_at: 2026-10-31T23:00:13+04:00
  status: provisional
  evidence: ""
  originSessionId: b9a49845-179c-4e8f-8401-adcc0c5c2952
---



T281 (SGD vs full-batch GD separation), 1 Nov. Target 1 asked whether the Amir-Koren-Livni SCO hard instances can be built as a random-features ReLU model. They cannot, for any width. A scalar-output fixed-feature model with an L-Lipschitz convex loss on a norm ball has Rademacher complexity L B R/sqrt n, with no width in it. So projected GD at every step size and step count generalizes, and GD with T = n matches SGD.

The SCO instances need the loss to see w through at least about n linear functionals: k >~ n outputs by Maurer's sqrt(k) bound. The dimension blow-up of 2102.01117 (d >= T 2^(n+5)) was already cut to d = O(n) by Livni 2404.04931, so dimension was never the real obstacle.

Target 2: the statistical sense must beat uniform convergence; the precision sense (Abbe-Sandon) is an SQ statement.

No numerics, written during a compute-distress spell (swap thrash from other agents' jobs). Pushed research_pushes/2026-11-01-loop-T281-glm-no-separation (fc65712); card claim_27e3ec5f8a564d58b5a1e6b378fc7e0b (3 links); frontier move.

Related: [[t365_three_level_scalar_chain_is_two_level_2026_11_01]] and [[t288_multilayer_glm_free_energy_is_proved_by_chen_xia_for_every_depth_2026_11_01]]: in both, the row's proposed route was settled by a standard fact before any building.
