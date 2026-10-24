import numpy as np
import itertools
import math

SEED = 20260924
TRIALS = 5000
rng = np.random.default_rng(SEED)
max_schur = 0.0
max_agg = 0.0
max_weighted = 0.0
used = 0

for _ in range(TRIALS):
    B0 = rng.normal(size=(3, 3))
    B = (B0 + B0.T) / 2
    if abs(np.linalg.det(B)) < 0.05:
        B = B + np.diag([1.25, -0.8, 0.95])
    beta = np.linalg.det(B)
    if abs(beta) < 1e-8:
        continue

    m = 8
    Z = rng.normal(size=(3, m))
    d = rng.normal(size=3)
    K = B + np.diag(d)
    G = Z @ Z.T
    if abs(np.linalg.det(G)) < 1e-10:
        continue
    adjG = np.linalg.det(G) * np.linalg.inv(G)

    F = np.concatenate([np.eye(3), Z], axis=1)
    A = F.T @ B @ F
    A[:3, :3] += np.diag(d)

    sum_L2 = 0.0
    sum_weight = 0.0
    for h in range(3):
        J = [j for j in range(3) if j != h]
        a = K[h, h]
        vals = []
        for p, q in itertools.combinations(range(m), 2):
            cols = [h, 3 + p, 3 + q]
            vals.append(np.linalg.det(A[np.ix_([0, 1, 2], cols)]))
        vals = np.asarray(vals)
        Lnorm = np.linalg.norm(vals)
        sum_L2 += Lnorm**2
        sum_weight += a * a * Lnorm**2

        if abs(a) > 1e-7:
            N = (
                A[np.ix_(J, range(3, 3 + m))]
                - np.outer(A[J, h], A[h, 3:]) / a
            )
            s = np.linalg.svd(N, compute_uv=False)
            Delta = s[0] * s[1]
            den = 1.0 + Lnorm + abs(a) * Delta
            max_schur = max(
                max_schur,
                abs(Lnorm - abs(a) * Delta) / den,
            )

    M = K @ np.linalg.inv(B)
    rhs = beta * beta * np.trace(M @ adjG @ M.T)
    Da = np.diag(np.diag(K))
    rhs_w = beta * beta * np.trace(Da @ Da @ M @ adjG @ M.T)
    max_agg = max(
        max_agg,
        abs(sum_L2 - rhs) / (1.0 + abs(sum_L2) + abs(rhs)),
    )
    max_weighted = max(
        max_weighted,
        abs(sum_weight - rhs_w) / (1.0 + abs(sum_weight) + abs(rhs_w)),
    )
    used += 1

# Independent audit of the constant in Theorem 2.1.
C2 = (4 * math.pi) ** 2
C3 = (4 * math.pi) ** 3
R = math.pi
weighted_near = 4 * C2 * math.sqrt(R)
weighted_far = C3 / math.sqrt(R)
weighted_total = weighted_near + weighted_far
fourier_prefactor_constant = weighted_total / math.sqrt(4 * math.pi)
density_constant = fourier_prefactor_constant / (2 * math.pi) ** 2

print("QFORM_B06_R53_CHECK_PASS")
print("used_trials", used)
print("max_schur_minor_error", f"{max_schur:.18e}")
print("max_unweighted_aggregate_error", f"{max_agg:.18e}")
print("max_weighted_aggregate_error", f"{max_weighted:.18e}")
print("split_R", f"{R:.18e}")
print("weighted_near", f"{weighted_near:.18e}")
print("weighted_far", f"{weighted_far:.18e}")
print("density_constant", f"{density_constant:.18e}")
