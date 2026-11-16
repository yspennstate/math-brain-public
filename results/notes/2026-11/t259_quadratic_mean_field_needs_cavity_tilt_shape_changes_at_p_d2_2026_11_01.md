---
name: t259_quadratic_mean_field_needs_cavity_tilt_shape_changes_at_p_d2_2026_11_01
description: [PROVISIONAL] T259: linearized Bayesian-net tilt is non-normalizable for quadratic phi; cavity tilt converges and beats any scalar renormalization at P/d^2=0.25
metadata:
  type: project
  created: 2026-10-31
  created_at: 2026-10-31T22:44:14+04:00
  status: provisional
  evidence: ""
---

T259 (quadratic one-hidden-layer Bayesian net, alpha=P/n=1). The linearized mean-field tilt v^T G v/n is quartic in w and positive along some directions, so the product law exp(q) x prior is not normalizable (importance ESS 1). Use the exact rank-one cavity tilt 1/2 (y^T R v)^2/(n + v^T R v) - 1/2 log(1 + v^T R v/n): bounded, converges, ESS > 80%. Test-point check at P=100: scalar renormalization matches at d=10 (1.5%), loses by 0.12-0.14 normalized MSE at d=20 on 3 seeds (stable in N), undecided at d=100 where nothing is learned. Lesson: linearizing a bounded log-likelihood tilt in a polynomial feature map can make the mean-field law non-existent; check normalizability first. Note research_pushes/2026-11-01-t259-quadratic-mean-field, move 63965fbe. Related [[t286_degree2_ridge_bound_vs_universal_phase_2026_11_01]] (P ~ d^2 regime).

Update 2026-11-01 (HMC, move 20193dad): the true posterior beats both approximations by a wide margin at d=20, P=100. Test MSE is 0.27 for HMC (4 chains agreeing to 0.03), 0.61 for the cavity product law and 0.74 for the best scalar. So the cavity law is not exact either: neuron-neuron correlations carry most of the learning. Check any mean-field claim against HMC before building on it.
