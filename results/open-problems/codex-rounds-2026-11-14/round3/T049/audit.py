#!/usr/bin/env python3
"""Independent event recursion and arithmetic/overlap audit of saved results."""
from collections import Counter
from fractions import Fraction as Q
from functools import lru_cache
import json
from math import gcd, lcm
import os
from pathlib import Path
import resource
import signal
import sys

assert os.environ['OMP_NUM_THREADS'] == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
signal.alarm(120)
HERE = Path(__file__).resolve().parent


def event_probability(n, edges, spokes):
    """Directly recurse on allowed partitions, without fixing a final tree."""
    def join(p, a, b):
        x, y = p[a], p[b]
        raw = [x if z == y else z for z in p]
        names = {}
        return tuple(names.setdefault(z, len(names)) for z in raw)

    @lru_cache(None)
    def visit(p):
        # Once the entire path is accepted its eventual root edge is certain.
        if len(set(p[:n])) == 1:
            return Q(1)
        denominator = sum(p[a] != p[b] for a, b in edges)
        denominator += sum(spokes[v] for v in range(n) if p[v] != p[n])
        numerator = Q(0)
        for a in range(n-1):
            if p[a] != p[a+1]:
                numerator += visit(join(p, a, a+1))
        # A successful tree has exactly one root edge. An accepted second root
        # edge or any internal non-path edge makes success impossible.
        if all(p[v] != p[n] for v in range(n)):
            for v in range(n):
                numerator += spokes[v] * visit(join(p, v, n))
        return numerator / denominator
    return visit(tuple(range(n+1)))


def lattice_edge(a, b):
    return tuple(sorted((tuple(a), tuple(b))))


rows = json.loads((HERE/'extension.json').read_text())['rows']
for row in rows:
    d = row['d']
    path = [(i, i+1) for i in range(5)]
    for name, chord in [('C', []), ('A', [(1, 4)]), ('B', [(0, 3)])]:
        edges = path + [(0, 5)] + chord
        degree = Counter(v for edge in edges for v in edge)
        prob = event_probability(6, edges, [2*d-degree[v] for v in range(6)])
        assert prob == Q(row['probabilities'][name])
print('Direct event-partition recursion: 33/33 exact matches')

paths = json.loads((HERE/'paths_d3.json').read_text())
assert len(paths) == 44
edge_sets = []
for item in paths:
    vertices = item['vertices']
    edge_sets.append({lattice_edge(a, b) for a, b in zip(vertices, vertices[1:])})
u, v = (0, 0, 0), (1, 0, 0)
for axis in (1, 2):
    for sign in (-1, 1):
        a, b = list(u), list(v)
        a[axis] = b[axis] = sign
        edge_sets.append({lattice_edge(u, a), lattice_edge(a, b), lattice_edge(b, v)})
assert len({frozenset(s) for s in edge_sets}) == 48
overlap_pairs = 0
for i, first in enumerate(edge_sets):
    for second in edge_sets[:i]:
        union = first | second
        vertices = {v for edge in union for v in edge}
        # Their union is connected, and |E|>=|V| certifies a cycle.
        assert len(union) >= len(vertices)
        overlap_pairs += 1
assert overlap_pairs == 48*47//2
print('Explicit d=3 incompatible path pairs:', overlap_pairs)

# Re-derive the displayed d=3 result with integer common denominators,
# independently of the arithmetic that generated extension.json.
terms = [(8, 187806637, 902104087500),
         (12, 44663374963, 205507902600000),
         (24, 14856501533, 67257131760000)]
den = lcm(*(c for _, _, c in terms))
num = sum(a*b*(den//c) for a, b, c in terms)
divisor = gcd(num, den)
gain = (num//divisor, den//divisor)
assert gain == (8829469757, 922150845000)
oldnum, oldden = 120767, 329175
den2 = lcm(oldden, gain[1])
num2 = oldnum*(den2//oldden) + gain[0]*(den2//gain[1])
divisor = gcd(num2, den2)
answer = (num2//divisor, den2//divisor)
assert answer == (347146143557, 922150845000)
assert str(Q(*gain)) == rows[1]['improvement']
assert str(Q(*answer)) == rows[1]['bound']
assert abs(answer[0]/answer[1] - 0.376452665461) < 5e-13
print('Integer-LCM check: gain =', gain, '; bound =', answer)

# A particularly restrictive event gives a crude positive lower bound:
# all five desired edges are first among every edge meeting the six vertices.
for row in rows:
    d = row['d']
    for name, internal_count in [('C', 6), ('A', 7), ('B', 7)]:
        total_edges = 12*d-internal_count
        crude = Q(1, __import__('math').comb(total_edges, 5))
        assert Q(row['probabilities'][name]) > crude
    assert Q(row['previous_bound']) < Q(row['bound']) < 1
print('Crude sufficient-event and magnitude checks: 33/33 passed')
peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
if sys.platform != 'darwin':
    peak *= 1024
assert peak < 1024**3
print('PASS; peak RSS bytes:', peak, '; nice:', os.getpriority(os.PRIO_PROCESS, 0))
