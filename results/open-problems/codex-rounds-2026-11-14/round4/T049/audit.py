#!/usr/bin/env python3
"""Independent direction-multiset enumeration, cycle integrals, integer audit."""
from collections import Counter
from decimal import Decimal, localcontext
from fractions import Fraction
from itertools import permutations
import json
from math import comb, factorial, gcd, lcm
import os
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


def compositions(total, parts):
    if parts == 1:
        yield (total,)
    else:
        for first in range(total+1):
            for tail in compositions(total-first, parts-1):
                yield (first,)+tail


def multiset_orders(counts):
    """Generate every distinct permutation of a direction multiset."""
    order = []
    def visit():
        if len(order) == sum_original:
            yield tuple(order)
            return
        for direction in range(len(counts)):
            if counts[direction]:
                counts[direction] -= 1
                order.append(direction)
                yield from visit()
                order.pop()
                counts[direction] += 1
    sum_original = sum(counts)
    yield from visit()


def closed_multiset_paths(d, length):
    """No reachability recursion: form all zero-displacement step multisets.

    The final step, -e_1, is reserved. Reject repeated vertices only after
    constructing the entire remaining direction word.
    """
    half = (length+1)//2
    raw = accepted = 0
    paths = []
    for extra in compositions(half-1, d):
        positive = (extra[0]+1,)+extra[1:]
        counts = [x for a in positive for x in (a, a)]
        counts[1] -= 1  # reserve final step -e_1
        expected = factorial(length)
        for count in counts:
            expected //= factorial(count)
        seen_words = 0
        for word in multiset_orders(counts):
            seen_words += 1
            position = [0]*d
            path = [tuple(position)]
            for direction in word:
                position[direction//2] += 1 if direction % 2 == 0 else -1
                path.append(tuple(position))
            assert tuple(position) == (1,)+(0,)*(d-1)
            if len(set(path)) != length+1:
                continue
            assert not any(a == (0,)*d and b == path[-1]
                           for a, b in zip(path, path[1:]))
            paths.append(tuple(path))
            accepted += 1
        assert seen_words == expected
        raw += seen_words
    assert len(set(paths)) == len(paths)
    return paths, raw


def neighbor_signature(path):
    """Induced edges by neighbor lookup, independently of distance-pair scans."""
    where = {v: i for i, v in enumerate(path)}
    edges = set()
    outside_counts = []
    d = len(path[0])
    for i, vertex in enumerate(path):
        outside = 0
        for axis in range(d):
            for sign in (-1, 1):
                w = list(vertex)
                w[axis] += sign
                j = where.get(tuple(w))
                if j is None:
                    outside += 1
                else:
                    edges.add(tuple(sorted((i, j))))
        outside_counts.append(outside)
    degree = Counter(v for e in edges for v in e)
    assert all(outside_counts[v] == 2*d-degree[v] for v in range(len(path)))
    reverse = {(len(path)-1-b, len(path)-1-a) for a, b in edges}
    return min(tuple(sorted(edges)), tuple(sorted(reverse)))


def route_mask(tree, start, finish):
    adj = [[] for _ in range(9)]
    for bit, (a, b) in enumerate(tree):
        adj[a].append((b, bit))
        adj[b].append((a, bit))
    queue = [(start, -1, 0)]
    for v, parent, mask in queue:
        if v == finish:
            return mask
        queue.extend((w, v, mask | (1 << bit)) for w, bit in adj[v] if w != parent)
    raise AssertionError('no tree route')


def simplex_probability(edges, d):
    """Explicitly sum 8!*8 cycle-inequality simplex integrals, no contraction."""
    degree = Counter(v for e in edges for v in e)
    spokes = [2*d-degree[v] for v in range(8)]
    path = [(i, i+1) for i in range(7)]
    result = Fraction(0)
    simplex_count = 0
    group_count = 0
    for r in range(8):
        if spokes[r] == 0:
            continue
        tree = path+[(r, 8)]
        constraints = [(route_mask(tree, a, b), 1) for a, b in edges
                       if (a, b) not in path]
        constraints += [(route_mask(tree, v, 8), spokes[v]-(v == r))
                        for v in range(8)]
        # For a suffix S of the label order, a non-tree edge contributes
        # iff its tree path meets S: its largest path label then lies in S.
        denominator = [0]*256
        for mask in range(1, 256):
            denominator[mask] = mask.bit_count()+sum(m for route, m in constraints
                                                     if route & mask)
        products = Counter()
        for order in permutations(range(8)):
            mask = 255
            product = 1
            for bit in order:
                product *= denominator[mask]
                mask ^= 1 << bit
            products[product] += 1
            simplex_count += 1
        assert sum(products.values()) == factorial(8)
        group_count += len(products)
        result += sum((Fraction(spokes[r]*count, product)
                       for product, count in products.items()), Fraction(0))
    return result, simplex_count, group_count


def main():
    graphs = json.loads((HERE/'graphs.json').read_text())['graphs']
    saved = json.loads((HERE/'extension.json').read_text())
    assert saved['status'] == 'PASS'
    graph_by_edges = {tuple(tuple(e) for e in g['internal']): g for g in graphs}
    assert len(graph_by_edges) == 15
    geometry = []
    paths3 = None
    for d in (2, 3, 4, 5):
        paths, raw = closed_multiset_paths(d, 7)
        counts = Counter(neighbor_signature(p) for p in paths)
        expected = {edges: sum(comb(d-1, k)*g['support_counts'][k-1]
                               for k in (1, 2, 3) if k <= d-1)
                    for edges, g in graph_by_edges.items()}
        assert counts == Counter({e: n for e, n in expected.items() if n})
        support = Counter(sum(any(v[j] for v in p) for j in range(1, d)) for p in paths)
        assert all(support[k] == comb(d-1, k)*[28, 496, 1296][k-1]
                   for k in (1, 2, 3) if k <= d-1)
        geometry.append(dict(d=d, raw_direction_words=raw, simple_paths=len(paths),
                             types=len(counts), support_counts=dict(support)))
        print('multiset geometry d', d, 'raw', raw, 'simple', len(paths),
              'graph types', len(counts), 'PASS', flush=True)
        if d == 3:
            paths3 = paths

    # Explicit incompatibility audit, including different lengths and overlaps.
    paths = paths3+closed_multiset_paths(3, 3)[0]+closed_multiset_paths(3, 5)[0]
    assert len(paths) == 600
    vertex_ids, edge_ids = {}, {}
    masks = []
    for path in paths:
        vertices = edges = 0
        for v in path:
            vertices |= 1 << vertex_ids.setdefault(v, len(vertex_ids))
        for a, b in zip(path, path[1:]):
            edge = tuple(sorted((a, b)))
            edges |= 1 << edge_ids.setdefault(edge, len(edge_ids))
        masks.append((vertices, edges))
    assert len(set(masks)) == 600
    pair_count = 0
    for i, (va, ea) in enumerate(masks):
        for vb, eb in masks[:i]:
            assert (ea | eb).bit_count() >= (va | vb).bit_count()
            pair_count += 1
    assert pair_count == comb(600, 2) == 179700
    print('incompatible path-pair checks:', pair_count, 'PASS', flush=True)

    # Third probability method on every graph in d=3.
    row3 = next(row for row in saved['rows'] if row['d'] == 3)
    probabilities = {item['id']: item for item in row3['graphs']}
    integral_rows = []
    for graph in graphs:
        edges = [tuple(e) for e in graph['internal']]
        p, simplices, groups = simplex_probability(edges, 3)
        assert p == Fraction(probabilities[graph['id']]['probability'])
        integral_rows.append(dict(id=graph['id'], probability=str(p),
                                  simplices=simplices, denominator_products=groups))
        print('cycle integral', graph['id'], p, 'PASS', flush=True)

    # Rational addition using integers only, for all dimensions.
    decimals = []
    for row in saved['rows']:
        values = []
        for item in row['graphs']:
            a, b = map(int, item['probability'].split('/'))
            values.append((item['count']*a, b))
        denominator = lcm(*(b for a, b in values))
        numerator = sum(a*(denominator//b) for a, b in values)
        g = gcd(numerator, denominator)
        gain = (numerator//g, denominator//g)
        assert '%s/%s' % gain == row['gain']
        olda, oldb = map(int, row['previous_bound'].split('/'))
        denominator = lcm(oldb, gain[1])
        numerator = olda*(denominator//oldb)+gain[0]*(denominator//gain[1])
        g = gcd(numerator, denominator)
        bound = (numerator//g, denominator//g)
        assert '%s/%s' % bound == row['bound']
        with localcontext() as ctx:
            ctx.prec = 55
            bdec = str(Decimal(bound[0])/Decimal(bound[1]))
            gdec = str(Decimal(gain[0])/Decimal(gain[1]))
        decimals.append(dict(d=row['d'], gain=gdec, bound=bdec))
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform != 'darwin':
        rss *= 1024
    assert rss < 1024**3
    result = dict(status='PASS', geometry=geometry, incompatible_pairs=pair_count,
                  integral_rows=integral_rows, decimals=decimals,
                  usage=dict(peak_rss_bytes=rss, elapsed_seconds=time.monotonic()-START,
                             nice=os.getpriority(os.PRIO_PROCESS, 0),
                             OMP_NUM_THREADS='1', alarm_seconds=600))
    (HERE/'audit.json').write_text(json.dumps(result, indent=2)+'\n')
    print('PASS: independent geometry, all 15 cycle integrals, 11 integer sums')
    print(json.dumps(result['usage']))
    for row in decimals[:3]:
        print('decimal', json.dumps(row))


if __name__ == '__main__':
    main()
