"""an agent: independent NUMERICAL search for T<0 on split 4+5 with isolates and lower trace (generalised from
my_44_search.py, written from the STRAT17/18 RESULT.md formula, not from Codex's STRAT20 code). Each n-vertex block:
u unit zero-sum, A = J/n + K G G^T K^T (K basis of {1,u}^perp) so PSD, A1=1, Au=0 exact; entrywise A>=0 by SLSQP.
C = diag(I-A4, I-A5), P = uu^T (+) vv^T, M0 = trC/2, s = lower trace in [0,k-8], spectral term of lowers dropped.
Also prints the K4+K5 fixture at k=7 (Codex: T = 99/2401) as a check that this formula is the same functional.
Usage: python3 my_35_search.py STARTS SEED. Corroboration only, not proof."""
import sys
import numpy as np
from scipy.optimize import minimize
S = int(sys.argv[1]); rng = np.random.default_rng(int(sys.argv[2]))
SIZES = (4, 5)
NP = [n + (n - 2) * (n - 1) // 2 for n in SIZES]   # u entries + lower-triangular G entries

def block(x, n):
    u = x[:n] - x[:n].mean(); nu = np.linalg.norm(u)
    if nu < 1e-12:
        u = np.zeros(n); u[0], u[1] = 1, -1
        nu = np.sqrt(2)
    u = u / nu
    K = np.linalg.svd(np.vstack([np.ones(n) / np.sqrt(n), u]))[2][2:].T
    G = np.zeros((n - 2, n - 2)); G[np.tril_indices(n - 2)] = x[n:]
    return u, np.ones((n, n)) / n + K @ G @ G.T @ K.T

def parts(y, k, lowers):
    u, A1 = block(y[:NP[0]], SIZES[0]); v, A2 = block(y[NP[0]:NP[0] + NP[1]], SIZES[1])
    s = (k - 8) * (np.tanh(y[-1]) + 1) / 2 if lowers else 0.0
    return u, A1, v, A2, s

def Tval(blocks, k, s):
    trc = Bs = h = Y = trC = 0.0
    for z, A in blocks:
        n = len(z); iu = np.triu_indices(n, 1)
        C = np.eye(n) - A; dC = np.diag(C)
        trc += 2 * (np.trace(C) - np.trace(C @ C))
        Bs += np.sum(np.outer(z, z) * A * A)
        h += np.sum(z * z * dC)
        w = A[iu]; i, j = iu
        Y += 2 * np.sum(w * (z[i] - z[j]) ** 2 * (2 - dC[i] - dC[j] - 2 * w))
        trC += np.trace(C)
    M = trC / 2 + s / 2
    X = (M - 1) / k**2 * (2 * (k + 1) * (k - 2) - 4 * k * M + 2 * (k + 2) * h)
    return (trc + 2 * (k + 2) * Bs / k + X - Y) / M**2

def T(y, k, lowers):
    u, A1, v, A2, s = parts(y, k, lowers)
    return Tval(((u, A1), (v, A2)), k, s)

def cons(y):
    _, A1, _, A2, _ = parts(y, 8.0, False)
    return np.concatenate([A1[np.triu_indices(4, 1)], A2[np.triu_indices(5, 1)], np.diag(A1), np.diag(A2)])

# fixture: K4 + K5, any unit zero-sum selected vectors (A = J/n)
u3 = np.array([1, -1, 0, 0]) / np.sqrt(2); u5 = np.array([1, -1, 0, 0, 0]) / np.sqrt(2)
for k in (7.0, 1e9):
    print('fixture K4+K5 k=%g T=%.10f (Codex N9: 99/2401=%.10f, infinity 20/49=%.10f)' % (
        k, Tval(((u3, np.ones((4, 4)) / 4), (u5, np.ones((5, 5)) / 5)), k, 0.0), 99 / 2401, 20 / 49), flush=True)

for lowers in (False, True):
    for k in ([7.0, 8.0, 9.0, 11.0, 20.0, 1e6] if not lowers else [9.0, 10.0, 11.0, 20.0, 1e6]):
        best = (np.inf, None)
        for _ in range(S):
            y0 = np.concatenate([rng.standard_normal(4), 0.4 * rng.standard_normal(NP[0] - 4),
                                 rng.standard_normal(5), 0.4 * rng.standard_normal(NP[1] - 5), rng.standard_normal(1)])
            r = minimize(T, y0, args=(k, lowers), method='SLSQP', constraints=[{'type': 'ineq', 'fun': cons}],
                         options={'maxiter': 500, 'ftol': 1e-13})
            if (r.success or r.status in (8, 9)) and cons(r.x).min() > -1e-7 and r.fun < best[0]:
                best = (r.fun, r.x.copy())
        u, A1, v, A2, s = parts(best[1], k, lowers)
        print('lowers=%s k=%g min T=%.6g s=%.4f edges=%d+%d' % (lowers, k, best[0], s,
              int((A1[np.triu_indices(4, 1)] > 1e-4).sum()), int((A2[np.triu_indices(5, 1)] > 1e-4).sum())), flush=True)
        print('   w1=', np.round(A1[np.triu_indices(4, 1)], 4), ' w2=', np.round(A2[np.triu_indices(5, 1)], 4), flush=True)
