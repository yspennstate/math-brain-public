#!/usr/bin/env python3
"""Exact lemma checks for the restricted odd-crossing FEI derivation.

The analytic large-dimension constants are not tested by enumerating a cube
at N0: N0 is deliberately huge. This checker tests the actual constituent
identities on rational endpoint examples, including atoms, and numerical
entropy/CDF comparisons on finite cubes. It imports no author helper.
"""
from collections import Counter
from fractions import Fraction as Q
from itertools import product
from math import erf, exp, log, log2, pi, sqrt
from pathlib import Path
import json
import random

RNG = random.Random(2026100303)
COUNTS = Counter()
MAXIMA = Counter()
TOL = 5e-11


def phi(t):
    return (1 + erf(t / sqrt(2))) / 2


def label(t, cuts, endpoint_right):
    above = sum(t > c for c in cuts)
    for j, c in enumerate(cuts):
        if t == c:
            return (-1) ** (j + int(endpoint_right[j]))
    return (-1) ** above


def score_distribution(weights):
    out = Counter({0: 1})
    for w in weights:
        nxt = Counter()
        for s, count in out.items():
            nxt[s - w] += count
            nxt[s + w] += count
        out = nxt
    return out


def open_pivotal_intervals(cuts, ties, u, v):
    endpoints = sorted({c - u for c in cuts} | {c - v for c in cuts})
    out = []
    signed_integral = Q(0)
    for a, b in zip(endpoints, endpoints[1:]):
        mid = (a + b) / 2
        fu, fv = label(mid + u, cuts, ties), label(mid + v, cuts, ties)
        signed_integral += (b - a) * (fv - fu)
        if fu != fv:
            out.append((a, b))
    tail_jump = (-1) ** len(cuts) - 1
    assert signed_integral == (v - u) * tail_jump
    measure = sum((b - a for a, b in out), Q(0))
    assert measure >= abs(u - v)
    assert len(out) <= 2 * len(cuts)
    COUNTS['exact_signed_translation'] += 1
    COUNTS['exact_open_measure_lower_bound'] += 1
    for c in endpoints:
        left = sum(a < c < b for a, b in out)
        assert left == 0
        COUNTS['excluded_translated_endpoints'] += 1
    return out


def walsh(values):
    coeff = list(values)
    stride = 1
    while stride < len(coeff):
        for base in range(0, len(coeff), stride * 2):
            for j in range(base, base + stride):
                a, b = coeff[j], coeff[j + stride]
                coeff[j], coeff[j + stride] = a + b, a - b
        stride *= 2
    return coeff


