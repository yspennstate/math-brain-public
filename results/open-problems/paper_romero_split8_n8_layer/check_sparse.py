from math import comb
from collections import deque

# Exact integer certificate for ROMERO-2025-SPLIT8, m=14,...,19.
# N_6(G;s,t) is computed as the two-root Laplacian minor determinant,
# i.e. the all-minors Matrix-Tree count of spanning two-forests that
# separate the terminals.

def edge(a,b):
    return tuple(sorted((a,b)))

def complete_edges(vertices):
    V=list(vertices)
    return {edge(V[i],V[j]) for i in range(len(V)) for j in range(i+1,len(V))}

def in_I0(n,m):
    return comb(n-1,2)+2 <= m <= comb(n,2)

def balloon_edges(n,m):
    if in_I0(n,m):
        E=complete_edges(range(n-1))
        r=m-comb(n-1,2)
        E |= {edge(n-1,u) for u in range(r)}
        return E
    if (n,m)==(4,4):
        return complete_edges(range(3)) | {edge(3,0)}
    E=balloon_edges(n-1,m-1)
    deg=[0]*(n-1)
    for a,b in E:
        deg[a]+=1; deg[b]+=1
    u=min(range(n-1), key=lambda x:(deg[x],x))
    return E | {edge(u,n-1)}

def connected(n,E):
    adj=[[] for _ in range(n)]
    for a,b in E:
        adj[a].append(b); adj[b].append(a)
    seen={0}; q=deque([0])
    while q:
        u=q.popleft()
        for v in adj[u]:
            if v not in seen:
                seen.add(v); q.append(v)
    return len(seen)==n

def distances(n,E,s):
    adj=[[] for _ in range(n)]
    for a,b in E:
        adj[a].append(b); adj[b].append(a)
    d=[None]*n; d[s]=0; q=deque([s])
    while q:
        u=q.popleft()
        for v in adj[u]:
            if d[v] is None:
                d[v]=d[u]+1; q.append(v)
    return d

def diameter(n,E):
    return max(max(distances(n,E,s)) for s in range(n))

def det_bareiss(A):
    A=[row[:] for row in A]
    n=len(A)
    if n==0: return 1
    sign=1; prev=1
    for k in range(n-1):
        if A[k][k]==0:
            r=next((i for i in range(k+1,n) if A[i][k]),None)
            if r is None: return 0
            A[k],A[r]=A[r],A[k]; sign=-sign
        pivot=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=A[i][j]*pivot-A[i][k]*A[k][j]
                assert num%prev==0
                A[i][j]=num//prev
        prev=pivot
        for i in range(k+1,n):
            A[i][k]=0
    return sign*A[-1][-1]

def two_forest_minor(n,E,s,t):
    L=[[0]*n for _ in range(n)]
    for a,b in E:
        L[a][a]+=1; L[b][b]+=1
        L[a][b]-=1; L[b][a]-=1
    keep=[v for v in range(n) if v not in (s,t)]
    M=[[L[i][j] for j in keep] for i in keep]
    return det_bareiss(M),M

terminal={14:(2,7),15:(3,7),16:(5,7),17:(1,7),18:(2,7),19:(3,7)}
expected={14:(840,900),15:(1404,1440),16:(2160,2592),17:(3024,3780),18:(5292,5880),19:(8232,8575)}
mods={
    16:({edge(2,4)},{edge(2,6)}),
    17:({edge(0,1)},{edge(4,6)}),
    18:({edge(0,1)},{edge(4,6)}),
    19:({edge(3,4)},{edge(4,6)}),
}

print('ROMERO-2025-SPLIT8 exact two-forest certificate')
print('m  |E(G)| |E(H)| diam(G) terminals N6(G) N6(H) gap')
for m in range(14,20):
    G=balloon_edges(8,m)
    s,t=terminal[m]
    assert len(G)==m and connected(8,G)
    assert distances(8,G,s)[t]==diameter(8,G)
    if m in (14,15):
        # Contract tail bridge 5-6 (so 6-7 becomes 5-7), then subdivide
        # core edge 0-1 by the restored vertex 6.
        H=set(G)
        H-={edge(5,6),edge(6,7),edge(0,1)}
        H|={edge(5,7),edge(0,6),edge(1,6)}
    else:
        rem,add=mods[m]
        H=(set(G)-rem)|add
    assert len(H)==m and connected(8,H)
    ng,_=two_forest_minor(8,G,s,t)
    nh,_=two_forest_minor(8,H,s,t)
    assert (ng,nh)==expected[m]
    assert nh>ng
    print(f'{m:2d} {len(G):6d} {len(H):6d} {diameter(8,G):7d} {s}-{t:1d} {ng:5d} {nh:5d} {nh-ng:4d}')
print('PASS: six source-open n=8 classes have explicit competitors with larger N_6.')
