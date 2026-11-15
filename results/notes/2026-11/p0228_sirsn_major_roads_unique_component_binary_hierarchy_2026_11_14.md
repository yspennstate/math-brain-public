---
name: p0228_sirsn_major_roads_unique_component_binary_hierarchy_2026_11_14
description: "[PROVISIONAL] Does E(inf,1) of a SIRSN have one unbounded component (Aldous OP33, P0228)? Yes for the binary hierarchy model (14 Nov, unaudited): every road line of height >= h0(gamma) lies in E(inf,1), a connected grid; general SIRSN open"
metadata:
  type: project
  created: 2026-11-14
  created_at: 2026-11-14T17:24:21+02:00
  status: provisional
  evidence: ""
---

P0228 = Aldous SIRSN Open Problem 33. Result (an agent, 14 Nov 2026, commit 5bd6e0fb, OP/P0228/NOTE.md): in the binary hierarchy model, a.s. every point of every road line of height >= h0(gamma) lies on a route between dense points at distance >= 3 from both, so E(inf,1) contains the grid of those lines; any component of diameter > sqrt2 * grid spacing meets the grid, so exactly one unbounded component. Key step: points straddling a height-h line X with vertical gap 2a and route box inside |x-X|<2^h (Aldous Lemma 4) make X = peak(I_x); Lemma 3(ii) single segment on X; comparing cost with Lemma 8 upper bound gives off-X vertical travel <= eta = 2K' delta^beta/(gamma^{h-1}(1-gamma)), uniform in the lattice H, then Prop 9 passes to the continuum and the random translation/rotation/scale of section 3.7 keeps it. General SIRSN still open; sufficient condition: a connected subset of E(inf,1) whose complement has bounded components. Next model: Kahn's Poisson line SIRSN (fast lines as the grid). status: provisional, author reread once, needs independent audit before posting. Related [[p0230_sirsn_span_length_reduced_to_one_route_tail_2026_11_14]].
