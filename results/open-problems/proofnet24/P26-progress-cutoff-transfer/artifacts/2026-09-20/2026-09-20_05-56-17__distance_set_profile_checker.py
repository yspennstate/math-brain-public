from fractions import Fraction
from collections import defaultdict, deque
import networkx as nx
import numpy as np


def jump_counts_for_j(d, j):
    q = d - 1
    c = defaultdict(int)
    c[j] += q**j
    for a in range(1, j):
        c[j - 2 * a] += (q - 1) * q ** (j - a - 1)
    c[-j] += 1
    assert sum(c.values()) == d * q ** (j - 1)
    return c


def distance_set_moments(d, J):
    q = d - 1
    D = 0
    counts = defaultdict(int)
    for j in J:
        Nj = d * q ** (j - 1)
        D += Nj
        for delta, c in jump_counts_for_j(d, j).items():
            counts[delta] += c
    v = sum(Fraction(delta * c, D) for delta, c in counts.items())
    e2 = sum(Fraction(delta * delta * c, D) for delta, c in counts.items())
    return D, dict(sorted(counts.items())), v, e2, e2 / (v**3)


def girth(G):
    best = 10**9
    for s in G:
        dist = {s: 0}
        par = {s: None}
        Q = deque([s])
        while Q:
            u = Q.popleft()
            for v in G[u]:
                if v not in dist:
                    dist[v] = dist[u] + 1
                    par[v] = u
                    Q.append(v)
                elif par[u] != v:
                    best = min(best, dist[u] + dist[v] + 1)
    return best


# All small fixed distance sets containing distance 1: positive speed,
# exact degree, and strict output-vs-base branching mismatch.
for d in range(3, 9):
    q = d - 1
    for m in range(2, 6):
        for mask in range(1 << (m - 1)):
            J = [1] + [j for j in range(2, m + 1) if mask & (1 << (j - 2))]
            if max(J) < 2:
                continue
            D, counts, v, e2, tau2 = distance_set_moments(d, J)
            assert D == sum(d * q ** (j - 1) for j in J)
            assert v > 0 and e2 > 0 and tau2 > 0
            M = max(J)
            assert q**M < D - 1

# McGee graph: girth 7 permits exact distance-set algebra through m=3.
G = nx.LCF_graph(24, [12, 7, -7], 8)
assert girth(G) == 7
nodes = list(G)
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
M13 = np.zeros((n, n), dtype=object)
for u in nodes:
    for v, r in dist[u].items():
        if r in (1, 3):
            M13[idx[u], idx[v]] = 1
assert np.array_equal(M13, A + A3)
assert set(int(x) for x in np.asarray(M13.sum(axis=1)).ravel()) == {15}

# Degree-six LPS application with J={1,3}.
D, counts, v, e2, tau2 = distance_set_moments(6, [1, 3])
assert D == 156
assert counts == {-3: 1, -1: 5, 1: 25, 3: 125}
assert v == Fraction(98, 39)
assert e2 == Fraction(97, 13)
assert tau2 == Fraction(442611, 941192)
assert Fraction(6, D) == Fraction(1, 26)
assert 5**3 < D - 1
assert Fraction(5**3, D - 1) == Fraction(25, 31)

print('distance_set_grid = PASS')
print('mcgee_girth = 7')
print('mcgee_distance_1_3_degree = 15')
print('mcgee_A1_plus_A3_identity = PASS')
print('d6_J13_degree = 156')
print('d6_J13_increment_counts =', counts)
print('d6_J13_speed =', f'{v.numerator}/{v.denominator}')
print('d6_J13_second_moment =', f'{e2.numerator}/{e2.denominator}')
print('d6_J13_profile_tau2 =', f'{tau2.numerator}/{tau2.denominator}')
print('d6_J13_gap_transfer_factor = 1/26')
print('d6_J13_branching_ratio = 25/31')
print('P26_T08_DISTANCE_SET_EXACT_PASS')
