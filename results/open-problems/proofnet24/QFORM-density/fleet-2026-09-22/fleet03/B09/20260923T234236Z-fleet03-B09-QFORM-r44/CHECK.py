import math
import numpy as np

rng = np.random.default_rng(20260923)
max_detL = 0.0
max_detM = 0.0
max_residual = 0.0
accepted = 0

for _ in range(300):
    n = rng.normal(size=3)
    n /= np.linalg.norm(n)
    if np.min(np.abs(n)) < 0.05:
        continue

    T = rng.normal(size=(3, 2))
    T = T - n[:, None] * (n @ T)[None, :]
    E, _ = np.linalg.qr(T)
    K = rng.normal(size=(2, 7))
    C = E @ K

    P = rng.normal(size=(3, 3))
    P = (P + P.T) / 2

    singular = np.linalg.svd(C, compute_uv=False)
    Delta = singular[0] * singular[1]
    a = P @ n

    for h in range(3):
        idx = [i for i in range(3) if i != h]
        B = C[idx, :]
        U, s, Vt = np.linalg.svd(B, full_matrices=False)
        L = U @ np.diag(s)
        R = Vt.T
        q = R.T @ C[h, :]
        p = P[idx, h]
        d = P[h, h]

        M = np.block([[np.array([[d]]), q[None, :]], [p[:, None], L]])
        detL = abs(np.linalg.det(L))
        detM = abs(np.linalg.det(M))

        max_detL = max(max_detL, abs(detL - abs(n[h]) * Delta))
        max_detM = max(max_detM, abs(detM - Delta * abs(a[h])))

        if abs(d) > 1e-8:
            Lprime = L - np.outer(p, q) / d
            max_residual = max(
                max_residual,
                abs(abs(np.linalg.det(Lprime)) - detM / abs(d)),
            )

    accepted += 1

# Exact target-valid flat-kernel regression.
n = np.ones(3) / math.sqrt(3)
E = np.array([[1.0, -1.0, 0.0], [1.0, 1.0, -2.0]]).T
E, _ = np.linalg.qr(E)
C = E
P = np.outer(n, n)
A = np.block([[P, C], [C.T, np.zeros((2, 2))]])
Delta = np.prod(np.linalg.svd(C, compute_uv=False))
a = P @ n
V = Delta**2 * np.dot(a, a)
D = Delta * np.abs(a)
d = np.diag(P)
evals = np.linalg.eigvalsh(A)

print(f"accepted_random_instances={accepted}")
print(f"max_abs_error_detL={max_detL:.16e}")
print(f"max_abs_error_detM={max_detM:.16e}")
print(f"max_abs_error_residual_det={max_residual:.16e}")
print(f"target_regression_eigenvalues={evals.tolist()}")
print(f"target_regression_Delta={Delta:.16f}")
print(f"target_regression_V={V:.16f}")
print(f"target_regression_D={D.tolist()}")
print(f"target_regression_d={d.tolist()}")
print(f"target_regression_D_to_one_third={(D**(1/3)).tolist()}")
print(f"large_diagonal_exit_constant={2**(11/4)*3**(1/6):.15f}")
print(f"partner_K_diag_2_3_4_bound={3*24**(-1/3):.15f}")
