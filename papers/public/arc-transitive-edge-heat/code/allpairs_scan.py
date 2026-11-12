"""Floating-point scan: r_{xy}(t) = H_t(x,y)/H_t(x,x) for every pair of vertices of thirteen arc-transitive graphs (GP(10,2) is the dodecahedron).

For each graph: arc-transitivity is checked (an automorphism carrying a fixed arc to every arc, by VF2 in networkx),
distance-regularity is reported, and for x = 0 (enough, since the graphs are vertex-transitive) and every y the
smallest step of r_{xy} on a grid of [0, 20] is printed per distance d(x, y). A negative value would be a decrease.
Requires numpy and networkx."""
import numpy as np
import networkx as nx
from networkx.algorithms.isomorphism import GraphMatcher

ts = np.linspace(0, 20, 8001)


def gp(n, k):
    G = nx.Graph()
    for i in range(n):
        G.add_edge(('u', i), ('u', (i + 1) % n)); G.add_edge(('u', i), ('v', i)); G.add_edge(('v', i), ('v', (i + k) % n))
    return nx.convert_node_labels_to_integers(G)


def arc_transitive(G):
    u0, v0 = next(iter(G.edges()))
    for u, v in list(G.edges()) + [(b, a) for a, b in G.edges()]:
        H = G.copy(); G2 = G.copy()
        nx.set_node_attributes(H, 0, 'c'); H.nodes[u0]['c'] = 1; H.nodes[v0]['c'] = 2
        nx.set_node_attributes(G2, 0, 'c'); G2.nodes[u]['c'] = 1; G2.nodes[v]['c'] = 2
        if not GraphMatcher(H, G2, node_match=lambda p, q: p['c'] == q['c']).is_isomorphic():
            return False
    return True


graphs = {f'GP({n},{k})': gp(n, k) for n, k in [(4, 1), (5, 2), (8, 3), (10, 2), (10, 3), (12, 5), (24, 5)]}
graphs['L(Petersen)'] = nx.convert_node_labels_to_integers(nx.line_graph(nx.petersen_graph()))
graphs['Heawood'] = nx.heawood_graph()
graphs['Tutte-Coxeter'] = nx.convert_node_labels_to_integers(nx.LCF_graph(30, [-13, -9, 7, -7, 9, 13], 5))
graphs['Pappus'] = nx.pappus_graph()
graphs['F26 (LCF [-7,7]^13)'] = nx.convert_node_labels_to_integers(nx.LCF_graph(26, [-7, 7], 13))
graphs['icosahedron'] = nx.icosahedral_graph()
ok = True
for name, G in graphs.items():
    n = G.number_of_nodes(); d = G.degree(0)
    A = nx.to_numpy_array(G, nodelist=range(n)); L = np.eye(n) - A / d
    w, V = np.linalg.eigh(L); E = np.exp(-np.outer(ts, w))
    dist = nx.single_source_shortest_path_length(G, 0)
    a = E @ (V[0] ** 2)
    worst = {}
    for y in range(1, n):
        r = (E @ (V[0] * V[y])) / a
        m = np.diff(r).min()
        k = dist[y]
        if k not in worst or m < worst[k]: worst[k] = m
    at = arc_transitive(G)
    mono = min(worst.values()) > -1e-12
    ok &= at and mono
    print(f'{name}: n={n} d={d} arc_transitive={at} distance_regular={nx.is_distance_regular(G)} '
          f'distinct_eigenvalues={len(set(np.round(w, 8)))} min_step_by_distance=' +
          ' '.join(f'{k}:{v:.1e}' for k, v in sorted(worst.items())), flush=True)
print('RESULT', 'PASS' if ok else 'FAIL')
