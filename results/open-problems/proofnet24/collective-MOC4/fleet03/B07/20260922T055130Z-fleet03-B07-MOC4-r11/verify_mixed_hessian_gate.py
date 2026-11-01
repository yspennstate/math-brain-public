#!/usr/bin/env python3
"""Exact rational consistency checks for MOC4-MIXED-CONFORMAL-HESSIAN-GATE-v1.

This script is a deterministic algebraic consistency checker, not the proof itself.
The proof is in REPORT.md.  No floating point arithmetic is used.
"""
from fractions import Fraction as F
from random import Random


def mat(a,b,c,d):
    return [[F(a),F(b)],[F(c),F(d)]]

def add(A,B):
    return [[A[i][j]+B[i][j] for j in range(2)] for i in range(2)]

def scale(c,A):
    return [[c*A[i][j] for j in range(2)] for i in range(2)]

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]

def tr(A):
    return A[0][0]+A[1][1]

def tp(A):
    return [[A[j][i] for j in range(2)] for i in range(2)]

def det(A):
    return A[0][0]*A[1][1]-A[0][1]*A[1][0]

def frob2(A):
    return sum(A[i][j]*A[i][j] for i in range(2) for j in range(2))

def inner(A,B):
    return sum(A[i][j]*B[i][j] for i in range(2) for j in range(2))

def qdet(A,B):
    # det(A+B)-det(A)-det(B), the symmetric determinant polarization.
    return det(add(A,B))-det(A)-det(B)

def r(A):
    return frob2(A)/2

def h_formula(A,G,Z,Ka,Kg,Xa,Xg):
    A0=Ka*det(A)+Kg*det(G)
    C=Ka*det(G)+Kg*det(A)
    ZZt=mm(Z,tp(Z)); ZtZ=mm(tp(Z),Z)
    pG=tr(mm(mm(ZtZ,G),tp(G)))
    pA=tr(mm(mm(tp(Z),mm(A,tp(A))),Z))
    return -A0*frob2(Z)+2*C*det(Z)+(Xa-Xg)*(pG-pA)/2

def h_direct(A,G,Z,Ka,Kg,Xa,Xg):
    Ap=mm(Z,G); Gp=scale(-1,mm(tp(Z),A))
    App=scale(-1,mm(mm(Z,tp(Z)),A))
    Gpp=scale(-1,mm(mm(tp(Z),Z),G))
    det2A=qdet(A,App)+2*det(Ap)
    det2G=qdet(G,Gpp)+2*det(Gp)
    r2A=frob2(Ap)+inner(A,App)
    r2G=frob2(Gp)+inner(G,Gpp)
    return Ka*det2A+Kg*det2G+(Xa*r2A+Xg*r2G)/2

I=mat(1,0,0,1)
J=mat(0,-1,1,0)
S=mat(1,0,0,-1)
T0=mat(0,1,1,0)
PLUS=[I,J]; MINUS=[S,T0]

def pol(H,P,Q):
    return (H(add(P,Q))-H(P)-H(Q))/2

def gram(A):
    return mm(A,tp(A))

def lincomb(cs, mats):
    out=mat(0,0,0,0)
    for c,M in zip(cs,mats): out=add(out,scale(c,M))
    return out

def rho2(Sm):
    u=(Sm[0][0]-Sm[1][1])/2
    v=Sm[0][1]
    return u*u+v*v

rng=Random(20260922055130)
for trial in range(40):
    blocks=[]
    for beta in range(3):
        A=mat(*[rng.randint(-4,4) for _ in range(4)])
        G=mat(*[rng.randint(-4,4) for _ in range(4)])
        blocks.append((A,G))
    K_a=[F(rng.randint(-5,5)) for _ in range(3)]
    K_g=[F(rng.randint(-5,5)) for _ in range(3)]
    X_a=[F(rng.randint(-5,5)) for _ in range(3)]
    X_g=[F(rng.randint(-5,5)) for _ in range(3)]

    def H(Z):
        return sum(h_formula(A,G,Z,ka,kg,xa,xg)
                   for (A,G),ka,kg,xa,xg in zip(blocks,K_a,K_g,X_a,X_g))
    def HD(Z):
        return sum(h_direct(A,G,Z,ka,kg,xa,xg)
                   for (A,G),ka,kg,xa,xg in zip(blocks,K_a,K_g,X_a,X_g))

    # Formula (1) agrees exactly with direct second differentiation.
    for _ in range(8):
        Z=mat(*[rng.randint(-3,3) for _ in range(4)])
        assert H(Z)==HD(Z)

    # Build the mixed block by polarization.
    M=[[pol(H,P,Q) for Q in MINUS] for P in PLUS]

    # Independent closed form from the weighted Gram sums.
    dx=[xa-xg for xa,xg in zip(X_a,X_g)]
    Avec=lincomb(dx,[gram(A) for A,G in blocks])
    Gvec=lincomb(dx,[gram(G) for A,G in blocks])
    u=(Gvec[0][0]-Gvec[1][1])/2
    v=Gvec[0][1]
    p=(Avec[0][0]-Avec[1][1])/2
    q=Avec[0][1]
    Mclosed=[[u-p,v-q],[-v-q,u+p]]
    assert M==Mclosed

    # Exact singular-value invariant identity:
    # eigenvalues of M^T M are (rho(G) +/- rho(A))^2.
    MtM=mm(tp(M),M)
    rg2=rho2(Gvec); ra2=rho2(Avec)
    assert tr(MtM)==2*(rg2+ra2)
    assert det(MtM)==(rg2-ra2)**2

print("PASS: 40 exact rational fixtures; Hessian formula, mixed block, and anisotropy invariants agree.")
