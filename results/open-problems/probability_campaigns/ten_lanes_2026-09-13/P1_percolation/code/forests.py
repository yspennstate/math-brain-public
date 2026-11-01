r"""Fast exact forest counting for (multi)graphs, and the uniform-forest covariance test.

F(G) = number of acyclic edge subsets of G = T_G(2,1).
Computed by the connected-partition DP:  f(S) = sum over blocks B containing min(S)
of tau(G[B]) * f(S \ B), with tau = number of spanning trees of the induced
sub-multigraph (Kirchhoff, exact integer arithmetic).

Grimmett's conjecture:  F(G) * F(G/e/f)  <=  F(G/e) * F(G/f)   for all e != f.
"""
import itertools, sys
from fractions import Fraction

def int_det(M):
    """exact integer determinant by fraction-free Gaussian elimination (Bareiss)."""
    n=len(M)
    if n==0: return 1
    A=[row[:] for row in M]; sign=1; prev=1
    for k in range(n-1):
        if A[k][k]==0:
            for i in range(k+1,n):
                if A[i][k]!=0:
                    A[k],A[i]=A[i],A[k]; sign=-sign; break
            else: return 0
        for i in range(k+1,n):
            for j in range(k+1,n):
                A[i][j]=(A[i][j]*A[k][k]-A[i][k]*A[k][j])//prev
        prev=A[k][k]
    return sign*A[n-1][n-1]

def tau(nodes, adj):
    """spanning trees of the sub-multigraph induced on the list `nodes` (adj = dict of
    multiplicities keyed by frozenset pairs)."""
    k=len(nodes)
    if k==0: return 0
    if k==1: return 1
    idx={v:i for i,v in enumerate(nodes)}
    L=[[0]*k for _ in range(k)]
    for i,u in enumerate(nodes):
        for j in range(i+1,k):
            v=nodes[j]
            c=adj.get((u,v),0)+adj.get((v,u),0)
            if c:
                L[i][j]-=c; L[j][i]-=c; L[i][i]+=c; L[j][j]+=c
    M=[row[:k-1] for row in L[:k-1]]
    return int_det(M)

def forest_count(verts, edges):
    """number of acyclic subsets of the multigraph (verts, edges)."""
    verts=list(verts); n=len(verts)
    pos={v:i for i,v in enumerate(verts)}
    adj={}
    for (u,v) in edges:
        if u==v: continue          # loops are never in a forest
        key=(u,v) if pos[u]<pos[v] else (v,u)
        adj[key]=adj.get(key,0)+1
    taus=[0]*(1<<n)
    for S in range(1,1<<n):
        nodes=[verts[i] for i in range(n) if S>>i&1]
        taus[S]=tau(nodes,adj)
    f=[0]*(1<<n); f[0]=1
    for S in range(1,1<<n):
        low=(S&-S)
        rest=S^low
        tot=0
        sub=rest
        while True:
            B=sub|low
            if taus[B]: tot+=taus[B]*f[S^B]
            if sub==0: break
            sub=(sub-1)&rest
        f[S]=tot
    return f[(1<<n)-1]


def contract_id(verts, edges, ids, ei_id):
    """contract the edge whose id is ei_id; keep ids of the surviving edges.
    Returns (verts, edges, ids).  Loops created by the contraction are dropped,
    and their ids disappear -- a dropped id means that edge can never coexist
    with the contracted one in a forest."""
    k=ids.index(ei_id); (u,v)=edges[k]
    nv=[x for x in verts if x!=v]
    ne=[]; ni=[]
    for i,(a,b) in enumerate(edges):
        if i==k: continue
        a2=u if a==v else a; b2=u if b==v else b
        if a2==b2: continue           # loop: this edge is now forbidden
        ne.append((a2,b2)); ni.append(ids[i])
    return nv, ne, ni

def contract(verts, edges, ei):
    (u,v)=edges[ei]
    rep={x:x for x in verts}
    nv=[x for x in verts if x!=v]
    ne=[]
    for i,(a,b) in enumerate(edges):
        if i==ei: continue
        a2=u if a==v else a; b2=u if b==v else b
        if a2==b2: continue
        ne.append((a2,b2))
    return nv, ne

def cov_sign_uniform_forest(verts, edges, i, j):
    """sign of Cov(1{e_i in F}, 1{e_j in F}) under the uniform forest measure,
    as F(G)F(G/e/f) - F(G/e)F(G/f)."""
    FG=forest_count(verts,edges)
    v1,e1=contract(verts,edges,i)
    # index of edge j after removing edge i
    jj = j-1 if j>i else j
    FGe=forest_count(v1,e1)
    v2,e2=contract(verts,edges,j)
    ii = i-1 if i>j else i
    FGf=forest_count(v2,e2)
    v3,e3=contract(v1,e1,jj)
    FGef=forest_count(v3,e3)
    return FG*FGef-FGe*FGf, (FG,FGe,FGf,FGef)

def brute_forests(n, edges):
    from fk_lib import comps
    m=len(edges); c=0
    for mask in range(1<<m):
        if comps(n,edges,mask)==n-bin(mask).count("1"): c+=1
    return c

if __name__=="__main__":
    from graphs_iso import connected_iso
    # validation of the DP against brute force
    bad=0; tested=0
    for n in range(2,7):
        for edges in connected_iso(n, mmax=9):
            a=forest_count(list(range(n)),edges); b=brute_forests(n,edges)
            tested+=1
            if a!=b: bad+=1; print("MISMATCH",n,edges,a,b)
    print("forest-count DP validated on %d graphs, %d mismatches"%(tested,bad))
