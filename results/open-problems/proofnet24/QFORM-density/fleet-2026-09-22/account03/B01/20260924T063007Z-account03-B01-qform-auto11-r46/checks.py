import math
import numpy as np

# Deterministic verification for account03/B01 r46.
# No Monte Carlo density claims are made: the random-looking matrices below are
# seeded algebraic stress tests of exact Schur identities and singular-value inequalities.

alpha = 1.0 / 3.0
C_alpha = (12.0 / math.e) ** alpha / math.sqrt(1.0 - 2.0 * alpha)
H_alpha = (2.0 ** alpha) * C_alpha
A0 = 2.0 * math.sqrt(2.0)
Bconst = (C_alpha / alpha) * (2.0 ** (2.0 * alpha))
C_pair = (
    (1.0 + 2.0 * alpha)
    * (2.0 * alpha) ** (-2.0 * alpha / (1.0 + 2.0 * alpha))
    * A0 ** (2.0 * alpha / (1.0 + 2.0 * alpha))
    * Bconst ** (1.0 / (1.0 + 2.0 * alpha))
)

assert abs(C_alpha - 2.841337885233845) < 1e-12
assert abs(H_alpha - 3.579861411469905) < 1e-12
assert abs(C_pair - 14.18083262050194) < 1e-12

# Large-edge constants from the previously isolated physical pair chamber.
large_edge = C_pair * (3.0 / 4096.0) ** (-3.0 / 10.0) * (1.0 / 64.0) ** (-1.0 / 5.0)
hyperbolic_1_over_32 = C_pair * (1.0 / 32.0) ** (-4.0 / 5.0)
assert abs(large_edge - 284.1249247758415) < 1e-10
assert abs(hyperbolic_1_over_32 - 226.8933219280311) < 1e-10

# Schur decomposition / Eckart-Young stress test.
rng = np.random.default_rng(20260924)
max_decomposition_error = 0.0
max_interlacing_violation = -1e100
tested = 0
indefinite_pairs = 0
for _ in range(1000):
    n = 7
    M = rng.normal(size=(n, n))
    A = (M + M.T) / 2.0
    P = A[-2:, -2:]
    if abs(np.linalg.det(P)) < 1e-4:
        continue
    C = A[:-2, :-2]
    K = A[:-2, -2:]
    Pinv = np.linalg.inv(P)
    S = C - K @ Pinv @ K.T
    rank_two_term = np.block([[K @ Pinv @ K.T, K], [K.T, P]])
    schur_term = np.block(
        [[S, np.zeros((n - 2, 2))], [np.zeros((2, n - 2)), np.zeros((2, 2))]]
    )
    max_decomposition_error = max(
        max_decomposition_error, np.linalg.norm(A - rank_two_term - schur_term, ord=2)
    )
    s3 = np.linalg.svd(A, compute_uv=False)[2]
    max_interlacing_violation = max(
        max_interlacing_violation, s3 - np.linalg.norm(S, ord=2)
    )
    tested += 1
    if np.linalg.det(P) < 0:
        indefinite_pairs += 1

assert tested == 1000
assert indefinite_pairs == 723
assert max_decomposition_error < 1e-12
assert max_interlacing_violation <= 1e-12

# Exact cross-collapse target witness: eigenvalues {-1,1,1}.
stress = np.array([[1.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, 1.0, 0.0]])
eigs = np.linalg.eigvalsh(stress)
assert np.allclose(eigs, np.array([-1.0, 1.0, 1.0]), atol=1e-13)

print(f"C_alpha_1_3={C_alpha:.15f}")
print(f"H_alpha_1_3={H_alpha:.15f}")
print(f"C_pair_1_3={C_pair:.15f}")
print(f"large_edge_bound={large_edge:.15f}")
print(f"hyperbolic_c_1_over_32={hyperbolic_1_over_32:.15f}")
print(f"schur_trials={tested}")
print(f"indefinite_pair_trials={indefinite_pairs}")
print(f"max_decomposition_error={max_decomposition_error:.3e}")
print(f"max_interlacing_violation={max_interlacing_violation:.3e}")
print(f"stress_eigenvalues={eigs.tolist()}")
print("STATUS=PASS")
