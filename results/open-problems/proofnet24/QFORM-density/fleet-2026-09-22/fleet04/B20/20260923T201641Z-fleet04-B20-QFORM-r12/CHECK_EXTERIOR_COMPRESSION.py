#!/usr/bin/env python3
"""Deterministic numerical check of QFORM-ANCHORED-D3-EXTERIOR-COMPRESSION-v1."""

from itertools import combinations
from math import sqrt
from random import Random


def det2(a, b, c, d):
    return a * d - b * c


def det3(m):
    return (
        m[0][0] * det2(m[1][1], m[1][2], m[2][1], m[2][2])
        - m[0][1] * det2(m[1][0], m[1][2], m[2][0], m[2][2])
        + m[0][2] * det2(m[1][0], m[1][1], m[2][0], m[2][1])
    )


def trial(rng, nr, nc):
    b = rng.uniform(-3.0, 3.0)
    r = [rng.uniform(-3.0, 3.0) for _ in range(nc)]
    c = [rng.uniform(-3.0, 3.0) for _ in range(nr)]
    n = [[rng.uniform(-3.0, 3.0) for _ in range(nc)] for _ in range(nr)]

    j3 = 0.0
    for rows in combinations(range(nr), 2):
        for cols in combinations(range(nc), 2):
            mat = [
                [b, r[cols[0]], r[cols[1]]],
                [c[rows[0]], n[rows[0]][cols[0]], n[rows[0]][cols[1]]],
                [c[rows[1]], n[rows[1]][cols[0]], n[rows[1]][cols[1]]],
            ]
            j3 += det3(mat) ** 2

    e2 = 0.0
    for rows in combinations(range(nr), 2):
        for cols in combinations(range(nc), 2):
            e2 += det2(
                n[rows[0]][cols[0]], n[rows[0]][cols[1]],
                n[rows[1]][cols[0]], n[rows[1]][cols[1]],
            ) ** 2

    rf = sqrt(sum(x * x for x in r))
    cf = sqrt(sum(x * x for x in c))
    nf = sqrt(sum(x * x for row in n for x in row))
    rhs_root = abs(b) * sqrt(e2) + rf * cf * nf
    currency = max(b * b * e2, rf * rf * cf * cf * nf * nf)

    scale = max(1.0, j3, rhs_root * rhs_root, currency)
    assert sqrt(j3) <= rhs_root + 1e-10 * sqrt(scale)
    assert j3 <= 4.0 * currency + 1e-10 * scale


def main():
    rng = Random(20260923201641)
    for nr, nc in [(2, 2), (3, 4), (5, 3), (6, 7)]:
        for _ in range(100):
            trial(rng, nr, nc)
    delta_over_4 = 47045881 / (48 * 10**18)
    print("random exterior-compression checks: PASS")
    print(f"delta_over_4={delta_over_4:.16e}")


if __name__ == "__main__":
    main()
