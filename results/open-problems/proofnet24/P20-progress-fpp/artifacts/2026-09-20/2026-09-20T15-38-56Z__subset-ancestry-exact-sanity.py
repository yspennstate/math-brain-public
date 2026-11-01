#!/usr/bin/env python3
from fractions import Fraction
from functools import lru_cache

# Exact finite sanity for the subset-only ancestry recursion.
# Supplementary finite checking only; no asymptotic/source closure is inferred.

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
                if j is not None and i<j: edges.append((i,j))
    left=[idx[(0,d)] for d in range(-W,W+1) if (0,d) in idx]
    right=[idx[(2*L,d)] for d in range(-W,W+1) if (2*L,d) in idx]
    return verts,edges,left,right

def solve_block(L,W):
    verts,edges,left,right=band(L,W)
    n=len(verts); m=len(left); init=sum(1<<v for v in left)

    @lru_cache(None)
    def R(mask):
        # Returns q[j] and H[j][v].  H is the linear coefficient of the
        # scalar carried by currently infected vertex v in the eventual
        # scalar inherited by output j.  No source labels are stored.
        bedges=[]
        for u,v in edges:
            iu=(mask>>u)&1; iv=(mask>>v)&1
            if iu and not iv: bedges.append((u,v))
            elif iv and not iu: bedges.append((v,u))
        b=len(bedges)
        qs=[]; HH=[]
        for jj,t in enumerate(right):
            if (mask>>t)&1:
                qs.append(Fraction(0))
                h=[Fraction(0)]*n; h[t]=Fraction(1); HH.append(tuple(h))
            else:
                assert b>0
                q=Fraction(1,b); h=[Fraction(0)]*n
                for x,v in bedges:
                    cqs,cHH=R(mask|(1<<v))
                    q += cqs[jj]/b
                    ch=cHH[jj]
                    # Child v copied the scalar at parent x.  Substitute
                    # w_v=w_x in the child's linear ancestry functional.
                    for z in range(n):
                        if (mask>>z)&1: h[z]+=ch[z]/b
                    h[x]+=ch[v]/b
                qs.append(q); HH.append(tuple(h))
        return tuple(qs),tuple(HH)

    q,H=R(init)
    K=[[H[j][left[i]] for j in range(m)] for i in range(m)]

    # Exact stationary vector K alpha = alpha, sum alpha=1.
    A=[]; rhs=[]
    for i in range(m-1):
        A.append([K[i][j]-(Fraction(1) if i==j else 0) for j in range(m)])
        rhs.append(Fraction(0))
    A.append([Fraction(1)]*m); rhs.append(Fraction(1))
    aug=[A[r]+[rhs[r]] for r in range(m)]
    for c in range(m):
        p=next(r for r in range(c,m) if aug[r][c])
        aug[c],aug[p]=aug[p],aug[c]
        z=aug[c][c]; aug[c]=[x/z for x in aug[c]]
        for r in range(m):
            if r!=c and aug[r][c]:
                z=aug[r][c]
                aug[r]=[aug[r][k]-z*aug[c][k] for k in range(m+1)]
    alpha=tuple(aug[r][-1] for r in range(m))
    Ka=tuple(sum(K[i][j]*alpha[j] for j in range(m)) for i in range(m))
    lam=sum(alpha[j]*q[j] for j in range(m))
    assert all(sum(K[i][j] for i in range(m))==1 for j in range(m))
    assert Ka==alpha and sum(alpha)==1 and all(x>=0 for x in alpha)
    return verts,q,K,alpha,Ka,lam,R.cache_info().currsize

def fs(x):
    return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"

for W in (2,4):
    verts,q,K,alpha,Ka,lam,states=solve_block(1,W)
    print(f"L=1 W={W} V={len(verts)} subset_states={states}")
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
