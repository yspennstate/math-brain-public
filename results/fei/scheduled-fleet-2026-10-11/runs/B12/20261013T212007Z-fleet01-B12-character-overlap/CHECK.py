#!/usr/bin/env python3
"""Finite controls for the character-overlap theorem and shared-potential no-go."""

from fractions import Fraction
from itertools import product
from math import log2
import random

SEED = 0xB12A058
TOL = 4e-12


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


def raw_entropy(values):
    return sum(float(a * a) * log2(1.0 / float(a * a))
               for a in fwht(values) if a)


def influence(values):
    n = len(values).bit_length() - 1
    return sum(Fraction(sum(values[x] != values[x ^ (1 << i)]
                            for x in range(len(values))), len(values))
               for i in range(n))


def restrict(values, i, bit):
    n = len(values).bit_length() - 1
    return tuple(values[(z & ((1 << i) - 1)) | (bit << i) |
                        ((z >> i) << (i + 1))]
                 for z in range(1 << (n - 1)))


def decrement(values, i):
    return raw_entropy(values) - 0.5 * (
        raw_entropy(restrict(values, i, 0)) +
        raw_entropy(restrict(values, i, 1)))


def direct_character_product(shared_bits, masks, residuals):
    widths = [len(f).bit_length() - 1 for f in residuals]
    offsets = []
    k = shared_bits
    for width in widths:
        offsets.append(k)
        k += width
    out = []
    for x in range(1 << k):
        value = 1
        shared = x & ((1 << shared_bits) - 1)
        for mask, f, width, offset in zip(masks, residuals, widths, offsets):
            if (shared & mask).bit_count() & 1:
                value = -value
            value *= f[(x >> offset) & ((1 << width) - 1)]
        out.append(value)
    return tuple(out)


def check_character_case(shared_bits, masks, residuals):
    f = direct_character_product(shared_bits, masks, residuals)
    xor_mask = 0
    for mask in masks:
        xor_mask ^= mask
    expected_h = sum(raw_entropy(g) for g in residuals)
    expected_i = xor_mask.bit_count() + sum(influence(g) for g in residuals)
    assert abs(raw_entropy(f) - expected_h) <= TOL
    assert influence(f) == expected_i

    ratios = [raw_entropy(g) / float(influence(g))
              for g in residuals if influence(g)]
    c = max(ratios, default=0.0)
    assert raw_entropy(f) <= c * float(influence(f)) + TOL
    return raw_entropy(f), float(influence(f))


def corrected_potential(u, v, h):
    a = tuple(Fraction(x + y, 2) for x, y in zip(u, v))
    b = tuple(Fraction(y - x, 2) for x, y in zip(u, v))
    hb = tuple(s * t for s, t in zip(h, b))
    f = tuple(x + y for x, y in zip(a, hb))
    return raw_entropy(f) - raw_entropy(hb) + raw_entropy(b)


def explicit_shared_witness():
    u = (-1, -1, -1, -1, -1, 1, -1, -1)
    v = (1, 1, 1, -1, 1, 1, 1, 1)
    h = (-1, 1, -1, 1, -1, 1, -1, -1)
    a = tuple(Fraction(x + y, 2) for x, y in zip(u, v))
    b = tuple(Fraction(y - x, 2) for x, y in zip(u, v))
    hb = tuple(s * t for s, t in zip(h, b))
    f = tuple(x + y for x, y in zip(a, hb))
    i = 2

    assert decrement(f, i) == 0.0
    assert decrement(a, i) == 0.0
    assert decrement(b, i) == 0.0
    exact_drop = 1.25 - (9.0 / 16.0) * log2(16.0 / 9.0)
    assert abs(decrement(hb, i) - exact_drop) <= TOL
    parent = corrected_potential(u, v, h)
    children = 0.5 * sum(corrected_potential(restrict(u, i, t),
                                              restrict(v, i, t),
                                              restrict(h, i, t))
                         for t in (0, 1))
    assert abs(parent - children + exact_drop) <= TOL
    assert exact_drop > 11.0 / 16.0
    return parent - children, exact_drop


def exhaustive_two_bit_potential():
    signs = list(product((-1, 1), repeat=4))
    minimum = float("inf")
    negative = 0
    cases = 0
    for u in signs:
        for v in signs:
            for h in signs:
                parent = corrected_potential(u, v, h)
                for i in range(2):
                    child = 0.5 * sum(corrected_potential(restrict(u, i, t),
                                                          restrict(v, i, t),
                                                          restrict(h, i, t))
                                      for t in (0, 1))
                    drop = parent - child
                    minimum = min(minimum, drop)
                    negative += drop < -TOL
                    cases += 1
    return cases, minimum, negative


def main():
    one_bit = list(product((-1, 1), repeat=2))
    exhaustive = 0
    max_h = 0.0
    max_i = 0.0
    for shared in range(4):
        masks = list(range(1 << shared))
        for factors in range(1, 4):
            for chosen_masks in product(masks, repeat=factors):
                for residuals in product(one_bit, repeat=factors):
                    h, i = check_character_case(shared, chosen_masks, residuals)
                    max_h = max(max_h, h); max_i = max(max_i, i)
                    exhaustive += 1

    rng = random.Random(SEED)
    random_cases = 5000
    for _ in range(random_cases):
        shared = rng.randint(0, 4)
        factors = rng.randint(1, 5)
        widths = [rng.randint(1, 2) for _ in range(factors)]
        while shared + sum(widths) > 14:
            widths[-1] = 1
            if shared + sum(widths) <= 14:
                break
            factors -= 1
            widths = widths[:factors]
        masks = [rng.randrange(1 << shared) for _ in range(factors)]
        residuals = [tuple(rng.choice((-1, 1)) for _ in range(1 << w))
                     for w in widths]
        h, i = check_character_case(shared, masks, residuals)
        max_h = max(max_h, h); max_i = max(max_i, i)

    potential_cases, min_two_bit, negative_two_bit = exhaustive_two_bit_potential()
    witness_drop, witness_exact = explicit_shared_witness()

    print(f"seed={SEED}")
    print(f"exhaustive_character_overlap_cases={exhaustive}")
    print(f"random_character_overlap_cases={random_cases}")
    print(f"maximum_checked_entropy={max_h:.17g}")
    print(f"maximum_checked_influence={max_i:.17g}")
    print("character_overlap_exact_laws=PASS")
    print(f"two_bit_shared_potential_decrements={potential_cases}")
    print(f"two_bit_minimum_corrected_potential_decrement={min_two_bit:.17g}")
    print(f"two_bit_negative_decrements={negative_two_bit}")
    print(f"three_bit_certified_negative_decrement={witness_drop:.17g}")
    print(f"three_bit_exact_loss={witness_exact:.17g}")
    print("full_FEI=OPEN")
    print("PASS")


if __name__ == "__main__":
    main()
