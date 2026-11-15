---
name: t227_one_example_relu_catapult_is_an_arc_map_no_divergence_2026_11_05
description: "[PROVISIONAL] T227 catapult: one-example 2-layer net reduces exactly to (v_i,z_i); bias-free ReLU limit = map on (alpha, beta, arc of live neurons); clean catapult c in (2,~3.45), collapse above, NO divergence to c=20 (neurons die instead); width 1e4 matches"
metadata:
  type: project
  created: 2026-11-05
  created_at: 2026-11-05T16:24:46+02:00
  status: provisional
  evidence: ""
---

status: provisional (exact reduction and arc structure proved; outcome classes read off the map numerically; limit through the O(log m) catapult not proved).

What: a two-layer network f = sum v_i sigma(w_i.x/sqrt d)/sqrt m trained by GD on ONE example only moves through the 2m scalars (v_i, z_i), z_i = w_i.x/sqrt d (checked against the full network to 2e-15). For bias-free ReLU every live neuron moves by the same linear map; with s = v+z, t = v-z, rho = r/sqrt m, a neuron is (alpha_t s0, beta_t t0), alpha = prod(1 - eta rho), beta = prod(1 + eta rho), and the live set is an arc of the polar angle of (s0, t0). Infinite width: P = (2/pi) alpha^2 int_I cos^2, Q = (2/pi) beta^2 int_I sin^2, rho = (P-Q)/4, lambda = (P+Q)/2. No deaths = the uv map (edge 4).

Measured (c = eta lambda_0): clean catapult for c in (2, ~3.45), live fraction 0.5 -> 0.32, end eta*lambda 2 -> 0.1, insensitive to the seed; above ~3.45 almost all neurons die, outcome seed-dependent, end eta*lambda ~0.01; c >= 7: 52/56 limit runs all neurons dead; no divergence to c = 20 (limit) and none at width 1e4 for c 3.8-20 (12/12 all-dead at c 8-20). Width 1e4 matches the limit within a few percent for c 2.25-3.5. Contrast: with 64 examples the same net diverges near c 4.6-4.9 [[t227_catapult_edge_relu_near_4_tanh_near_8_not_12_2026_10_30]].

Where: brain-repo/06_math_research/frontier/rows/T227/w_agent/ (one_example.py, limit_map.py, *.out); cards from loop_math_agent/staging/gen/make_334.py (bundle_334). What would change it: a finite-width one-example ReLU run that diverges, or a proof that the map's limit fails over the catapult's O(log m) steps.

Related: [[t227_catapult_edge_relu_near_4_tanh_near_8_not_12_2026_10_30]] (64-example width sweep), [[compaction_agent_20261105T155433]] (this loop).
