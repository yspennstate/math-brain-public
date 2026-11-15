#!/usr/bin/env python3
"""Exact arithmetic audit of the four-vertex wired plaquette certificate."""
import os
import resource
import signal
import json
from fractions import Fraction as F
from itertools import permutations
from collections import Counter
from math import prod

assert os.environ.get('OMP_NUM_THREADS') == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
try:
    resource.setrlimit(resource.RLIMIT_AS, (768 * 1024**2, 768 * 1024**2))
    memory_guard = 'RLIMIT_AS'
except ValueError:
    try:
        resource.setrlimit(resource.RLIMIT_RSS, (768 * 1024**2, 768 * 1024**2))
        memory_guard = 'RLIMIT_RSS (Darwin may treat this as advisory)'
    except ValueError:
        memory_guard = 'setrlimit unavailable; measured RSS and bounded small state space'
signal.alarm(120)

P = [(0, 1), (1, 2), (2, 3)]
CYCLE = P + [(0, 3)]

def canonical(p):
    labels = {}
    return tuple(labels.setdefault(x, len(labels)) for x in p)

def merge(p, a, b):
    x, y = p[a], p[b]
    return canonical(tuple(x if v == y else v for v in p))

def crossing(p, m):
    return sum(p[a] != p[b] for a, b in CYCLE) + m * sum(p[v] != p[4] for v in range(4))

def kruskal_recursion(m):
    """Ignore rejected edges; the next crossing edge is uniform over crossing edges."""
    memo = {}
    def visit(p):
        if len(set(p)) == 1:
            return F(1)
        if p in memo:
            return memo[p]
        total = F(0)
        for a, b in P:
            if p[a] != p[b]:
                total += visit(merge(p, a, b))
        # A second spoke would preclude retaining all three path edges.
        if all(p[v] != p[4] for v in range(4)):
            for v in range(4):
                total += m * visit(merge(p, v, 4))
        answer = total / crossing(p, m)
        memo[p] = answer
        return answer
    return visit(tuple(range(5))), len(memo)

def tree_path(tree, a, b):
    stack = [(a, [])]
    seen = {a}
    while stack:
        v, route = stack.pop()
        if v == b:
            return route
        for i, (x, y) in enumerate(tree):
            w = y if x == v else x if y == v else None
            if w is not None and w not in seen:
                seen.add(w)
                stack.append((w, route + [i]))
    raise AssertionError('tree disconnected')

def cycle_integral(m):
    """Cycle criterion, then integrate monomials over 24 ordered simplices."""
    total = F(0)
    for r in range(4):
        tree = P + [(r, 4)]
        non_tree = [((0, 3), 1)] + [((v, 4), m - (v == r)) for v in range(4)]
        for order in permutations(range(4)):
            rank = {edge: i for i, edge in enumerate(order)}
            exponents = [0] * 4
            for (a, b), multiplicity in non_tree:
                largest = max(rank[i] for i in tree_path(tree, a, b))
                exponents[largest] += multiplicity
            # y_i=1-x_i: 1>y_0>...>y_3>0.
            value = F(m)
            for j in range(4):
                value /= sum(exponents[j:]) + 4 - j
            total += value
    return total

def grouped_formula():
    groups = Counter()
    for r in range(4):
        tree = P + [(r, 4)]
        for order in permutations(tree):
            p = tuple(range(5))
            factors = []
            for a, b in order:
                factors.append((sum(p[v] != p[4] for v in range(4)),
                                sum(p[x] != p[y] for x, y in CYCLE)))
                p = merge(p, a, b)
            groups[tuple(sorted(factors))] += 1
    return groups

def brute_force_m1():
    """All 8! raw edge orders; does not skip cycle edges probabilistically."""
    edges = CYCLE + [(v, 4) for v in range(4)]
    good = total = 0
    for order in permutations(range(8)):
        p = tuple(range(5))
        accepted = set()
        for i in order:
            a, b = edges[i]
            if p[a] != p[b]:
                accepted.add(i)
                p = merge(p, a, b)
        good += {0, 1, 2}.issubset(accepted)
        total += 1
    return good, total

