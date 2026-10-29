"""Predicted (x*/x0 - 1)/d for the RR next-order term with eps > 0 (note, 20 Oct 04:2x): r K - p2 T H/(r K B2 B3),
r = s/(s+eps), p2 = s(eps+3s)/(4(eps+s)^2), s = sqrt(B2); and the iid-style S terms it says are absent, for comparison.
usage: python rr2e_pred.py EPS B1V B2V BO"""
import math
import sys
import numpy as np
sys.path.insert(0, "../agent_B")
from kfactor import K_rr
n = 10
eps = float(sys.argv[1])
bv = [float(s) for s in sys.argv[2:5]]
b = np.array([bv[0], bv[1]] + [bv[2]] * (n - 2))
B2, B3 = np.mean(b ** 2), np.mean(b ** 3)
Z = b * b - B2
T, S = np.mean(b * Z * Z), np.mean(Z * Z)
s = math.sqrt(B2); r = s / (s + eps)
p2 = s * (eps + 3 * s) / (4 * (eps + s) ** 2)
p3 = -3 * s * (eps ** 2 + 4 * eps * s + 5 * s * s) / (8 * (eps + s) ** 3)
print("eps %g b %s: B2 %.6g B3 %.6g T %.6g S %.6g r %.6f p2 %.6f; iid-style S terms (p2/4 + p3/(2r)) S/B2^2 = %.4f"
      % (eps, bv, B2, B3, T, S, r, p2, (p2 / 4 + p3 / (2 * r)) * S / B2 ** 2))
for b1 in (0.0, 0.5, 0.9):
    p = np.arange(n)
    h = 1 - 3 * p / (n - 1) + 2 * p * (p - 1) / ((n - 1) * (n - 2))
    H = np.mean((1 - b1 ** (p + 1)) * h)
    K0 = np.mean((1 - b1 ** (p + 1)) * (1 - p / (n - 1)))
    row = ["beta1 %g H %.6f limit %.6f" % (b1, H, r * K0 - p2 * T * H / (r * K0 * B2 * B3))]
    for b2 in (0.9995, 0.999, 0.998):
        K = K_rr(n, b1, b2)
        row.append("b2 %g K-form %.6f" % (b2, r * K - p2 * T * H / (r * K * B2 * B3)))
    print(" | ".join(row))
