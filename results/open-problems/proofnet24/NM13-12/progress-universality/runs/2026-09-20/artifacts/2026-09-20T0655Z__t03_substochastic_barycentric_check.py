from fractions import Fraction
import numpy as np

# Exact one-row marginal moments for the concrete random barycentric model
# b = U g_1 + (1-U) g_2, U ~ Uniform[0,1], g_1,g_2 iid N(0,1).
E_S = Fraction(2, 3)
E_S2 = Fraction(7, 15)
E_B4 = 3 * E_S2
GAUSSIAN_SAME_VAR_B4 = 3 * E_S * E_S
KURTOSIS = E_B4 / (E_S * E_S)
FOURTH_MOMENT_GAP = E_B4 - GAUSSIAN_SAME_VAR_B4

print("E_S", E_S)
print("E_S2", E_S2)
print("E_B2", E_S)
print("E_B4", E_B4)
print("GAUSSIAN_SAME_VAR_B4", GAUSSIAN_SAME_VAR_B4)
print("FOURTH_MOMENT_GAP", FOURTH_MOMENT_GAP)
print("STANDARDIZED_KURTOSIS", KURTOSIS)

assert E_S == Fraction(2, 3)
assert E_S2 == Fraction(7, 15)
assert E_B4 == Fraction(7, 5)
assert GAUSSIAN_SAME_VAR_B4 == Fraction(4, 3)
assert FOURTH_MOMENT_GAP == Fraction(1, 15)
assert KURTOSIS == Fraction(63, 20)

# Deterministic strict class-separation witness: the new theorem accepts
# B = W A with W=I at kappa<=0 regardless of singular scale. At A=10 I,
# every singular value equals 10, so the previous s_{r+1}(B)<=1 hypothesis
# fails for every r<N even though the added constraints are exact duplicates.
N = 5
A = 10 * np.eye(N)
W = np.eye(N)
B = W @ A
svals = np.linalg.svd(B, compute_uv=False)
print("DET_CLASS_SEPARATION_RANK_B", np.linalg.matrix_rank(B))
print("DET_CLASS_SEPARATION_MIN_SINGULAR", float(svals[-1]))
assert np.allclose(B, A)
assert np.linalg.matrix_rank(B) == N
assert svals[-1] > 1.0

# Concrete full-rank dependent/non-Gaussian model used in the report.
# For j=1,...,N: b_j = U_j g_j + (1-U_j) g_{N+1}.
rng = np.random.default_rng(20260920)
N = 6
m = 10
G = rng.normal(size=(m, N))
U = rng.uniform(size=N)
W = np.zeros((N, m))
for j, u in enumerate(U):
    W[j, j] = u
    W[j, N] = 1 - u
B = W @ G

print("RANDOM_W_ROW_SUM_MAX_ERR", float(np.max(np.abs(W.sum(axis=1) - 1))))
print("RANDOM_W_RANK", np.linalg.matrix_rank(W))
print("RANDOM_B_RANK", np.linalg.matrix_rank(B))
print("RANDOM_B_MIN_SINGULAR", float(np.linalg.svd(B, compute_uv=False)[-1]))
assert np.max(np.abs(W.sum(axis=1) - 1)) < 1e-15
assert np.linalg.matrix_rank(W) == N
assert np.linalg.matrix_rank(B) == N

# Pointwise sanity check of exact redundancy at kappa=-1 over sampled sphere points.
kappa = -1.0
violations = 0
core_feasible_count = 0
min_slack = float("inf")
for _ in range(20000):
    x = rng.normal(size=N)
    x /= np.linalg.norm(x)
    gx = G @ x
    bx = B @ x
    if np.min(gx) >= kappa:
        core_feasible_count += 1
        min_slack = min(min_slack, float(np.min(bx) - kappa))
        if np.min(bx) < kappa - 1e-12:
            violations += 1

print("SAMPLED_CORE_FEASIBLE_POINTS", core_feasible_count)
print("SAMPLED_REDUNDANCY_VIOLATIONS", violations)
print("SAMPLED_MIN_ADDED_SLACK_GIVEN_CORE_FEASIBLE", min_slack if core_feasible_count else "NA")
assert violations == 0

# Project endpoints used only for arithmetic reconciliation, not as an audit.
ALPHA_L = 6.302974375068753
ALPHA_U_CANDIDATE = 12.31963485
ALPHA_U_HISTORICAL_RIGOROUS = 12.78437096216
print("AUGMENTED_LOWER_BETA1", ALPHA_L + 1)
print("AUGMENTED_UPPER_CANDIDATE_BETA1", ALPHA_U_CANDIDATE + 1)
print("AUGMENTED_UPPER_HISTORICAL_RIGOROUS_BETA1", ALPHA_U_HISTORICAL_RIGOROUS + 1)
print("PARENT_CANDIDATE_WIDTH", ALPHA_U_CANDIDATE - ALPHA_L)
print("AUGMENTED_CANDIDATE_WIDTH", (ALPHA_U_CANDIDATE + 1) - (ALPHA_L + 1))
assert abs(((ALPHA_U_CANDIDATE + 1) - (ALPHA_L + 1)) - (ALPHA_U_CANDIDATE - ALPHA_L)) < 1e-14

print("ALL_SUBSTOCHASTIC_BARYCENTRIC_CHECKS_PASS")
