# agent C, 19 Oct: independent check of cert_renyi_int_arb.py (P||Q) and cert_renyi_qp_arb.py (Q||P) - J(g1) =
# int p^alpha q^(1-alpha) dg2 from the UNSHIFTED construction (see kl_indep_scipy.py), log-sum-exp, scipy quad.
import numpy as np, sys
from scipy.integrate import quad
from scipy.special import logsumexp
lN = lambda x, m: -(x - m) ** 2 / 2 - 0.5 * np.log(2 * np.pi)
def lpq(g1, z, same):
    a, c = (0, -1) if same else (2, 1)
    lp = logsumexp([lN(g1, -2) + lN(z, 0), lN(g1, 0) + lN(z, a)]) - np.log(2)
    lq = logsumexp([lN(g1, -1) + lN(z, 0), lN(g1, 0) + lN(z, c)]) - np.log(2)
    return lp, lq
def J(g1, same, qp, al):
    def f(z):
        lp, lq = lpq(g1, z, same)
        if qp: lp, lq = lq, lp
        return np.exp(al * lp + (1 - al) * lq)
    return quad(f, -40, 40, points=[-6, -3, 0, 3, 6], limit=400, epsabs=1e-16, epsrel=1e-12)[0]
# (direction, order, script interval) - script g1 = construction g1 + 1; cert lower bounds from the write-up
cases = [("PQ", 2, -2.01, -1.99, None), ("PQ", 3, -2.21, -2.19, 2.2074e-4), ("PQ", 4, -3.01, -2.99, 1.3960e-3),
         ("PQ", 5, -3.502, -3.498, 3.7922e-3), ("QP", 2, -0.6, -0.4, 1.582e-3), ("QP", 3, 0.4, 0.6, 0.15034)]
for d, al, a, b, cert in cases:
    qp = d == "QP"
    diff = lambda s: J(s - 1, True, qp, al) - J(s - 1, False, qp, al)
    g = quad(diff, a, b, epsabs=1e-14)[0]
    print("%s order %d [%g,%g]: diff ends %.6e %.6e  mid %.6e  true gain %.6e  certified >= %s  %s" % (
        d, al, a, b, diff(a), diff(b), diff((a + b) / 2), g, cert, "" if cert is None else ("OK" if g >= cert else "VIOLATION")), flush=True)
print("control order 2 PQ at script g1 -2 (write-up 1.80412e-3): %.6e" % (J(-3, True, False, 2) - J(-3, False, False, 2)))
print("control order 2 QP at script g1 -1 (write-up J_SAME 0.102224949, J_ANTI 0.098766951, unscaled weights): %.9f %.9f" % (
    J(-2, True, True, 2), J(-2, False, True, 2)))
