---
name: t371_learned_critic_adds_eps_once_2026_11_01
description: [VERIFIED] T371 critic: advantage error eps_A adds F_1 eps_A/((1-gamma) beta) to the uniform-in-time particle error; ring: bias ~2 eps_A
metadata:
  type: project
  created: 2026-11-01
  created_at: 2026-11-01T10:52:13+04:00
  status: provisional
  evidence: ""
---



Pushed 5ce7a21, move b7a3797b. Follows [[t371_particle_error_sqrt_k_over_n_any_states_2026_11_01]].

- The drift error is at most F_1 eps_A/(1-gamma), because the weights d(s) pi(a|s) sum to 1. Only the L1(d_nu pi) error enters.
- The coupling becomes d sqrt(D)/dt <= -beta sqrt(D) + L_z eps_N + delta.
- Ring MDP: a fixed bias costs about 2.0 eps_A in the logits; it grows 19-36 percent from t=5 to t=20 (my no-growth prediction was wrong as worded), then stays flat to t=40.
- Fresh zero-mean noise costs about 0.28 eps_A, a seventh of the bias cost; the order sqrt(h) delta fits.

**Why:** this closes the T371 learned-critic item inside beta > 0.

**How to apply:** a bounded-in-time claim needs a run long enough to see the plateau. Run to twice the transient before saying it does not grow.

Folder: research-repo research_pushes/2026-11-01-loop-T371-critic
