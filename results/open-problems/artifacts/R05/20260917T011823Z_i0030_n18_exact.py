#!/usr/bin/env python3
"""
R05/I0030 exact order-18 certificate.
Input representatives are a graph6 encoding of the 14 order-18 adjacency lists
in Marston Conder's Dec-2021 complete census of connected symmetric
(arc-transitive) graphs of orders 2..47. Completeness/arc-transitivity are
source facts; all checks below are exact/combinatorial.
"""
import networkx as nx
import numpy as np

N=18
G6=['QKGOOGA?O@?A?A?@??G?C_?D??_', 'QCO__OCOHCOG@@CC@@ACCGOQ?__', 'Q?d_`@?_BCqKICDGHOCI??WgAPO', 'Q??EE?oK?W@_KBKB@w?]?oKB?o?', 'QDp_goKorBSSBDDEB@eDBWoi`b?', 'QKU`OiHPadSIIEDHGosQQgSXQaO', 'Q??E]Zo{@wF_N{N{XfeXw{rBrK?', 'QKhTIpYhQsskhYUdSlIskUdidhO', 'Q??????~~~^{~w~w^{F~?~wB~_?', 'QDpd]hwj]lNW]ujZYudZ\\tlpzX_', 'Q??F~z{~Fw^_~~~~^~f~w~~B~{?', 'QFzf~z{~~~^{~~~~^~f~~~~z~~_', 'Q]~v~z~~v~~}~~~~^~~~}~~~~~o', 'Q~~~~~~~~~~~~~~~~~~~~~~~~~w']
DEG=[2,3,4,4,6,6,8,8,9,10,12,15,16,17]

def dr_exact(G):
    expected={}; witness=None
    for root in G:
        dist=nx.single_source_shortest_path_length(G,root)
        for v in G:
            k=dist[v]
            p=(sum(dist[w]==k-1 for w in G[v]),
               sum(dist[w]==k for w in G[v]),
               sum(dist[w]==k+1 for w in G[v]))
            if k not in expected: expected[k]=p
            elif expected[k]!=p and witness is None:
                witness=(root,v,k,expected[k],p)
    return witness is None,witness

graphs=[]; dr=[]; witnesses=[]
for i,(code,d) in enumerate(zip(G6,DEG),1):
    G=nx.from_graph6_bytes(code.encode())
    G=nx.convert_node_labels_to_integers(G,first_label=1)
    assert len(G)==N and nx.number_of_selfloops(G)==0 and nx.is_connected(G)
    assert all(G.degree(v)==d for v in G)

    A=np.zeros((N,N),dtype=object)
    for u,v in G.edges(): A[u-1,v-1]=A[v-1,u-1]=1
    M=np.eye(N,dtype=object)
    e=next(iter(G.edges()))
    for m in range(43):
        assert len({M[x,x] for x in range(N)})==1,(i,m,"diag")
        assert len({M[u-1,v-1] for u,v in G.edges()})==1,(i,m,"edge")
        AM=A@M
        assert AM[0,0]==d*M[e[0]-1,e[1]-1],(i,m,"identity")
        M=AM

    flag,w=dr_exact(G); dr.append(flag); witnesses.append(w); graphs.append(G)

# Distinct valencies distinguish all but class pairs 3/4, 5/6, 7/8.
for i,j in [(2,3),(4,5),(6,7)]:
    assert not nx.is_isomorphic(graphs[i],graphs[j]),(i+1,j+1)

expected_dr=[True,True,False,False,False,False,False,True,True,False,True,True,True,True]
assert dr==expected_dr
print("R05 I0030 exact order-18 Conder-census certificate")
print("census_source_complete_classes",len(graphs))
print("valencies",DEG)
print("connected_regular_simple_all",True)
print("equal_valency_representatives_pairwise_nonisomorphic",True)
print("arc_transitivity_and_completeness_source","Conder Dec-2021 census orders 2..47")
print("walk_regular_and_edge_walk_regular_exact_through_m",42)
print("identity_(A^(m+1))xx=d(A^m)xy_exact_through_m",42)
print("distance_regular_classes",[i+1 for i,x in enumerate(dr) if x])
print("non_distance_regular_classes",[i+1 for i,x in enumerate(dr) if not x])
for i,w in enumerate(witnesses,1):
    if w is not None: print("non_DR_witness",i,w)
print("metric_largest_fully_certified_vertex_count",18)
print("RESULT PASS")
