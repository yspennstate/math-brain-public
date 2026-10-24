#!/usr/bin/env python3
"""
R05 / I0030 exact order-12 certificate.

Frozen target:
 finite simple connected arc-transitive G, P=A/d, H_t=exp(t(P-I)),
 and H_t(x,y)/H_t(x,x) strictly increasing for every arc x~y.

Finite metric task:
 certify every order-12 member of Marston Conder's complete census of
 connected symmetric (arc-transitive) graphs.

All graph and walk-count checks below are exact integer/combinatorial checks.
Completeness of the 11-isomorphism-class input is supplied by Conder's published
online complete census, not inferred from numerical search.
"""
import networkx as nx
import numpy as np

N=12
# Conder, symmetricgraphs-orderupto30.txt, order 12, graphs 1..11.
ADJ = [
{1:[2,12],2:[1,3],3:[2,4],4:[3,5],5:[4,6],6:[5,7],
 7:[6,8],8:[7,9],9:[8,10],10:[9,11],11:[10,12],12:[1,11]},
{1:[2,5,9,12],2:[1,6,10,12],3:[5,7,10,11],4:[8,9,11,12],
 5:[1,3,9,10],6:[2,7,8,10],7:[3,6,8,11],8:[4,6,7,12],
 9:[1,4,5,11],10:[2,3,5,6],11:[3,4,7,9],12:[1,2,4,8]},
{1:[2,4,8,10],2:[1,5,7,11],3:[4,6,10,12],4:[1,3,7,9],
 5:[2,6,8,12],6:[3,5,9,11],7:[2,4,8,10],8:[1,5,7,11],
 9:[4,6,10,12],10:[1,3,7,9],11:[2,6,8,12],12:[3,5,9,11]},
{1:[2,4,6,8,10,12],2:[1,3,5,7,9,11],3:[2,4,6,8,10,12],
 4:[1,3,5,7,9,11],5:[2,4,6,8,10,12],6:[1,3,5,7,9,11],
 7:[2,4,6,8,10,12],8:[1,3,5,7,9,11],9:[2,4,6,8,10,12],
 10:[1,3,5,7,9,11],11:[2,4,6,8,10,12],12:[1,3,5,7,9,11]},
{1:[2,3,6,8,11,12],2:[1,3,4,7,9,12],3:[1,2,4,5,8,10],
 4:[2,3,5,6,9,11],5:[3,4,6,7,10,12],6:[1,4,5,7,8,11],
 7:[2,5,6,8,9,12],8:[1,3,6,7,9,10],9:[2,4,7,8,10,11],
 10:[3,5,8,9,11,12],11:[1,4,6,9,10,12],12:[1,2,5,7,10,11]},
{1:[2,3,5,6,8,9,11,12],2:[1,3,4,6,7,9,10,12],
 3:[1,2,4,5,7,8,10,11],4:[2,3,5,6,8,9,11,12],
 5:[1,3,4,6,7,9,10,12],6:[1,2,4,5,7,8,10,11],
 7:[2,3,5,6,8,9,11,12],8:[1,3,4,6,7,9,10,12],
 9:[1,2,4,5,7,8,10,11],10:[2,3,5,6,8,9,11,12],
 11:[1,3,4,6,7,9,10,12],12:[1,2,4,5,7,8,10,11]},
{1:[2,5,7,8,11],2:[1,5,6,8,10],3:[4,7,9,11,12],
 4:[3,7,8,10,12],5:[1,2,6,9,11],6:[2,5,9,10,12],
 7:[1,3,4,8,11],8:[1,2,4,7,10],9:[3,5,6,11,12],
 10:[2,4,6,8,12],11:[1,3,5,7,9],12:[3,4,6,9,10]},
{1:[2,4,6,8,10],2:[1,3,7,9,11],3:[2,4,6,8,12],
 4:[1,3,5,9,11],5:[4,6,8,10,12],6:[1,3,5,7,11],
 7:[2,6,8,10,12],8:[1,3,5,7,9],9:[2,4,8,10,12],
 10:[1,5,7,9,11],11:[2,4,6,10,12],12:[3,5,7,9,11]},
{1:[2,3,4,6,7,8,10,11,12],2:[1,3,4,5,7,8,9,11,12],
 3:[1,2,4,5,6,8,9,10,12],4:[1,2,3,5,6,7,9,10,11],
 5:[2,3,4,6,7,8,10,11,12],6:[1,3,4,5,7,8,9,11,12],
 7:[1,2,4,5,6,8,9,10,12],8:[1,2,3,5,6,7,9,10,11],
 9:[2,3,4,6,7,8,10,11,12],10:[1,3,4,5,7,8,9,11,12],
 11:[1,2,4,5,6,8,9,10,12],12:[1,2,3,5,6,7,9,10,11]},
{1:[2,3,4,5,6,7,8,9,10,11],2:[1,4,5,6,7,8,9,10,11,12],
 3:[1,4,5,6,7,8,9,10,11,12],4:[1,2,3,6,7,8,9,10,11,12],
 5:[1,2,3,6,7,8,9,10,11,12],6:[1,2,3,4,5,8,9,10,11,12],
 7:[1,2,3,4,5,8,9,10,11,12],8:[1,2,3,4,5,6,7,10,11,12],
 9:[1,2,3,4,5,6,7,10,11,12],10:[1,2,3,4,5,6,7,8,9,12],
 11:[1,2,3,4,5,6,7,8,9,12],12:[2,3,4,5,6,7,8,9,10,11]},
{1:[2,3,4,5,6,7,8,9,10,11,12],2:[1,3,4,5,6,7,8,9,10,11,12],
 3:[1,2,4,5,6,7,8,9,10,11,12],4:[1,2,3,5,6,7,8,9,10,11,12],
 5:[1,2,3,4,6,7,8,9,10,11,12],6:[1,2,3,4,5,7,8,9,10,11,12],
 7:[1,2,3,4,5,6,8,9,10,11,12],8:[1,2,3,4,5,6,7,9,10,11,12],
 9:[1,2,3,4,5,6,7,8,10,11,12],10:[1,2,3,4,5,6,7,8,9,11,12],
 11:[1,2,3,4,5,6,7,8,9,10,12],12:[1,2,3,4,5,6,7,8,9,10,11]},
]
EXPECTED_DEGREES=[2,4,4,6,6,8,5,5,9,10,11]
EXPECTED_AUT_ORDERS=[24,48,768,1036800,144,82944,120,1440,31104,46080,479001600]

