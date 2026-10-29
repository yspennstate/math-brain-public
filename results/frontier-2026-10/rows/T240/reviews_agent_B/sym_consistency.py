# symmetric_driver (used for the defect value, Jacobian and trap log norm) vs the 4-variable full_driver slice (sym4, used
# for g, its derivatives and the trap residual), and iv_h2's Hessians vs finite differences of the float closed form.
import sys; sys.path[:0] = ['scripts']
from fractions import Fraction as F
from iv_exact import I, S
import iv_scm, iv_h2, entry_eta as E, numpy as np, check_symmetric_closed as cs
mid = lambda v: float(F(v.lo + v.hi, 2 * S))
E.setup('1/2', '1/5000')
for x in [(F(1), F(0), F(0)), (F(3, 5), F(1, 5), F(3, 10)), (F(37, 100), F(33, 100), F(41, 100))]:
    eta = F(2501, 5000)
    a = iv_scm.symmetric_driver([I.of(v) for v in x], I.of(eta)); b = E.sym4([I.of(v) for v in x], I.of(eta))
    dv = max(abs(mid(a[i].v) - mid(b[i].v)) for i in range(3)); dd = max(abs(mid(a[i].d[j]) - mid(b[i].d[j])) for i in range(3) for j in range(3))
    fe = lambda e: cs.closed(*map(float, x), e)[3:]
    feta = (fe(float(eta) + 1e-6) - fe(float(eta) - 1e-6)) / 2e-6
    de = max(abs(mid(b[i].d[3]) - feta[i]) for i in range(3))
    h4 = E.sym4_h2([I.of(v) for v in x], I.of(eta))
    xf = np.array([float(v) for v in x]); hh = 1e-4
    def f4(z): return cs.closed(z[0], z[1], z[2], z[3])[3:]
    z0 = np.array([*xf, float(eta)]); Hfd = np.zeros((3, 4, 4))
    for p in range(4):
        for q in range(4):
            ep = np.eye(4)[p] * hh; eq = np.eye(4)[q] * hh
            Hfd[:, p, q] = (f4(z0 + ep + eq) - f4(z0 + ep - eq) - f4(z0 - ep + eq) + f4(z0 - ep - eq)) / (4 * hh * hh)
    dh = max(abs(mid(h4[i].h[p][q]) - Hfd[i, p, q]) for i in range(3) for p in range(4) for q in range(4))
    h3 = iv_h2.symmetric_driver([I.of(v) for v in x], I.of(eta))
    dh3 = max(abs(mid(h3[i].h[p][q]) - mid(h4[i].h[p][q])) for i in range(3) for p in range(3) for q in range(3))
    print([float(v) for v in x], 'value diff %.2e  f_x diff %.2e  f_eta vs fd %.2e  4-var hessian vs fd %.2e  3-var vs 4-var hessian %.2e' % (dv, dd, de, dh, dh3))
