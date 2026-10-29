# Audit of agent B's next-order term with unequal curvatures (T354 NOTE.md, section of 20 Oct 05:1x)

Auditor agent A, 20 Oct 2026 05:2x. Scope: random reshuffling, eps = 0, any beta1, g_i = a_i x + b_i with mean b = 0.
Verdict: CONFIRMED.

    x0 = d K B3/(2 abar B2),   x*/x0 = 1 + d ( K c1/(2 abar) - (3/4) T H/(K B2 B3) ) + O(d^2),
    c1 = (3 E[a b^2] - abar B2)/B2 - 2 B3 E[a b]/B2^2.

## By hand

With V = E g^2 and h = g^2 - V, the first-order term is sum_j c_j E[g_i h_j]/V. Under reshuffling, within one epoch
sum_j h_j = 0 exactly (V is the epoch mean of g^2 at the frozen x), so for i != j in one epoch E[g_i h_j] = -E[g h]/(n-1), across
epochs it is E g_i E h_j = 0, and E[g h] = E g^3 - V E g = C. So a enters the linear term only through C, and the mean of m is
abar x. Expanding, E g^3 = B3 + 3x E[a b^2] + O(x^2) and V = B2 + 2x E[a b] + O(x^2), so
C/V = B3/B2 + x [ (3 E[a b^2] - abar B2)/B2 - 2 B3 E[a b]/B2^2 ] + O(x^2): the stated c1, equal to 2 when a = 1.
In the quadratic term, the x-dependent parts are x times E[(y-1)^2], which is O(d^2) under reshuffling because each epoch's h
sums to zero. That makes them O(d^3), so Q may be taken at x = 0, where a drops out. Solving abar x = (d K/2)(B3/B2 + c1 x) - (3/8) Q
to first order in d gives the bracket.

## Exact check on different b vectors (rr_a_check.py, rr_a_check_n5_*.txt, rr_a_check_n6_neg.txt)

The peer's check used b = (9, -1 x 9), n = 10. These runs change n, b and a, using my rr_exact_mom_eps.py with n, the two gradient
values and x0 replaced. H is taken from the momentum section's h(p) at the new n.

    n  b              a (s, o)    c1    beta1 0: gap/d (d 5e-4, 1e-3, 2e-3)   beta1 0.5               beta1 0.9
    5  (4, -1 x 4)    (2, 1)      3.0   -1.435 -1.435 -1.433                   -0.009 -0.009 -0.005    1.065 1.066 1.071
    5  (4, -1 x 4)    (0.5, 2)    2.5   -1.401 -1.401 -1.400                   -0.026 -0.025 -0.022    1.061 1.063 1.067
    6  (-5, 1 x 5)    (1.5, 0.5)  2.0   -2.234 -2.233 -2.230                   -0.104 -0.102 -0.097    1.799 1.802 1.811

gap = exact (x*/x0 - 1)/d minus the prediction. In all nine rows gap/d is flat over a factor 4 in d, so the O(d) coefficient is
exact and the remainder is O(d^2). The n = 6 vector has negative skew (B3 = -20, x0 < 0) and abar < 1. At n = 5, beta1 0.5 the
prediction meets the exact value to 1e-5 (0.13529 against 0.13530).

## Not covered

- eps > 0 with unequal curvatures is not checked.
- Both exact checks (the peer's and mine) run the same solver, on two-valued b only. The independent evidence is the hand
  derivation above plus new n, b and a. A three-valued b would need a different exact route.
