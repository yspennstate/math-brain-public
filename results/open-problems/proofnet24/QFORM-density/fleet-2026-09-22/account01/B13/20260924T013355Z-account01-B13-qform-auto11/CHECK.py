"""Finite diagnostics for account01/B13 20260924T013355Z.

These checks are not proofs. They verify the exact algebraic identities used in REPORT.md
on random finite Parseval two-frames.
"""
import numpy as np

rng = np.random.default_rng(20260924)

def det2(rows):
    return np.linalg.det(np.asarray(rows, dtype=float))

for trial in range(50):
    n = int(rng.integers(5, 12))
    G = rng.normal(size=(n, 2))
    U, _ = np.linalg.qr(G)
    # U has orthonormal columns.
    q = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            q[i, j] = q[j, i] = det2(U[[i, j], :]) ** 2

    # Cauchy--Binet on a random subset.
    mask = rng.random(n) < 0.6
    S = np.flatnonzero(mask)
    if len(S) >= 2:
        lhs = sum(q[i, j] for a, i in enumerate(S) for j in S[a+1:])
        rhs = np.linalg.det(U[S, :].T @ U[S, :])
        assert abs(lhs - rhs) < 2e-12

    # Parseval wedge identity.
    for i in range(n):
        lhs = q[i, :].sum()
        rhs = float(U[i, :] @ U[i, :])
        assert abs(lhs - rhs) < 2e-12

    # Cross determinant factorization for A=D+U Lambda U^T on disjoint pairs.
    L = rng.normal(size=(2, 2))
    Lam = (L + L.T) / 2
    if abs(np.linalg.det(Lam)) < 0.1:
        Lam += np.eye(2)
    D = np.diag(rng.normal(size=n))
    A = D + U @ Lam @ U.T
    ids = rng.choice(n, size=4, replace=False)
    E, F = ids[:2], ids[2:]
    lhs = np.linalg.det(A[np.ix_(E, F)])
    rhs = np.linalg.det(Lam) * np.linalg.det(U[E, :]) * np.linalg.det(U[F, :])
    assert abs(lhs - rhs) < 2e-11

    # Tau factorization after deterministic latent-frame alignment.
    k = int(rng.integers(n))
    uk = U[k].copy()
    c = float(uk @ uk)
    if c < 1e-10:
        continue
    e1 = uk / np.sqrt(c)
    e2 = np.array([-e1[1], e1[0]])
    R = np.column_stack([e1, e2])
    V = U @ R
    d = rng.normal(size=n)
    candidates = [i for i in range(n) if i != k and abs(V[i,1]) > 1e-7]
    if len(candidates) < 2:
        continue
    i, j = rng.choice(candidates, size=2, replace=False)
    x_i, y_i = V[i]
    x_j, y_j = V[j]
    s_i, s_j = y_i*y_i, y_j*y_j
    r_i, r_j = x_i/y_i, x_j/y_j
    qij = np.linalg.det(V[[i,j],:])**2
    qki = np.linalg.det(V[[k,i],:])**2
    qkj = np.linalg.det(V[[k,j],:])**2
    tau = d[k]*qij + d[i]*qkj + d[j]*qki
    rhs = s_i*s_j*(d[k]*(r_i-r_j)**2 + c*d[i]/s_i + c*d[j]/s_j)
    assert abs(tau-rhs) < 2e-10

print("all finite diagnostic identities passed")
