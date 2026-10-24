#!/usr/bin/env python3
"""Independent truth-table check of the antichain-address overlap identity."""
from fractions import Fraction
from itertools import combinations, product
import random
from decimal import Decimal, getcontext

getcontext().prec = 90
LN2 = Decimal(2).ln()
def D(q):
    return Decimal(q.numerator)/Decimal(q.denominator) if isinstance(q,Fraction) else Decimal(q)
def log2(x): return Decimal(x).ln()/LN2
rng = random.Random(20261014)

def parity(mask, bits):
    return -1 if sum(bits[j] for j in range(len(bits)) if mask >> j & 1) & 1 else 1

def walsh(vals, n):
    out=[]
    den=1<<n
    for s in range(1<<n):
        out.append(Fraction(sum(v*parity(s,x) for x,v in vals.items()), den))
    return out

def U_of(vals,n):
    w=walsh(vals,n); p=[q*q for q in w]
    ans=Decimal(0)
    for s,ps in enumerate(p):
        if not ps: continue
        pi=sum(p[t] for t in range(1<<n) if t & s == s)
        ans += D(ps) * log2(D(pi)/D(ps))
    return ans

def influence(vals,n):
    w=walsh(vals,n)
    return sum(Fraction(s.bit_count())*q*q for s,q in enumerate(w))

def restrict(vals,n,j,b):
    out={}
    for x in product((0,1),repeat=n-1):
        xx=x[:j]+(b,)+x[j:]
        out[x]=vals[xx]
    return out

def build(k,n,A):
    vals={}
    for bits in product((0,1),repeat=k+n):
        z=sum(bits[j]<<j for j in range(k))
        vals[bits]=parity(A[z],bits[k:])
    return vals

def antichain(A):
    return all(not (a & b == a or a & b == b) for a,b in combinations(A,2))

def formula(k,n,A):
    m=1<<k
    refund=Decimal(0)
    for i in range(n):
        B=[a & ~(1<<i) for a in A]
        for z,b in enumerate(B):
            d=sum(1 for c in B if b & c == b)
            refund += log2(d)/Decimal(m)
    return Decimal(k)/2-refund, refund

cases=[]
for k,n in [(1,3),(1,4),(2,4),(2,5)]:
    m=1<<k; subs=list(range(1,1<<n))
    pool=[a for a in combinations(subs,m) if antichain(a)]
    if len(pool)>180: pool=rng.sample(pool,180)
    cases += [(k,n,a) for a in pool]
for n in (5,6):
    m=8; layer=[a for a in range(1,1<<n) if a.bit_count()==n//2]
    if len(layer)>=m:
        for _ in range(80): cases.append((3,n,tuple(rng.sample(layer,m))))

max_u=max_g=Decimal(0); assertions=0
for k,n,A in cases:
    vals=build(k,n,A); N=k+n
    U=U_of(vals,N)
    G=Decimal(N)*U
    for j in range(N):
        G -= (U_of(restrict(vals,N,j,0),N-1)+U_of(restrict(vals,N,j,1),N-1))/2
    gf,refund=formula(k,n,A)
    max_u=max(max_u,abs(U-Decimal(k)/2))
    max_g=max(max_g,abs(G-gf))
    I=influence(vals,N)
    If=Fraction(k,2)+sum(Fraction(a.bit_count(),len(A)) for a in A)
    assert I==If
    assert G <= D(I) + Decimal('1e-70')
    assertions += N+4

print('seed=20261014')
print('cases=',len(cases))
print('assertions=',assertions)
print('max_U_error=',format(max_u,'.8E'))
print('max_G_error=',format(max_g,'.8E'))
print('status=PASS')
