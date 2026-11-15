#!/usr/bin/env python3
"""Exact wired-path probabilities; standard library, bounded state spaces."""
import argparse
from collections import Counter
from fractions import Fraction
from itertools import permutations
import json
import os
from pathlib import Path
import resource
import signal
import sys
import time

assert os.environ.get('OMP_NUM_THREADS') == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
signal.alarm(180)
START = time.monotonic()
HERE = Path(__file__).resolve().parent


def components(n, edges):
    """Connected-component labels, calculated by graph traversal."""
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    labels = [-1] * n
    for v in range(n):
        if labels[v] >= 0:
            continue
        stack = [v]
        labels[v] = v
        while stack:
            u = stack.pop()
            for w in adj[u]:
                if labels[w] < 0:
                    labels[w] = v
                    stack.append(w)
    return labels


def subset_probability(n, internal, d):
    """Sum fixed-tree probabilities by DP over accepted tree-edge subsets."""
    degrees = Counter(v for e in internal for v in e)
    spokes = [2*d - degrees[v] for v in range(n)]
    assert min(spokes) > 0
    path = [(i, i+1) for i in range(n-1)]
    assert set(path).issubset(internal)
    answer = Fraction(0)
    for r in range(n):
        tree = path + [(r, n)]
        dp = [Fraction(0) for _ in range(1 << n)]
        dp[-1] = Fraction(1)
        for mask in range((1 << n)-2, -1, -1):
            labels = components(n+1, [tree[k] for k in range(n) if mask >> k & 1])
            crossing = sum(labels[a] != labels[b] for a, b in internal)
            crossing += sum(spokes[v] for v in range(n) if labels[v] != labels[n])
            dp[mask] = sum((dp[mask | (1 << k)] for k in range(n)
                            if not mask >> k & 1), Fraction(0)) / crossing
        answer += spokes[r] * dp[0]
    return answer


def route(tree, n, a, b):
    adj = [[] for _ in range(n+1)]
    for k, (x, y) in enumerate(tree):
        adj[x].append((y, k))
        adj[y].append((x, k))
    stack = [(a, -1, ())]
    while stack:
        v, parent, edges = stack.pop()
        if v == b:
            return edges
        stack.extend((w, v, edges+(k,)) for w, k in adj[v] if w != parent)
    raise AssertionError('disconnected tree')


def integral_terms(n, internal):
    """Group ordered-simplex integrals by their affine denominator factors.

    h[j] is an affine function a*d+b counting non-tree edges whose tree-path
    maximum has rank j. No component partitions or Kruskal transitions here.
    """
    path = [(i, i+1) for i in range(n-1)]
    degrees = Counter(v for edge in internal for v in edge)
    groups = Counter()
    for r in range(n):
        tree = path + [(r, n)]
        constraints = []
        for a, b in internal:
            if (a, b) not in path:
                constraints.append((route(tree, n, a, b), (0, 1)))
        for v in range(n):
            constraints.append((route(tree, n, v, n), (2, -degrees[v]-(v == r))))
        for order in permutations(range(n)):
            rank = [0] * n
            for j, edge in enumerate(order):
                rank[edge] = j
            h = [[0, 0] for _ in range(n)]
            for edges, (a, b) in constraints:
                j = max(rank[k] for k in edges)
                h[j][0] += a
                h[j][1] += b
            factors = []
            for j in range(n):
                factors.append((sum(x[0] for x in h[j:]),
                                n-j + sum(x[1] for x in h[j:])))
            groups[(degrees[r], tuple(sorted(factors)))] += 1
    assert sum(groups.values()) == n * __import__('math').factorial(n)
    return groups


def evaluate_integrals(groups, d):
    answer = Fraction(0)
    for (degree, factors), multiplicity in groups.items():
        value = Fraction(multiplicity * (2*d-degree))
        for a, b in factors:
            assert a*d+b > 0
            value /= a*d+b
        answer += value
    return answer


