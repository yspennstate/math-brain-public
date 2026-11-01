import itertools
import numpy as np


def anchored_z(B, i, j):
    rows = [a for a in range(B.shape[0]) if a != i]
    cols = [b for b in range(B.shape[1]) if b != j]
    z = 0.0
    for R in itertools.combinations(rows, 2):
        for T in itertools.combinations(cols, 2):
            z += np.linalg.det(B[np.ix_((i,) + R, (j,) + T)]) ** 2
    return z


def e2(S):
    z = 0.0
    for R in itertools.combinations(range(S.shape[0]), 2):
        for T in itertools.combinations(range(S.shape[1]), 2):
            z += np.linalg.det(S[np.ix_(R, T)]) ** 2
    return z


rng = np.random.default_rng(0)
err_nonzero = []
err_zero = []
for _ in range(100):
    B = rng.normal(size=(5, 6))
    i, j = 1, 2
    rr = [a for a in range(B.shape[0]) if a != i]
    cc = [b for b in range(B.shape[1]) if b != j]

    b = B[i, j]
    c = B[rr, j]
    r = B[i, cc]
    D = B[np.ix_(rr, cc)]
    S = D - np.outer(c, r) / b
    lhs = anchored_z(B, i, j)
    rhs = b * b * e2(S)
    err_nonzero.append(abs(lhs - rhs) / (1.0 + abs(lhs)))

    B0 = B.copy()
    B0[i, j] = 0.0
    c = B0[rr, j]
    r = B0[i, cc]
    D = B0[np.ix_(rr, cc)]
    nr = np.linalg.norm(r)
    nc = np.linalg.norm(c)
    Pr = np.eye(len(r)) - np.outer(r, r) / nr**2
    Pc = np.eye(len(c)) - np.outer(c, c) / nc**2
    lhs = anchored_z(B0, i, j)
    rhs = nr**2 * nc**2 * np.linalg.norm(Pc @ D @ Pr, 'fro') ** 2
    err_zero.append(abs(lhs - rhs) / (1.0 + abs(lhs)))

print('trials=100')
print('max_relative_error_nonzero=', max(err_nonzero))
print('max_relative_error_zero=', max(err_zero))
