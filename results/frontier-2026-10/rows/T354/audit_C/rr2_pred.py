"""Predicted (x*/x0 - 1)/d for the RR next-order term (note, 20 Oct 04:0x/04:1x), at the K of each beta2 and at the limit K0.
usage: python rr2_pred.py B1V B2V BO"""
import sys
import numpy as np
sys.path.insert(0, "../agent_B")
from kfactor import K_rr
n = 10
bv = [float(s) for s in sys.argv[1:4]]
b = np.array([bv[0], bv[1]] + [bv[2]] * (n - 2))
B2, B3 = np.mean(b ** 2), np.mean(b ** 3)
Z = b * b - B2
T = np.mean(b * Z * Z)
print("b %s: B2 %.6g B3 %.6g T %.6g" % (bv, B2, B3, T))
for b1 in (0.0, 0.5, 0.9):
    p = np.arange(n)
    h = 1 - 3 * p / (n - 1) + 2 * p * (p - 1) / ((n - 1) * (n - 2))
    H = np.mean((1 - b1 ** (p + 1)) * h)
    K0 = np.mean((1 - b1 ** (p + 1)) * (1 - p / (n - 1)))
    row = ["beta1 %g H %.6f K0 %.6f limit %.6f" % (b1, H, K0, K0 - 0.75 * T * H / (K0 * B2 * B3))]
    for b2 in (0.9995, 0.999, 0.998):
        K = K_rr(n, b1, b2)
        row.append("b2 %g K-form %.6f" % (b2, K - 0.75 * T * H / (K * B2 * B3)))
    print(" | ".join(row))
