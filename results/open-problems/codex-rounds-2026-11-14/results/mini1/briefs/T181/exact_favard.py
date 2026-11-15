#!/usr/bin/env python3
"""Exact slope arrangements and rational Favard enclosures; standard library only.

Run: OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 \
     nice -n 15 python3 exact_favard.py --max-n 5
Outputs are confined to the current directory. No network or subprocess calls.
"""
import argparse
from collections import defaultdict
import csv
from fractions import Fraction as F
from itertools import product
import json
from math import atan, cos, gcd, isqrt, pi, sin, sqrt
import os
from pathlib import Path
import resource
import signal
import time


def coordinates(n):
    out = [0]
    for _ in range(n):
        out = [4 * a + d for a in out for d in (0, 3)]
    return sorted(out)


def word_coordinates(n):
    return sorted(sum(3 * bit * 4 ** j for j, bit in enumerate(bits))
                  for bits in product((0, 1), repeat=n))


def crossings(coords):
    """All endpoint crossings, using coordinate differences and equal endpoint offsets."""
    diffs = sorted({a - b for a in coords for b in coords})
    events = {F(0), F(1)}
    for dx in diffs:
        for dy in diffs:
            for delta in (-1, 0, 1):
                a, b = dx + delta, dy + delta
                if b and a * b < 0 and abs(a) < abs(b):
                    events.add(F(-a, b))
    return sorted(events)


def pair_crossings(points):
    """Independent, literal pair enumeration of the endpoint lines."""
    endpoints = [(a + e, b + e) for a, b in points for e in (0, 1)]
    events = {F(0), F(1)}
    for i, (a, b) in enumerate(endpoints):
        for c, d in endpoints[:i]:
            if b != d:
                t = F(c - a, b - d)
                if 0 < t < 1:
                    events.add(t)
    return sorted(events)


def gap_coefficients(points, p, q):
    """Union of equal intervals: width + sum min(consecutive start gap, width)."""
    ordered = sorted(points, key=lambda ab: ab[0] * q + ab[1] * p)
    a_total = b_total = 1
    for (a, b), (c, d) in zip(ordered, ordered[1:]):
        da, db = c - a, d - b
        if da * q + db * p < q + p:
            a_total += da
            b_total += db
        else:
            a_total += 1
            b_total += 1
    return a_total, b_total


def sweep_length(points, p, q):
    """Independent exact union length, scaled by q, via endpoint occupancy."""
    endpoints = sorted([(a * q + b * p, 1) for a, b in points]
                       + [((a + 1) * q + (b + 1) * p, -1) for a, b in points])
    count = total = 0
    previous = endpoints[0][0]
    for position, change in endpoints:
        if count:
            total += position - previous
        count += change
        assert count >= 0
        previous = position
    assert count == 0
    return total


def arctan_bounds(inverse, terms=100):
    partial = sum((F((-1) ** k, (2 * k + 1) * inverse ** (2 * k + 1))
                   for k in range(terms)), F(0))
    next_term = F((-1) ** terms, (2 * terms + 1) * inverse ** (2 * terms + 1))
    return min(partial, partial + next_term), max(partial, partial + next_term)


def pi_bounds():
    a, b = arctan_bounds(5)
    c, d = arctan_bounds(239)
    return 16 * a - 4 * d, 16 * b - 4 * c


