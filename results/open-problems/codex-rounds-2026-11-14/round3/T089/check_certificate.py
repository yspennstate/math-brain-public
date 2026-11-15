#!/usr/bin/env python3
"""Exact audits of the finite correlation certificate; standard library only."""
from collections import Counter
from fractions import Fraction as Q
from itertools import combinations, combinations_with_replacement
from math import comb, factorial
from pathlib import Path
import json
import os
import resource
import time

START = time.monotonic()


def guard():
    assert os.environ.get('OMP_NUM_THREADS') == '1'
    assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
    assert resource.getrusage(resource.RUSAGE_SELF).ru_maxrss < 256*1024**2
    assert time.monotonic()-START < 120


def histogram(points, w, s):
    """Integrate counts by geometric event cells, never using gap lengths."""
    assert 0 <= s < w
    cuts = sorted({Q(0), w, *points, *((p-s) % w for p in points)})
    hist = [Q(0)] * (len(points)+1)
    for left, right in zip(cuts, cuts[1:]):
        mid = (left+right)/2
        count = sum(0 < (p-mid) % w <= s for p in points)
        hist[count] += (right-left)/w
    assert sum(hist) == 1
    return hist


def moments(hist, order):
    return [sum((p*comb(n, k) for n, p in enumerate(hist)), Q(0))
            for k in range(order+1)]


def subset_moment(points, w, s, k):
    """Sum intersections of start arcs over labelled k-subsets."""
    if k == 0:
        return Q(1)
    total = Q(0)
    for selected in combinations(points, k):
        intersections = [(Q(0), w)]
        for p in selected:
            lo = (p-s) % w
            if s == 0:
                arcs = []
            elif lo < p:
                arcs = [(lo, p)]
            else:
                arcs = [(Q(0), p), (lo, w)]
            intersections = [(max(a, c), min(b, d))
                             for a, b in intersections for c, d in arcs
                             if max(a, c) < min(b, d)]
        total += sum((b-a for a, b in intersections), Q(0))
    return total/w


def gaps(points, w):
    return [b-a for a, b in zip(points, points[1:])] + [w-points[-1]+points[0]]


def void(gs, w, s):
    return sum((max(g-s, Q(0)) for g in gs), Q(0))/w


def audit_geometry():
    configs = identities = brackets = 0
    w = Q(6)
    for n in range(2, 6):
        for points in combinations_with_replacement(map(Q, range(6)), n):
            guard()
            configs += 1
            for i in range(12):
                s = Q(i, 2)
                hist = histogram(points, w, s)
                ak = moments(hist, 6)
                assert hist[0] == void(gaps(points, w), w, s)
                assert ak[1] == n*s/w
                for k in range(n+1):
                    assert ak[k] == subset_moment(points, w, s, k)
                    identities += 1
                for m in (1, 2, 3):
                    lo = sum(((-1)**k*ak[k] for k in range(2*m)), Q(0))
                    hi = lo+ak[2*m]
                    assert lo <= hist[0] <= hi
                    brackets += 1
    return dict(configurations=configs, subset_vs_count_moment_identities=identities,
                void_and_mean_checks=12*configs, bonferroni_brackets=brackets)


def audit_comparison():
    # All probability laws on {0,...,4} with denominator 4, plus a rare
    # large cluster. This checks the target-only remainder for arbitrary laws.
    laws = []
    for atoms in combinations_with_replacement(range(5), 4):
        counts = Counter(atoms)
        laws.append([Q(counts[n], 4) for n in range(5)])
    cluster = [Q(0)]*21
    cluster[0], cluster[20] = Q(99, 100), Q(1, 100)
    laws.append(cluster)
    stats = [(p[0], moments(p, 6)) for p in laws]
    checks = nonvacuous = 0
    for v, ak in stats:
        guard()
        for e, bk in stats:
            for m in (1, 2, 3):
                error = sum((abs(ak[k]-bk[k]) for k in range(1, 2*m+1)), Q(0))
                bound = error+bk[2*m]
                assert abs(v-e) <= bound
                checks += 1
                nonvacuous += bound < 1
    return dict(laws=len(laws), target_only_remainder_comparisons=checks,
                bound_below_one=nonvacuous, clustered_law_included=True)


def audit_grid():
    cases = 0
    for n in range(2, 6):
        raw = list(combinations_with_replacement(map(Q, range(6)), n))
        # Widely separated pairs, both unfolded to exactly unit density.
        for p, q in zip(raw, reversed(raw)):
            guard()
            w = Q(n)
            points = [x*w/6 for x in p]
            target = [x*w/6 for x in q]
            r = w*Q(3, 4)
            grid = [i*r/6 for i in range(7)]
            data = [moments(histogram(points, w, s), 6) for s in grid]
            ref = [moments(histogram(target, w, s), 6) for s in grid]
            ga, gb = gaps(points, w), gaps(target, w)
            cuts = {Q(0), r, *(g for g in ga+gb if g <= r)}
            exact_error = max(abs(void(ga, w, s)-void(gb, w, s)) for s in cuts)
            for order in (2, 4, 6):
                eps = max(sum((abs(a[k]-b[k]) for k in range(1, order+1)), Q(0))
                          for a, b in zip(data, ref))
                # Here the target is another finite spectrum, so use its
                # actual final factorial moment rather than the GOE bound.
                bound = eps+ref[-1][order]+r/6
                assert exact_error <= bound
                cases += 1
    return dict(finite_target_grid_certificates=cases,
                full_void_supremum_at_all_hinges=True)


