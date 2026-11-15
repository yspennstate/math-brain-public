#!/usr/bin/env python3
"""Independent 3x3-cell exhaustive audit of the eight-corner rank classification."""
from collections import Counter, defaultdict
from fractions import Fraction as Q
from itertools import product
import json
from math import prod
import os
from pathlib import Path
import resource
import time


def edges_of_cells(cells):
    edges = set()
    for x, y in cells:
        square = ((x, y), (x + 1, y), (x + 1, y + 1), (x, y + 1))
        for v, w in zip(square, square[1:] + square[:1]):
            e = tuple(sorted((v, w)))
            if e in edges:
                edges.remove(e)
            else:
                edges.add(e)
    return edges


def simple_cycle(edges):
    neighbors = defaultdict(list)
    for a, b in edges:
        neighbors[a].append(b)
        neighbors[b].append(a)
    if not neighbors or any(len(v) != 2 for v in neighbors.values()):
        return None
    start = min(neighbors)
    cycle = [start]
    previous, current = start, neighbors[start][0]
    while current != start:
        cycle.append(current)
        following = next(w for w in neighbors[current] if w != previous)
        previous, current = current, following
    if len(cycle) != len(neighbors):
        return None
    return cycle


def corner_vertices(cycle):
    return [v for i, v in enumerate(cycle)
            if (v[0] - cycle[i - 1][0], v[1] - cycle[i - 1][1]) !=
            (cycle[(i + 1) % len(cycle)][0] - v[0],
             cycle[(i + 1) % len(cycle)][1] - v[1])]


def canonical(v):
    v = tuple(v)
    return min(w[i:] + w[:i] for w in (v, v[::-1]) for i in range(len(v)))


def enumerate_cells():
    found = {}
    grid = list(product(range(3), repeat=2))
    for mask in range(1, 1 << 9):
        cells = {v for i, v in enumerate(grid) if mask & (1 << i)}
        ox, oy = min(x for x, y in cells), min(y for x, y in cells)
        cells = {(x - ox, y - oy) for x, y in cells}
        cycle = simple_cycle(edges_of_cells(cells))
        if cycle is None:
            continue
        corners = corner_vertices(cycle)
        if len(corners) != 8:
            continue
        width, height = max(x for x, y in cycle), max(y for x, y in cycle)
        if {x for x, y in corners} != set(range(width + 1)):
            continue
        if {y for x, y in corners} != set(range(height + 1)):
            continue
        h = tuple(sum(v[1] == w[1] and min(v[0], w[0]) <= j < max(v[0], w[0])
                      for v, w in zip(cycle, cycle[1:] + cycle[:1])) // 2
                  for j in range(width))
        vert = tuple(sum(v[0] == w[0] and min(v[1], w[1]) <= j < max(v[1], w[1])
                         for v, w in zip(cycle, cycle[1:] + cycle[:1])) // 2
                     for j in range(height))
        rows = tuple(''.join('1' if (x, y) in cells else '0' for x in range(width))
                     for y in range(height))
        found[canonical(corners)] = {'rows_bottom_to_top': rows, 'h': h, 'v': vert,
                                    'width': width, 'height': height}
    return found


def coefficient_formula(m):
    from math import comb
    return (40 * comb(m + 1, 6) if m >= 5 else 0) + (92 * comb(m, 6) if m >= 6 else 0)


