---
name: t383_depth3_lemma_pieces_change_only_at_kink_extrema_2026_11_02
description: T383 depth 3: piece count changes only at endpoint crossings or a second-layer kink extremum crossing 0 (proved); lazy route to N_t/N_0 = O(1) needs a bounded Gaussian density at init (unchecked)
metadata:
  type: project
  created: 2026-11-02
  created_at: 2026-11-02T02:27:43+04:00
  status: provisional
  evidence: "research_pushes/2026-11-02-loop-T383-depth3-route (research-repo 708e3d9); move e179425"
---

T383 target 1, depth 3 (two hidden layers, 1-D input, segment [A, B]), 2 Nov. At research-repo research_pushes/2026-11-02-loop-T383-depth3-route/DEPTH3_ROUTE.md (708e3d9); frontier move the private repository e179425.

Lemma (proved): N = 1 + K + sum_j Z_j, where K counts first-layer breakpoints and Z_j the zeros of the j-th second-layer pre-activation, which is continuous and piecewise linear with kinks at the breakpoints. Along training N changes only when:
- a breakpoint or a second-layer zero crosses A or B;
- some z_j has a local extremum at a kink (opposite slopes on the two sides) whose value crosses 0, changing Z_j by 2.
Transversal zeros pass over kinks without changing any count. A zero-slope piece at value 0 is excluded as non-generic.

Route (unchecked): in the lazy regime the extremum event needs value and one-side slope both O(m^-1/2) at init. Given the first layer, z_j is Gaussian in x, so a bounded joint density of (value, slope) at the kinks gives O(m^-1) per (j, i) pair: O(m) events against N_0 of order m, so N_t/N_0 = O(1), the constant factor target 1 asks for. The open input is a lower bound on that Gaussian conditional covariance at initialization, which moves the dossier's failure point from trained weights to init. The depth-3 numerics (ratios 1.17, 1.03, 1.02) suggest the events mostly cancel. See [[t383_two_layer_crossing_bound_pieces_change_o_sqrt_m_lazy_2026_11_02]].


Init check (2 Nov, research_pushes/2026-11-02-loop-T383-depth3-density, 77f3bb2): candidate pairs per m at c = 1 average 1.51, 1.46, 1.04, 1.16, 1.61 for m = 64..1024 (3 seeds), so O(m) holds numerically, slow growth not excluded; same order as N_0, so the route gives a constant, not 1 + o(1).
