#!/usr/bin/env python3
"""Deterministic checks for the full-star point-defect GU' class.

The proof in FULL_STAR_DEFECT_GU.md is analytic.  This script independently
checks the Fourier laws, restriction identities, G/I inequalities, and
disjoint-quadratic additivity on a bounded range.
"""

from __future__ import annotations

import json
import math


TOL = 2.0e-10


def fwht(values):
    out = [float(x) for x in values]
    n = len(out)
    h = 1
    while h < n:
        for i in range(0, n, 2 * h):
            for j in range(i, i + h):
                x, y = out[j], out[j + h]
                out[j], out[j + h] = x + y, x - y
        h *= 2
    return [x / n for x in out]


def upper_u(truth):
    p = [a * a for a in fwht(truth)]
    pi = p[:]
    m = len(p).bit_length() - 1
    for bit in range(m):
        step = 1 << bit
        for s in range(1 << m):
            if not (s & step):
                pi[s] += pi[s | step]
    return sum(x * math.log2(y / x) for x, y in zip(p, pi) if x > 0.0)


def entropy(truth):
    return sum(-p * math.log2(p) for a in fwht(truth) if (p := a * a) > 0.0)


def influence(truth):
    m = len(truth).bit_length() - 1
    N = len(truth)
    return sum(
        sum(truth[x] != truth[x ^ (1 << bit)] for x in range(N)) / N
        for bit in range(m)
    )


def coordinate_influences(truth):
    m = len(truth).bit_length() - 1
    N = len(truth)
    return [
        sum(truth[x] != truth[x ^ (1 << bit)] for x in range(N)) / N
        for bit in range(m)
    ]


def restrict(truth, bit, value):
    m = len(truth).bit_length() - 1
    out = []
    for y in range(1 << (m - 1)):
        lo = y & ((1 << bit) - 1)
        hi = y >> bit
        x = lo | (value << bit) | (hi << (bit + 1))
        out.append(truth[x])
    return out


def G(truth):
    m = len(truth).bit_length() - 1
    u = upper_u(truth)
    return sum(
        u - 0.5 * (upper_u(restrict(truth, bit, 0)) + upper_u(restrict(truth, bit, 1)))
        for bit in range(m)
    )


def defect(n):
    return [-1 if x == 0 else 1 for x in range(1 << n)]


def shifted_defect(n):
    return [((-1) ** x.bit_count()) * (-1 if x == 0 else 1) for x in range(1 << n)]


def full_star_defect(n):
    # Variable 0 is z; variables 1,...,n are the data bits.
    out = []
    for state in range(1 << (n + 1)):
        z = state & 1
        x = state >> 1
        d = -1 if x == 0 else 1
        out.append(d * ((-1) ** (z * (x.bit_count() & 1))))
    return out


def quadratic_phase(n, edge_mask, affine_mask=0, constant=0):
    edges = [(i, j) for i in range(n) for j in range(i + 1, n)]
    out = []
    for x in range(1 << n):
        e = constant ^ ((x & affine_mask).bit_count() & 1)
        for k, (i, j) in enumerate(edges):
            if (edge_mask >> k) & 1:
                e ^= ((x >> i) & 1) & ((x >> j) & 1)
        out.append(-1 if e else 1)
    return out


