# agent C, 20 Oct: independent check of cert_renyi_real_arb_sigma.py at sigma 1, orders 3/2 and 5/2, both directions.
# scipy quad in log-sum-exp form on the UNSHIFTED construction (script g1 = construction g1 + 1), as in sigma_points_indep.py.
# Prints SAME - ANTI at the interval ends and middle, the integrated true gain over the certified interval (must be >= the
# certified gain), and the scan controls.
import numpy as np
from scipy.integrate import quad
from scipy.special import logsumexp
S = 1.0
lN = lambda x, m: -(x - m) ** 2 / (2 * S * S) - 0.5 * np.log(2 * np.pi * S * S)
def J(sg, al, qp, same):
    g1 = sg - 1
    a, c = (0, -1) if same else (2, 1)
    def f(z):
        lp = logsumexp([lN(g1, -2) + lN(z, 0), lN(g1, 0) + lN(z, a)]) - np.log(2)
        lq = logsumexp([lN(g1, -1) + lN(z, 0), lN(g1, 0) + lN(z, c)]) - np.log(2)
        if qp: lp, lq = lq, lp
        return np.exp(al * lp + (1 - al) * lq)
    return quad(f, -46, 46, points=[-2, -1, 0, 1, 2, 3], limit=1000, epsabs=0, epsrel=1e-13)[0]
D = lambda sg, al, qp: J(sg, al, qp, True) - J(sg, al, qp, False)
for al, qp, a, b, minlo, gain in [(1.5, False, -1.51, -1.49, 4.5372e-4, 9.20947e-6), (2.5, False, -2.11, -2.09, 3.5292e-3, 7.14287e-5),
                                  (1.5, True, -0.51, -0.49, 1.0951e-3, 2.30495e-5), (2.5, True, -0.01, 0.01, 8.9638e-2, 1.80232e-3)]:
    ends = [D(x, al, qp) for x in (a, (a + b) / 2, b)]
    tg = quad(lambda x: D(x, al, qp), a, b, epsrel=1e-10)[0]
    print("alpha %g %s [%g, %g]: diff ends/mid %.5e %.5e %.5e | min end %.5e vs certified min lower %.4e %s | true gain %.6e vs certified %.6e %s" % (
        al, "QP" if qp else "PQ", a, b, ends[0], ends[2], ends[1], min(ends), minlo, "OK" if min(ends) >= minlo else "CHECK",
        tg, gain, "OK" if tg >= gain else "CHECK"), flush=True)
for al, qp, x, want in [(2.5, False, -2.1, 0.00528547), (2.5, False, -2.8, 0.00162283), (2.5, True, 0.0, 0.0906194), (2.5, True, -1.5, 0.000750686)]:
    print("scan control alpha %g %s g1 %g: %.8f (script %s)" % (al, "QP" if qp else "PQ", x, D(x, al, qp), want), flush=True)
