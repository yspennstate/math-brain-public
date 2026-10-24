#!/usr/bin/env python3
"""
R05 / I0030 exact order-14 finite certificate.

Frozen source class:
  finite simple connected arc-transitive graphs.
Frozen walk:
  rate-one continuous-time simple random walk, P=A/d, H_t=exp(t(P-I)).
Frozen finite metric:
  largest N through which every admissible graph has a complete exact
  finite certificate.

Completeness input:
  Marston Conder's December 2021 complete census of connected symmetric
  (arc-transitive) graphs of orders 2..47.  The order-14 block has exactly
  the eight adjacency lists frozen below.

This checker uses only discrete graph decisions and Python integer arithmetic.
For the four lower-symmetry representatives (2--5) it independently verifies
arc-transitivity by exact marked-graph isomorphism.  For representatives
1,6,7,8 it verifies exact structural descriptions whose automorphism groups
are manifestly arc-transitive: C14, K7,7, K14 minus a perfect matching, K14.
It also verifies 1-walk-regularity and the coefficient identity behind the
heat-ratio proof through length 34.
"""
import itertools
import networkx as nx

DATA = {
1: (2, {
1:[2,14],2:[1,3],3:[2,4],4:[3,5],5:[4,6],6:[5,7],7:[6,8],8:[7,9],
9:[8,10],10:[9,11],11:[10,12],12:[11,13],13:[12,14],14:[1,13]}),
2: (3, {
1:[2,10,12],2:[1,5,7],3:[4,12,14],4:[3,7,9],5:[2,6,14],6:[5,9,11],
7:[2,4,8],8:[7,11,13],9:[4,6,10],10:[1,9,13],11:[6,8,12],12:[1,3,11],
13:[8,10,14],14:[3,5,13]}),
3: (4, {
1:[2,4,6,12],2:[1,3,5,11],3:[2,4,10,14],4:[1,3,9,13],5:[2,8,12,14],
6:[1,7,11,13],7:[6,10,12,14],8:[5,9,11,13],9:[4,8,10,12],
10:[3,7,9,11],11:[2,6,8,10],12:[1,5,7,9],13:[4,6,8,14],14:[3,5,7,13]}),
4: (4, {
1:[2,7,9,14],2:[1,3,8,10],3:[2,4,9,11],4:[3,5,10,12],5:[4,6,11,13],
6:[5,7,12,14],7:[1,6,8,13],8:[2,7,9,14],9:[1,3,8,10],
10:[2,4,9,11],11:[3,5,10,12],12:[4,6,11,13],13:[5,7,12,14],
14:[1,6,8,13]}),
5: (6, {
1:[2,4,6,10,12,14],2:[1,3,5,7,11,13],3:[2,4,6,8,12,14],
4:[1,3,5,7,9,13],5:[2,4,6,8,10,14],6:[1,3,5,7,9,11],
7:[2,4,6,8,10,12],8:[3,5,7,9,11,13],9:[4,6,8,10,12,14],
10:[1,5,7,9,11,13],11:[2,6,8,10,12,14],12:[1,3,7,9,11,13],
13:[2,4,8,10,12,14],14:[1,3,5,9,11,13]}),
6: (7, {i:[j for j in range(1,15) if (i-j)%2] for i in range(1,15)}),
7: (12, {
1:[2,3,4,5,6,7,9,10,11,12,13,14],
2:[1,3,4,5,6,7,8,10,11,12,13,14],
3:[1,2,4,5,6,7,8,9,11,12,13,14],
4:[1,2,3,5,6,7,8,9,10,12,13,14],
5:[1,2,3,4,6,7,8,9,10,11,13,14],
6:[1,2,3,4,5,7,8,9,10,11,12,14],
7:[1,2,3,4,5,6,8,9,10,11,12,13],
8:[2,3,4,5,6,7,9,10,11,12,13,14],
9:[1,3,4,5,6,7,8,10,11,12,13,14],
10:[1,2,4,5,6,7,8,9,11,12,13,14],
11:[1,2,3,5,6,7,8,9,10,12,13,14],
12:[1,2,3,4,6,7,8,9,10,11,13,14],
13:[1,2,3,4,5,7,8,9,10,11,12,14],
14:[1,2,3,4,5,6,8,9,10,11,12,13]}),
8: (13, {i:[j for j in range(1,15) if j != i] for i in range(1,15)})
}

