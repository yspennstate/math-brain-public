#!/usr/bin/env python3
"""Exact/floating audit for the NAND indicator tensor obstruction."""

from fractions import Fraction
import math


def fwht(values):
    a = list(values)
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2 * h):
            for j in range(i, i + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    return a


def raw_entropy(values):
    n = len(values)
    return sum(
        (z / n) ** 2 * math.log2(1 / (z / n) ** 2)
        for z in fwht(values)
        if z
    )


def spectral_influence(values):
    n = len(values)
    d = n.bit_length() - 1
    return sum(
        sum((values[x] - values[x ^ (1 << i)]) ** 2 for x in range(n))
        / (4 * n)
        for i in range(d)
    )


def indicator_gap(values, coefficient=2):
    p = sum(values) / len(values)
    return (
        raw_entropy(values)
        - coefficient * spectral_influence(values)
        - p * math.log2(1 / p)
    )


def tensor(a, b):
    return [x * y for x in a for y in b]


r = [1, 1, 1, 0]
w = fwht(r)
assert w == [3, 1, 1, -1]
assert sum(r) == 3

# Exact rational Fourier masses and influence of the two-bit NAND indicator.
fourier_masses = [Fraction(z * z, 16) for z in w]
assert fourier_masses == [Fraction(9, 16)] + [Fraction(1, 16)] * 3
assert sum(fourier_masses) == Fraction(3, 4)
assert spectral_influence(r) == Fraction(1, 4)

# The coefficient-2 gap is positive iff log_2(3)<8/3, certified by 3^3<2^8.
assert 3**3 < 2**8
gap_exact_form = 1 - Fraction(3, 8) * math.log2(3)
assert abs(indicator_gap(r) - gap_exact_form) < 1e-14

# Tensor-square is the exhaustive n<=4 maximizer found by EXPLORE.py.
r2 = tensor(r, r)
assert r2 == [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0]
assert fwht(r2) == [9, 3, 3, -3, 3, 1, 1, -1, 3, 1, 1, -1, -3, -1, -1, 1]
assert spectral_influence(r2) == Fraction(3, 8)
assert abs(indicator_gap(r2) - Fraction(3, 2) * gap_exact_form) < 1e-14

# General k-fold tensor formulas and genuine Boolean companions f_k=2q_k-1.
log3 = math.log2(3)
K_nand = 6 - 1.5 * log3
fei_limit = 12 - 4.5 * log3
assert K_nand > 2

rows = []
q = [1]
for k in range(1, 11):
    q = tensor(q, r)
    p = (3 / 4) ** k
    phi_formula = p * k * (2 - 0.5 * log3)
    i_formula = p * k / 3
    e_formula = p * k * (4 - 1.5 * log3)
    assert abs(raw_entropy(q) - e_formula) < 2e-12
    assert abs(spectral_influence(q) - i_formula) < 2e-12
    phi_direct = raw_entropy(q) - p * math.log2(1 / p)
    assert abs(phi_direct - phi_formula) < 2e-12
    assert abs(phi_direct / spectral_influence(q) - K_nand) < 2e-12

    f = [2 * x - 1 for x in q]
    hf = raw_entropy(f)
    inf = spectral_influence(f)
    assert abs(inf - 4 * i_formula) < 2e-12
    rows.append((k, len(q).bit_length() - 1, p, phi_direct / spectral_influence(q), hf / inf))

print("STATUS PASS")
print("NAND_WALSH", w)
print("NAND_MASSES", [str(x) for x in fourier_masses])
print("NAND_I", "1/4")
print("COEFFICIENT_2_GAP", f"{gap_exact_form:.15f}")
print("EXACT_SIGN_CERTIFICATE", f"3^3={3**3}<2^8={2**8}")
print("K_NAND", f"{K_nand:.15f}")
print("GENUINE_BOOLEAN_LIMIT", f"{fei_limit:.15f}")
print("k dimension p Phi_over_I Hf_over_If")
for row in rows:
    print(row[0], row[1], f"{row[2]:.15f}", f"{row[3]:.15f}", f"{row[4]:.15f}")

# Stronger five-bit exact seed recovered by the deterministic exploratory sweep.
s = [
    1, 1, 1, 0, 1, 1, 1, 1,
    1, 1, 1, 0, 1, 1, 1, 1,
    0, 1, 0, 0, 0, 1, 0, 0,
    1, 1, 1, 0, 1, 1, 1, 1,
]
sw = fwht(s)
expected_sw = [
    23, 1, 5, -5, -3, 3, 3, -3,
    -5, -3, 1, -1, 1, -1, -1, 1,
    5, 3, -1, 1, -1, 1, 1, -1,
    5, 3, -1, 1, -1, 1, 1, -1,
]
assert sw == expected_sw
assert sum(z * z for z in sw) == 32 * 23
assert sum(z * z * i.bit_count() for i, z in enumerate(sw)) == 368
assert spectral_influence(s) == Fraction(23, 64)

# Normalized Fourier law: 529/736, five atoms 25/736,
# seven atoms 9/736, and nineteen atoms 1/736.
h5 = math.log2(736) - (
    529 * math.log2(529) + 125 * math.log2(25) + 63 * math.log2(9)
) / 736
K5 = 2 * h5
gap5 = indicator_gap(s)
assert abs(gap5 - (Fraction(23, 64) * (K5 - 2))) < 2e-14

# K5>3.921 is equivalent, after prime-factor cancellation, to this
# exact integer comparison.
assert 2**139817 > 23**20125 * 5**15625 * 3**7875

# Tensor powers preserve Phi/I exactly; their sign companions are genuine
# Boolean functions and have a finite limiting H/I ratio.
sign_limit5 = 2 * (h5 + math.log2(Fraction(32, 23)))
q = [1]
five_rows = []
for k in range(1, 4):
    q = tensor(q, s)
    pk = (23 / 32) ** k
    phi = raw_entropy(q) - pk * math.log2(1 / pk)
    iq = spectral_influence(q)
    assert abs(phi / iq - K5) < 3e-11
    f = [2 * x - 1 for x in q]
    five_rows.append((k, 5 * k, pk, phi / iq, raw_entropy(f) / spectral_influence(f)))

print("FIVE_BIT_MASK", 4146264055)
print("FIVE_BIT_WALSH", sw)
print("FIVE_BIT_SQUARE_COUNTS", "529x1 25x5 9x7 1x19")
print("FIVE_BIT_P", "23/32")
print("FIVE_BIT_I", "23/64")
print("FIVE_BIT_COEFFICIENT_2_GAP", f"{gap5:.15f}")
print("K_FIVE", f"{K5:.15f}")
print("K_FIVE_CERTIFIED_LOWER_BOUND", "3.921")
print("K_FIVE_SIGN_CERTIFICATE", "2^139817 > 23^20125*5^15625*3^7875")
print("FIVE_BIT_GENUINE_BOOLEAN_LIMIT", f"{sign_limit5:.15f}")
print("k dimension p Phi_over_I Hf_over_If")
for row in five_rows:
    print(row[0], row[1], f"{row[2]:.15f}", f"{row[3]:.15f}", f"{row[4]:.15f}")
