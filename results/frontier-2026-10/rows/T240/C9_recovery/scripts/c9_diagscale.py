"""Diagnostic (float only): best diagonal rescaling D of each multi-column block's orthonormal basis, lognorm(D^-1 B D)."""
import json, sys
import numpy as np
from scipy.optimize import minimize
from c9_flow import *
import c9_cluster
ref = json.load(open('ref_T820_W0.004_U99o10000000_h0.5.json'))
tq = [float(F(v)) for v in ref['tq']]
ln = lambda A: float(np.max(np.linalg.eigvalsh((A + A.T) / 2)))
Ds = {}
for k in [int(a) for a in sys.argv[1:]]:
    J = np.array(fdrive.jac(fl([F(v) for v in ref['nodes'][k]]), ETA_F), float)
    P, blocks = c9_cluster.frame_c(J)
    M = np.linalg.solve(P, J @ P)
    for b in blocks:
        if len(b) < 2: continue
        B = M[np.ix_(b, b)]
        f = lambda z: ln(np.diag(np.exp(-np.r_[0, z])) @ B @ np.diag(np.exp(np.r_[0, z])))
        best = min((minimize(f, z0, method='Nelder-Mead', options=dict(xatol=1e-6, fatol=1e-9, maxiter=4000)) for z0 in
                    [np.zeros(len(b) - 1), np.full(len(b) - 1, 1.0), np.full(len(b) - 1, -1.0)]), key=lambda r: r.fun)
        Ds[k] = best.x
        print('k', k, 't %.1f' % tq[k], 'n%d' % len(b), 'abs %+.4f' % max(np.linalg.eigvals(B).real), 'ln %+.4f' % ln(B),
              'diag-best %+.4f' % best.fun, 'scale', np.round(np.exp(np.r_[0, best.x]), 3).tolist())
ks = sorted(Ds)
for k in ks:   # fixed scaling from the first node, applied at the later ones
    pass
