#!/usr/bin/env python3
"""Exact audits for the four/six-turn simple-orbit calculation (stdlib only)."""
import argparse
from collections import Counter
from fractions import Fraction
from itertools import product
import json
from math import comb
import os
from pathlib import Path
import resource
import time


DIRECTIONS = ((1, 0), (0, 1), (-1, 0), (0, -1))
ROOT = ((0, 0), (1, 0))


def turns(vertices):
    steps = [(vertices[(i + 1) % len(vertices)][0] - v[0],
              vertices[(i + 1) % len(vertices)][1] - v[1])
             for i, v in enumerate(vertices)]
    return sum(steps[i - 1] != steps[i] for i in range(len(steps)))


def walk_counts(limit):
    """Walk from the fixed eastward edge; forbid every repeated vertex except closure.

    No rectangle/hexagon parametrization or formula enters this enumeration.
    The closing step returns to the origin; both root vertices contribute turns.
    """
    counts = Counter()
    path = list(ROOT)
    visited = set(path)
    nodes = 0

    def visit():
        nonlocal nodes
        nodes += 1
        x, y = path[-1]
        for dx, dy in DIRECTIONS:
            vertex = x + dx, y + dy
            if vertex == ROOT[0]:
                if len(path) >= 4:
                    counts[len(path), turns(path)] += 1
                continue
            # len(path) is the edge count after the proposed step; at least
            # Manhattan distance(vertex, origin) further edges must remain.
            if vertex in visited or len(path) + abs(vertex[0]) + abs(vertex[1]) > limit:
                continue
            path.append(vertex)
            visited.add(vertex)
            visit()
            visited.remove(vertex)
            path.pop()

    visit()
    for length in range(4, limit + 1, 2):
        m = length // 2
        assert counts[length, 4] == m * (m - 1)
        assert counts[length, 6] == (16 * comb(m, 4) if m >= 4 else 0)
    return counts, nodes


def unit_boundary(corners):
    vertices = []
    for i, (x, y) in enumerate(corners):
        target = corners[(i + 1) % len(corners)]
        dx = (target[0] > x) - (target[0] < x)
        dy = (target[1] > y) - (target[1] < y)
        while (x, y) != target:
            vertices.append((x, y))
            x, y = x + dx, y + dy
    assert len(set(vertices)) == len(vertices)
    return vertices


def bounded_shape_counts():
    """Generate rectangles/Ls geometrically, then translate every horizontal edge to root."""
    box = set(product(range(-1, 2), repeat=2))
    shapes = {}

    def add(corners):
        polygon = unit_boundary(corners)
        for i, v in enumerate(polygon):
            w = polygon[(i + 1) % len(polygon)]
            if v[1] != w[1]:
                continue
            offset = min(v[0], w[0]), v[1]
            shifted = [(x - offset[0], y - offset[1]) for x, y in polygon]
            if set(shifted) <= box:
                edges = frozenset(tuple(sorted((vtx, shifted[(j + 1) % len(shifted)])))
                                  for j, vtx in enumerate(shifted))
                shapes[edges] = (len(shifted), turns(shifted))

    for width, height in product(range(1, 3), repeat=2):
        add([(0, 0), (width, 0), (width, height), (0, height)])
    for a, b, c, d in product(range(1, 2), repeat=4):
        corners = [(0, 0), (a + b, 0), (a + b, c), (a, c),
                   (a, c + d), (0, c + d)]
        for sx, sy in product((-1, 1), repeat=2):
            add([(sx * x, sy * y) for x, y in corners])
    return Counter(shapes.values())


def environment_counts():
    """Exhaust all 3^9 environments; trace actual reflections, without polygon assumptions."""
    box = list(product(range(-1, 2), repeat=2))
    index = {v: i for i, v in enumerate(box)}
    # Values are outgoing direction vectors for empty, slash, backslash.
    reflection = (
        {(1, 0): (1, 0), (-1, 0): (-1, 0), (0, 1): (0, 1), (0, -1): (0, -1)},
        {(1, 0): (0, 1), (-1, 0): (0, -1), (0, 1): (1, 0), (0, -1): (-1, 0)},
        {(1, 0): (0, -1), (-1, 0): (0, 1), (0, 1): (-1, 0), (0, -1): (1, 0)},
    )
    weighted = {p: Fraction(0) for p in (Fraction(1, 4), Fraction(1, 2), Fraction(3, 4))}
    outcomes = Counter()
    raw_success = 0
    for config in product(range(3), repeat=9):
        position, direction = ROOT[1], (1, 0)
        visited = set()
        mirror_count = 0
        length = 0
        while True:
            if position not in index or position in visited:
                outcomes['exit_or_nonsimple'] += 1
                break
            visited.add(position)
            local = config[index[position]]
            mirror_count += local != 0
            direction = reflection[local][direction]
            length += 1
            nxt = position[0] + direction[0], position[1] + direction[1]
            if (position, nxt) == ROOT:
                if mirror_count <= 6:
                    raw_success += 1
                    outcomes[f'simple_{mirror_count}_mirrors_length_{length}'] += 1
                    occupied = sum(state != 0 for state in config)
                    for p in weighted:
                        weighted[p] += (p / 2) ** occupied * (1 - p) ** (9 - occupied)
                else:
                    outcomes['simple_more_than_6'] += 1
                break
            position = nxt

    shapes = bounded_shape_counts()
    for p, value in weighted.items():
        geometric = sum(number * (p / 2) ** k * (1 - p) ** (length - k)
                        for (length, k), number in shapes.items())
        assert value == geometric
    assert sum(outcomes.values()) == 3 ** 9
    return {
        'environments': 3 ** 9,
        'raw_successes': raw_success,
        'outcomes': dict(sorted(outcomes.items())),
        'bounded_shapes': [{'length': length, 'mirrors': k, 'count': n}
                           for (length, k), n in sorted(shapes.items())],
        'weighted_probabilities': {str(p): str(v) for p, v in weighted.items()},
    }


