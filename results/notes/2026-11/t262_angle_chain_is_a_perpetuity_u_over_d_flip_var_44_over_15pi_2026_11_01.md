---
name: t262_angle_chain_is_a_perpetuity_u_over_d_flip_var_44_over_15pi_2026_11_01
description: [PROVISIONAL] T262 Target 1 proof: u=1/(n theta) obeys u'=u/D+xi/n with D theta-free, so u_L is a perpetuity (Donsker, no Ethier-Kurtz); flip variance 44/(15 pi n theta), checked 11/12
metadata:
  type: project
  created: 2026-11-01
  created_at: 2026-11-01T15:00:24+04:00
  status: provisional
  evidence: "one_layer_xi_run1.txt; moves m262a 89acdbda"
---

Deep He-ReLU, two inputs, width n, depth L = t n (row T262). With u = 1/(n theta), one layer is exactly
u' = u/D + xi/n, where D = |P g'_A| / |g_A| is the chi-square chord ratio sqrt(chi2_(k-1)/chi2_k) over the active set
A = {g > 0}. D does not depend on theta, and that is the whole trick: unrolled, u_L = u_0 e^(S_L) + (1/n) sum_k xi_k e^(S_L - S_(k+1)),
a discrete perpetuity whose weights are independent of the layer they multiply. Donsker on the 2-d walk (S = -sum log D, log|h|^2)
plus continuity of z -> int e^(z(t) - z(q)) dq gives the joint limit (t A_t/(3 pi), Hanin-Nica norm) with no generator convergence,
no localisation and no entrance-time argument. The start u_0 = 1/(n theta_0) is just the first term.

The flip term: E xi = 1/(3 pi) + O(theta + n^-1/2), and Var xi = 44/(15 pi n theta) to leading order, from
E R^4 (1/(2 pi)) int_0^theta ((e^2 - theta^2)^2 + e^4) de = 44 theta^5/(15 pi).

Measurement (one_layer_xi.py, 100,000 draws per cell, pre-registered within 10 pct at phi = 1, 4, 16, n 400 and 1600):
- E xi: 0.1024-0.1088 against 0.1061, so 6 of 6 pass.
- phi Var xi: 5 of 6 within 10 pct of 0.934. The miss is at theta 0.04 (+14 pct), and the excess grows with theta:
  +4 to 5 pct at theta 0.01, +40 pct at theta 0.16.

**Why:** the same structure (a theta-free random factor per layer plus a small additive correction) should turn the p-input
Gram problem (T262 Target 2) into a matrix perpetuity, and probably other "angle -> 0 at rate 1/l" chains (T244, T250 tanh).
CORRECTION (1 Nov, later, m262b): not a matrix perpetuity for p >= 3. The contraction acts on each pairwise angle and is not linear
in the positions. What holds is a per-side step u_ij' = u_ij/|M e_ij| + xi_ij/n with ONE shared theta-free M = P[g'_A g''_A]/|g_A|:
E xi = 1/(3 pi) on 12/12 side-cells, but phi Var xi is about 0.78 x 44/(15 pi) on the side away from the reference input (4/4 low). The per-coordinate flip integral with both
endpoints moving (side_const.py) gives 0.694 = 0.743 x 44/(15 pi) for that side, which the measurements approach as theta -> 0.
**How to apply:** for a Markov chain whose state shrinks like 1/l with multiplicative width noise, look for the reciprocal
variable that makes the step affine with a state-free multiplier, before reaching for Ethier-Kurtz.
Locators: the private repository, 06_math_research/frontier/rows/T262/DOSSIER.md section "1 Nov (an agent)",
moves.jsonl m262a (89acdbda). Related: [[t340_linear_bn_width_floor_exact_n_n1_over_2n1_per_mode_2026_11_01]].

