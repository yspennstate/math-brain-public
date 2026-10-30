#!/usr/bin/env python3
"""Exact/floating verification of GU character-core overlap factorization."""

from fractions import Fraction
from itertools import product
from math import log2
import random

SEED = 0xB12A05802
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
    return [x / len(a) for x in a]


def spectral_law(values):
    return [c * c for c in fwht(values)]


def upper_masses(p):
    z = list(p)
    n = len(p).bit_length() - 1
    for i in range(n):
        bit = 1 << i
        for s in range(1 << n):
            if not (s & bit):
                z[s] += z[s | bit]
    return z


def u_value(values):
    p = spectral_law(values)
    pi = upper_masses(p)
    return sum(float(x) * log2(float(y / x))
               for x, y in zip(p, pi) if x)


def influence(values):
    n = len(values).bit_length() - 1
    p = spectral_law(values)
    return sum(Fraction(mask.bit_count()) * mass
               for mask, mass in enumerate(p))


def restrict(values, i, bit):
    n = len(values).bit_length() - 1
    return tuple(values[(z & ((1 << i) - 1)) | (bit << i) |
                        ((z >> i) << (i + 1))]
                 for z in range(1 << (n - 1)))


def g_value(values):
    n = len(values).bit_length() - 1
    parent = u_value(values)
    return sum(parent - 0.5 * (u_value(restrict(values, i, 0)) +
                               u_value(restrict(values, i, 1)))
               for i in range(n))


def direct_character_product(shared_bits, masks, residuals):
    widths = [len(f).bit_length() - 1 for f in residuals]
    offsets = []
    total = shared_bits
    for width in widths:
        offsets.append(total)
        total += width
    out = []
    for x in range(1 << total):
        value = 1
        shared = x & ((1 << shared_bits) - 1)
        for mask, f, width, offset in zip(masks, residuals, widths, offsets):
            if (shared & mask).bit_count() & 1:
                value = -value
            value *= f[(x >> offset) & ((1 << width) - 1)]
        out.append(value)
    return tuple(out)


def check_case(shared_bits, masks, residuals):
    f = direct_character_product(shared_bits, masks, residuals)
    xor_mask = 0
    for mask in masks:
        xor_mask ^= mask
    lhs_u = u_value(f)
    rhs_u = sum(u_value(q) for q in residuals)
    lhs_g = g_value(f)
    rhs_g = sum(g_value(q) for q in residuals)
    lhs_i = influence(f)
    rhs_i = Fraction(xor_mask.bit_count()) + sum(influence(q) for q in residuals)
    assert abs(lhs_u - rhs_u) <= TOL
    assert abs(lhs_g - rhs_g) <= TOL
    assert lhs_i == rhs_i

    # A deliberately non-optimal frozen pair inferred from the factors.
    # This tests the algebraic closure implication, not universal GU.
    b = 0.5
    a = max(((g_value(q) - b * u_value(q)) / float(influence(q))
             for q in residuals if influence(q)), default=0.0)
    a = max(a, 0.0)
    assert lhs_g <= a * float(lhs_i) + b * lhs_u + TOL
    return lhs_u, lhs_g, float(lhs_i), xor_mask.bit_count()


def main():
    one_bit = list(product((-1, 1), repeat=2))
    exhaustive = 0
    max_u_error = 0.0
    max_g_error = 0.0
    max_dimension = 0
    cancellation_cases = 0

    for shared in range(3):
        masks = list(range(1 << shared))
        for factors in range(1, 4):
            for chosen_masks in product(masks, repeat=factors):
                for residuals in product(one_bit, repeat=factors):
                    f = direct_character_product(shared, chosen_masks, residuals)
                    u0, g0, _, core = check_case(shared, chosen_masks, residuals)
                    max_u_error = max(max_u_error,
                                      abs(u0 - sum(u_value(q) for q in residuals)))
                    max_g_error = max(max_g_error,
                                      abs(g0 - sum(g_value(q) for q in residuals)))
                    max_dimension = max(max_dimension, len(f).bit_length() - 1)
                    total_appearances = sum(mask.bit_count() for mask in chosen_masks)
                    cancellation_cases += core < total_appearances
                    exhaustive += 1

    rng = random.Random(SEED)
    random_cases = 3000
    for _ in range(random_cases):
        shared = rng.randint(0, 4)
        factors = rng.randint(1, 4)
        widths = [rng.randint(1, 2) for _ in range(factors)]
        while shared + sum(widths) > 12:
            widths[-1] = 1
            if shared + sum(widths) <= 12:
                break
            factors -= 1
            widths = widths[:factors]
        masks = [rng.randrange(1 << shared) for _ in range(factors)]
        residuals = [tuple(rng.choice((-1, 1)) for _ in range(1 << w))
                     for w in widths]
        f = direct_character_product(shared, masks, residuals)
        u0, g0, _, _ = check_case(shared, masks, residuals)
        max_u_error = max(max_u_error,
                          abs(u0 - sum(u_value(q) for q in residuals)))
        max_g_error = max(max_g_error,
                          abs(g0 - sum(g_value(q) for q in residuals)))
        max_dimension = max(max_dimension, len(f).bit_length() - 1)

    # Exact deterministic-core check: all spectral sets have the XOR core.
    residuals = [(-1, -1, -1, 1), (-1, 1), (1, 1, -1, 1)]
    masks = [0b1111, 0b1011, 0b0110]
    f = direct_character_product(4, masks, residuals)
    core = masks[0] ^ masks[1] ^ masks[2]
    support = [s for s, p in enumerate(spectral_law(f)) if p]
    assert all((s & 0b1111) == core for s in support)

    print("STATUS PASS")
    print(f"seed={SEED}")
    print(f"exhaustive_cases={exhaustive}")
    print(f"random_cases={random_cases}")
    print(f"cancellation_cases={cancellation_cases}")
    print(f"maximum_dimension={max_dimension}")
    print(f"max_U_factorization_error={max_u_error:.17g}")
    print(f"max_G_factorization_error={max_g_error:.17g}")
    print(f"deterministic_core={core:04b}")
    print(f"deterministic_core_support_size={len(support)}")
    print("universal_GU=OPEN")


if __name__ == "__main__":
    main()
