import itertools
import numpy as np

SEED = 2026092403
TRIALS = 120
rng = np.random.default_rng(SEED)


def e3_cross(B):
    s = np.linalg.svd(B, compute_uv=False)
    x = s * s
    ans = 0.0
    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            for k in range(j + 1, len(x)):
                ans += x[i] * x[j] * x[k]
    return ans


def mixed_T(N, D):
    m, r = N.shape
    total = off = overlap = 0.0
    for t in range(m):
        for I in itertools.combinations(range(m), 3):
            for J in itertools.combinations(range(r), 2):
                M = np.column_stack((N[np.ix_(I, J)], D[list(I), t]))
                z = float(np.linalg.det(M)) ** 2
                total += z
                if t in I:
                    overlap += z
                else:
                    off += z
    return total, off, overlap


def max_left_split_e3(A, m):
    best = 0.0
    for mask in range(1 << m):
        S = [i for i in range(m) if (mask >> i) & 1]
        if len(S) < 3:
            continue
        Sc = [i for i in range(A.shape[0]) if i not in S]
        if len(Sc) < 3:
            continue
        best = max(best, e3_cross(A[np.ix_(S, Sc)]))
    return best


viol_T = viol_split = viol_approx = 0
max_negative_relative_T = 0.0
min_split_ratio = float("inf")
max_approx_ratio = 0.0

for _ in range(TRIALS):
    m = int(rng.integers(4, 7))
    r = int(rng.integers(2, 5))
    N = rng.normal(size=(m, r))
    D = rng.normal(size=(m, m)); D = (D + D.T) / 2
    C = rng.normal(size=(r, r)); C = (C + C.T) / 2

    U, s, Vt = np.linalg.svd(N, full_matrices=True)
    x = s * s
    P = U[:, :2] @ U[:, :2].T
    V = Vt.T
    R = V[:, :2] @ V[:, :2].T

    deltaL2 = np.linalg.norm((np.eye(m) - P) @ D, "fro") ** 2
    total, off, overlap = mixed_T(N, D)
    lower = x[0] * x[1] * deltaL2
    if total + 1e-8 < lower:
        viol_T += 1
    if lower > 1e-10:
        max_negative_relative_T = max(max_negative_relative_T, (lower - total) / lower)

    A = np.block([[D, N], [N.T, C]])
    best = max_left_split_e3(A, m)
    if best + 1e-8 < off / 16:
        viol_split += 1
    if off > 1e-10:
        min_split_ratio = min(min_split_ratio, best / (off / 16))

    N2 = P @ N @ R
    D0 = P @ D @ P
    C0 = R @ C @ R
    A0 = np.block([[D0, N2], [N2.T, C0]])
    tail2 = float(np.sum(x[2:])) if len(x) > 2 else 0.0
    deltaR2 = np.linalg.norm((np.eye(r) - R) @ C, "fro") ** 2
    bound = 2 * (deltaL2 + deltaR2 + tail2)
    err2 = np.linalg.norm(A - A0, "fro") ** 2
    if err2 > bound + 1e-8:
        viol_approx += 1
    if bound > 1e-12:
        max_approx_ratio = max(max_approx_ratio, err2 / bound)

print({
    "seed": SEED,
    "trials": TRIALS,
    "violations_mixed_lower_bound": viol_T,
    "violations_physicalization": viol_split,
    "violations_near_rank4_frobenius": viol_approx,
    "max_negative_relative_mixed_discrepancy": max_negative_relative_T,
    "min_observed_split_ratio": min_split_ratio,
    "max_observed_approx_ratio": max_approx_ratio,
})
