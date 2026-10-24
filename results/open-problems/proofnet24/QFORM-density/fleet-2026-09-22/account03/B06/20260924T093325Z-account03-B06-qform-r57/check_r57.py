import numpy as np

rng = np.random.default_rng(0)
max_err = 0.0
count = 0
for _ in range(10000):
    M = rng.normal(size=(3, 3))
    B = (M + M.T) / 2
    if abs(np.linalg.det(B)) < 0.1:
        continue
    w = rng.normal(size=3)
    w /= np.linalg.norm(w)
    if np.min(np.abs(w)) < 0.05:
        continue
    d = -(B @ w) / w
    F = B + np.diag(d)
    u = B @ w
    n = u / np.linalg.norm(u)

    # Build an orthonormal basis of n^perp and an arbitrary two-plane tail bank.
    seed = np.column_stack([n, rng.normal(size=(3, 2))])
    Q, _ = np.linalg.qr(seed)
    basis = Q[:, 1:3]
    Z = basis @ rng.normal(size=(2, 7))

    assert np.linalg.norm(F @ w) < 1e-8
    assert np.linalg.norm(Z.T @ B @ w) < 1e-8

    evals = np.linalg.eigvalsh(Z @ Z.T)
    W = evals[-1] * evals[-2]
    for i in range(3):
        jk = [j for j in range(3) if j != i]
        L = np.column_stack([np.eye(3)[:, jk[0]], np.eye(3)[:, jk[1]], Z])
        G = L @ L.T
        lhs = np.linalg.det(G)
        rhs = np.linalg.norm(Z.T @ np.eye(3)[:, i]) ** 2 + (1 - n[i] ** 2) * W
        err = abs(lhs - rhs) / (1 + abs(lhs) + abs(rhs))
        max_err = max(max_err, err)
        count += 1

print("QFORM_B06_R57_CHECK_PASS", count, max_err)
