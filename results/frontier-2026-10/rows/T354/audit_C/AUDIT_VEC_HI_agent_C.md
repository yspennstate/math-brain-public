# T354 vector case with per-sample Hessians H_i, random reshuffling, audit 1 (agent C, 20 Oct 2026 06:5x)

Object: the NOTE section "Vector case, per-sample Hessians H_i: CANDIDATE (20 Oct 06:1x)" of agent_B (push d714532b). Per coordinate j,

    (Hbar x)_j - (d K/2) [ r_j m_j + r_j (M x)_j + m_j (R x)_j ] + (p2_j/2) d^2 T_j H(beta1)/B2_j^2 = 0,
    M_jk = (3 E[b_j^2 H_jk] - Hbar_jk B2_j)/B2_j - 2 B3_j E[b_j H_jk]/B2_j^2,   R_jk = eps E[b_j H_jk]/(s_j (s_j + eps)^2),

a linear system for x* to O(d^2).

Verdict: CONFIRMED.
- M and R are re-derived by hand below.
- The solver's closed-form M and R agree with a central-difference gradient of the exact moment ratio to at most 1.4e-9.
- The test model is new: three coordinates, three-valued b in each coordinate, b vectors not collinear across coordinates, and three
  distinct non-commuting Hessians.
- 30 exact roots were computed: two Hessian sets, (beta1, eps) in {(0,0), (0.9,0), (0,1), (0.9,1), (0.5,1)}, and beta2 0.9995, 0.999 and 0.998.
- In all 30, the statistic G_j = (x*_j - pred_j)/(x0_j d^2) is flat in d. With M = R = 0 it doubles each time d halves.

## Re-derived by hand

- Coordinatewise Adam builds m_j and v_j from g_{.j} alone.
- At frozen x, coordinate j's drift is the scalar random-reshuffling drift at the values g_ij = (H_i x)_j + b_ij. It is a symmetric
  function of those values, and the coordinates couple only through x.
- So the scalar expansion carries over line by line, with the mean gradient abar x replaced by (Hbar x)_j:
  0 = (Hbar x)_j - (d K/2) r_j(x) C_j/V_j + (p2_j/2) Q_j + O(d^3), where Q_j = (d/B2_j)^2 T_j H(beta1) is taken at x = 0.
- K is unchanged: it uses only the zero-sum of Z within an epoch.
- To first order in x:
  - V_j = E g_j^2 = B2_j + 2 sum_k E[b_j H_jk] x_k.
  - E g_j^3 = B3_j + 3 sum_k E[b_j^2 H_jk] x_k.
  - C_j/V_j = E g_j^3/V_j - (Hbar x)_j = m_j + (M x)_j, with M exactly as in the note. The -Hbar_jk B2_j/B2_j term is the mean.
- s_j(x) = sqrt(V_j) = s_j + sum_k E[b_j H_jk] x_k/s_j and dr/ds = eps/(s + eps)^2. So r_j(x) = r_j + (R x)_j with R as in the note.
- The linear part of r_j C_j/V_j is therefore r_j (M x)_j + m_j (R x)_j. With H_i = a_i (scalar) and one coordinate this is the
  scalar unequal-curvature term, which is verified (two audits each at eps = 0 and eps > 0).

## Exact roots (vec3_audit.py, vec3_batch.sh, vec3_jobs.txt, vec3_out/, table vec3_table.py -> vec3_table.txt)

Model:
- n = 10: samples 1 and 2 carry (H_1, b_1) and (H_2, b_2); the other eight carry (H_o, b_o).
- b_1 = (6, -3, 2), b_2 = (2, 5, -6), b_o = -(b_1 + b_2)/8.
- B3 per coordinate is (21.6, 9.79, -20.7), so both signs occur.
- Hessian set P: [[4,1,0],[1,2,.5],[0,.5,1]], [[.5,-.3,.2],[-.3,3,0],[.2,0,2]], [[1,.2,-.1],[.2,.8,.3],[-.1,.3,1.5]].
- Hessian set Q: [[.6,-.9,.4],[-.9,3.5,-.7],[.4,-.7,1.2]], [[2.5,.6,-.8],[.6,.4,.3],[-.8,.3,3]], [[1.2,-.25,.15],[-.25,1,-.35],[.15,-.35,.9]].

