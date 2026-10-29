import sys; sys.path[:0]=['.']
from fractions import Fraction as F
import c9_cone, numpy as np
from c9_flow import matvec, I
xs = c9_cone.plateau_float()
P, Pinv, par, w = c9_cone.adapted_frame(xs)
for rho in [F(4,10**10), F(2,10**10), F(1,10**10)]:
    ok, X, xc = c9_cone.krawczyk(xs, rho)
    if not ok: print(float(rho), 'FAIL'); continue
    zo = matvec(Pinv, [X[i] - I.of(xc[i]) for i in range(7)])
    print(float(rho), 'OK width', max(float(F(v.hi - v.lo, 2**160)) for v in X), 'zo', ['%.2e' % float(F(v.maxabs(), 2**160)) for v in zo], flush=True)
