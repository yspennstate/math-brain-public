#!/usr/bin/env python3
from math import factorial

NMAX=29

def parts(n, maxp=None, pref=()):
    if n==0:
        yield pref; return
    if maxp is None or maxp>n: maxp=n
    for a in range(maxp,0,-1):
        yield from parts(n-a,a,pref+(a,))

def hookdim(lam):
    n=sum(lam); f=factorial(n); w=lam[0]; r=len(lam)
    col=[sum(1 for x in lam if x>c) for c in range(w)]
    hp=1
    for i,a in enumerate(lam):
        for c in range(a): hp *= (a-c)+(col[c]-i-1)
    assert f%hp==0
    return f//hp

def ellrow(n):
    e=[0]*(n+1)
    for lam in parts(n):
        d=hookdim(lam); e[lam[0]] += d*d
    assert sum(e)==factorial(n)
    return e

rows={n:ellrow(n) for n in range(1,NMAX+2)}
checks=0
min_gap=None; min_at=None
for n in range(1,NMAX+1):
    e,e1=rows[n],rows[n+1]
    U=[0]*(n+1); U1=[0]*(n+2)
    for k in range(1,n+1): U[k]=U[k-1]+e[k]
    for k in range(1,n+2): U1[k]=U1[k-1]+e1[k]
    H=[0]*(n+1)
    for k in range(1,n+1):
        H[k]=U1[k]-(n+1)*U[k-1]
        assert e[k] <= H[k] <= n*e[k]
    for k in range(1,n+1):
        lhs=e1[k]
        rhs=H[k] + (n+1)*e[k-1] - H[k-1]
        assert lhs==rhs
    for k in range(1,n):
        gap=H[k+1]*e[k]-H[k]*e[k+1]
        assert gap>=0
        checks+=1
        if min_gap is None or gap<min_gap:
            min_gap=gap; min_at=(n,k)
print(f'NMAX={NMAX}')
print(f'Plancherel_rows_checked={NMAX+1}')
print(f'insertion_flux_rows_checked={NMAX}')
print(f'alpha_adjacent_monotonicity_checks={checks}')
print(f'min_exact_cross_gap={min_gap} at_n_k={min_at}')
print('ALL_EXACT_CHECKS_PASS')
