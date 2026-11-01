import itertools
import json
import math
import numpy as np


def sylvester(n):
    H = np.array([[1.0]])
    while H.shape[0] < n:
        H = np.block([[H, H], [H, -H]])
    if H.shape != (n, n):
        raise ValueError("n must be a power of two")
    return H

n = 32
N = n - 2
H = sylvester(n)
V = H / math.sqrt(n)
d = np.array([2.0, 2.0] + [1.0] * N)
M = np.diag(d) @ V
A = np.block([[np.zeros((n, n)), M], [M.T, np.zeros((n, n))]])

sv = np.linalg.svd(M, compute_uv=False)
eig = np.linalg.eigvalsh(A)
T2 = float(np.sum(sv[2:] ** 2))
h0 = 3.0 * sv[0] ** 2 / T2
E3_exact = math.comb(N, 3) + 8 * math.comb(N, 2) + 16 * N
bound_E3 = 3 * math.e * E3_exact ** (-1 / 6)
bound_tail = 3 * math.e * (sv[0] ** 2 * sv[1] ** 2 * T2) ** (-1 / 6)

R = tuple(range(6))
a = {}
for S in itertools.combinations(R, 3):
    G = M[list(S), :] @ M[list(S), :].T
    a[S] = float(np.linalg.det(G))
C_R = 0.0
for S in itertools.combinations(R, 3):
    Sbar = tuple(sorted(set(R) - set(S)))
    C_R += math.sqrt(max(a[S], 0.0) * max(a[Sbar], 0.0))
hellinger_bound = 3 * math.e * C_R ** (-1 / 6)

out = {
    "hadamard_orthogonality_error_op": float(np.linalg.norm(V @ V.T - np.eye(n), ord=2)),
    "MMt_diagonal_error_op": float(np.linalg.norm(M @ M.T - np.diag(d * d), ord=2)),
    "singular_values_head": [float(x) for x in sv[:5]],
    "singular_values_tail": [float(x) for x in sv[-3:]],
    "min_abs_eigenvalue_A": float(np.min(np.abs(eig))),
    "min_abs_entry_M": float(np.min(np.abs(M))),
    "max_abs_entry_M": float(np.max(np.abs(M))),
    "T2": T2,
    "h_P_zero": h0,
    "E3_exact": E3_exact,
    "density_bound_exact_E3": bound_E3,
    "density_bound_tail_lower_bound": bound_tail,
    "six_row_C_R": C_R,
    "six_row_hellinger_bound": hellinger_bound,
    "top_two_left_projection_max_diagonal": 1.0,
    "checks_pass": bool(
        np.linalg.norm(V @ V.T - np.eye(n), ord=2) < 1e-12
        and np.linalg.norm(M @ M.T - np.diag(d * d), ord=2) < 1e-12
        and np.min(np.abs(eig)) > 1 - 1e-12
        and np.min(np.abs(M)) > 0
        and abs(T2 - 30.0) < 1e-10
        and abs(h0 - 0.4) < 1e-10
        and E3_exact == 8020
        and abs(C_R - 80.0) < 1e-10
    ),
}
print(json.dumps(out, indent=2, sort_keys=True))
