"""Independent cycle-integral and lattice-geometry recheck of rounds 1,3,4."""
import json
import os
from collections import Counter
from fractions import Fraction as Q
from functools import lru_cache
from math import comb
from pathlib import Path
import resource
import signal
import sys
import time

assert os.environ.get('OMP_NUM_THREADS') == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
signal.alarm(600)
START = time.monotonic()
HERE = Path(__file__).resolve().parent
BASE = Path('~')
R1 = BASE/'codex_op_1114/briefs/T049'
R3 = BASE/'codex_op_1114r3/briefs/T049'
R4 = BASE/'codex_op_1114r4/briefs/T049'


def route_bits(tree, n, start, end):
    adjacency = [[] for _ in range(n+1)]
    for i, (u, v) in enumerate(tree):
        adjacency[u].append((v, i))
        adjacency[v].append((u, i))
    queue = [(start, -1, 0)]
    for u, parent, bits in queue:
        if u == end:
            return bits
        queue.extend((v, u, bits | (1 << i)) for v, i in adjacency[u] if v != parent)
    raise AssertionError('disconnected tree')


def integral(n, internal, d):
    """Sum ordered-simplex monomials by deleting one suffix edge at a time."""
    path = [(i, i+1) for i in range(n-1)]
    degree = Counter(x for edge in internal for x in edge)
    spokes = [2*d-degree[i] for i in range(n)]
    assert min(spokes) >= 0
    answer = Q(0)
    for r, multiplicity in enumerate(spokes):
        if not multiplicity:
            continue
        tree = path + [(r, n)]
        constraints = [(route_bits(tree, n, a, b), 1) for a, b in internal
                       if (a, b) not in path]
        constraints += [(route_bits(tree, n, v, n), spokes[v]-(v == r))
                        for v in range(n)]
        values = [Q(1)] + [Q(0)]*((1 << n)-1)
        for suffix in range(1, 1 << n):
            denominator = suffix.bit_count() + sum(k for route, k in constraints
                                                      if route & suffix)
            values[suffix] = sum((values[suffix ^ (1 << i)] for i in range(n)
                                 if suffix >> i & 1), Q(0))/denominator
        answer += multiplicity*values[-1]
    return answer


def signature(path):
    location = {x: i for i, x in enumerate(path)}
    edges = set()
    for x, i in location.items():
        for a in range(len(x)):
            y = list(x)
            y[a] += 1
            if tuple(y) in location:
                edges.add(tuple(sorted((i, location[tuple(y)]))))
    reverse = {(len(path)-1-v, len(path)-1-u) for u, v in edges}
    return min(tuple(sorted(edges)), tuple(sorted(reverse)))


def path_counts(d):
    """Nonbacktracking coordinate walks; early arrivals at the endpoint are rejected."""
    zero, end = (0,)*d, (1,)+(0,)*(d-1)
    counts = Counter()
    def extend(path):
        remaining = 8-len(path)
        if sum(abs(x-y) for x, y in zip(path[-1], end)) > remaining:
            return
        if not remaining:
            if path[-1] == end:
                counts[signature(path)] += 1
            return
        for a in range(d):
            for step in (-1, 1):
                y = list(path[-1])
                y[a] += step
                y = tuple(y)
                if y in path or (y == end and remaining != 1):
                    continue
                extend(path+(y,))
    extend((zero,))
    return counts


def main():
    square = [(0, 1), (1, 2), (2, 3), (0, 3)]
    square_probs = {}
    for row in json.loads((R1/'data.json').read_text())['rows']:
        d = row['d']
        square_probs[d] = p = integral(4, square, d)
        assert p == Q(row['plaquette_probability'])
        assert Q(1, d)+2*(d-1)*p == Q(row['connectivity_lower_bound'])
    six_probs = {}
    for row in json.loads((R3/'extension.json').read_text())['rows']:
        d = row['d']
        cycle = [(i, i+1) for i in range(5)] + [(0, 5)]
        result = {}
        for name, extra in [('C', []), ('A', [(1, 4)]), ('B', [(0, 3)])]:
            p = integral(6, cycle+extra, d)
            assert p == Q(row['probabilities'][name])
            result[name] = p
        bound = Q(1, d)+2*(d-1)*square_probs[d]
        bound += 4*(d-1)*(d-2)*result['C']
        bound += 2*(d-1)*(2*d-3)*result['A']
        bound += 4*(d-1)*(2*d-3)*result['B']
        assert bound == Q(row['bound'])
        six_probs[d] = bound
    graphs = json.loads((R4/'graphs.json').read_text())['graphs']
    old = json.loads((R4/'extension.json').read_text())['rows']
    matched = 0
    for row in old:
        d = row['d']
        gain = Q(0)
        for item in row['graphs']:
            g = next(g for g in graphs if g['id'] == item['id'])
            p = integral(8, [tuple(e) for e in g['internal']], d)
            assert p == Q(item['probability'])
            count = sum(comb(d-1, k)*c for k, c in enumerate(g['support_counts'], 1)
                        if k <= d-1)
            assert count == item['count']
            gain += count*p
            matched += 1
        assert gain == Q(row['gain'])
        assert six_probs[d]+gain == Q(row['bound'])
        print('probabilities and B7 d', d, 'PASS', flush=True)
    geometry = []
    for d in range(2, 6):
        found = path_counts(d)
        expected = Counter()
        for g in graphs:
            count = sum(comb(d-1, k)*c for k, c in enumerate(g['support_counts'], 1)
                        if k <= d-1)
            if count:
                expected[tuple(tuple(e) for e in g['internal'])] = count
        assert found == expected
        geometry.append(dict(d=d, paths=sum(found.values()), types=len(found)))
        print('coordinate geometry d', d, 'paths', sum(found.values()), 'PASS', flush=True)
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform != 'darwin':
        rss *= 1024
    assert rss < 1024**3
    result = dict(status='PASS', square_comparisons=11, six_vertex_comparisons=33,
                  eight_vertex_comparisons=matched, geometry=geometry,
                  usage=dict(elapsed_seconds=time.monotonic()-START, peak_rss_bytes=rss,
                             nice=os.getpriority(os.PRIO_PROCESS, 0), threads=1))
    (HERE/'recheck.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result))


if __name__ == '__main__':
    main()
