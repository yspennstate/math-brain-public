import itertools
import numpy as np

rng = np.random.default_rng(0)
max_err = np.zeros(5)
for n in (5, 8, 12, 30):
    for _ in range(50):
        G0 = rng.normal(size=(n, 3))
        R, _ = np.linalg.qr(G0)
        R = R[:, :3]
        P = R @ R.T
        i = int(rng.integers(n))
        ell = P[i, i]
        J = [j for j in range(n) if j != i]
        G = R[J].T @ R[J]
        invG = np.linalg.inv(G)
        lev = np.array([R[j] @ invG @ R[j] for j in J])
        pred = np.array([P[j, j] + P[i, j] ** 2 / (1 - ell) for j in J])

        mass = 0.0
        avoiding = 0.0
        for I in itertools.combinations(range(n), 3):
            w = np.linalg.det(R[list(I)]) ** 2
            mass += w
            if i not in I:
                avoiding += w

        err = np.array([
            abs(np.linalg.det(G) - (1 - ell)),
            np.max(np.abs(lev - pred)),
            abs(lev.sum() - 3),
            abs(mass - 1),
            abs(avoiding - (1 - ell)),
        ])
        max_err = np.maximum(max_err, err)

print("max errors:", max_err)
print("QFORM_B06_R46_CHECK_PASS")