def tensor(a, b):
    # a occupies the low-order variables and b the high-order variables.
    return [a[x % len(a)] * b[x // len(a)] for x in range(len(a) * len(b))]


def assert_close(a, b, label, tol=TOL):
    if abs(a - b) > tol:
        raise AssertionError(f"{label}: {a} != {b}")


def main():
    star_rows = []
    max_star_ratio = 0.0
    for n in range(1, 11):
        f = full_star_defect(n)
        delta = 2.0 ** (-n)
        alpha = (0.5 - 2.0 * delta) ** 2
        eps = 4.0 * delta * delta
        got = sorted(a * a for a in fwht(f) if a * a > 1.0e-25)
        expected = sorted(x for x in [0.25, 0.25, alpha, alpha] + [eps] * (2**n - 2) if x > 1.0e-25)
        if len(got) != len(expected) or any(abs(x - y) > TOL for x, y in zip(got, expected)):
            raise AssertionError(f"full-star spectrum mismatch at n={n}")
        for j, val in enumerate(coordinate_influences(f)):
            assert_close(val, 0.5, f"Inf_{j}(F_{n})")
        h, u, g, inf = entropy(f), upper_u(f), G(f), influence(f)
        if h > 4.0 + TOL or u > h + TOL or g > 8.0 * inf + TOL:
            raise AssertionError(f"full-star inequality failed at n={n}")
        max_star_ratio = max(max_star_ratio, g / inf)
        star_rows.append({"n": n, "H": h, "U": u, "G": g, "I": inf, "G_over_I": g / inf})

        # Restriction identities defining the closure.
        if restrict(f, 0, 0) != defect(n):
            raise AssertionError(f"z=0 restriction mismatch at n={n}")
        if restrict(f, 0, 1) != shifted_defect(n):
            raise AssertionError(f"z=1 restriction mismatch at n={n}")
        if n >= 2:
            if restrict(f, 1, 0) != full_star_defect(n - 1):
                raise AssertionError(f"x_1=0 restriction mismatch at n={n}")
            # x_1=1: (-1)^[z(1+sum remaining x)], a quadratic phase.
            expected_q = []
            for state in range(1 << n):
                z = state & 1
                x = state >> 1
                expected_q.append((-1) ** (z * (1 + x.bit_count())))
            if restrict(f, 1, 1) != expected_q:
                raise AssertionError(f"x_1=1 restriction mismatch at n={n}")
            if G(expected_q) > 3.0 * influence(expected_q) + TOL:
                raise AssertionError(f"quadratic child bound failed at n={n}")

    defect_rows = []
    shifted_rows = []
    for n in range(1, 15):
        d = defect(n)
        sd = shifted_defect(n)
        for name, f, rows in [("defect", d, defect_rows), ("shifted", sd, shifted_rows)]:
            h, u, g, inf = entropy(f), upper_u(f), G(f), influence(f)
            if g > 8.0 * inf + TOL:
                raise AssertionError(f"{name} G<=8I failed at n={n}")
            rows.append({"n": n, "H": h, "U": u, "G": g, "I": inf,
                         "G_over_I": None if inf == 0 else g / inf})

    # Exhaustive disjoint quadratic transfer for w<=3 and star n<=4.
    transfer_cases = 0
    max_additivity_error = 0.0
    for w in range(0, 4):
        edge_count = w * (w - 1) // 2
        for edge_mask in range(1 << edge_count):
            for affine_mask in range(1 << w):
                q = quadratic_phase(w, edge_mask, affine_mask)
                for n in range(1, 5):
                    f = full_star_defect(n)
                    qf = tensor(q, f)
                    errs = [
                        abs(upper_u(qf) - upper_u(q) - upper_u(f)),
                        abs(G(qf) - G(q) - G(f)),
                        abs(influence(qf) - influence(q) - influence(f)),
                    ]
                    max_additivity_error = max(max_additivity_error, *errs)
                    if max(errs) > 2.0e-9:
                        raise AssertionError(f"tensor additivity failed w={w}, n={n}")
                    if G(qf) > 8.0 * influence(qf) + 2.0e-9:
                        raise AssertionError(f"transferred class bound failed w={w}, n={n}")
                    transfer_cases += 1

    result = {
        "status": "PASS",
        "full_star_dimensions_checked": [1, 10],
        "defect_dimensions_checked": [1, 14],
        "disjoint_quadratic_transfer_cases": transfer_cases,
        "maximum_full_star_G_over_I": max_star_ratio,
        "maximum_tensor_additivity_error": max_additivity_error,
        "sample_full_star_rows": star_rows,
        "sample_defect_rows": defect_rows,
        "sample_shifted_rows": shifted_rows,
        "scope": "finite deterministic verification only; the theorem is proved analytically in FULL_STAR_DEFECT_GU.md",
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
