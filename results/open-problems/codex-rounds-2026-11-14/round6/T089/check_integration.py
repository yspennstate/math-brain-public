#!/usr/bin/env python3
"""Exact determinant integrals and GOE envelope constants. Stdlib only."""
from fractions import Fraction as Q
from functools import lru_cache
from itertools import combinations_with_replacement
from math import factorial, isqrt, comb, prod
from pathlib import Path
import json
import os
import resource
import time

START = time.monotonic()
P = Q(22, 7)


def guard():
    assert os.environ['OMP_NUM_THREADS'] == '1'
    assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
    assert time.monotonic()-START < 120
    assert resource.getrusage(resource.RUSAGE_SELF).ru_maxrss < 256*1024**2


def determinant_integral(exponents):
    """Integrate the expanded determinant over the ordered unit simplex.

    Each monomial integrates to the product of inverse prefix degree sums.
    Sum signed permutations by their last exponent, using subsets. This
    never constructs a Pfaffian, pair product, or factorial formula.
    """
    size = 1 << len(exponents)
    values = [Q(0)]*size
    values[0] = Q(1)
    for mask in range(1, size):
        if mask % 512 == 0:
            guard()
        terms = Q(0)
        degree_sum = 0
        for a, exponent in enumerate(exponents):
            if mask & (1 << a):
                degree_sum += exponent+1
                inversions = (mask >> (a+1)).bit_count()
                terms += (-1)**inversions*values[mask ^ (1 << a)]
        values[mask] = terms/degree_sum
    return values[-1]


def pfaffian(matrix):
    """Matching expansion, memoized by the remaining row/column set."""
    @lru_cache(None)
    def recurse(indices):
        if not indices:
            return Q(1)
        i = indices[0]
        return sum(((-1)**(position+1)*matrix[i][j]
                    *recurse(indices[1:position]+indices[position+1:])
                    for position, j in enumerate(indices[1:], 1)), Q(0))
    return recurse(tuple(range(len(matrix))))


def moment_pfaffian(exponents):
    t = [a+1 for a in exponents]
    n = len(t)
    matrix = [[Q(t[j]-t[i], t[i]*t[j]*(t[i]+t[j]))
               for j in range(n)] for i in range(n)]
    if n % 2:
        for i, row in enumerate(matrix):
            row.append(Q(1, t[i]))
        matrix.append([Q(-1, x) for x in t]+[Q(0)])
    return pfaffian(matrix)


def schur_product(exponents):
    t = [a+1 for a in exponents]
    result = Q(1, prod(t))
    for i in range(len(t)):
        for j in range(i+1, len(t)):
            result *= Q(t[j]-t[i], t[i]+t[j])
    return result


def row_product(k):
    a = Q(k-1, 4)+sum((Q(1, i*i) for i in range(1, k+1)), Q(0))
    d = a**k
    for i in range(1, k+1):
        d *= Q(k, i*i)+P**2*sum(
            (Q(1, (i+j)**2) for j in range(1, k+1) if i != j), Q(0))
    return d


def fourth_bound(r, k):
    degree = k*(k-1)//2
    denominator = factorial(k)*prod(i+j for i in range(1, k+1)
                                     for j in range(i+1, k+1))
    return (P**degree*r**(k+degree)/denominator)**4*row_product(k)


def entrywise_bound(r, k):
    # Independently construct every row majorant and all scale factors.
    result = Q(1)
    for row in range(2*k):
        norm = Q(0)
        for column in range(2*k):
            if row < k and column < k:
                entry = Q(1, 2) if row != column else Q(0)
            elif row >= k and column >= k:
                entry = P/(row+column-2*k+2) if row != column else Q(0)
            else:
                smooth = max(row, column)-k+1
                entry = Q(1, smooth)
            norm += entry*entry
        result *= norm
    for i in range(1, k+1):
        result *= (r**i/i)**4
        for j in range(1, i):
            result *= (P/(i+j))**4
    return result


