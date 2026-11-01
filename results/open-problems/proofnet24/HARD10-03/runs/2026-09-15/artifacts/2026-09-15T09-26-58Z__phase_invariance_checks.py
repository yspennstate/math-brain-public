#!/usr/bin/env python3
"""
HARD10-03 finite-cycle checks for cyclic phase invariance and the r=2 kernel identity.
Sanity check only; proofs are in the report.
"""
import itertools, numpy as np
from scipy.linalg import expm

def compose(P,Q): return tuple(P[Q[i]] for i in range(len(P)))
def tau(n,a,b):
    p=list(range(n)); p[a],p[b]=p[b],p[a]; return tuple(p)
def edges_cycle(n): return [(i,(i+1)%n) for i in range(n)]

def generator(n):
    perms=list(itertools.permutations(range(n))); idx={p:i for i,p in enumerate(perms)}
    G=np.zeros((len(perms),len(perms)))
    ts=[tau(n,*e) for e in edges_cycle(n)]
    for p in perms:
        i=idx[p]
        for tr in ts:
            q=compose(tr,p); G[i,idx[q]]+=1; G[i,i]-=1
    return perms,idx,G

def two_tag_generator(n):
    states=[(a,b) for a in range(n) for b in range(n) if a!=b]
    idx={z:i for i,z in enumerate(states)}
    G=np.zeros((len(states),len(states)))
    for a,b in states:
        i=idx[(a,b)]
        for u,v in edges_cycle(n):
            aa,bb=a,b
            if aa==u: aa=v
            elif aa==v: aa=u
            if bb==u: bb=v
            elif bb==v: bb=u
            j=idx[(aa,bb)]
            if j!=i:
                G[i,j]+=1
                G[i,i]-=1
    return states,idx,G

def check(n=5,beta=1.3):
    perms,idx,G=generator(n); ident=tuple(range(n)); i0=idx[ident]
    Pb=expm(beta*G)[i0]
    base={}
    for r in (1,2,3):
        h=np.zeros(n)
        for w,P in zip(Pb,perms):
            x=0
            for _ in range(r): x=P[x]
            h[x]+=w
        base[r]=h

    errs={}
    for s in (0.0,.2,.7,1.3):
        Ps=expm(s*G)[i0]; Pt=expm((beta-s)*G)[i0]
        for r in (1,2,3):
            h=np.zeros(n)
            for wq,Q in zip(Ps,perms):
                if wq<1e-16: continue
                for wr,R in zip(Pt,perms):
                    w=wq*wr
                    if w<1e-18: continue
                    P=compose(R,Q)
                    y=0
                    for _ in range(r): y=P[y]
                    a=Q[0]; b=Q[y]
                    h[(b-a)%n]+=w
            errs[(s,r)]=float(np.max(np.abs(h-base[r])))

    states2,idx2,G2=two_tag_generator(n); K2=expm(beta*G2)
    id_err=0.0
    for x in range(1,n):
        rhs=0.0
        for y in range(n):
            if y in (0,x): continue
            rhs += K2[idx2[(0,y)], idx2[(y,x)]]
        id_err=max(id_err,abs(rhs-base[2][x]))
    return max(errs.values()),float(id_err)

if __name__=="__main__":
    a,b=check()
    print({"phase_invariance_max_error":a,"r2_kernel_identity_max_error":b})
    assert a<2e-12 and b<2e-12
