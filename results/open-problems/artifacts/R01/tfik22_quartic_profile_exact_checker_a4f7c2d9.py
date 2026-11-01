#!/usr/bin/env python3
"""
Exact finite checker for R01 / KIM-MATTMAN-OH-2026-TFIK22-D34,
quartic profile (n4,n3)=(11,0).

The two edge lists are the two 4-regular 11-vertex, 22-edge MMN2A graphs
listed by Mattman--Pierce (2017). Wallis (2010), citing Meringer's
exhaustive regular-graph census, proves that up to isomorphism there are
exactly two triangle-free (4,11)-graphs.

This checker verifies for the two explicit representatives:
  * 11 vertices, 22 edges, 4-regular, connected, triangle-free;
  * non-isomorphism (also certified by different numbers of 4-cycles);
  * neither graph is 2-apex;
  * every immediate proper minor (edge deletion, edge contraction,
    vertex deletion) is 2-apex.

All tests are finite/combinatorial. NetworkX check_planarity uses an
exact graph algorithm; no floating-point numerical tolerance is involved.
"""

from itertools import combinations
import networkx as nx

E1 = [
    (1,6),(1,9),(1,10),(1,11),
    (2,6),(2,9),(2,10),(2,11),
    (3,7),(3,8),(3,9),(3,10),
    (4,7),(4,8),(4,9),(4,11),
    (5,7),(5,8),(5,10),(5,11),
    (6,7),(6,8),
]

E2 = [
    (1,5),(1,6),(1,7),(1,8),
    (2,6),(2,7),(2,8),(2,9),
    (3,7),(3,8),(3,9),(3,10),
    (4,8),(4,9),(4,10),(4,11),
    (5,9),(5,10),(5,11),
    (6,10),(6,11),(7,11),
]

def make_graph(edges):
    G = nx.Graph()
    G.add_nodes_from(range(1,12))
    G.add_edges_from(edges)
    return G

def triangle_count(G):
    return sum(nx.triangles(G).values()) // 3

def c4_count(G):
    # A 4-cycle has exactly two opposite vertex-pairs. For each unordered
    # pair {u,v}, choose two common neighbors; divide the total by 2.
    total = 0
    V = list(G.nodes())
    nbr = {u: set(G.neighbors(u)) for u in V}
    for i,u in enumerate(V):
        for v in V[i+1:]:
            k = len(nbr[u] & nbr[v])
            total += k * (k-1) // 2
    assert total % 2 == 0
    return total // 2

def two_apex_witness(G):
    V = list(G.nodes())
    # "At most two" apex vertices: planarity itself and one-apex are also
    # accepted, although they do not arise for the two parent graphs.
    if nx.check_planarity(G, counterexample=False)[0]:
        return ()
    for u in V:
        H = G.copy()
        H.remove_node(u)
        if nx.check_planarity(H, counterexample=False)[0]:
            return (u,)
    for u,v in combinations(V,2):
        H = G.copy()
        H.remove_nodes_from((u,v))
        if nx.check_planarity(H, counterexample=False)[0]:
            return (u,v)
    return None

def contract_simple(G, e):
    u,v = e
    H = nx.contracted_nodes(G, u, v, self_loops=False, copy=True)
    return nx.Graph(H)

def immediate_proper_minors(G):
    for e in list(G.edges()):
        H = G.copy()
        H.remove_edge(*e)
        yield ("edge_delete", e, H)
    for e in list(G.edges()):
        yield ("edge_contract", e, contract_simple(G,e))
    for v in list(G.nodes()):
        H = G.copy()
        H.remove_node(v)
        yield ("vertex_delete", v, H)

def verify(name, G):
    assert G.number_of_nodes() == 11
    assert G.number_of_edges() == 22
    assert set(dict(G.degree()).values()) == {4}
    assert nx.is_connected(G)
    assert triangle_count(G) == 0

    witness = two_apex_witness(G)
    assert witness is None, (name, "unexpected 2-apex witness", witness)

    minors = list(immediate_proper_minors(G))
    assert len(minors) == 55  # 22 deletions + 22 contractions + 11 vertex deletions
    witnesses = []
    for op,obj,H in minors:
        w = two_apex_witness(H)
        assert w is not None, (name, op, obj, "not certified 2-apex")
        witnesses.append((op,obj,w))

    print(
        f"{name}: n={G.number_of_nodes()} m={G.number_of_edges()} "
        f"degree=4 connected triangle_free YES C4_count={c4_count(G)}"
    )
    print(f"{name} 2-apex witness: {witness}")
    print(f"{name} immediate proper minors checked 2-apex: {len(witnesses)}/{len(minors)}")
    return c4_count(G)

G1 = make_graph(E1)
G2 = make_graph(E2)

print("networkx_version =", nx.__version__)
c1 = verify("E1", G1)
c2 = verify("E2", G2)
assert c1 != c2
assert not nx.is_isomorphic(G1,G2)
print(f"E1 != E2 certified by different C4 counts: {c1} != {c2}")
print("ALL_EXACT_TFIK22_QUARTIC_CHECKS_PASS")
