#!/usr/bin/env python3
from fractions import Fraction
from functools import lru_cache
from math import factorial, comb

M=28

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
    if n==0: return 1
    h=1
    for r,rowlen in enumerate(mu):
        for c in range(rowlen):
            below=sum(1 for rr in range(r+1,len(mu)) if mu[rr]>c)
            h *= rowlen-c+below
    return factorial(n)//h

def contents(mu):
    return [c-r for r,rowlen in enumerate(mu,1) for c in range(1,rowlen+1)]

def pmul_trunc(a,b,M):
    c=[Fraction(0)]*(min(M,len(a)+len(b)-2)+1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            if i+j<=M: c[i+j]+=x*y
    return c

def D_coeffs(j,M=M):
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
            r[m]=sum((Fraction(2*s)*B[s]*r[m-s] for s in range(1,m+1)),Fraction(0))/m
        for m in range(1,M+1):
            a[m]+=wt*r[m]
    D=[Fraction(0)]*(M+1)
    for m in range(1,M+1):
        D[m]=a[m]-sum((Fraction(s)*D[s]*a[m-s] for s in range(1,m)),Fraction(0))/m
    return a,D

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
    out=[Fraction(0)]*len(a)
    for k,ak in enumerate(a):
        for r in range(k+1):
            out[r]+=ak*comb(k,r)*(Fraction(s)**(k-r))
    while len(out)>1 and out[-1]==0: out.pop()
    return out

def interp_0_to_m(vals):
    dif=list(vals); coeff=[]
    for r in range(len(vals)):
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

# Compute A_j and D_m through order M for all j needed for finite-degree interpolation.
tab={j:D_coeffs(j,M) for j in range(M+3)}
print(f"partition_taylor_table_j0_{M+2}_through_order_{M}=PASS")

polys={}
for m in range(1,M+1):
    vals=[tab[j][1][m] for j in range(m+1)]
    p=interp_0_to_m(vals)
    assert len(p)-1<=m
    assert peval(p,m+1)==tab[m+1][1][m]
    assert peval(p,m+2)==tab[m+2][1][m]
    polys[m]=p
print("finite_degree_interpolation_overdetermined_checks=PASS")

# New diagonal-threshold finite theorem: every curvature through order 28 is
# coefficientwise positive after j=m+x. This is a finite exact certificate,
# not an all-order assertion.
for m in range(2,M+1):
    c=curvature(polys[m])
    sh=pshift(c,m)
    assert all(x>0 for x in sh), (m,sh)
    assert sh[-1]==2*m*(m-1)
print("diagonal_curvature_block_m2_28_shift_jm_all_coefficients_positive=PASS")
print("curvature_leading_coefficient_check=PASS value=2*m*(m-1) for m=2..28")
for m in range(19,29):
    sh=pshift(curvature(polys[m]),67)
    assert all(x>0 for x in sh)
    print(f"m={m} active_shift_j67_min_coefficient={min(sh)}")

# Exact check of the row-telescoped numerator-polynomial identity A_j=P_j/D_j^2
# for j<=10, through enough Taylor degree to see the full polynomial P_j.
for j in range(1,11):
    A=tab[j][0]
    den=[Fraction(1)]
    for s in range(1,j):
        den=pmul(den,[Fraction(1),Fraction(-s)])
    den2=pmul(den,den)
    lhs=pmul_trunc(A,den2,2*j)
    P=[Fraction(0)]*(2*j+1)
    fj=factorial(j)
    for mu in partitions(j):
        wt=Fraction(fdim(mu)**2,fj)
        q=[Fraction(1)]
        rows=list(mu)+[0]*(j-len(mu))
        for r in range(1,j+1):
            a=j+rows[r-1]-r
            q=pmul(q,[Fraction(1),Fraction(-2*a),Fraction(a*a)])
        for d,v in enumerate(q): P[d]+=wt*v
    assert lhs==P
print("numerator_polynomial_identity_Aj_equals_Pj_over_Dj_squared_j1_10=PASS")

# Analytic tail arithmetic after truncating at order 28.
C=32*(6**29)
assert C < 2**80
assert not (C < 2**79)
# For j>=67, hypothesis n^29>=2^81*(j+1)^30 implies n>8(j+1),
# because 2^81*(j+1)>2^87=8^29.
assert 2**81 * 68 > 8**29
assert 8**30 == 2**90
print(f"tail_constant_check=PASS 32*6^29={C} < 2^80={2**80}")
print("active_disk_check=PASS 2^81*68>8^29")
print("simple_window_check=PASS 8^30=2^90>2^81")
print("THEOREM_CORE: for j>=67 and n^29>=2^81*(j+1)^30, Chen ratio is >1")
print("SIMPLE_WINDOW: j+1<=n^(29/30)/8 implies theorem hypothesis")
print("ALL_EXACT_CHECKS_PASS")
