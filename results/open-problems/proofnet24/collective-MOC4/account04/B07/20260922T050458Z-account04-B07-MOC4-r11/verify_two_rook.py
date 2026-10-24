#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import product, permutations

# Exact true-unitary regression datum from account01/B08
# 20260922T024227Z-account01-B08-MOC4-r12.
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
def det(A):
    n=len(A); out=F(0)
    for p in permutations(range(n)):
        inv=sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
        x=F(1)
        for i in range(n): x*=A[i][p[i]]
        out += -x if inv%2 else x
    return out

assert all(matmul(U,tr(U))[i][j] == (1 if i == j else 0)
           for i in range(4) for j in range(4))
assert det(U)==1

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

# Exact complex numbers represented by rational pairs.
def cc(z): return (z[0],-z[1])
def abs2(z): return z[0]*z[0]+z[1]*z[1]

M=[[None]*3 for _ in range(3)]
N=[[None]*3 for _ in range(3)]
for a in range(3):
    for b in range(3):
        x=O[2*a][2*b]; y=O[2*a][2*b+1]
        z=O[2*a+1][2*b]; t=O[2*a+1][2*b+1]
        M[a][b]=((x+t)/2,(z-y)/2)
        N[a][b]=((x-t)/2,(z+y)/2)

def gauge_entry(m,n,r,c):
    if r==0 and c==0: return m,n
    if r==0 and c==1: return n,m
    if r==1 and c==0: return cc(n),cc(m)
    return cc(m),cc(n)

even_bits=[b for b in product((0,1),repeat=3) if sum(b)%2==0]
idx={b:i for i,b in enumerate(even_bits)}
assert even_bits == [(0,0,0),(0,1,1),(1,0,1),(1,1,0)]

def birkhoff4(T):
    T=[row[:] for row in T]
    out=[]
    while any(T[i][j] for i in range(4) for j in range(4)):
        p=None
        for cand in permutations(range(4)):
            if all(T[i][cand[i]]>0 for i in range(4)):
                p=cand; break
        assert p is not None
        w=min(T[i][p[i]] for i in range(4))
        out.append((w,p))
        for i in range(4): T[i][p[i]]-=w
    return out

max_terms=0
for r in even_bits:
    for c in even_bits:
        Mg=[[None]*3 for _ in range(3)]
        Ng=[[None]*3 for _ in range(3)]
        for a in range(3):
            for b in range(3):
                Mg[a][b],Ng[a][b]=gauge_entry(M[a][b],N[a][b],r[a],c[b])
        B=[[abs2(Ng[a][b]) for b in range(3)] for a in range(3)]
        p=U[idx[r]][idx[c]]**2
        t2=1-p
        assert sum(sum(row) for row in B)==2*t2
        assert all(sum(B[i][j] for j in range(3))<=t2 for i in range(3))
        assert all(sum(B[i][j] for i in range(3))<=t2 for j in range(3))
        if t2:
            S=[[x/t2 for x in row] for row in B]
            rd=[1-sum(S[i][j] for j in range(3)) for i in range(3)]
            cd=[1-sum(S[i][j] for i in range(3)) for j in range(3)]
            T=[[F(0) for _ in range(4)] for _ in range(4)]
            for i in range(3):
                for j in range(3): T[i][j]=S[i][j]
                T[i][3]=rd[i]
            for j in range(3): T[3][j]=cd[j]
            assert all(sum(T[i][j] for j in range(4))==1 for i in range(4))
            assert all(sum(T[i][j] for i in range(4))==1 for j in range(4))
            assert T[3][3]==0
            dec=birkhoff4(T)
            max_terms=max(max_terms,len(dec))
            rec=[[F(0) for _ in range(3)] for _ in range(3)]
            for w,p4 in dec:
                assert p4[3]!=3
                edges=[]
                for i in range(3):
                    if p4[i]<3:
                        rec[i][p4[i]]+=w
                        edges.append((i,p4[i]))
                assert len(edges)==2
            assert rec==S
        # Sharp nonlinear three-matching consequence from trace/nuclear norm.
        for rho in permutations(range(3)):
            prodq=F(1)
            for a in range(3): prodq*=B[a][rho[a]]
            assert prodq <= F(64,729)*t2**3

# Cross-gauge odd signed matchings.
qplus=[[abs2(M[a][b]) for b in range(3)] for a in range(3)]
qminus=[[abs2(N[a][b]) for b in range(3)] for a in range(3)]
shadow_maps=set()
max_mass_ratio=F(0)
max_product_ratio=F(0)
for rho in permutations(range(3)):
    for delta in even_bits:
        # delta=0 selects q^- and delta=1 selects q^+;
        # even delta means an odd number of q^- cells.
        selected=[]
        for a in range(3):
            b=rho[a]
            selected.append(qminus[a][b] if delta[a]==0 else qplus[a][b])
        pvals=[]
        mapping={}
        for r in even_bits:
            c=[None]*3
            for a in range(3):
                c[rho[a]]=r[a]^delta[a]
            c=tuple(c)
            assert c in idx
            mapping[idx[r]]=idx[c]
            pvals.append(U[idx[r]][idx[c]]**2)
        mt=tuple(mapping[i] for i in range(4))
        assert len(set(mt))==4
        shadow_maps.add(mt)
        pstar=max(pvals)
        mass=sum(selected)
        assert mass <= 2*(1-pstar)
        prodq=selected[0]*selected[1]*selected[2]
        assert prodq <= F(64,729)*(1-pstar)**3
        if 1-pstar:
            max_mass_ratio=max(max_mass_ratio,mass/(2*(1-pstar)))
            max_product_ratio=max(
                max_product_ratio,
                prodq/(F(64,729)*(1-pstar)**3)
            )

assert len(shadow_maps)==24
print("PASS MOC4-SPINOR-TWO-ROOK-CROSS-GAUGE-v1")
print("det_U =", det(U))
print("gauges_checked =", 16)
print("max_exact_birkhoff_terms =", max_terms)
print("odd_signed_matchings_checked =", 24)
print("distinct_shadow_permutations =", len(shadow_maps))
print("max_odd_mass_ratio =", max_mass_ratio)
print("max_odd_product_ratio =", max_product_ratio)
print("sharp_product_constant =", F(64,729))
