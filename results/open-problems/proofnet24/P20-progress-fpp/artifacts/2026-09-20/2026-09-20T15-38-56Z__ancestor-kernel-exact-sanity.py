#!/usr/bin/env python3
from fractions import Fraction
from functools import lru_cache
from collections import defaultdict

# Exact finite sanity check for P20-FPP-ANCESTOR-FIXED-POINT-BELLMAN.
# This is supplementary algebraic checking, not an asymptotic FPP certificate.

def band(L,W):
    verts=[]; idx={}
    for s in range(2*L+1):
        for d in range(-W,W+1):
            if (s-d)%2==0:
                idx[(s,d)]=len(verts); verts.append((s,d))
    edges=[]
    for (s,d),i in idx.items():
        if s<2*L:
            for nd in (d-1,d+1):
                j=idx.get((s+1,nd))
                if j is not None and i<j:
                    edges.append((i,j))
    left=[idx[(0,d)] for d in range(-W,W+1) if (0,d) in idx]
    right=[idx[(2*L,d)] for d in range(-W,W+1) if (2*L,d) in idx]
    return verts,edges,left,right

def solve(L,W):
    verts,edges,left,right=band(L,W)
    n=len(verts); m=len(left)
    own=[-1]*n; mask=0
    for a,v in enumerate(left):
        own[v]=a; mask|=1<<v
    own=tuple(own)

    @lru_cache(None)
    def rec(mask,own):
        if all((mask>>v)&1 for v in right):
            q=tuple(Fraction(0) for _ in right)
            p=[]
            for v in right:
                row=[Fraction(0) for _ in range(m)]
                row[own[v]]=1; p.append(tuple(row))
            return q,tuple(p)
        tr=defaultdict(int); b=0
        for u,v in edges:
            iu=(mask>>u)&1; iv=(mask>>v)&1
            if iu^iv:
                b+=1
                nv,src=(v,own[u]) if iu else (u,own[v])
                tr[(nv,src)]+=1
        children=[]
        for (v,src),mult in tr.items():
            no=list(own); no[v]=src
            children.append((mult,rec(mask|(1<<v),tuple(no))))
        qs=[]; ps=[]
        for j,t in enumerate(right):
            if (mask>>t)&1:
                qs.append(Fraction(0))
                row=[Fraction(0) for _ in range(m)]; row[own[t]]=1
                ps.append(tuple(row))
            else:
                qq=Fraction(1,b); row=[Fraction(0) for _ in range(m)]
                for mult,(cq,cp) in children:
                    qq+=Fraction(mult,b)*cq[j]
                    for a in range(m): row[a]+=Fraction(mult,b)*cp[j][a]
                qs.append(qq); ps.append(tuple(row))
        return tuple(qs),tuple(ps)

    q,p=rec(mask,own)
    K=[[p[j][i] for j in range(m)] for i in range(m)]

    # Solve (K-I) alpha=0, sum alpha=1 exactly.
    A=[]; rhs=[]
    for i in range(m-1):
        A.append([K[i][j]-(1 if i==j else 0) for j in range(m)])
        rhs.append(Fraction(0))
    A.append([Fraction(1)]*m); rhs.append(Fraction(1))
    aug=[A[r]+[rhs[r]] for r in range(m)]
    for c in range(m):
        pvt=next(r for r in range(c,m) if aug[r][c])
        aug[c],aug[pvt]=aug[pvt],aug[c]
        z=aug[c][c]; aug[c]=[x/z for x in aug[c]]
        for r in range(m):
            if r!=c and aug[r][c]:
                z=aug[r][c]; aug[r]=[aug[r][k]-z*aug[c][k] for k in range(m+1)]
    alpha=tuple(aug[r][-1] for r in range(m))
    Ka=tuple(sum(K[i][j]*alpha[j] for j in range(m)) for i in range(m))
    lam=sum(alpha[j]*q[j] for j in range(m))
    assert all(sum(K[i][j] for i in range(m))==1 for j in range(m))
    assert Ka==alpha and sum(alpha)==1 and all(x>=0 for x in alpha)
    return verts,q,K,alpha,Ka,lam,rec.cache_info().currsize

def fs(x):
    return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"

for W in (2,4):
    verts,q,K,alpha,Ka,lam,states=solve(1,W)
    print(f"L=1 W={W} V={len(verts)} states={states}")
    print("q =", " ".join(map(fs,q)))
    print("K rows:")
    for row in K: print("  "+" ".join(map(fs,row)))
    print("alpha =", " ".join(map(fs,alpha)))
    print("Kalpha =", " ".join(map(fs,Ka)))
    print("lambda =", fs(lam), f"float={float(lam):.15f}")
    print("columnsums =", " ".join(fs(sum(K[i][j] for i in range(len(K)))) for j in range(len(K))))
    print("FIXED_POINT_EXACT =", Ka==alpha)
    print()
print("ALL_EXACT_CHECKS_PASS = True")
