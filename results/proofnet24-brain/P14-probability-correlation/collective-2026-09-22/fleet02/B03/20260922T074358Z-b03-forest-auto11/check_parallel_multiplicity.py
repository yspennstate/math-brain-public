from fractions import Fraction
from itertools import combinations

def forest_stats(n, edges, marks=(), condition_disconnect=None, condition_edge=None):
    """Exact unit-forest counts. condition_edge=i means require physical edge i."""
    m=len(edges)
    Z=0
    N=[0]*m
    P=[[0]*m for _ in range(m)]
    for mask in range(1<<m):
        if condition_edge is not None and not (mask>>condition_edge)&1:
            continue
        par=list(range(n))
        def find(x):
            while par[x]!=x:
                par[x]=par[par[x]]
                x=par[x]
            return x
        ok=True
        inds=[]
        for i,(u,v) in enumerate(edges):
            if (mask>>i)&1:
                ru,rv=find(u),find(v)
                if ru==rv:
                    ok=False
                    break
                par[ru]=rv
                inds.append(i)
        if not ok:
            continue
        if condition_disconnect is not None:
            u,v=condition_disconnect
            if find(u)==find(v):
                continue
        Z+=1
        for i in inds:
            N[i]+=1
        for i,j in combinations(inds,2):
            P[i][j]+=1
            P[j][i]+=1
    return Z,N,P

def four_counts(n, edges, e, f, condition_disconnect=None, condition_edge=None):
    Z,N,P=forest_stats(n,edges,condition_disconnect=condition_disconnect,condition_edge=condition_edge)
    return Z,N[e],N[f],P[e][f]

def gap(t):
    Z,Ze,Zf,Zef=t
    return Ze*Zf-Z*Zef

def base_coeffs(n, edges, u,v,e,f):
    A,a,b,c = four_counts(n,edges,e,f)
    B,aa,bb,cc = four_counts(n,edges,e,f,condition_disconnect=(u,v))
    D0=a*b-A*c
    D1=aa*bb-B*cc
    M=a*bb+aa*b-A*cc-B*c
    return (A,B,a,aa,b,bb,c,cc,D0,M,D1)

def q(coeff,r):
    *_,D0,M,D1=coeff
    return D0+M*r+D1*r*r

# Named-partner 4-vertex base.
N_edges=[(0,1),(0,2),(0,3),(1,2)]
u,v=1,3
e,f=0,1 # 01,02
co=base_coeffs(4,N_edges,u,v,e,f)
assert co==(14,10,6,3,6,4,2,1,8,8,2)
assert [q(co,r) for r in range(6)] == [2*(r+2)**2 for r in range(6)]

# Exact one-step recurrence.
D0,M,D1=co[-3:]
for r in range(2,20):
    lhs=q(co,r)
    rhs=Fraction(r,r-1)*q(co,r-1)-Fraction(D0,r-1)+r*D1
    assert lhs==rhs

# A simple source whose contraction creates the doubled 13 class.
# g=14; contraction identifies 4 with 1, and 13,34 become parallel.
G_edges=[(0,1),(0,2),(0,3),(1,2),(1,3),(1,4),(3,4)]
g=5
all_counts=four_counts(5,G_edges,e,f)
cond_counts=four_counts(5,G_edges,e,f,condition_edge=g)
assert all_counts==(82,30,34,10)
assert gap(all_counts)==200
assert cond_counts==(34,12,14,4)
assert gap(cond_counts)==32==q(co,2)

# Verify the path-response lower bound D <= (2^ell-1) C for every
# connected terminal pair of every labelled simple graph through 5 vertices,
# using shortest-path length ell. Also record equality examples.
def graph_forest_pair_counts(n,edges):
    m=len(edges)
    pairs=list(combinations(range(n),2))
    C={p:0 for p in pairs}
    D={p:0 for p in pairs}
    for mask in range(1<<m):
        par=list(range(n))
        def find(x):
            while par[x]!=x:
                par[x]=par[par[x]]
                x=par[x]
            return x
        ok=True
        for i,(a,b) in enumerate(edges):
            if (mask>>i)&1:
                ra,rb=find(a),find(b)
                if ra==rb:
                    ok=False
                    break
                par[ra]=rb
        if not ok:
            continue
        for p in pairs:
            if find(p[0])==find(p[1]):
                C[p]+=1
            else:
                D[p]+=1
    return C,D

