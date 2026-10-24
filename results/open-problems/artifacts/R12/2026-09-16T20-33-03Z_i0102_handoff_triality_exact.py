#!/usr/bin/env python3
"""
R12 / I0102 exact-arithmetic self-check for C11 (quartic triality).

This verifies only the finite algebraic core of the written all-prime proof.
It does not prove Conjecture 28 or improve the uniform exponent.

For p in {5,13,17,29,37}, for every (xi,eta,zeta) in F_p^3:
  (1) swapping xi and eta leaves the doubled-root multiset unchanged;
  (2) swapping eta and zeta translates the doubled-root multiset by zeta-eta.
These two transpositions generate S3, and a common translation of all roots
does not change the character sum over s in F_p.

For p in {5,13,17}, it additionally evaluates the quartic character sum
directly and checks invariance under all 6 permutations.
"""
from itertools import permutations

PRIMES=(5,13,17,29,37)
DIRECT=(5,13,17)

def chi(a,p):
    a%=p
    if a==0:
        return 0
    return 1 if pow(a,(p-1)//2,p)==1 else -1

def roots2(p,xi,eta,zeta):
    return [(xi+eta-zeta)%p, (-zeta)%p, eta%p, xi%p]

def qsum(p,xi,eta,zeta):
    inv2=pow(2,-1,p)
    rr=[(r*inv2)%p for r in roots2(p,xi,eta,zeta)]
    ans=0
    for s in range(p):
        prod=1
        for r in rr:
            prod=(prod*(s-r))%p
        ans+=chi(prod,p)
    return ans

for p in PRIMES:
    for xi in range(p):
        for eta in range(p):
            for zeta in range(p):
                R=sorted(roots2(p,xi,eta,zeta))
                R12=sorted(roots2(p,eta,xi,zeta))
                assert R12==R, (p,xi,eta,zeta,"swap12",R,R12)
                d=(zeta-eta)%p
                R23=sorted(roots2(p,xi,zeta,eta))
                Rt=sorted(((r+d)%p) for r in roots2(p,xi,eta,zeta))
                assert R23==Rt, (p,xi,eta,zeta,"swap23",R23,Rt)
    print(f"p={p}: algebraic doubled-root S3 generators PASS")

for p in DIRECT:
    for xi in range(p):
        for eta in range(p):
            for zeta in range(p):
                v=qsum(p,xi,eta,zeta)
                for perm in set(permutations((xi,eta,zeta))):
                    assert qsum(p,*perm)==v, (p,xi,eta,zeta,perm,v,qsum(p,*perm))
    print(f"p={p}: direct quartic character-sum S3 invariance PASS")

print("ALL_EXACT_CHECKS_PASS")
