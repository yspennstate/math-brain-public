#!/usr/bin/env python3
from fractions import Fraction
from functools import lru_cache
from math import factorial

@lru_cache(None)
def partitions(n, max_part=None):
    if max_part is None or max_part > n:
        max_part = n
    if n == 0:
        return ((),)
    out = []
    for a in range(max_part, 0, -1):
        for tail in partitions(n-a, min(a, n-a)):
            out.append((a,)+tail)
    return tuple(out)

@lru_cache(None)
def fdim(mu):
    n = sum(mu)
    if n == 0:
        return 1
    h = 1
    for r,rowlen in enumerate(mu):
        for c in range(rowlen):
            below = sum(1 for rr in range(r+1,len(mu)) if mu[rr] > c)
            h *= rowlen-c+below
    return factorial(n)//h

def contents(mu):
    return [c-r for r,rowlen in enumerate(mu,1) for c in range(1,rowlen+1)]

def B_coeffs(mu,j,M):
    cs = contents(mu)
    B = [Fraction(0)]*(M+1)
    for m in range(1,M+1):
        B[m] = Fraction(-sum((j+x)**m-(j+x-1)**m for x in cs), m)
    return B

def D_coeffs(j,M=9):
    # A_j(t)=E_Plancherel exp(2 sum_{m>=1} B_m t^m)
    a = [Fraction(0)]*(M+1)
    a[0] = Fraction(1)
    fj = factorial(j)
    for mu in partitions(j):
        wt = Fraction(fdim(mu)**2, fj)
        B = B_coeffs(mu,j,M)
        r = [Fraction(0)]*(M+1)
        r[0] = Fraction(1)
        for m in range(1,M+1):
            r[m] = sum(Fraction(2*s)*B[s]*r[m-s] for s in range(1,m+1))/m
        for m in range(1,M+1):
            a[m] += wt*r[m]
    D = [Fraction(0)]*(M+1)
    for m in range(1,M+1):
        D[m] = a[m] - sum((Fraction(s)*D[s]*a[m-s] for s in range(1,m)), Fraction(0))/Fraction(m)
    return D

def D9_formula(j):
    p = (90*j**8 + 900*j**7 - 2520*j**6 - 8820*j**5
         + 40212*j**4 - 52635*j**3 + 17640*j**2 + 14820*j - 9677)
    return Fraction(-j*p,45)

def curvature_formula(j):
    p = (216*j**7 + 1680*j**6 - 2772*j**5 - 4620*j**4
         + 21432*j**3 - 28194*j**2 + 15810*j - 3049)
    return Fraction(2*p,3)

def R(mu,n,j):
    z = Fraction(1)
    for c in range(1, (mu[0] if mu else 0)+1):
        h = sum(1 for row in mu if row >= c)
        a = n-j-c+1
        assert a > 0
        z *= Fraction(a, a+h)
    return z

def A(n,j):
    s = Fraction(0)
    fj = factorial(j)
    for mu in partitions(j):
        rr = R(mu,n,j)
        s += Fraction(fdim(mu)**2,fj)*rr*rr
    return s

def Q(n,j):
    return (Fraction(j+1,j)*Fraction(n-j+1,n-j)**2
            * A(n,j)**2/(A(n,j-1)*A(n,j+1)))

def ceil_nth_root(A,p):
    hi = 1
    while hi**p < A:
        hi *= 2
    lo = hi//2
    while lo+1 < hi:
        mid=(lo+hi)//2
        if mid**p >= A:
            hi=mid
        else:
            lo=mid
    return hi

# RSK/shadow criterion for the exact n=3 matroid obstruction.
def rsk_partial(pairs):
    P=[]; Q=[]
    for x,y in sorted(pairs):
        v=y; r=0
        while True:
            if r == len(P):
                P.append([v]); Q.append([x]); break
            row=P[r]
            idx=next((i for i,a in enumerate(row) if a>v), len(row))
            if idx == len(row):
                row.append(v); Q[r].append(x); break
            row[idx],v=v,row[idx]
            r += 1
    return P,Q

def valid_shadow(n,pairs):
    P,Q=rsk_partial(tuple(sorted(pairs)))
    usedx={x for x,y in pairs}; usedy={y for x,y in pairs}
    ux=sorted(set(range(1,n+1))-usedx)
    uy=sorted(set(range(1,n+1))-usedy)
    if P and (len(uy)<len(P[0]) or len(ux)<len(Q[0])):
        return False
    if P:
        if any(not (uy[c] < v) for c,v in enumerate(P[0])):
            return False
        if any(not (ux[c] < v) for c,v in enumerate(Q[0])):
            return False
    return True

Aset=frozenset({(2,2)})
Bset=frozenset({(2,3),(3,2)})
assert valid_shadow(3,Aset)
assert valid_shadow(3,Bset)
assert all(not valid_shadow(3,Aset|{e}) for e in Bset-Aset)
print("shadow_matroid_augmentation_obstruction_n3=PASS")
print("A={(2,2)} B={(2,3),(3,2)} both_valid=True no_B_minus_A_augmentation=True")

vals=[]
for j in range(13):
    d9=D_coeffs(j,9)[9]
    vals.append(d9)
    assert d9 == D9_formula(j), (j,d9,D9_formula(j))
print("D9_exact_partition_values_j0_12=PASS")
print("D9_values=" + ",".join(str(v) for v in vals))

for j in range(1,120):
    lhs = 2*D9_formula(j)-D9_formula(j-1)-D9_formula(j+1)
    assert lhs == curvature_formula(j)
    assert lhs > 0
print("D9_curvature_formula_j1_119=PASS")

# With m=j-1, three times the curvature has the following positive coefficients.
shifted=[432,6384,23688,28560,32784,20796,5940,1006]
assert all(c>0 for c in shifted)
print("shifted_3curvature_coefficients_all_positive=True coeffs="+",".join(map(str,shifted)))

thresholds=[]
for j in range(1,13):
    n=ceil_nth_root((2**31)*(j+1)**11,10)
    assert n**10 >= (2**31)*(j+1)**11
    if n>0:
        assert (n-1)**10 < (2**31)*(j+1)**11
    q=Q(n,j)
    assert q>1
    thresholds.append(n)
print("ten_elevenths_thresholds_j1_12="+",".join(map(str,thresholds)))
print("exact_source_margin_at_thresholds_j1_12=PASS")
print("ALL_EXACT_CHECKS_PASS")
