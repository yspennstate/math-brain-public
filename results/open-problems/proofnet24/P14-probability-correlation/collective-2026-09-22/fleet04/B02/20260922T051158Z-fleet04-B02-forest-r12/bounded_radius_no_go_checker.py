from itertools import combinations
from collections import deque, Counter


def canon(a,b): return (a,b) if a<b else (b,a)

def is_forest(n, E, S):
    p=list(range(n))
    def f(x):
        while p[x]!=x:
            p[x]=p[p[x]]; x=p[x]
        return x
    for i in S:
        a,b=E[i]; ra,rb=f(a),f(b)
        if ra==rb: return False
        p[rb]=ra
    return True

def connected(n,E,S,s,t):
    A=[[] for _ in range(n)]
    for i in S:
        a,b=E[i]; A[a].append((b,i)); A[b].append((a,i))
    q=[s]; seen={s}
    for u in q:
        for v,_ in A[u]:
            if v not in seen: seen.add(v); q.append(v)
    return t in seen

def path_edges(n,E,S,s,t):
    A=[[] for _ in range(n)]
    for i in S:
        a,b=E[i]; A[a].append((b,i)); A[b].append((a,i))
    q=deque([s]); par={s:(None,None)}
    while q:
        u=q.popleft()
        if u==t: break
        for v,i in A[u]:
            if v not in par: par[v]=(u,i); q.append(v)
    assert t in par
    out=[]; u=t
    while u!=s:
        u0,i=par[u]; out.append(i); u=u0
    return tuple(reversed(out))

def addable(n,E,S,e): return not connected(n,E,S,*e)

def jointly(n,E,S,e,f):
    p=list(range(n))
    def rt(x):
        while p[x]!=x:
            p[x]=p[p[x]]; x=p[x]
        return x
    def un(a,b):
        a,b=rt(a),rt(b)
        if a==b: return False
        p[b]=a; return True
    for i in S:
        if not un(*E[i]): return False
    return un(*e) and un(*f)

def forests(n,E):
    out=[]
    for m in range(1<<len(E)):
        S=frozenset(i for i in range(len(E)) if (m>>i)&1)
        if is_forest(n,E,S): out.append(S)
    return out

def k_connected(n,G,k=3):
    G=set(map(lambda x:canon(*x),G))
    V=range(n)
    for r in range(k):
        for rem in combinations(V,r):
            rem=set(rem); left=[v for v in V if v not in rem]
            if len(left)<=1: continue
            q=[left[0]]; seen={left[0]}
            for u in q:
                for a,b in G:
                    if a in rem or b in rem: continue
                    if a==u and b not in seen: seen.add(b); q.append(b)
                    elif b==u and a not in seen: seen.add(a); q.append(a)
            if len(seen)!=len(left): return False
    return True

def hk(adj,nR):
    L=len(adj); pu=[-1]*L; pv=[-1]*nR; dist=[0]*L; INF=10**9
    def bfs():
        q=deque(); found=False
        for u in range(L):
            if pu[u]<0: dist[u]=0; q.append(u)
            else: dist[u]=INF
        while q:
            u=q.popleft()
            for v in adj[u]:
                w=pv[v]
                if w<0: found=True
                elif dist[w]==INF: dist[w]=dist[u]+1; q.append(w)
        return found
    def dfs(u):
        for v in adj[u]:
            w=pv[v]
            if w<0 or (dist[w]==dist[u]+1 and dfs(w)):
                pu[u]=v; pv[v]=u; return True
        dist[u]=INF; return False
    m=0
    while bfs():
        for u in range(L):
            if pu[u]<0 and dfs(u): m+=1
    return m

def instance(n,G,e,f,R):
    e=canon(*e); f=canon(*f); G=list(map(lambda x:canon(*x),G))
    E=[x for x in G if x not in (e,f)]
    FS=forests(n,E); A=[S for S in FS if addable(n,E,S,e)]
    B=[S for S in FS if addable(n,E,S,f)]
    D=[S for S in FS if jointly(n,E,S,e,f)]
    Ds=set(D); NA=[S for S in FS if S not in set(A)]; BD=[S for S in B if S not in Ds]
    ridx={(X,Y):i for i,(X,Y) in enumerate((x,y) for x in A for y in BD)}
    right=list(ridx)
    J={}
    for H in D:
        J[H]={}
        miss=[i for i in range(len(E)) if i not in H]
        for k in range(1,R+1):
            vals=[]
            for T in combinations(miss,k):
                Hp=frozenset(set(H)|set(T))
                if is_forest(n,E,Hp) and addable(n,E,Hp,f) and Hp not in Ds: vals.append(Hp)
            J[H][k]=tuple(vals)
    left=[]; adj=[]
    for F in NA:
        P=path_edges(n,E,F,*e)
        for H in D:
            left.append((F,H)); nb=set()
            for k in range(1,R+1):
                if k>len(P): continue
                for C in combinations(P,k):
                    Fp=frozenset(set(F)-set(C))
                    if Fp not in set(A): continue
                    for Hp in J[H][k]: nb.add(ridx[(Fp,Hp)])
            adj.append(tuple(sorted(nb)))
    return E,FS,A,B,D,NA,BD,left,right,adj,J

def es(E,S): return tuple(E[i] for i in sorted(S))

