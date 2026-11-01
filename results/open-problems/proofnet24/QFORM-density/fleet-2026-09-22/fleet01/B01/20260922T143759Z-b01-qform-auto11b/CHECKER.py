import numpy as np

C_bank = 5 * 2 ** (-2/5) * 3 ** (3/5)
print(f"C_bank={C_bank:.15f}")

rng = np.random.default_rng(20260922)
max_theta_diff = 0.0
max_cb_diff = 0.0
for trial in range(5):
    m = 7
    U, _ = np.linalg.qr(rng.normal(size=(3, 3)))
    V, _ = np.linalg.qr(rng.normal(size=(m, 2)))
    s = np.array([1.3 + 0.1 * trial, 0.7 + 0.05 * trial])
    M = U[:, :2] @ np.diag(s) @ V.T
    nu = U[:, 2]
    B = rng.normal(size=(3, 3))
    B = (B + B.T) / 2
    S = M @ M.T
    a = nu @ B @ nu
    Delta2 = (s[0] * s[1]) ** 2

    adj = np.empty((3, 3))
    for i in range(3):
        for j in range(3):
            # adj(S)_{ij} is the (j,i)-cofactor.
            minor = np.delete(np.delete(S, j, axis=0), i, axis=1)
            adj[i, j] = ((-1) ** (i + j)) * np.linalg.det(minor)

    theta1 = abs(a) * Delta2
    theta2 = abs(np.trace(adj @ B))
    max_theta_diff = max(max_theta_diff, abs(theta1 - theta2))

    cb = 0.0
    for r1 in range(3):
        for r2 in range(r1 + 1, 3):
            for c1 in range(m):
                for c2 in range(c1 + 1, m):
                    cb += np.linalg.det(M[np.ix_([r1, r2], [c1, c2])]) ** 2
    max_cb_diff = max(max_cb_diff, abs(cb - Delta2))

print(f"max_theta_identity_error={max_theta_diff:.3e}")
print(f"max_cauchy_binet_error={max_cb_diff:.3e}")
assert max_theta_diff < 1e-12
assert max_cb_diff < 1e-12

for m in [2, 3, 5, 10, 100]:
    Delta = (m - 1) / m**2
    Theta = Delta**2
    bound = C_bank * Theta ** (-1/5)
    print(f"bank m={m} Delta={Delta:.12g} Theta={Theta:.12g} bound={bound:.12g}")

print("STATUS=PASS")
