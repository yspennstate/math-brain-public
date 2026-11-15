#!/usr/bin/env python3
"""Independent exact check of the earlier empty-to-spacing inequality."""
from fractions import Fraction as Q
from itertools import combinations_with_replacement
from math import comb
import json
import os
import resource
import time

START = time.monotonic()


def guard():
    assert os.environ.get('OMP_NUM_THREADS') == '1'
    assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
    assert resource.getrusage(resource.RUSAGE_SELF).ru_maxrss < 256 * 1024**2
    assert time.monotonic() - START < 120


def target(s):
    return min(Q(1), s / 2)


def empty(gs, w, s):
    return sum((max(g - s, Q(0)) for g in gs), Q(0)) / w


def target_empty(s):
    return max(2 - s, Q(0))**2 / 4


def cdf_error(gs, right):
    return max(abs(Q(sum(g < s if left else g <= s for g in gs), len(gs))
                   - target(s))
               for s in {Q(0), right, *(g for g in gs if g <= right)}
               for left in (True, False))


def empty_error(gs, w, right):
    # On each cell, differentiate the explicit quadratic error, not V itself.
    cuts = sorted({Q(0), min(Q(2), right), right,
                   *(g for g in gs if g <= right)})
    values = [abs(empty(gs, w, s) - target_empty(s)) for s in cuts]
    for a, b in zip(cuts, cuts[1:]):
        if a >= 2:
            continue
        # Error is quadratic on this open interval; locate its vertex using
        # three exact values and a quadratic interpolant.
        mid = (a + b) / 2
        fa = empty(gs, w, a) - target_empty(a)
        fm = empty(gs, w, mid) - target_empty(mid)
        fb = empty(gs, w, b) - target_empty(b)
        curvature = 2 * (fa + fb - 2 * fm) / (b - a)**2
        if curvature:
            linear = (fb - fa) / (b - a) - curvature * (a + b)
            vertex = -linear / (2 * curvature)
            if a <= vertex <= b:
                values.append(abs(empty(gs, w, vertex) - target_empty(vertex)))
    return max(values)


def main():
    guard()
    configurations = checks = informative = 0
    for n in range(2, 6):
        for points in combinations_with_replacement(map(Q, range(6)), n):
            gs = [b-a for a, b in zip(points, points[1:])]
            gs += [6 - points[-1] + points[0]]
            # Rescale to cover both signs of rho-1, plus rho=1.
            for w in (Q(n, 2), Q(n), Q(2*n)):
                guard()
                scaled = [g * w / 6 for g in gs]
                rho = Q(n) / w
                for h in (Q(1, 4), Q(1, 2), Q(1)):
                    delta = empty_error(scaled, w, 2+h)
                    bound = Q(1, n) + (2*delta/h + h/2 + abs(rho-1))/rho
                    err = cdf_error(scaled[:-1], Q(2))
                    assert err <= bound, (points, w, h, err, bound)
                    checks += 1
                    informative += bound < 1
            configurations += 1
    assert configurations == sum(comb(5+n, n) for n in range(2, 6)) == 455
    sharpness = 0
    for n in (4, 8, 16, 32, 64, 128):
        for k in sorted({1, n//4, n//2}):
            guard()
            gs = [Q(2*j-1, n) for j in range(1, n+1)]
            gs[n//2-k:n//2+k] = [Q(1)] * (2*k)
            assert sum(gs) == n
            assert cdf_error(gs, Q(2)) == Q(k, n)
            assert empty_error(gs, Q(n), Q(3)) == Q(k, n)**2
            sharpness += 1
    print(json.dumps(dict(previous_result_holds=True,
                          configurations=configurations,
                          full_supremum_theorem_checks=checks,
                          bound_below_one=informative,
                          exact_sharpness_cases=sharpness,
                          nice=os.getpriority(os.PRIO_PROCESS, 0),
                          OMP_NUM_THREADS=os.environ['OMP_NUM_THREADS'],
                          peak_rss_bytes_macos=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                          elapsed_seconds=round(time.monotonic()-START, 3)),
                     sort_keys=True))


if __name__ == '__main__':
    main()
