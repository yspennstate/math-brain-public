"""
HARD10-02 exact certificate suite recovered from the completed
2026-09-15T09:55:19Z task response.

Recovery provenance
-------------------
The durable 09:55 report references an exact-certificate sibling artifact,
but bounded repository retrieval found that artifact absent. This file
archives the authored code from that completed run; it is not newly
invented evidence.

It certifies:
1. The first-order signed fresh-harmonic sum D is nonnegative for every
   connected labeled simple graph on n=3,4,5 vertices, fixing root 0,
   target n-1, and checking every non-target neighbor of the root.
2. The full first-excursion inequality Q_c <= h_0 for all such n=5
   graphs at c in {11/10, 2, 10}.
3. A five-vertex counterexample to the tempting claim that the current
   equilibrium voltage is a one-step supermartingale.

All computations use fractions.Fraction. No floating-point sign decisions.
"""

from fractions import Fraction as F
from itertools import combinations


def solveF(A,b):
    n=len(b)
    if n==0: return []
    M=[[F(x) for x in A[i]]+[F(b[i])] for i in range(n)]
    for col in range(n):
        piv=next(r for r in range(col,n) if M[r][col])
        M[col],M[piv]=M[piv],M[col]
        pv=M[col][col]
        M[col]=[z/pv for z in M[col]]
        for r in range(n):
            if r==col: continue
            q=M[r][col]
            if q:
                M[r]=[M[r][j]-q*M[col][j] for j in range(n+1)]
    return [M[i][-1] for i in range(n)]


def connected(n,edges):
    adj=[[] for _ in range(n)]
    for u,v in edges:
        adj[u].append(v); adj[v].append(u)
    seen={0}; stack=[0]
    while stack:
        x=stack.pop()
        for y in adj[x]:
            if y not in seen:
                seen.add(y); stack.append(y)
    return len(seen)==n


def graph_struct(n,edges,root=0,target=None):
    if target is None: target=n-1
    adj=[[] for _ in range(n)]
    for i,(u,v) in enumerate(edges):
        adj[u].append((v,i)); adj[v].append((u,i))
    inter=[v for v in range(n) if v not in (root,target)]
    ix={v:i for i,v in enumerate(inter)}
    return adj,inter,ix


def srw_h(n,edges,root=0,target=None):
    if target is None: target=n-1
    adj,inter,ix=graph_struct(n,edges,root,target)
    A=[[F(int(i==j)) for j in range(len(inter))] for i in range(len(inter))]
    b=[F(0) for _ in inter]
    for x in inter:
        p=F(1,len(adj[x]))
        for y,_ in adj[x]:
            if y in ix: A[ix[x]][ix[y]]-=p
            elif y==target: b[ix[x]]+=p
    sol=solveF(A,b)
    h={root:F(0),target:F(1)}
    for v in inter: h[v]=sol[ix[v]]
    return h,adj,inter,ix


def fresh_sum_D(n,edges,start,root=0,target=None):
    """D = E_SRW sum over fresh traversals of h(next)-h(current)."""
    if target is None: target=n-1
    h,adj,inter,ix=srw_h(n,edges,root,target)
    m=len(edges)
    H={}
    for mask in sorted(range(1<<m), key=int.bit_count, reverse=True):
        A=[[F(int(i==j)) for j in range(len(inter))] for i in range(len(inter))]
        b=[F(0) for _ in inter]
        for x in inter:
            p=F(1,len(adj[x]))
            for y,ei in adj[x]:
                if (mask>>ei)&1:
                    if y in ix: A[ix[x]][ix[y]]-=p
                else:
                    cont=F(0) if y in (root,target) else H[mask|(1<<ei)][y]
                    b[ix[x]] += p*((h[y]-h[x])+cont)
        sol=solveF(A,b)
        vals={root:F(0),target:F(0)}
        for v in inter: vals[v]=sol[ix[v]]
        H[mask]=vals
    eidx={tuple(sorted(e)):i for i,e in enumerate(edges)}
    return H[1<<eidx[(min(root,start),max(root,start))]][start], h[start]


