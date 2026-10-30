#!/usr/bin/env python3
"""Exact B17 checker for the RM(1,4) signed-resolvent sign-reversal witness.

No floating-point value is used to certify the finite claims.  Trigonometric
display values are optional diagnostics only.
"""
from collections import Counter
from fractions import Fraction
from math import log, sqrt

N = 16
NEG_F = {0,1,3,5,10,12,14,15}
Q = {0,3,4,7,9,10,12,15}

def points():
    return [tuple((i >> (3-j)) & 1 for j in range(4)) for i in range(16)]

PTS = points()

def affine_masks():
    out=[]
    for a_int in range(16):
        a=tuple((a_int >> (3-j)) & 1 for j in range(4))
        for b in (0,1):
            vals=[]
            for x in PTS:
                vals.append((sum(ai*xi for ai,xi in zip(a,x))+b)&1)
            out.append(vals)
    return out

M=affine_masks()
M_MASKS=[sum(bit<<i for i,bit in enumerate(m)) for m in M]

def uv(zset, qset, m):
    u=v=0
    for i in range(N):
        sign = -1 if ((i in zset) ^ bool(m[i])) else 1
        if i in qset: v += sign
        else: u += sign
    return u,v

def pair_counts(zset):
    return Counter(uv(zset,Q,m) for m in M)

CF=pair_counts(NEG_F)
C0=pair_counts(set())

EXPECTED_CF=Counter({
    (2,-2):12, (-2,2):12,
    (6,2):2, (-6,-2):2, (-2,-6):2, (2,6):2,
})
EXPECTED_C0=Counter({
    (0,0):22, (-4,4):4, (4,-4):4, (8,8):1, (-8,-8):1,
})
assert CF == EXPECTED_CF
assert C0 == EXPECTED_C0

# g=1_Q must genuinely enlarge RM(1,4).
QMASK=sum(1<<i for i in Q)
FMASK=sum(1<<i for i in NEG_F)
assert QMASK not in M_MASKS
assert len(Q)==8 and len(NEG_F)==8

# D=M^perp exact enumeration.
D=[]
for A in range(1<<N):
    if all(((A & mm).bit_count() & 1)==0 for mm in M_MASKS):
        D.append(A)
weights=Counter(A.bit_count() for A in D)
assert len(D)==2048
assert min(A.bit_count() for A in D if A) == 4
assert weights == Counter({8:870,6:448,10:448,4:140,12:140,0:1,16:1})

C4=sum(
    1 for A in D
    if A.bit_count()==4
    and ((A & QMASK).bit_count() & 1)
    and ((A & FMASK).bit_count() & 1)
)
assert C4==24
# Peer quartic theorem predicts 2*C4/N^4 = 3/4096.
assert Fraction(2*C4,N**4)==Fraction(3,4096)

def Phi(x,t):
    return x/(x+t) if x else Fraction(0)

def gate_difference(t):
    """Exact R_M(t)-R_{M+<g>}(t) from the authentic gate formula."""
    tot=Fraction(0)
    for m in M:
        uf,vf=uv(NEG_F,Q,m)
        u0,v0=uv(set(),Q,m)
        for sign,(u,v) in ((1,(uf,vf)),(-1,(u0,v0))):
            plus=Fraction((u+v)**2,N**2)
            minus=Fraction((u-v)**2,N**2)
            tot += sign*(Phi(plus,t)-Phi(minus,t))
    return Fraction(N,2)*tot/Fraction(len(M),1)

def closed_form(t):
    return Fraction(9,2)*(4*t-1)/((t+1)*(4*t+1)*(16*t+1))

for t in (
    Fraction(1,1024), Fraction(1,64), Fraction(1,16),
    Fraction(1,8), Fraction(1,4), Fraction(1,2), Fraction(3,1)
):
    assert gate_difference(t)==closed_form(t)

assert gate_difference(Fraction(1,16)) == Fraction(-108,85)
assert gate_difference(Fraction(1,8)) < 0
assert gate_difference(Fraction(1,4)) == 0
assert gate_difference(Fraction(1,2)) > 0

# Exact primitive:
# F(T)=ln(4T+1)-1/2 ln(16T^2+17T+1).
# Hence the window [1/16,1/8] equals ln(2*sqrt(51)/15)<0,
# because (2*sqrt(51))^2=204<225=15^2.
assert 204 < 225

# Walsh spectrum of f, exact boundary sanity check.
vals=[-1 if i in NEG_F else 1 for i in range(N)]
w=vals[:]
h=1
while h<N:
    for i in range(0,N,2*h):
        for j in range(i,i+h):
            x,y=w[j],w[j+h]
            w[j],w[j+h]=x+y,x-y
    h*=2
ps=[Fraction(x*x,N*N) for x in w]
assert Counter(ps)==Counter({Fraction(0):12,Fraction(1,4):4})
I=sum(Fraction(i.bit_count())*ps[i] for i in range(N))
assert I==Fraction(5,2)
H=Fraction(2,1)  # four atoms of mass 1/4
assert H/I==Fraction(4,5)

print("EXACT_PASS")
print("pair_counts_f =", sorted(CF.items()))
print("pair_counts_0 =", sorted(C0.items()))
print("dual_weight_distribution =", sorted(weights.items()))
print("C4 =", C4, "quartic_coefficient =", "3/4096")
print("Rdiff(t) = 9(4t-1) / [2(t+1)(4t+1)(16t+1)]")
print("Rdiff(1/16) =", gate_difference(Fraction(1,16)))
print("Rdiff(1/4) =", gate_difference(Fraction(1,4)))
print("window_[1/16,1/8] = ln(2*sqrt(51)/15) < 0")
print("integral_[0,infinity] Rdiff(t) dt = 0 (from exact primitive endpoints)")
print("f: H=2, I=5/2, H/I=4/5 (not an FEI counterexample)")
