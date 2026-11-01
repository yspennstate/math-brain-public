"""Independent check of the intersection-array formula for the maximum mean hitting time of a
distance-regular graph, by solving the hitting-time linear system on the actual graph.

For each target j, the vector h with h_j = 0 and h_i = 1 + (1/deg) sum_{u ~ i} h_u is the mean hitting
time.  Solving that for every j and taking the maximum gives tau_0 with no reference to the intersection
array at all.
"""
import numpy as np
import networkx as nx
from fractions import Fraction as F
from drg_hitting import tau0


def tau0_direct(G):
    nodes = list(G.nodes()); n = len(nodes)
    idx = {v: i for i, v in enumerate(nodes)}
    A = nx.to_numpy_array(G, nodelist=nodes)
    deg = A.sum(axis=1)
    best = 0.0
    for j in range(n):
        keep = [i for i in range(n) if i != j]
        M = np.eye(n - 1) - (A[np.ix_(keep, keep)] / deg[keep][:, None])
        h = np.linalg.solve(M, np.ones(n - 1))
        best = max(best, h.max())
    return best


CASES = [
    ("Petersen",     nx.petersen_graph(),              [3, 2],          [1, 1]),
    ("cube Q_3",     nx.hypercube_graph(3),            [3, 2, 1],       [1, 2, 3]),
    ("Q_4",          nx.hypercube_graph(4),            [4, 3, 2, 1],    [1, 2, 3, 4]),
    ("dodecahedron", nx.dodecahedral_graph(),          [3, 2, 1, 1, 1], [1, 1, 1, 2, 3]),
    ("Heawood",      nx.heawood_graph(),               [3, 2, 2],       [1, 1, 3]),
    ("Pappus",       nx.pappus_graph(),                [3, 2, 2, 1],    [1, 1, 2, 3]),
    ("Desargues",    nx.desargues_graph(),             [3, 2, 2, 1, 1], [1, 1, 2, 2, 3]),
    ("K_{3,3}",      nx.complete_bipartite_graph(3, 3),[3, 2],          [1, 3]),
    ("K_{5,5}",      nx.complete_bipartite_graph(5, 5),[5, 4],          [1, 5]),
    ("K_7",          nx.complete_graph(7),             [6],             [1]),
    ("C_12",         nx.cycle_graph(12),               [2, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 2]),
    ("icosahedron",  nx.icosahedral_graph(),           [5, 2, 1],       [1, 2, 5]),
]

print(f"{'graph':>14} {'n':>5} {'formula':>12} {'direct solve':>14} {'agree':>7}")
for name, G, b, c in CASES:
    t, n = tau0(b, c)
    d = tau0_direct(G)
    ok = abs(float(t) - d) < 1e-7
    print(f"{name:>14} {G.number_of_nodes():>5} {str(t):>12} {d:>14.6f} {'yes' if ok else 'NO':>7}")
