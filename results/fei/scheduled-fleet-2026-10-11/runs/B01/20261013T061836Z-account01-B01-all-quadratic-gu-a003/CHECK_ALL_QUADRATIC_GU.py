#!/usr/bin/env python3
"""Exact diagnostic for GU'(3,0) on all quadratic Boolean phases.

The proof is analytic.  This exhausts every quadratic/linear coefficient
choice through five variables (output sign quotiented out), using integer
Walsh transforms and Fraction arithmetic.
"""

from fractions import Fraction


def fwht_int(values):
    a = list(values)
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2 * h):
            for j in range(i, i + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    return a


def quadratic_truth(n, edges, linear):
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    out = []
    for x in range(1 << n):
        bit = (linear & x).bit_count() & 1
        for k, (i, j) in enumerate(pairs):
            if ((edges >> k) & 1) and ((x >> i) & 1) and ((x >> j) & 1):
                bit ^= 1
        out.append(-1 if bit else 1)
    return tuple(out)


def restriction(values, i, bit):
    return tuple(v for x, v in enumerate(values) if ((x >> i) & 1) == bit)


def affine_support(values):
    w = fwht_int(values)
    support = tuple(i for i, z in enumerate(w) if z)
    magnitudes = {abs(w[i]) for i in support}
    assert len(magnitudes) == 1
    assert len(support) and not (len(support) & (len(support) - 1))
    return support


def upper_potential(values):
    support = affine_support(values)
    total = 0
    for x in support:
        count = sum((x & ~y) == 0 for y in support)
        assert count and not (count & (count - 1))
        total += count.bit_length() - 1
    return Fraction(total, len(support))


def entropy(values):
    return Fraction((len(affine_support(values))).bit_length() - 1)


def directional_influence(values, i):
    n = len(values).bit_length() - 1
    flips = sum(values[x] != values[x ^ (1 << i)] for x in range(1 << n))
    return Fraction(flips, 1 << n)


def metrics(values):
    n = len(values).bit_length() - 1
    u = upper_potential(values)
    infs = [directional_influence(values, i) for i in range(n)]
    charges = []
    for i in range(n):
        child = (upper_potential(restriction(values, i, 0)) +
                 upper_potential(restriction(values, i, 1))) / 2
        charges.append(u - child)
    return entropy(values), sum(infs, Fraction()), u, infs, charges


def main():
    grand = 0
    for n in range(1, 6):
        edge_count = n * (n - 1) // 2
        count = 0
        max_ratio = Fraction(-10)
        max_local_ratio = Fraction(-10)
        equality = 0
        witness = None
        for edges in range(1 << edge_count):
            for linear in range(1 << n):
                values = quadratic_truth(n, edges, linear)
                H, I, U, infs, charges = metrics(values)
                G = sum(charges, Fraction())
                assert U <= I
                assert H <= 2 * I
                assert G <= 3 * I
                for di, ii in zip(charges, infs):
                    assert di <= 3 * ii
                    if ii:
                        max_local_ratio = max(max_local_ratio, di / ii)
                if I:
                    ratio = G / I
                    if ratio > max_ratio:
                        max_ratio = ratio
                        witness = (edges, linear, G, I, U, H)
                    if G == 3 * I:
                        equality += 1
                count += 1
        grand += count
        print(
            f"n={n} cases={count} max_G_over_I={max_ratio} "
            f"max_Delta_over_Ii={max_local_ratio} equality_G_3I={equality} "
            f"witness={witness}"
        )
    print(f"total_cases={grand}")
    print("arithmetic=integer_Walsh_plus_exact_Fraction; upper_fibers_power_of_two")
    print("scope=all quadratic and linear coefficient choices through n=5; output sign quotiented")
    print("RESULT=PASS")


if __name__ == "__main__":
    main()
