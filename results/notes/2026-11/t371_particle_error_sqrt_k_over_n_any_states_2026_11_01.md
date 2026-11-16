---
name: t371_particle_error_sqrt_k_over_n_any_states_2026_11_01
description: [PROVISIONAL] T371 continuous states: uniform-in-time particle error ~ sqrt(k/N), k = feature-span dim, free of |S|,|A|,d (beta>0, Gaussian prior)
metadata:
  type: project
  created: 2026-11-01
  created_at: 2026-11-01T09:06:47+04:00
  status: provisional
  evidence: ""
---



Pushed 65058ec, move 92be3a6e. Follows [[t371_particle_error_uniform_in_time_2026_11_01]].

The only finite-K step was eps_N. It is replaced as follows:

- The J-drift lies in the feature span V, which bounds E|P_V theta|^2 uniformly.
- Symmetrization, Ledoux-Talagrand (factor 2 with |.|) and Cauchy-Schwarz give 4 R_phi sqrt(M_V/N).
- Efron-Stein adds 2 F_0^2/N.

Checks:

- Static: the measured value is 6-16x below the bound. It grows with the number of feature points until they cover V, so my prediction of no growth was wrong as worded.
- Ring MDP: S=16 and S=128 give the same error x sqrt N, but the policy stays near the prior.

**Why:** this closes the continuous-state item of T371 target 2.

**How to apply:** the particle count needed scales with the feature-span dimension, not the state space. A push script derived from push_t371b.sh re-exports the old card into card/, so drop that block for result-only pushes.

Update 01 Nov 09:29: the first ring check could not move the policy at all. With features (cos s, sin s, a - 1/2) the gradient vanishes identically, by symmetry, at any reward scale. With (cos s, sin s, (2a-1) sin s) the policy reaches logits +-0.94 and +-0.998, error x sqrt N stays 0.29-0.68, and S=128 is 4-17% above S=16 in all six pairs (within the 8-seed noise). Before trusting a flow-tracking check, confirm the drift at the start is nonzero.

Folder: research-repo research_pushes/2026-11-01-loop-T371-cont
