# agent C, 19 Oct: pointwise independent check of the sigma 2 and sigma 0.5 certificates (cert_kl_arb_sigma.py,
# cert_renyi_arb_sigma.py): scipy value of SAME - ANTI at each certified script g1 must be >= the certified min lower end.
import numpy as np
from scipy.integrate import quad
from scipy.special import logsumexp
def run(S, kind, qp, sg, lower):
    lN = lambda x, m: -(x - m) ** 2 / (2 * S * S) - 0.5 * np.log(2 * np.pi * S * S)
    g1 = sg - 1
    def F(same):
        a, c = (0, -1) if same else (2, 1)
        def f(z):
            lp = logsumexp([lN(g1, -2) + lN(z, 0), lN(g1, 0) + lN(z, a)]) - np.log(2)
            lq = logsumexp([lN(g1, -1) + lN(z, 0), lN(g1, 0) + lN(z, c)]) - np.log(2)
            if qp: lp, lq = lq, lp
            return np.exp(lp) * (lp - lq) if kind == "KL" else np.exp(kind * lp + (1 - kind) * lq)
        pts = sorted(set([-2, -1, 0, 1, 2, 3] + [k * S for k in (-6, -3, 3, 6)]))
        return quad(f, -40 * S - 6, 40 * S + 6, points=pts, limit=1000, epsabs=0, epsrel=1e-13)
    (s, es), (t, et) = F(True), F(False)
    v = s - t
    print("sigma %s %s %s g1 %s: SAME-ANTI %.6e (quad err %.1e)  certified min lower %.4e  %s" % (
        S, kind, "QP" if qp else "PQ", sg, v, es + et, lower, "OK" if v - es - et >= lower else "CHECK"), flush=True)
for args in [(0.5, "KL", False, -1.4, 9.3520e-8), (0.5, "KL", True, -1.0, 5.5837e-7),
             (2.0, 2, False, -3.0, 1.5562e-3), (2.0, 3, False, -3.0, 6.6936e-3), (2.0, 2, True, -1.0, 2.1155e-3), (2.0, 3, True, -1.0, 9.2663e-3),
             (0.5, 2, False, -1.9, 3.3736e-7), (0.5, 3, False, -2.35, 1.2981e-5), (0.5, 2, True, -0.5, 1.4407e-3), (0.5, 3, True, -0.5, 0.23973)]:
    run(*args)
