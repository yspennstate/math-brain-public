import itertools
import math
import numpy as np

rng = np.random.default_rng(20260923)


def e2_svals(M):
    s = np.linalg.svd(M, compute_uv=False)
    x = s * s
    return 0.5 * (x.sum() ** 2 - (x * x).sum())


def proj_perp(v):
    nv = np.linalg.norm(v)
    if nv == 0:
        return np.eye(len(v))
    u = v / nv
    return np.eye(len(v)) - np.outer(u, u)


def oriented_mass(a, c, r, N):
    ans = 0.0
    for P in itertools.combinations(range(len(c)), 2):
        for Q in itertools.combinations(range(len(r)), 2):
            M = np.empty((3, 3))
            M[0, 0] = a
            M[0, 1:] = r[list(Q)]
            M[1:, 0] = c[list(P)]
            M[1:, 1:] = N[np.ix_(P, Q)]
            ans += np.linalg.det(M) ** 2
    return ans


max_rel_zero = 0.0
max_mink_excess = -1e100
max_resource_excess = -1e100
min_resource_ratio = float("inf")

for _ in range(1000):
    m = int(rng.integers(2, 7))
    n = int(rng.integers(2, 7))
    c = rng.normal(size=m)
    r = rng.normal(size=n)
    N = rng.normal(size=(m, n))
    Pc = proj_perp(c)
    Pr = proj_perp(r)
    C = Pc @ N @ Pr
    T = (c @ c) * (r @ r) * np.linalg.norm(C, "fro") ** 2

    D0 = oriented_mass(0.0, c, r, N)
    rel = abs(D0 - T) / max(1.0, abs(D0), abs(T))
    max_rel_zero = max(max_rel_zero, rel)

    a = float(rng.normal())
    D = oriented_mass(a, c, r, N)
    rhs = abs(a) * math.sqrt(max(e2_svals(N), 0.0)) + math.sqrt(max(T, 0.0))
    max_mink_excess = max(max_mink_excess, math.sqrt(max(D, 0.0)) - rhs)

    F2 = np.linalg.norm(C, "fro") ** 2
    if F2 > 1e-12:
        s = np.linalg.svd(C, compute_uv=False)
        rho = F2 / (s[0] ** 2)
        gamma = max(0.0, (1.0 - 1.0 / rho) / 2.0)
        u = c @ c
        w = r @ r
        b = min(u, w) / F2
        ZR = e2_svals(N @ Pr)
        ZL = e2_svals(Pc @ N)
        Rstar = max(w * ZR, u * ZL)
        lower = gamma * T / b
        max_resource_excess = max(max_resource_excess, lower - Rstar)
        if lower > 1e-12:
            min_resource_ratio = min(min_resource_ratio, Rstar / lower)

assert max_rel_zero < 1e-10
assert max_mink_excess < 1e-10
assert max_resource_excess < 1e-10

# Check the random-cut mean identity on 30 symmetric 7x7 packets.
def delta_i(A, i):
    K = [j for j in range(A.shape[0]) if j != i]
    ans = 0.0
    for P in itertools.combinations(K, 2):
        for Q in itertools.combinations(K, 2):
            if set(P).isdisjoint(Q):
                ans += np.linalg.det(A[np.ix_((i,) + P, (i,) + Q)]) ** 2
    return ans


def oriented_for_cut(A, i, L, R):
    return oriented_mass(A[i, i], A[L, i], A[i, R], A[np.ix_(L, R)])


max_cut_rel = 0.0
for _ in range(30):
    X = rng.normal(size=(7, 7))
    A = (X + X.T) / 2.0
    i = 0
    K = list(range(1, 7))
    delta = delta_i(A, i)
    vals = []
    for mask in range(1 << len(K)):
        L = [K[j] for j in range(len(K)) if (mask >> j) & 1]
        R = [K[j] for j in range(len(K)) if not ((mask >> j) & 1)]
        vals.append(oriented_for_cut(A, i, L, R) if len(L) >= 2 and len(R) >= 2 else 0.0)
    avg = sum(vals) / (1 << len(K))
    rel = abs(avg - delta / 16.0) / max(1.0, abs(avg), abs(delta / 16.0))
    max_cut_rel = max(max_cut_rel, rel)

assert max_cut_rel < 1e-10

C_h = 3 * 2 ** (7 / 6) * math.exp(1 / 3)
K_h = 2 ** (7 / 4) * math.pi ** 1.5 * math.exp(0.5)
L0 = 6 * math.pi * 2 ** (2 / 3)
C_hyb = 2 ** (61 / 24) * 3 ** 0.25 * math.exp(0.25)

print("STATUS=PASS")
print("max_relative_zero_edge_identity_error=", max_rel_zero)
print("max_minkowski_excess=", max_mink_excess)
print("max_resource_lower_bound_excess=", max_resource_excess)
print("min_observed_resource_ratio=", min_resource_ratio)
print("max_random_cut_mean_relative_error=", max_cut_rel)
print("C_h=", C_h)
print("2C_h=", 2 * C_h)
print("4piC_h=", 4 * math.pi * C_h)
print("K_h=", K_h)
print("L0=", L0)
print("C_hyb=", C_hyb)
print("64^(1/8)C_hyb=", 64 ** (1 / 8) * C_hyb)
