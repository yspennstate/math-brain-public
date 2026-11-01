import itertools
import numpy as np

rng = np.random.default_rng(20260922)
max_mixed_discriminant_error = 0.0
max_rank_one_factor_error = 0.0
min_best_split_ratio = float("inf")

# Mixed-discriminant coefficient check.
for _ in range(250):
    groups = []
    for _g in range(3):
        m = int(rng.integers(2, 7))
        X = 0.2 * rng.normal(size=(m, 3))
        groups.append(X)
    H = [X.T @ X for X in groups]
    T = sum(
        np.linalg.det(np.vstack([a, b, c])) ** 2
        for a in groups[0]
        for b in groups[1]
        for c in groups[2]
    )
    coeff = (
        np.linalg.det(H[0] + H[1] + H[2])
        - np.linalg.det(H[0] + H[1])
        - np.linalg.det(H[0] + H[2])
        - np.linalg.det(H[1] + H[2])
        + np.linalg.det(H[0])
        + np.linalg.det(H[1])
        + np.linalg.det(H[2])
    )
    max_mixed_discriminant_error = max(
        max_mixed_discriminant_error, abs(T - coeff)
    )

# Rank-one factorization T=e1*e2*e3*det(V)^2.
for _ in range(250):
    directions = rng.normal(size=(3, 3))
    directions /= np.linalg.norm(directions, axis=1)[:, None]
    groups = []
    energies = []
    for g in range(3):
        m = int(rng.integers(1, 8))
        a = rng.normal(size=m)
        a *= rng.uniform(0.05, 0.8) / max(np.linalg.norm(a), 1e-15)
        groups.append(a[:, None] * directions[g][None, :])
        energies.append(float(a @ a))
    T = sum(
        np.linalg.det(np.vstack([a, b, c])) ** 2
        for a in groups[0]
        for b in groups[1]
        for c in groups[2]
    )
    formula = np.prod(energies) * np.linalg.det(directions) ** 2
    max_rank_one_factor_error = max(
        max_rank_one_factor_error, abs(T - formula)
    )

# Exhaustive split check for random JJK packets.
for _ in range(100):
    m = int(rng.integers(2, 8))
    n = int(rng.integers(1, 6))
    J = rng.normal(size=(m, 3))
    K = rng.normal(size=(n, 3))
    total = sum(
        np.linalg.det(np.vstack([J[i], J[j], K[k]])) ** 2
        for i in range(m)
        for j in range(i + 1, m)
        for k in range(n)
    )
    best = 0.0
    for mask in range(1 << m):
        separated = 0.0
        for i in range(m):
            for j in range(i + 1, m):
                if ((mask >> i) & 1) != ((mask >> j) & 1):
                    for k in range(n):
                        separated += np.linalg.det(
                            np.vstack([J[i], J[j], K[k]])
                        ) ** 2
        best = max(best, separated)
    if total > 1e-14:
        min_best_split_ratio = min(min_best_split_ratio, best / total)

assert max_mixed_discriminant_error < 1e-12
assert max_rank_one_factor_error < 1e-12
assert min_best_split_ratio >= 0.5 - 1e-12

print("QFORM_TRIPARTITE_R20_CHECK_PASS")
print("max_mixed_discriminant_error", max_mixed_discriminant_error)
print("max_rank_one_factor_error", max_rank_one_factor_error)
print("min_best_split_ratio", min_best_split_ratio)