def graph_from_adj(adj):
    G = nx.Graph()
    G.add_nodes_from(range(1,15))
    for u, vs in adj.items():
        for v in vs:
            G.add_edge(u,v)
    return G

GRAPHS = {k: graph_from_adj(adj) for k,(d,adj) in DATA.items()}

for k,(d,adj) in DATA.items():
    G=GRAPHS[k]
    assert set(G)==set(range(1,15))
    assert nx.is_connected(G)
    assert all(G.degree(u)==d for u in G)
    assert all(set(G.neighbors(u))==set(adj[u]) for u in G)

for i,j in itertools.combinations(GRAPHS,2):
    Gi,Gj=GRAPHS[i],GRAPHS[j]
    if Gi.number_of_edges()==Gj.number_of_edges():
        assert not nx.is_isomorphic(Gi,Gj)

assert nx.is_isomorphic(GRAPHS[1], nx.cycle_graph(range(1,15)))

odd={i for i in range(1,15) if i%2}
for u in range(1,15):
    for v in range(u+1,15):
        assert GRAPHS[6].has_edge(u,v) == ((u in odd) != (v in odd))

missing={(i,i+7) for i in range(1,8)}
for u in range(1,15):
    for v in range(u+1,15):
        assert GRAPHS[7].has_edge(u,v) == ((u,v) not in missing)

assert GRAPHS[8].number_of_edges()==14*13//2

def marked_arc_iso(G, base, target):
    G1=G.copy()
    G2=G.copy()
    nx.set_node_attributes(G1,0,"mark")
    nx.set_node_attributes(G2,0,"mark")
    G1.nodes[base[0]]["mark"]=1
    G1.nodes[base[1]]["mark"]=2
    G2.nodes[target[0]]["mark"]=1
    G2.nodes[target[1]]["mark"]=2
    node_match=nx.algorithms.isomorphism.categorical_node_match("mark",0)
    return nx.algorithms.isomorphism.GraphMatcher(
        G1,G2,node_match=node_match
    ).is_isomorphic()

for k in (2,3,4,5):
    G=GRAPHS[k]
    arcs=[]
    for u,v in G.edges():
        arcs.extend(((u,v),(v,u)))
    base=arcs[0]
    assert all(marked_arc_iso(G,base,a) for a in arcs)

def matmul(X,Y):
    n=len(X)
    Z=[[0]*n for _ in range(n)]
    for i in range(n):
        Zi=Z[i]
        for k,x in enumerate(X[i]):
            if x:
                Yk=Y[k]
                for j,y in enumerate(Yk):
                    if y:
                        Zi[j]+=x*y
    return Z

MMAX=34
for k,G in GRAPHS.items():
    nodes=sorted(G)
    idx={u:i for i,u in enumerate(nodes)}
    n=len(nodes)
    d=G.degree(nodes[0])
    A=[[0]*n for _ in range(n)]
    for u,v in G.edges():
        A[idx[u]][idx[v]]=A[idx[v]][idx[u]]=1
    M=[[int(i==j) for j in range(n)] for i in range(n)]
    x=nodes[0]
    y=next(iter(G.neighbors(x)))
    for m in range(MMAX+1):
        assert len({M[i][i] for i in range(n)})==1
        assert len({M[idx[u]][idx[v]] for u,v in G.edges()})==1
        Mnext=matmul(M,A)
        assert Mnext[idx[x]][idx[x]] == d*M[idx[x]][idx[y]]
        M=Mnext

print("R05 I0030 exact order-14 certificate")
print("census_complete_classes_order14", len(GRAPHS))
print("valencies", [DATA[k][0] for k in sorted(DATA)])
print("pairwise_nonisomorphic", True)
print("connected_regular_simple_all", True)
print("arc_transitivity_classes_2_to_5_marked_iso", True)
print("arc_transitivity_classes_1_6_7_8_manifest_structures",
      ["C14","K7,7","K14-minus-perfect-matching","K14"])
print("walk_regular_and_edge_walk_regular_exact_through_m", MMAX)
print("identity_(A^(m+1))xx=d(A^m)xy_exact_through_m", MMAX)
print("metric_largest_fully_certified_vertex_count", 14)
print("RESULT PASS")
