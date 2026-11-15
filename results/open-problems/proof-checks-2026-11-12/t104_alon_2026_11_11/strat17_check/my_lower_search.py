"""an agent: independent NUMERICAL minimum search for T on the STRAT16 2+5 class (written from RESULT.md formula (1),
not from algebra.py). Domain: u unit zero-sum in R^5; A in K_u = {A sym PSD, A >= 0 entrywise, A1 = 1, Au = 0};
C = I - A, w_ij = A_ij (i != j). Parametrised A = J/5 + K G G^T K^T (K orthonormal basis of {1,u}^perp), so PSD, A1=1,
Au=0 hold exactly; entrywise A >= 0 is an SLSQP inequality. Objective T = T*/M^2. Prints min found per k.
Usage: python3 my_min_search.py STARTS SEED. Corroboration only, not proof."""
import sys
import numpy as np
from scipy.optimize import minimize

S = int(sys.argv[1]); rng = np.random.default_rng(int(sys.argv[2]))
KS = [7.0, 8.0, 10.0, 20.0, 1e6]
iu = np.triu_indices(5, 1)


def unpack(x):
    u = x[:5] - x[:5].mean(); nu = np.linalg.norm(u)
    u = u / nu if nu > 1e-12 else np.array([1, -1, 0, 0, 0]) / np.sqrt(2)
    M = np.vstack([np.ones(5) / np.sqrt(5), u])
    K = np.linalg.svd(M)[2][2:].T
    G = np.zeros((3, 3)); G[np.tril_indices(3)] = x[5:]
    A = np.ones((5, 5)) / 5 + K @ G @ G.T @ K.T
    return u, A


def Tval(x, k):
    u, A = unpack(x)
    C = np.eye(5) - A
    trC = np.trace(C); M = (1 + trC) / 2
    h = 0.5 + np.sum(u * u * np.diag(C))
    B = np.sum(np.outer(u, u) * A * A)
    w = A[iu]; dC = np.diag(C)
    Y = 2 * np.sum(w * (u[iu[0]] - u[iu[1]]) ** 2 * (2 - dC[iu[0]] - dC[iu[1]] - 2 * w))
    Ts = (2 * (trC - np.trace(C @ C)) + 2 * (k + 2) * B / k
          + (M - 1) / k**2 * (2 * (k + 1) * (k - 2) - 4 * k * M + 2 * (k + 2) * h) - Y)
    return Ts / M**2


def cons(x):
    return unpack(x)[1][iu]  # off-diagonal >= 0 (diagonal of A is >= 0 automatically? enforce too)


def cons_diag(x):
    return np.diag(unpack(x)[1])


for k in KS:
    best = (np.inf, None)
    for s in range(S):
        x0 = np.concatenate([rng.standard_normal(5), 0.3 * rng.standard_normal(6)])
        r = minimize(Tval, x0, args=(k,), method='SLSQP',
                     constraints=[{'type': 'ineq', 'fun': cons}, {'type': 'ineq', 'fun': cons_diag}],
                     options={'maxiter': 400, 'ftol': 1e-12})
        if r.success or r.status in (8, 9):
            u, A = unpack(r.x)
            if A[iu].min() > -1e-7 and r.fun < best[0]:
                best = (r.fun, r.x.copy())
    u, A = unpack(best[1])
    print('k=%g  min T = %.6g  edges(w>1e-4)=%d  u=%s' % (k, best[0], int((A[iu] > 1e-4).sum()), np.round(u, 3)))
    print('   A offdiag =', np.round(A[iu], 4), ' rank(A-J/5) =', np.linalg.matrix_rank(A - np.ones((5, 5)) / 5, 1e-6))


# an agent STRAT17 check: lower components add trace s to M (s in [0, k-6] for N>=9) and a nonnegative
# spectral term 2*sum mu(1-mu), dropped here (worst case). Minimise T*(x, s) / (M+s/2)^2 jointly over the 2+5 top and s.
def Tlow(y, k):
    x, t = y[:-1], y[-1]
    s = (k - 6) * (np.tanh(t) + 1) / 2
    u, A = unpack(x)
    C = np.eye(5) - A
    trC = np.trace(C); M = (1 + trC) / 2 + s / 2
    h = 0.5 + np.sum(u * u * np.diag(C))
    B = np.sum(np.outer(u, u) * A * A)
    w = A[iu]; dC = np.diag(C)
    Y = 2 * np.sum(w * (u[iu[0]] - u[iu[1]]) ** 2 * (2 - dC[iu[0]] - dC[iu[1]] - 2 * w))
    Ts = (2 * (trC - np.trace(C @ C)) + 2 * (k + 2) * B / k
          + (M - 1) / k**2 * (2 * (k + 1) * (k - 2) - 4 * k * M + 2 * (k + 2) * h) - Y)
    return Ts / M**2


print('--- with lower trace s in [0,k-6], spectral term dropped ---')
for k in KS:
    best = (np.inf, None)
    for s_ in range(S):
        y0 = np.concatenate([rng.standard_normal(5), 0.3 * rng.standard_normal(6), [3 * rng.standard_normal()]])
        r = minimize(Tlow, y0, args=(k,), method='SLSQP',
                     constraints=[{'type': 'ineq', 'fun': lambda y: cons(y[:-1])},
                                  {'type': 'ineq', 'fun': lambda y: cons_diag(y[:-1])}],
                     options={'maxiter': 400, 'ftol': 1e-12})
        if r.success or r.status in (8, 9):
            u, A = unpack(r.x[:-1])
            if A[iu].min() > -1e-7 and r.fun < best[0]:
                best = (r.fun, r.x.copy())
    s = (k - 6) * (np.tanh(best[1][-1]) + 1) / 2
    print('k=%g  min T = %.6g at s=%.4g (k-6=%g)' % (k, best[0], s, k - 6))
