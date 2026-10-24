"""Exact certificate for S(psi) >= 0 (P0291, condition C2).

S(psi) = sum_{l,c,c' in {2,3}} [psi(l,l,l,l) - psi(l,l,1,c') - psi(1,c,l,l) + psi(1,c,1,c')].
Elementary supermodular inequalities on {1,2,3}^4:  E[x; i, j](psi) = psi(x+e_i+e_j) - psi(x+e_i) - psi(x+e_j) + psi(x) >= 0.
We find weights w >= 0 with  S = sum w_r E_r  (as linear functionals on R^{81}) by LP, then round to rationals and
verify the identity EXACTLY with fractions.  A valid certificate is a complete proof that S(psi) >= 0 for every
supermodular psi, hence of condition (C2) for the symmetric star chain.
"""
import itertools
from fractions import Fraction
import numpy as np
from scipy.optimize import linprog

m = 3
pts = list(itertools.product(range(1, m+1), repeat=4)); idx = {x: i for i, x in enumerate(pts)}; N = len(pts)
elem = []   # (x, i, j, vector)
for x in pts:
    for i in range(4):
        for j in range(i+1, 4):
            if x[i] + 1 <= m and x[j] + 1 <= m:
                xi = list(x); xi[i] += 1; xj = list(x); xj[j] += 1; xij = list(x); xij[i] += 1; xij[j] += 1
                r = np.zeros(N); r[idx[tuple(xij)]] += 1; r[idx[x]] += 1; r[idx[tuple(xi)]] -= 1; r[idx[tuple(xj)]] -= 1
                elem.append((x, i, j, r))
S = np.zeros(N)
for l in (2, 3):
    for c in (2, 3):
        for cp in (2, 3):
            S[idx[(l, l, l, l)]] += 1; S[idx[(l, l, 1, cp)]] -= 1; S[idx[(1, c, l, l)]] -= 1; S[idx[(1, c, 1, cp)]] += 1
A = np.array([e[3] for e in elem]).T          # N x R
R = A.shape[1]
# feasibility LP: A w = S, w >= 0, minimise sum w (sparse certificate)
res = linprog(np.ones(R), A_eq=A, b_eq=S, bounds=[(0, None)]*R, method="highs")
assert res.status == 0, res.message
w = res.x
print("LP certificate found; total weight", round(res.fun, 6), "; nonzero weights:", int((w > 1e-9).sum()))
# exact verification with rationals (weights rounded to nearest 1/4)
W = [Fraction(round(v * 4), 4) for v in w]
tot = [Fraction(0)] * N
for k, (x, i, j, r) in enumerate(elem):
    if W[k] == 0: continue
    for p in range(N):
        if r[p] != 0: tot[p] += W[k] * Fraction(int(r[p]))
ok = all(tot[p] == Fraction(int(S[p])) for p in range(N))
print("EXACT rational identity S = sum w_r E_r holds:", ok)
for k, (x, i, j, r) in enumerate(elem):
    if W[k] != 0:
        y = list(x); y[i] += 1; y[j] += 1
        print(f"  {W[k]} * [ psi{tuple(y)} - psi{tuple(x[:i]+(x[i]+1,)+x[i+1:])} - psi{tuple(x[:j]+(x[j]+1,)+x[j+1:])} + psi{x} ]")
