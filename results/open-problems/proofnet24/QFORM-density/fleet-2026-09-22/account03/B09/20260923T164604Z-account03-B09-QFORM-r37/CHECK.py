import json
import math
import numpy as np

rng = np.random.default_rng(370923)
max_rel = 0.0
for _ in range(100):
    nt = 8
    ns = 7
    B = rng.normal(size=(2, nt))
    while np.linalg.matrix_rank(B) < 2:
        B = rng.normal(size=(2, nt))
    D = rng.normal(size=(ns, nt))
    Delta = float(np.linalg.det(B @ B.T))
    Pi = B.T @ np.linalg.inv(B @ B.T) @ B
    C = D @ (np.eye(nt) - Pi)
    V_projected = Delta * float(np.sum(C * C))
    V_cb = 0.0
    for k in range(ns):
        N = np.vstack([B, D[k]])
        V_cb += float(np.linalg.det(N @ N.T))
    rel = abs(V_projected - V_cb) / max(1.0, abs(V_projected), abs(V_cb))
    max_rel = max(max_rel, rel)

C_diffuse = 3 * 2 ** (5 / 6)
C_concentrated = 3 * math.sqrt(2) * 2 ** (1 / 6)
C_r35_Gstar = C_diffuse * (400 / 27) ** (1 / 6)

eps = 1 / 16
M = np.diag([1.0, 1.0, 1.0, eps])
A = np.block([[np.zeros((4, 4)), M], [M, np.zeros((4, 4))]])
eigs = np.linalg.eigvalsh(A)

out = {
    "trials": 100,
    "max_relative_identity_error": max_rel,
    "C_diffuse": C_diffuse,
    "C_concentrated": C_concentrated,
    "C_r35_Gstar": C_r35_Gstar,
    "stress_eps": eps,
    "stress_spectrum": eigs.tolist(),
    "stress_full_range_max_leverage": 1.0,
    "partner_det_K": 1.0,
    "partner_bound": 3.0,
}
print(json.dumps(out, indent=2))
