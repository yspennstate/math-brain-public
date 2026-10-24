"""Exact K_{2,3} counterexample to the archived series-parallel flow-cut claim.

No floating-point input is used. The optimal-flow value is justified in
agents/001.md by edge-transitive averaging of dual edge lengths.
"""
from fractions import Fraction as F
from itertools import combinations

A, B = (0, 1), (2, 3, 4)
V = A + B
edges = {(a, b) for a in A for b in B}
pi = {v: F(1, 4) if v in A else F(1, 6) for v in V}
c = F(1, 12)
distance = lambda x, y: 0 if x == y else 1 if ((x in A) != (y in A)) else 2
mean_distance = sum(pi[x] * pi[y] * distance(x, y) for x in V for y in V)
cut_values = []
for size in range(1, len(V)):
    for group in combinations(V, size):
        S = set(group)
        mass = sum(pi[v] for v in S)
        boundary = sum((x in S) != (y in S) for x, y in edges)
        cut_values.append((2 * mass * (1 - mass) / (c * boundary), group))
best_cut, witness = max(cut_values)
flow = 2 * mean_distance
print('mean_distance =', mean_distance)
print('optimal_flow =', flow)
print('best_cut =', best_cut, 'witness =', witness)
print('flow_cut_gap =', flow / best_cut)
print('diameter_ratio =', flow / 2)
assert mean_distance == F(13, 12)
assert flow == F(13, 6)
assert best_cut == F(35, 18)
assert flow / best_cut == F(39, 35)