def radical_bounds(radicals, digits=55):
    """Bounds for sum c/sqrt(m), with sign-aware rational interval arithmetic."""
    scale = 10 ** digits
    low = high = 0
    for m, c in radicals.items():
        r = isqrt(m * scale * scale)
        if r * r == m * scale * scale:
            lo = hi = F(scale, r)
        else:
            lo, hi = F(scale, r + 1), F(scale, r)
        lower, upper = (c * lo, c * hi) if c >= 0 else (c * hi, c * lo)
        lower *= scale
        upper *= scale
        low += lower.numerator // lower.denominator
        high += -((-upper.numerator) // upper.denominator)
    return F(low, scale), F(high, scale)


def decimal_outer(low, high, places=14):
    scale = 10 ** places
    lo = low.numerator * scale // low.denominator
    hi = -((-high.numerator * scale) // high.denominator)
    def show(x):
        sign = '-' if x < 0 else ''
        x = abs(x)
        return f'{sign}{x // scale}.{x % scale:0{places}d}'
    return show(lo), show(hi)


def floating_projection(points, D, theta):
    c, s = cos(theta), sin(theta)
    intervals = sorted((a * c + b * s, (a + 1) * c + (b + 1) * s)
                       for a, b in points)
    total = 0.0
    left, right = intervals[0]
    for a, b in intervals[1:]:
        if a > right:
            total += right - left
            left, right = a, b
        else:
            right = max(right, b)
    return (total + right - left) / D


def compute(n, output_dir):
    started = time.monotonic()
    D = 4 ** n
    coords = coordinates(n)
    assert coords == word_coordinates(n)
    points = list(product(coords, repeat=2))
    events = crossings(coords)
    if n <= 4:
        assert events == pair_crossings(points)
    raw_cells = []
    sweep_checks = 0
    for lo, hi in zip(events, events[1:]):
        # Two distinct rational samples give an independent affine identity check.
        for weight in (1, 2):
            t = (weight * lo + hi) / (weight + 1)
            p, q = t.numerator, t.denominator
            ab = gap_coefficients(points, p, q)
            assert ab[0] * q + ab[1] * p == sweep_length(points, p, q)
            sweep_checks += 1
            if weight == 1:
                a, b = ab
            else:
                assert ab == (a, b)
        raw_cells.append((lo, hi, a, b))
    # Check all event angles too, including ties and multiple simultaneous crossings.
    for i, t in enumerate(events):
        p, q = t.numerator, t.denominator
        exact = sweep_length(points, p, q)
        if i:
            _, _, a, b = raw_cells[i - 1]
            assert a * q + b * p == exact
        if i < len(raw_cells):
            _, _, a, b = raw_cells[i]
            assert a * q + b * p == exact
    # Merge cells with identical affine expressions.
    cells = []
    for lo, hi, a, b in raw_cells:
        if cells and cells[-1][2:] == (a, b):
            cells[-1] = (cells[-1][0], hi, a, b)
        else:
            cells.append((lo, hi, a, b))
    radicals = defaultdict(int)
    for lo, hi, a, b in cells:
        for t, sign in ((lo, -1), (hi, 1)):
            p, q = t.numerator, t.denominator
            radicals[p * p + q * q] += sign * (a * p - b * q)
    radicals = {m: c for m, c in sorted(radicals.items()) if c}
    if n == 0:
        assert radicals == {1: 1}
    if n == 1:
        assert cells == [(F(0), F(1, 2), 2, 8), (F(1, 2), F(1), 6, 0)]
        assert radicals == {1: 8, 2: 6, 5: -20}
    rlo, rhi = radical_bounds(radicals)
    plo, phi = pi_bounds()
    assert rlo > 0
    flo, fhi = 4 * rlo / (D * phi), 4 * rhi / (D * plo)
    assert fhi - flo < F(1, 10 ** 45)
    lo_str, hi_str = decimal_outer(flo, fhi)
    approx = 4 / (pi * D) * sum(c / sqrt(m) for m, c in radicals.items())
    assert abs(approx - float(flo)) < 1e-11
    # Analytic exceptional directions; these are exact unnormalized lengths.
    assert sweep_length(points, 0, 1) == 2 ** n
    assert sweep_length(points, 1, 1) == 2 * 3 ** n
    assert sweep_length(points, 1, 2) == 3 * D
    # Independent direct angular midpoint integration, no event list or affine cells.
    quadrature = []
    for samples in (2048, 8192):
        value = sum(floating_projection(points, D, (i + 0.5) * pi / (4 * samples))
                    for i in range(samples)) / samples
        quadrature.append({'samples': samples, 'value': value,
                           'absolute_error': abs(value - float(flo))})
    assert quadrature[-1]['absolute_error'] < 2e-4
    with (output_dir / f'cells_n{n}.csv').open('w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['left_p', 'left_q', 'right_p', 'right_q', 'A', 'B'])
        for lo, hi, a, b in cells:
            writer.writerow([lo.numerator, lo.denominator, hi.numerator, hi.denominator, a, b])
    certificate = {
        'n': n, 'D': D,
        'normalization': 'Fav(K_n) = 4/(pi*D) * sum(coefficient/sqrt(radicand))',
        'radicals': [{'radicand': m, 'coefficient': c} for m, c in radicals.items()],
        'lower_rational': str(flo), 'upper_rational': str(fhi),
        'lower_decimal': lo_str, 'upper_decimal': hi_str,
        'candidate_cells': len(raw_cells), 'affine_pieces': len(cells),
        'sweep_sample_checks': sweep_checks, 'event_checks': len(events),
        'literal_event_enumeration': n <= 4,
        'direct_quadrature': quadrature,
        'elapsed_seconds': round(time.monotonic() - started, 3),
    }
    (output_dir / f'certificate_n{n}.json').write_text(json.dumps(certificate, indent=2) + '\n')
    print(f'n={n} squares={len(points)} candidate_cells={len(raw_cells)} '
          f'affine_pieces={len(cells)} radical_terms={len(radicals)} '
          f'Fav=[{lo_str}, {hi_str}] '
          f'quadrature_error={quadrature[-1]["absolute_error"]:.3g} '
          f'seconds={certificate["elapsed_seconds"]}', flush=True)
    return certificate


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--max-n', type=int, default=5, choices=range(0, 6))
    args = parser.parse_args()
    signal.alarm(1100)
    priority = os.getpriority(os.PRIO_PROCESS, 0)
    assert priority >= 15, f'Expected nice >= 15; got {priority}'
    assert os.environ.get('OMP_NUM_THREADS') == '1'
    print(f'priority={priority} OMP_NUM_THREADS=1 single_thread=standard_library', flush=True)
    started = time.monotonic()
    output_dir = Path('data')
    output_dir.mkdir(exist_ok=True)
    certificates = [compute(n, output_dir) for n in range(args.max_n + 1)]
    with (output_dir / 'summary.csv').open('w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['n', 'lower', 'upper', 'candidate_cells', 'affine_pieces', 'radical_terms'])
        for c in certificates:
            writer.writerow([c['n'], c['lower_decimal'], c['upper_decimal'],
                             c['candidate_cells'], c['affine_pieces'], len(c['radicals'])])
    # macOS reports bytes; Linux reports KiB.
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    import sys
    rss_bytes = rss if sys.platform == 'darwin' else rss * 1024
    assert rss_bytes < 1_000_000_000
    print(f'PASS elapsed_seconds={time.monotonic() - started:.3f} peak_rss_bytes={rss_bytes}', flush=True)


if __name__ == '__main__':
    main()
