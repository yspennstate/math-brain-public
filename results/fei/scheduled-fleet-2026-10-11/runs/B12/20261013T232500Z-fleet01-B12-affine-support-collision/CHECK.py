#!/usr/bin/env python3
"""Exact controls for the affine-support collision theorem and X007 guard."""

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import product
from math import log2
import random

SEED = 0xB12A0584
TOL = 2e-11


def fwht(values):
    a = [Fraction(x) for x in values]
    step = 1
    while step < len(a):
        for start in range(0, len(a), 2 * step):
            for j in range(start, start + step):
                x, y = a[j], a[j + step]
                a[j], a[j + step] = x + y, x - y
        step *= 2
    return tuple(x / len(a) for x in a)


def eraw(values):
    ans = 0.0
    for coefficient in fwht(values):
        square = coefficient * coefficient
        if square:
            ans += float(square) * log2(1.0 / float(square))
    return ans


def real_influence(values):
    n = len(values).bit_length() - 1
    total = Fraction(0)
    for i in range(n):
        total += sum((Fraction(values[x]) - Fraction(values[x ^ (1 << i)])) ** 2
                     for x in range(len(values))) / (4 * len(values))
    return total


def subcube_indicator(n, r):
    return tuple(int((x & ((1 << r) - 1)) == 0) for x in range(1 << n))


def collision_gap(f, q):
    fq = tuple(x * y for x, y in zip(f, q))
    return eraw(f) + eraw(q) - eraw(fq)


def exhaustive_affine_collision():
    cases = 0
    minimum = float("inf")
    for n in range(5):
        N = 1 << n
        for f in product((-1, 1), repeat=N):
            for r in range(n + 1):
                q = subcube_indicator(n, r)
                gap = collision_gap(f, q)
                assert gap >= -TOL
                minimum = min(minimum, gap)
                cases += 1
    return cases, minimum


def exhaustive_signed_affine_formula():
    cases = 0
    for n in range(6):
        for r in range(n + 1):
            d = n - r
            if d > 4:
                continue
            p = Fraction(1, 1 << r)
            q = subcube_indicator(n, r)
            for signs in product((-1, 1), repeat=1 << d):
                b = tuple(q[x] * signs[x >> r] for x in range(1 << n))
                expected = 2 * r * float(p) + float(p) * eraw(signs)
                assert abs(eraw(b) - expected) <= TOL
                assert eraw(b) + TOL >= eraw(q)
                cases += 1
    return cases


def transverse_parity_controls():
    rng = random.Random(SEED)
    cases = 0
    largest_ratio = 0.0
    for n in range(1, 11):
        A = [x for x in range(1 << n) if x.bit_count() % 2 == 0]
        trials = 256 if n <= 6 else 64
        for _ in range(trials):
            values = [0] * (1 << n)
            for x in A:
                values[x] = rng.choice((-1, 1))
            entropy = eraw(values)
            influence = float(real_influence(values))
            assert abs(influence - n / 4) <= TOL
            assert entropy <= 4 * influence + TOL
            largest_ratio = max(largest_ratio, entropy / influence)
            cases += 1
    # A point support attains the constant four exactly.
    point = (1,) + (0,) * 15
    assert abs(eraw(point) / float(real_influence(point)) - 4.0) <= TOL
    return cases, largest_ratio


NEGATIVE_F = {
    2, 3, 6, 7, 8, 9, 11, 13, 16, 17, 19, 20, 21, 22, 26, 27,
    28, 31, 32, 36, 37, 38, 42, 43, 44, 49, 50, 52, 53, 56, 57,
    59, 60, 61, 62, 64, 65, 68, 69, 70, 71, 72, 73, 75, 76, 82,
    86, 88, 89, 92, 94, 97, 100, 101, 102, 104, 105, 106, 107, 110,
    111, 113, 115, 118, 119, 123, 127,
}


def factor_integer(n):
    out = {}
    prime = 2
    while prime * prime <= n:
        while n % prime == 0:
            out[prime] = out.get(prime, 0) + 1
            n //= prime
        prime += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def exact_x007_support_falsifier():
    N = 128
    f = tuple(-1 if x in NEGATIVE_F else 1 for x in range(N))
    q = tuple(0 if x == 0 else 1 for x in range(N))
    fq = tuple(x * y for x, y in zip(f, q))
    hist_f = Counter(abs(int(x * N)) for x in fwht(f))
    hist_fq = Counter(abs(int(x * N)) for x in fwht(fq))
    hist_q = Counter(abs(int(x * N)) for x in fwht(q))
    assert hist_f == Counter({2: 60, 6: 48, 26: 16, 30: 4})
    assert hist_fq == Counter({3: 60, 7: 48, 25: 16, 29: 4})
    assert hist_q == Counter({1: 127, 127: 1})

    # N^2 J# = sum_p exponent[p] log_2(p).  Compare the two integer
    # products exactly, rather than trusting a floating logarithm.
    exponents = defaultdict(int)
    for sign, histogram in ((1, hist_f), (1, hist_q), (-1, hist_fq)):
        for k, multiplicity in histogram.items():
            factors_n = factor_integer(N)
            factors_k = factor_integer(k)
            for prime in set(factors_n) | set(factors_k):
                exponents[prime] += sign * multiplicity * k * k * (
                    2 * factors_n.get(prime, 0) - 2 * factors_k.get(prime, 0))
    expected = {2: 196608, 3: -9576, 5: 32800, 7: 4704,
                13: -21632, 29: 6728, 127: -32258}
    assert dict(sorted(exponents.items())) == expected
    positive = 1
    negative = 1
    for prime, exponent in exponents.items():
        if exponent > 0:
            positive *= prime ** exponent
        elif exponent < 0:
            negative *= prime ** (-exponent)
    assert positive < negative
    gap = collision_gap(f, q)
    assert gap < -0.12
    multiplier = tuple(2 * x - 1 for x in q)
    needed_activation_coefficient = -gap / eraw(multiplier)
    return (gap, needed_activation_coefficient, dict(sorted(exponents.items())),
            positive.bit_length(), negative.bit_length())


def main():
    collision_cases, minimum = exhaustive_affine_collision()
    signing_cases = exhaustive_signed_affine_formula()
    transverse_cases, largest_ratio = transverse_parity_controls()
    gap, coefficient, exponents, pos_bits, neg_bits = exact_x007_support_falsifier()
    print(f"exhaustive_affine_collision_cases={collision_cases}")
    print(f"minimum_affine_collision_gap={minimum:.17g}")
    print(f"exhaustive_signed_affine_formula_cases={signing_cases}")
    print(f"transverse_parity_signing_cases={transverse_cases}")
    print(f"largest_sampled_transverse_E_over_I={largest_ratio:.17g}")
    print("sharp_transverse_constant=4")
    print(f"x007_support_correction_gap={gap:.17g}")
    print(f"x007_minimum_H_activation_coefficient={coefficient:.17g}")
    print(f"x007_prime_exponents={exponents}")
    print(f"x007_integer_bitlengths=({pos_bits},{neg_bits})")
    print("full_FEI=OPEN")
    print("PASS")


if __name__ == "__main__":
    main()
