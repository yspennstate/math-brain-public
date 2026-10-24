"""Exact integer check of the key lemma |fhat(S)| <= 2^{|S|-1} I_S(f), i.e. W_S^2 4^n <= 4^{|S|-1} (sum_{T>=S} W_T^2)^2
for all S != empty, all Boolean f with n<=4, and random f with n<=9."""
import numpy as np
from feilib import all_tables, hadamard, fwht_int, sizes

def superset_int(a, n):
    b = a.copy(); idx = np.arange(1 << n)
    for j in range(n):
        lo = idx[(idx >> j) & 1 == 0]; b[..., lo] += b[..., lo | (1 << j)]
    return b

viol = 0; tight = 0; total = 0
for n in [1, 2, 3, 4]:
    T = all_tables(n).astype(np.int64); W = T @ hadamard(n).T
    W2 = W * W; Pi = superset_int(W2, n); s = sizes(n)
    for S in range(1, 1 << n):
        lhs = W2[:, S] * (4 ** n); rhs = (4 ** (s[S] - 1)) * Pi[:, S] ** 2
        viol += int((lhs > rhs).sum()); tight += int(((lhs == rhs) & (lhs > 0)).sum()); total += len(lhs)
print('n<=4 exhaustive: pairs', total, 'violations', viol, 'equalities (nonzero)', tight)
rng = np.random.default_rng(7); viol = 0; total = 0
for trial in range(300):
    n = int(rng.integers(5, 10)); t = rng.choice([-1, 1], size=1 << n)
    if trial % 3 == 0:  # structured: sparse perturbation of a constant
        t = np.ones(1 << n, dtype=np.int64); t[rng.choice(1 << n, size=int(rng.integers(1, 6)), replace=False)] = -1
    W = fwht_int(t).astype(object); W2 = np.array([int(w) * int(w) for w in W], dtype=object)
    Pi = W2.copy(); idx = np.arange(1 << n)
    for j in range(n):
        lo = idx[(idx >> j) & 1 == 0]; Pi[lo] = Pi[lo] + Pi[lo | (1 << j)]
    s = sizes(n)
    for S in range(1, 1 << n):
        total += 1
        if W2[S] * (4 ** n) > (4 ** (int(s[S]) - 1)) * Pi[S] ** 2: viol += 1
print('random n=5..9 (300 functions): pairs', total, 'violations', viol)
