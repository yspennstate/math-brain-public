---
name: t383_two_layer_crossing_bound_pieces_change_o_sqrt_m_lazy_2026_11_02
description: T383 target 1 proved for two layers: piece count on a segment changes only via neurons whose endpoint pre-activation is within their movement of 0; lazy R=c/sqrt(m) gives N_t/N_0 = 1+O(m^-1/2); checked 12 of 12 nets, m 64-4096; depth>=3 open
metadata:
  type: project
  created: 2026-11-02
  created_at: 2026-11-02T02:15:48+04:00
  status: provisional
  evidence: "research_pushes/2026-11-02-loop-T383-two-layer-crossing (research-repo 2c91222); frontier move 24e1ec6"
---

T383 target 1, two-layer case, proved on 2 Nov. It is at research-repo research_pushes/2026-11-02-loop-T383-two-layer-crossing (2c91222: TWO_LAYER.md, two_layer_bound.py, run2.txt), with the frontier move on T383 at the private repository 24e1ec6.

Statement: g_t(x) = sum a_i relu(w_i x + b_i) on [A,B], and N_t = 1 + #{i : z_i(A), z_i(B) of opposite sign}, which equals the activation-pattern piece count when the breakpoints are distinct. If each neuron moves at most R_i up to time t, then sup_{s<=t} |N_s - N_0| <= #{i : |z_{i,0}(A)| <= R_i sqrt(1+A^2)} + the same at B. The proof is Cauchy-Schwarz on the endpoint signs: a neuron changes the count only if a sign at an endpoint flips.

With i.i.d. N(0, I) init and a deterministic bound R, E sup |N_t - N_0| <= 4mR/sqrt(2 pi), against E N_0 = 1 + m theta/pi. A lazy-regime bound R = c/sqrt(m), such as Du-Zhai-Poczos-Singh arXiv:1810.02054 for first-layer GD on unit-norm inputs, gives N_t/N_0 = 1 + O(m^-1/2) uniformly in time. Their bound holds only with high probability, so it has to be combined with the count by Markov plus a union bound.

Check on 12 trained nets (m = 64 to 4096, GD lr 1, 2,000 steps, sin(3x)): the bound holds 12 of 12 and is loose 10-70x. The relative change falls 0.037-0.055, 0.020-0.021, 0.003-0.011, 0.001-0.006. sqrt(m) times the largest single-neuron move grows from about 15 to 25, because it is a maximum over m neurons.

Depth >= 3 is still open: second-layer kinks move with every first-layer weight, so the argument needs the density of deep pre-activations near 0. That is the dossier's failure point. Earlier numerics on this row: [[t383_lazy_regime_piece_ratio_1p17_1p03_1p02_widths_32_128_512_2026_11_02]].


Math-store cards (2 Nov): the two-layer bound is claim_4afd603bc3184331842655f645e252d6, depends_on the Du-Zhai-Poczos-Singh movement-bound card claim_b9519788c8344754bcec495812468b0d; exported to research_pushes/2026-11-02-loop-T383-two-layer-crossing/card_* (879ca75).
