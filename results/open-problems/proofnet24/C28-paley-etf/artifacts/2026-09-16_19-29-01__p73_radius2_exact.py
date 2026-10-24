#!/usr/bin/env python3
# C28 / I0103 exact radius-two certificate around the frozen p=73,m=14 Paley-ETF witness.
# Every finite assertion below is exact. The exhaustive loop uses integer Bareiss elimination.

from itertools import combinations
from math import comb
import sympy as sp
import numpy as np

p = 73
S0 = (0,1,2,3,5,32,38,41,45,46,52,54,58,61)
n = p + 1
m = len(S0)


def legendre(a):
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p-1)//2, p) == 1 else -1


def conference_entry(i,j):
    if i == j:
        return 0
    if i == p or j == p:
        return 1
    return legendre(i-j)


C = np.zeros((n,n), dtype=np.int64)
for i in range(n):
    for j in range(n):
        C[i,j] = conference_entry(i,j)

def submatrix(S):
    idx = np.array(S, dtype=int)
    return C[np.ix_(idx,idx)]


def bareiss_positive_definite(M):
    """Sylvester criterion using exact fraction-free Bareiss elimination.

    For a symmetric integer matrix M, each Bareiss diagonal pivot is the next
    leading principal determinant divided by the preceding positive factor.
    Positivity of every pivot is therefore equivalent to positivity of all
    leading principal minors.
    """
    a = M.tolist() if hasattr(M, 'tolist') else [row[:] for row in M]
    N = len(a)
    prev = 1
    for k in range(N):
        piv = a[k][k]
        if piv <= 0:
            return False, k, piv
        if k == N-1:
            return True, k, piv
        for i in range(k+1,N):
            aik = a[i][k]
            for j in range(i,N):
                num = piv*a[i][j] - aik*a[k][j]
                if k:
                    assert num % prev == 0
                    num //= prev
                a[i][j] = num
                a[j][i] = num
        prev = piv
    raise AssertionError('unreachable')

# Baseline witness exact characteristic polynomial.
x = sp.symbols('x')
A0 = sp.Matrix(submatrix(S0).tolist())
char0 = sp.factor(A0.charpoly(x).as_expr())
expected = (x-5)*(x-3)**2*(x-1)**3*(x+1)**3*(x+3)**3*(x**2+2*x-51)
assert sp.expand(char0-expected) == 0

r = sp.sqrt(73)
s = sp.sqrt(13)
kappa2_witness = sp.simplify((r-1+2*s)/(r-1-2*s))
assert sp.simplify(r-1-2*s > 0) is sp.true

# Radius-two neighbors: remove exactly two witness columns and add exactly two outside columns.
outside = tuple(i for i in range(n) if i not in S0)
expected_count = comb(m,2)*comb(n-m,2)
assert expected_count == 161070

# We prove for every radius-two neighbor T that lambda_min(C_T)>-161/20.
# This is equivalent to positive definiteness of 20*C_T+161*I, which is
# checked exactly by Sylvester/Bareiss. Gershgorin gives lambda_max(C_T)<=13.
checked = 0
for rem in combinations(S0,2):
    base = set(S0)
    base.remove(rem[0]); base.remove(rem[1])
    for add in combinations(outside,2):
        T = tuple(sorted(base | set(add)))
        A = submatrix(T)
        M = 20*A + 161*np.eye(m,dtype=np.int64)
        ok,k,piv = bareiss_positive_definite(M)
        if not ok:
            raise AssertionError((T,k,piv))
        checked += 1
assert checked == expected_count

# Exact condition-number comparison. For a Gram principal submatrix G=I+C/sqrt(73):
#   lambda_min(G) > 1 - 161/(20 sqrt(73)),
#   lambda_max(G) <= 1 + 13/sqrt(73)  (Gershgorin on C).
# Hence kappa(T)^2 is below the following exact upper bound.
kappa2_radius2_ub = sp.simplify((1 + 13/r)/(1 - sp.Rational(161,20)/r))
assert sp.simplify(1 - sp.Rational(161,20)/r > 0) is sp.true
assert sp.simplify(kappa2_witness - kappa2_radius2_ub > 0) is sp.true

print('C28_P73_RADIUS2_EXACT_CERTIFICATE')
print('p=73 m=14')
print('witness_subset=' + repr(S0))
print('witness_charpoly=' + str(char0))
print('witness_kappa2_exact=' + str(kappa2_witness))
print('witness_kappa_30d=' + str(sp.N(sp.sqrt(kappa2_witness),30)))
print('radius2_neighbor_count=' + str(checked))
print('all_neighbors_lambda_min_gt=-161/20')
print('all_neighbors_lambda_max_le=13_by_Gershgorin')
print('radius2_kappa2_upper_exact=' + str(kappa2_radius2_ub))
print('radius2_kappa_upper_30d=' + str(sp.N(sp.sqrt(kappa2_radius2_ub),30)))
print('strict_radius2_local_maximum=PASS')
print('ALL_EXACT_CHECKS_PASS')
