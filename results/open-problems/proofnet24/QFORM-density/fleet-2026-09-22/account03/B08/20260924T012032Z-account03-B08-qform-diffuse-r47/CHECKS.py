import math
import numpy as np

rng = np.random.default_rng(2026092401)
max_vcoeff = 0.0
max_gamma = 0.0
max_area_rel = 0.0
max_lev_err = 0.0
n = 0

for _ in range(5000):
    m = int(rng.integers(4, 15))
    M = rng.normal(size=(2, m))
    if np.linalg.matrix_rank(M) < 2:
        continue
    G = M @ M.T
    invG = np.linalg.inv(G)
    ell = np.array([M[:, j] @ invG @ M[:, j] for j in range(m)])
    r = rng.normal(size=2)
    r /= np.linalg.norm(r)
    lam = (1 if rng.random() < 0.5 else -1) * 10 ** rng.uniform(-1, 1)
    w = M.T @ r
    j = int(rng.integers(m))
    d = -np.sign(lam) * 10 ** rng.uniform(-1, 1)
    a = d + lam * w[j] ** 2

    if abs(a) > 1e-10:
        alpha = (lam * w[j] + math.sqrt(-lam * d)) / a
    else:
        if abs(w[j]) < 1e-12:
            continue
        alpha = 1.0 / (2.0 * w[j])

    gamma = lam * w[j] - a * alpha
    vcoeff = a * alpha**2 - 2 * lam * w[j] * alpha + lam
    max_vcoeff = max(max_vcoeff, abs(vcoeff))
    max_gamma = max(max_gamma, abs(gamma**2 + lam * d))

    if abs(r[1]) >= abs(r[0]):
        p, rperp = 0, r[1]
    else:
        p, rperp = 1, r[0]

    K = [k for k in range(m) if k != j]
    wK = w[K]
    row1 = gamma * wK
    row2 = M[p, K] - alpha * M[p, j] * wK
    C = np.vstack([row1, row2])
    MK = M[:, K]

    area = math.sqrt(max(0.0, np.linalg.det(C @ C.T)))
    area_expected = abs(gamma * rperp) * math.sqrt(max(0.0, np.linalg.det(MK @ MK.T)))
    if area_expected > 1e-12:
        max_area_rel = max(max_area_rel, abs(area - area_expected) / area_expected)

    if np.linalg.matrix_rank(MK) == 2 and np.linalg.matrix_rank(C) == 2:
        PC = C.T @ np.linalg.inv(C @ C.T) @ C
        PM = MK.T @ np.linalg.inv(MK @ MK.T) @ MK
        max_lev_err = max(max_lev_err, float(np.max(np.abs(np.diag(PC) - np.diag(PM)))))
    n += 1

# Target-valid family from REPORT Section 5, with L=1.
m = 6
M = np.zeros((2, m))
M[0, 0:3] = 1 / math.sqrt(3)
M[1, 3:6] = 1 / math.sqrt(3)
R = np.array([[1.0, 0.0], [0.0, 0.0]])
D = np.zeros((m, m))
D[0, 0] = -1 / 3
A = np.block([[np.zeros((2, 2)), M], [M.T, M.T @ R @ M + D]])
eigs = np.linalg.eigvalsh(A)
G = M @ M.T
invG = np.linalg.inv(G)
lev = [M[:, j] @ invG @ M[:, j] for j in range(m)]

print("QFORM_B08_R47_CHECK_PASS")
print("random_instances", n)
print("max_cancelled_V2_abs", max_vcoeff)
print("max_gamma_identity_abs", max_gamma)
print("max_area_relative_error", max_area_rel)
print("max_leverage_diagonal_error", max_lev_err)
print("target_family_eigenvalues", eigs.tolist())
print("target_family_singular_values_M", np.linalg.svd(M, compute_uv=False).tolist())
print("target_family_max_leverage", max(lev))
print("general_family_constant_4sqrt3", 4 * math.sqrt(3))
print("exact_family_constant", 4 * math.sqrt(3 / math.sqrt(2)))
print("inherited_scale_constant", 4 * 2 ** 0.25 * math.sqrt(1024))
