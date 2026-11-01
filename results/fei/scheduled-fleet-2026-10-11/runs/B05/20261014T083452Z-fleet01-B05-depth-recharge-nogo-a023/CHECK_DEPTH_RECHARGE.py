#!/usr/bin/env python3
"""Exact Walsh check for the fixed-dimension overlap-recharge no-go."""
from fractions import Fraction
from itertools import product
from math import log, log2

NAMES=("y","x","z","u")


def truth(point):
    y,x,z,u=point
    return x if y==1 else z*u


POINTS=list(product((-1,1),repeat=4))


def character(point,mask):
    ans=1
    for i,v in enumerate(point):
        if mask>>i&1: ans*=v
    return ans


HAT=[]
for mask in range(16):
    HAT.append(sum(Fraction(truth(p)*character(p,mask),16) for p in POINTS))
P=[a*a for a in HAT]


def orbit_energy(block,outside):
    bmask=sum(1<<NAMES.index(v) for v in block)
    omask=sum(1<<NAMES.index(v) for v in outside)
    total=Fraction(0)
    sub=bmask
    while True:
        total += P[omask|sub]
        if sub==0: break
        sub=(sub-1)&bmask
    return total


def q(t):
    if not t: return 0.0
    x=float(t)
    return x*log2(1/x)+2*x/log(2)


def lam(block):
    k=len(block)
    e0=orbit_energy(block,())
    ans=q(e0)+float(e0)*log2(k)
    for v in NAMES:
        if v not in block:
            ans += q(orbit_energy(block,(v,)))
    return ans


def influence(v):
    i=NAMES.index(v)
    return sum(P[s] for s in range(16) if s>>i&1)


X=("y","x")
Y=("y","z")
lx,ly=lam(X),lam(Y)
D=ly-lx
assert orbit_energy(X,())==Fraction(1,2)
assert orbit_energy(Y,())==0
assert orbit_energy(Y,("x",))==Fraction(1,2)
assert orbit_energy(Y,("u",))==Fraction(1,2)
assert all(influence(v)==Fraction(1,2) for v in NAMES)
assert abs(D-1/log(2))<1e-14

print("status=PASS")
print("dimension=4")
print("function=f(y,x,z,u)=x if y=1 else z*u")
print("X={y,x}")
print("Y={y,z}")
print("E_X_empty=1/2")
print("E_Y_empty=0")
print("E_Y_x=1/2")
print("E_Y_u=1/2")
print("Inf_x=Inf_y=Inf_z=Inf_u=1/2")
print("I_total=2")
print(f"Lambda_X={lx:.15f}")
print(f"Lambda_Y={ly:.15f}")
print(f"D=Lambda_Y-Lambda_X={D:.15f}")
print(f"one_over_ln2={1/log(2):.15f}")
for r in (1,2,5,20,100):
    # Path X,Y,X,Y,...,Y with 2r-1 swaps: r positive entries and r-1 refunds.
    positive=r*D
    negative=(r-1)*D
    signed=positive-negative
    assert abs(signed-D)<1e-12
    print(f"r={r} swaps={2*r-1} positive_variation={positive:.15f} refunds={negative:.15f} signed_total={signed:.15f}")

