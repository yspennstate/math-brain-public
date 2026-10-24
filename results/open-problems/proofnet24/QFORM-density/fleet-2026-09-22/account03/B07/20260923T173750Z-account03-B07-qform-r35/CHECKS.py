from itertools import combinations
from math import ceil, exp, sqrt
import random
import numpy as np


def det2(M, rows, cols):
    i, k = rows
    j, l = cols
    return int(M[i, j])*int(M[k, l]) - int(M[i, l])*int(M[k, j])


def det3(M, rows, cols):
    a = [[int(M[i, j]) for j in cols] for i in rows]
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
            - a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
            + a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))


def e2_minors(M):
    return sum(det2(M, rr, cc)**2
               for rr in combinations(range(M.shape[0]), 2)
               for cc in combinations(range(M.shape[1]), 2))


def e3_minors(M):
    if min(M.shape) < 3:
        return 0
    return sum(det3(M, rr, cc)**2
               for rr in combinations(range(M.shape[0]), 3)
               for cc in combinations(range(M.shape[1]), 3))


def mixed_21(K, Y):
    m, n = K.shape
    T = np.concatenate([K, Y], axis=1)
    return sum(det3(T, rr, (a, b, n+j))**2
               for rr in combinations(range(m), 3)
               for a, b in combinations(range(n), 2)
               for j in range(Y.shape[1]))


def exact_trace_identity(K, Y):
    Ko = np.array(K, dtype=object)
    Yo = np.array(Y, dtype=object)
    T = np.concatenate([Ko, Yo], axis=1)
    B = Ko @ Ko.T
    S = sum(B[i, i] for i in range(B.shape[0]))
    Z = e2_minors(np.asarray(K, dtype=int))
    H = B @ B - S*B + Z*np.eye(B.shape[0], dtype=object)
    lhs = 0
    for j in range(T.shape[1]):
        y = T[:, j]
        lhs += sum(y[i]*sum(H[i, k]*y[k] for k in range(len(y)))
                   for i in range(len(y)))
    rhs = 3*e3_minors(np.asarray(K, dtype=int)) + mixed_21(np.asarray(K, dtype=int), np.asarray(Y, dtype=int))
    V = e3_minors(np.concatenate([np.asarray(K, dtype=int), np.asarray(Y, dtype=int)], axis=1))
    assert int(lhs) == int(rhs)
    assert int(lhs) <= 3*V


random.seed(20260923)
exact_cases = 0
for m in range(3, 6):
    for n in range(2, 5):
        for p in range(1, 4):
            for _ in range(10):
                K = np.array([[random.randint(-3, 3) for _ in range(n)] for __ in range(m)], dtype=int)
                Y = np.array([[random.randint(-3, 3) for _ in range(p)] for __ in range(m)], dtype=int)
                exact_trace_identity(K, Y)
                exact_cases += 1

# Numerical regression of the spectral projection inequality.
spectral_cases = 0
rng = np.random.default_rng(20260923)
for m in range(3, 7):
    for n in range(2, 6):
        for p in range(1, 4):
            for _ in range(30):
                K = rng.integers(-4, 5, size=(m, n)).astype(float)
                Y = rng.integers(-4, 5, size=(m, p)).astype(float)
                B = K @ K.T
                x, U = np.linalg.eigh(B)
                x = np.maximum(x, 0.0)
                S = float(x.sum())
                Z = sum(float(x[i]*x[j]) for i in range(m) for j in range(i+1, m))
                if Z < 1e-10:
                    continue
                alpha = x*(S-x)/Z
                heavy = alpha > (2.0/3.0 + 1e-10)
                assert int(heavy.sum()) <= 2
                P = U[:, heavy] @ U[:, heavy].T if heavy.any() else np.zeros((m, m))
                T = np.concatenate([K, Y], axis=1)
                lam = np.maximum(np.linalg.eigvalsh(T @ T.T), 0.0)
                V = sum(float(lam[i]*lam[j]*lam[k])
                        for i in range(m) for j in range(i+1, m) for k in range(j+1, m))
                lhs = np.linalg.norm((np.eye(m)-P) @ T, 'fro')**2
                rhs = 9.0*V/Z
                assert lhs <= rhs*(1+1e-7) + 1e-7
                spectral_cases += 1

h = (2*sqrt(2)-1)/1572864
zcoef = 854675.100194511
C_E3 = 3*(2**(4/3))*exp(1/3)
tube_factor = 3/sqrt(zcoef)
density_bound = C_E3/h
det_cap = (sqrt(3)*h/8)**3
minor_count = ceil(h**6/det_cap**2 - 1e-12)
assert minor_count == 9710

print(f'exact_integer_identity_cases={exact_cases}')
print(f'spectral_projection_cases={spectral_cases}')
print(f'h={h:.16e}')
print(f'C_E3={C_E3:.15f}')
print(f'C_E3_over_h={density_bound:.9f}')
print(f'tube_factor={tube_factor:.15f}')
print(f'absolute_tube_scale={tube_factor*h:.16e}')
print(f'nonzero_3x3_minor_count_lower_bound={minor_count}')
print('STATUS=PASS')
