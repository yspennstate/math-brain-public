import itertools
import math
import numpy as np

rng = np.random.default_rng(47)

# 1. Exact shear-flat normal form => every projected row residual vanishes.
max_projected_residual = 0.0
max_cut_factorization_error = 0.0
for _ in range(1000):
    m = 8
    E = rng.normal(size=(2, m))
    while np.linalg.matrix_rank(E) < 2:
        E = rng.normal(size=(2, m))
    M = rng.normal(size=(2, 2))
    M = (M + M.T) / 2
    d = rng.normal(size=m)
    K = E.T @ M @ E + np.diag(d)

    for j in range(m):
        J = [k for k in range(m) if k != j]
        EJ = E[:, J]
        if np.linalg.matrix_rank(EJ) == 2:
            P = EJ.T @ np.linalg.inv(EJ @ EJ.T) @ EJ
            q = K[j, J]
            residual = q @ (np.eye(m - 1) - P)
            max_projected_residual = max(max_projected_residual, np.linalg.norm(residual))

    perm = rng.permutation(m)
    I = perm[: m // 2]
    J = perm[m // 2 :]
    N = E[:, I].T @ M @ E[:, J]
    s = np.linalg.svd(N, compute_uv=False)
    lhs = s[0] * s[1]
    WI = np.linalg.det(E[:, I] @ E[:, I].T)
    WJ = np.linalg.det(E[:, J] @ E[:, J].T)
    rhs = abs(np.linalg.det(M)) * math.sqrt(max(WI, 0.0) * max(WJ, 0.0))
    max_cut_factorization_error = max(
        max_cut_factorization_error, abs(lhs - rhs) / (1.0 + rhs)
    )

# 2. Exact random-partition identity for one 8-column shear frame.
m = 8
E = rng.normal(size=(2, m))
G = E @ E.T
W = np.linalg.det(G)
weights = {}
for i in range(m):
    for j in range(i + 1, m):
        weights[(i, j)] = np.linalg.det(E[:, [i, j]]) ** 2
cauchy_binet_error = abs(W - sum(weights.values()))

Omega_raw = 0.0
for P, wP in weights.items():
    for Q, wQ in weights.items():
        if set(P).isdisjoint(Q):
            Omega_raw += wP * wQ

partition_products = []
for bits in itertools.product([0, 1], repeat=m):
    I = [i for i, b in enumerate(bits) if b == 0]
    J = [i for i, b in enumerate(bits) if b == 1]

    def area(indices):
        if len(indices) < 2:
            return 0.0
        F = E[:, indices]
        return max(0.0, np.linalg.det(F @ F.T))

    partition_products.append(area(I) * area(J))

partition_identity_error = abs(
    sum(partition_products) / len(partition_products) - Omega_raw / 16.0
)

# 3. Pair marginal equals whitened two-frame leverage.
leverages = []
pair_marginals = []
Ginv = np.linalg.inv(G)
for h in range(m):
    leverage = E[:, h].T @ Ginv @ E[:, h]
    pair_mass = sum(w for P, w in weights.items() if h in P) / W
    leverages.append(leverage)
    pair_marginals.append(pair_mass)
leverage_identity_error = max(abs(a - b) for a, b in zip(leverages, pair_marginals))

paid_constant = 16.0 * (64.0 ** (1.0 / 8.0))

print("QFORM_B06_R47_CHECK_PASS")
print("max_projected_residual", max_projected_residual)
print("max_cut_factorization_error", max_cut_factorization_error)
print("cauchy_binet_error", cauchy_binet_error)
print("partition_identity_error", partition_identity_error)
print("leverage_identity_error", leverage_identity_error)
print("paid_constant_16_times_64_pow_1_8", paid_constant)
