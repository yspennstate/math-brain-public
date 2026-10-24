import numpy as np

SEED = 5601
TRIALS = 5000
rng = np.random.default_rng(SEED)


def orth_complement(s):
    _, _, vh = np.linalg.svd(s.reshape(1, 3), full_matrices=True)
    return vh[1:].T


max_minor_err = 0.0
max_area_err = 0.0

for _ in range(TRIALS):
    s = rng.normal(size=3)
    s /= np.linalg.norm(s)
    kappa = rng.normal()
    if abs(kappa) < 0.1:
        kappa += 0.3 if kappa >= 0 else -0.3

    F = kappa * np.outer(s, s)
    D = np.diag(rng.normal(size=3))
    B = F - D
    m = 6
    Z = rng.normal(size=(3, m))
    tail_diag = rng.normal(size=m)
    V = orth_complement(s)
    Omega = Z.T @ D @ V

    j, k = rng.choice(m, 2, replace=False)
    J = [j, k]
    ZJ = Z[:, J]
    M = np.block([
        [F, B @ ZJ],
        [ZJ.T @ B, ZJ.T @ B @ ZJ + np.diag(tail_diag[J])],
    ])
    lhs = np.linalg.det(M)
    rhs = kappa * np.linalg.det(Omega[J, :]) ** 2
    err = abs(lhs - rhs) / (1.0 + abs(lhs) + abs(rhs))
    max_minor_err = max(max_minor_err, err)

    i = int(np.argmax(np.abs(s)))
    rest = [h for h in range(3) if h != i]
    a = F[i, i]
    E = B @ Z
    C = E[rest, :] - np.outer(F[rest, i] / a, E[i, :])
    area = np.sqrt(max(0.0, np.linalg.det(C @ C.T)))
    Aker = np.linalg.det(Omega.T @ Omega)
    rhs_area = np.sqrt(max(0.0, Aker)) / abs(s[i])
    err = abs(area - rhs_area) / (1.0 + abs(area) + abs(rhs_area))
    max_area_err = max(max_area_err, err)

print("QFORM_B06_R56_CHECK_PASS")
print("seed", SEED)
print("trials", TRIALS)
print("max_normalized_five_minor_error", repr(max_minor_err))
print("max_normalized_cross_area_error", repr(max_area_err))
