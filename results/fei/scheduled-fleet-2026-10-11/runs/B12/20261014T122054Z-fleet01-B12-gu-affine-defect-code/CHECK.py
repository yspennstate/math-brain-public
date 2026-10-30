#!/usr/bin/env python3
"""Exact-Walsh pilot for arbitrary affine-subspace defect sets."""

from fractions import Fraction
from functools import lru_cache
from math import log2


@lru_cache(maxsize=None)
def fwht(values):
    a = [Fraction(x) for x in values]
    h = 1
    while h < len(a):
        for s in range(0, len(a), 2 * h):
            for j in range(s, s + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    return tuple(x / len(a) for x in a)


@lru_cache(maxsize=None)
def law(values):
    return tuple(x * x for x in fwht(values))


def upper(p):
    z = list(p)
    n = len(p).bit_length() - 1
    for i in range(n):
        bit = 1 << i
        for s in range(1 << n):
            if not s & bit:
                z[s] += z[s | bit]
    return tuple(z)


@lru_cache(maxsize=None)
def U(values):
    p = law(values)
    pi = upper(p)
    return sum(float(x) * log2(float(y / x))
               for x, y in zip(p, pi) if x)


@lru_cache(maxsize=None)
def restrict_one(values, i, bit):
    n = len(values).bit_length() - 1
    return tuple(values[(z & ((1 << i) - 1)) | (bit << i) |
                        ((z >> i) << (i + 1))]
                 for z in range(1 << (n - 1)))


def G(values):
    n = len(values).bit_length() - 1
    return sum(U(values) - (U(restrict_one(values, i, 0)) +
                            U(restrict_one(values, i, 1))) / 2
               for i in range(n))


def I(values):
    return sum(Fraction(s.bit_count()) * p for s, p in enumerate(law(values)))


def span_add(space, v):
    return frozenset(space | {x ^ v for x in space})


def subspaces(n):
    seen = {frozenset({0})}
    frontier = list(seen)
    for space in frontier:
        for v in range(1, 1 << n):
            if v not in space:
                nxt = span_add(space, v)
                if nxt not in seen:
                    seen.add(nxt)
                    frontier.append(nxt)
    return seen


def affine_defect_from_annihilator(n, L, shift=0):
    E = {x for x in range(1 << n)
         if all(((x & t).bit_count() & 1) == 0 for t in L)}
    E = {x ^ shift for x in E}
    return tuple(-1 if x in E else 1 for x in range(1 << n))


def expected_law(n, L, shift=0):
    m = (len(L)).bit_length() - 1
    q = Fraction(4, 1 << (2 * m))
    p0 = Fraction(((1 << m) - 2) ** 2, 1 << (2 * m))
    return tuple(p0 if t == 0 else (q if t in L else Fraction(0))
                 for t in range(1 << n))


def heavy_entropy(m):
    p = (1 - 2 ** (1 - m)) ** 2
    return 0.0 if p == 0 else p * log2(1 / p)


def coloop_delta(m):
    q = 2 ** (2 - 2 * m)
    return (heavy_entropy(m) - 0.5 * heavy_entropy(m - 1) +
            q * (2 ** (m - 1) + m - 2))


def main():
    total = 0
    maximum = (-1e100, None)
    by_codim = {}
    coordinate_max = (-1e100, None)
    noncoloop_max = (-1e100, None)
    coloop_cases = noncoloop_cases = 0
    max_coloop_identity_error = 0.0
    for n in range(1, 7):
        spaces = subspaces(n)
        local = (-1e100, None)
        for L in spaces:
            m = len(L).bit_length() - 1
            if m == 0:
                continue  # constant -1
            f = affine_defect_from_annihilator(n, L)
            assert law(f) == expected_law(n, L)
            inf = I(f)
            if not inf:
                continue
            ratio = G(f) / float(inf)
            item = (ratio, (n, m, tuple(sorted(L)), U(f), G(f), float(inf)))
            maximum = max(maximum, item)
            local = max(local, item)
            by_codim[m] = max(by_codim.get(m, (-1e100, None)), item)
            root = U(f)
            for i in range(n):
                fi = Fraction(1, 1 << (m - 1)) if any(t & (1 << i) for t in L) else Fraction(0)
                if not fi:
                    continue
                delta = root - (U(restrict_one(f, i, 0)) +
                                U(restrict_one(f, i, 1))) / 2
                punctured = {((t & ((1 << i) - 1)) |
                              ((t >> (i + 1)) << i)) for t in L}
                coloop = len(punctured) == len(L) // 2
                ci = (delta / float(fi), (n, m, i, coloop, tuple(sorted(L))))
                coordinate_max = max(coordinate_max, ci)
                if coloop:
                    coloop_cases += 1
                    max_coloop_identity_error = max(
                        max_coloop_identity_error, abs(delta - coloop_delta(m)))
                else:
                    noncoloop_cases += 1
                    noncoloop_max = max(noncoloop_max, ci)
            total += 1
        print(f"n={n} subspaces={len(spaces)} max={local}")
    print(f"tested_nonconstant_subspaces={total}")
    print(f"overall_max={maximum}")
    print(f"by_codimension={by_codim}")
    print(f"coordinate_max={coordinate_max}")
    print(f"noncoloop_coordinate_max={noncoloop_max}")
    print(f"coloop_cases={coloop_cases}")
    print(f"noncoloop_cases={noncoloop_cases}")
    print(f"max_coloop_identity_error={max_coloop_identity_error:.17g}")


if __name__ == "__main__":
    main()
