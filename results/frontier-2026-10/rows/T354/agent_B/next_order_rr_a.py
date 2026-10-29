# T354 next-order term under random reshuffling with UNEQUAL curvatures, eps = 0, any beta1 (agent B, 20 Oct 2026). Candidate.
# g_i = a_i x + b_i, mean b = 0, abar = E a, B_k = E b^k, Z = b^2 - B2, T = E[b Z^2], K = K_rr(n, beta1, beta2).
# The lemma is unchanged except f' = abar x and the slope of C/V at x = 0, C = E[g Z] = E g^3 - abar x V, V = E g^2:
#   c1 = (C/V)'(0) = (3 E[a b^2] - abar B2)/B2 - 2 B3 E[a b]/B2^2        (c1 = 2 when a = 1).
# 0 = abar x - (d K/2)(B3/B2 + c1 x) + (3/8) Q, Q = (d/B2)^2 T H as before (Q is taken at x = 0, where a drops out). So
#   x0 = d K B3/(2 abar B2),   x*/x0 = 1 + d (K c1/(2 abar) - (3/4) T H/(K B2 B3)) + O(d^2).
# Check: exact roots on b = (9, -1 x 9) with a_special = AS, a_other = AO, from audit_A/rr_exact_mom_eps.py with only
# g_s, g_o (and the bracket for the root) changed: the solver needs just the two gradient values, so it carries over exactly.
import sys, numpy as np
from kfactor import K_rr
n = 10; P = np.arange(n); B2, B3, T = 9.0, 72.0, 4608.0     # the test model's moments (next_order_rr_mom.py prints them)
h = 1 - 3 * P / (n - 1) + 2 * P * (P - 1) / ((n - 1) * (n - 2))
def H(b1): return np.mean((1 - b1 ** (P + 1)) * h)
src = open("../audit_A/rr_exact_mom_eps.py", encoding="utf-8").read().split("import os")[0]
assert "gs, go = 9 + x, -1 + x" in src
src = src.replace("gs, go = 9 + x, -1 + x", "gs, go = AS * x + 9, AO * x - 1")
n = 10
for AS, AO in [(3.0, 1.0), (1.0, 2.0), (0.5, 1.5), (4.0, 0.5)]:
    a = np.array([AS] + [AO] * 9); bb = np.array([9.0] + [-1.0] * 9)
    abar = a.mean(); Eab = np.mean(a * bb); Eab2 = np.mean(a * bb * bb)
    c1 = (3 * Eab2 - abar * B2) / B2 - 2 * B3 * Eab / B2 ** 2
    for b1 in (0.0, 0.5, 0.9):
        for b2 in (0.9999, 0.9995, 0.999):
            d = 1 - b2; ns = {"AS": AS, "AO": AO}
            sys.argv = ["x", str(b1), str(b2), "0"]
            exec(compile(src, "rr_exact_a", "exec"), ns)
            from scipy.optimize import brentq
            K = K_rr(n, b1, b2); x0 = d * K * B3 / (2 * abar * B2)
            xs = brentq(ns["D"], 0.05 * x0, 5 * x0, xtol=1e-12 * x0)
            ex = (xs / x0 - 1) / d; pr = K * c1 / (2 * abar) - 0.75 * T * H(b1) / (K * B2 * B3)
            print("a_s %.1f a_o %.1f abar %.2f c1 %.5f beta1 %.1f beta2 %s K %.6f exact (x*/x0-1)/d %.5f predicted %.5f gap/d %.3f"
                  % (AS, AO, abar, c1, b1, b2, K, ex, pr, (ex - pr) / d), flush=True)
