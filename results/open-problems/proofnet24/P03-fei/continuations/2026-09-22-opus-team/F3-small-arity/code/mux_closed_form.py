"""Check of the closed form of the MUX selector remainder R_a (expansion on the data input a) against the direct value
D_MUX - (1-p) D_AND(not s, b) - p D_OR(s, b), and of the W-remainder r(1-r)[d - (p1-p0)^2].
MUX(s, a, b) = s ? a : b, inputs bits 0 (s, bias t), 1 (a, bias p), 2 (b, bias q)."""
import sys, os
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import fgate as F
F.lowprio()

pot = F.Pot(os.path.join(HERE, "..", "..", "inputs", "cert_vi_h24k40.npz"), 0.01)
MUX = np.array([1.0 - 2.0 * ((((x >> 1) & 1) if (x & 1) else ((x >> 2) & 1))) for x in range(8)])
AND = np.array([1.0, 1.0, 1.0, -1.0]); OR = np.array([1.0, -1.0, -1.0, -1.0])


def phi(w):
    w = np.asarray(w, float)
    return np.where(w > 0, -w * np.log2(np.where(w > 0, w, 1.0)), 0.0)


rng = np.random.default_rng(2)
N = 20000
U = rng.uniform(-14, 14, (N, 3))
P = 1 / (1 + 2.0 ** (-U))
t, p, q = P[:, 0], P[:, 1], P[:, 2]
DM, WM, _, _ = F.stats(MUX, P, pot)
DA, WA, _, _ = F.stats(AND, np.column_stack([1 - t, q]), pot)
DO, WO, _, _ = F.stats(OR, np.column_stack([t, q]), pot)
R_direct = DM - (1 - p) * DA - p * DO
RW_direct = WM - (1 - p) * WA - p * WO
p0 = (1 - t) * q; p1 = t + (1 - t) * q; po = t * p + (1 - t) * q
Vp = 4 * p * (1 - p); Vt = 4 * t * (1 - t)
a0 = (1 - 2 * p0) ** 2; a1 = (1 - 2 * p1) ** 2; m0 = (1 - p) * a0 + p * a1
yb = (1 - p) * q ** 2 + p * (1 - q) ** 2
R_closed = (t * (pot(p) + F.h2(Vp)) + (1 - p) * pot(p0) + p * pot(p1) - pot(po)
            - (phi(m0) - (1 - p) * phi(a0) - p * phi(a1)) - m0 * F.h2(4 * p * (1 - p) * t ** 2 / m0)
            - Vt * (phi(yb) - (1 - p) * phi(q ** 2) - p * phi((1 - q) ** 2) + yb * F.h2(p * (1 - p) / yb)))
RW_closed = p * (1 - p) * (t - (p1 - p0) ** 2)
err = np.abs(R_closed - R_direct)
print("MUX R_a closed form vs direct: max abs diff %.3e over %d random points (max |R| %.3e)" % (err.max(), N, np.abs(R_direct).max()))
print("W-remainder closed form p(1-p)[t - (p1-p0)^2] vs direct: max abs diff %.3e; min W-remainder %.3e"
      % (np.abs(RW_closed - RW_direct).max(), RW_direct.min()))
print("min R_a over the sample: %.4e ; min R_a / (t p (1-p)): %.4e" % (R_direct.min(), (R_direct / (t * p * (1 - p))).min()))