def check_function(weights, cuts, ties):
    n, m = len(weights), len(cuts)
    assert m % 2 == 1
    size = 1 << n
    values = [label(sum(w if x >> i & 1 else -w
                        for i, w in enumerate(weights)), cuts, ties)
              for x in range(size)]
    pivotal = [sum(values[x] != values[x ^ (1 << i)] for x in range(size))
               for i in range(n)]
    coeff = walsh(values)
    assert sum(a * a for a in coeff) == size * size
    assert sum(a * a * s.bit_count() for s, a in enumerate(coeff)) == \
        size * sum(pivotal)
    inf = Q(sum(pivotal), size)
    spectral = [Q(a * a, size * size) for a in coeff]
    entropy = -sum(float(p) * log2(float(p)) for p in spectral if p)
    assert entropy <= (log2(n) + 3) * float(inf) + TOL
    A = 41 / (sqrt(2) * (1 - exp(-1)))
    entropy_cap = (1 + 4 * A * m) * sqrt(n) / log(2)
    assert entropy <= entropy_cap + TOL
    COUNTS['weighted_odd_crossing_functions'] += 1
    COUNTS['exact_walsh_parseval_and_energy'] += 1
    COUNTS['numeric_weak_and_noise_entropy_bounds'] += 1
    if inf:
        MAXIMA['entropy_over_influence'] = max(
            MAXIMA['entropy_over_influence'], entropy / float(inf))

    # Fixed block size remains small for meaningful complete moment/noise
    # checks. This does not pretend that the proof's K is this small.
    for k in sorted({1, min(2, n), min(4, n)}):
        block = sorted(RNG.sample(range(n), k))
        selected = [weights[i] for i in block]
        rest = [weights[i] for i in range(n) if i not in block]
        du, dr = score_distribution(selected), score_distribution(rest)
        nb, nr = 1 << k, 1 << (n - k)
        moment1 = sum(cu * cv * abs(u - v)
                      for u, cu in du.items() for v, cv in du.items())
        moment2 = sum(cu * cv * (u - v) ** 2
                      for u, cu in du.items() for v, cv in du.items())
        moment4 = sum(cu * cv * (u - v) ** 4
                      for u, cu in du.items() for v, cv in du.items())
        ea, e2, e4 = Q(moment1, nb * nb), Q(moment2, nb * nb), Q(moment4, nb * nb)
        avar = sum(w * w for w in selected)
        assert e2 == 2 * avar
        assert e4 == 3 * (2 * avar) ** 2 - 4 * sum(w ** 4 for w in selected)
        assert ea * ea * e4 >= e2 ** 3
        assert ea * ea >= Q(2 * avar, 3)
        COUNTS['exact_selected_difference_moments'] += 1

        nsnum = 0
        for r, cr in dr.items():
            plus = sum(cu for u, cu in du.items() if label(r + u, cuts, ties) == 1)
            nsnum += cr * 2 * plus * (nb - plus)
        ns = Q(nsnum, nr * nb * nb)
        assert ns <= Q(sum(pivotal[i] for i in block), 2 * size)
        COUNTS['exact_fixed_block_resampling_union'] += 1

        # All selected score pairs when small; a deterministic sample otherwise.
        pairs = [(Q(u), Q(v)) for u in du for v in du]
        if len(pairs) > 16:
            pairs = RNG.sample(pairs, 16)
        if rest:
            s2 = sum(w * w for w in rest)
            stdev = sqrt(s2)
            be = .56 * sum(abs(w) ** 3 for w in rest) / stdev ** 3
            cdf_error = 0.0
            for t in sorted(dr):
                left = Q(sum(cr for r, cr in dr.items() if r < t), nr)
                right = left + Q(dr[t], nr)
                cdf_error = max(cdf_error, abs(float(left) - phi(t / stdev)),
                                abs(float(right) - phi(t / stdev)))
            assert cdf_error <= be + TOL
            COUNTS['numeric_berry_esseen_cdf_and_left_limits'] += 1
            MAXIMA['observed_cdf_error_over_BE_bound'] = max(
                MAXIMA['observed_cdf_error_over_BE_bound'], cdf_error / be)
        for u, v in pairs:
            intervals = open_pivotal_intervals(cuts, ties, u, v)
            pivotal_prob = Q(sum(cr for r, cr in dr.items()
                                 if label(r + u, cuts, ties) != label(r + v, cuts, ties)), nr)
            open_prob = Q(sum(cr for r, cr in dr.items()
                             if any(a < r < b for a, b in intervals)), nr)
            assert pivotal_prob >= open_prob
            COUNTS['exact_endpoint_atom_inclusion'] += 1
            if rest:
                gaussian = sum(phi(float(b) / stdev) - phi(float(a) / stdev)
                               for a, b in intervals)
                assert float(open_prob) >= gaussian - 2 * len(intervals) * be - TOL
                COUNTS['numeric_open_interval_BE_union'] += 1

    # Rational epsilon tests exercise the physical flip/Fourier degree convention.
    degree_weights = [sum(spectral[s] for s in range(size) if s.bit_count() == j)
                      for j in range(n + 1)]
    for k in range(1, min(n, 5) + 1):
        epsilon = Q(1, 2 * k)
        ns = sum(degree_weights[j] * (1 - (1 - 2 * epsilon) ** j)
                 for j in range(n + 1)) / 2
        tail = sum(degree_weights[k:])
        assert tail * (1 - (1 - 2 * epsilon) ** k) <= 2 * ns
        assert float(ns) <= 20.5 * m * sqrt(float(epsilon)) + TOL
        assert float(tail) <= A * m / sqrt(k) + TOL
        COUNTS['exact_degree_noise_tail_identity'] += 1


