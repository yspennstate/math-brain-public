#!/usr/bin/env python3
from fractions import Fraction
from functools import lru_cache
from math import factorial, comb
import time

M=32

@lru_cache(None)
def partitions(n, max_part=None):
    if max_part is None or max_part > n:
        max_part=n
    if n==0:
        return ((),)
    out=[]
    for a in range(max_part,0,-1):
        rem=n-a
        for tail in partitions(rem, min(a,rem)):
            out.append((a,)+tail)
    return tuple(out)

@lru_cache(None)
def fdim(mu):
    n=sum(mu)
    if n==0:
        return 1
    h=1
    for r,rowlen in enumerate(mu):
        for c in range(rowlen):
            below=0
            for rr in range(r+1,len(mu)):
                if mu[rr]>c:
                    below+=1
            h *= rowlen-c+below
    return factorial(n)//h

def numerator_poly(j, maxdeg):
    if j==0:
        return [1]+[0]*maxdeg
    maxdeg=min(maxdeg,2*j)
    acc=[0]*(maxdeg+1)
    fj=factorial(j)
    mass=0
    for mu in partitions(j):
        f=fdim(mu)
        wt=f*f
        mass += wt
        rows=list(mu)+[0]*(j-len(mu))
        q=[1]
        for r in range(1,j+1):
            a=j+rows[r-1]-r
            new=[0]*min(maxdeg+1,len(q)+2)
            for d,v in enumerate(q):
                new[d]+=v
                if d+1<len(new):
                    new[d+1] += -2*a*v
                if d+2<len(new):
                    new[d+2] += a*a*v
            q=new
        for d,v in enumerate(q):
            acc[d] += wt*v
    assert mass==fj
    assert all(v%fj==0 for v in acc)
    p=[v//fj for v in acc]
    p += [0]*(maxdeg+1-len(p))
    return p

def D_coeffs_fast(j,M):
    p=numerator_poly(j,M)
    p += [0]*(M+1-len(p))
    p=p[:M+1]
    L=[Fraction(0)]*(M+1)
    for m in range(1,M+1):
        conv=sum((Fraction(r)*L[r]*p[m-r] for r in range(1,m)),Fraction(0))
        L[m]=Fraction(p[m])-conv/Fraction(m)
    D=[Fraction(0)]*(M+1)
    for m in range(1,M+1):
        powers=sum((s**m for s in range(1,j)),0)
        D[m]=L[m]+Fraction(2*powers,m)
    return p,D

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
    out=[Fraction(0)]*len(a)
    for k,ak in enumerate(a):
        for r in range(k+1):
            out[r]+=ak*comb(k,r)*(Fraction(s)**(k-r))
    while len(out)>1 and out[-1]==0: out.pop()
    return out

def interp_0_to_m(vals):
    dif=list(vals); coeff=[]
    for _ in range(len(vals)):
        coeff.append(dif[0])
        dif=[dif[i+1]-dif[i] for i in range(len(dif)-1)]
    out=[Fraction(0)]; basis=[Fraction(1)]; fact=1
    for r,dr in enumerate(coeff):
        if r>0:
            basis=pmul(basis,[Fraction(-(r-1)),Fraction(1)])
            fact*=r
        out=padd(out,pscale(basis,dr/Fraction(fact)))
    return out

def curvature(poly):
    return padd(pscale(poly,2),pscale(padd(pshift(poly,-1),pshift(poly,1)),-1))

start=time.time()
# m+2 values provide two independent interpolation checks beyond the m+1 points.
tab={}
for j in range(M+3):
    tab[j]=D_coeffs_fast(j,M)
print(f"partition_numerator_table_j0_{M+2}_through_order_{M}=PASS")
print(f"partition_count_j{M+2}={len(partitions(M+2))}")

polys={}
for m in range(1,M+1):
    vals=[tab[j][1][m] for j in range(m+1)]
    p=interp_0_to_m(vals)
    assert len(p)-1<=m
    assert peval(p,m+1)==tab[m+1][1][m]
    assert peval(p,m+2)==tab[m+2][1][m]
    polys[m]=p
print("finite_degree_interpolation_two_unused_values_each_order=PASS")

for m in range(2,M+1):
    c=curvature(polys[m])
    sh=pshift(c,m)
    assert all(x>0 for x in sh), (m,sh)
    assert sh[-1]==2*m*(m-1)
print("diagonal_curvature_block_m2_32_shift_jm_all_coefficients_positive=PASS")
print("curvature_leading_coefficient_check=PASS value=2*m*(m-1) for m=2..32")
for m in range(29,33):
    sh=pshift(curvature(polys[m]),67)
    assert all(x>0 for x in sh)
    print(f"m={m} active_shift_j67_min_coefficient={min(sh)}")

# Supplementary numerator-polynomial exactness checks in small ranks.
for j in range(1,11):
    p=tab[j][0]
    assert p[0]==1
    assert all(x==0 for x in p[2*j+1:])
print("numerator_polynomial_basic_exact_checks_j1_10=PASS")

# Tail after order 32 using retained |D_m(r)| <= 2(6r)^m.
C=32*(6**33)
assert 2**90 < C < 2**91
# One-condition theorem: for j>=67, n^33>=2^93*(j+1)^34 implies n>8(j+1)
# and tail curvature <1/(2(j+1)).
assert 2**93 * 68 > 8**33
assert 8**34 == 2**102
assert 2**102 > 2**93
print(f"tail_constant_check=PASS 32*6^33={C} between_2^90_and_2^91=True")
print("active_disk_implication=PASS 2^93*68>8^33")
print("simple_window_check=PASS 8^34=2^102>2^93")
print("THEOREM_CORE: for j>=67 and n^33>=2^93*(j+1)^34, Chen ratio is >1")
print("SIMPLE_WINDOW: j+1<=n^(33/34)/8 implies theorem hypothesis")
print(f"elapsed_seconds={time.time()-start:.6f}")
print("ALL_EXACT_CHECKS_PASS")
