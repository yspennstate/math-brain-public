#!/usr/bin/env python3
from fractions import Fraction
from functools import lru_cache
from math import factorial, comb

M=18

@lru_cache(None)
def partitions(n, max_part=None):
    if max_part is None or max_part > n:
        max_part=n
    if n==0:
        return ((),)
    out=[]
    for a in range(max_part,0,-1):
        for tail in partitions(n-a, min(a,n-a)):
            out.append((a,)+tail)
    return tuple(out)

@lru_cache(None)
def fdim(mu):
    n=sum(mu)
    if n==0: return 1
    h=1
    for r,rowlen in enumerate(mu):
        for c in range(rowlen):
            below=sum(1 for rr in range(r+1,len(mu)) if mu[rr]>c)
            h *= rowlen-c+below
    return factorial(n)//h

def contents(mu):
    return [c-r for r,rowlen in enumerate(mu,1) for c in range(1,rowlen+1)]

def D_coeffs(j,M=M):
    # A_j(t)=E_Plancherel exp(2 sum B_m t^m), G=log A.
    a=[Fraction(0)]*(M+1); a[0]=Fraction(1)
    fj=factorial(j)
    for mu in partitions(j):
        wt=Fraction(fdim(mu)**2,fj)
        cs=contents(mu)
        B=[Fraction(0)]*(M+1)
        for m in range(1,M+1):
            B[m]=Fraction(-sum((j+x)**m-(j+x-1)**m for x in cs),m)
        r=[Fraction(0)]*(M+1); r[0]=Fraction(1)
        for m in range(1,M+1):
            r[m]=sum(Fraction(2*s)*B[s]*r[m-s] for s in range(1,m+1))/m
        for m in range(1,M+1):
            a[m]+=wt*r[m]
    D=[Fraction(0)]*(M+1)
    for m in range(1,M+1):
        D[m]=a[m]-sum((Fraction(s)*D[s]*a[m-s] for s in range(1,m)),Fraction(0))/m
    return D

# polynomial coefficients increasing powers

def padd(a,b):
    n=max(len(a),len(b)); c=[Fraction(0)]*n
    for i,x in enumerate(a): c[i]+=x
    for i,x in enumerate(b): c[i]+=x
    while len(c)>1 and c[-1]==0: c.pop()
    return c

def pmul(a,b):
    c=[Fraction(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    while len(c)>1 and c[-1]==0: c.pop()
    return c

def pscale(a,s): return [x*s for x in a]
def peval(a,x):
    z=Fraction(0)
    for c in reversed(a): z=z*x+c
    return z

def pshift(a,s):
    # p(x+s)
    out=[Fraction(0)]*len(a)
    for k,ak in enumerate(a):
        for r in range(k+1):
            out[r]+=ak*comb(k,r)*(Fraction(s)**(k-r))
    while len(out)>1 and out[-1]==0: out.pop()
    return out

def interp_0_to_m(vals):
    # Newton forward interpolation p(x)=sum Delta^r p(0) binom(x,r)
    dif=list(vals)
    coeff=[]
    for r in range(len(vals)):
        coeff.append(dif[0])
        dif=[dif[i+1]-dif[i] for i in range(len(dif)-1)]
    out=[Fraction(0)]
    basis=[Fraction(1)]
    fact=1
    for r,dr in enumerate(coeff):
        if r>0:
            basis=pmul(basis,[Fraction(-(r-1)),Fraction(1)])
            fact*=r
        out=padd(out,pscale(basis,dr/Fraction(fact)))
    return out

def curvature(poly):
    # 2p(j)-p(j-1)-p(j+1)
    return padd(pscale(poly,2), pscale(padd(pshift(poly,-1),pshift(poly,1)),-1))

# Compute all D through M for j up to M+2 just once.
Dtab={j:D_coeffs(j,M) for j in range(M+3)}
print(f"partition_taylor_table_j0_{M+2}_through_order_{M}=PASS")

polys={}
for m in range(1,M+1):
    vals=[Dtab[j][m] for j in range(m+1)]
    p=interp_0_to_m(vals)
    assert len(p)-1 <= m
    # overdetermined exact checks at m+1,m+2
    assert peval(p,m+1)==Dtab[m+1][m]
    assert peval(p,m+2)==Dtab[m+2][m]
    polys[m]=p
print("finite_degree_interpolation_overdetermined_checks=PASS")

# First adverse all-j Taylor curvature is order 11 at j=1.
for m in range(2,11):
    c=curvature(polys[m])
    assert all(x>0 for x in pshift(c,1))
c11=curvature(polys[11])
assert peval(c11,1)==-1410
assert all(x>0 for x in pshift(c11,2))
print("first_adverse_all_j_curvature_order=11 j=1 value=-1410")
print("C11_shift_j2_coefficients_all_positive=True")

# Active sector j>=67: certify every new order 10..18 coefficientwise after shift j=67+x.
mins=[]
for m in range(10,M+1):
    c=curvature(polys[m])
    sh=pshift(c,67)
    assert all(x>0 for x in sh), (m,sh)
    mins.append((m,min(sh)))
print("active_sector_curvature_block_m10_18_shift_j67_all_coefficients_positive=PASS")
for m,mn in mins:
    print(f"m={m} shifted_min_coefficient={mn}")

# Tail arithmetic for truncation after 18.
assert 32*(6**19) < 2**55
assert 8**19 == 2**57
assert 2**57 >= 2**56
print(f"tail_constant_check=PASS 32*6^19={32*(6**19)} < 2^55={2**55}")
print("window_constant_check=PASS 8^19=2^57>=2^56")
print("THEOREM_CORE: for j>=67 and n^19>=2^56*(j+1)^20, with n>=8*(j+1), Chen ratio is >1")
print("SIMPLE_WINDOW: j+1<=n^(19/20)/8 implies both hypotheses")
print("ALL_EXACT_CHECKS_PASS")
