"""an agent: float corroboration of STRAT16 concavity (n=5, k=N-2>=5, incl. k->inf).
Own implementation of STRAT7 formula (5):
Q(E) = -2 tr E^2 + [2(k+2)/k - 4] B_E + 4 sum_i p_i (E^2)_ii - 2 p^T E d + mE/k^2 [-4k mE + 2(k+2) p^T d]
p_i=u_i^2, d=diag E, mE=tr E/2, B_E=sum_ij u_i u_j E_ij^2, E symmetric with E1=Eu=0.
For each random unit zero-sum u, the max over E of Q(E)/|E|^2 is the top eigenvalue of the 6x6 form in V (E=K V K^T).
Prints the worst (largest) value found; concavity predicts <= 0. Usage: python3 my_concavity_sample.py SAMPLES SEED
"""
import sys
import numpy as np
S = int(sys.argv[1]); rng = np.random.default_rng(int(sys.argv[2]))
n = 5
KS = [5.0, 6.0, 8.0, 20.0, 1e3, 1e9]

def Q(E, u, k):
    p = u * u; d = np.diag(E); m = np.trace(E) / 2; E2 = E @ E
    B = np.sum(np.outer(u, u) * E * E)
    return (-2 * np.trace(E2) + (2 * (k + 2) / k - 4) * B + 4 * np.sum(p * np.diag(E2))
            - 2 * p @ E @ d + m / k**2 * (-4 * k * m + 2 * (k + 2) * p @ d))

def basis(u):
    M = np.vstack([np.ones(n) / np.sqrt(n), u])
    _, _, Vt = np.linalg.svd(M)
    return Vt[2:].T  # n x 3 orthonormal basis of {1,u}^perp

sym = []
for i in range(3):
    for j in range(i, 3):
        A = np.zeros((3, 3)); A[i, j] = A[j, i] = 1.0 if i == j else 1 / np.sqrt(2); sym.append(A)

worst = {k: -np.inf for k in KS}; arg = {}
for s in range(S):
    mode = s % 3
    if mode == 0: u = rng.standard_normal(n)
    elif mode == 1: u = rng.standard_normal(n) * (rng.random(n) < 0.6)  # sparse-ish
    else: u = np.array([1, -1, 0, 0, 0], float) + 1e-3 * rng.standard_normal(n)  # near edge contrast
    u -= u.mean()
    if np.linalg.norm(u) < 1e-9: continue
    u /= np.linalg.norm(u)
    K = basis(u)
    Es = [K @ A @ K.T for A in sym]
    for k in KS:
        G = np.zeros((6, 6))
        for a in range(6):
            G[a, a] = Q(Es[a], u, k)
        for a in range(6):
            for b in range(a + 1, 6):
                G[a, b] = G[b, a] = (Q(Es[a] + Es[b], u, k) - G[a, a] - G[b, b]) / 2
        # E basis is orthonormal in Frobenius norm, so top eigenvalue = max Q/|E|^2
        lam = np.linalg.eigvalsh(G)[-1]
        if lam > worst[k]: worst[k] = lam; arg[k] = u.copy()
for k in KS:
    print('k=%g  max Q/|E|^2 = %.6g  at u=%s' % (k, worst[k], np.round(arg[k], 4)))
print('PASS (all <= 1e-9)' if all(v <= 1e-9 for v in worst.values()) else 'FAIL: a positive direction found')
