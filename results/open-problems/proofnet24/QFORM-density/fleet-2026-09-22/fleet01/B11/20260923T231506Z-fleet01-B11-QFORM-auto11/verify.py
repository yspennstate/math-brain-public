import math
import numpy as np

rng = np.random.default_rng(20260923)
max_absorption_error = 0.0
max_orthonormality_error = 0.0
minimum_exact_family_nonzero_abs_eigenvalue = float('inf')

for _ in range(1000):
    C0 = rng.normal(size=(3, 3))
    while abs(np.linalg.det(C0)) < 0.1:
        C0 = rng.normal(size=(3, 3))
    m = int(rng.integers(1, 6))
    D = rng.normal(size=(3, m))
    K = np.linalg.solve(C0, D)

    T = rng.normal(size=3)
    R = rng.normal(size=3)
    W = rng.normal(size=m)
    lhs = T @ C0 @ R + T @ D @ W
    rhs = T @ C0 @ (R + K @ W)
    max_absorption_error = max(max_absorption_error, abs(lhs-rhs))

    H2 = np.eye(3) + K @ K.T
    evals, evecs = np.linalg.eigh(H2)
    H = evecs @ np.diag(np.sqrt(evals)) @ evecs.T
    L = np.concatenate([np.eye(3), K], axis=1)
    O = np.linalg.solve(H, L)
    max_orthonormality_error = max(
        max_orthonormality_error,
        float(np.max(np.abs(O @ O.T - np.eye(3))))
    )

    M = np.diag([1.0, 1.0, -1.0])
    G = np.concatenate([np.eye(3), np.eye(3), K], axis=1)
    A = G.T @ M @ G
    eig = np.linalg.eigvalsh(A)
    nz = np.abs(eig[np.abs(eig) > 1e-8])
    minimum_exact_family_nonzero_abs_eigenvalue = min(
        minimum_exact_family_nonzero_abs_eigenvalue,
        float(np.min(nz))
    )

beta0 = 289/15984
eta0 = math.sqrt(191)/16 * beta0
kappa_star = (34/111)*(17/288)**2
delta = kappa_star * eta0 / 8
branch_constant = 6 * delta**(-1/3)

print('max_absorption_error', max_absorption_error)
print('max_orthonormality_error', max_orthonormality_error)
print('minimum_exact_family_nonzero_abs_eigenvalue', minimum_exact_family_nonzero_abs_eigenvalue)
print('beta0', beta0)
print('eta0', eta0)
print('kappa_star', kappa_star)
print('delta', delta)
print('branch_constant', branch_constant)

assert max_absorption_error < 1e-10
assert max_orthonormality_error < 1e-9
assert minimum_exact_family_nonzero_abs_eigenvalue > 1.999999999
assert branch_constant < 469.774
print('QFORM_B11_HUB_TRANSFER_ABSORPTION_CHECK_PASS')
