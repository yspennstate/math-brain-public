#!/usr/bin/env python3
"""Exact site-animal counts and spanning-tree multiplicities; standard library only.

Translation classes only: rotations and reflections remain distinct.
Two independent animal generators and two spanning-tree counters are compared.
"""
import argparse
import csv
import hashlib
import itertools
import json
import os
from pathlib import Path
import resource
import signal
import time


def neighbours(v):
    for axis in range(len(v)):
        for step in (-1, 1):
            yield v[:axis] + (v[axis] + step,) + v[axis + 1:]


def canonical(vertices):
    anchor = min(vertices)
    return tuple(sorted(tuple(x - y for x, y in zip(v, anchor)) for v in vertices))


def grow_levels(d, maximum):
    """Add every boundary vertex, then deduplicate translations."""
    levels = {1: {(tuple([0] * d),)}}
    for n in range(2, maximum + 1):
        shapes = set()
        for shape in levels[n - 1]:
            occupied = set(shape)
            boundary = {v for u in shape for v in neighbours(u)} - occupied
            for v in boundary:
                shapes.add(canonical(shape + (v,)))
        levels[n] = shapes
    return levels


def exclusion_levels(d, maximum):
    """Lexicographic-root recursion with exclusions; no translation deduplication."""
    origin = tuple([0] * d)
    # Construct adjacency independently of the coordinate-slicing growth helper.
    offsets = [v for v in itertools.product((-1, 0, 1), repeat=d)
               if sum(abs(x) for x in v) == 1]

    def adjacent(v):
        return [tuple(a + b for a, b in zip(v, offset)) for offset in offsets]

    levels = {n: set() for n in range(1, maximum + 1)}
    calls = {n: 0 for n in levels}

    def visit(occupied, frontier, excluded):
        n = len(occupied)
        calls[n] += 1
        shape = tuple(sorted(occupied))
        assert shape not in levels[n], ('duplicate exclusion output', d, shape)
        levels[n].add(shape)
        if n == maximum:
            return
        remaining = set(frontier)
        blocked = set(excluded)
        while remaining:
            v = min(remaining)
            remaining.remove(v)
            enlarged = occupied | {v}
            fresh = {w for w in adjacent(v)
                     if w > origin and w not in enlarged and w not in blocked}
            visit(enlarged, remaining | fresh, blocked)
            blocked.add(v)

    visit({origin}, {v for v in adjacent(origin) if v > origin}, set())
    assert all(calls[n] == len(levels[n]) for n in levels)
    return levels


def edges_of(shape):
    """All-pairs Manhattan-distance check, independent of growth neighbours."""
    return [(i, j) for i in range(len(shape)) for j in range(i + 1, len(shape))
            if sum(abs(a - b) for a, b in zip(shape[i], shape[j])) == 1]


def bareiss(matrix):
    """Fraction-free elimination. Laplacian cofactors here are positive definite."""
    a = [row[:] for row in matrix]
    if not a:
        return 1
    previous = 1
    for k in range(len(a) - 1):
        pivot = a[k][k]
        assert pivot > 0
        for i in range(k + 1, len(a)):
            for j in range(k + 1, len(a)):
                numerator = a[i][j] * pivot - a[i][k] * a[k][j]
                assert numerator % previous == 0
                a[i][j] = numerator // previous
            a[i][k] = 0
        previous = pivot
    return a[-1][-1]


def tree_count_determinant(n, edges):
    laplacian = [[0] * n for _ in range(n)]
    for i, j in edges:
        laplacian[i][i] += 1
        laplacian[j][j] += 1
        laplacian[i][j] -= 1
        laplacian[j][i] -= 1
    return bareiss([row[:-1] for row in laplacian[:-1]])


def tree_count_subsets(n, edges):
    """Enumerate every (n-1)-edge subset and reject cycles by disjoint sets."""
    total = 0
    for chosen in itertools.combinations(edges, n - 1):
        parent = list(range(n))

        def root(v):
            while parent[v] != v:
                v = parent[v]
            return v

        for i, j in chosen:
            a, b = root(i), root(j)
            if a == b:
                break
            parent[a] = b
        else:
            # An acyclic graph with n vertices and n-1 edges is connected.
            total += 1
    return total