Solver:
- Each coordinate's exact drift is D of rr_exact_two_special_a.py, my scalar solver (audit a9724714), evaluated at the three values (g_1j, g_2j, g_oj).
- The root comes from Newton with a difference Jacobian. The residual is at most 8e-17 everywhere, against drifts of order 1e-3.

Prediction:
- The prediction is built without the note's algebra: phi_j(x) = r_j(x) C_j(x)/V_j(x) is linearised by central differences at
  x = 0 from the exact three-valued moments.
- The note's M and R are computed separately. The largest gap between the two ("MR vs grad") is 1.4e-9.

| H | beta1 | eps | G at beta2 0.9995 | 0.999 | 0.998 | G(0.998) - G(0.9995) | noM, coord 1, at 0.9995 / 0.999 / 0.998 |
|---|---|---|---|---|---|---|---|
| P | 0 | 0 | [-6.073 -8.677 -5.750] | [-6.065 -8.669 -5.740] | [-6.050 -8.652 -5.721] | [0.024 0.026 0.029] | 2144 / 1071 / 534 |
| P | 0 | 1 | [-5.235 -7.157 -5.396] | [-5.226 -7.145 -5.385] | [-5.209 -7.122 -5.361] | [0.026 0.035 0.035] | 1638 / 818 / 408 |
| P | 0.5 | 1 | [-2.333 -3.911 -2.303] | [-2.325 -3.900 -2.293] | [-2.309 -3.879 -2.274] | [0.024 0.032 0.029] | 1349 / 674 / 337 |
| P | 0.9 | 0 | [3.386 2.648 4.705] | [3.400 2.668 4.723] | [3.427 2.707 4.760] | [0.041 0.060 0.055] | 654 / 329 / 167 |
| P | 0.9 | 1 | [1.885 1.074 2.544] | [1.895 1.089 2.558] | [1.916 1.118 2.585] | [0.031 0.043 0.041] | 499 / 251 / 127 |
| Q | 0 | 0 | [-3.912 -7.424 -5.856] | [-3.897 -7.407 -5.849] | [-3.867 -7.373 -5.834] | [0.045 0.051 0.022] | 226 / 111 / 54 |
| Q | 0 | 1 | [-4.110 -6.275 -5.506] | [-4.096 -6.259 -5.497] | [-4.068 -6.226 -5.478] | [0.042 0.050 0.029] | 138 / 67 / 32 |
| Q | 0.5 | 1 | [-1.806 -3.840 -2.130] | [-1.796 -3.827 -2.122] | [-1.775 -3.802 -2.104] | [0.031 0.039 0.026] | 115 / 56 / 27 |
| Q | 0.9 | 0 | [3.382 0.889 5.439] | [3.396 0.905 5.458] | [3.423 0.937 5.496] | [0.041 0.048 0.057] | 73 / 38 / 21 |
| Q | 0.9 | 1 | [1.793 -0.073 3.054] | [1.804 -0.061 3.069] | [1.825 -0.038 3.097] | [0.032 0.036 0.042] | 45 / 23 / 13 |

How to read it:
- G is O(1) and moves by at most 0.06 while d changes fourfold. Each step from 0.9995 to 0.999 to 0.998 moves it about twice as
  much as the step before, which is the O(d^3) term, linear in d after dividing by d^2. So the O(d) relative term of the note is exact
  on this model.
- With the coupling through H_i dropped (M = R = 0, Hbar kept), G grows as 1/d. That is an O(1) error in the coefficient.
- A mistake in M or R, or a mixing between coordinates that the note missed, would show as G scaling like 1/d in some coordinate.
  None does, including coordinate 2 of Q at beta1 0.9, eps 1, where G passes through zero.

## Not covered

- A rigorous remainder.
- The regime where n d is not small.
- More than three distinct sample values per coordinate. Here every coordinate is three-valued. With three values the linear
  response of the drift is pinned at three points, so a test with four or more values would also check that the response is
  quadratic in b.
- Non-symmetric H_i. Every H_i here is symmetric. The derivation does not use symmetry.
