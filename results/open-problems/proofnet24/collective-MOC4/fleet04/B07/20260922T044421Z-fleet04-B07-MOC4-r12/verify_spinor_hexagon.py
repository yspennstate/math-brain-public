#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import product, permutations

# Exact true-unitary regression datum from fleet01/B08
# 20260922T024227Z-fleet01-B08-MOC4-r12.
U = [
    [F(636,1105), F(-423,1105), F(-12,65), F(-772,1105)],
    [F(3576,5525), F(332,5525), F(-144,325), F(3411,5525)],
    [F(164,425), F(348,425), F(9,25), F(-96,425)],
    [F(27,85), F(-36,85), F(4,5), F(24,85)],
]

def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]
def tr(A): return [list(x) for x in zip(*A)]
assert all(matmul(U,tr(U))[i][j] == (1 if i == j else 0)
           for i in range(4) for j in range(4))

canon=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
basis=[((0,1),1),((2,3),1),((0,2),1),((1,3),-1),((0,3),1),((1,2),1)]
def minor2(i,j,k,l):
    return U[i][k]*U[j][l]-U[i][l]*U[j][k]
C=[[minor2(*rp,*cp) for cp in canon] for rp in canon]
O=[]
for rp,rs in basis:
    rr=canon.index(rp)
    O.append([rs*cs*C[rr][canon.index(cp)] for cp,cs in basis])
assert all(matmul(O,tr(O))[i][j] == (1 if i == j else 0)
           for i in range(6) for j in range(6))

# Exact complex numbers represented as (real, imaginary) rational pairs.
def ca(z,w): return (z[0]+w[0],z[1]+w[1])
def cs(z,w): return (z[0]-w[0],z[1]-w[1])
def cm(z,w): return (z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0])
def cc(z): return (z[0],-z[1])
def abs2(z): return z[0]*z[0]+z[1]*z[1]
def cprod(v):
    z=(F(1),F(0))
    for x in v: z=cm(z,x)
    return z
def det3(A):
    out=(F(0),F(0))
    for p in permutations(range(3)):
        inv=sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))
        t=cprod([A[i][p[i]] for i in range(3)])
        out=cs(out,t) if inv%2 else ca(out,t)
    return out
def minor2c(A, rows, cols):
    i,j=rows; k,l=cols
    return cs(cm(A[i][k],A[j][l]),cm(A[i][l],A[j][k]))

M=[[None]*3 for _ in range(3)]
N=[[None]*3 for _ in range(3)]
for a in range(3):
    for b in range(3):
        x=O[2*a][2*b]; y=O[2*a][2*b+1]
        z=O[2*a+1][2*b]; t=O[2*a+1][2*b+1]
        M[a][b]=((x+t)/2,(z-y)/2)
        N[a][b]=((x-t)/2,(z+y)/2)

def gauge_entry(m,n,r,c):
    # T(z)=m z+n zbar.  Conjugating input/output coordinates:
    # 00:(m,n), 01:(n,m), 10:(conj n,conj m), 11:(conj m,conj n).
    if r==0 and c==0: return m,n
    if r==0 and c==1: return n,m
    if r==1 and c==0: return cc(n),cc(m)
    return cc(m),cc(n)

even_bits=[b for b in product((0,1),repeat=3) if sum(b)%2==0]
assert even_bits == [(0,0,0),(0,1,1),(1,0,1),(1,1,0)]
idx={b:i for i,b in enumerate(even_bits)}

max_detN_abs2=F(0)
max_reconstruction_error=F(0)
max_adjugate_error=F(0)
for r in even_bits:
    for c in even_bits:
        Mg=[[None]*3 for _ in range(3)]
        Ng=[[None]*3 for _ in range(3)]
        for a in range(3):
            for b in range(3):
                Mg[a][b],Ng[a][b]=gauge_entry(M[a][b],N[a][b],r[a],c[b])
        dN=det3(Ng)
        dM=det3(Mg)
        L=sum(abs2(Ng[a][b]) for a in range(3) for b in range(3))
        tau=L/2
        Pij=U[idx[r]][idx[c]]**2
        adjnorm2=sum(abs2(minor2c(Ng,rows,cols))
                     for rows in ((0,1),(0,2),(1,2))
                     for cols in ((0,1),(0,2),(1,2)))
        max_detN_abs2=max(max_detN_abs2,abs2(dN))
        max_reconstruction_error=max(max_reconstruction_error,abs((1-tau)-Pij))
        max_adjugate_error=max(max_adjugate_error,abs(adjnorm2-tau*tau))
        assert dN==(F(0),F(0))
        assert 1-tau == Pij
        assert abs2(dM) == Pij*Pij
        assert adjnorm2 == tau*tau

# One nontrivial six-term closure from the gauge that was tightest in r11.
r=c=(0,1,1)
Ng=[[None]*3 for _ in range(3)]
for a in range(3):
    for b in range(3):
        _,Ng[a][b]=gauge_entry(M[a][b],N[a][b],r[a],c[b])
terms=[]
signed=(F(0),F(0))
for p in permutations(range(3)):
    inv=sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))
    z=cprod([Ng[i][p[i]] for i in range(3)])
    terms.append((p,-1 if inv%2 else 1,z))
    signed=cs(signed,z) if inv%2 else ca(signed,z)
assert signed==(F(0),F(0))

L=sum(abs2(Ng[a][b]) for a in range(3) for b in range(3))
P=U[1][1]**2
print("PASS MOC4-SPINOR-HEXAGON-COMPATIBILITY-v1")
print("even_even_gauges =", 16)
print("max_detN_abs2 =", max_detN_abs2)
print("max_mask_to_P_reconstruction_error =", max_reconstruction_error)
print("max_adjugate_norm_identity_error =", max_adjugate_error)
print("sample_gauge = 011,011")
print("sample_L =", L)
print("sample_1_minus_L_over_2 =", 1-L/2)
print("sample_P22 =", P)
print("sample_six_term_signed_sum =", signed)
for p,s,z in terms:
    print("term",p,"sign",s,"=",z)
