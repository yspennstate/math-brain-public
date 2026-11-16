"""an agent: NUMERICAL corroboration (not proof) for STRAT17's five-vertex double carrier with lower components.
Written from STRAT17/RESULT.md's functional, not from its code:
  T* = 2(trC - trC^2) + 2(trD - trD^2) + 2(k+2)B/k + X_k(M0+s/2, h) - Y,  T = T*/M^2,  M = M0 + s/2,
  B = sum P_ij A_ij^2 (A = I-C), h = sum P_ii C_ii, Y = 2 sum_{i<j} w_ij (P_ii+P_jj-2P_ij)(2-C_ii-C_jj-2w_ij),
  X_k(m,h) = (m-1)/k^2 [2(k+1)(k-2) - 4km + 2(k+2)h].
Top: C on 5 vertices with C u = u, C v = v (P = uu^T+vv^T, u,v orthonormal zero-sum), C <= I, Laplacian.
Parametrised A = J/5 + K G G^T K^T, K orthonormal basis of {1,u,v}^perp (2-dim), so A1=1, Au=Av=0, A psd hold exactly;
off-diagonal A >= 0 is an SLSQP inequality. Lowers: trace s in [0, k-4] (N>=7, at least one nontrivial lower), the
nonnegative spectral term 2(trD - trD^2) dropped (worst case). Usage: python3 my_double_lower_search.py STARTS SEED"""
import sys
import numpy as np
from scipy.optimize import minimize

S = int(sys.argv[1]); rng = np.random.default_rng(int(sys.argv[2]))
KS = [5.0, 6.0, 7.0, 10.0, 20.0, 1e6]
iu = np.triu_indices(5, 1)


def unpack(x):
    U = x[:10].reshape(5, 2); U = U - U.mean(0)
    Q, _ = np.linalg.qr(U)
    if np.linalg.matrix_rank(U, 1e-9) < 2:
        Q = np.linalg.qr(np.array([[1, 0], [-1, 0], [0, 1], [0, -1], [0, 0]], float))[0]
    P = Q @ Q.T
    M = np.column_stack([np.ones(5) / np.sqrt(5), Q])
    K = np.linalg.svd(M.T)[2][3:].T
    G = np.array([[x[10], 0.0], [x[11], x[12]]])
    A = np.ones((5, 5)) / 5 + K @ G @ G.T @ K.T
    return P, A


def Tval(y, k, with_s=True):
    x = y[:13]
    s = (k - 4) * (np.tanh(y[13]) + 1) / 2 if with_s else 0.0
    P, A = unpack(x)
    C = np.eye(5) - A
    trC = np.trace(C); M0 = trC / 2; m = M0 + s / 2
    h = np.sum(np.diag(P) * np.diag(C))
    B = np.sum(P * A * A)
    w = A[iu]; dC = np.diag(C); dP = np.diag(P)
    Y = 2 * np.sum(w * (dP[iu[0]] + dP[iu[1]] - 2 * P[iu]) * (2 - dC[iu[0]] - dC[iu[1]] - 2 * w))
    X = (m - 1) / k**2 * (2 * (k + 1) * (k - 2) - 4 * k * m + 2 * (k + 2) * h)
    Ts = 2 * (trC - np.trace(C @ C)) + 2 * (k + 2) * B / k + X - Y
    return Ts / m**2


cons = [{'type': 'ineq', 'fun': lambda y: unpack(y[:13])[1][iu]}]
for with_s in (False, True):
    print('--- %s ---' % ('lower trace s in [0,k-4], spectral term dropped' if with_s else 'isolates only (s=0), STRAT15 control'))
    for k in KS:
        best = (np.inf, None)
        for _ in range(S):
            y0 = np.concatenate([rng.standard_normal(10), 0.3 * rng.standard_normal(3), [3 * rng.standard_normal()]])
            r = minimize(Tval, y0, args=(k, with_s), method='SLSQP', constraints=cons,
                         options={'maxiter': 500, 'ftol': 1e-12})
            if (r.success or r.status in (8, 9)) and unpack(r.x[:13])[1][iu].min() > -1e-7 and r.fun < best[0]:
                best = (r.fun, r.x.copy())
        P, A = unpack(best[1][:13])
        s = (k - 4) * (np.tanh(best[1][13]) + 1) / 2 if with_s else 0.0
        print('k=%g  min T = %.6g  s=%.4g  trC=%.4f  edges=%d' % (k, best[0], s, 5 - np.trace(A), int((A[iu] > 1e-4).sum())))
