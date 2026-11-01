"""Exact certificates for the four monomial pieces T_k of S_p (star with equal return rates, leaf coin p):
S_p = sum_k p^k q^{3-k} T_k,  T_k = sum over (l,c,c') with exactly k labels equal to 2 of
      psi(l,l,l,l) - psi(l,l,1,c') - psi(1,c,l,l) + psi(1,c,1,c').
Each T_k is written as a nonnegative rational combination of elementary increasing-difference inequalities and the
identity is verified exactly.  T_k >= 0 for k = 0..3 proves S_p >= 0 for every p in [0,1].
"""
import itertools
from fractions import Fraction
import numpy as np
from scipy.optimize import linprog

m = 3
pts = list(itertools.product(range(1, m+1), repeat=4)); idx = {x: i for i, x in enumerate(pts)}; N = len(pts)
elem = []
for x in pts:
    for i in range(4):
        for j in range(i+1, 4):
            if x[i] + 1 <= m and x[j] + 1 <= m:
                xi = list(x); xi[i] += 1; xj = list(x); xj[j] += 1; xij = list(x); xij[i] += 1; xij[j] += 1
                r = np.zeros(N); r[idx[tuple(xij)]] += 1; r[idx[x]] += 1; r[idx[tuple(xi)]] -= 1; r[idx[tuple(xj)]] -= 1
                elem.append((x, i, j, r))
A = np.array([e[3] for e in elem]).T

def term(l, c, cp):
    v = np.zeros(N)
    v[idx[(l, l, l, l)]] += 1; v[idx[(l, l, 1, cp)]] -= 1; v[idx[(1, c, l, l)]] -= 1; v[idx[(1, c, 1, cp)]] += 1
    return v

for k in (0, 1, 2, 3):
    T = sum(term(l, c, cp) for l in (2, 3) for c in (2, 3) for cp in (2, 3) if [l, c, cp].count(2) == k)
    res = linprog(np.ones(A.shape[1]), A_eq=A, b_eq=T, bounds=[(0, None)]*A.shape[1], method="highs")
    assert res.status == 0, (k, res.message)
    W = [Fraction(round(v * 8), 8) for v in res.x]
    tot = [Fraction(0)] * N
    for r_i, (x, i, j, r) in enumerate(elem):
        if W[r_i] == 0: continue
        for p in range(N):
            if r[p]: tot[p] += W[r_i] * Fraction(int(r[p]))
    ok = all(tot[p] == Fraction(int(round(T[p]))) for p in range(N))
    print(f"== T_{k} (coefficient of p^{k} q^{3-k}): exact identity holds: {ok}; terms:")
    for r_i, (x, i, j, r) in enumerate(elem):
        if W[r_i] != 0:
            print(f"     {W[r_i]} * E[{x}; {i+1},{j+1}]")
