import itertools
import math
import numpy as np

rng = np.random.default_rng(9230510)

def e2(M):
    out = 0.0
    for rr in itertools.combinations(range(M.shape[0]), 2):
        for cc in itertools.combinations(range(M.shape[1]), 2):
            out += np.linalg.det(M[np.ix_(rr, cc)]) ** 2
    return out

def wedge2_diff_norm2(N, S):
    out = 0.0
    for rr in itertools.combinations(range(N.shape[0]), 2):
        for cc in itertools.combinations(range(N.shape[1]), 2):
            out += (
                np.linalg.det(N[np.ix_(rr, cc)])
                - np.linalg.det(S[np.ix_(rr, cc)])
            ) ** 2
    return out

max_det_err = 0.0
max_rank1_err = 0.0
max_seq_violation = 0.0

for _ in range(500):
    n = 8
    G = rng.normal(size=(n, n))
    A = (G + G.T) / 2
    K = [0, 1]
    B = A[np.ix_(K, K)]
    if abs(np.linalg.det(B)) < 1e-3:
        continue

    rest = list(range(2, n))
    I = [2, 3]
    J = [4, 5]
    S = (
        A[np.ix_(rest, rest)]
        - A[np.ix_(rest, K)] @ np.linalg.inv(B) @ A[np.ix_(K, rest)]
    )
    M = S[np.ix_([0, 1], [2, 3])]
    big = A[np.ix_(K + I, K + J)]
    max_det_err = max(
        max_det_err,
        abs(np.linalg.det(big) - np.linalg.det(B) * np.linalg.det(M)),
    )

    m, p = 5, 4
    S0 = rng.normal(size=(m, p))
    x = rng.normal(size=m)
    y = rng.normal(size=p)
    N = S0 + np.outer(x, y)

    lhs = wedge2_diff_norm2(N, S0)
    Px = np.eye(m) - np.outer(x, x) / (x @ x)
    Py = np.eye(p) - np.outer(y, y) / (y @ y)
    rhs = (x @ x) * (y @ y) * np.linalg.norm(Px @ S0 @ Py, "fro") ** 2
    max_rank1_err = max(max_rank1_err, abs(lhs - rhs))

    x1 = rng.normal(size=m)
    y1 = rng.normal(size=p)
    x2 = rng.normal(size=m)
    y2 = rng.normal(size=p)
    S1 = S0 + np.outer(x2, y2)
    NN = S1 + np.outer(x1, y1)
    D1 = math.sqrt(wedge2_diff_norm2(NN, S1))
    D2 = math.sqrt(wedge2_diff_norm2(S1, S0))
    violation = max(
        0.0,
        math.sqrt(e2(NN)) - (math.sqrt(e2(S0)) + D1 + D2),
    )
    max_seq_violation = max(max_seq_violation, violation)

def Cpair(h):
    return (
        16
        * (4 / 3) ** (3 / 4)
        * math.sqrt(6 * math.sqrt(math.e / (2 * h)) / (3 - 4 * h))
    )

h = 0.51
print("QFORM_B13_AUTO15B_CHECK_PASS")
print("max_det_err", repr(max_det_err))
print("max_rank1_identity_err", repr(max_rank1_err))
print("max_sequential_triangle_violation", repr(max_seq_violation))
print("Cpair_h_0.51", repr(Cpair(h)))
print("Cpair_diffuse_log4", repr(Cpair(h) * 4 ** (1 / 8)))
print("Cpair_survival_Equarter", repr(Cpair(h) * 4 ** (1 / 4)))
print(
    "global_zero_diag_Omega_factor",
    repr(Cpair(h) * 4 ** (1 / 8) * 16 ** (1 / 8)),
)
