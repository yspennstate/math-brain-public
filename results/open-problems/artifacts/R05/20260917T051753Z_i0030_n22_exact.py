#!/usr/bin/env python3
"""Exact order-22 certificate for R05 / Aldous-Fill OP 7.30 finite metric.

Source representatives are the eight order-22 connected symmetric
(arc-transitive) graphs in Marston Conder's census
symmetricgraphs-orderupto30.txt (April 2014).

The checker uses only integer arithmetic.  It verifies:
  * simple, connected, regular graphs;
  * the eight valencies 2,5,10,11,6,20,4,21 are distinct, hence the
    frozen representatives are pairwise non-isomorphic;
  * constant diagonal and constant edge entries of A^m for 0<=m<=50;
  * (A^(m+1))_{xx} = d (A^m)_{xy} on every edge, 0<=m<=50;
  * exact distance-regularity profiles, showing graph 7 is the unique
    non-distance-regular representative at order 22.

Arc-transitivity/completeness of the order-22 source class is imported
from Conder's primary census; the algebraic claims below are independently checked.
"""
from collections import deque, defaultdict

N = 22

def mk(adj1):
    return {i-1:{j-1 for j in nbrs} for i,nbrs in adj1.items()}

G = {}

G[1] = {i:{(i-1)%N,(i+1)%N} for i in range(N)}

G[2]=mk({
1:[3,7,9,11,19],2:[5,13,15,17,21],3:[1,8,15,17,20],4:[6,9,11,14,22],
5:[2,7,11,14,16],6:[4,10,17,20,21],7:[1,5,12,20,21],8:[3,9,14,16,18],
9:[1,4,8,13,21],10:[6,11,16,18,19],11:[1,4,5,10,15],12:[7,14,18,19,22],
13:[2,9,16,19,22],14:[4,5,8,12,17],15:[2,3,11,18,22],16:[5,8,10,13,20],
17:[2,3,6,14,19],18:[8,10,12,15,21],19:[1,10,12,13,17],20:[3,6,7,16,22],
21:[2,6,7,9,18],22:[4,12,13,15,20]})

G[3]=mk({
1:[4,5,8,9,12,14,16,18,20,22],2:[3,6,7,10,11,13,15,17,19,21],
3:[2,5,8,9,12,14,16,18,20,22],4:[1,6,7,10,11,13,15,17,19,21],
5:[1,3,7,10,11,13,15,17,19,21],6:[2,4,8,9,12,14,16,18,20,22],
7:[2,4,5,9,12,14,16,18,20,22],8:[1,3,6,10,11,13,15,17,19,21],
9:[1,3,6,7,11,13,15,17,19,21],10:[2,4,5,8,12,14,16,18,20,22],
11:[2,4,5,8,9,14,16,18,20,22],12:[1,3,6,7,10,13,15,17,19,21],
13:[2,4,5,8,9,12,16,18,20,22],14:[1,3,6,7,10,11,15,17,19,21],
15:[2,4,5,8,9,12,14,18,20,22],16:[1,3,6,7,10,11,13,17,19,21],
17:[2,4,5,8,9,12,14,16,20,22],18:[1,3,6,7,10,11,13,15,19,21],
19:[2,4,5,8,9,12,14,16,18,22],20:[1,3,6,7,10,11,13,15,17,21],
21:[2,4,5,8,9,12,14,16,18,20],22:[1,3,6,7,10,11,13,15,17,19]})

G[4] = {i:(set(range(11,22)) if i<11 else set(range(0,11))) for i in range(N)}

G[5]=mk({
1:[12,16,18,19,21,22],2:[13,14,15,19,21,22],3:[13,14,16,17,18,22],4:[13,15,16,18,19,20],
5:[12,14,15,17,18,19],6:[14,16,17,19,20,21],7:[12,14,15,16,20,22],8:[12,13,15,16,17,21],
9:[15,17,18,20,21,22],10:[12,13,17,19,20,22],11:[12,13,14,18,20,21],
12:[1,5,7,8,10,11],13:[2,3,4,8,10,11],14:[2,3,5,6,7,11],15:[2,4,5,7,8,9],
16:[1,3,4,6,7,8],17:[3,5,6,8,9,10],18:[1,3,4,5,9,11],19:[1,2,4,5,6,10],
20:[4,6,7,9,10,11],21:[1,2,6,8,9,11],22:[1,2,3,7,9,10]})

