#!/usr/bin/env python3
"""Exact/diagnostic checks for the dense nullity-two shield theorem.

All Walsh numerators and influences are integral/rational.  Floating logs
are used only to check the analytic entropy identities numerically.
"""

from fractions import Fraction
from itertools import product
from math import log2
from random import Random


def gf2_rank(rows, width):
    a = list(rows)
    out = 0
    for j in range(width):
        p = next((i for i in range(out, len(a)) if (a[i] >> j) & 1), None)
        if p is None:
            continue
        a[out], a[p] = a[p], a[out]
        for i in range(len(a)):
            if i != out and ((a[i] >> j) & 1):
                a[i] ^= a[out]
        out += 1
    return out


def fwht(a):
    a = list(a)
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2 * h):
            for j in range(i, i + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    return a


def entropy_from_walsh(w):
    n2 = len(w) ** 2
    return sum(-float(Fraction(x * x, n2)) * log2(float(Fraction(x * x, n2)))
               for x in w if x)


def influence_truth(vals):
    n = len(vals).bit_length() - 1
    N = len(vals)
    return sum(Fraction(sum(vals[x] != vals[x ^ (1 << j)] for x in range(N)), N)
               for j in range(n))


def fiber_inequalities():
    counts = {0: 0, 1: 0, 2: 0}
    for mask in range(16):
        f = [-1 if (mask >> x) & 1 else 1 for x in range(4)]
        h = entropy_from_walsh(fwht(f))
        inf = []
        for j in range(2):
            inf.append(Fraction(sum(f[x] != f[x ^ (1 << j)] for x in range(4)), 4))
        assert h <= 2 + 1e-12
        assert h <= 1 + 2 * float(inf[0]) + 1e-12
        assert h <= 2 * float(inf[0] + inf[1]) + 1e-12
        counts[sum(q > 0 for q in inf)] += 1
    return counts


def kernel_vectors(rows, m):
    return [y for y in range(1 << m)
            if all(((row & y).bit_count() & 1) == 0 for row in rows)]


def check_instance(rows, m, dvals):
    s = len(rows)
    r = gf2_rank(rows, m)
    assert m - r == 2
    vals = []
    for z in range(1 << (s + m)):
        x = z & ((1 << s) - 1)
        y = z >> s
        phase = 0
        for i, row in enumerate(rows):
            phase ^= ((x >> i) & 1) * ((row & y).bit_count() & 1)
        vals.append(dvals[y] * (-1 if phase else 1))
    h = entropy_from_walsh(fwht(vals))
    infl = influence_truth(vals)
    assert h <= 2 * float(infl) + 2e-10

    K = kernel_vectors(rows, m)
    assert len(K) == 4
    # Pick any basis of K and average the four-point fiber entropies.
    v1 = next(v for v in K if v)
    v2 = next(v for v in K if v and v != v1 and v != (0 ^ v1))
    seen = set()
    hs = []
    for y in range(1 << m):
        coset = frozenset((y, y ^ v1, y ^ v2, y ^ v1 ^ v2))
        if coset in seen:
            continue
        seen.add(coset)
        fib = [dvals[y], dvals[y ^ v1], dvals[y ^ v2], dvals[y ^ v1 ^ v2]]
        hs.append(entropy_from_walsh(fwht(fib)))
    assert abs(h - (2 * r + sum(hs) / len(hs))) < 2e-10
    return h, infl, sum(row == 0 for row in [
        sum((((rows[i] >> j) & 1) << i) for i in range(s)) for j in range(m)
    ])


def main():
    fiber_counts = fiber_inequalities()
    exhaustive = 0
    max_ratio = 0.0
    by_zero_columns = {0: 0, 1: 0, 2: 0}

    # Exhaust every rank-(m-2) matrix/core pair for m <= 3 and s <= 3.
    for m in (2, 3):
        r = m - 2
        for s in range(max(1, r), 4):
            for code in range(1 << (s * m)):
                rows = tuple((code >> (i * m)) & ((1 << m) - 1) for i in range(s))
                if gf2_rank(rows, m) != r:
                    continue
                for dmask in range(1 << (1 << m)):
                    d = [-1 if (dmask >> y) & 1 else 1 for y in range(1 << m)]
                    h, infl, z = check_instance(rows, m, d)
                    exhaustive += 1
                    by_zero_columns[z] += 1
                    if infl:
                        max_ratio = max(max_ratio, h / float(infl))

    # Deterministic larger diagnostics in dense and partially aligned cases.
    rng = Random(20261013)
    sampled = 0
    for m in range(4, 8):
        r = m - 2
        for _ in range(250):
            while True:
                rows = tuple(rng.randrange(1 << m) for _ in range(r + 2))
                if gf2_rank(rows, m) == r:
                    break
            d = [rng.choice((-1, 1)) for _ in range(1 << m)]
            h, infl, z = check_instance(rows, m, d)
            sampled += 1
            by_zero_columns[z] += 1
            max_ratio = max(max_ratio, h / float(infl))

    print("B05 A023 dense nullity-two shield check")
    print(f"two_bit_truth_tables=16 fiber_case_counts={fiber_counts}")
    print(f"exhaustive_matrix_core_instances={exhaustive}")
    print(f"sampled_larger_instances={sampled}")
    print(f"instances_by_zero_columns={by_zero_columns}")
    print(f"largest_H_over_I={max_ratio:.15f}")
    print("verified=H(P)=2r+average_fiber_H and H(P)<=2I(P)")
    print("PASS")


if __name__ == "__main__":
    main()
