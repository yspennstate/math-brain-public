import json
import math
import numpy as np

rng = np.random.default_rng(12345)
n = 9
eps = 1.0/8.0
delta = 1.0/16.0
gamma = 7.0/24.0
final_floor = 11.0/48.0
spectral_floor = 47.0/16.0

V = np.zeros((n, 2))
V[[0, 3, 6], 0] = 1.0 / math.sqrt(3.0)
V[[1, 4, 7], 1] = 1.0 / math.sqrt(3.0)

Lp = np.array([
    [-23/24, 13/16, 7/48],
    [13/16, -7/24, -25/48],
    [7/48, -25/48, 3/8],
], dtype=float)
Lm = np.array([
    [-25/24, 41/48, 3/16],
    [41/48, -3/8, -23/48],
    [3/16, -23/48, 7/24],
], dtype=float)

A0 = V @ V.T
A0[np.ix_([0, 3, 6], [0, 3, 6])] += Lp
A0[np.ix_([1, 4, 7], [1, 4, 7])] += Lm
for i in [2, 5, 8]:
    A0[i, i] += 3.0

cores = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

def best_core_gap(A):
    return max(np.min(np.abs(np.linalg.eigvalsh(A[np.ix_(I, I)]))) for I in cores)

exact_residual = float(np.linalg.norm(A0 @ V - V, 2))
orthogonality_residual = float(np.linalg.norm(V.T @ V - np.eye(2), 2))

min_grid_gap = float("inf")
grid_violations = 0
grid_cases = 0
for a in np.linspace(-4.0, 4.0, 17):
    for b in np.linspace(-4.0, 4.0, 17):
        for theta in np.linspace(0.0, math.pi, 13, endpoint=False):
            R = np.array([[math.cos(theta), -math.sin(theta)],
                          [math.sin(theta), math.cos(theta)]])
            Theta = R @ np.diag([a, b]) @ R.T
            A = A0 + V @ Theta @ V.T
            gap = best_core_gap(A)
            min_grid_gap = min(min_grid_gap, gap)
            grid_cases += 1
            if gap + 1e-10 < gamma:
                grid_violations += 1

random_cases = 10000
min_random_gap = float("inf")
min_random_lambda3 = float("inf")
random_violations = 0
for _ in range(random_cases):
    ev = rng.uniform(-1e5, 1e5, 2)
    theta = rng.uniform(0.0, math.pi)
    R = np.array([[math.cos(theta), -math.sin(theta)],
                  [math.sin(theta), math.cos(theta)]])
    Theta = R @ np.diag(ev) @ R.T
    G = rng.normal(size=(n, n))
    T = 0.5 * (G + G.T)
    op = float(np.max(np.abs(np.linalg.eigvalsh(T))))
    if op > 0:
        T *= delta / op
    A = A0 + V @ Theta @ V.T + T
    gap = best_core_gap(A)
    lam3 = float(np.linalg.eigvalsh(A)[-3])
    min_random_gap = min(min_random_gap, gap)
    min_random_lambda3 = min(min_random_lambda3, lam3)
    if gap + 1e-8 < final_floor or lam3 + 1e-8 < spectral_floor:
        random_violations += 1

out = {
    "construction": {
        "A0V_minus_V_op": exact_residual,
        "VtV_minus_I_op": orthogonality_residual,
        "baseline_eigenvalues": [float(x) for x in np.linalg.eigvalsh(A0)],
        "claimed_pre_tail_core_floor": gamma,
        "claimed_final_core_floor": final_floor,
        "claimed_global_lambda3_floor": spectral_floor,
        "density_constant_288sqrtpi_over_11": 288.0 * math.sqrt(math.pi) / 11.0,
    },
    "grid": {
        "cases": grid_cases,
        "minimum_best_core_gap": min_grid_gap,
        "violations": grid_violations,
    },
    "random_dense_tail": {
        "seed": 12345,
        "cases": random_cases,
        "theta_eigenvalue_range": [-100000.0, 100000.0],
        "tail_operator_norm": delta,
        "minimum_best_core_gap": min_random_gap,
        "minimum_third_largest_eigenvalue": min_random_lambda3,
        "violations": random_violations,
    },
}
print(json.dumps(out, indent=2, sort_keys=True))
