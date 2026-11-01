"""Integrated 2-norm log norm of the merged block over t 320..400 for fixed diagonal scalings of its orthonormal basis."""
import json
import numpy as np
from c9_flow import *
import c9_cluster
ref = json.load(open('ref_T820_W0.004_U99o10000000_h0.5.json'))
tq = [float(F(v)) for v in ref['tq']]
ln = lambda A: float(np.max(np.linalg.eigvalsh((A + A.T) / 2)))
ks = [k for k in range(len(tq) - 1) if 320 <= tq[k] <= 400][::4]
Bs = []
for k in ks:
    J = np.array(fdrive.jac(fl([F(v) for v in ref['nodes'][k]]), ETA_F), float)
    P, blocks = c9_cluster.frame_c(J)
    M = np.linalg.solve(P, J @ P)
    b = [bb for bb in blocks if len(bb) == 3]
    Bs.append((tq[k], M[np.ix_(b[0], b[0])] if b else None))
for s in ([1, 1, 1], [1, 1.4, 0.6], [1, 1.7, 0.5], [1, 2, 0.4], [1, 2, 0.25]):
    D = np.diag(s); Di = np.diag(1 / np.array(s, float))
    tot = 0.0; mx = -9
    for (t0, B), (t1, _) in zip(Bs, Bs[1:]):
        if B is None: continue
        l = ln(Di @ B @ D); tot += l * (t1 - t0); mx = max(mx, l)
    print(s, 'integral %.3f' % tot, 'max %+.4f' % mx, 'nodes', len(Bs))