G[6] = {i:{j for j in range(N) if j!=i and j!=(i^1)} for i in range(N)}

G[7]=mk({
1:[3,4,21,22],2:[3,4,21,22],3:[1,2,5,6],4:[1,2,5,6],5:[3,4,7,8],6:[3,4,7,8],
7:[5,6,9,10],8:[5,6,9,10],9:[7,8,11,12],10:[7,8,11,12],11:[9,10,13,14],12:[9,10,13,14],
13:[11,12,15,16],14:[11,12,15,16],15:[13,14,17,18],16:[13,14,17,18],17:[15,16,19,20],18:[15,16,19,20],
19:[17,18,21,22],20:[17,18,21,22],21:[1,2,19,20],22:[1,2,19,20]})

G[8] = {i:{j for j in range(N) if j!=i} for i in range(N)}

def matmul(A,B):
    n=len(A)
    C=[[0]*n for _ in range(n)]
    for i in range(n):
        for k,a in enumerate(A[i]):
            if a:
                Bk=B[k]
                for j,b in enumerate(Bk):
                    if b:
                        C[i][j]+=a*b
    return C

def identity(n):
    return [[1 if i==j else 0 for j in range(n)] for i in range(n)]

def matrix_from_adj(adj):
    A=[[0]*N for _ in range(N)]
    for i in range(N):
        for j in adj[i]:
            A[i][j]=1
    return A

def basic_check(adj):
    assert set(adj)==set(range(N))
    d=len(adj[0])
    assert all(len(adj[v])==d for v in range(N))
    for v in range(N):
        assert v not in adj[v]
        for w in adj[v]:
            assert v in adj[w]
    seen={0}
    q=deque([0])
    while q:
        v=q.popleft()
        for w in adj[v]:
            if w not in seen:
                seen.add(w); q.append(w)
    assert len(seen)==N
    return d

def walk_check(adj,d,max_power=50):
    A=matrix_from_adj(adj)
    M=identity(N)
    for m in range(max_power+1):
        diag={M[i][i] for i in range(N)}
        edge={M[i][j] for i in range(N) for j in adj[i]}
        assert len(diag)==1, (m,"diag",diag)
        assert len(edge)==1, (m,"edge",edge)
        MA=matmul(M,A)
        ev=next(iter(edge))
        assert all(MA[i][i]==d*ev for i in range(N)), (m,"identity")
        M=MA

def distance_profile(adj):
    profiles=defaultdict(set)
    for x in range(N):
        dist=[None]*N
        dist[x]=0
        q=deque([x])
        while q:
            v=q.popleft()
            for w in adj[v]:
                if dist[w] is None:
                    dist[w]=dist[v]+1; q.append(w)
        for y in range(N):
            k=dist[y]
            c=sum(k>0 and dist[z]==k-1 for z in adj[y])
            a=sum(dist[z]==k for z in adj[y])
            b=sum(dist[z]==k+1 for z in adj[y])
            profiles[k].add((c,a,b))
    return profiles

expected_degrees=[2,5,10,11,6,20,4,21]
assert len(G)==8
degrees=[]
distance_regular=[]
non_distance_regular=[]
for idx in range(1,9):
    adj=G[idx]
    d=basic_check(adj)
    degrees.append(d)
    walk_check(adj,d,50)
    prof=distance_profile(adj)
    if all(len(s)==1 for s in prof.values()):
        distance_regular.append(idx)
    else:
        non_distance_regular.append(idx)
        print("distance_regular_witness_graph",idx,
              {k:sorted(v) for k,v in prof.items() if len(v)>1})

assert degrees==expected_degrees, degrees
assert len(set(degrees))==8
assert distance_regular==[1,2,3,4,5,6,8], distance_regular
assert non_distance_regular==[7], non_distance_regular

print("order_22_graph_count",len(G))
print("order_22_valencies",degrees)
print("distance_regular_classes",distance_regular)
print("non_distance_regular_classes",non_distance_regular)
print("walk_power_max",50)
print("metric_largest_fully_certified_vertex_count",22)
print("RESULT PASS")
