#!/usr/bin/env python3
from itertools import permutations, combinations
from math import comb
from collections import deque

V=range(8)
EDGES=list(combinations(V,2))
EI={e:i for i,e in enumerate(EDGES)}
FULL=(1<<28)-1

def perm_edge_cycles(p6):
    p={0:0,1:1}
    for i,v in enumerate(range(2,8)): p[v]=p6[i]
    em=[]
    for a,b in EDGES:
        x,y=sorted((p[a],p[b])); em.append(EI[(x,y)])
    seen=[0]*28; lens=[]
    for i in range(28):
        if not seen[i]:
            j=i; L=0
            while not seen[j]:
                seen[j]=1; L+=1; j=em[j]
            lens.append(L)
    return lens

def burnside_counts(K=8):
    tot=[0]*(K+1)
    for p6 in permutations(range(2,8)):
        c=[1]+[0]*28
        for L in perm_edge_cycles(p6):
            for k in range(28,L-1,-1): c[k]+=c[k-L]
        for k in range(K+1): tot[k]+=c[k]
    assert all(x%720==0 for x in tot)
    return [x//720 for x in tot]

def inI0(n,m): return comb(n-1,2)+2 <= m <= comb(n,2)
def balloon(n,m):
    if inI0(n,m):
        E=set(combinations(range(n-1),2))
        r=m-comb(n-1,2)
        E|={tuple(sorted((n-1,u))) for u in range(r)}
        return E
    if (n,m)==(4,4): return set(combinations(range(3),2))|{(0,3)}
    E=balloon(n-1,m-1); d=[0]*(n-1)
    for a,b in E: d[a]+=1; d[b]+=1
    u=min(range(n-1),key=lambda x:(d[x],x))
    return E|{tuple(sorted((u,n-1)))}

def bareiss(M):
    A=[r[:] for r in M]; n=len(A); prev=1; sign=1
    if n==0:return 1
    for k in range(n-1):
        if A[k][k]==0:
            q=next((i for i in range(k+1,n) if A[i][k]),None)
            if q is None:return 0
            A[k],A[q]=A[q],A[k]; sign=-sign
        piv=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                z=A[i][j]*piv-A[i][k]*A[k][j]
                assert z%prev==0
                A[i][j]=z//prev
        prev=piv
        for i in range(k+1,n): A[i][k]=0
    return sign*A[-1][-1]

def forest2(E,s,t):
    L=[[0]*8 for _ in range(8)]
    for a,b in E:
        L[a][a]+=1;L[b][b]+=1;L[a][b]-=1;L[b][a]-=1
    keep=[x for x in range(8) if x not in (s,t)]
    return bareiss([[L[i][j] for j in keep] for i in keep])

def emask(E): return sum(1<<EI[tuple(sorted(e))] for e in E)
def conn(M):
    A=[0]*8
    for i,(a,b) in enumerate(EDGES):
        if M>>i&1: A[a]|=1<<b; A[b]|=1<<a
    seen=front=1
    while front:
        nxt=0
        for u in range(8):
            if front>>u&1:nxt|=A[u]
        nxt&=~seen;seen|=nxt;front=nxt
    return (seen&255)==255

def diameter_pair(M):
    A=[[] for _ in range(8)]
    for i,(a,b) in enumerate(EDGES):
        if M>>i&1:A[a].append(b);A[b].append(a)
    best=(-1,0,1)
    for s in range(8):
        d=[-1]*8;d[s]=0;q=deque([s])
        while q:
            u=q.popleft()
            for v in A[u]:
                if d[v]<0:d[v]=d[u]+1;q.append(v)
        for t in range(s+1,8):
            if d[t]>best[0]:best=(d[t],s,t)
    return best[1],best[2]

def relabel(M,s,t):
    mp={s:0,t:1};z=2
    for v in range(8):
        if v not in (s,t):mp[v]=z;z+=1
    R=0
    for i,(a,b) in enumerate(EDGES):
        if M>>i&1:
            x,y=sorted((mp[a],mp[b]));R|=1<<EI[(x,y)]
    return R

def conv(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                if y:c[i+j]+=x*y
    return c

def splitvec(M):
    ec=[0]*256
    for S in range(256):
        ec[S]=sum(1 for i,(a,b) in enumerate(EDGES) if M>>i&1 and S>>a&1 and S>>b&1)
    C=[None]*256
    for sz in range(1,9):
        for S in range(1,256):
            if S.bit_count()!=sz:continue
            p=[comb(ec[S],j) for j in range(ec[S]+1)]
            r=(S&-S).bit_length()-1; rest=S^(1<<r); sub=rest
            while True:
                T=(1<<r)|sub
                if T!=S:
                    q=conv(C[T],[comb(ec[S^T],j) for j in range(ec[S^T]+1)])
                    if len(p)<len(q):p += [0]*(len(q)-len(p))
                    for j,x in enumerate(q):p[j]-=x
                if sub==0:break
                sub=(sub-1)&rest
            assert min(p)>=0; C[S]=p
    ans=[0]*29
    for S in range(256):
        if S&1 and not S&2:
            q=conv(C[S],C[255^S])
            for j,x in enumerate(q):ans[j]+=x
    return ans

def direct_dense(m):
    B=emask(balloon(8,m)); s,t=diameter_pair(B); B=relabel(B,s,t); bv=splitvec(B)
    k=28-m; checked=0
    for miss in combinations(range(28),k):
        G=FULL
        for e in miss:G^=1<<e
        if not conn(G):continue
        checked+=1
        gv=splitvec(G)
        assert all(gv[j]<=bv[j] for j in range(29))
    return checked

print("P26 ROMERO SPLIT8 independent exact cross-check")
bc=burnside_counts()
print("Burnside terminal-fixed missing-edge orbit counts k=2..8:",bc[2:9])
assert bc[2:9]==[13,43,137,419,1189,3021,6860]

term={14:(2,7),15:(3,7),16:(5,7),17:(1,7),18:(2,7),19:(3,7)}
mods={16:({(2,4)},{(2,6)}),17:({(0,1)},{(4,6)}),18:({(0,1)},{(4,6)}),19:({(3,4)},{(4,6)})}
want={14:(840,900),15:(1404,1440),16:(2160,2592),17:(3024,3780),18:(5292,5880),19:(8232,8575)}
got={}
for m in range(14,20):
    G=balloon(8,m); s,t=term[m]
    if m in (14,15):
        H=set(G)-{(5,6),(6,7),(0,1)}
        H|={(5,7),(0,6),(1,6)}
    else:
        rem,add=mods[m];H=(set(G)-rem)|add
    got[m]=(forest2(G,s,t),forest2(H,s,t))
    assert got[m]==want[m] and got[m][1]>got[m][0]
print("low-density N6 determinant pairs:",got)

for m,w in [(26,comb(28,2)),(25,comb(28,3))]:
    checked=direct_dense(m)
    print(f"direct labeled dense check m={m}: connected={checked}, all coefficientwise dominated")
    assert checked==w
print("ALL_P26_ROMERO_CROSSCHECKS_PASS")