def orrw_values(n,edges,c,root=0,target=None):
    if target is None: target=n-1
    h,adj,inter,ix=srw_h(n,edges,root,target)
    m=len(edges)
    V={}
    for mask in sorted(range(1<<m),key=int.bit_count,reverse=True):
        A=[[F(int(i==j)) for j in range(len(inter))] for i in range(len(inter))]
        b=[F(0) for _ in inter]
        for x in inter:
            den=sum(c if (mask>>ei)&1 else F(1) for y,ei in adj[x])
            for y,ei in adj[x]:
                w=c if (mask>>ei)&1 else F(1)
                p=w/den
                if (mask>>ei)&1:
                    if y in ix: A[ix[x]][ix[y]]-=p
                    elif y==target: b[ix[x]]+=p
                else:
                    cont=F(0) if y==root else F(1) if y==target else V[mask|(1<<ei)][y]
                    b[ix[x]]+=p*cont
        sol=solveF(A,b)
        vals={root:F(0),target:F(1)}
        for v in inter: vals[v]=sol[ix[v]]
        V[mask]=vals
    return V,h,adj


def exhaustive_D(maxn=5):
    rows=[]
    for n in range(3,maxn+1):
        allE=list(combinations(range(n),2))
        gc=cases=negative=zeros=0
        min_positive=None
        for bm in range(1,1<<len(allE)):
            edges=[allE[i] for i in range(len(allE)) if (bm>>i)&1]
            if not connected(n,edges): continue
            gc+=1
            for start in range(1,n-1):
                if (0,start) not in edges: continue
                cases+=1
                D,_=fresh_sum_D(n,edges,start)
                if D<0:
                    negative+=1
                    raise AssertionError(("negative D",n,edges,start,D))
                if D==0:
                    zeros+=1
                elif min_positive is None or D<min_positive:
                    min_positive=D
        rows.append((n,gc,cases,negative,zeros,min_positive))
    return rows


def exhaustive_full_c(n,c):
    allE=list(combinations(range(n),2))
    gc=cases=0
    maxdiff=None
    for bm in range(1,1<<len(allE)):
        edges=[allE[i] for i in range(len(allE)) if (bm>>i)&1]
        if not connected(n,edges): continue
        gc+=1
        V,h,_=orrw_values(n,edges,c)
        eidx={tuple(sorted(e)):i for i,e in enumerate(edges)}
        for start in range(1,n-1):
            key=(0,start)
            if key not in eidx: continue
            cases+=1
            diff=V[1<<eidx[key]][start]-h[start]
            if maxdiff is None or diff>maxdiff: maxdiff=diff
            if diff>0:
                raise AssertionError(("C1 violation",n,c,edges,start,diff))
    return gc,cases,maxdiff


def harmonic_env(n,edges,mask,c=F(2),root=0,target=None):
    if target is None: target=n-1
    adj,inter,ix=graph_struct(n,edges,root,target)
    A=[[F(int(i==j)) for j in range(len(inter))] for i in range(len(inter))]
    b=[F(0) for _ in inter]
    for x in inter:
        den=sum(c if (mask>>ei)&1 else F(1) for y,ei in adj[x])
        for y,ei in adj[x]:
            w=c if (mask>>ei)&1 else F(1)
            p=w/den
            if y in ix: A[ix[x]][ix[y]]-=p
            elif y==target: b[ix[x]]+=p
    sol=solveF(A,b)
    h={root:F(0),target:F(1)}
    for v in inter: h[v]=sol[ix[v]]
    return h,adj


def voltage_counterexample():
    edges=[(0,1),(1,2),(1,4),(1,3),(0,2),(2,3),(2,4)]
    eidx={tuple(sorted(e)):i for i,e in enumerate(edges)}
    mask=(1<<eidx[(0,1)]) | (1<<eidx[(1,2)])
    h,adj=harmonic_env(5,edges,mask,F(2))
    x=2
    den=sum(F(2) if (mask>>ei)&1 else F(1) for y,ei in adj[x])
    nxt=F(0)
    for y,ei in adj[x]:
        w=F(2) if (mask>>ei)&1 else F(1)
        nm=mask if (mask>>ei)&1 else mask|(1<<ei)
        h2,_=harmonic_env(5,edges,nm,F(2))
        nxt += (w/den)*h2[y]
    assert h[x]==F(16,37)
    assert nxt==F(2329,5365)
    assert nxt-h[x]==F(9,5365)>0
    return h[x],nxt,nxt-h[x]


if __name__=="__main__":
    print("FIRST-ORDER D CERTIFICATE")
    for row in exhaustive_D(5):
        print(row)
    print("FULL C1 FINITE CHECKS ON n=5")
    for c in (F(11,10),F(2),F(10)):
        print("c=",c, exhaustive_full_c(5,c))
    print("DYNAMIC VOLTAGE COUNTEREXAMPLE")
    print(voltage_counterexample())
    print("ALL EXACT CHECKS PASSED")
