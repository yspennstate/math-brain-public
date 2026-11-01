#!/usr/bin/env python3
"""
R20/I0100 exact-integer SELF-CHECKS for the run's analytic identities.

This file is not the proof of the all-prime statements.  The run report gives
the written proofs.  It checks:
  (1) the Paley global-block / local-conference identity
      S_H^2 + 4 B B^T = p I + (n-2) J;
  (2) the exact local graph degree n/2-1;
  (3) the quantitative k-shift Legendre-correlation bound for k<=3
      on all distinct shift sets for several primes.

No floating-point arithmetic is used.
"""
from itertools import combinations
import numpy as np

PRIMES=[13,17,29,37,41,53,61,73,89,97,101]

def leg(a,p):
    a%=p
    if a==0:return 0
    z=pow(a,(p-1)//2,p)
    return 1 if z==1 else -1

def primitive_root(p):
    phi=p-1
    fac=[]
    x=phi; d=2
    while d*d<=x:
        if x%d==0:
            fac.append(d)
            while x%d==0:x//=d
        d+=1
    if x>1:fac.append(x)
    for g in range(2,p):
        if all(pow(g,phi//q,p)!=1 for q in fac):
            return g
    raise AssertionError

def check_prime(p):
    assert p%4==1
    n=(p-1)//2
    assert n%2==0
    g=primitive_root(p)
    alpha=pow(g,2,p)
    Q=[pow(alpha,j,p) for j in range(n)]
    NQ=[(g*x)%p for x in Q]

    H=np.zeros((n,n),dtype=np.int64)
    B=np.zeros((n,n),dtype=np.int64)
    for i,x in enumerate(Q):
        for j,y in enumerate(Q):
            if i!=j and leg(x-y,p)==1:H[i,j]=1
        for j,y in enumerate(NQ):
            if leg(x-y,p)==1:B[i,j]=1
    d=n//2-1
    assert np.all(H.sum(axis=1)==d)
    assert np.all(B.sum(axis=1)==n//2)
    assert np.all(B.sum(axis=0)==n//2)

    I=np.eye(n,dtype=np.int64)
    J=np.ones((n,n),dtype=np.int64)
    SH=J-I-2*H
    lhs=SH@SH+4*(B@B.T)
    rhs=p*I+(n-2)*J
    assert np.array_equal(lhs,rhs)

    sigma=[leg(pow(alpha,d,p)-1,p) for d in range(n)]
    assert sigma[0]==0
    worst={}
    for k in (1,2,3):
        mx=0
        arg=None
        for hs in combinations(range(n),k):
            s=0
            for dd in range(n):
                z=1
                for h in hs:z*=sigma[(dd+h)%n]
                s+=z
            if abs(s)>mx:
                mx=abs(s);arg=hs
            # Exact square check of 2|s| <= (2k-1)sqrt(p)+1.
            L=2*abs(s)-1
            if L>0:
                assert L*L <= (2*k-1)*(2*k-1)*p
        worst[k]=(mx,arg)
    return n,d,worst

def main():
    print("R20/I0100 analytic-route exact self-check")
    for p in PRIMES:
        n,d,w=check_prime(p)
        print("p",p,"n",n,"degree",d,"worst_abs_shift_sums",w)
    print("PASS: exact integer self-checks")
if __name__=="__main__":
    main()
