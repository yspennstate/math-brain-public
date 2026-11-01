import math
import numpy as np

rng = np.random.default_rng(20260923)
mmax = 124
N = mmax * (mmax - 1) // 2
sigma = 1 / 480
S0 = sigma / math.sqrt(N)
zero_B_bound = 2 * math.sqrt(math.pi * math.e / S0)
definite_bound = math.pi / math.sqrt(S0)

max_coeff = 0.0
max_identity_residual = 0.0
min_E_over_s3 = float('inf')

for _ in range(200):
    m = int(rng.integers(3, 12))
    q = int(rng.integers(2, 15))
    C = rng.normal(size=(m, q))

    best = -1.0
    pair = None
    for i in range(m):
        for j in range(i + 1, m):
            area2 = np.linalg.det(C[[i, j]] @ C[[i, j]].T)
            if area2 > best:
                best = area2
                pair = (i, j)

    order = list(pair) + [k for k in range(m) if k not in pair]
    C = C[order]
    M = C[:2]
    G = M @ M.T
    P = M.T @ np.linalg.inv(G) @ M
    K = (C[2:] @ P) @ M.T @ np.linalg.inv(G)
    R = C[2:] - K @ M
    max_coeff = max(max_coeff, float(np.max(np.abs(K))))

    B = rng.normal(size=(2, 2))
    B = (B + B.T) / 2
    if abs(np.linalg.det(B)) < 0.15:
        B = B + np.diag([1.0, -0.7])
        if abs(np.linalg.det(B)) < 0.05:
            B = B + np.eye(2)

    AH = rng.normal(size=(m, m))
    AH = (AH + AH.T) / 2
    AH[:2, :2] = B
    D = rng.normal(size=(q, q))
    D = (D + D.T) / 2
    A = np.block([[AH, C], [C.T, D]])

    U = np.vstack([np.eye(2), K])
    W = np.vstack([U, M.T @ np.linalg.inv(B)])
    latent = W @ B @ W.T

    EH = AH - U @ B @ U.T
    EL = D - M.T @ np.linalg.inv(B) @ M
    EHL = np.vstack([np.zeros((2, q)), R])
    expected = np.block([[EH, EHL], [EHL.T, EL]])
    E = A - latent

    max_identity_residual = max(
        max_identity_residual, float(np.linalg.norm(E - expected, 2))
    )
    s = np.linalg.svd(A, compute_uv=False)
    if s[2] > 1e-12:
        min_E_over_s3 = min(min_E_over_s3, float(np.linalg.norm(E, 2) / s[2]))

print(f"N={N}")
print(f"S0={S0:.15g}")
print(f"zero_B_bound={zero_B_bound:.12f}")
print(f"definite_det_ge_S0_bound={definite_bound:.12f}")
print(f"max_abs_K_coeff_200={max_coeff:.12f}")
print(f"max_block_identity_residual_200={max_identity_residual:.3e}")
print(f"min_E_over_s3_ratio_200={min_E_over_s3:.12f}")
assert max_coeff <= 1 + 1e-10
assert max_identity_residual < 1e-10
assert min_E_over_s3 >= 1 - 1e-10
print("QFORM_B19_R39_MAXVOL_LATENT_CHECK_PASS")