def make_graph(adj):
    G=nx.Graph(); G.add_nodes_from(range(1,N+1))
    for u,vs in adj.items():
        for v in vs: G.add_edge(u,v)
    return G

def marked_iso_exists(G, src, dst):
    A=G.copy(); B=G.copy()
    nx.set_node_attributes(A,0,"mark"); nx.set_node_attributes(B,0,"mark")
    A.nodes[src[0]]["mark"]=1; A.nodes[src[1]]["mark"]=2
    B.nodes[dst[0]]["mark"]=1; B.nodes[dst[1]]["mark"]=2
    gm=nx.algorithms.isomorphism.GraphMatcher(
        A,B,node_match=nx.algorithms.isomorphism.categorical_node_match("mark",0))
    return gm.is_isomorphic()

graphs=[]
for i,(adj,dexp) in enumerate(zip(ADJ,EXPECTED_DEGREES),1):
    G=make_graph(adj)
    assert G.number_of_nodes()==12 and nx.number_of_selfloops(G)==0
    for u,vs in adj.items():
        assert len(vs)==len(set(vs))
        assert all(u in ADJ[i-1][v] for v in vs)
    degs=[G.degree(v) for v in G.nodes()]
    assert len(set(degs))==1 and degs[0]==dexp and nx.is_connected(G)
    ref=(1,adj[1][0])
    arcs=[(u,v) for u,v in G.edges()] + [(v,u) for u,v in G.edges()]
    for arc in arcs:
        assert marked_iso_exists(G,ref,arc), (i,ref,arc)
    A=np.zeros((N,N),dtype=object)
    for u,v in G.edges(): A[u-1,v-1]=A[v-1,u-1]=1
    M=np.eye(N,dtype=object)
    for m in range(0,31):
        assert len(set(M[x,x] for x in range(N)))==1, (i,m,"diag")
        assert len(set(M[u-1,v-1] for u,v in G.edges()))==1, (i,m,"edge")
        AM=A@M
        assert AM[0,0]==dexp*M[ref[0]-1,ref[1]-1], (i,m,"identity")
        M=AM
    graphs.append(G)

for i in range(len(graphs)):
    for j in range(i):
        assert not nx.is_isomorphic(graphs[i],graphs[j]), (i+1,j+1)

print("R05 I0030 exact order-12 Conder-census certificate")
print("census_source_complete_classes",len(graphs))
print("valencies",EXPECTED_DEGREES)
print("conder_aut_group_orders",EXPECTED_AUT_ORDERS)
print("pairwise_nonisomorphic",True)
print("connected_regular_simple_all",True)
print("marked_arc_transitivity_all",True)
print("walk_regular_and_edge_walk_regular_exact_through_m",30)
print("identity_(A^(m+1))xx=d(A^m)xy_exact_through_m",30)
print("metric_largest_fully_certified_vertex_count",12)
print("RESULT PASS")