def usage():
    peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform != 'darwin':
        peak *= 1024
    assert peak < 1024**3
    return dict(nice=os.getpriority(os.PRIO_PROCESS, 0),
                peak_rss_bytes=peak, elapsed_seconds=time.monotonic()-START,
                deadline_seconds=180, OMP_NUM_THREADS=os.environ['OMP_NUM_THREADS'])


def recheck():
    earlier = json.loads(Path('~/codex_op_1114/briefs/T049/data.json').read_text())
    internal = [(0, 1), (1, 2), (2, 3), (0, 3)]
    terms = integral_terms(4, internal)
    rows = []
    for old in earlier['rows']:
        d = old['d']
        a = subset_probability(4, internal, d)
        b = evaluate_integrals(terms, d)
        assert a == b == Fraction(old['plaquette_probability'])
        bound = Fraction(1, d) + 2*(d-1)*a
        assert bound == Fraction(old['connectivity_lower_bound'])
        rows.append(dict(d=d, probability=str(a), bound=str(bound)))
        print('recheck', d, a, bound)
    result = dict(status='PASS', comparisons=len(rows), rows=rows, usage=usage())
    (HERE / 'recheck.json').write_text(json.dumps(result, indent=2)+'\n')
    print('PASS earlier result:', len(rows), 'dimensions; independent subset DP and cycle integrals')
    print(json.dumps(result['usage']))


def detours(d, length):
    origin = (0,) * d
    target = (1,) + (0,) * (d-1)
    path = [origin]
    visited = {origin}

    def walk():
        v = path[-1]
        remaining = length - len(path) + 1
        distance = sum(abs(a-b) for a, b in zip(v, target))
        if distance > remaining or (remaining-distance) % 2:
            return
        if remaining == 0:
            if v == target:
                yield tuple(path)
            return
        for axis in range(d):
            for sign in (-1, 1):
                w = list(v)
                w[axis] += sign
                w = tuple(w)
                if w in visited or (w == target and remaining != 1):
                    continue
                if {v, w} == {origin, target}:
                    continue
                path.append(w)
                visited.add(w)
                yield from walk()
                visited.remove(w)
                path.pop()
    yield from walk()


def induced_edges(path):
    return tuple((a, b) for a in range(len(path)) for b in range(a+1, len(path))
                 if sum(abs(x-y) for x, y in zip(path[a], path[b])) == 1)


def canonical_graph(internal, n):
    reverse = tuple(sorted((n-1-b, n-1-a) for a, b in internal))
    return min(tuple(sorted(internal)), reverse)


def lattice_audit(d):
    counts = Counter()
    stored = []
    for path in detours(d, 5):
        internal = induced_edges(path)
        signature = canonical_graph(internal, 6)
        counts[signature] += 1
        # Verify every spoke count using actual lattice neighbors, not degrees.
        for i, vertex in enumerate(path):
            outside = 0
            for axis in range(d):
                for step in (-1, 1):
                    w = list(vertex)
                    w[axis] += step
                    outside += tuple(w) not in path
            assert outside == 2*d - sum(i in e for e in internal)
        if d == 3:
            stored.append(dict(vertices=path, internal=internal))
    cycle = tuple([(i, i+1) for i in range(5)] + [(0, 5)])
    signatures = {'C': canonical_graph(cycle, 6),
                  'A': canonical_graph(cycle+((1, 4),), 6),
                  'B': canonical_graph(cycle+((0, 3),), 6)}
    # Second derivation: 2x1 rectangles and six-cycles of unit three-cubes.
    expected = {'C': 4*(d-1)*(d-2),
                'A': 2*(d-1)*(2*d-3),
                'B': 4*(d-1)*(2*d-3)}
    assert set(counts).issubset(signatures.values())
    assert all(counts[signatures[name]] == count for name, count in expected.items())
    assert sum(counts.values()) == (d-1)*(16*d-26)
    # Check the short-path count independently with the same exhaustive walk.
    assert sum(1 for _ in detours(d, 3)) == 2*(d-1)
    return expected, stored


