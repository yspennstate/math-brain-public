# Second audit of agent B's unequal-curvature RR next-order term with eps > 0 (T354 NOTE, push 194cfa01)

Auditor agent A, 20 Oct 2026 06:0x. Verdict: CONFIRMED on two-valued b, at beta1 0, 0.5 and 0.9 and eps 1, 3 and 10. The
statement checked, with s = sqrt(B2):

    x0 = r d K B3/(2 abar B2),   x*/x0 = 1 + d ( K (r c1 + r1 B3/B2)/(2 abar) - p2 T H/(r K B2 B3) ) + O(d^2),
    r = s/(s + eps),  r1 = eps E[a b]/(s (s + eps)^2),  p2 = s (eps + 3 s)/(4 (eps + s)^2).

## Route

rr_a_eps_check.py is rr_a_check.py (the eps = 0 curvature audit, AUDIT_RR_CURV_agent_A.md) with eps passed to the exact solver
rr_exact_mom_eps.py (Laplace kernel k(u) = (pi u)^(-1/2) [1 - eps sqrt(pi u) erfcx(eps sqrt u)], epochs factorized given u, no Taylor
step) and the eps > 0 prediction. At eps 0 it reproduces rr_a_check_n5_a2_1.txt digit for digit. By hand: r1 is the x-slope of r at
x = 0. V(x) = E[(a x + b)^2] = B2 + 2 x E[a b] + O(x^2), so s'(0) = E[a b]/s and dr/dx = eps s'/(s + eps)^2 = r1, as stated.

## Results (gap/d = (exact - predicted)/d of (x*/x0 - 1)/d, at beta2 0.9995 / 0.999 / 0.998)

    case                                  eps   beta1 0                 beta1 0.5               beta1 0.9
    n 5, b (4, -1 x 4), a (2, 1)          1     -1.180 -1.181 -1.179    -0.171 -0.171 -0.169    0.610 0.610 0.613
    n 5, b (4, -1 x 4), a (2, 1)          10    -0.645 -0.651 -0.651    -0.158 -0.164 -0.165    0.246 0.240 0.240
    n 6, b (-5, 1 x 5), a (1.5, 0.5)      10    -1.068 -1.074 -1.073    -0.307 -0.312 -0.311    0.424 0.418 0.420
    n 5, b (4, -1 x 4), a (0.5, 2)        3     -0.881 -0.883 -0.881    -0.199 -0.201 -0.200    0.367 0.365 0.367

gap/d is flat in d in all twelve families (spread at most 0.012), so the coefficient of d is right in every case. Without the r1 term
the prediction is off by 0.006 to 0.037, a fixed amount rather than one proportional to d (for example n 6, eps 10, beta1 0: exact
-0.18964, with r1 -0.18911, without -0.22649). The n 6 case has B3 < 0 and E[a b] < 0, so r1 enters with the other sign. The eps 10
case repeated at h 0.01 (rr_a_eps_n5_a2_1_e10_h01.txt) reproduces every printed digit.

## Not covered

Three-valued b and a_i varying within the bulk: this exact solver tracks one special sample per epoch, so it needs b and a to be
two-valued. beta1 0.5 and eps 10, uncovered by the first audit, are covered here.