def independent_series_checks():
    """Check the rational sums by exact finite sums and rigorous tail estimates."""
    result = []
    cutoff = 400
    for p in (Fraction(1, 10), Fraction(1, 4), Fraction(1, 2), Fraction(3, 4), Fraction(1)):
        q = 1 - p
        r = q * q
        rect = p / (8 * (2 - p) ** 3)
        hexa = p * q * q / (4 * (2 - p) ** 5)
        # Group by semiperimeter, independently of the side-length factorization.
        finite4 = sum(Fraction(m * (m - 1)) * (p / 2) ** 4 * q ** (2 * m - 4)
                      for m in range(2, cutoff + 1))
        finite6 = sum(Fraction(16 * comb(m, 4)) * (p / 2) ** 6 * q ** (2 * m - 6)
                      for m in range(4, cutoff + 1))
        # Each positive tail term after cutoff is bounded by its first term times
        # 1/(1-ratio): consecutive polynomial coefficients have decreasing ratios.
        first4 = Fraction((cutoff + 1) * cutoff) * (p / 2) ** 4 * q ** (2 * cutoff - 2)
        first6 = Fraction(16 * comb(cutoff + 1, 4)) * (p / 2) ** 6 * q ** (2 * cutoff - 4)
        ratio4 = r * Fraction(cutoff + 2, cutoff)
        ratio6 = r * Fraction(cutoff + 2, cutoff - 2)
        assert ratio4 < 1 and ratio6 < 1
        error4 = first4 / (1 - ratio4)
        error6 = first6 / (1 - ratio6)
        assert 0 <= rect - finite4 <= error4
        assert 0 <= hexa - finite6 <= error6
        assert error4 + error6 < Fraction(1, 10 ** 25)
        combined = p * (6 - 8 * p + 3 * p * p) / (8 * (2 - p) ** 5)
        assert combined == rect + hexa
        result.append({'p': str(p), 'rectangles': str(rect), 'hexagons': str(hexa),
                       'sum': str(combined), 'sum_decimal': float(combined),
                       'finite_sum_cutoff': cutoff,
                       'tail_upper_bound_exact': str(error4 + error6),
                       'tail_upper_bound_decimal': float(error4 + error6)})
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--max-length', type=int, default=14, choices=range(8, 17, 2))
    parser.add_argument('--output', default='audit_data.json')
    args = parser.parse_args()
    start = time.monotonic()
    resource.setrlimit(resource.RLIMIT_CPU, (180, 180))
    counts, nodes = walk_counts(args.max_length)
    coefficient = Fraction(6, 8 * 2 ** 5)
    assert coefficient == Fraction(1, 8 * 2 ** 3) + Fraction(1, 4 * 2 ** 5)
    data = {
        'max_length': args.max_length,
        'walk_nodes': nodes,
        'walk_counts': [{'length': length, 'turns': k, 'count': n}
                        for (length, k), n in sorted(counts.items())],
        'environment_check': environment_counts(),
        'series_checks': independent_series_checks(),
        'small_p_linear_coefficient': str(coefficient),
        'process_priority': os.getpriority(os.PRIO_PROCESS, 0),
        'omp_num_threads': os.environ.get('OMP_NUM_THREADS'),
        'elapsed_seconds': round(time.monotonic() - start, 6),
        'max_rss_bytes': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
    }
    assert data['process_priority'] >= 15
    assert data['omp_num_threads'] == '1'
    # macOS reports ru_maxrss in bytes.
    assert data['max_rss_bytes'] < 1_000_000_000
    Path(args.output).write_text(json.dumps(data, indent=2) + '\n')
    print('PASS: rooted self-avoiding polygons through length', args.max_length)
    for length in range(4, args.max_length + 1, 2):
        print(f'length={length}: four_turns={counts[length, 4]}, six_turns={counts[length, 6]}')
    env = data['environment_check']
    print(f'PASS: all {env["environments"]} three-by-three environments; {env["raw_successes"]} successes')
    print('PASS: five exact rational series checks, including p=1; tails < 1e-25')
    print('small-p coefficient:', coefficient)
    print(f'priority={data["process_priority"]}; OMP_NUM_THREADS=1; peak_RSS_bytes={data["max_rss_bytes"]}')
    print('elapsed_seconds=' + str(data['elapsed_seconds']))
    print('data=' + args.output)


if __name__ == '__main__':
    main()
