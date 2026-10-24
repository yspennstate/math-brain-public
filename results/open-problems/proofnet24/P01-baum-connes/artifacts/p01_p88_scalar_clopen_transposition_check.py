#!/usr/bin/env python3
"""Exact rational self-check for P01-P88 scalar clopen-transposition unitary.

This verifies only the finite group-ring algebra and Z^2 coordinate bookkeeping.
The K-theory/assembly identification uses Pooya's published theorem and is proved
in the accompanying report, not by this script.
"""
from fractions import Fraction
from collections import defaultdict

def red(w):
    s=[]
    for a in w:
        if s and s[-1] == -a:
            s.pop()
        else:
            s.append(a)
    return tuple(s)

def wmul(a,b): return red(a+b)
def winv(w): return tuple(-x for x in reversed(w))
E=()

# G = (direct sum_{F2} C2) semidirect F2.
# Group element = (frozenset of toggled lamp positions, reduced F2 word).
def gmul(g,h):
    L,w=g; M,v=h
    shifted=frozenset(wmul(w,x) for x in M)
    return (L.symmetric_difference(shifted), wmul(w,v))

def ginv(g):
    L,w=g
    wi=winv(w)
    return (frozenset(wmul(wi,x) for x in L), wi)

ID=(frozenset(),E)

def clean(D): return {g:c for g,c in D.items() if c}

def add(A,B):
    C=defaultdict(Fraction)
    for g,c in A.items(): C[g]+=c
    for g,c in B.items(): C[g]+=c
    return clean(C)

def scale(A,c): return clean({g:c*a for g,a in A.items()})

def mul(A,B):
    C=defaultdict(Fraction)
    for g,a in A.items():
        for h,b in B.items():
            C[gmul(g,h)] += a*b
    return clean(C)

def star(A): return clean({ginv(g):a for g,a in A.items()})
def mono(g,c=1): return {g:Fraction(c)}
ONE=mono(ID)
ZERO={}
def sub(A,B): return add(A,scale(B,-1))

def lamp(x): return (frozenset([x]),E)
def free(w): return (frozenset(),red(w))

s=(1,)
u_s=mono(free(s))
u_sm=mono(free((-1,)))
a_e=mono(lamp(E))
a_s=mono(lamp(s))

p_e=scale(add(ONE,a_e), Fraction(1,2))
q_s=scale(sub(ONE,a_s), Fraction(1,2))
p=mul(p_e,q_s)
r=mul(mul(u_s,p),u_sm)
v=mul(u_s,p)
W=add(add(v,star(v)),sub(sub(ONE,p),r))

assert mul(p,p)==p
assert mul(r,r)==r
assert mul(p,r)==ZERO and mul(r,p)==ZERO
assert mul(star(v),v)==p
assert mul(v,star(v))==r
assert star(W)==W
assert mul(W,W)==ONE

def quotient(A):
    C=defaultdict(Fraction)
    for (L,w),c in A.items():
        C[w]+=c
    return clean(C)

assert quotient(W)=={E:Fraction(1)}

w=red((1,1,-2,1,1,1,1,-2,-2,-2,-2))
def expsum(w):
    return (
        sum(1 if a==1 else -1 if a==-1 else 0 for a in w),
        sum(1 if a==2 else -1 if a==-2 else 0 for a in w)
    )
assert expsum(w)==(6,-5)

U=mul(mono(free(w)),W)
assert mul(star(U),U)==ONE
assert mul(U,star(U))==ONE
assert quotient(U)=={w:Fraction(1)}

print("P01-P88 exact finite self-check")
print("p^2=p: PASS")
print("r^2=r and pr=rp=0: PASS")
print("v*v=p and vv*=r: PASS")
print("W*=W and W^2=1: PASS")
print("q(W)=1: PASS")
print("free-word exponent sums: (6,-5): PASS")
print("U*=U^{-1} and q(U)=u_w: PASS")
print(f"expanded W support size: {len(W)}")
print(f"expanded U support size: {len(U)}")
print("ALL EXACT SELF-CHECK ASSERTIONS PASSED")
