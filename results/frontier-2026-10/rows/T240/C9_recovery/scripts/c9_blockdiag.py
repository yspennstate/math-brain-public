"""Diagnostic (float only): per clustered block, spectral abscissa vs 2-norm log norm of the block of P^-1 J P, and the
same after a balancing change of basis inside each block (real Schur + diagonal scaling). Prints numbers only."""
import json
import sys
import numpy as np
import scipy.linalg as sl
from c9_flow import *
import c9_cluster

ref = json.load(open('ref_T820_W0.004_U99o10000000_h0.5.json'))
tq = [float(F(v)) for v in ref['tq']]


def lognorm(A):
    return float(np.max(np.linalg.eigvalsh((A + A.T) / 2)))


def balanced(B, eps):
    T, Z = sl.schur(B, output='real')
    k = T.shape[0]
    s = np.array([eps ** i for i in range(k)])
    return np.diag(1 / s) @ T @ np.diag(s), np.linalg.cond(Z @ np.diag(s))


for k in [int(a) for a in sys.argv[1:]]:
    J = np.array(fdrive.jac(fl([F(v) for v in ref['nodes'][k]]), ETA_F), float)
    P, blocks = c9_cluster.frame_c(J)
    M = np.linalg.solve(P, J @ P)
    out = []
    for b in blocks:
        B = M[np.ix_(b, b)]
        ab = max(np.linalg.eigvals(B).real)
        row = 'n%d abs %+.4f ln %+.4f' % (len(b), ab, lognorm(B))
        if len(b) > 1:
            for eps in (0.3, 0.1, 0.03):
                Bb, c = balanced(B, eps)
                row += ' | e%.2f ln %+.4f cond %.0f' % (eps, lognorm(Bb), c)
        out.append(row)
    off = max(np.linalg.norm(M[np.ix_(a, c)]) for a in blocks for c in blocks if a != c)
    print('k', k, 't %.1f' % tq[k], 'cond(P) %.1f' % np.linalg.cond(P), 'max off %.4f' % off)
    for r in out:
        print('   ', r)
