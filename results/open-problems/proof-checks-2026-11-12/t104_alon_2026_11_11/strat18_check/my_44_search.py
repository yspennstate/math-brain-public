"""an agent: independent NUMERICAL search for T<0 on split 4+4 with isolates and lower trace (written from
STRAT17 RESULT.md 'Formula and closures', not from Codex's algebra44.py). Each 4-vertex block: u unit zero-sum,
A = J/4 + K G G^T K^T (K basis of {1,u}^perp) so PSD, A1=1, Au=0 exact; entrywise A>=0 by SLSQP.
C = diag(I-A1, I-A2), P = uu^T (+) vv^T, M0 = trC/2, s = lower trace in [0,k-7], spectral term of lowers dropped.
Usage: python3 my_44_search.py STARTS SEED. Corroboration only, not proof."""
import sys
import numpy as np
from scipy.optimize import minimize
S = int(sys.argv[1]); rng = np.random.default_rng(int(sys.argv[2]))
iu4 = np.triu_indices(4, 1)

def block(x):
    u = x[:4] - x[:4].mean(); nu = np.linalg.norm(u)
    u = u / nu if nu > 1e-12 else np.array([1, -1, 0, 0]) / np.sqrt(2)
    K = np.linalg.svd(np.vstack([np.ones(4) / 2, u]))[2][2:].T
    G = np.zeros((2, 2)); G[np.tril_indices(2)] = x[4:7]
    return u, np.ones((4, 4)) / 4 + K @ G @ G.T @ K.T

def parts(y, k, lowers):
    u, A1 = block(y[:7]); v, A2 = block(y[7:14])
    s = (k - 7) * (np.tanh(y[14]) + 1) / 2 if lowers else 0.0
    return u, A1, v, A2, s

def T(y, k, lowers):
    u, A1, v, A2, s = parts(y, k, lowers)
    trc = trB = h = Y = Bs = 0.0
    for z, A in ((u, A1), (v, A2)):
        C = np.eye(4) - A; dC = np.diag(C)
        trc += 2 * (np.trace(C) - np.trace(C @ C))
        Bs += np.sum(np.outer(z, z) * A * A)
        h += np.sum(z * z * dC)
        w = A[iu4]; i, j = iu4
        Y += 2 * np.sum(w * (z[i] - z[j]) ** 2 * (2 - dC[i] - dC[j] - 2 * w))
        trB += np.trace(C)
    M = trB / 2 + s / 2
    X = (M - 1) / k**2 * (2 * (k + 1) * (k - 2) - 4 * k * M + 2 * (k + 2) * h)
    return (trc + 2 * (k + 2) * Bs / k + X - Y) / M**2

def cons(y):
    _, A1, _, A2, _ = parts(y, 8.0, False)
    return np.concatenate([A1[iu4], A2[iu4], np.diag(A1), np.diag(A2)])

for lowers in (False, True):
    for k in ([6.0, 7.0, 8.0, 10.0, 20.0, 1e6] if not lowers else [7.0, 8.0, 10.0, 20.0, 1e6]):
        best = (np.inf, None)
        for _ in range(S):
            y0 = np.concatenate([rng.standard_normal(4), 0.4 * rng.standard_normal(3),
                                 rng.standard_normal(4), 0.4 * rng.standard_normal(3), rng.standard_normal(1)])
            r = minimize(T, y0, args=(k, lowers), method='SLSQP', constraints=[{'type': 'ineq', 'fun': cons}],
                         options={'maxiter': 500, 'ftol': 1e-13})
            if (r.success or r.status in (8, 9)) and cons(r.x).min() > -1e-7 and r.fun < best[0]:
                best = (r.fun, r.x.copy())
        u, A1, v, A2, s = parts(best[1], k, lowers)
        print('lowers=%s k=%g min T=%.6g s=%.4f edges=%d+%d' % (lowers, k, best[0], s,
              int((A1[iu4] > 1e-4).sum()), int((A2[iu4] > 1e-4).sum())), flush=True)
        print('   w1=', np.round(A1[iu4], 4), ' w2=', np.round(A2[iu4], 4), flush=True)
