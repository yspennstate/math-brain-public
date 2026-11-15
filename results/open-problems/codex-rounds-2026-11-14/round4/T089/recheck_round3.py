#!/usr/bin/env python3
"""Independent exact audit of the target-only comparison and old threshold."""
from fractions import Fraction as Q
from itertools import combinations_with_replacement
from math import comb, factorial
import json
import os
import resource
import time

START = time.monotonic()


def guard():
    assert os.environ['OMP_NUM_THREADS'] == '1'
    assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
    assert resource.getrusage(resource.RUSAGE_SELF).ru_maxrss < 128*1024**2
    assert time.monotonic()-START < 120


def partial(n, r):
    return sum((-1)**j*comb(n, j) for j in range(min(r, n)+1))


def main():
    guard()
    identities = 0
    for n in range(81):
        for r in range(81):
            expected = 1 if n == 0 else (-1)**r*(comb(n-1, r) if r < n else 0)
            assert partial(n, r) == expected
            identities += 1
    # Enumerate rational laws by integer compositions, independently of the
    # earlier histogram and subset-intersection implementations.
    laws = []
    for atoms in combinations_with_replacement(range(7), 3):
        laws.append([Q(atoms.count(n), 3) for n in range(7)])
    cluster = [Q(0)]*41
    cluster[0], cluster[40] = Q(999, 1000), Q(1, 1000)
    laws.append(cluster)
    table = []
    for law in laws:
        guard()
        table.append((law[0], [sum((p*comb(n, k) for n, p in enumerate(law)
                                   if n >= k), Q(0)) for k in range(11)]))
    checks = sharp_checks = 0
    for va, a in table:
        guard()
        for vb, b in table:
            for k in range(2, 11, 2):
                upper = sum((-1)**j*(a[j]-b[j]) for j in range(k+1))
                lower = upper-(a[k]-b[k])
                sharp = b[k]+max(abs(upper), abs(lower))
                simple = b[k]+sum(abs(a[j]-b[j]) for j in range(1,k+1))
                assert abs(va-vb) <= sharp <= simple
                checks += 1
                sharp_checks += sharp < simple
    # Direct factorial formula against a recurrence independently reduced
    # by cancelling the two new factorial factors.
    old = Q(50)
    first = None
    comparisons = 0
    for m in range(1, 221):
        guard()
        direct = Q(5)**(2*m)*(4*m)**m/factorial(2*m)
        assert old == direct
        comparisons += 1
        if first is None and direct <= Q(1,10**6):
            first = 2*m
        old *= Q(50,2*m+1)*Q(m+1,m)**m
    assert first == 390
    print(json.dumps(dict(previous_result_holds=True,
        binomial_identities=identities, rational_count_laws=len(laws),
        target_only_comparisons=checks, sharper_than_sum=sharp_checks,
        old_formula_vs_recurrence=comparisons, old_R2_first_even_order=first,
        nice=os.getpriority(os.PRIO_PROCESS,0),
        OMP_NUM_THREADS=os.environ['OMP_NUM_THREADS'],
        peak_rss_bytes_macos=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        elapsed_seconds=round(time.monotonic()-START,3)),sort_keys=True))


if __name__ == '__main__':
    main()
