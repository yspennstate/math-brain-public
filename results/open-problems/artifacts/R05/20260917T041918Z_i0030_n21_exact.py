#!/usr/bin/env python3
"""
R05/I0030 exact order-21 certificate.

Representatives are graph6 encodings transcribed from the 13 order-21
adjacency lists in Marston Conder's complete census of connected symmetric
(= arc-transitive) graphs of orders 2..30.

Completeness and arc-transitivity are source facts. The checks below are
exact/combinatorial: simplicity, connectedness, regularity, pairwise
non-isomorphism within each repeated valency, diagonal/edge walk
homogeneity, the identity (A^(m+1))_xx=d(A^m)_xy, and exact
distance-regularity witnesses.

No floating-point arithmetic is used.
"""
import networkx as nx
import numpy as np

N = 21
G6 = ['T@`?_OC?O@?O?A?@?A??@??_?@C??I??__?G', 'TBj?goK?WD?W?D?E?@_?B??g?BD??u??X_?S', 'TA_@_P?a?ICOc_?HC`@?`SQ?C`A@_cGCGHD?', 'T@`CaOcPP`POSaIPOe@aaaIHEECc`aQSOcdC', 'TEYeZiwmuZMsr\\\\mVXeZj\\mizNDu]uZjXuys', 'T???F~}~f{^o~_~_^~~~}~~r~~F~}F~}B~~?', 'TBaDQhGZKeQCqPLhDJEHRMI_fUDJHQsHhEZG', 'T?X_lAs?rWLwDmoEYs?ugotZW@_oulBuAx_S', 'T~~}DERa{NkWShQdgpxbKITSdKwpeohTkKXn', 'T??@yxk\\BoRfjUlYVME[rtijYrFMXNUiRreO', 'TFz_ww[?wF?[?F?F?B_?F??w?Bf??~??z_?[', 'TFzf~z{~~~^{~~~~^~f~~~~z~~f~~~~~z~~{', 'T~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~']
DEG = [2, 4, 4, 6, 12, 14, 8, 8, 10, 10, 6, 18, 20]

def dr_exact(G):
    expected = {}
    witness = None
    for root in G:
        dist = nx.single_source_shortest_path_length(G, root)
        for v in G:
            k = dist[v]
            profile = (
                sum(dist[w] == k-1 for w in G[v]),
                sum(dist[w] == k for w in G[v]),
                sum(dist[w] == k+1 for w in G[v]),
            )
            if k not in expected:
                expected[k] = profile
            elif expected[k] != profile and witness is None:
                witness = (root, v, k, expected[k], profile)
    return witness is None, witness

graphs = []
dr_flags = []
dr_witnesses = []

for i, (code, d) in enumerate(zip(G6, DEG), 1):
    G = nx.from_graph6_bytes(code.encode())
    G = nx.convert_node_labels_to_integers(G, first_label=1)
    assert len(G) == N
    assert nx.number_of_selfloops(G) == 0
    assert nx.is_connected(G)
    assert all(G.degree(v) == d for v in G)

    A = np.zeros((N, N), dtype=object)
    for u, v in G.edges():
        A[u-1, v-1] = A[v-1, u-1] = 1

    M = np.eye(N, dtype=object)
    edge = next(iter(G.edges()))
    for m in range(49):
        assert len({M[x, x] for x in range(N)}) == 1, (i, m, "diag")
        assert len({M[u-1, v-1] for u, v in G.edges()}) == 1, (i, m, "edge")
        AM = A @ M
        assert AM[0, 0] == d * M[edge[0]-1, edge[1]-1], (i, m, "identity")
        M = AM

    flag, witness = dr_exact(G)
    dr_flags.append(flag)
    dr_witnesses.append(witness)
    graphs.append(G)

# Different valencies already imply non-isomorphism. Check every repeated
# valency class independently.
for i in range(len(graphs)):
    for j in range(i+1, len(graphs)):
        if DEG[i] == DEG[j]:
            assert not nx.is_isomorphic(graphs[i], graphs[j]), (i+1, j+1)

expected_dr = [True, False, True, False, False, True, False, False,
               True, True, False, True, True]
assert dr_flags == expected_dr

print("R05 I0030 exact order-21 Conder-census certificate")
print("census_source_complete_classes", len(graphs))
print("valencies", DEG)
print("connected_regular_simple_all", True)
print("equal_valency_representatives_pairwise_nonisomorphic", True)
print("arc_transitivity_and_completeness_source",
      "Conder complete census orders 2..30")
print("walk_regular_and_edge_walk_regular_exact_through_m", 48)
print("identity_(A^(m+1))xx=d(A^m)xy_exact_through_m", 48)
print("distance_regular_classes", [i+1 for i, x in enumerate(dr_flags) if x])
print("non_distance_regular_classes", [i+1 for i, x in enumerate(dr_flags) if not x])
for i, w in enumerate(dr_witnesses, 1):
    if w is not None:
        print("non_DR_witness", i, w)
print("metric_largest_fully_certified_vertex_count", 21)
print("RESULT PASS")