def abstract_translations():
    # Coincident translated endpoints, arbitrary rational gaps, all endpoint
    # choices, and opposite displacement signs are included deliberately.
    for m in (1, 3, 5, 7):
        for case in range(120):
            cuts = sorted({Q(RNG.randrange(-30, 31), RNG.choice((1, 2, 3)))
                           for _ in range(4 * m)})[:m]
            assert len(cuts) == m
            ties = [RNG.choice((False, True)) for _ in cuts]
            for u, v in ((Q(0), Q(0)), (Q(0), cuts[-1] - cuts[0]),
                         (Q(-4), Q(7)), (Q(7), Q(-4)),
                         (Q(RNG.randrange(-12, 13), 3), Q(RNG.randrange(-12, 13), 2))):
                open_pivotal_intervals(cuts, ties, u, v)
    COUNTS['abstract_rational_translation_families'] = 480


def constant_regimes():
    for m, B, bias in product((1, 3, 5, 7), (1., 1.5, 3., 10.), (0., .5, 2., 4.)):
        d, cd, err = exp(-(bias + 1) ** 2) / sqrt(2 * pi), sqrt(2 / 3), 2.24 * sqrt(2)
        from math import ceil
        K = max(1, ceil((2 * err * m * B / (d * cd)) ** 2))
        N0 = ceil(max(2 * K * B * B, K * K * B * B))
        assert d * cd * sqrt(K) >= 2 * err * m * B * (1 - 1e-14)
        assert N0 >= K
        assert N0 >= 2 * K * B * B * (1 - 1e-14)
        assert sqrt(N0) >= K * B * (1 - 1e-14)
        COUNTS['explicit_parameter_cutoff_checks'] += 1


def main():
    abstract_translations()
    for n in range(1, 10):
        for case in range(24):
            weights = [RNG.randrange(1, 5) for _ in range(n)]
            m = (1, 3, 5)[case % 3]
            extent = sum(weights)
            # Many crossings land exactly on attained score atoms. Other
            # examples have half-integer endpoints and very narrow gaps.
            cuts = sorted(RNG.sample(range(-2 * extent - 4, 2 * extent + 5), m))
            cuts = [Q(c, 2) for c in cuts]
            ties = [bool(RNG.randrange(2)) for _ in cuts]
            check_function(weights, cuts, ties)
    for n in (10, 11, 12):
        for case in range(8):
            weights = [RNG.randrange(1, 5) for _ in range(n)]
            m = (1, 3, 5)[case % 3]
            cuts = [Q(2 * j - m + 1, 3) for j in range(m)]
            check_function(weights, cuts, [bool(RNG.randrange(2)) for _ in cuts])
    constant_regimes()
    report = {
        'status': 'PASS exact constituent-lemma checks; full analytic audit separate',
        'counts': dict(COUNTS), 'maxima': dict(MAXIMA), 'numerical_tolerance': TOL,
        'exact': ['rational signed translation and open pivotal measure',
                  'endpoint-atom deletion preserves a lower bound',
                  'selected difference second/fourth moments and Holder interpolation',
                  'fixed-block resampling union with physical influence factor one half',
                  'Walsh Parseval, physical energy, and degree-noise tail'],
        'numerical': ['Berry-Esseen CDF including left limits and open interval unions',
                      'spectral entropy and established noise upper bounds',
                      'explicit huge K/N0 parameter cutoffs'],
        'limits': 'No enumeration at enormous N0; not an arbitrary-weight or arbitrary-bias FEI theorem; novelty unverified'
    }
    path = Path(__file__).with_name('regular_moderate_bias_odd_crossing_checks.json')
    path.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
