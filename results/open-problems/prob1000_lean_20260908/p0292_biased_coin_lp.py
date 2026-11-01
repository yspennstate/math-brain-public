"""Star with equal return rates b and unequal arrival rates a2, a3 (leaf coin P(2) = p = a2/(a2+a3), q = 1 - p).
Spectral reduction gives (C1) unchanged and (C2_p): Phi11 + p Phi22 + q Phi33 >= p(Phi12+Phi21) + q(Phi13+Phi31).
Under the skeleton coupling this integrates to
    S_p(psi) = sum_l w_l sum_{c,c'} w_c w_c' [psi(l,l,l,l) - psi(l,l,1,c') - psi(1,c,l,l) + psi(1,c,1,c')] >= 0 ?
with w_2 = p, w_3 = q.  LP: minimise S_p over supermodular psi on {1,2,3}^4, |psi| <= 1, for several p.
Also extracts a certificate at each p and checks whether a p-INDEPENDENT decomposition exists in the form
S_p = p^3 T_222 + p^2 q (...) + ... with each coefficient a nonnegative combination (sufficient for all p).
"""
import itertools
import numpy as np
from scipy.optimize import linprog

m = 3
pts = list(itertools.product(range(1, m+1), repeat=4)); idx = {x: i for i, x in enumerate(pts)}; N = len(pts)
rows = []
for x in pts:
    for i in range(4):
        for j in range(i+1, 4):
            if x[i] + 1 <= m and x[j] + 1 <= m:
                xi = list(x); xi[i] += 1; xj = list(x); xj[j] += 1; xij = list(x); xij[i] += 1; xij[j] += 1
                r = np.zeros(N); r[idx[tuple(xij)]] += 1; r[idx[x]] += 1; r[idx[tuple(xi)]] -= 1; r[idx[tuple(xj)]] -= 1
                rows.append(r)
A = np.array(rows)                                    # R x N, each row an elementary inequality (>= 0)

def term(l, c, cp):
    v = np.zeros(N)
    v[idx[(l, l, l, l)]] += 1; v[idx[(l, l, 1, cp)]] -= 1; v[idx[(1, c, l, l)]] -= 1; v[idx[(1, c, 1, cp)]] += 1
    return v

def S_p(p):
    w = {2: p, 3: 1 - p}
    return sum(w[l] * w[c] * w[cp] * term(l, c, cp) for l in (2, 3) for c in (2, 3) for cp in (2, 3))

print("== minimise S_p over supermodular psi, |psi|<=1")
for p in (0.05, 0.2, 0.35, 0.5, 0.65, 0.8, 0.95):
    res = linprog(S_p(p), A_ub=-A, b_ub=np.zeros(A.shape[0]), bounds=[(-1, 1)]*N, method="highs")
    print(f"   p={p}: min = {res.fun:+.6f}")

# monomial decomposition: S_p = sum over (l,c,c') of w_l w_c w_c' term(l,c,c'); group by the multiset of 2s among (l,c,c')
print("== is each monomial coefficient (grouped by number k of '2' labels among l,c,c') itself >= 0 on supermodular psi?")
for k in (0, 1, 2, 3):
    v = sum(term(l, c, cp) for l in (2, 3) for c in (2, 3) for cp in (2, 3) if [l, c, cp].count(2) == k)
    res = linprog(v, A_ub=-A, b_ub=np.zeros(A.shape[0]), bounds=[(-1, 1)]*N, method="highs")
    print(f"   k={k} (coefficient of p^{k} q^{3-k}): min = {res.fun:+.6f}")
