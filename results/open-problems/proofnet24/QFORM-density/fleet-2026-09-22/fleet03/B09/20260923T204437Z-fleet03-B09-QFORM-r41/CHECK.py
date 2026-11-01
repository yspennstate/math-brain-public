import itertools
import math
import numpy as np

rng = np.random.default_rng(20260923)

C_overlap = 72 ** (1 / 3)
C_r40 = 3 * 2 ** (4 / 3) * math.e ** (1 / 3)
print(f"C_overlap={C_overlap:.15f}")
print(f"C_r40={C_r40:.15f}")
print(f"C_disjoint_if_D3_ge_half={2*C_r40*2**(1/6):.15f}")

A5 = np.zeros((5, 5))
A5[0, 0] = 1
for i, j in [(1, 3), (2, 4)]:
    A5[i, j] = A5[j, i] = 1
e5 = np.linalg.eigvalsh(A5)
print("A5_eigs=" + np.array2string(e5, precision=12))
print(f"A5_target_large={sum(abs(e5) >= 1 - 1e-12)}")
assert sum(abs(e5) >= 1 - 1e-12) >= 3

A6 = np.zeros((6, 6))
A6[0, 0] = 1
for i, j in [(0, 5), (1, 3), (2, 4)]:
    A6[i, j] = A6[j, i] = 1
e6 = np.linalg.eigvalsh(A6)
K = A6[np.ix_([0, 1, 2], [3, 4, 5])]
print("A6_eigs=" + np.array2string(e6, precision=12))
print(f"A6_detK={np.linalg.det(K):.15f}")
print(f"partner_bound={3*abs(np.linalg.det(K))**(-1/3):.15f}")
print(f"new_bound_after_condition_X5={C_overlap:.15f}")
assert sum(abs(e6) >= 1 - 1e-12) >= 3
assert abs(np.linalg.det(K) - 1) < 1e-12

maxerr1 = 0.0
maxerr2 = 0.0
for _ in range(100):
    n = 9
    M = rng.normal(size=(n, n))
    A = (M + M.T) / 2
    A[0, 0] += 2.5
    h = 0
    idx = list(range(1, n))
    S = A[np.ix_(idx, idx)] - np.outer(A[idx, h], A[h, idx]) / A[h, h]
    P = [1, 2]
    Q = [3, 4]
    lhs = np.linalg.det(A[np.ix_([h] + P, [h] + Q)])
    rhs = A[h, h] * np.linalg.det(S[np.ix_([0, 1], [2, 3])])
    maxerr1 = max(maxerr1, abs(lhs-rhs)/(1+abs(lhs)+abs(rhs)))

    H = [0, 1]
    E = A[np.ix_(H, H)]
    if abs(np.linalg.det(E)) < 1e-6:
        continue
    bar = [i for i in range(n) if i not in H]
    SH = (A[np.ix_(bar, bar)]
          - A[np.ix_(bar, H)] @ np.linalg.inv(E) @ A[np.ix_(H, bar)])
    i, j = 2, 3
    li, lj = bar.index(i), bar.index(j)
    lhs2 = np.linalg.det(A[np.ix_(H + [i], H + [j])])
    rhs2 = np.linalg.det(E) * SH[li, lj]
    maxerr2 = max(maxerr2, abs(lhs2-rhs2)/(1+abs(lhs2)+abs(rhs2)))

print(f"max_rel_scalar_schur_det={maxerr1:.3e}")
print(f"max_rel_pair_schur_det={maxerr2:.3e}")
assert maxerr1 < 1e-12
assert maxerr2 < 1e-12

n = 7
M = rng.normal(size=(n, n))
A = (M + M.T) / 2
triples = list(itertools.combinations(range(n), 3))
E3_sum = 0.0
D3 = 0.0
for R in triples:
    for C in triples:
        d = np.linalg.det(A[np.ix_(R, C)])
        E3_sum += d*d
        if set(R).isdisjoint(C):
            D3 += d*d

evals = np.linalg.eigvalsh(A)
E3_spec = sum((evals[i]*evals[j]*evals[k])**2 for i, j, k in triples)

zsum = 0.0
for mask in range(1 << n):
    I = [i for i in range(n) if (mask >> i) & 1]
    J = [i for i in range(n) if not ((mask >> i) & 1)]
    if len(I) < 3 or len(J) < 3:
        continue
    B = A[np.ix_(I, J)]
    BB = B @ B.T
    for rr in itertools.combinations(range(len(I)), 3):
        zsum += np.linalg.det(BB[np.ix_(rr, rr)])
avg = zsum/(1 << n)
err_cb = abs(E3_sum-E3_spec)/(1+abs(E3_spec))
err_part = abs(avg-D3/64)/(1+abs(D3/64))
print(f"E3_cauchy_rel={err_cb:.3e}")
print(f"D3_partition_rel={err_part:.3e}")
assert err_cb < 1e-12
assert err_part < 1e-12
print("ALL CHECKS PASSED")
