# agent C, 19 Oct: independent check of cert_kl_arb_sigma.py at sigma 2 (unshifted construction, every
# Gaussian N(., mu, s^2); script g1 = construction g1 + 1).
import numpy as np
from scipy.integrate import quad
from scipy.special import logsumexp
S = 2.0
lN = lambda x, m: -(x - m) ** 2 / (2 * S * S) - 0.5 * np.log(2 * np.pi * S * S)
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
    return quad(f, -80, 80, points=[-6, 0, 6], limit=400, epsabs=1e-15, epsrel=1e-12)[0]
for qp, cert in ((False, 1.442e-5), (True, 1.484e-5)):
    d = lambda s: K(s - 1, True, qp) - K(s - 1, False, qp)
    g = quad(d, -2.01, -1.99, epsabs=1e-14)[0]
    print("QP" if qp else "PQ", "control at script g1 -2: %.6e  ends %.6e %.6e  true gain %.6e  certified >= %g  %s" % (
        d(-2.0), d(-2.01), d(-1.99), g, cert, "OK" if g >= cert else "VIOLATION"))
