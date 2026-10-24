#!/usr/bin/env python3
"""Deterministic corroboration for account03/B02 r41.

No numerical check is used as proof.  This script checks:
  (i) anchored 3x3 -> Schur E2 identity,
 (ii) shared-hub exterior star norm identity,
(iii) reverse/forward triangle inequalities for the coefficient arrays,
 (iv) the new spectral inequality e2(x)*sum_{j>=3}x_j <= 3 e3(x),
  (v) the resulting 1/192 near-rank-two implication.
Only the Python standard library is used.
"""
from __future__ import annotations
import itertools, math, random

SEED = 20260923
rng = random.Random(SEED)


def det2(a,b,c,d):
    return a*d-b*c


def dot(x,y): return sum(a*b for a,b in zip(x,y))
def norm2(x): return dot(x,x)


def matvec(A,x): return [dot(row,x) for row in A]

def transpose(A): return list(map(list,zip(*A)))

def matmul(A,B):
    BT=transpose(B)
    return [[dot(r,c) for c in BT] for r in A]

def outer(x,y): return [[a*b for b in y] for a in x]

def sub(A,B): return [[a-b for a,b in zip(r,s)] for r,s in zip(A,B)]
def fro2(A): return sum(v*v for r in A for v in r)

def eye(n): return [[1.0 if i==j else 0.0 for j in range(n)] for i in range(n)]
def proj_perp(v):
    q=norm2(v)
    I=eye(len(v))
    return [[I[i][j]-v[i]*v[j]/q for j in range(len(v))] for i in range(len(v))]


def e2_minors(N):
    L=len(N); R=len(N[0]); out=0.0
    for i,j in itertools.combinations(range(L),2):
        for k,l in itertools.combinations(range(R),2):
            m=det2(N[i][k],N[i][l],N[j][k],N[j][l])
            out += m*m
    return out


def local_trial(L=5,R=6):
    a=rng.uniform(-2,2)
    if abs(a)<0.05: a=0.05 if a>=0 else -0.05
    c=[rng.gauss(0,1) for _ in range(L)]
    r=[rng.gauss(0,1) for _ in range(R)]
    N=[[rng.gauss(0,1) for _ in range(R)] for _ in range(L)]
    D=Z=0.0
    for i,j in itertools.combinations(range(L),2):
        for k,l in itertools.combinations(range(R),2):
            m=det2(N[i][k],N[i][l],N[j][k],N[j][l])
            z=(r[k]*(N[j][l]*c[i]-N[i][l]*c[j])
               +r[l]*(-N[j][k]*c[i]+N[i][k]*c[j]))
            D += (a*m-z)**2
            Z += z*z
    S=sub(N,[[c[i]*r[j]/a for j in range(R)] for i in range(L)])
    schur=a*a*e2_minors(S)
    Pc=proj_perp(c); Pr=proj_perp(r)
    C=matmul(matmul(Pc,N),Pr)
    T=norm2(c)*norm2(r)*fro2(C)
    E=e2_minors(N)
    p=abs(a)*math.sqrt(E); q=math.sqrt(T); d=math.sqrt(D)
    rel_s=abs(D-schur)/max(1.0,D,schur)
    rel_z=abs(Z-T)/max(1.0,Z,T)
    ok_tri=(abs(p-q) <= d+1e-9 and d <= p+q+1e-9)
    return rel_s,rel_z,ok_tri


def elementary(xs):
    xs=sorted(xs,reverse=True); n=len(xs)
    e2=sum(xs[i]*xs[j] for i in range(n) for j in range(i+1,n))
    e3=sum(xs[i]*xs[j]*xs[k] for i in range(n) for j in range(i+1,n) for k in range(j+1,n))
    tail=sum(xs[2:]); e1=sum(xs)
    return e1,e2,e3,tail

max_s=max_z=0.0; tri_fail=0
for _ in range(1000):
    rs,rz,ok=local_trial()
    max_s=max(max_s,rs); max_z=max(max_z,rz)
    tri_fail += (not ok)

max_ratio=0.0; spectral_fail=0; eligible=0
for n in range(3,20):
    for _ in range(5000):
        xs=[math.exp(rng.uniform(-12,12)) for _ in range(n)]
        e1,e2,e3,tail=elementary(xs)
        if e3>0:
            max_ratio=max(max_ratio,e2*tail/(3*e3))
        if e2*tail > 3*e3*(1+1e-12): spectral_fail += 1
        if e3 < e2**1.5/192:
            eligible += 1
            if not (tail < math.sqrt(e2)/64*(1+1e-12)): spectral_fail += 1
            if not (tail < e1/64*(1+1e-12)): spectral_fail += 1

print({
  "seed":SEED,
  "local_trials":1000,
  "max_relative_schur_identity_error":max_s,
  "max_relative_star_identity_error":max_z,
  "triangle_failures":tri_fail,
  "spectral_trials":17*5000,
  "max_ratio_e2_tail_over_3e3":max_ratio,
  "near_rank2_eligible":eligible,
  "spectral_failures":spectral_fail,
})
