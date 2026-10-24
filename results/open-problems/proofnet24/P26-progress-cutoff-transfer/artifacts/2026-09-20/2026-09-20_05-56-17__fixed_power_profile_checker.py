from fractions import Fraction
from collections import defaultdict, deque
import networkx as nx
import numpy as np


def tree_jump_distribution(d, m):
    q = d - 1
    counts = defaultdict(int)
    D = 0
    by_j = {}
    for j in range(1, m + 1):
        cj = defaultdict(int)
        cj[j] += q**j
        for a in range(1, j):
            cj[j - 2 * a] += (q - 1) * q ** (j - a - 1)
        cj[-j] += 1
        Nj = d * q ** (j - 1)
        assert sum(cj.values()) == Nj
        by_j[j] = dict(sorted(cj.items()))
        D += Nj
        for k, v in cj.items():
            counts[k] += v
    return D, dict(sorted(counts.items())), by_j


def moments(d, m):
    D, counts, _ = tree_jump_distribution(d, m)
    v = sum(Fraction(delta * c, D) for delta, c in counts.items())
    e2 = sum(Fraction(delta * delta * c, D) for delta, c in counts.items())
    q = d - 1
    den = sum(q ** (j - 1) for j in range(1, m + 1))
    v_formula = (
        sum(Fraction(j * q ** (j - 1), 1) for j in range(1, m + 1))
        - Fraction(2, q * q - 1) * sum(q**j - 1 for j in range(1, m + 1))
    ) / den
    assert v == v_formula
    return D, counts, v, e2


def graph_girth(G):
    best = 10**9
    for s in G.nodes():
        dist = {s: 0}
        parent = {s: None}
        Q = deque([s])
        while Q:
            u = Q.popleft()
            for v in G[u]:
                if v not in dist:
                    dist[v] = dist[u] + 1
                    parent[v] = u
                    Q.append(v)
                elif parent[u] != v:
                    best = min(best, dist[u] + dist[v] + 1)
    return best


# Exact radial combinatorics over a grid of fixed powers.
for d in range(3, 10):
    for m in range(2, 6):
        D, counts, v, e2 = moments(d, m)
        q = d - 1
        assert D == d * sum(q**j for j in range(m))
        assert v > 0 and e2 > 0
        assert q**m < D - 1

# Finite adjacency-polynomial check for m=3 on the McGee graph.
G = nx.LCF_graph(24, [12, 7, -7], 8)
assert set(dict(G.degree()).values()) == {3}
assert graph_girth(G) == 7
nodes = list(G.nodes())
idx = {v: i for i, v in enumerate(nodes)}
n = len(nodes)
A = np.zeros((n, n), dtype=object)
for u, v in G.edges():
    A[idx[u], idx[v]] = 1
    A[idx[v], idx[u]] = 1
I = np.eye(n, dtype=object)
A2 = A @ A - 3 * I
A3 = A @ A2 - 2 * A

dist = dict(nx.all_pairs_shortest_path_length(G, cutoff=3))
M2 = np.zeros((n, n), dtype=object)
M3 = np.zeros((n, n), dtype=object)
Cube = np.zeros((n, n), dtype=object)
for u in nodes:
    for v, r in dist[u].items():
        if r == 2:
            M2[idx[u], idx[v]] = 1
        if r == 3:
            M3[idx[u], idx[v]] = 1
        if 1 <= r <= 3:
            Cube[idx[u], idx[v]] = 1
assert np.array_equal(A2, M2)
assert np.array_equal(A3, M3)
assert np.array_equal(Cube, A + A2 + A3)
assert set(int(x) for x in np.asarray(Cube.sum(axis=1)).ravel()) == {21}

# Concrete degree-6, m=3 constants for the LPS application.
D, counts, v, e2 = moments(6, 3)
assert D == 186
assert counts == {-3: 1, -2: 1, -1: 5, 0: 4, 1: 25, 2: 25, 3: 125}
assert v == Fraction(220, 93)
assert e2 == Fraction(634, 93)
tau2 = e2 / (v**3)
assert tau2 == Fraction(2741733, 5324000)
assert Fraction(6, D) == Fraction(1, 31)
assert 5**3 < D - 1

print('fixed_power_grid = PASS')
print('mcgee_girth =', graph_girth(G))
print('mcgee_cube_degree = 21')
print('mcgee_A2_A3_polynomial_identity = PASS')
print('d6_m3_degree =', D)
print('d6_m3_increment_counts =', counts)
print('d6_m3_speed =', f'{v.numerator}/{v.denominator}')
print('d6_m3_second_moment =', f'{e2.numerator}/{e2.denominator}')
print('d6_m3_profile_tau2 =', f'{tau2.numerator}/{tau2.denominator}')
print('d6_m3_gap_transfer_factor = 1/31')
print('d6_m3_branching_mismatch = 125 < 185')
print('P26_T08_FIXED_POWER_EXACT_PASS')
