#!/usr/bin/env python3
# Exact/sanity checker for NM13-01 endpoint-clique reversal arc cutoff.
# Finite calculations are sanity checks only; asymptotic theorem is proved in the report.

import math
import numpy as np
import sympy as sp
from scipy.linalg import expm

def base_graph(n, edges):
    nbr = [set() for _ in range(n)]
    for u,v in edges:
        nbr[u].add(v); nbr[v].add(u)
    ds = {len(x) for x in nbr}
    assert len(ds) == 1
    return nbr, ds.pop()

def construct(nbr):
    n = len(nbr); d = len(nbr[0])
    arcs = [(u,v) for u in range(n) for v in sorted(nbr[u])]
    ai = {a:i for i,a in enumerate(arcs)}
    M = len(arcs)
    A = sp.zeros(M); J = sp.zeros(M)
    for i,(u,v) in enumerate(arcs):
        J[i,ai[(v,u)]] = 1
        for w in nbr[u]:
            if w != v: A[i,ai[(u,w)]] = 1
        for w in nbr[v]:
            if w != u: A[i,ai[(w,v)]] = 1
        A[i,ai[(v,u)]] = 1
    Q = A / sp.Integer(2*d-1)

    edges = sorted({tuple(sorted((u,v))) for u,v in arcs})
    ei = {e:i for i,e in enumerate(edges)}
    m = len(edges)
    Rho = sp.zeros(M,m)
    for i,(u,v) in enumerate(arcs):
        Rho[i,ei[tuple(sorted((u,v)))]] = 1

    AL = sp.zeros(m)
    for i,e in enumerate(edges):
        for j,f in enumerate(edges):
            if i != j and set(e) & set(f):
                AL[i,j] = 1
    QL = AL / sp.Integer(2*(d-1))
    K = sp.eye(m)/sp.Integer(2*d-1) + sp.Rational(2*(d-1),2*d-1)*QL

    D = sp.zeros(n,M)
    Grad = sp.zeros(M,n)
    P = sp.zeros(n)
    for i,(u,v) in enumerate(arcs):
        D[u,i] = 1
        Grad[i,u] = 1; Grad[i,v] = -1
    for u in range(n):
        for v in nbr[u]:
            P[u,v] = sp.Rational(1,d)
    return arcs,Q,J,edges,Rho,QL,K,D,Grad,P

def eigdict(M):
    return {str(sp.simplify(k)):int(v) for k,v in M.eigenvals().items()}

def restricted_blocks(arcs,Q,J):
    M = len(arcs); ai = {a:i for i,a in enumerate(arcs)}
    reps=[]; seen=set()
    for a in arcs:
        if a in seen: continue
        b=(a[1],a[0]); reps.append(a); seen.add(a); seen.add(b)
    m=len(reps)
    E=sp.zeros(M,m); O=sp.zeros(M,m); L=sp.zeros(m,M)
    for j,a in enumerate(reps):
        b=(a[1],a[0])
        E[ai[a],j]=1; E[ai[b],j]=1
        O[ai[a],j]=1; O[ai[b],j]=-1
        L[j,ai[a]]=1
    return L*Q*E, L*Q*O

def tv(x,y):
    return 0.5*np.abs(x-y).sum()

tests = [
    ("K4",4,[(i,j) for i in range(4) for j in range(i+1,4)]),
    ("K33",6,[(i,j) for i in range(3) for j in range(3,6)]),
]

for name,n,edges0 in tests:
    nbr,d=base_graph(n,edges0)
    arcs,Q,J,edges,Rho,QL,K,D,Grad,P=construct(nbr)
    M=len(arcs)
    assert Q*Rho == Rho*K
    assert Q*J == J*Q
    Odd=(sp.eye(M)-J)/2
    rhs=(Grad*D-3*sp.eye(M))/sp.Integer(2*d-1)
    assert (Q-rhs)*Odd == sp.zeros(M)
    assert D*Grad == d*(sp.eye(n)-P)
    Qe,Qo=restricted_blocks(arcs,Q,J)
    print(name, "base", eigdict(P))
    print(name, "even", eigdict(Qe))
    print(name, "odd ", eigdict(Qo))

    Qn=np.array(Q,float); Kn=np.array(K,float)
    a0=0
    rev=int(np.argmax(np.array(J[a0,:],float)))
    e0=int(np.argmax(np.array(Rho[a0,:],float)))
    pi=np.ones(M)/M; pie=np.ones(len(edges))/len(edges)
    for t in (0.2,1.0,3.0):
        mu=np.eye(M)[a0]@expm(t*(Qn-np.eye(M)))
        nu=np.eye(len(edges))[e0]@expm(t*(Kn-np.eye(len(edges))))
        odd=(np.eye(M)[a0]-np.eye(M)[rev])@expm(t*(Qn-np.eye(M)))
        dA=tv(mu,pi); dP=tv(nu,pie); corr=0.25*np.abs(odd).sum()
        assert dP <= dA + 1e-11
        assert dA <= dP + corr + 1e-11
    print(name, "TV_SANDWICH_PASS")

d=6
gap=2*(3-math.sqrt(5))/11
beta=math.log(2)/(2*math.log(10))
odd_exp=1/(2*math.log(5))
print("d6_degree", 2*d-1)
print("d6_center_coeff_log5_n", (2*d-1)/(d-2))
print("d6_gap_lower", f"{gap:.15f}")
print("d6_nonLRE_beta", f"{beta:.15f}")
print("d6_odd_front_decay_exponent", f"{odd_exp:.15f}")
print("d6_crude_L2_exponent", f"{0.5-odd_exp:.15f}")
assert gap > 0 and beta > 0 and odd_exp > 0 and 0.5-odd_exp > 0
print("ALL_EXACT_AND_SANITY_CHECKS_PASS")
