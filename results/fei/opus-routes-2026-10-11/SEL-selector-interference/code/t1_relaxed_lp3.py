"""Relaxed T1-half-sharp for m = 3 cells: sup over laws of unit c in R^3 with E[c c^T] = diag(p) of
E[Phi(c)], Phi(c) = H(|sum_k c_k phi_k|^2) - H(c^2) - sum_k c_k^2 H(phi_k^2), phi_k = ahat_k/sqrt(p_k).
LP over sampled directions.  Report sup / B, B = sum p_k (1-p_k)."""
import numpy as np
from scipy.optimize import linprog
from fei_lib import fwht_float
def H(P):
    P = np.asarray(P); 
    with np.errstate(divide='ignore', invalid='ignore'):
        return np.where(P > 0, -P*np.log2(np.where(P > 0, P, 1)), 0.0).sum(axis=-1)
rng = np.random.default_rng(4)
for trial in range(8):
    a = 3; N = 8
    while True:
        lab = rng.integers(0, 3, size=N)
        if len(set(lab)) == 3: break
    p = np.array([np.mean(lab == k) for k in range(3)])
    phis = np.array([fwht_float((lab == k).astype(float))/N/np.sqrt(p[k]) for k in range(3)])   # 3 x N
    Hq = H(phis**2)
    # directions: random + near vertices
    C = rng.standard_normal((30000, 3)); C /= np.linalg.norm(C, axis=1, keepdims=True)
    V = []
    for k in range(3):
        for s in (1e-3, 3e-3, 1e-2, 3e-2, 0.1):
            D = np.zeros((400, 3)); D[:, k] = 1; D += s*rng.standard_normal((400, 3)); D /= np.linalg.norm(D, axis=1, keepdims=True); V.append(D)
    C = np.vstack([C] + V + [np.eye(3), -np.eye(3)])
    amp = C @ phis
    Phi = H(amp**2) - H(C**2) - (C**2) @ Hq
    rows = [np.ones(len(C))] + [C[:, i]*C[:, j] for i in range(3) for j in range(i, 3)]
    rhs = [1.0] + [p[i] if i == j else 0.0 for i in range(3) for j in range(i, 3)]
    r = linprog(-Phi, A_eq=np.array(rows), b_eq=np.array(rhs), bounds=(0, None), method='highs')
    B = np.sum(p*(1-p))
    print('cells', lab.tolist(), 'p', p, ' sup E[Phi] = %.5f  sup/B = %.3f  H(p) = %.3f' % (-r.fun, -r.fun/B, H(p)))
