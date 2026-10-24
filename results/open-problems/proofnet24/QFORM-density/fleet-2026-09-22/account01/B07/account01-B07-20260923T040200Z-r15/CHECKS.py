import itertools
import math
import numpy as np


def e_t(A, t):
    m, n = A.shape
    if min(m, n) < t:
        return 0.0
    out = 0.0
    for R in itertools.combinations(range(m), t):
        for C in itertools.combinations(range(n), t):
            out += np.linalg.det(A[np.ix_(R, C)]) ** 2
    return float(out)


def anchored_h(M, i, j, u):
    m, n = M.shape
    if min(m, n) < u:
        return 0.0
    out = 0.0
    rr = [x for x in range(m) if x != i]
    cc = [x for x in range(n) if x != j]
    for R0 in itertools.combinations(rr, u - 1):
        R = (i,) + R0
        for C0 in itertools.combinations(cc, u - 1):
            C = (j,) + C0
            out += np.linalg.det(M[np.ix_(R, C)]) ** 2
    return float(out)


def anchored_sigma(M, i, j, t, tol=1e-10):
    m, n = M.shape
    out = 0.0
    for k in range(m):
        if k == i:
            continue
        for l in range(n):
            if l == j:
                continue
            P = [i, k]
            Q = [j, l]
            B = M[np.ix_(P, Q)]
            d = float(np.linalg.det(B))
            if abs(d) <= tol:
                continue
            RR = [x for x in range(m) if x not in P]
            CC = [x for x in range(n) if x not in Q]
            S = (M[np.ix_(RR, CC)]
                 - M[np.ix_(RR, Q)] @ np.linalg.inv(B) @ M[np.ix_(P, CC)])
            out += d * d * e_t(S, t)
    return out


def check_matrix(M):
    m, n = M.shape
    for i in range(m):
        for j in range(n):
            for t in (1, 2, 3):
                if t + 2 > min(m, n):
                    continue
                H = anchored_h(M, i, j, t + 2)
                if H <= 1e-10:
                    continue
                S = anchored_sigma(M, i, j, t)
                assert S + 1e-7 >= H
                assert S <= (t + 1) ** 2 * H + 1e-7 * max(1.0, H)


rng = np.random.default_rng(20260923)
for shape in ((5, 5), (6, 7), (4, 6)):
    for _ in range(20):
        check_matrix(rng.normal(size=shape))

# Sparse controls. The 3-cycle attains the lower multiplicity one for a suitable anchor.
check_matrix(np.array([[0., 1., 0.], [0., 0., 1.], [1., 0., 0.]]))
check_matrix(np.eye(5))
for _ in range(100):
    M = rng.integers(-1, 2, size=(5, 5)).astype(float)
    if abs(np.linalg.det(M)) > 1e-9:
        check_matrix(M)

# Constant identity in the partner-scale application.
theta = 1.0 / 16.0
eta_star = theta ** 6 / (120.0 * 3072.0 ** 2)
gamma = (24.0 / 5.0) * theta ** 4 / 3072.0 ** 2
rho = theta ** 2 / (16.0 * math.sqrt(5.0))
assert abs(gamma / rho ** 2 - 1.0 / 1536.0) < 1e-15
assert abs((1.0 / 16.0) ** 2 / 6.0 - 1.0 / 1536.0) < 1e-15

print('QFORM_ANCHORED_SCHUR_COMPOUND_CHECK_PASS')
print('eta_star=', eta_star)
print('gamma=', gamma)
print('rho=', rho)
print('gamma_over_rho2=', gamma / rho ** 2)
