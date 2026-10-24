#!/usr/bin/env python3
"""
R12 / I0102 exact self-check for run 2026-09-16T16-54-38Z_5e2ac1.

This checks the exact finite/symbolic core of the two-parameter
cross-character theta-dual obstruction.  It does not prove Conjecture 28.

All finite Paley computations below are integer arithmetic.  SymPy is used
only for exact symbolic identities.
"""
import itertools
import numpy as np
import sympy as sp

def paley(p):
    squares={pow(x,2,p) for x in range(1,p)}
    Q=np.zeros((p,p),dtype=np.int64)
    for i in range(p):
        for j in range(p):
            if i != j:
                Q[i,j]=1 if ((i-j)%p) in squares else -1
    edges=[(i,j) for i in range(p) for j in range(i+1,p) if Q[i,j]==1]
    E=len(edges)
    N=np.zeros((E,p),dtype=np.int64)
    for k,(a,b) in enumerate(edges):
        N[k,a]=N[k,b]=1
    C=N@Q@N.T
    L=N@N.T-2*np.eye(E,dtype=np.int64)
    I=np.eye(E,dtype=np.int64)
    J=np.ones((E,E),dtype=np.int64)
    K1=C+L+2*I-4*J
    K2=C*C-7*C-2*I+12*J
    return Q,edges,N,C,L,K1,K2

# Scalar required-position identities.
assert 2+0+2-4 == 0       # K1 diagonal, C=2
assert 3+1+0-4 == 0       # K1 overlapping H-edge, C=3
assert 4+0+0-4 == 0       # K1 disjoint H-edge, C=4
assert 2**2-7*2-2+12 == 0
assert 3**2-7*3+12 == 0
assert 4**2-7*4+12 == 0
print("K1/K2 required-position vanishing: PASS")

# Exact finite verification of the incidence compression.
for p in [5,13,17,29]:
    Q,edges,N,C,L,K1,K2=paley(p)
    R=N.T@K2@N
    I=np.eye(p,dtype=np.int64)
    J=np.ones((p,p),dtype=np.int64)
    # 4R=(p-1)[-(13p-8)I+(16p-11)J-(7p-8)Q].
    rhs=(p-1)*(-(13*p-8)*I+(16*p-11)*J-(7*p-8)*Q)
    assert np.array_equal(4*R,rhs)
    # N^T N = d I + A, Q^2=pI-J.
    assert np.array_equal(Q@Q,p*I-J)
    print(f"p={p}: compression identity PASS")

# Symbolic Paley association algebra check for N^T C N = DQD.
p=sp.symbols('p', positive=True)
# Represent alpha I + beta J + gamma Q as a triple.
def mul(u,v):
    x,y,z=u
    X,Y,Z=v
    return (
        sp.factor(x*X+p*z*Z),
        sp.factor(x*Y+y*X+p*y*Y-z*Z),
        sp.factor(x*Z+z*X),
    )
D=((p-2)/2, sp.Rational(1,2), sp.Rational(1,2))
Qalg=(0,0,1)
DQD=mul(mul(D,Qalg),D)
target=(
    p*(p-2)/2,
    -(p-2)/2,
    (p**2-3*p+4)/4,
)
assert all(sp.simplify(a-b)==0 for a,b in zip(DQD,target))
print("symbolic DQD association-algebra identity: PASS")

# Symbolic conversion from S=N^T(C∘C)N to R=N^T K2 N.
S=(
    (p**2-3*p-16)/4,
    (4*p**2-17*p+31)/4,
    -3*(p-4)/2,
)
R=tuple(sp.factor(
    S[i]-7*DQD[i]-2*D[i]+(12*((p-1)/2)**2 if i==1 else 0)
) for i in range(3))
Rtarget=(
    -(p-1)*(13*p-8)/4,
    (p-1)*(16*p-11)/4,
    -(p-1)*(7*p-8)/4,
)
assert all(sp.simplify(a-b)==0 for a,b in zip(R,Rtarget))
print("symbolic K2 compression coefficient identity: PASS")

# Three-Rayleigh minimax certificate.
r=sp.symbols('r', positive=True)
P=r**2
nH=P*(P-1)/4
k1c=-(P-1)**2
k2c=4*P**2-6*P+2

dplus=(P-2+r)/2
dminus=(P-2-r)/2
kplus=(1+r)*dplus
kminus=(1-r)*dminus
rplus=(P-1)/4*(-(13*P-8)-(7*P-8)*r)
rminus=(P-1)/4*(-(13*P-8)+(7*P-8)*r)
muplus=sp.factor(rplus/dplus)
muminus=sp.factor(rminus/dminus)

den=3*P**2-16*P+11
a0=2*(2*P**2-11*P+8)/(P*den)
ap=(P-1)*(r+2)*(3*r**3-4*r**2-9*r+8)/(2*P*den)
am=(P-1)*(r-2)*(3*r**3+4*r**2-9*r-8)/(2*P*den)

assert sp.simplify(a0+ap+am-1)==0
assert sp.simplify(a0*k1c+ap*kplus+am*kminus)==0
assert sp.simplify(a0*k2c+ap*muplus+am*muminus)==0

z=sp.factor(a0*nH)
ztarget=(P-1)*(2*P**2-11*P+8)/(2*den)
assert sp.simplify(z-ztarget)==0
print("positive-weight cancellation identities: PASS")
print("lower envelope z_p =", sp.factor(ztarget))

# Intersection point of the three affine Rayleigh lower bounds.
tstar=(7*P**2-35*P+24)/(4*den)
sstar=(P-1)*(P-4)/(4*den)
c0=sp.expand(nH+tstar*k1c+sstar*k2c)
cp=sp.expand(tstar*kplus+sstar*muplus)
cm=sp.expand(tstar*kminus+sstar*muminus)
assert sp.simplify(c0-ztarget)==0
assert sp.simplify(cp-ztarget)==0
assert sp.simplify(cm-ztarget)==0
print("three-way intersection identities: PASS")

print("POSITIVITY NOTE: for p>=5, den>0 and all displayed weight factors are")
print("positive; the report gives the elementary inequalities proving this.")
print("ALL_EXACT_CHECKS_PASS")
