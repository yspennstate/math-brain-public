#!/usr/bin/env python3
"""
R05/I0030 exact order-20 certificate.

Representatives are graph6 encodings transcribed from the 22 order-20
adjacency lists in Marston Conder's Dec-2021 complete census of connected
symmetric (= arc-transitive) graphs of orders 2..47.

Completeness and arc-transitivity are source facts.  The checks below are
exact/combinatorial: simplicity, connectedness, regularity, pairwise
non-isomorphism within each repeated valency, diagonal/edge walk
homogeneity, the identity (A^(m+1))_xx=d(A^m)_xy, and exact
distance-regularity witnesses.

No floating point arithmetic is used.
"""
import networkx as nx
import numpy as np

N = 20
G6 = ['SQC_GOA?O@?A?A?@??O?A??C??a??K??O', 'S?`???CAC_K?CGGCDG?k?O_Q@A?Co?BG?', 'S?Q???CAA_S?CCGGDO?i?OOQAA?Ag?DO?', 'SQCcQGaCOH@A?`?QOAI@CG@GOGSOAIGCO', 'SWK?WAB_?_AE@Bp??GXa??CKKOA?OYEO?', 'S]KoWWB?o@_E?B?B??W?E??K??u??]??W', 'S?]uf?FAoY@o?F?J?E_@o[?]oAu_Ef?F?', 'SKGQlPPg_S_k`QQ`OAi@SHDCWgcoArGDG', 'SKCalPPg_I`SPPaaODQ?iDDGggQgBLOCo', 'SKGRKqPW_L@I`aQPGDK?kDDCggagBTOCg', 'S?r???KBF_]?KKKKFw@}?oorBB?Fw?Fw?', 'S]Ku]WrKoX`e?r?rWE]@eKBKoKuWE]WEW', 'S?rFf_{N?]@w?{?{WFe@w{BroN@wF`wF_', 'SQhRShdedRIqXieTLSkisUeeddarRTKkg', 'SQdbShhdbQqsdiYTQtJQkYTiUhSlQrQlG', 'S]Ku]WrKuXxeKrKrXe]XeKrKrKuXe]XeW', 'S?]uf@vmuy\\o\\vmzZmf\\o\\v]zmuzmf\\v?', 'S]~vfbNrp~f}{o{oXe]XeNB{{NoF~wF~w', 'S?B~vrw}F~~}~{~{^}F~~~~z~~f~~F~~?', 'S]~v~z~~p~f}r~r~]^~f}~N~{~v}^~}^w', 'S]~v~z~~v~~}~~~~^~~~}~~~~~v~~~~~w', 'S~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{']
DEG = [2, 3, 3, 4, 4, 4, 6, 6, 6, 6, 6, 8, 8, 9, 9, 10, 12, 12, 15, 16, 18, 19]

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
    for m in range(47):
        assert len({M[x, x] for x in range(N)}) == 1, (i, m, "diag")
        assert len({M[u-1, v-1] for u, v in G.edges()}) == 1, (i, m, "edge")
        AM = A @ M
        assert AM[0, 0] == d * M[edge[0]-1, edge[1]-1], (i, m, "identity")
        M = AM

    flag, witness = dr_exact(G)
    dr_flags.append(flag)
    dr_witnesses.append(witness)
    graphs.append(G)

# Conder's representatives are asserted non-isomorphic by the census.
# Independently verify all pairs sharing a valency (different valencies
# are automatically non-isomorphic).
for i in range(len(graphs)):
    for j in range(i+1, len(graphs)):
        if DEG[i] == DEG[j]:
            assert not nx.is_isomorphic(graphs[i], graphs[j]), (i+1, j+1)

expected_dr = [True, True, True, False, False, False, False, False, False, False,
               False, False, False, True, True, True, False, False, True, True,
               True, True]
assert dr_flags == expected_dr

print("R05 I0030 exact order-20 Conder-census certificate")
print("census_source_complete_classes", len(graphs))
print("valencies", DEG)
print("connected_regular_simple_all", True)
print("equal_valency_representatives_pairwise_nonisomorphic", True)
print("arc_transitivity_and_completeness_source",
      "Conder Dec-2021 complete census orders 2..47")
print("walk_regular_and_edge_walk_regular_exact_through_m", 46)
print("identity_(A^(m+1))xx=d(A^m)xy_exact_through_m", 46)
print("distance_regular_classes", [i+1 for i, x in enumerate(dr_flags) if x])
print("non_distance_regular_classes", [i+1 for i, x in enumerate(dr_flags) if not x])
for i, w in enumerate(dr_witnesses, 1):
    if w is not None:
        print("non_DR_witness", i, w)
print("metric_largest_fully_certified_vertex_count", 20)
print("RESULT PASS")
