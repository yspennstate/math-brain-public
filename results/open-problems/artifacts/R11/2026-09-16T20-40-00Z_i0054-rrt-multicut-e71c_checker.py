#!/usr/bin/env python3
"""
R11 / I0054 exact finite self-check for the random-recursive-tree multi-cut
hierarchy (RRT-MC).

Checks only finite algebra/combinatorics:
  1. Exact expected fringe-subtree counts in ordinary random recursive trees:
       E Z_{m,s} = m/[s(s+1)].
  2. Exact sampled visible-hazard identity:
       sum_s E Z_{m,s} w_m(s) P(sample intersection=A | |subtree|=s)
       = (1/2) B(i,b-i),
     for w_m(s)=(s+1)/(2(m-s)).
  3. Exact total expected edge weight = H_{m-1}.
  4. Exact N=3 positive three-way split witness for the multi-cut model.
  5. Pairwise separation of the finite three-way witnesses from earlier
     R11 classes: CTCS/HGPF=0, RRT-MC=1/118098, C002 nCRP=1/28,
     C003 ternary Dirichlet=2/135, C004 positive-discount PY=6/91.
  6. Raw mark probabilities are valid for delta_N=N^-5, and the crude
     >=2-mark bound is o(delta_N).

This checker does NOT establish the asymptotic CTCS convergence theorem.
"""
from fractions import Fraction
from itertools import product
from math import comb, factorial

def beta_int(a,b):
    return Fraction(factorial(a-1)*factorial(b-1), factorial(a+b-1))

def subtree_sizes_from_parents(n, parents):
    children={i:[] for i in range(1,n+1)}
    for j,p in enumerate(parents, start=2):
        children[p].append(j)
    sizes=[0]*(n+1)
    def dfs(v):
        z=1
        for c in children[v]:
            z += dfs(c)
        sizes[v]=z
        return z
    dfs(1)
    return sizes

# 1. Enumerate all standard recursive trees through n=9.
for n in range(2,10):
    total=1
    for j in range(2,n+1):
        total *= (j-1)
    counts=[0]*(n+1)
    ranges=[range(1,j) for j in range(2,n+1)]
    seen=0
    for parents in product(*ranges):
        seen += 1
        sizes=subtree_sizes_from_parents(n, parents)
        for v in range(2,n+1):
            counts[sizes[v]] += 1
    assert seen == total
    for s in range(1,n):
        lhs=Fraction(counts[s], total)
        rhs=Fraction(n, s*(s+1))
        assert lhs == rhs, (n,s,lhs,rhs)
print("fringe exact enumeration PASS")

# 2. Exact sampled visible-hazard identity.
checks=0
for m in range(2,31):
    for b in range(2,m+1):
        for i in range(1,b):
            R=Fraction(0)
            for s in range(i, m-(b-i)+1):
                EZ=Fraction(m, s*(s+1))
                w=Fraction(s+1, 2*(m-s))
                hyp=Fraction(comb(m-b, s-i), comb(m,s))
                R += EZ*w*hyp
            target=Fraction(1,2)*beta_int(i,b-i)
            assert R == target, (m,b,i,R,target)
            checks += 1
print("hazard identity PASS", checks)

# 3. Exact total expected weighted edge hazard.
for m in range(2,101):
    total=Fraction(0)
    for s in range(1,m):
        total += Fraction(m, s*(s+1))*Fraction(s+1,2*(m-s))
    H=sum((Fraction(1,j) for j in range(1,m)), Fraction(0))
    assert total == H
print("total hazard PASS")

# 4. N=3 exact three-way root split witness.
N=3
delta=Fraction(1,N**5)
w1=Fraction(1+1, 2*(3-1))
w2=Fraction(2+1, 2*(3-2))
p3=Fraction(1,2)*(delta*w1)**2 + Fraction(1,2)*(delta*w1)*(delta*w2)
assert p3 == Fraction(1,118098)
print("RRT-MC three-way witness PASS", p3)

# 5. Pairwise finite witnesses against earlier counted classes.
ctcs_hgpf=Fraction(0)
rrtmc=p3
ncrp=Fraction(1,28)
ternary=Fraction(2,135)
py=Fraction(1,3)*Fraction(1,2) / (Fraction(7,6)*Fraction(13,6))
assert py == Fraction(6,91)
vals=[ctcs_hgpf, rrtmc, ncrp, ternary, py]
assert len(set(vals)) == len(vals)
print("finite-class witness separation PASS", *vals)

# 6. Mark validity and crude multi-mark error.
for N in range(2,501):
    d=Fraction(1,N**5)
    for m in range(2,N+1):
        for s in (1, m-1):
            w=Fraction(s+1,2*(m-s))
            assert d*w <= Fraction(1,2*N**4)
    err=Fraction(1,8*N**6)
    assert err/d == Fraction(1,8*N)
print("mark bounds PASS")
print("ALL_EXACT_CHECKS_PASS")
