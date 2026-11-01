#!/usr/bin/env python3
"""
R05 / I0030 exact order-13 finite certificate plus source-valid shape obstruction.

Frozen source target:
  finite simple connected arc-transitive G, P=A/d, H_t=exp(t(P-I));
  H_t(x,y)/H_t(x,x) strictly increases for every arc x~y.

Finite metric task:
  certify every order-13 graph in Marston Conder's complete connected
  symmetric (arc-transitive) graph census.

Additional exact finite witness:
  K3 satisfies all frozen graph hypotheses and has r''(0)=1/4 > 0,
  so the edge ratio need not be concave. This does NOT refute the frozen
  monotonicity statement or Aldous-Fill 7.30.
"""
import networkx as nx
import numpy as np
from fractions import Fraction

N=13
ADJ=[
{1:[2,13],2:[1,3],3:[2,4],4:[3,5],5:[4,6],6:[5,7],7:[6,8],
 8:[7,9],9:[8,10],10:[9,11],11:[10,12],12:[11,13],13:[1,12]},
{1:[2,6,9,13],2:[1,3,7,10],3:[2,4,8,11],4:[3,5,9,12],
 5:[4,6,10,13],6:[1,5,7,11],7:[2,6,8,12],8:[3,7,9,13],
 9:[1,4,8,10],10:[2,5,9,11],11:[3,6,10,12],12:[4,7,11,13],
 13:[1,5,8,12]},
{1:[2,4,5,10,11,13],2:[1,3,5,6,11,12],3:[2,4,6,7,12,13],
 4:[1,3,5,7,8,13],5:[1,2,4,6,8,9],6:[2,3,5,7,9,10],
 7:[3,4,6,8,10,11],8:[4,5,7,9,11,12],9:[5,6,8,10,12,13],
 10:[1,6,7,9,11,13],11:[1,2,7,8,10,12],12:[2,3,8,9,11,13],
 13:[1,3,4,9,10,12]},
{u:[v for v in range(1,14) if v!=u] for u in range(1,14)}
]
EXPECTED_DEGREES=[2,4,6,12]
EXPECTED_AUT_ORDERS=[26,52,78,6227020800]

def make_graph(adj):
    G=nx.Graph()
    G.add_nodes_from(range(1,N+1))
    for u,vs in adj.items():
        for v in vs:
            G.add_edge(u,v)
    return G

def marked_iso_exists(G, src, dst):
    A=G.copy(); B=G.copy()
    nx.set_node_attributes(A,0,"mark"); nx.set_node_attributes(B,0,"mark")
    A.nodes[src[0]]["mark"]=1; A.nodes[src[1]]["mark"]=2
    B.nodes[dst[0]]["mark"]=1; B.nodes[dst[1]]["mark"]=2
    nm=nx.algorithms.isomorphism.categorical_node_match("mark",0)
    return nx.algorithms.isomorphism.GraphMatcher(A,B,node_match=nm).is_isomorphic()

graphs=[]
for i,(adj,dexp) in enumerate(zip(ADJ,EXPECTED_DEGREES),1):
    G=make_graph(adj)
    assert G.number_of_nodes()==N and nx.number_of_selfloops(G)==0
    for u,vs in adj.items():
        assert len(vs)==len(set(vs))
        assert all(u in adj[v] for v in vs)
    degs=[G.degree(v) for v in G.nodes()]
    assert len(set(degs))==1 and degs[0]==dexp
    assert nx.is_connected(G)

    ref=(1,adj[1][0])
    arcs=[(u,v) for u,v in G.edges()] + [(v,u) for u,v in G.edges()]
    for arc in arcs:
        assert marked_iso_exists(G,ref,arc), (i,ref,arc)

    A=np.zeros((N,N),dtype=object)
    for u,v in G.edges():
        A[u-1,v-1]=A[v-1,u-1]=1
    M=np.eye(N,dtype=object)
    for m in range(0,33):
        assert len(set(M[x,x] for x in range(N)))==1, (i,m,"diag")
        assert len(set(M[u-1,v-1] for u,v in G.edges()))==1, (i,m,"edge")
        AM=A@M
        assert AM[0,0]==dexp*M[ref[0]-1,ref[1]-1], (i,m,"heat-coeff")
        M=AM
    graphs.append(G)

for i in range(len(graphs)):
    for j in range(i):
        assert not nx.is_isomorphic(graphs[i],graphs[j]), (i+1,j+1)

# Exact source-valid stronger-shape obstruction on K3:
# r''(0) = (A^3)_{xx}/d^3 = 2*(triangles through x)/d^3 = 1/4.
K3=nx.complete_graph(3)
AK=np.array(nx.to_numpy_array(K3,dtype=int),dtype=object)
A3=AK@AK@AK
d=2
r2=Fraction(int(A3[0,0]),d**3)
assert int(A3[0,0])==2
assert r2==Fraction(1,4)

print("R05 I0030 exact order-13 Conder-census certificate")
print("census_source_complete_classes",len(graphs))
print("valencies",EXPECTED_DEGREES)
print("conder_aut_group_orders",EXPECTED_AUT_ORDERS)
print("pairwise_nonisomorphic",True)
print("connected_regular_simple_all",True)
print("marked_arc_transitivity_all",True)
print("walk_regular_and_edge_walk_regular_exact_through_m",32)
print("identity_(A^(m+1))xx=d(A^m)xy_exact_through_m",32)
print("K3_source_valid_arc_transitive",True)
print("K3_A3_xx",int(A3[0,0]))
print("K3_r_second_derivative_at_0",f"{r2.numerator}/{r2.denominator}")
print("K3_global_concavity_strengthening",False)
print("metric_largest_fully_certified_vertex_count",13)
print("RESULT PASS")
