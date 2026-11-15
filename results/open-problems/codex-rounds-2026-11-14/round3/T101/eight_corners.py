#!/usr/bin/env python3
"""Coordinate-rank enumeration and independent unit-walk audit; stdlib only."""
import argparse
from collections import Counter
from fractions import Fraction as Q
from itertools import product
import json
import os
from pathlib import Path
import resource
import time


def canonical(vertices):
    """Fix coordinates; quotient only by starting corner and traversal direction."""
    v = tuple(vertices)
    w = v[::-1]
    return min(seq[i:] + seq[:i] for seq in (v, w) for i in range(len(v)))


def boundary(corners):
    out = []
    for (x, y), (u, v) in zip(corners, corners[1:] + corners[:1]):
        assert (x == u) != (y == v)
        dx, dy = (u > x) - (u < x), (v > y) - (v < y)
        while (x, y) != (u, v):
            out.append((x, y))
            x, y = x + dx, y + dy
    return out


def rank_sequences(n, a):
    return [s for s in product(range(a), repeat=n)
            if len(set(s)) == a and all(s[i] != s[(i + 1) % n] for i in range(n))]


def skeletons(k):
    n = k // 2
    found = {}
    candidates = 0
    valid_representations = 0
    for a, b in product(range(2, n + 1), repeat=2):
        for xs, ys in product(rank_sequences(n, a), rank_sequences(n, b)):
            candidates += 1
            corners = tuple(v for i in range(n)
                            for v in ((xs[i], ys[i]), (xs[(i + 1) % n], ys[i])))
            unit = boundary(corners)
            if len(set(unit)) != len(unit):
                continue
            valid_representations += 1
            key = canonical(corners)
            h = tuple(sum(min(xs[i], xs[(i + 1) % n]) <= j <
                          max(xs[i], xs[(i + 1) % n]) for i in range(n))
                      for j in range(a - 1))
            v = tuple(sum(min(ys[i], ys[(i + 1) % n]) <= j <
                          max(ys[i], ys[(i + 1) % n]) for i in range(n))
                      for j in range(b - 1))
            assert all(c > 0 and c % 2 == 0 for c in h + v)
            found[key] = (tuple(c // 2 for c in h), tuple(c // 2 for c in v))
    assert valid_representations == k * len(found)
    return found, candidates, valid_representations


def finite_series(gaps, limit):
    """Coefficients of product r^c/(1-r^c), independently as integer DP."""
    coeff = [1] + [0] * limit
    for c in gaps:
        nxt = [0] * (limit + 1)
        for m, value in enumerate(coeff):
            for d in range(c, limit - m + 1, c):
                nxt[m + d] += value
        coeff = nxt
    return coeff


def root_coefficients(found, limit):
    unrooted = [0] * (limit + 1)
    for h, v in found.values():
        seq = finite_series(h + v, limit)
        unrooted = [x + y for x, y in zip(unrooted, seq)]
    # Interchanging coordinates pairs the horizontal and vertical root counts.
    return [m * unrooted[m] for m in range(limit + 1)]


def exact_root_gf(found, r):
    """Sum the horizontal-edge weights directly, without coordinate symmetry."""
    total = Q(0)
    for h, v in found.values():
        term = Q(1)
        for c in h + v:
            term *= r ** c / (1 - r ** c)
        # Weighted sum of 2*c*d over each horizontal gap d>=1.
        total += term * sum(2 * c / (1 - r ** c) for c in h)
    return total


def direct_walk_counts(max_length):
    """Rooted unit-step search, with no rank coordinates or shape formulas."""
    path = [(0, 0), (1, 0)]
    seen = set(path)
    counts = Counter()
    nodes = 0
    directions = ((1, 0), (0, 1), (-1, 0), (0, -1))

    def visit(last, internal_turns):
        nonlocal nodes
        nodes += 1
        x, y = path[-1]
        for d in directions:
            z = x + d[0], y + d[1]
            newturns = internal_turns + (d != last)
            if newturns > 8:
                continue
            if z == (0, 0):
                if len(path) >= 4:
                    k = newturns + (d != (1, 0))
                    if k <= 8:
                        counts[len(path), k] += 1
                continue
            if z in seen or len(path) + abs(z[0]) + abs(z[1]) > max_length:
                continue
            seen.add(z)
            path.append(z)
            visit(d, newturns)
            path.pop()
            seen.remove(z)

    visit((1, 0), 0)
    return counts, nodes


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--stage', choices=('earlier', 'eight'), default='eight')
    parser.add_argument('--max-length', type=int, default=16, choices=range(8, 21, 2))
    parser.add_argument('--output', default='eight_data.json')
    args = parser.parse_args()
    resource.setrlimit(resource.RLIMIT_CPU, (180, 180))
    start = time.monotonic()
    assert os.environ.get('OMP_NUM_THREADS') == '1'
    assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
    data = {'stage': args.stage, 'families': {}}
    for k in ((4, 6) if args.stage == 'earlier' else (4, 6, 8)):
        found, candidates, reps = skeletons(k)
        groups = Counter(tuple(sorted(h + v)) for h, v in found.values())
        rows = Counter((h, v) for h, v in found.values())
        coeff = root_coefficients(found, args.max_length // 2)
        checks = []
        for p in (Q(1, 10), Q(1, 4), Q(1, 2), Q(3, 4)):
            r = (1 - p) ** 2
            value = (p / 2) ** k * (1 - p) ** (-k) * exact_root_gf(found, r)
            if k == 4:
                assert value == p / (8 * (2 - p) ** 3)
            if k == 6:
                assert value == p * (1 - p) ** 2 / (4 * (2 - p) ** 5)
            checks.append({'p': str(p), 'probability': str(value)})
        entry = {'candidates': candidates, 'valid_representations': reps,
                 'skeleton_count': len(found),
                 'groups': [{'gaps': g, 'count': c} for g, c in sorted(groups.items())],
                 'axis_groups': [{'horizontal': h, 'vertical': v, 'count': c}
                                 for (h, v), c in sorted(rows.items())],
                 'root_counts': {str(2 * m): coeff[m]
                                 for m in range(2, len(coeff))},
                 'rational_checks': checks,
                 'skeletons': [{'corners': s, 'horizontal': h, 'vertical': v}
                               for s, (h, v) in sorted(found.items())]}
        data['families'][str(k)] = entry
        print(f'k={k}: candidates={candidates}, valid_representations={reps}, '
              f'skeletons={len(found)}, gap_groups={dict(groups)}', flush=True)
        print('root_counts=' + str(entry['root_counts']), flush=True)
        print('exact_probabilities=' + str(checks), flush=True)
    if args.stage == 'eight':
        walks, nodes = direct_walk_counts(args.max_length)
        for k in (4, 6, 8):
            for length, count in data['families'][str(k)]['root_counts'].items():
                assert walks[int(length), k] == count, (length, k, count, walks[int(length), k])
        data['walk_nodes'] = nodes
        print(f'PASS independent rooted walks through length {args.max_length}; nodes={nodes}', flush=True)
    data['priority'] = os.getpriority(os.PRIO_PROCESS, 0)
    data['elapsed_seconds'] = round(time.monotonic() - start, 6)
    data['peak_rss_bytes'] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert data['peak_rss_bytes'] < 1_000_000_000
    Path(args.output).write_text(json.dumps(data, indent=2) + '\n')
    print(f'priority={data["priority"]}; elapsed_seconds={data["elapsed_seconds"]}; '
          f'peak_rss_bytes={data["peak_rss_bytes"]}; output={args.output}')


if __name__ == '__main__':
    main()