rows = []
for d in range(2, 13):
    m = 2*d - 2
    a, states = kruskal_recursion(m)
    b = cycle_integral(m)
    assert a == b
    old_certificate = F(1, (8*d-4)*(8*d-5)*(8*d-6)//6)
    assert a > old_certificate
    bound = F(1, d) + 2*(d-1)*a
    assert 0 < bound < 1
    rows.append(dict(d=d, m=m, plaquette_probability=str(a),
                     connectivity_lower_bound=str(bound), decimal=float(bound),
                     recursion_states=states))

good, total = brute_force_m1()
assert F(good, total) == kruskal_recursion(1)[0] == cycle_integral(1)
groups = grouped_formula()
assert sum(groups.values()) == 96
for d in range(2, 13):
    m = 2*d - 2
    from_groups = sum((F(m * count, 1) / prod(a*m+b for a,b in factors)
                       for factors, count in groups.items()), F(0))
    assert from_groups == kruskal_recursion(m)[0]

# Check geometry by constructing actual lattice-edge sets, independently of m.
def edge(a, b):
    return tuple(sorted((a, b)))

geometry_checks = []
for d in range(2, 13):
    u = (0,) * d
    v = (1,) + (0,) * (d-1)
    paths = []
    incident_counts = []
    for j in range(1, d):
        for sign in [-1, 1]:
            a, b = list(u), list(v)
            a[j] = b[j] = sign
            a, b = tuple(a), tuple(b)
            vertices = {u, a, b, v}
            path = {edge(u,a), edge(a,b), edge(b,v)}
            incident = set()
            for w in vertices:
                for k in range(d):
                    for step in [-1, 1]:
                        z = list(w)
                        z[k] += step
                        incident.add(edge(w, tuple(z)))
            inside = {f for f in incident if f[0] in vertices and f[1] in vertices}
            assert len(inside) == 4
            assert len(incident - inside) == 8*d-8
            assert len(incident) == 8*d-4
            paths.append(path)
            incident_counts.append(len(incident))
    assert len(paths) == 2*(d-1)
    for i, path in enumerate(paths):
        for other in paths[i+1:]:
            assert not (path & other)
            degree = Counter(w for f in path | other for w in f)
            assert len(degree) == 6 and set(degree.values()) == {2}
    geometry_checks.append(dict(d=d, plaquettes=len(paths), incident_edges=incident_counts[0]))

asymptotic_coefficient = sum((F(count, prod(a for a,b in factors))
                              for factors,count in groups.items()), F(0))

peak_bytes = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
if __import__('sys').platform != 'darwin':
    peak_bytes *= 1024
assert peak_bytes < 1024**3
data = dict(nice=os.getpriority(os.PRIO_PROCESS, 0), peak_rss_bytes=peak_bytes, memory_guard=memory_guard,
            geometry_checks=geometry_checks, limit_m3_a_m=str(asymptotic_coefficient),
            rows=rows, brute_force_m1=dict(success=good, total=total, probability=str(F(good,total))),
            grouped_formula=[dict(multiplicity=n, factors=list(f)) for f,n in sorted(groups.items())])
with open('data.json', 'w') as out:
    json.dump(data, out, indent=2)
print('priority:', data['nice'], '; memory guard:', memory_guard, '; deadline: 120 s')
print('peak RSS bytes:', peak_bytes)
print('d  plaquette probability  nearest-neighbor connectivity lower bound')
for row in rows:
    print(row['d'], row['plaquette_probability'], row['connectivity_lower_bound'], format(row['decimal'], '.12f'))
print('Independent cycle-integral checks: 11/11 exact matches')
print('Raw permutation check m=1:', good, '/', total, '=', F(good,total))
print('Explicit lattice geometry checks: 11/11 passed')
print('Limit m^3 a_m:', asymptotic_coefficient)
print('Grouped formula terms:', len(groups), '; multiplicities sum:', sum(groups.values()))
for factors, count in sorted(groups.items()):
    print(count, '*m /', ' '.join('(%sm+%s)' % (a,b) for a,b in factors))
print('PASS; data written to data.json')
