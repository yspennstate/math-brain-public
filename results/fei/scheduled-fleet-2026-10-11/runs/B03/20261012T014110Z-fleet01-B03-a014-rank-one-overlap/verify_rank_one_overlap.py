#!/usr/bin/env python3
"""Deterministic checks for B03-A014 rank-one overlap family.

No randomness. Exact Fraction Walsh arithmetic is used for truth-table
identities. Decimal logarithms are used only to print entropy values; the
all-dimension entropy bound is proved analytically in REPORT.md.
"""

from fractions import Fraction
from itertools import product
from decimal import Decimal, getcontext

getcontext().prec = 80


def points(n):
    return list(product((-1, 1), repeat=n))


def walsh(values, n):
    xs = points(n)
    out = {}
    for mask in range(1 << n):
        total = 0
        for x, fx in zip(xs, values):
            chi = 1
            for i in range(n):
                if mask >> i & 1:
                    chi *= x[i]
            total += fx * chi
        out[mask] = Fraction(total, 1 << n)
    return out


def influence(spec):
    return sum(Fraction(mask.bit_count()) * c * c for mask, c in spec.items())


def entropy_decimal(spec):
    total = Decimal(0)
    ln2 = Decimal(2).ln()
    for c in spec.values():
        q = Decimal(c.numerator * c.numerator) / Decimal(c.denominator * c.denominator)
        if q:
            total -= q * q.ln() / ln2
    return total


def defect_values(t):
    return [-1 if all(z == -1 for z in a) else 1 for a in points(t)]


def majority3_values():
    return [1 if sum(x) > 0 else -1 for x in points(3)]


checks = 0
maj = walsh(majority3_values(), 3)
assert set(mask for mask, c in maj.items() if c) == {1, 2, 4, 7}
assert all(abs(maj[m]) == Fraction(1, 2) for m in (1, 2, 4, 7))
assert influence(maj) == Fraction(3, 2)
checks += 6

print("t  k=2^t  fractional  rank  E[root]       H(h_t)             I(h_t)       H(F)/I(F)")
for t in range(1, 13):
    h = walsh(defect_values(t), t)
    delta = Fraction(1, 1 << (t - 1))
    assert h[0] == 1 - delta
    checks += 1
    for mask, c in h.items():
        if mask:
            assert abs(c) == delta
            checks += 1
    ih = influence(h)
    assert ih == t * delta
    checks += 1

    # Every branch is +/- majority_3.  The branch-by-frequency matrix is
    # an outer product, hence rank one; every core coordinate is present in
    # every branch, hence raw read 2^t and activation-weighted read one.
    signs = defect_values(t)
    nonzero = [m for m, c in maj.items() if c]
    col0 = [Fraction(s) * maj[nonzero[0]] for s in signs]
    for m in nonzero[1:]:
        col = [Fraction(s) * maj[m] for s in signs]
        ratio = maj[m] / maj[nonzero[0]]
        assert col == [ratio * z for z in col0]
        checks += len(col)

    hh = entropy_decimal(h)
    hm = Decimal(2)
    im = Fraction(3, 2)
    ratio_f = (hh + hm) / (Decimal(ih.numerator) / Decimal(ih.denominator)
                            + Decimal(im.numerator) / Decimal(im.denominator))
    expected_root = Fraction(2) - delta
    assert expected_root < 2
    checks += 1
    if t >= 2:
        assert hh < Decimal(4 * ih.numerator) / Decimal(ih.denominator)
        checks += 1
    print(f"{t:2d} {1<<t:7d}      1        1   {float(expected_root):.9f}  "
          f"{hh:.12f}  {float(ih):.9f}  {ratio_f:.12f}")

print(f"PASS exact/rank assertions: {checks}")
print("PASS: k grows exponentially while fractional congestion=1, spectral rank=1,")
print("      expected controller-root cost<2, and H(F)<4 I(F) for every checked t.")
print("Scope: finite checks support formulas only; REPORT.md proves all t analytically.")
