#!/usr/bin/env python3
from itertools import combinations, permutations
from collections import defaultdict

def closure_from_mask(n, mask):
    R = [[False]*n for _ in range(n)]
    k=0
    for i in range(n):
        for j in range(i+1,n):
            if (mask>>k)&1:
                R[i][j]=True
            k+=1
    for k in range(n):
        for i in range(n):
            if R[i][k]:
                for j in range(n):
                    if R[k][j]:
                        R[i][j]=True
    return tuple(tuple(row) for row in R)

def transitive_closure(n, edges):
    R=[[False]*n for _ in range(n)]
    for i,j in edges:
        R[i][j]=True
    for k in range(n):
        for i in range(n):
            if R[i][k]:
                for j in range(n):
                    if R[k][j]:
                        R[i][j]=True
    return tuple(tuple(row) for row in R)

def width(R):
    n=len(R); ans=1
    for mask in range(1,1<<n):
        S=[i for i in range(n) if (mask>>i)&1]
        if all(not R[i][j] and not R[j][i] for i,j in combinations(S,2)):
            ans=max(ans,len(S))
    return ans

def incomparable(R,a,b):
    return a!=b and not R[a][b] and not R[b][a]

def linexts(R):
    n=len(R)
    pred=[0]*n
    for j in range(n):
        for i in range(n):
            if R[i][j]:
                pred[j]|=1<<i
    out=[]
    def rec(mask,L):
        if mask==(1<<n)-1:
            out.append(tuple(L)); return
        for v in range(n):
            if not ((mask>>v)&1) and (pred[v]&~mask)==0:
                rec(mask|(1<<v),L+[v])
    rec(0,[])
    return out

def valid(L,R):
    p={v:i for i,v in enumerate(L)}
    n=len(R)
    return all((not R[i][j]) or p[i]<p[j] for i in range(n) for j in range(n))

def swap(L,a,b):
    L=list(L); ia=L.index(a); ib=L.index(b)
    L[ia],L[ib]=L[ib],L[ia]
    return tuple(L)

def canonical(R,a,b):
    n=len(R)
    T=[t for t in range(n) if R[t][b] and incomparable(R,t,a)]
    T={t for t in T if not any(R[t][u] for u in T if u!=t)}
    U=[s for s in range(n) if R[a][s] and incomparable(R,s,b)]
    U={s for s in U if not any(R[u][s] for u in U if u!=s)}
    return T,U

def exhaustive(maxn=6):
    for n in range(3,maxn+1):
        closures={}
        m=n*(n-1)//2
        for mask in range(1<<m):
            closures[closure_from_mask(n,mask)]=None
        wp=[R for R in closures if width(R)<=3]
        chambers=badL=badR=0; maxC=0
        for R in wp:
            X=linexts(R)
            for S in combinations(range(n),3):
                if not all(incomparable(R,u,v) for u,v in combinations(S,2)):
                    continue
                for a,b,c in permutations(S):
                    H=[]
                    for L in X:
                        p={v:i for i,v in enumerate(L)}
                        if p[a]<p[b]<p[c]:
                            H.append((L,p))
                    if not H:
                        continue
                    chambers+=1
                    T1,U1=canonical(R,a,b); C1=T1|U1
                    T2,U2=canonical(R,b,c); C2=T2|U2
                    assert len(T1)<=2 and len(U1)<=2
                    assert len(T2)<=2 and len(U2)<=2
                    assert not (C1&C2)
                    maxC=max(maxC,len(C1),len(C2))
                    for L,p in H:
                        x=not valid(swap(L,a,b),R)
                        y=not valid(swap(L,b,c),R)
                        cx=any(p[a]<p[v]<p[b] for v in C1)
                        cy=any(p[b]<p[v]<p[c] for v in C2)
                        assert x==cx and y==cy
                        badL+=int(x); badR+=int(y)
        print("n",n,"closures",len(closures),"width<=3",len(wp),
              "ordered_antichain_chambers",chambers,
              "max_canonical_side",maxC,
              "bad_left_occurrences",badL,
              "bad_right_occurrences",badR)

def calibration():
    covers=[(0,2),(0,4),(0,6),(1,4),(1,5),(1,6),(2,5),(3,4),(3,5)]
    R=transitive_closure(7,covers)
    assert width(R)==3
    a,b,c=3,2,6
    assert incomparable(R,a,b) and incomparable(R,b,c) and incomparable(R,a,c)
    X=linexts(R); E=len(X)
    P=[{v:i for i,v in enumerate(L)} for L in X]
    Nab=sum(p[a]<p[b] for p in P)
    Nbc=sum(p[b]<p[c] for p in P)
    H=[L for L,p in zip(X,P) if p[a]<p[b]<p[c]]
    BAC=sum(p[b]<p[a]<p[c] for p in P)
    ACB=sum(p[a]<p[c]<p[b] for p in P)
    BL=sum(not valid(swap(L,a,b),R) for L in H)
    BR=sum(not valid(swap(L,b,c),R) for L in H)
    assert 3*Nab>2*E and 3*Nbc>2*E and 3*len(H)>E
    assert BL>=len(H)-BAC and BR>=len(H)-ACB
    T1,U1=canonical(R,a,b); T2,U2=canonical(R,b,c)
    assert not ((T1|U1)&(T2|U2))
    print("calibration E",E,"N(a<b)",Nab,"N(b<c)",Nbc,
          "H_abc",len(H),"BAC",BAC,"ACB",ACB,
          "bad_ab",BL,"bad_bc",BR,
          "C_ab",sorted(T1|U1),"C_bc",sorted(T2|U2))

if __name__=="__main__":
    exhaustive()
    calibration()
    print("POS3_THREE_ANTICHAIN_GATE_CHECK_PASS")