# General bounded-radius no-go family, checked for representative radii.
for r in range(2,7):
    # theta endpoints a=0,b=1. P has r edges; Q has r+1. Triangle at a has f as edge c-d.
    a,b=0,1; nxt=2
    P=[]; prev=a
    for _ in range(r-1):
        v=nxt; nxt+=1; P.append(canon(prev,v)); prev=v
    P.append(canon(prev,b))
    Q=[]; prev=a
    for _ in range(r):
        v=nxt; nxt+=1; Q.append(canon(prev,v)); prev=v
    Q.append(canon(prev,b))
    c,d=nxt,nxt+1; nxt+=2
    e=canon(a,b); f=canon(c,d)
    tri=[canon(a,c),canon(a,d),f]
    G=[e]+P+Q+tri
    E=[x for x in G if x not in (e,f)]
    ix={g:i for i,g in enumerate(E)}
    H=frozenset()
    Pset=frozenset(ix[x] for x in P); Qset=frozenset(ix[x] for x in Q)
    F0=Qset
    Fjs=[frozenset(set(Pset)|{ix[q]}) for q in Q]
    assert all(is_forest(nxt,E,F) and not addable(nxt,E,F,e) for F in [F0]+Fjs)
    assert jointly(nxt,E,H,e,f)
    # exact J_k(empty): none below r, singleton P at r
    FS=forests(nxt,E) if len(E)<=16 else None
    # Direct local enumeration of join subsets is enough and avoids full forest census for larger r.
    Js={}
    for k in range(1,r+1):
        vals=[]
        for T in combinations(range(len(E)),k):
            S=frozenset(T)
            if is_forest(nxt,E,S) and addable(nxt,E,S,f) and not jointly(nxt,E,S,e,f): vals.append(S)
        Js[k]=vals
    assert all(len(Js[k])==0 for k in range(1,r))
    assert set(Js[r])=={Pset}
    outs=set()
    for F in [F0]+Fjs:
        pe=path_edges(nxt,E,F,*e)
        assert len(pe)>=r
        for C in combinations(pe,r): outs.add(frozenset(set(F)-set(C)))
    # For this selected S, union of first-coordinate outputs is exactly r+1 Q singletons.
    expected={frozenset({ix[q]}) for q in Q}
    assert outs==expected
    Ae=(1<<(2*r+1))-3*(1<<r)+1
    Ce=3*(1<<r)-2
    n00,n10,n01,n11,q=Ce,Ae,3*Ce,3*Ae,0
    gap=n10*n01-n00*n11+(n00+n10+n01+n11)*q
    assert gap==0
    print(f"family r={r}: Hall witness {r+2}>{r+1}; J_<r=0; J_r=1; partner_gap={gap}; marks nonbridges=yes")

# Strong nondegenerate r=2 witness: triangular-prism-plus-chord, both marks nonbridge and graph 3-connected.
n=6
G=[(0,2),(0,3),(0,4),(0,5),(1,2),(1,3),(1,5),(2,4),(3,4),(3,5)]
e=(1,5); f=(2,4)
assert k_connected(n,G,3)
E,FS,A,B,D,NA,BD,left,right,adj,J=instance(n,G,e,f,2)
assert (len(FS),len(A),len(B),len(D),len(NA),len(BD))==(177,115,115,71,62,44)
Aset=set(A); Bset=set(B)
n11=len(Aset&Bset); n10=len(Aset-Bset); n01=len(Bset-Aset); n00=len(set(FS)-Aset-Bset); q=n11-len(D)
assert (n00,n10,n01,n11,q)==(31,31,31,84,13)
gap=len(A)*len(B)-len(FS)*len(D)
assert gap==658==n10*n01-n00*n11+len(FS)*q
empty=frozenset(); assert empty in set(D)
assert len(J[empty][1])==0
assert len(J[empty][2])==1
H2=J[empty][2][0]
assert set(es(E,H2))=={(1,3),(3,5)}
ix={g:i for i,g in enumerate(E)}
Fraw=[[(0,2),(0,5),(1,2)],[(0,2),(1,3),(3,5)],[(0,5),(1,3),(3,5)],[(1,2),(1,3),(3,5)]]
W=[]
for rr in Fraw:
    F=frozenset(ix[canon(*x)] for x in rr); assert F in set(NA); W.append(F)
firstouts=set()
for F in W:
    P=path_edges(n,E,F,*e)
    for C in combinations(P,2): firstouts.add(frozenset(set(F)-set(C)))
expected={frozenset({ix[(0,2)]}),frozenset({ix[(0,5)]}),frozenset({ix[(1,2)]})}
assert firstouts==expected
# Full radius-2 matching, plus radius-3 repair.
m2=hk(adj,len(right)); assert m2==4398 and len(left)==4402
E3,FS3,A3,B3,D3,NA3,BD3,left3,right3,adj3,J3=instance(n,G,e,f,3)
m3=hk(adj3,len(right3)); assert m3==len(left3)==4402
print(f"3conn witness: cells={(n00,n10,n01,n11,q)}; residual={len(left)}<={len(right)}; Rayleigh_gap={gap}")
print(f"3conn radius2 explicit Hall witness=4>3; full_matching={m2}/{len(left)} deficiency={len(left)-m2}")
print(f"3conn radius3 diagnostic repair: full_matching={m3}/{len(left3)}")
print("ALL_EXACT_ASSERTIONS_PASSED")
