"""P0291, condition (C2) reduced to a finite inequality.

Under the monotone skeleton coupling the prefix configurations (A^x, x) for x = 1,2,3 differ only on the current
block I of the leaf-started chain: value x for x in {2,3}; for x = 1 the value is 1 on I \ O and a fair coin c on the
overlap O (O = the part of I after the center-started chain has jumped up and coalesced).  Same for the suffix with
J, O', c'.  Writing psi(u, u', v, v') for phi with the four blocks I\O, O, J\O', O' set to constants (psi is
supermodular on {1,2,3}^4 whenever phi is), condition (C2) integrates to

    S(psi) = sum_{l in {2,3}} sum_{c, c' in {2,3}} [ psi(l,l,l,l) - psi(l,l,1,c') - psi(1,c,l,l) + psi(1,c,1,c') ] >= 0 .

This script minimises S over supermodular psi with |psi| <= 1 (LP).  min >= 0  <=>  (C2) holds pointwise in the
base randomness, for every rate pair (a,b), and the single-gap monotonicity (hence the whole supermodular
time-ordering) of the symmetric star chain follows.  It also checks the degenerate cases O empty and/or O' empty
(psi independent of u' and/or v'), and (C1) in the same language as a control.
"""
import itertools
import numpy as np
from scipy.optimize import linprog

m = 3
pts = list(itertools.product(range(1, m+1), repeat=4)); idx = {x: i for i, x in enumerate(pts)}; N = len(pts)

def supermod_rows(extra_equal=()):
    rows = []
    for x in pts:
        for i in range(4):
            for j in range(i+1, 4):
                if x[i] + 1 <= m and x[j] + 1 <= m:
                    xi = list(x); xi[i] += 1; xj = list(x); xj[j] += 1; xij = list(x); xij[i] += 1; xij[j] += 1
                    r = np.zeros(N); r[idx[tuple(xij)]] += 1; r[idx[x]] += 1; r[idx[tuple(xi)]] -= 1; r[idx[tuple(xj)]] -= 1
                    rows.append(-r)
    return np.array(rows)

def equality_rows(dead):
    """psi independent of the coordinates in `dead` (empty overlap blocks)"""
    eq = []
    for x in pts:
        for d in dead:
            if x[d] + 1 <= m:
                y = list(x); y[d] += 1
                r = np.zeros(N); r[idx[x]] += 1; r[idx[tuple(y)]] -= 1; eq.append(r)
    return np.array(eq) if eq else None

def S_vector():
    c = np.zeros(N)
    for l in (2, 3):
        for cc in (2, 3):
            for cp in (2, 3):
                c[idx[(l, l, l, l)]] += 1; c[idx[(l, l, 1, cp)]] -= 1; c[idx[(1, cc, l, l)]] -= 1; c[idx[(1, cc, 1, cp)]] += 1
    return c

def C1_vector():
    c = np.zeros(N)
    c[idx[(2,2,2,2)]] += 1; c[idx[(3,3,3,3)]] += 1; c[idx[(2,2,3,3)]] -= 1; c[idx[(3,3,2,2)]] -= 1
    return c

A = supermod_rows()
for name, vec in (("S (condition C2)", S_vector()), ("C1 control", C1_vector())):
    for dead in ((), (1,), (3,), (1, 3)):
        E = equality_rows(dead)
        res = linprog(vec, A_ub=A, b_ub=np.zeros(A.shape[0]), A_eq=E, b_eq=np.zeros(E.shape[0]) if E is not None else None,
                      bounds=[(-1, 1)]*N, method="highs")
        assert res.status == 0, res.message
        print(f"{name}: dead blocks {dead}: min over supermodular psi = {res.fun:+.6f}")
