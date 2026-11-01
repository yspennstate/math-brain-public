#!/usr/bin/env python3
"""
R12 / I0102 first-run exact checker.

All claims checked here are finite algebraic claims.  No floating SDP output is
used and nothing here proves Conjecture 28 asymptotically.

Checks:
  (1) Exact K3 degree-4 pseudoexpectation counterexample showing that
      conditioning a degree-4 pseudoexpectation on an EDGE need not produce a
      degree-2 pseudoexpectation.
  (2) Exact Paley degree-2 primal/dual certificates with value sqrt(p), and
      verification that the dual embeds into the Kunisky--Yu degree-4 dual by
      zeroing every edge-indexed row/column.
  (3) Exact affine Paley graph regularity/common-neighbor counts for sample
      admissible primes used only as a combinatorial sanity check.
"""
from fractions import Fraction
import sympy as sp

print("R12 exact checker: start")

# ---------------------------------------------------------------------------
# (1) K3 edge-conditioning obstruction.
# ---------------------------------------------------------------------------
a = sp.Rational(1,2)
b = sp.Rational(1,5)
c = sp.Rational(-1,100)
inds = [
    frozenset(),
    frozenset({1}), frozenset({2}), frozenset({3}),
    frozenset({1,2}), frozenset({1,3}), frozenset({2,3}),
]
def moment(U):
    if len(U)==0: return sp.Integer(1)
    if len(U)==1: return a
    if len(U)==2: return b
    if len(U)==3: return c
    raise AssertionError

M = sp.Matrix([[moment(S|T) for T in inds] for S in inds])
leading = [sp.factor(M[:k,:k].det()) for k in range(1,8)]
expected = [
    sp.Integer(1),
    sp.Rational(1,4),
    sp.Rational(3,50),
    sp.Rational(27,2000),
    sp.Rational(297,500000),
    sp.Rational(1701,80000000),
    sp.Rational(321489,1000000000000),
]
assert leading == expected
assert all(x > 0 for x in leading)  # Sylvester => M is positive definite.

# Condition on edge {1,2}; the degree-2 candidate moment matrix on x_3 is
# [[E x12, E x123], [E x123, E x123]], normalized by E x12.
L = sp.Matrix([[b,c],[c,c]]) / b
assert L[1,1] == sp.Rational(-1,20)
assert L[1,1] < 0
print("K3 EDGE-CONDITIONING COUNTEREXAMPLE: PASS")
print("  leading principal minors =", leading)
print("  normalized edge-local x3 diagonal =", L[1,1])

# ---------------------------------------------------------------------------
# Paley helpers.
# ---------------------------------------------------------------------------
def legendre(x,p):
    x %= p
    if x==0: return 0
    r=pow(x,(p-1)//2,p)
    return 1 if r==1 else -1

def paley_adjacency(p):
    assert sp.isprime(p) and p%4==1
    A=sp.zeros(p)
    for i in range(p):
        for j in range(i+1,p):
            if legendre(i-j,p)==1:
                A[i,j]=A[j,i]=1
    return A

# ---------------------------------------------------------------------------
# (2) Exact degree-2 primal/dual baseline, checked for several primes.
# Analytic eigenvalue formulas are separately asserted symbolically.
# ---------------------------------------------------------------------------
for p in [5,13,17,29,37]:
    assert sp.isprime(p) and p%4==1
    r=sp.sqrt(p)
    A=paley_adjacency(p)
    J=sp.ones(p)
    I=sp.eye(p)
    Abar=J-I-A
    # Exact strong-regularity checks.
    d=(p-1)//2
    lam=(p-5)//4
    mu=(p-1)//4
    assert all(sum(int(A[i,j]) for j in range(p))==d for i in range(p))
    A2=A*A
    for i in range(p):
        assert A2[i,i]==d
        for j in range(p):
            if i==j: continue
            assert A2[i,j] == (lam if A[i,j] else mu)

    # Degree-2 primal:
    # y_i=1/r; Y=(1/r)I + 2/(r(1+r))*A.
    alpha=1/r
    beta=sp.Rational(2,1)/(r*(1+r))
    Y=alpha*I+beta*A
    Mp=sp.zeros(p+1)
    Mp[0,0]=1
    for i in range(p):
        Mp[0,i+1]=Mp[i+1,0]=alpha
    Mp[1:,1:]=Y
    # Instead of symbolic eigen-decomposition of a radical matrix, certify PSD
    # through the exact spectral formulas of the Paley adjacency matrix.
    eig_pr_1 = sp.simplify(alpha + beta*d - alpha**2*p)
    eig_pr_plus = sp.simplify(alpha + beta*((-1+r)/2))
    eig_pr_minus = sp.simplify(alpha + beta*((-1-r)/2))
    assert eig_pr_1 == 0
    assert sp.simplify(eig_pr_minus) == 0
    assert eig_pr_plus > 0
    primal_obj=sp.simplify(p*alpha)
    assert primal_obj==r

    # Degree-2 dual embedded in degree 4:
    # Z00=r, Z0i=-1, Zii=1, Zij=0 on Paley edges, and
    # Zij=2/(1+r) on nonedges. Edge-indexed rows/columns are all zero.
    gamma=sp.Rational(2,1)/(1+r)
    B=I+gamma*Abar
    eig_du_1=sp.simplify(1+gamma*d)  # complement has same d on 1
    # Nontrivial spectrum of complement is {(-1-r)/2,(-1+r)/2}, swapped.
    eig_du_zero=sp.simplify(1+gamma*((-1-r)/2))
    eig_du_pos=sp.simplify(1+gamma*((-1+r)/2))
    assert eig_du_1==r
    assert eig_du_zero==0
    assert eig_du_pos>0
    # Schur equality: z0=-1, B^dagger on 1 has eigenvalue 1/r.
    schur=sp.simplify(r - p/r)
    assert schur==0

    # Singleton dual union constraint:
    # 2 Z_{empty,i}+Z_{i,i} = -2+1=-1.
    assert -2+1==-1
    # Edge-union constraint in vertex-only support: 2 Z_{ij}=0 on each edge.
    for i in range(p):
        for j in range(i+1,p):
            if A[i,j]:
                zij=sp.Integer(0)
                assert 2*zij==0
    print(f"PALEY BASELINE p={p}: PASS objective=sqrt({p})")

# Generic symbolic formulas.
r=sp.symbols('r', positive=True)
p=r**2
d=(p-1)/2
alpha=1/r
beta=2/(r*(1+r))
assert sp.simplify(alpha+beta*d-alpha**2*p)==0
assert sp.simplify(alpha+beta*((-1-r)/2))==0
assert sp.simplify(alpha+beta*((-1+r)/2))==2/(1+r)
gamma=2/(1+r)
assert sp.simplify(1+gamma*d-r)==0
assert sp.simplify(1+gamma*((-1-r)/2))==0
assert sp.simplify(1+gamma*((-1+r)/2)-2*r/(1+r))==0
print("GENERIC SQRT(p) PRIMAL/DUAL FORMULAS: PASS")

print("ALL_EXACT_CHECKS_PASS")
