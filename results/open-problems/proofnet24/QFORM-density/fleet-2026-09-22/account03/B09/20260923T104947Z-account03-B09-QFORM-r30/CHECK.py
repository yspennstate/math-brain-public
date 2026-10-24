import itertools
import math
import numpy as np


def walsh_frame(N: int) -> np.ndarray:
    if N % 4:
        raise ValueError("N must be a multiple of four")
    idx = np.arange(N)
    return np.stack(
        [
            np.ones(N),
            (-1) ** (idx & 1),
            (-1) ** ((idx >> 1) & 1),
        ],
        axis=1,
    ) / math.sqrt(N)


def exact_max_minor(B: np.ndarray) -> float:
    N = B.shape[0]
    best = 0.0
    triples = list(itertools.combinations(range(N), 3))
    for I in triples:
        for J in triples:
            best = max(best, abs(np.linalg.det(B[np.ix_(I, J)])))
    return best


for N in [4, 8, 16, 64]:
    P = walsh_frame(N)
    B = P @ P.T
    A = np.block([[np.zeros((N, N)), B], [B.T, np.zeros((N, N))]])

    orth_err = np.max(np.abs(P.T @ P - np.eye(3)))
    singulars = np.linalg.svd(B, compute_uv=False)[:3]
    eig = np.linalg.eigvalsh(A)
    large_eigs = eig[np.abs(eig) > 0.999999]

    c = 1 - 3 / N
    grouped_bound = 3 * (c ** (-(N - 3) / 2) * c ** (-(N - 3) / 2)) ** (1 / 3)
    formula_minor = 16 / N**3
    partner_best = 3 * formula_minor ** (-1 / 3)

    print(
        f"N={N}: orth_err={orth_err:.3e}, "
        f"singulars={singulars}, large_eigs={large_eigs}, "
        f"grouped_bound={grouped_bound:.12f}, "
        f"formula_max_physical_minor={formula_minor:.12g}, "
        f"partner_best_minor_bound={partner_best:.12f}"
    )

    if N <= 16:
        brute = exact_max_minor(B)
        assert abs(brute - formula_minor) < 1e-10, (N, brute, formula_minor)

print(f"3e={3 * math.e:.15f}")

# Exact residual-structure regression: D=C M C^T + diagonal implies every
# singleton augmentation has rank at most two.
rng = np.random.default_rng(20260923)
m = 7
C = rng.normal(size=(m, 2))
M0 = rng.normal(size=(2, 2))
M = (M0 + M0.T) / 2
diag = rng.normal(size=m)
D = C @ M @ C.T + np.diag(diag)

ranks = []
for k in range(m):
    rest = [j for j in range(m) if j != k]
    K = np.vstack([C[rest, :].T, D[k, rest]])
    ranks.append(np.linalg.matrix_rank(K, tol=1e-10))

print(f"residual_augmented_ranks={ranks}")
assert all(r <= 2 for r in ranks)
