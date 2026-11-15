#!/usr/bin/env python3
"""Independent exact arithmetic recheck of rounds 3 and 4. Stdlib only."""
from fractions import Fraction as F
from itertools import combinations_with_replacement
from math import comb, factorial
import json
import os
import resource
import time

START = time.monotonic()


def guard():
    assert os.environ.get('OMP_NUM_THREADS') == '1'
    assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
    assert time.monotonic() - START < 120
    assert resource.getrusage(resource.RUSAGE_SELF).ru_maxrss < 256 * 1024**2


def main():
    guard()
    c = F(121, 147)
    tests = 0
    firsts = []
    for r in (F(1, 2), F(1), F(2)):
        first = None
        for k in range(2, 101, 2):
            guard()
            direct = r**(2*k) * (k * (k + (k-1)*c))**(k//2) / factorial(k)**2
            # Form the whole fourth power one factor at a time, independently
            # of the square-root exponent used in the direct expression.
            fourth = F(1)
            for j in range(1, k+1):
                fourth *= r**4 * k * (k + (k-1)*c) / j**4
            assert direct**2 == fourth
            if first is None and fourth < F(1, 10**24):
                first = k
            if (r, k) == (F(2), 58):
                assert F(913316, 10**12)**4 < fourth < F(913317, 10**12)**4
            tests += 1
        firsts.append(first)
    assert firsts == [14, 26, 58]

    identities = 0
    for n in range(65):
        for m in range(33):
            total = sum((-1)**j * comb(n, j) for j in range(min(n, m)+1))
            expected = 1 if n == 0 else (-1)**m * (comb(n-1, m) if m < n else 0)
            assert total == expected
            identities += 1

    laws = []
    for atoms in combinations_with_replacement(range(6), 3):
        laws.append([F(atoms.count(n), 3) for n in range(6)])
    laws.append([F(9999, 10000)] + [F(0)]*63 + [F(1, 10000)])
    statistics = []
    for law in laws:
        moments = [sum((p * comb(n, j) for n, p in enumerate(law) if n >= j), F(0))
                   for j in range(11)]
        statistics.append((law[0], moments))
    comparisons = 0
    for va, a in statistics:
        guard()
        for vb, b in statistics:
            for k in range(2, 11, 2):
                ua = sum((-1)**j*a[j] for j in range(k+1))
                ub = sum((-1)**j*b[j] for j in range(k+1))
                la, lb = ua-a[k], ub-b[k]
                sharp = b[k] + max(abs(ua-ub), abs(la-lb))
                assert abs(va-vb) <= sharp <= b[k]+sum(abs(a[j]-b[j]) for j in range(1,k+1))
                comparisons += 1

    guard()
    print(json.dumps(dict(previous_result_holds=True,
        bound_fourth_power_checks=tests, first_even_orders=firsts,
        order58_enclosure='913316/10^12 < sqrt(Q58) < 913317/10^12',
        binomial_identities=identities, count_laws=len(laws),
        target_only_comparisons=comparisons,
        rare_count64_cluster=True,
        nice=os.getpriority(os.PRIO_PROCESS, 0),
        peak_rss_bytes_macos=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        elapsed_seconds=round(time.monotonic()-START, 3)), sort_keys=True))


if __name__ == '__main__':
    main()
