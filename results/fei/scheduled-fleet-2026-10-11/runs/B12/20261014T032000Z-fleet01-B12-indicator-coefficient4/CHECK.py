#!/usr/bin/env python3
"""Exact-formula audit for co-singleton indicator tensor families."""

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


def influence(values):
    n = len(values)
    d = n.bit_length() - 1
    return sum(
        sum((values[x] - values[x ^ (1 << i)]) ** 2 for x in range(n))
        / (4 * n)
        for i in range(d)
    )


def tensor(a, b):
    return [x * y for x in a for y in b]


def theory(r):
    n = 1 << r
    p = Fraction(n - 1, n)
    h = r - Fraction(n - 2, n) * math.log2(n - 1)
    mean_degree = Fraction(r, 2 * (n - 1))
    K = h / mean_degree
    return p, h, mean_degree, K


rows = []
for r in range(1, 11):
    n = 1 << r
    q = [0] + [1] * (n - 1)
    w = fwht(q)
    assert w[0] == n - 1
    assert all(abs(z) == 1 for z in w[1:])
    p, h, mean_degree, K = theory(r)
    assert abs(sum(z * z for z in w) - n * (n - 1)) == 0
    weighted = sum(i.bit_count() * z * z for i, z in enumerate(w))
    assert weighted == r * (n // 2)
    assert abs(influence(q) - float(p * mean_degree)) < 1e-15
    phi = raw_entropy(q) - float(p) * math.log2(1 / float(p))
    assert abs(phi / influence(q) - K) < 5e-12
    rows.append((r, n, float(p), K))

# Exact coefficient-four failure at r=3:
# K_3 = 14-(7/2)log_2(7)>4 iff 7^7<2^20.
assert 7**7 < 2**20
K3 = 14 - Fraction(7, 2) * math.log2(7)
assert K3 > 4

# Stronger clean lower bound at r=5:
# K_5 = 62-(93/8)log_2(31)>22/5 iff 31^155<2^768.
assert 31**155 < 2**768
K5 = 62 - Fraction(93, 8) * math.log2(31)
assert K5 > Fraction(22, 5)

# Tensor powers preserve Phi/I exactly.  Directly verify the r=3 family
# through dimension 15, including genuine Boolean companions.
seed = [0] + [1] * 7
q = [1]
tensor_rows = []
p0, h0, m0, _ = theory(3)
sign_limit = (h0 + math.log2(1 / float(p0))) / m0
for k in range(1, 6):
    q = tensor(q, seed)
    pk = float(p0) ** k
    phi = raw_entropy(q) - pk * math.log2(1 / pk)
    iq = influence(q)
    assert abs(phi / iq - K3) < 2e-11
    f = [2 * x - 1 for x in q]
    assert abs(influence(f) - 4 * iq) < 2e-12
    tensor_rows.append((k, 3 * k, pk, phi / iq, raw_entropy(f) / influence(f)))

print("STATUS PASS")
print("R3_K", f"{K3:.15f}")
print("R3_EXACT_SIGN", f"7^7={7**7}<2^20={2**20}")
print("R5_K", f"{K5:.15f}")
print("R5_CERTIFIED_LOWER_BOUND", "4.4")
print("R5_EXACT_SIGN", "31^155<2^768")
print("R3_GENUINE_BOOLEAN_LIMIT", f"{sign_limit:.15f}")
print("r N p K_r")
for row in rows:
    print(row[0], row[1], f"{row[2]:.15f}", f"{row[3]:.15f}")
print("k dimension p Phi_over_I Hf_over_If")
for row in tensor_rows:
    print(row[0], row[1], f"{row[2]:.15f}", f"{row[3]:.15f}", f"{row[4]:.15f}")

# Stronger six-bit exact seed found by the deterministic search.
mask6 = 18446708751093190623
s6 = [(mask6 >> x) & 1 for x in range(64)]
assert [x for x, bit in enumerate(s6) if not bit] == [5, 12, 13, 28, 29, 37, 45]
w6 = fwht(s6)
square_counts = {u: sum(z * z == u for z in w6) for u in {z * z for z in w6}}
assert square_counts == {1: 36, 9: 24, 49: 3, 3249: 1}
assert sum(z * z for z in w6) == 3648
assert sum(i.bit_count() * z * z for i, z in enumerate(w6)) == 832
assert influence(s6) == Fraction(13, 64)
h6 = math.log2(3648) - (
    3249 * math.log2(3249) + 3 * 49 * math.log2(49) + 24 * 9 * math.log2(9)
) / 3648
K6 = Fraction(57, 13) * h6
assert K6 > Fraction(9, 2)
# K6>9/2 is exactly equivalent, after prime cancellation, to:
assert 2**3024 > 3**547 * 19**475 * 7**49

q = [1]
six_rows = []
p6 = Fraction(57, 64)
m6 = Fraction(13, 57)
sign_limit6 = (h6 + math.log2(1 / float(p6))) / m6
for k in range(1, 3):
    q = tensor(q, s6)
    pk = float(p6) ** k
    phi = raw_entropy(q) - pk * math.log2(1 / pk)
    iq = influence(q)
    assert abs(phi / iq - K6) < 2e-11
    f = [2 * x - 1 for x in q]
    six_rows.append((k, 6 * k, pk, phi / iq, raw_entropy(f) / influence(f)))

print("SIX_BIT_MASK", mask6)
print("SIX_BIT_ZEROS", [x for x, bit in enumerate(s6) if not bit])
print("SIX_BIT_SQUARE_COUNTS", square_counts)
print("SIX_BIT_P", "57/64")
print("SIX_BIT_I", "13/64")
print("SIX_BIT_K", f"{K6:.15f}")
print("SIX_BIT_CERTIFIED_LOWER_BOUND", "4.5")
print("SIX_BIT_EXACT_SIGN", "2^3024>3^547*19^475*7^49")
print("SIX_BIT_GENUINE_BOOLEAN_LIMIT", f"{sign_limit6:.15f}")
print("k dimension p Phi_over_I Hf_over_If")
for row in six_rows:
    print(row[0], row[1], f"{row[2]:.15f}", f"{row[3]:.15f}", f"{row[4]:.15f}")
