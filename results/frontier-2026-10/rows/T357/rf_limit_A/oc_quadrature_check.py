# Compare OC from rf_cgmt.py's Gauss-Hermite pop() with rf_ridge_inf.py's split-Legendre oc_fm at the same (q, c).
import math, numpy as np
sig = lambda t: 0.5 * (1 + np.tanh(t / 2))
for beta, q, rho in ((2.0, 1.4843, 0.8705), (5.0, 2.4844, 0.8705), (2.0, 1.47, 0.8704)):
    cz = rho * q
    for ng in (120, 400):
        gx, gw = np.polynomial.hermite_e.hermegauss(ng); gw = gw / gw.sum()
        s_ = q * gx; mu_ = (cz / q ** 2) * s_[:, None]; sd = math.sqrt(max(1 - cz ** 2 / q ** 2, 0))
        hx, hw = np.polynomial.hermite_e.hermegauss(120); hw = hw / hw.sum()
        ey = (sig(beta * (mu_ + sd * hx[None, :])) * hw[None, :]).sum(1); p = sig(s_)
        print(beta, q, 'GH', ng, 'OC %.6f' % ((p - ey) * np.sign(p - .5) * gw).sum())
    lx, lw = np.polynomial.legendre.leggauss(200); lx = 5 * (lx + 1); lw = 5 * lw * np.exp(-lx ** 2 / 2) / math.sqrt(2 * math.pi)
    ux = np.concatenate([-lx[::-1], lx]); uw = np.concatenate([lw[::-1], lw])
    mu = (cz / q) * ux; ey = (sig(beta * (mu[:, None] + sd * hx[None, :])) * hw[None, :]).sum(1); p = sig(q * ux)
    print(beta, q, 'Legendre split OC %.6f' % ((p - ey) * np.sign(ux) * uw).sum())
