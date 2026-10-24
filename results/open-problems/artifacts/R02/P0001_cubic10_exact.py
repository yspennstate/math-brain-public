from itertools import combinations
import networkx as nx

# P0001 exact finite core.
#
# The 19 connected simple cubic graphs on 10 vertices are represented below
# using one LCF representation per Hamiltonian graph from the standard cubic
# graph table, plus the unique listed bridge example and Petersen graph.
# The checker verifies that the resulting 19 graphs are connected, simple,
# 3-regular, pairwise non-isomorphic, and then exhaustively enumerates every
# edge subset (2^15 per graph), retaining exactly the acyclic ones.
#
# For each distinct edge pair e,f it checks the integer Rayleigh inequality
#     Z_e Z_f - Z Z_ef >= 0,
# which is exactly equivalent to
#     P(e,f in F) <= P(e in F) P(f in F)
# under the uniform forest measure.
#
# Completeness of the list uses the classical external enumeration that there
# are exactly 19 connected simple cubic graphs on 10 vertices (McKay--Royle;
# also recorded in standard tables). The checker independently verifies the
# 19 supplied representatives are pairwise non-isomorphic.


def anti(prefix):
    return prefix + [-x for x in reversed(prefix)]


def rep(seq, k):
    return seq * k


def from_lcf(ds):
    n = len(ds)
    E = set()
    for i in range(n):
        E.add(tuple(sorted((i, (i + 1) % n))))
    for i, d in enumerate(ds):
        j = (i + d) % n
        assert i != j
        E.add(tuple(sorted((i, j))))
    G = nx.Graph()
    G.add_nodes_from(range(n))
    G.add_edges_from(sorted(E))
    assert len(G) == 10
    assert G.number_of_edges() == 15
    assert all(d == 3 for _, d in G.degree())
    assert nx.is_connected(G)
    return G


bridge_edges = [
    (0, 1), (0, 6), (0, 9), (1, 2), (1, 5),
    (2, 3), (2, 4), (3, 4), (3, 5), (4, 5),
    (6, 7), (6, 8), (7, 8), (7, 9), (8, 9),
]
G0 = nx.Graph()
G0.add_nodes_from(range(10))
G0.add_edges_from(bridge_edges)

lcfs = [
    [4, 2, 3, -2, -4, -3, 2, 2, -2, -2],
    anti([2, -3, -2, 2, 2]),
    anti([-2, -2, 3, 3, 3]),
    rep([2, 2, -2, -2, 5], 2),
    rep([2, 3, -2, 5, -3], 2),
    [2, -4, -2, 5, 2, 4, -2, 4, 5, -4],
    [5, 3, 5, -4, -3, 5, 2, 5, -2, 4],
    [-4, 3, 3, 5, -3, -3, 4, 2, 5, -2],
    [3, -3, 5, -3, 2, 4, -2, 5, 3, -4],
    anti([2, 3, -2, 3, -3]),
    [5, -2, 2, 4, -2, 5, 2, -4, -2, 2],
    rep([2, 5, -2, 5, 5], 2),
    rep([5, -3, -3, 3, 3], 2),
    rep([5, -4, 4, -4, 4], 2),
    rep([5, -4, 4, 5, 5], 2),
    rep([5], 10),
    rep([-4, 4, -3, 5, 3], 2),
]

graphs = [G0] + [from_lcf(x) for x in lcfs] + [nx.petersen_graph()]
assert len(graphs) == 19

for G in graphs:
    assert len(G) == 10
    assert G.number_of_edges() == 15
    assert nx.is_connected(G)
    assert all(d == 3 for _, d in G.degree())

for i in range(19):
    for j in range(i):
        assert not nx.is_isomorphic(graphs[i], graphs[j]), (i, j)


graph6 = [nx.to_graph6_bytes(G, header=False).decode().strip() for G in graphs]


def rayleigh_counts(G):
    edges = list(G.edges())
    m = len(edges)
    Z = 0
    one = [0] * m
    pair = [[0] * m for _ in range(m)]

    for mask in range(1 << m):
        parent = list(range(10))
        rank = [0] * 10

        def find(a):
            while parent[a] != a:
                parent[a] = parent[parent[a]]
                a = parent[a]
            return a

        selected = []
        acyclic = True
        for k, (u, v) in enumerate(edges):
            if (mask >> k) & 1:
                ru, rv = find(u), find(v)
                if ru == rv:
                    acyclic = False
                    break
                if rank[ru] < rank[rv]:
                    ru, rv = rv, ru
                parent[rv] = ru
                if rank[ru] == rank[rv]:
                    rank[ru] += 1
                selected.append(k)

        if not acyclic:
            continue

        Z += 1
        for i in selected:
            one[i] += 1
        for a in range(len(selected)):
            i = selected[a]
            for b in range(a + 1, len(selected)):
                j = selected[b]
                pair[i][j] += 1
                pair[j][i] += 1

    min_delta = None
    argmin = None
    for i, j in combinations(range(m), 2):
        # Uniform-forest p-NC is exactly Z * Z_ef <= Z_e * Z_f.
        delta = one[i] * one[j] - Z * pair[i][j]
        if min_delta is None or delta < min_delta:
            min_delta = delta
            argmin = (edges[i], edges[j], one[i], one[j], pair[i][j])
        assert delta >= 0, (edges[i], edges[j], delta)

    return Z, min_delta, argmin


print("P0001 cubic-10 exact certificate")
print(
    "graphs=", len(graphs),
    "pairwise_nonisomorphic=PASS",
    "all_connected_cubic_10=PASS_given_external_count_19",
)
print("graph6:")
for i, s in enumerate(graph6, 1):
    print(f"{i:02d} {s}")

global_min = None
for i, G in enumerate(graphs, 1):
    Z, min_delta, argmin = rayleigh_counts(G)
    global_min = min_delta if global_min is None else min(global_min, min_delta)
    print(
        f"G{i:02d}: forests={Z} min_Rayleigh_delta={min_delta} "
        f"witness_pair={argmin[0]},{argmin[1]}"
    )

print("global_min_Rayleigh_delta=", global_min)
print("PAIRWISE_NEGATIVE_CORRELATION_ALL_19=PASS")
