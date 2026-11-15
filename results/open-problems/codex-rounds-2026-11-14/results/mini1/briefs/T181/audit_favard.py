#!/usr/bin/env python3
"""Independent audit of saved CSVs, without importing exact_favard.py."""
import csv
from fractions import Fraction as R
import json
from math import isqrt
import os
from pathlib import Path
import resource
import signal
import sys
import time


SCALE = 10 ** 60


def floor(x):
    return x.numerator // x.denominator


def ceil(x):
    return -((-x.numerator) // x.denominator)


def atan_interval(q):
    # Even partial sum is below the value; next positive term is the remainder bound.
    terms = 150
    total = sum((R((-1) ** k, (2 * k + 1) * q ** (2 * k + 1))
                 for k in range(terms)), R(0))
    return total, total + R(1, (2 * terms + 1) * q ** (2 * terms + 1))


def independent_pi():
    a, b = atan_interval(2)
    c, d = atan_interval(3)
    return R(floor(4 * (a + c) * SCALE), SCALE), R(ceil(4 * (b + d) * SCALE), SCALE)


def root_interval(m):
    k = isqrt(m * SCALE ** 2)
    assert k * k <= m * SCALE ** 2 < (k + 1) ** 2
    return R(k, SCALE), R(k if k * k == m * SCALE ** 2 else k + 1, SCALE)


def merge_length(starts, p, q):
    intervals = sorted((a * q + b * p, a * q + b * p + q + p) for a, b in starts)
    result = 0
    left, right = intervals[0]
    for a, b in intervals[1:]:
        if a <= right:
            right = max(right, b)
        else:
            result += right - left
            left, right = a, b
    return result + right - left


def audit(n, pi_lo, pi_hi):
    D = 4 ** n
    # A third coordinate construction: examine all base-4 digits of integers in [0,D).
    coords = [k for k in range(D) if all((k // 4 ** j) % 4 in (0, 3) for j in range(n))]
    assert len(coords) == 2 ** n
    starts = [(x, y) for x in coords for y in coords]
    rows = list(csv.DictReader((Path('data') / f'cells_n{n}.csv').open()))
    pieces = [(R(int(r['left_p']), int(r['left_q'])),
               R(int(r['right_p']), int(r['right_q'])), int(r['A']), int(r['B'])) for r in rows]
    assert pieces[0][0] == 0 and pieces[-1][1] == 1
    for i, (lo, hi, a, b) in enumerate(pieces):
        assert lo < hi
        if i:
            _, previous_hi, previous_a, previous_b = pieces[i - 1]
            assert previous_hi == lo
            assert previous_a + previous_b * lo == a + b * lo
            assert (previous_a, previous_b) != (a, b)
        t = (lo + hi) / 2
        assert a * t.denominator + b * t.numerator == merge_length(starts, t.numerator, t.denominator)
    # Integration by parts, with derivative jumps, rather than endpoint primitives:
    # I = B_first + (A_last-B_last)/sqrt(2)
    #     + sum_j (B_right-B_left)*sqrt(1+t_j^2).
    terms = [(1, R(pieces[0][3])), (2, R(pieces[-1][2] - pieces[-1][3], 2))]
    for previous, current in zip(pieces, pieces[1:]):
        t = current[0]
        terms.append((t.numerator ** 2 + t.denominator ** 2,
                      R(current[3] - previous[3], t.denominator)))
    if n == 2:
        # Check the printed closed form in PROOF.md, equation (14).
        coefficients = {}
        for m, c in terms:
            if m == 25:
                m, c = 1, 5 * c
            coefficients[m] = coefficients.get(m, R(0)) + c
        assert coefficients == {1: 94, 2: 45, 5: -32, 17: 12, 34: 6,
                                41: 4, 65: -8, 74: -2, 233: -2,
                                290: -2, 365: -2}
        print('n=2 printed_closed_form=PASS', flush=True)
    lower = upper = 0
    for m, c in terms:
        a, b = root_interval(m)
        lo, hi = (c * a, c * b) if c >= 0 else (c * b, c * a)
        lower += floor(lo * SCALE)
        upper += ceil(hi * SCALE)
    integral_lo, integral_hi = R(lower, SCALE), R(upper, SCALE)
    assert integral_lo > 0
    lower = 4 * integral_lo / (D * pi_hi)
    upper = 4 * integral_hi / (D * pi_lo)
    certificate = json.loads((Path('data') / f'certificate_n{n}.json').read_text())
    # Distinct rigorous enclosures must overlap, and independently reproduce the printed digits.
    assert lower <= R(certificate['upper_rational'])
    assert R(certificate['lower_rational']) <= upper
    assert R(certificate['lower_decimal']) < lower <= upper < R(certificate['upper_decimal'])
    assert upper - lower < R(1, 10 ** 50)
    assert len(pieces) == certificate['affine_pieces']
    print(f'n={n} merge_checks={len(pieces)} independent_integral=PASS '
          f'decimal_enclosure=PASS width_lt_1e-50=PASS', flush=True)


def main():
    signal.alarm(1100)
    started = time.monotonic()
    assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
    assert os.environ.get('OMP_NUM_THREADS') == '1'
    pi_lo, pi_hi = independent_pi()
    for n in range(6):
        audit(n, pi_lo, pi_hi)
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss_bytes = rss if sys.platform == 'darwin' else rss * 1024
    assert rss_bytes < 1_000_000_000
    print(f'PASS elapsed_seconds={time.monotonic() - started:.3f} peak_rss_bytes={rss_bytes}', flush=True)


if __name__ == '__main__':
    main()
