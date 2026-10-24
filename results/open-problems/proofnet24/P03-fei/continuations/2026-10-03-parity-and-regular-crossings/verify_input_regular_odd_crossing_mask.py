#!/usr/bin/env python3
"""Exact new mask-averaging checks, including arbitrarily small/zero weights.

This tests the new input-regular argument separately from the unchanged
bounded-ratio checker. All algebraic tests use Fraction; square roots and
entropy supplements are labeled numerical. No other research helper is
imported.
"""
from collections import Counter
from fractions import Fraction as Q
from itertools import combinations
from math import log2, sqrt
from pathlib import Path
import json
import random

RNG = random.Random(2026100304)
COUNTS = Counter()
MAXIMA = Counter()
TOL = 5e-11


def dist(weights):
    out = Counter({Q(0): 1})
    for w in weights:
        nxt = Counter()
        for s, count in out.items():
            nxt[s - w] += count
            nxt[s + w] += count
        out = nxt
    return out


def fscore(t, cuts):
    return (-1) ** sum(t >= c for c in cuts)


def walsh(values):
    a = list(values)
    step = 1
    while step < len(a):
        for base in range(0, len(a), 2 * step):
            for j in range(base, base + step):
                u, v = a[j], a[j + step]
                a[j], a[j + step] = u + v, u - v
        step *= 2
    return a


def check_weights(weights):
    n = len(weights)
    sigma2 = sum(w * w for w in weights)
    if not sigma2:
        COUNTS['zero_score_cases'] += 1
        return
    wmax2 = max(w * w for w in weights)
    B2 = Q(n) * wmax2 / sigma2
    assert B2 >= 1
    for k in sorted({1, min(2, n), min(3, n)}):
        masks = list(combinations(range(n), k))
        first = Q(0)
        average_sqrt = 0.
        amax = Q(k) * B2 * sigma2 / n
        assert amax == k * wmax2
        for J in masks:
            selected = [weights[i] for i in J]
            a = sum(w * w for w in selected)
            first += a
            average_sqrt += sqrt(float(a))
            assert 0 <= a <= amax
            # Squaring sqrt(a)>=a/sqrt(amax) loses no sign and is exact.
            assert a * a <= amax * a
            sd = dist(selected)
            den = 1 << (2 * k)
            ea = Q(sum(cu * cv * abs(u - v)
                       for u, cu in sd.items() for v, cv in sd.items()), den)
            e2 = Q(sum(cu * cv * (u - v) ** 2
                       for u, cu in sd.items() for v, cv in sd.items()), den)
            e4 = Q(sum(cu * cv * (u - v) ** 4
                       for u, cu in sd.items() for v, cv in sd.items()), den)
            assert e2 == 2 * a
            assert e4 == 3 * (2 * a) ** 2 - 4 * sum(w ** 4 for w in selected)
            assert ea * ea * e4 >= e2 ** 3
            assert ea * ea >= Q(2, 3) * a
            COUNTS['exact_mask_bounds_and_difference_moments'] += 1
            if a == 0:
                COUNTS['zero_variance_masks'] += 1
        assert first / len(masks) == Q(k, n) * sigma2
        average_sqrt /= len(masks)
        target = sqrt(float(Q(k) * sigma2 / (B2 * n)))
        assert average_sqrt + TOL >= target
        COUNTS['exact_uniform_mask_first_moments'] += 1
        COUNTS['numeric_average_square_root_lower_bounds'] += 1
        MAXIMA['B'] = max(MAXIMA['B'], sqrt(float(B2)))
        MAXIMA['weight_ratio_when_positive'] = max(
            MAXIMA['weight_ratio_when_positive'],
            float(max(weights) / min(w for w in weights if w)))

    # Complete physical/Fourier checks are inexpensive in small dimension.
    if n <= 8:
        size = 1 << n
        cuts = (Q(-1, 1024), Q(0), Q(1, 1024))
        values = [fscore(sum(w if x >> i & 1 else -w
                             for i, w in enumerate(weights)), cuts)
                  for x in range(size)]
        pivotal = [sum(values[x] != values[x ^ (1 << i)] for x in range(size))
                   for i in range(n)]
        a = walsh(values)
        assert sum(v * v for v in a) == size * size
        assert sum(v * v * s.bit_count() for s, v in enumerate(a)) == size * sum(pivotal)
        entropy = -sum((v * v / size ** 2) * log2(v * v / size ** 2)
                       for v in a if v)
        assert entropy <= (log2(n) + 3) * sum(pivotal) / size + TOL
        J = tuple(range(min(3, n)))
        selected = dist([weights[i] for i in J])
        remain = dist([weights[i] for i in range(n) if i not in J])
        nb = 1 << len(J)
        nsnum = 0
        for r, cr in remain.items():
            plus = sum(cu for u, cu in selected.items() if fscore(r + u, cuts) == 1)
            nsnum += cr * 2 * plus * (nb - plus)
        ns = Q(nsnum, size * nb)
        assert ns <= Q(sum(pivotal[i] for i in J), 2 * size)
        COUNTS['exact_tiny_weight_truth_noise_and_energy'] += 1


def main():
    for n in range(1, 13):
        for pattern in range(12):
            values = (Q(0), Q(1, 1048576), Q(1, 1024), Q(1, 2), Q(1))
            weights = [RNG.choice(values) for _ in range(n)]
            if pattern % 3 == 0:
                # Comparable large coordinates alongside vanishing weights:
                # this retains a bounded normalized maximum despite an
                # arbitrarily large largest/smallest ratio.
                weights = [Q(1) if i % 2 == 0 else Q(1, 1048576) for i in range(n)]
            if pattern == 11:
                weights = [Q(0)] * n
            check_weights(weights)
            COUNTS['weight_families'] += 1
    report = {
        'status': 'PASS exact new mask argument; analytic proof separately supplied',
        'counts': dict(COUNTS), 'maxima': dict(MAXIMA),
        'exact': ['uniform K-mask first moment',
                  'pointwise aJ bound establishing lower square-root average',
                  'difference second/fourth moments and Holder interpolation',
                  'zero-variance masks interpreted without division',
                  'tiny-weight truth Walsh energy and resampling factor one half'],
        'numerical': ['average square-root lower bound', 'small-cube weak entropy'],
        'scope': 'No large-N0 enumeration or historical novelty certificate',
        'tolerance': TOL
    }
    Path(__file__).with_name('input_regular_odd_crossing_mask_checks.json').write_text(
        json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
