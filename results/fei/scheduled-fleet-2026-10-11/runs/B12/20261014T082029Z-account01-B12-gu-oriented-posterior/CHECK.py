#!/usr/bin/env python3
"""Verify the oriented posterior decomposition and rare-activation laws."""

from fractions import Fraction
from functools import lru_cache
from itertools import product
from math import log2, log
import random

SEED = 0xB12A05806
TOL = 8e-10


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
            if not (s & bit):
                z[s] += z[s | bit]
    return tuple(z)


@lru_cache(maxsize=None)
def u_value(values):
    p = spectral_law(values)
    pi = upper_masses(p)
    return sum(float(x) * log2(float(y / x))
               for x, y in zip(p, pi) if x)


@lru_cache(maxsize=None)
def influence(values):
    return sum(Fraction(s.bit_count()) * x
               for s, x in enumerate(spectral_law(values)))


@lru_cache(maxsize=None)
def restrict_one(values, i, bit):
    n = len(values).bit_length() - 1
    return tuple(values[(z & ((1 << i) - 1)) | (bit << i) |
                        ((z >> i) << (i + 1))]
                 for z in range(1 << (n - 1)))


@lru_cache(maxsize=None)
def g_value(values):
    n = len(values).bit_length() - 1
    return sum(u_value(values) - 0.5 * (
        u_value(restrict_one(values, i, 0)) +
        u_value(restrict_one(values, i, 1))) for i in range(n))


def endpoint_xlog_ratio(weight, numerator, denominator):
    if weight == 0:
        return 0.0
    return float(weight) * log2(float(numerator / denominator))


@lru_cache(maxsize=None)
def pair_terms(fplus, fminus):
    pp = spectral_law(fplus)
    pm = spectral_law(fminus)
    up = upper_masses(pp)
    um = upper_masses(pm)
    mix = kl = orient = 0.0
    for xp, xm, yp, ym in zip(pp, pm, up, um):
        q = (xp + xm) / 2
        m = (yp + ym) / 2
        if not q:
            continue
        mix += float(q) * log2(float(m / q))
        rp = xp / (2 * q)
        rm = xm / (2 * q)
        sp = yp / (2 * m)
        sm = ym / (2 * m)
        kl += endpoint_xlog_ratio(q * rp, rp, sp)
        kl += endpoint_xlog_ratio(q * rm, rm, sm)
        t = rp - rm
        L = log2(float(m / q))
        omega = float(t) * L
        omega += endpoint_xlog_ratio(rp, sp, rp)
        omega -= endpoint_xlog_ratio(rm, sm, rm)
        orient += float(q) * omega
    return mix, kl, orient


def pair_laplacians(fplus, fminus):
    root = pair_terms(fplus, fminus)
    n = len(fplus).bit_length() - 1
    out = [0.0, 0.0, 0.0]
    for i in range(n):
        children = [pair_terms(restrict_one(fplus, i, bit),
                               restrict_one(fminus, i, bit))
                    for bit in (0, 1)]
        for j in range(3):
            out[j] += root[j] - 0.5 * (children[0][j] + children[1][j])
    return tuple(out)


def defect(f, a, b):
    return g_value(f) - a * float(influence(f)) - b * u_value(f)


def verify_pair(fplus, fminus, frozen_pairs):
    mix, kl, zu = pair_terms(fplus, fminus)
    lm, lk, lzu = pair_laplacians(fplus, fminus)
    assert abs(u_value(fplus) - (mix - kl + zu)) <= TOL
    assert abs(u_value(fminus) - (mix - kl - zu)) <= TOL
    assert abs(g_value(fplus) - (lm - lk + lzu)) <= TOL
    assert abs(g_value(fminus) - (lm - lk - lzu)) <= TOL
    avg_i = 0.5 * (float(influence(fplus)) + float(influence(fminus)))
    zi = 0.5 * (float(influence(fplus)) - float(influence(fminus)))
    max_error = 0.0
    for a, b in frozen_pairs:
        center = lm - a * avg_i - b * mix + b * kl - lk
        oriented = lzu - a * zi - b * zu
        ep = abs(defect(fplus, a, b) - (center + oriented))
        em = abs(defect(fminus, a, b) - (center - oriented))
        max_error = max(max_error, ep, em)
        assert ep <= TOL and em <= TOL
    swapped = pair_terms(fminus, fplus)
    assert abs(swapped[0] - mix) <= TOL
    assert abs(swapped[1] - kl) <= TOL
    assert abs(swapped[2] + zu) <= TOL
    return max_error


