import numpy as np
from math import sqrt

rng = np.random.default_rng(20260922)

# Random PSD check of min_j lambda_2(H[T_j]) <= tr(H)/(2K).
max_violation = 0.0
tests = 0
for K in range(1, 9):
    n = 3*K + 5
    for _ in range(200):
        M = rng.normal(size=(n, n))
        H = M @ M.T
        eta = []
        for j in range(K):
            I = np.arange(3*j, 3*j+3)
            ev = np.linalg.eigvalsh(H[np.ix_(I, I)])[::-1]
            eta.append(float(ev[1]))
        max_violation = max(max_violation, min(eta) - np.trace(H)/(2*K))
        tests += 1

# Exact sharp family up to floating arithmetic.
sharp = []
for K in range(1, 9):
    L = 1.0
    n = 3*K
    v1 = np.zeros(n)
    v2 = np.zeros(n)
    for j in range(K):
        v1[3*j] = 1/sqrt(K)
        v2[3*j+1] = 1/sqrt(K)
    H = K*L*(np.outer(v1, v1) + np.outer(v2, v2))
    A = L*np.eye(n) - H
    local_eta = []
    for j in range(K):
        I = np.arange(3*j, 3*j+3)
        evH = np.linalg.eigvalsh(H[np.ix_(I, I)])[::-1]
        local_eta.append(float(evH[1]))
    spec = np.linalg.eigvalsh(A)
    sharp.append((K, float(np.trace(H)/(2*K)), min(local_eta), spec[0], spec[-1]))
    assert abs(np.trace(H)/(2*K) - min(local_eta)) < 1e-10

# Rank-one hostile compression has zero second eigenvalue, independent of magnitude.
rank1_max = 0.0
for K, tau in [(1, 10.0), (2, 100.0), (4, 1e4), (8, 1e6)]:
    n = 3*K
    v = rng.normal(size=n)
    v /= np.linalg.norm(v)
    H = tau*np.outer(v, v)
    for j in range(K):
        I = np.arange(3*j, 3*j+3)
        ev = np.linalg.eigvalsh(H[np.ix_(I, I)])[::-1]
        rank1_max = max(rank1_max, abs(float(ev[1])))

print('PASS')
print('random_psd_tests', tests)
print('max_lhs_minus_rhs', max_violation)
print('sharp_family_rows', sharp)
print('rank1_max_second_eigen_abs', rank1_max)