def cube_audit():
    """Enumerate missing-vertex pairs of an abstract cube, independently of walks."""
    from itertools import product, combinations
    vertices = list(product((0, 1), repeat=3))
    cycles = Counter()
    marked_edges = Counter()
    for missing in combinations(range(8), 2):
        kept = [i for i in range(8) if i not in missing]
        edges = [(a, b) for a, b in combinations(kept, 2)
                 if sum(x != y for x, y in zip(vertices[a], vertices[b])) == 1]
        # Pick six edges: exactly the cycles, without any self-avoiding-walk code.
        for chosen in combinations(edges, 6):
            degree = Counter(v for edge in chosen for v in edge)
            if len(degree) != 6 or set(degree.values()) != {2}:
                continue
            labels = components(8, chosen)
            if len({labels[v] for v in kept}) != 1:
                continue
            full_degree = Counter(v for edge in edges for v in edge)
            kind = 'C' if len(edges) == 6 else 'chorded'
            cycles[kind] += 1
            for a, b in chosen:
                if (a, b) != (0, 4):  # distinguished cube edge, axis 0
                    continue
                key = 'C' if kind == 'C' else ('A' if full_degree[a] == full_degree[b] == 2 else 'B')
                marked_edges[key] += 1
    assert cycles == {'C': 4, 'chorded': 12}
    assert marked_edges == {'C': 2, 'A': 2, 'B': 4}
    return dict(cycles=cycles, fixed_edge_counts=marked_edges)


def extend():
    cycle = tuple([(i, i+1) for i in range(5)] + [(0, 5)])
    graphs = dict(C=cycle, A=cycle+((1, 4),), B=cycle+((0, 3),))
    square = [(0, 1), (1, 2), (2, 3), (0, 3)]
    terms = {name: integral_terms(6, graph) for name, graph in graphs.items()}
    cube = cube_audit()
    rows = []
    stored_paths = []
    for d in range(2, 13):
        counts, stored = lattice_audit(d)
        stored_paths += stored
        probs = {name: subset_probability(6, graph, d) for name, graph in graphs.items()}
        assert all(probs[name] == evaluate_integrals(terms[name], d) for name in graphs)
        a = subset_probability(4, square, d)
        old = Fraction(1, d) + 2*(d-1)*a
        gain = sum((counts[name]*probs[name] for name in graphs), Fraction(0))
        bound = old + gain
        assert 0 < old < bound < 1
        row = dict(d=d, counts=counts, probabilities={k: str(v) for k, v in probs.items()},
                   previous_bound=str(old), improvement=str(gain), bound=str(bound),
                   decimal=float(bound))
        rows.append(row)
        print('d', d, 'counts', counts)
        print(' probabilities', ' '.join(name+'='+str(probs[name]) for name in graphs))
        print(' gain', gain, 'bound', bound, format(float(bound), '.12f'), flush=True)
    result = dict(status='PASS', rows=rows, cube_audit=cube,
                  integral_group_counts={k: len(v) for k, v in terms.items()},
                  usage=usage())
    (HERE / 'extension.json').write_text(json.dumps(result, indent=2)+'\n')
    (HERE / 'paths_d3.json').write_text(json.dumps(stored_paths, indent=2)+'\n')
    (HERE / 'integral_terms.json').write_text(json.dumps({
        name: [dict(degree=degree, factors=factors, multiplicity=count)
               for (degree, factors), count in sorted(group.items())]
        for name, group in terms.items()}, indent=2)+'\n')
    print('PASS: all length-five detours, independent cube count, two exact probability methods')
    print('Integral group counts:', result['integral_group_counts'])
    print(json.dumps(result['usage']))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--recheck', action='store_true')
    parser.add_argument('--extend', action='store_true')
    args = parser.parse_args()
    if args.recheck:
        recheck()
    elif args.extend:
        extend()
    else:
        parser.error('select --recheck or --extend')
