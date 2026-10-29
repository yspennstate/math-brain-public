"""C9 local part: 7-dim Krawczyk enclosure of the plateau x*(eta) for eta in E, a teacher-swap adapted eigenframe P*,
and the cone lemma on N = {|u| <= U, |s| <= kappa U}.  Usage: python c9_cone.py U kappa [nsplit]"""
import sys, json
sys.path[:0] = ['.']
from fractions import Fraction as F
import numpy as np
from scipy.optimize import fsolve
from c9_flow import *

TAU = [0, 1, 2, 4, 3, 6, 5]          # teacher swap R_i1 <-> R_i2

def plateau_float():
    x0 = np.array([0.3677197, 0.3253855, 0.3677197] + [0.4143942] * 4)
    return fsolve(lambda z: fdrive.f(z, ETA_F), x0, xtol=1e-15)

def krawczyk(xs, rho):
    xc = [F(float(v)) for v in xs]
    Y = invert_rational([[F(float(v)) for v in row] for row in fdrive.jac(xs, ETA_F)])
    X = [I.of(c) + pm(rho) for c in xc]
    fc = f_point(xc); JX = jac_box(X)
    Kx = []
    for i in range(N):
        v = I.of(xc[i]) - sum((I.of(Y[i][l]) * fc[l] for l in range(N)), I.of(0))
        for j in range(N):
            mij = I.of(int(i == j)) - sum((I.of(Y[i][l]) * JX[l][j] for l in range(N)), I.of(0))
            v = v + mij * (X[j] - I.of(xc[j]))
        Kx.append(v)
    ok = all(X[i].lo < Kx[i].lo and Kx[i].hi < X[i].hi for i in range(N))
    return ok, Kx, xc

def adapted_frame(xs):
    w, V = np.linalg.eig(fdrive.jac(xs, ETA_F)); o = np.argsort(-w.real); w = w[o].real; V = np.real(V[:, o])
    cols = []; par = []
    for k in range(N):
        v = V[:, k] / np.linalg.norm(V[:, k]); vt = v[TAU]
        sgn = 1 if np.linalg.norm(v + vt) > np.linalg.norm(v - vt) else -1
        c = [F(float(u)) for u in v]
        c = [(c[i] + sgn * c[TAU[i]]) / 2 for i in range(N)]       # exactly even (+1) or odd (-1)
        cols.append(c); par.append(sgn)
    P = [[cols[b][a] for b in range(N)] for a in range(N)]
    return P, invert_rational(P), par, w

def cone(Xstar, P, Pinv, U, kappa, nsplit=1):
    """Worst-case cone and growth margins over N, split into nsplit pieces along u and each s axis is not split."""
    worst = None
    for a in range(nsplit):
        ua, ub = -U + 2 * U * F(a, nsplit), -U + 2 * U * F(a + 1, nsplit)
        Z = [iv(ua, ub)] + [pm(kappa * U)] * (N - 1)
        box = [Xstar[i] + sum((I.of(P[i][k]) * Z[k] for k in range(N)), I.of(0)) for i in range(N)]
        M = mm_iv_rat(mm_rat_iv(Pinv, jac_box(box)), P)
        muu = lo(M[0][0])
        mus = norm2_up([M[0][j] for j in range(1, N)])
        msu = norm2_up([M[i][0] for i in range(1, N)])
        mss = lognorm_up([[M[i][j] for j in range(1, N)] for i in range(1, N)])
        grow = muu - kappa * mus
        margin = kappa * grow - (mss * kappa + msu)
        rec = {'u': [float(ua), float(ub)], 'muu': float(muu), 'mus': float(mus), 'msu': float(msu), 'mss': float(mss),
               'grow': float(grow), 'margin': float(margin), 'grow_ex': grow, 'margin_ex': margin}
        if worst is None or margin < worst['margin_ex'] or grow < worst['grow_ex']:
            worst = rec if worst is None else {**rec, 'margin_ex': min(margin, worst['margin_ex']), 'grow_ex': min(grow, worst['grow_ex'])}
    return worst

if __name__ == '__main__':
    xs = plateau_float()
    ok, Xstar, xc = krawczyk(xs, F(1, 10 ** 9))
    print('krawczyk', ok, max(float(hi(v) - lo(v)) for v in Xstar))
    P, Pinv, par, w = adapted_frame(xs)
    print('parities', par, 'eig', np.round(w, 6))
    D = mm_iv_rat(mm_rat_iv(Pinv, jac_box([I.of(c) for c in xc])), P)
    print('offdiag max at x*', max(float(maxabs(D[i][j])) for i in range(N) for j in range(N) if i != j))
    for U in sys.argv[1].split(','):
        for kap in sys.argv[2].split(','):
            r = cone(Xstar, P, Pinv, F(U), F(kap), int(sys.argv[3]) if len(sys.argv) > 3 else 1)
            print(U, kap, {k: (round(v, 6) if isinstance(v, float) else v) for k, v in r.items() if not k.endswith('_ex')},
                  'OK' if r['margin_ex'] > 0 and r['grow_ex'] > 0 else 'FAIL')
