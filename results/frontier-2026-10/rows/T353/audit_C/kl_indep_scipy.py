# agent C, 19 Oct: independent check of cert_kl_arb.py with scipy - densities rebuilt from the construction in
# REFUTATION_T2.md with NO shift (x: B -> N(-2)xN(0), notB -> N(0)xN(a2-v2); x': B -> N(-1)xN(0), notB -> N(0)xN(-v2);
# ANTI a2-v2 = 2, -v2 = 1; SAME 0, -1). The script's g1 is this g1 + 1. Log-sum-exp form, so no underflow in the tails.
import numpy as np
from scipy.integrate import quad
from scipy.special import logsumexp
lN = lambda x, m: -(x - m) ** 2 / 2 - 0.5 * np.log(2 * np.pi)
def lpq(g1, z, same):
    a, c = (0, -1) if same else (2, 1)
    lp = logsumexp([lN(g1, -2) + lN(z, 0), lN(g1, 0) + lN(z, a)]) - np.log(2)
    lq = logsumexp([lN(g1, -1) + lN(z, 0), lN(g1, 0) + lN(z, c)]) - np.log(2)
    return lp, lq
def K(g1, same, qp):
    def f(z):
        lp, lq = lpq(g1, z, same)
        if qp: lp, lq = lq, lp
        return np.exp(lp) * (lp - lq)
    return quad(f, -40, 40, points=[-3, 0, 3], limit=400, epsabs=1e-15, epsrel=1e-12)[0]
for qp in (False, True):
    d = lambda g: K(g, True, qp) - K(g, False, qp)
    vals = [d(g) for g in (-2.51, -2.5, -2.49)]
    gain = quad(d, -2.51, -2.49, epsabs=1e-14)[0]
    print("QP" if qp else "PQ", "diff at script g1 -1.51/-1.5/-1.49:", ["%.6e" % v for v in vals], " gain over [-1.51,-1.49]: %.6e" % gain)
    print("  control at the write-up's point (PQ g1 -2 -> here -3; QP g1 -1.5 -> -2.5): %.6e" % (d(-3.0) if not qp else d(-2.5)))
