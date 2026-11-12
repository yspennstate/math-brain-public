"""Checks for the examples in the paper.

For each graph: simple, connected, regular; arc-transitive (an automorphism found for every arc, by VF2 in networkx);
1-walk-regular (diagonal of A^k constant and A^k constant on edges for k < n, which suffices by Cayley-Hamilton);
distance-regular or not (intersection numbers per distance). Then
  * continuous time, floating point: r(t) = H_t(x,y)/H_t(x,x) on an edge is increasing on a grid of [0, 15], and
    r'(t) (central difference) agrees with the variance of lambda under the tilted local spectral law;
  * discrete time, exact rationals: for the lazy walk (I + A/d)/2, P^k(x,y)/P^k(x,x) is strictly increasing for
    1 <= k <= 60 on every edge from x.
Requires numpy and networkx."""
from fractions import Fraction as Fr
import itertools
import numpy as np
import networkx as nx
from networkx.algorithms.isomorphism import GraphMatcher


def wreath_cycle(n):
    """C_n[2K_1]: vertices (i, a), i in Z_n, a in {0, 1}; (i, a) ~ (j, b) iff j - i = +-1 mod n."""
    G = nx.Graph()
    for i in range(n):
        for a, b in itertools.product((0, 1), repeat=2):
            G.add_edge((i, a), ((i + 1) % n, b))
    return nx.convert_node_labels_to_integers(G, ordering='sorted')


def circulant(n, S):
    return nx.convert_node_labels_to_integers(nx.circulant_graph(n, S))


GRAPHS = {
    'Petersen': nx.petersen_graph(),
    'cube Q3': nx.convert_node_labels_to_integers(nx.hypercube_graph(3)),
    'C7[2K1]': wreath_cycle(7),
    'C11[2K1]': wreath_cycle(11),
    'circulant C13(1,5)': circulant(13, [1, 5]),
}


def arc_transitive_fast(G):
    """Seeded search: for each target arc, look for an automorphism with u0 -> u, v0 -> v."""
    u0, v0 = next(iter(G.edges()))
    nodes = list(G.nodes())
    for u, v in list(G.edges()) + [(b, a) for a, b in G.edges()]:
        H = G.copy()
        G2 = G.copy()
        nx.set_node_attributes(H, {w: 0 for w in nodes}, 'c'); H.nodes[u0]['c'] = 1; H.nodes[v0]['c'] = 2
        nx.set_node_attributes(G2, {w: 0 for w in nodes}, 'c'); G2.nodes[u]['c'] = 1; G2.nodes[v]['c'] = 2
        if not GraphMatcher(H, G2, node_match=lambda p, q: p['c'] == q['c']).is_isomorphic():
            return False
    return True


def int_powers(A, kmax):
    n = len(A); P = [[int(i == j) for j in range(n)] for i in range(n)]; out = [P]
    for _ in range(kmax):
        P = [[sum(P[i][l] * A[l][j] for l in range(n) if A[l][j]) for j in range(n)] for i in range(n)]
        out.append(P)
    return out


def one_walk_regular(G):
    n = G.number_of_nodes(); A = nx.to_numpy_array(G, nodelist=range(n), dtype=int).tolist()
    E = list(G.edges())
    for P in int_powers(A, n - 1):
        if len({P[i][i] for i in range(n)}) != 1 or len({P[u][v] for u, v in E}) != 1:
            return False
    return True


def distance_regular(G):
    return nx.is_distance_regular(G)


def continuous_checks(G):
    n = G.number_of_nodes(); d = G.degree(0)
    A = nx.to_numpy_array(G, nodelist=range(n)); L = np.eye(n) - A / d
    w, V = np.linalg.eigh(L)
    ts = np.linspace(0, 15, 3001); E = np.exp(-np.outer(ts, w))
    x = 0; worst_step = np.inf; worst_var = 0.0
    m = V[x] ** 2
    a = E @ m
    for y in G.neighbors(x):
        b = E @ (V[x] * V[y]); r = b / a
        worst_step = min(worst_step, np.diff(r).min())
        h = ts[1] - ts[0]
        dr = (r[2:] - r[:-2]) / (2 * h)
        tilt = E[1:-1] * m / a[1:-1, None]
        var = tilt @ (w ** 2) - (tilt @ w) ** 2
        worst_var = max(worst_var, np.abs(dr - var).max())
    return worst_step, worst_var


def lazy_discrete_exact(G, K=60):
    n = G.number_of_nodes(); d = G.degree(0); x = 0
    vec = [Fr(int(i == x)) for i in range(n)]
    nbr = {i: list(G.neighbors(i)) for i in range(n)}
    rs = {y: [] for y in nbr[x]}
    for k in range(1, K + 1):
        vec = [(vec[i] + sum(vec[j] for j in nbr[i]) / d) / 2 for i in range(n)]
        for y in nbr[x]:
            rs[y].append(vec[y] / vec[x])
    return all(all(s[i] < s[i + 1] for i in range(len(s) - 1)) for s in rs.values()), min(s[-1] for s in rs.values())


ok_all = True
for name, G in GRAPHS.items():
    n = G.number_of_nodes(); degs = {g for _, g in G.degree()}
    assert nx.is_connected(G) and len(degs) == 1 and nx.number_of_selfloops(G) == 0
    at = arc_transitive_fast(G); owr = one_walk_regular(G); dr = distance_regular(G)
    step, verr = continuous_checks(G); lazy_ok, last = lazy_discrete_exact(G)
    ok = at and owr and step > 0 and verr < 1e-6 and lazy_ok
    ok_all &= ok
    print(f'{name}: n={n} d={degs.pop()} arc_transitive={at} one_walk_regular={owr} distance_regular={dr} '
          f'min_grid_step={step:.3e} max|r\'-Var|={verr:.1e} lazy_strict_k<=60={lazy_ok} r_60={float(last):.6f} '
          f'{"PASS" if ok else "FAIL"}')
print('RESULT', 'PASS' if ok_all else 'FAIL')