def rare_u(n):
    N = 1 << n
    p0 = ((N - 2) / N) ** 2
    first = 0.0 if p0 == 0 else p0 * log2(1 / p0)
    return first + 4 / (N * N) * (n * (1 << (n - 1)) - n)


def rare_k(n):
    N = 1 << n
    p0 = ((N - 2) / N) ** 2
    first = 0.0 if p0 == 0 else p0 * log2(2 * p0 / (1 + p0))
    return 0.5 * (first + log2(2 / (1 + p0)))


def rare_g(n):
    return n * (rare_u(n) - 0.5 * rare_u(n - 1))


def rare_lk(n):
    return n * (rare_k(n) - 0.5 * rare_k(n - 1))


def main():
    frozen_pairs = ((0.0, 0.0), (4.0, 0.5), (6.0, 0.25))
    exhaustive_pairs = 0
    max_error = 0.0
    for n in range(1, 4):
        functions = list(product((-1, 1), repeat=1 << n))
        for fplus in functions:
            for fminus in functions:
                max_error = max(max_error,
                                verify_pair(fplus, fminus, frozen_pairs))
                exhaustive_pairs += 1

    rng = random.Random(SEED)
    random_pairs = 240
    maximum_dimension = 3
    for _ in range(random_pairs):
        n = rng.randint(4, 7)
        fplus = tuple(rng.choice((-1, 1)) for _ in range(1 << n))
        fminus = tuple(rng.choice((-1, 1)) for _ in range(1 << n))
        max_error = max(max_error, verify_pair(fplus, fminus, frozen_pairs))
        maximum_dimension = max(maximum_dimension, n)

    # Direct checks of the rare family against the closed forms.
    rare_lines = []
    last_zu_ratio = last_zg_ratio = 0.0
    for n in range(2, 13):
        N = 1 << n
        fplus = tuple([1] * (N - 1) + [-1])
        fminus = tuple([1] * N)
        mix, kl, zu = pair_terms(fplus, fminus)
        lm, lk, lzu = pair_laplacians(fplus, fminus)
        assert abs(u_value(fplus) - rare_u(n)) <= TOL
        assert abs(kl - rare_k(n)) <= TOL
        assert abs(g_value(fplus) - rare_g(n)) <= TOL
        assert abs(lk - rare_lk(n)) <= TOL
        assert abs(zu - rare_u(n) / 2) <= TOL
        assert abs(lzu - rare_g(n) / 2) <= TOL
        zi = n / N
        last_zu_ratio = abs(zu) / kl
        last_zg_ratio = abs(lzu) / (kl + abs(lk))
        rare_lines.append(
            f"rare_n={n},K={kl:.17g},LK={lk:.17g},"
            f"ZU={zu:.17g},LZU={lzu:.17g},ZI={zi:.17g},"
            f"ZU_over_K={last_zu_ratio:.17g},"
            f"LZU_over_K_plus_absLK={last_zg_ratio:.17g}")

    # Closed-form large-n asymptotic controls without constructing the cube.
    n = 30
    N = 1 << n
    k_scaled = rare_k(n) * N * N
    zu_scaled = (rare_u(n) / 2) * N / n
    lk_scaled = rare_lk(n) * N * N / n
    lzu_scaled = (rare_g(n) / 2) * N / n
    assert abs(k_scaled - 2 / log(2)) < 2e-5
    assert abs(zu_scaled - 1) < 0.11
    assert abs(lk_scaled + 2 / log(2)) < 2e-5
    assert abs(lzu_scaled - 1) < 2e-6

    print("STATUS PASS")
    print(f"seed={SEED}")
    print(f"exhaustive_boolean_pairs={exhaustive_pairs}")
    print(f"random_boolean_pairs={random_pairs}")
    print(f"maximum_dimension={maximum_dimension}")
    print(f"maximum_defect_decomposition_error={max_error:.17g}")
    print(f"n12_ZU_over_K={last_zu_ratio:.17g}")
    print(f"n12_LZU_over_K_plus_absLK={last_zg_ratio:.17g}")
    print(f"n30_N2K={k_scaled:.17g}")
    print(f"n30_NZU_over_n={zu_scaled:.17g}")
    print(f"n30_N2LK_over_n={lk_scaled:.17g}")
    print(f"n30_NLZU_over_n={lzu_scaled:.17g}")
    for line in rare_lines:
        print(line)
    print("posterior_only_projection=REFUTED")
    print("universal_GU=OPEN")


if __name__ == "__main__":
    main()
