#!/usr/bin/env python3
"""Exact symbolic/finite self-check for P04-I0101 anharmonic J-parity identity.

The symbolic identities are over Z(x,y,t); finite-field checks are corroborating
only. No floating point arithmetic is used.
"""
import sympy as sp

x,y,t = sp.symbols('x y t')
N = lambda z: (z*z-z+1)**3
D = lambda z: z*z*(1-z)**2

factor_rhs = ((x-y)*(x*y-1)*(x+y-1)*(x*y-x+1)*(x*y-x-y)*(x*y-y+1))
assert sp.expand(N(x)*D(y)-N(y)*D(x)-factor_rhs) == 0

J = lambda z: sp.cancel(N(z)/D(z))
assert sp.cancel(J(1-x)-J(x)) == 0
assert sp.cancel(J(1/x)-J(x)) == 0

xt = sp.cancel(((1-t*t)/(1+t*t))**2)
oct_rhs = (t**8+14*t**4+1)**3 / (16*t**4*(t**4-1)**4)
assert sp.cancel(J(xt)-oct_rhs) == 0


def leg(a,p):
    a %= p
    if a == 0: return 0
    return 1 if pow(a,(p-1)//2,p) == 1 else -1

def jmod(a,p):
    num = pow((a*a-a+1)%p,3,p)
    den = (a*a*(1-a)*(1-a))%p
    return num*pow(den,-1,p)%p

def orbit(a,p):
    r=lambda z:(1-z)%p
    s=lambda z:pow(z,-1,p)
    seen=set(); stack=[a]
    while stack:
        z=stack.pop()
        if z in seen: continue
        seen.add(z); stack += [r(z),s(z)]
    return seen

checked=[]
for p in (29,53,101,149):
    assert p%24==5
    V=[a for a in range(2,p) if leg(a,p)==1 and leg(a-1,p)==1]
    assert len(V)==(p-5)//4
    orbs=[]; seen=set()
    for a in V:
        if a in seen: continue
        o=orbit(a,p); assert len(o)==6 and o<=set(V)
        seen |= o; orbs.append(o)
    assert len(orbs)==(p-5)//24
    labels=[jmod(next(iter(o)),p) for o in orbs]
    assert len(set(labels))==len(labels)
    for oi,o in enumerate(orbs):
        assert all(jmod(z,p)==labels[oi] for z in o)
    reps=[next(iter(o)) for o in orbs]
    for i,a in enumerate(reps):
        for j,b in enumerate(reps):
            if i==j: continue
            ob=orbs[j]
            prod=1; k=0
            for z in ob:
                sgn=leg(a-z,p); assert sgn in (-1,1)
                prod *= sgn
                k += (sgn==1)
            lhs=leg(jmod(a,p)-jmod(b,p),p)
            assert lhs==prod==((-1)**k)
    checked.append((p,len(V),len(orbs)))

print('P04-I0101-ANHARMONIC-J-PARITY-23-SELFCHECK=PASS')
print('SYMBOLIC_FACTOR_IDENTITY=PASS')
print('S3_INVARIANCE=PASS')
print('OCTAHEDRAL_PARAMETER_IDENTITY=PASS')
print('FINITE_FREE_FAMILY_CHECKS='+repr(checked))
print('FLOATING_POINT_USED=NO')