def enclosure(value, digits):
    scale = 10**digits
    lower = isqrt(isqrt(value.numerator*scale**4//value.denominator))
    lo, hi = Q(lower, scale), Q(lower+1, scale)
    assert lo**4 <= value < hi**4
    return [str(lo), str(hi)]


def audit_integrals():
    rows = []
    checks = 0
    for k in range(1, 15):
        guard()
        exponents = list(range(k))
        integral = determinant_integral(exponents)
        assert integral == moment_pfaffian(exponents) == schur_product(exponents)
        recurrence = Q(1)
        for j in range(1, k+1):
            recurrence *= Q(factorial(j-1)**2, factorial(2*j-1))
        assert integral == recurrence
        rows.append(dict(k=k, ordered_integral=str(integral)))
        checks += 1
    # Extra exponent sets exercise orientation, equal rows, and odd augmentation.
    for k in range(1, 11):
        for exponents in ([2*i for i in range(k)],
                          [i*i+1 for i in range(k)],
                          list(reversed(range(k))), [0]*k):
            guard()
            value = determinant_integral(exponents)
            assert value == moment_pfaffian(exponents) == schur_product(exponents)
            checks += 1
    assert rows[0]['ordered_integral'] == '1'
    assert rows[1]['ordered_integral'] == '1/6'
    assert rows[2]['ordered_integral'] == '1/180'
    return dict(three_way_exact_integral_checks=checks,
                ordinary_Vandermonde_dimensions=14,
                arbitrary_exponent_cases=40, both_parities=True,
                reversed_and_repeated_exponents=True, rows=rows)


def audit_constants():
    checks = 0
    thresholds = []
    for r in (Q(0), Q(1, 2), Q(1), Q(2), Q(3)):
        first = first_even = None
        for k in range(1, 21):
            guard()
            q = fourth_bound(r, k)
            assert q == entrywise_bound(r, k)
            checks += 1
            if q < Q(1, 10**24):
                if first is None:
                    first = k
                if k % 2 == 0 and first_even is None:
                    first_even = k
        thresholds.append(dict(R=str(r), first_order=first,
                               first_even_order=first_even,
                               enclosure=enclosure(fourth_bound(r, first), 18)))
    assert [row['first_order'] for row in thresholds[1:4]] == [5, 6, 9]
    assert [row['first_even_order'] for row in thresholds[1:4]] == [6, 6, 10]
    q9, q10 = fourth_bound(Q(2), 9), fourth_bound(Q(2), 10)
    assert Q(55771278, 10**15)**4 < q9 < Q(55771279, 10**15)**4 < Q(1, 10**24)
    assert Q(8253202, 10**18)**4 < q10 < Q(8253203, 10**18)**4 < Q(1, 10**44)
    # Independently integrate the predecessor's envelope using the determinant
    # integrals, including every factorial and the k! cube-to-simplex factor.
    integral_checks = 0
    for k in range(1, 15):
        guard()
        integral = moment_pfaffian(list(range(k)))
        f = prod(factorial(i) for i in range(k))
        c = P**(k*(k-1)//2)*Q(2)**(k*(k+1)//2)*integral/f
        assert c**4*row_product(k) == fourth_bound(Q(2), k)
        integral_checks += 1
    # Compare the previous maximum envelope with the integrated envelope.
    ratios = []
    for k in range(1, 21):
        guard()
        a = schur_product(list(range(k)))
        maximum_fourth = Q(2)**(4*(k-1))*k**(2*k)/Q(4)**(2*k*(k-1))
        ratio_fourth = maximum_fourth/(factorial(k)*a)**4
        assert ratio_fourth >= 1
        if k == 10:
            assert ratio_fourth > 60000**4
            ratios.append(dict(k=k, old_over_new_fourth_power=str(ratio_fourth),
                               old_over_new_greater_than=60000))
    return dict(formula_vs_entrywise_checks=checks,
                integral_vs_cancelled_formula_checks=integral_checks,
                maximum_vs_integral_checks=20, thresholds=thresholds,
                R2_order9_fourth_power=str(q9),
                R2_order9_enclosure=enclosure(q9, 15),
                R2_order10_fourth_power=str(q10),
                R2_order10_enclosure=enclosure(q10, 18), comparisons=ratios)


def audit_comparison():
    laws = [[Q(atoms.count(n), 3) for n in range(6)]
            for atoms in combinations_with_replacement(range(6), 3)]
    laws.append([Q(9999, 10000)]+[Q(0)]*63+[Q(1, 10000)])
    data = []
    for law in laws:
        moments = [sum((p*comb(n, j) for n, p in enumerate(law) if n >= j), Q(0))
                   for j in range(13)]
        partials = []
        value = Q(0)
        for j in range(13):
            value += (-1)**j*moments[j]
            partials.append(value)
        data.append((law[0], moments, partials))
    checks = odd_checks = 0
    for va, a, sa in data:
        guard()
        for vb, b, sb in data:
            for k in range(1, 13):
                lo, hi = (k, k-1) if k % 2 else (k-1, k)
                assert sa[lo] <= va <= sa[hi]
                assert sb[lo] <= vb <= sb[hi]
                assert sb[hi]-sb[lo] == b[k]
                sharp = b[k]+max(abs(sa[lo]-sb[lo]), abs(sa[hi]-sb[hi]))
                assert abs(va-vb) <= sharp <= b[k]+sum(abs(a[j]-b[j]) for j in range(1, k+1))
                checks += 1
                odd_checks += k % 2
    return dict(count_laws=len(laws), target_only_checks=checks,
                odd_order_checks=odd_checks, rare_count64_cluster=True)


def main():
    guard()
    result = dict(integrals=audit_integrals(), constants=audit_constants(),
                  comparison=audit_comparison())
    guard()
    result['resources'] = dict(nice=os.getpriority(os.PRIO_PROCESS, 0),
        OMP_NUM_THREADS=os.environ['OMP_NUM_THREADS'],
        peak_rss_bytes_macos=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        elapsed_seconds=round(time.monotonic()-START, 3),
        measured_rss_guard_bytes=256*1024**2, elapsed_guard_seconds=120,
        processes=1, standard_library_only=True, os_hard_memory_cap=False)
    Path(__file__).with_name('integration_data.json').write_text(json.dumps(result, indent=2)+'\n')
    print('All exact determinant-integral and remainder checks passed.')
    for key, value in result.items():
        brief = {k: v for k, v in value.items() if 'fourth_power' not in k}
        print(key+': '+json.dumps(brief, sort_keys=True))


if __name__ == '__main__':
    main()
