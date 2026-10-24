#!/usr/bin/env python3
"""Exact-Walsh pilot for three exceptional points and coordinate GU decrements."""

from fractions import Fraction
from functools import lru_cache
from math import log2


@lru_cache(maxsize=None)
def fwht(values):
    a = [Fraction(x) for x in values]
    h = 1
    while h < len(a):
        for start in range(0, len(a), 2 * h):
            for j in range(start, start + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    return tuple(x / len(a) for x in a)


@lru_cache(maxsize=None)
def spectral_law(values):
    return tuple(x * x for x in fwht(values))


def upper_masses(p):
    z = list(p)
    n = len(p).bit_length() - 1
    for i in range(n):
        bit = 1 << i
        for s in range(1 << n):
            if not s & bit:
                z[s] += z[s | bit]
    return tuple(z)


@lru_cache(maxsize=None)
def u_value(values):
    p = spectral_law(values)
    pi = upper_masses(p)
    return sum(float(x) * log2(float(y / x))
               for x, y in zip(p, pi) if x)


@lru_cache(maxsize=None)
def restrict_one(values, i, bit):
    n = len(values).bit_length() - 1
    return tuple(values[(z & ((1 << i) - 1)) | (bit << i) |
                        ((z >> i) << (i + 1))]
                 for z in range(1 << (n - 1)))


def three_defect(n, a, b, c, mask=0):
    # Coordinate blocks: u-only, v-only, shared.
    u = ((1 << a) - 1) | (((1 << c) - 1) << (a + b))
    v = (((1 << b) - 1) << a) | (((1 << c) - 1) << (a + b))
    return tuple((-1 if (x & mask).bit_count() & 1 else 1) *
                 (-1 if x in (0, u, v) else 1)
                 for x in range(1 << n))


def rank2_expected(n, a, b, c, mask):
    N = 1 << n
    u = ((1 << a) - 1) | (((1 << c) - 1) << (a + b))
    v = (((1 << b) - 1) << a) | (((1 << c) - 1) << (a + b))
    p0 = Fraction((N - 6) ** 2, N * N)
    q = Fraction(4, N * N)
    law = []
    for T in range(N):
        R = T ^ mask
        high = ((R & u).bit_count() % 2 == 0 and
                (R & v).bit_count() % 2 == 0)
        law.append(p0 if T == mask else (9 * q if high else q))
    pi = []
    for S in range(N):
        free = [j for j in range(n) if not S & (1 << j)]
        count = 0
        for bits in range(1 << len(free)):
            T = S
            for k, j in enumerate(free):
                if bits & (1 << k):
                    T |= 1 << j
            R = T ^ mask
            count += ((R & u).bit_count() % 2 == 0 and
                      (R & v).bit_count() % 2 == 0)
        heavy = p0 - 9 * q if (S | mask) == mask else 0
        pi.append(q * (1 << (n - S.bit_count())) + 8 * q * count + heavy)
    return tuple(law), tuple(pi)


def coordinate_influence(values, i):
    n = len(values).bit_length() - 1
    return Fraction(sum(values[x] != values[x ^ (1 << i)]
                        for x in range(1 << n)), 1 << n)


def main():
    overall = (-1e100, None)
    aggregate = (-1e100, None)
    cases = 0
    grouped = {"u": (-1e100, None), "v": (-1e100, None),
               "shared": (-1e100, None)}
    kernel_cases = 0
    for n in range(2, 6):
        for a in range(n + 1):
            for b in range(n - a + 1):
                c = n - a - b
                if min(a + c, b + c, a + b) == 0:
                    continue
                for mask in range(1 << n):
                    f = three_defect(n, a, b, c, mask)
                    law, pi = rank2_expected(n, a, b, c, mask)
                    assert spectral_law(f) == law
                    assert upper_masses(law) == pi
                    kernel_cases += 1
    for n in range(2, 13):
        local = (-1e100, None)
        for a in range(n + 1):
            for b in range(n - a + 1):
                c = n - a - b
                if min(a + c, b + c, a + b) == 0:
                    continue
                f = three_defect(n, a, b, c)
                root = u_value(f)
                total_delta = 0.0
                total_i = Fraction(0)
                for i in range(n):
                    delta = root - 0.5 * (u_value(restrict_one(f, i, 0)) +
                                          u_value(restrict_one(f, i, 1)))
                    inf = coordinate_influence(f, i)
                    ratio = delta / float(inf)
                    item = (ratio, (n, a, b, c, i, delta, float(inf)))
                    local = max(local, item)
                    overall = max(overall, item)
                    total_delta += delta
                    total_i += inf
                    cases += 1
                    kind = "u" if i < a else ("v" if i < a + b else "shared")
                    grouped[kind] = max(grouped[kind], item)
                agg = total_delta / float(total_i)
                aggregate = max(aggregate, (agg, (n, a, b, c,
                                                   total_delta, float(total_i))))
        print(f"n={n} coordinate_max={local}")
    print(f"coordinate_cases={cases}")
    print(f"exact_rank2_kernel_cases={kernel_cases}")
    print(f"overall_coordinate_max={overall}")
    print(f"overall_aggregate_max={aggregate}")
    print(f"grouped_coordinate_max={grouped}")


if __name__ == "__main__":
    main()
