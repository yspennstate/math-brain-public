# T354 next-order term, random reshuffling, unequal curvatures AND eps > 0 (agent B, 20 Oct 2026). Candidate.
# Same as next_order_rr_a.py, plus eps. With s = sqrt(B2), r = s/(s+eps), p2 = s(eps+3s)/(4(eps+s)^2) (the verified a = 1 eps
# lemma) the linear term carries r(x) C(x)/V(x). For a != 1, V'(0) = 2 E[ab] != 0, so r moves with x at first order:
#   r1 = dr/dx(0) = eps E[a b]/(s (s+eps)^2).   Prediction:
#   x0 = r d K B3/(2 abar B2),   x*/x0 = 1 + d ( K (r c1 + r1 B3/B2)/(2 abar) - p2 T H/(r K B2 B3) ) + O(d^2).
# Without the r1 term (my first guess) the a != 1 rows should miss by d K r1 B3/(2 abar B2 r) per unit d.
import sys, numpy as np
from kfactor import K_rr
n = 10; P = np.arange(n); B2, B3, T = 9.0, 72.0, 4608.0     # the test model's moments (next_order_rr_mom.py prints them)
h = 1 - 3 * P / (n - 1) + 2 * P * (P - 1) / ((n - 1) * (n - 2))
def H(b1): return np.mean((1 - b1 ** (P + 1)) * h)
src = open("../audit_A/rr_exact_mom_eps.py", encoding="utf-8").read().split("import os")[0]
assert "gs, go = 9 + x, -1 + x" in src
src = src.replace("gs, go = 9 + x, -1 + x", "gs, go = AS * x + 9, AO * x - 1")
n = 10
for AS, AO in [(3.0, 1.0), (4.0, 0.5)]:
    a = np.array([AS] + [AO] * 9); bb = np.array([9.0] + [-1.0] * 9)
    abar = a.mean(); Eab = np.mean(a * bb); Eab2 = np.mean(a * bb * bb)
    c1 = (3 * Eab2 - abar * B2) / B2 - 2 * B3 * Eab / B2 ** 2
    for b1, EPS in [(0.0, 1.0), (0.0, 10.0), (0.9, 1.0), (0.9, 10.0)]:
        for b2 in (0.9999, 0.9995, 0.999):
            d = 1 - b2; ns = {"AS": AS, "AO": AO}
            sys.argv = ["x", str(b1), str(b2), str(EPS)]
            exec(compile(src, "rr_exact_a", "exec"), ns)
            from scipy.optimize import brentq
            K = K_rr(n, b1, b2); sq = B2 ** 0.5; r = sq / (sq + EPS); p2 = sq * (EPS + 3 * sq) / (4 * (EPS + sq) ** 2)
            r1 = EPS * Eab / (sq * (sq + EPS) ** 2); x0 = r * d * K * B3 / (2 * abar * B2)
            xs = brentq(ns["D"], 0.05 * x0, 5 * x0, xtol=1e-12 * x0)
            ex = (xs / x0 - 1) / d; pr = K * (r * c1 + r1 * B3 / B2) / (2 * abar) - p2 * T * H(b1) / (r * K * B2 * B3); pr0 = K * r * c1 / (2 * abar) - p2 * T * H(b1) / (r * K * B2 * B3)
            print("a_s %.1f a_o %.1f eps %g beta1 %.1f beta2 %s r1 %.5f exact (x*/x0-1)/d %.5f predicted %.5f gap/d %.3f | no-r1 guess %.5f"
                  % (AS, AO, EPS, b1, b2, r1, ex, pr, (ex - pr) / d, pr0), flush=True)
