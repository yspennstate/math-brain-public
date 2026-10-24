import math
import json
import numpy as np

m = 100
eps = 1e-2
delta = 1e-6

v = np.array([1.0, 1.0, 1.0]) / math.sqrt(3.0)
u1 = np.array([1.0, -1.0, 0.0]) / math.sqrt(2.0)
u2 = np.array([1.0, 1.0, -2.0]) / math.sqrt(6.0)
U = np.column_stack([u1, u2])

c1 = np.ones(m) / math.sqrt(m)
c2 = np.r_[np.ones(m // 2), -np.ones(m // 2)] / math.sqrt(m)
V = np.column_stack([c1, c2])
K = U @ V.T
B = eps * np.outer(u1, u1) + delta * np.outer(v, v)
A = np.block([[B, K], [K.T, np.zeros((m, m))]])

eigs = np.linalg.eigvalsh(A)
nonzero = eigs[np.abs(eigs) > 1e-10]

pair_max = 0.0
for i in range(m + 3):
    for j in range(i + 1, m + 3):
        det = A[i, i] * A[j, j] - A[i, j] ** 2
        pair_max = max(pair_max, abs(det))

# Delete center coordinate 3 (zero-based index 2), keeping physical hubs 1,2.
keep = [0, 1]
Kh = K[keep, :]
G = Kh @ Kh.T
Ginv = np.linalg.inv(G)
leverages = np.array([Kh[:, j] @ Ginv @ Kh[:, j] for j in range(m)])

sv = np.linalg.svd(K, compute_uv=False)
Delta = sv[0] * sv[1]
d = abs(v @ B @ v)
g = np.linalg.norm((np.eye(3) - np.outer(v, v)) @ (B @ v))
partner = (135 * math.e / 32) * (4 + max(0.0, math.log(math.sqrt(Delta) / d)))
hub = 4 * np.linalg.det(G) ** (-0.25)

out = {
    "m": m,
    "eps": eps,
    "delta": delta,
    "UtU_maxerr": float(np.max(np.abs(U.T @ U - np.eye(2)))),
    "VtV_maxerr": float(np.max(np.abs(V.T @ V - np.eye(2)))),
    "K_singular_values": sv.tolist(),
    "Delta": float(Delta),
    "nonzero_eigenvalues": nonzero.tolist(),
    "max_abs_diagonal": float(np.max(np.abs(np.diag(A)))),
    "max_abs_physical_pair_det": float(pair_max),
    "d": float(d),
    "g": float(g),
    "Gamma_selected": float(math.sqrt(np.linalg.det(G))),
    "max_leaf_leverage": float(leverages.max()),
    "Theorem_H_density_bound": float(hub),
    "partner_log_bound": float(partner),
}
print(json.dumps(out, indent=2))