def shortest(n,edges,s,t):
    adj=[[] for _ in range(n)]
    for a,b in edges:
        adj[a].append(b); adj[b].append(a)
    q0=[s]; dist={s:0}
    for x in q0:
        if x==t:
            return dist[x]
        for y in adj[x]:
            if y not in dist:
                dist[y]=dist[x]+1
                q0.append(y)
    return None

checked_pairs=0
equalities=0
for n in range(2,6):
    allE=list(combinations(range(n),2))
    for gm in range(1<<len(allE)):
        edges=[allE[i] for i in range(len(allE)) if (gm>>i)&1]
        C,D=graph_forest_pair_counts(n,edges)
        for uv in combinations(range(n),2):
            ell=shortest(n,edges,*uv)
            if ell is None:
                continue
            checked_pairs+=1
            assert D[uv] <= (2**ell-1)*C[uv]
            if D[uv] == (2**ell-1)*C[uv]:
                equalities+=1

# Exhaustive minimality check for the crude "D1 >= D0/2 is necessary"
# idea: no witness on <=3 vertices, while the named-partner 4-vertex base
# is a smallest (vertices,edges) witness with all of h,e,f in one
# edge-biconnected block after h is added.
def edge_block_same(n,edges,h,eidx,fidx):
    E=edges+[h]
    m=len(E)
    rel=[set([i]) for i in range(m)]
    for mask in range(1,1<<m):
        inds=[i for i in range(m) if (mask>>i)&1]
        if len(inds)<3:
            continue
        deg=[0]*n
        adj=[[] for _ in range(n)]
        for i in inds:
            a,b=E[i]; deg[a]+=1;deg[b]+=1;adj[a].append(b);adj[b].append(a)
        verts=[x for x in range(n) if deg[x]]
        if not verts or any(deg[x]!=2 for x in verts):
            continue
        seen={verts[0]}; stack=[verts[0]]
        while stack:
            x=stack.pop()
            for y in adj[x]:
                if y not in seen:
                    seen.add(y);stack.append(y)
        if len(seen)!=len(verts):
            continue
        for i in inds:
            rel[i].update(inds)
    changed=True
    while changed:
        changed=False
        for i in range(m):
            z=set(rel[i])
            for j in list(z):
                z |= rel[j]
            if z!=rel[i]:
                rel[i]=z; changed=True
    return fidx in rel[eidx] and m-1 in rel[eidx]

small_witnesses=[]
for n in range(2,5):
    allE=list(combinations(range(n),2))
    for gm in range(1<<len(allE)):
        edges=[allE[i] for i in range(len(allE)) if (gm>>i)&1]
        if len(edges)<2:
            continue
        es=set(edges)
        for uv in combinations(range(n),2):
            if uv in es:
                continue
            for ee,ff in combinations(range(len(edges)),2):
                cc=base_coeffs(n,edges,*uv,ee,ff)
                d0,mm,d1=cc[-3:]
                q1=q(cc,1); q2=q(cc,2)
                if d0>0 and 2*d1<d0 and q1>=0 and q2>=0 and edge_block_same(n,edges,uv,ee,ff):
                    small_witnesses.append((n,len(edges),tuple(edges),uv,ee,ff,d0,mm,d1,q1,q2))
assert small_witnesses
best=min(small_witnesses)
assert best[0]==4 and best[1]==4
assert best[2]==tuple(N_edges) and best[3]==(1,3) and best[4:6]==(0,1)
assert best[6:]==(8,8,2,18,32)

print("PARTNER_BASE_COUNTS", co[:8])
print("PARTNER_GAP_POLYNOMIAL", f"Q_r={D0}+{M}r+{D1}r^2=2(r+2)^2")
print("SOURCE_PARENT_COUNTS", all_counts, "DELTA", gap(all_counts))
print("SOURCE_CONDITIONAL_G_COUNTS", cond_counts, "DELTA", gap(cond_counts))
print("PARALLEL_RECURRENCE", "Q_r=r/(r-1)Q_{r-1}-D0/(r-1)+rD1")
print("PATH_RESPONSE_REGRESSION_PAIRS", checked_pairs, "EQUALITY_CASES", equalities)
print("SMALLEST_CRUDE_CREDIT_WITNESS", best)
print("STATUS=PASS")