def audit_algebra(data):
    # Direct rational evaluation versus a closed formula, with exact tail bounds.
    checks = []
    cutoff = 500
    for p in (Q(1, 10), Q(1, 4), Q(1, 2), Q(3, 4), Q(1)):
        q, d = 1 - p, 2 - p
        r = q * q
        closed = p * q * q * (10 + 23 * q * q) / (64 * d ** 7)
        if q:
            geometric = Q(0)
            for shape in data.values():
                h, v = shape['h'], shape['v']
                term = Q(1)
                # Differentiate by total semiperimeter, rather than horizontal roots.
                for c in h + v:
                    term *= r ** c / (1 - r ** c)
                geometric += term * sum(Q(c, 1) / (1 - r ** c) for c in h + v)
            assert (p / 2) ** 8 * q ** (-8) * geometric == closed
        finite = sum(coefficient_formula(m) * (p / 2) ** 8 * q ** (2 * m - 8)
                     for m in range(5, cutoff + 1))
        first = coefficient_formula(cutoff + 1) * (p / 2) ** 8 * q ** (2 * cutoff - 6)
        # The larger of the two shifted-binomial successive ratios bounds their sum.
        ratio = r * Q(cutoff + 2, cutoff - 4)
        assert ratio < 1
        tail = first / (1 - ratio)
        assert 0 <= closed - finite <= tail < Q(1, 10 ** 30)
        baseline = p / (8 * d ** 3) + p * q * q / (4 * d ** 5)
        combined = p * (8 + 32 * q + 74 * q ** 2 + 64 * q ** 3 + 47 * q ** 4) / (64 * d ** 7)
        assert combined == baseline + closed
        checks.append({'p': str(p), 'R8': str(closed), 'B8': str(combined),
                       'tail_bound_exact': str(tail), 'cutoff': cutoff})
    # Coefficient from leading gap singularities, independent of the closed numerator.
    leading = sum(Q(6, 1) / (2 ** 8 * 2 ** 7 * prod(s['h'] + s['v']))
                  for s in data.values() if len(s['h'] + s['v']) == 6)
    assert leading == Q(33, 8192)
    assert leading + Q(3, 128) == Q(225, 8192)
    assert checks[2]['R8'] == '7/3888' and checks[2]['B8'] == '95/3888'
    return checks, leading


def main():
    resource.setrlimit(resource.RLIMIT_CPU, (180, 180))
    assert os.environ.get('OMP_NUM_THREADS') == '1'
    assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
    start = time.monotonic()
    found = enumerate_cells()
    prior = json.loads(Path('eight_data.json').read_text())['families']['8']
    assert set(found) == {tuple(map(tuple, s['corners'])) for s in prior['skeletons']}
    for length, count in prior['root_counts'].items():
        assert coefficient_formula(int(length) // 2) == count
    groups = Counter((s['width'], s['height'], tuple(sorted(s['h'] + s['v'])))
                     for s in found.values())
    assert len(found) == 38
    checks, leading = audit_algebra(found)
    print('PASS: all 511 nonempty subsets of a 3x3 cell box; identical 38 skeletons')
    for key, count in sorted(groups.items()):
        print(f'width,height,gaps={key}: count={count}')
        rows = sorted('/'.join(s['rows_bottom_to_top']) for s in found.values()
                      if (s['width'], s['height'], tuple(sorted(s['h'] + s['v']))) == key)
        print('cell_rows=' + ', '.join(rows))
    print('PASS: binomial formula agrees with every stored rooted-walk count')
    print('PASS: exact rational shape sums and binomial-series tails <1e-30 at five densities')
    for check in checks:
        print('p=' + check['p'] + ': R8=' + check['R8'] + ', B8=' + check['B8'])
    print('small-p: R8/p -> ' + str(leading) + '; B8/p -> 225/8192')
    result = {'groups': [{'width': w, 'height': h, 'gaps': g, 'count': c}
                         for (w, h, g), c in sorted(groups.items())],
              'shapes': [dict(s, corners=k) for k, s in sorted(found.items())],
              'checks': checks, 'R8_linear_coefficient': str(leading),
              'B8_linear_coefficient': '225/8192',
              'elapsed_seconds': round(time.monotonic() - start, 6),
              'peak_rss_bytes': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
              'priority': os.getpriority(os.PRIO_PROCESS, 0)}
    assert result['peak_rss_bytes'] < 1_000_000_000
    Path('cell_audit.json').write_text(json.dumps(result, indent=2) + '\n')
    print(f'priority={result["priority"]}; elapsed_seconds={result["elapsed_seconds"]}; '
          f'peak_rss_bytes={result["peak_rss_bytes"]}; output=cell_audit.json')


if __name__ == '__main__':
    main()
