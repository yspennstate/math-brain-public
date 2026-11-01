"""Finite regression check for QFORM-COMMONPLANE-SMALL-S3-LATENT-COMPLETION-v1.
The proof is algebraic; this script only checks constants/numerics on random examples.
"""
import math
import numpy as np

CE3 = 3 * 2 ** (4 / 3) * math.exp(1 / 3)
sigma2 = 0.000356312664981148
m2 = (63 / 64) * sigma2
eta = 1 / 512
print("C_E3", CE3)
print("m_*^2", m2)
print("paid_bound", 4 * CE3 / (m2 * eta))
print("stability_factor_at_eta", (73 / 9) * eta)

rng = np.random.default_rng(20260923)
worst_ratio = 0.0
checked = 0
for _ in range(5000):
    O, _ = np.linalg.qr(rng.normal(size=(2, 2)))
    vals = rng.uniform(0.5, 3.0, size=2) * rng.choice([-1.0, 1.0], size=2)
    S0 = O @ np.diag(vals) @ O.T
    I = np.eye(2)
    K0 = np.block([[S0, S0, I], [S0, S0, I], [I, I, np.linalg.inv(S0)]])

    # Preserve the two identity legs and perturb only D1,D2,D3,R.
    E1 = rng.normal(size=(2, 2)); E1 = (E1 + E1.T) / 2
    E2 = rng.normal(size=(2, 2)); E2 = (E2 + E2.T) / 2
    E3 = rng.normal(size=(2, 2)); E3 = (E3 + E3.T) / 2
    ER = rng.normal(size=(2, 2))
    scale = 10 ** rng.uniform(-6, -2)
    K = K0 + scale * np.block([[E1, ER, np.zeros((2,2))],
                               [ER.T, E2, np.zeros((2,2))],
                               [np.zeros((2,2)), np.zeros((2,2)), E3]])

    ew, U = np.linalg.eigh(K)
    keep = np.argsort(np.abs(ew))[-2:]
    L = U[:, keep] @ np.diag(ew[keep]) @ U[:, keep].T
    eps = np.linalg.svd(K, compute_uv=False)[2]
    if not (eps < 0.25):
        continue
    A = L[:2, 4:6]
    B = L[2:4, 4:6]
    H = L[4:6, 4:6]
    S = np.linalg.inv(H)
    R = K[:2, 2:4]
    KS = np.block([[S, S, I], [S, S, I], [I, I, np.linalg.inv(S)]])
    rhs = (73 / 9) * eps * (1 + np.linalg.norm(R, 2))
    ratio = np.linalg.norm(K - KS, 2) / rhs
    worst_ratio = max(worst_ratio, ratio)
    assert np.linalg.norm(S - R, 2) <= (28 / 9) * eps * (1 + np.linalg.norm(R, 2)) * (1 + 1e-8)
    assert ratio <= 1 + 1e-8
    checked += 1

print("checked", checked)
print("worst_ratio", worst_ratio)
