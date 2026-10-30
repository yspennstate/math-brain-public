#!/usr/bin/env python3
"""Exact Walsh controls for the affine-defect source-reserve theorem."""

from fractions import Fraction
import math


def fwht(values):
    out = list(map(Fraction, values))
    h = 1
    while h < len(out):
        for start in range(0, len(out), 2 * h):
            for j in range(start, start + h):
                x, y = out[j], out[j + h]
                out[j], out[j + h] = x + y, x - y
        h *= 2
    return tuple(x / len(out) for x in out)


def entropy(hat):
    return sum(float(x * x) * math.log(1 / float(x * x)) for x in hat if x)


def influence(hat):
    return sum(s.bit_count() * x * x for s, x in enumerate(hat))


def linear_subspaces(n):
    """All linear subspaces for n<=4, by exact xor closure."""
    size = 1 << n
    for mask in range(1 << (size - 1)):
        space = {0} | {x for x in range(1, size) if mask >> (x - 1) & 1}
        if all((x ^ y) in space for x in space for y in space):
            yield frozenset(space)


def cosets(space, n):
    unseen = set(range(1 << n))
    while unseen:
        x = min(unseen)
        coset = frozenset(x ^ v for v in space)
        unseen -= coset
        yield coset


def classify(chi, defect):
    values = {chi[x] for x in defect}
    return "vary" if len(values) == 2 else ("plus" if 1 in values else "minus")


counts = {"vary": 0, "plus": 0, "minus": 0}
total = 0
maximum = (-1.0, None)

for n in range(1, 5):
    size = 1 << n
    for direction in linear_subspaces(n):
        for defect in cosets(direction, n):
            for r in range(1, size):
                chi = tuple(1 if (r & x).bit_count() % 2 == 0 else -1
                            for x in range(size))
                b = tuple(-chi[x] if x in defect else 0 for x in range(size))
                a = tuple(chi[x] + b[x] for x in range(size))
                h = tuple(-z for z in chi)
                hb = tuple(h[x] * b[x] for x in range(size))
                composed = tuple(a[x] + hb[x] for x in range(size))
                assert all(x in (-1, 1) for x in composed)

                ha, hbhat, hf = fwht(a), fwht(hb), fwht(composed)
                omega = entropy(hf) - entropy(ha) - entropy(hbhat)
                ib = influence(fwht(b))
                kind = classify(chi, defect)
                counts[kind] += 1
                total += 1

                if kind == "vary":
                    assert abs(omega) < 1e-11
                elif kind == "plus":
                    assert omega <= 1e-11
                assert omega <= 8 * math.log(2) * float(ib) + 1e-10
                if ib and omega / float(ib) > maximum[0]:
                    maximum = (omega / float(ib),
                               (n, len(defect), r, kind, omega, float(ib)))

    print(f"n={n} exhaustive_affine_cosets=PASS")

# The B01/A003 parity/two-defect selector is the varying-character case.
chi = tuple(1 if x.bit_count() % 2 == 0 else -1 for x in range(8))
defect = {0, 7}
b = tuple(-chi[x] if x in defect else 0 for x in range(8))
a = tuple(chi[x] + b[x] for x in range(8))
h = tuple(-z for z in chi)
hb = tuple(h[x] * b[x] for x in range(8))
composed = tuple(a[x] + hb[x] for x in range(8))
b01_omega = entropy(fwht(composed)) - entropy(fwht(a)) - entropy(fwht(hb))
assert b01_omega == 0.0

print(f"total_instances={total}")
print(f"classification_counts={counts}")
print(f"maximum_ratio_seen={maximum[0]:.15f}")
print(f"maximum_instance={maximum[1]}")
print(f"sharp_limit_8ln2={8 * math.log(2):.15f}")
print("B01_A003_two_defect_control_omega=0")
print("RESULT=PASS")