def check_small_hand_cases():
    assert tree_count_determinant(1, []) == tree_count_subsets(1, []) == 1
    for length in (4, 6, 8):
        cycle = [(i, (i + 1) % length) for i in range(length)]
        assert tree_count_determinant(length, cycle) == length
        assert tree_count_subsets(length, cycle) == length
    rectangle = [(x, y) for x in range(3) for y in range(2)]
    assert tree_count_determinant(6, edges_of(rectangle)) == 15
    assert tree_count_subsets(6, edges_of(rectangle)) == 15


def run(d, maximum, output):
    start = time.monotonic()
    growth = grow_levels(d, maximum)
    exclusion = exclusion_levels(d, maximum)
    for n in growth:
        assert growth[n] == exclusion[n], ('generator disagreement', d, n)
    del exclusion
    first_collision = None
    summaries = []
    hist_rows = []
    certificate = output / f'shapes_d{d}.jsonl'
    with certificate.open('w') as f:
        for n, shapes in sorted(growth.items()):
            histogram = {}
            examples = {}
            total_trees = 0
            for shape in sorted(shapes):
                edges = edges_of(shape)
                k = len(edges) - n + 1
                tau = tree_count_determinant(n, edges)
                check = tree_count_subsets(n, edges)
                assert tau == check and tau >= 1, (d, shape, tau, check)
                histogram[k, tau] = histogram.get((k, tau), 0) + 1
                examples.setdefault(k, {}).setdefault(tau, shape)
                total_trees += tau
                f.write(json.dumps({'n': n, 'vertices': shape, 'edges': len(edges),
                                    'excess': k, 'tau': tau}, separators=(',', ':')) + '\n')
            for (k, tau), count in sorted(histogram.items()):
                hist_rows.append([d, n, k, tau, count])
            if first_collision is None:
                for k, choices in sorted(examples.items()):
                    if len(choices) > 1:
                        first_collision = {'d': d, 'n': n, 'excess': k,
                                           'examples': [{'tau': tau, 'vertices': shape}
                                                        for tau, shape in sorted(choices.items())]}
                        break
            induced_trees = histogram.get((0, 1), 0)
            summary = {'d': d, 'n': n, 'site_animals': len(shapes),
                       'bond_trees': total_trees, 'induced_trees': induced_trees,
                       'max_tau': max(tau for k, tau in histogram)}
            summaries.append(summary)
            print('COUNT', json.dumps(summary, sort_keys=True), flush=True)
    with (output / f'histogram_d{d}.csv').open('w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['dimension', 'vertices', 'excess', 'spanning_trees', 'site_animals'])
        writer.writerows(hist_rows)
    digest = hashlib.sha256(certificate.read_bytes()).hexdigest()
    print('FIRST_COLLISION', json.dumps(first_collision, sort_keys=True), flush=True)
    print('AUDIT', json.dumps({'d': d, 'shapes_checked_by_both_methods':
                              sum(len(s) for s in growth.values()),
                              'sha256': digest, 'seconds': round(time.monotonic() - start, 3)}), flush=True)
    return {'dimension': d, 'maximum_n': maximum, 'counts': summaries,
            'first_collision': first_collision, 'shape_file_sha256': digest}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--d2', type=int, default=8)
    parser.add_argument('--d3', type=int, default=7)
    parser.add_argument('--output', type=Path, default=Path('data'))
    args = parser.parse_args()
    # Fail closed for ranges outside this modest, reviewed computation.
    if not (1 <= args.d2 <= 8 and 1 <= args.d3 <= 7):
        parser.error('supported ranges are d2 <= 8 and d3 <= 7')
    resource.setrlimit(resource.RLIMIT_CPU, (1100, 1100))
    signal.alarm(1190)
    print('RUNTIME', json.dumps({'nice': os.getpriority(os.PRIO_PROCESS, 0),
                                 'OMP_NUM_THREADS': os.environ.get('OMP_NUM_THREADS')}), flush=True)
    check_small_hand_cases()
    args.output.mkdir(exist_ok=True)
    results = [run(2, args.d2, args.output), run(3, args.d3, args.output)]
    (args.output / 'summary.json').write_text(json.dumps(results, indent=2) + '\n')
    # macOS reports ru_maxrss in bytes. Linux reports kilobytes.
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    print('PEAK_RSS_RAW', rss, flush=True)
    print('ALL_ASSERTIONS_PASSED', flush=True)


if __name__ == '__main__':
    main()
