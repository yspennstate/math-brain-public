---
name: t384_stable_ntk_first_layer_jumps_at_time_zero_top_neuron_speed_log_m_2026_11_01
description: [PROVISIONAL] T384: in the alpha-stable NTK net the top-|w| neuron's u moves at speed (log m)^(1/alpha), so H~(1) jumps at t=0+ with positive probability
metadata:
  type: project
  created: 2026-11-01
  created_at: 2026-11-01T00:05:14+04:00
  status: provisional
  evidence: ""
---

T384 move 46e6ecec (written 2026-11-01 00:05 +0400). 2206.08065 scaling sc = (m log m)^(-1/alpha), eta = (log m)^(2/alpha): eta sc^2 w_(k)^2 -> Gamma_k^(-2/alpha) (top neurons carry H~(1)); u_(1) speed (log m)^(1/alpha), its effect on f only (log m)^(-1/alpha) per unit move, so it flips a pattern before the residual moves whenever its motion direction leaves the pattern's recession cone; H~(1) then changes by Gamma_1^(-2/alpha) x O(1). Numerics alpha 1, 48 seeds: first-flip time x log m = 0.47, 0.34, 0.48 at m = 1e2, 1e3, 1e4; flipped share 0.44 -> 0.73. Residual already moved 0.2-0.4 by the flip at these widths (log separation only). Extends an agent's 18 Oct measurement in the row dossier. Same few-largest-terms mechanism as heavy-tailed sums elsewhere; scaling corrected from the script header's O(1) speed.

Update 2026-11-01 04:06: move de2f4e89. The limit flip share is computable from the initial state: the share of seeds whose top-neuron ray v = sign(w) sum_{active j} r_j x_j leaves its pattern cone is 0.860, 0.873, 0.850, 0.835 (400 seeds, se 0.02) at m 1e2-1e5, alpha 1, k 4, d 5, flat in m (exit_cone.py, same seeding as flip.py). Measured flipped-by-T=1 0.44, 0.54, 0.73 rises toward it, so at reachable widths the log m separation of time scales is still only partial. The numpy matmul overflow warnings on this Mac (Accelerate) were spurious: 0 of 1600 seeds non-finite or off an einsum recomputation.