def pair_measure(points, w):
    return Counter((y-x) % w for i, x in enumerate(points)
                   for j, y in enumerate(points) if i != j)


def cdf(gs, s):
    return Q(sum(g <= s for g in gs), len(gs))


def audit_homometric():
    a = list(map(Q, (0, 1, 4, 6)))
    b = list(map(Q, (0, 1, 3, 7)))
    a, b = [x/3 for x in a], [x/3 for x in b]
    rows = []
    for repeat in (1, 2, 3, 8):
        guard()
        w = Q(4*repeat)
        aa = [x+4*l for l in range(repeat) for x in a]
        bb = [x+4*l for l in range(repeat) for x in b]
        assert pair_measure(aa, w) == pair_measure(bb, w)
        for s in (Q(i, 12) for i in range(48)):
            ma, mb = moments(histogram(aa, w, s), 3), moments(histogram(bb, w, s), 3)
            assert ma[:3] == mb[:3]
        ha, hb = histogram(aa, w, Q(4, 3)), histogram(bb, w, Q(4, 3))
        assert ha[:4] == [Q(1, 6), Q(1, 3), Q(1, 2), Q(0)]
        assert hb[:4] == [Q(1, 12), Q(7, 12), Q(1, 4), Q(1, 12)]
        ga, gb = gaps(aa, w), gaps(bb, w)
        assert cdf(ga, Q(1))-cdf(gb, Q(1)) == Q(1, 4)
        assert void(ga, w, Q(4, 3))-void(gb, w, Q(4, 3)) == Q(1, 12)
        internal = cdf(ga[:-1], Q(1))-cdf(gb[:-1], Q(1))
        assert internal == Q(repeat, 4*repeat-1)
        rows.append(dict(repetitions=repeat, points_per_spectrum=4*repeat,
                         full_pair_measures_equal=True,
                         cyclic_cdf_difference='1/4', void_difference='1/12',
                         internal_cdf_difference=str(internal)))
    # The difference measure can also be checked without a point-pair loop.
    expected = Counter({Q(r, 3): 1 for r in range(1, 12) if r != 6})
    expected[Q(2)] = 2
    assert pair_measure(a, Q(4)) == expected
    # Independent power-spectrum audit at all twelve Fourier modes, with
    # rounded complex arithmetic only as a diagnostic, never as proof.
    import cmath
    for mode in range(12):
        xa = abs(sum(cmath.exp(2j*cmath.pi*mode*float(x)/4) for x in a))**2
        xb = abs(sum(cmath.exp(2j*cmath.pi*mode*float(x)/4) for x in b))**2
        assert abs(xa-xb) < 1e-10
    return dict(period_repetitions=rows,
                exact_pair_difference_multiplicities={str(k): v for k, v in sorted(expected.items())},
                count_histogram_A=[str(x) for x in histogram(a, Q(4), Q(4, 3))],
                count_histogram_B=[str(x) for x in histogram(b, Q(4), Q(4, 3))],
                Fourier_diagnostic_modes=12)


def audit_tail():
    rows = []
    for r in (Q(1, 2), Q(1), Q(2)):
        guard()
        a = r*max(Q(2), r+Q(1, 2))
        recurrence = 2*a*a
        m = 1
        while True:
            direct = a**(2*m)*(4*m)**m/factorial(2*m)
            assert direct == recurrence
            if direct <= Q(1, 10**6):
                denominator = 10**12
                ceiling = (direct.numerator*denominator+direct.denominator-1)//direct.denominator
                rows.append(dict(R=str(r), C_R=str(max(Q(2), r+Q(1, 2))),
                                 first_even_order_below_one_millionth=2*m,
                                 certified_rational_upper_bound=str(Q(ceiling, denominator))))
                break
            recurrence *= 2*a*a*Q(m+1, m)**m/(2*m+1)
            m += 1
            assert m <= 1000
    return rows


def main():
    guard()
    result = dict(geometry=audit_geometry(), comparison=audit_comparison(),
                  grids=audit_grid(), obstruction=audit_homometric(),
                  GOE_analytic_tail_bounds=audit_tail())
    result['resources'] = dict(nice=os.getpriority(os.PRIO_PROCESS, 0),
                               OMP_NUM_THREADS=os.environ['OMP_NUM_THREADS'],
                               elapsed_seconds=round(time.monotonic()-START, 3),
                               peak_rss_bytes_macos=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                               measured_rss_guard_bytes=256*1024**2,
                               elapsed_guard_seconds=120, os_hard_memory_cap=False)
    Path(__file__).with_name('certificate_data.json').write_text(json.dumps(result, indent=2)+'\n')
    print('All exact certificate checks passed; Fourier checks are diagnostic only.')
    for key, value in result.items():
        if key == 'obstruction':
            value = value['period_repetitions']
        print(key+': '+json.dumps(value, sort_keys=True))


if __name__ == '__main__':
    main()
