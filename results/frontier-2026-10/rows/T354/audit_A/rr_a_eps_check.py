# Second audit of agent B's unequal-curvature RR next-order term with eps > 0 (T354 NOTE, push 194cfa01), agent A,
# 20 Oct 05:5x. Copy of rr_a_check.py with eps passed to the exact solver and the eps > 0 prediction:
#   x0 = r d K B3/(2 abar B2), x*/x0 = 1 + d (K (r c1 + r1 B3/B2)/(2 abar) - p2 T H/(r K B2 B3)),
#   s = sqrt(B2), r = s/(s+eps), r1 = eps E[a b]/(s (s+eps)^2), p2 = s (eps + 3 s)/(4 (eps + s)^2).  Argv: n BS AS AO EPS [h].
# A different b vector and n: b = (BS, BO x (n-1)) with mean 0, g = a x + b. Exact roots from rr_exact_mom_eps.py with n, the two
# gradient values and x0 replaced (the solver only uses the slot of the special sample), against
#   x*/x0 = 1 + d (K c1/(2 abar) - (3/4) T H/(K B2 B3)),  x0 = d K B3/(2 abar B2),
#   c1 = (3 E[a b^2] - abar B2)/B2 - 2 B3 E[a b]/B2^2,  H = avg_p (1 - b1^(p+1)) h(p),  h(p) = 1 - 3p/(n-1) + 2p(p-1)/((n-1)(n-2)).
# Argv: n BS AS AO; the b1/b2 grid is below.
import sys, numpy as np
from scipy.optimize import brentq
sys.path.insert(0, "../agent_B"); from kfactor import K_rr
NS, BS, AS, AO, EPS = int(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5])
HH = sys.argv[6] if len(sys.argv) > 6 else "0.02"
BO = -BS / (NS - 1)
src = open("rr_exact_mom_eps.py", encoding="utf-8").read().split("import os")[0]
for old, new in [("n = 10; d = 1 - b2", "n = NS; d = 1 - b2"), ("gs, go = 9 + x, -1 + x", "gs, go = AS * x + BS, AO * x + BO")]:
    assert src.count(old) == 1, old
    src = src.replace(old, new)
b = np.array([BS] + [BO] * (NS - 1)); a = np.array([AS] + [AO] * (NS - 1))
B2, B3 = np.mean(b ** 2), np.mean(b ** 3); Z = b ** 2 - B2; T = np.mean(b * Z ** 2)
sB = np.sqrt(B2); r = sB / (sB + EPS); r1 = EPS * np.mean(a * b) / (sB * (sB + EPS) ** 2); p2 = sB * (EPS + 3 * sB) / (4 * (EPS + sB) ** 2)
abar = a.mean(); c1 = (3 * np.mean(a * b * b) - abar * B2) / B2 - 2 * B3 * np.mean(a * b) / B2 ** 2
P = np.arange(NS); hp = 1 - 3 * P / (NS - 1) + 2 * P * (P - 1) / ((NS - 1) * (NS - 2))
print("eps %g h %s n %d b (%g, %g x %d) a (%g, %g): B2 %.6g B3 %.6g T %.6g abar %.4f c1 %.6f" % (EPS, HH, NS, BS, BO, NS - 1, AS, AO, B2, B3, T, abar, c1), flush=True)
for b1 in (0.0, 0.5, 0.9):
    for b2 in (0.9995, 0.999, 0.998):
        d = 1 - b2; ns = {"NS": NS, "AS": AS, "AO": AO, "BS": BS, "BO": BO}
        sys.argv = ["x", str(b1), str(b2), str(EPS), HH]
        exec(compile(src, "rr_exact_a", "exec"), ns)
        K = K_rr(NS, b1, b2); x0 = r * d * K * B3 / (2 * abar * B2)
        lo, hi = 0.05 * x0, 5 * x0
        if x0 < 0: lo, hi = hi, lo
        xs = brentq(ns["D"], lo, hi, xtol=1e-12 * abs(x0))
        H = np.mean((1 - b1 ** (P + 1)) * hp)
        ex = (xs / x0 - 1) / d; pr = K * (r * c1 + r1 * B3 / B2) / (2 * abar) - p2 * T * H / (r * K * B2 * B3)
        pr0 = K * r * c1 / (2 * abar) - p2 * T * H / (r * K * B2 * B3)
        print("  beta1 %.1f beta2 %s K %.6f x* %.10g exact (x*/x0-1)/d %.5f predicted %.5f gap/d %.3f  (no r1: %.5f)" % (b1, b2, K, xs, ex, pr, (ex - pr) / d, pr0), flush=True)
