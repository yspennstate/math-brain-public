# Audit of agent B's per-sample-Hessian vector term (T354, NOTE.md "Vector case, per-sample Hessians H_i", push d714532b)

Auditor agent A, 20 Oct 2026 06:4x. Verdict: CONFIRMED on an independent model and code, nine exact rows.

The statement checked, per coordinate j, with g_i(x) = H_i x + b_i, E b = 0, coordinatewise Adam under random reshuffling:

    (Hbar x)_j - (d K/2) [ r_j m_j + r_j (M x)_j + m_j (R x)_j ] + (p2_j/2) d^2 T_j H(beta1)/B2_j^2 = 0,
    M_jk = (3 E[b_j^2 H_jk] - Hbar_jk B2_j)/B2_j - 2 B3_j E[b_j H_jk]/B2_j^2,    R_jk = eps E[b_j H_jk]/(s_j (s_j + eps)^2).

## By hand

At frozen x, coordinate j's m and v are built from the values g_ij(x) alone, so its drift is the scalar RR drift at those values;
the scalar next-order derivation uses the values only through E g, V = E g^2, C = E g^3 - E g V and the Q term at x = 0. With
g_ij = sum_k (H_i)_jk x_k + b_ij:

    E g_j = (Hbar x)_j,   V_j = B2_j + 2 sum_k E[b_j H_jk] x_k + O(x^2),   E g_j^3 = B3_j + 3 sum_k E[b_j^2 H_jk] x_k + O(x^2),

so C_j/V_j = m_j + (M x)_j + O(x^2) with M exactly as stated (the scalar c1 with a_i -> the row (H_i)_{j.}), and
r_j(x) = s_j(x)/(s_j(x) + eps) has dr_j/dx_k = eps (dV_j/dx_k)/(2 s_j (s_j + eps)^2) = R_jk. The product r_j C_j/V_j to first order
in x is r_j m_j + r_j (M x)_j + m_j (R x)_j. Q is evaluated at x = 0, where H_i drops out, so the T_j H(beta1) term is the scalar one.
Within an epoch h_i = g_i^2 - V(x) still sums to zero, since V(x) is the epoch mean at the same x. Every step matches the NOTE.

## Independent exact check (vec_three_valued.py, vt_runs_*.txt)

Own code (not a copy of rr_exact_mom_eps.py): the scalar RR drift for a coordinate with TWO special samples, so three values
g1, g2, go; the slots (q1, q2) of the specials are uniform over the 30 ordered distinct pairs of each epoch, independent across
epochs; the far epochs by the cumulants of Y = A1 b2^(-q1) + A2 b2^(-q2) to order 4. Model: n = 6, three coordinates,

    b (rows j, columns s1 s2 other x4) = (5, 1, -1.5), (-6, 2, 1), (6, -2, -1),
    H_s1 = [[2,.5,.3],[.5,1,-.4],[.3,-.4,1.5]],  H_s2 = [[.7,-.6,0],[-.6,2.5,.5],[0,.5,.8]],  H_o = [[1.2,.2,-.3],[.2,1,.1],[-.3,.1,1.3]],

non-commuting, three-valued b in every coordinate and B3 of both signs - the case the candidate's own check (two coordinates,
one special, n = 10) does not reach. 3-d root by Newton with a difference Jacobian, residual under 1e-16.
G_j = (x*_j - pred_j)/(x0_j d^2): flat in d means the O(d) relative term is exact.

    beta1  eps   coordinate   G at beta2 0.998     0.999      0.9995
    0      0     1, 2, 3      -2.296 -2.316 -2.225  -2.299 -2.317 -2.227  -2.299 -2.317 -2.226
    0.5    1     1, 2, 3      -0.663 -0.444 -0.433  -0.666 -0.447 -0.436  -0.666 -0.447 -0.436
    0.9    3     1, 2, 3       0.319  0.620  0.614   0.316  0.616  0.610   0.317  0.617  0.611

d = 1 - beta2 halves along each row. In every family and coordinate G moves by at most 0.004 over a factor 4 in d, so the
O(d) term in x*/x0 is the candidate's, and the O(d^2) remainder is what G measures (all nine runs in vt_runs_*.txt).

Control "no-r1" (R dropped): at eps > 0 it moves by a factor 2 per halving of d (for example beta1 0.5 eps 1, coordinate 1:
10.9, 22.4, 45.5), so R is needed and the check can see it; at eps = 0, R = 0 and the two columns coincide, as they should.

## Not covered

H_i varying across more than three sample types; a rigorous remainder for the vector system (this confirms the O(d) coefficient,
not a bound). The scalar ingredients (K_rr, p2, T, H(beta1)) were taken as verified by the earlier audits.
