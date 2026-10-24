#!/usr/bin/env python3
"""Deterministic reconstruction checks for the B12 GU tensor theorem package."""

from fractions import Fraction
from decimal import Decimal, getcontext

getcontext().prec = 110
D = Decimal
LN2 = D(2).ln()


def walsh(values):
    out = [Fraction(v) for v in values]
    n = len(out)
    step = 1
    while step < n:
        for base in range(0, n, 2 * step):
            for j in range(base, base + step):
                x, y = out[j], out[j + step]
                out[j], out[j + step] = x + y, x - y
        step *= 2
    return [x / n for x in out]


def spectral_probabilities(values):
    return [x * x for x in walsh(values)]


def u_value(values):
    p = spectral_probabilities(values)
    nbits = len(values).bit_length() - 1
    upper = p[:]
    for bit in range(nbits):
        for mask in range(len(p)):
            if not ((mask >> bit) & 1):
                upper[mask] += upper[mask | (1 << bit)]
    ans = D(0)
    for x, q in zip(p, upper):
        if x:
            xd = D(x.numerator) / x.denominator
            qd = D(q.numerator) / q.denominator
            ans += xd * (qd / xd).ln() / LN2
    return ans


def restrict(values, bit, sign):
    want = 1 if sign == 1 else 0
    return [v for mask, v in enumerate(values) if ((mask >> bit) & 1) == want]


def influence(values):
    p = spectral_probabilities(values)
    return sum(Fraction(mask.bit_count()) * x for mask, x in enumerate(p))


def g_value(values):
    root = u_value(values)
    nbits = len(values).bit_length() - 1
    return sum(
        root - (u_value(restrict(values, bit, -1)) + u_value(restrict(values, bit, 1))) / 2
        for bit in range(nbits)
    )


def point_defect(n):
    return [-1] * ((1 << n) - 1) + [1]


def point_u_formula(n):
    N = D(2) ** n
    p0 = (1 - 2 / N) ** 2
    first = D(0) if p0 == 0 else p0 * (1 / p0).ln() / LN2
    return first + 2 * n / N - 4 * n / (N * N)


def tensor_point_defects(parts):
    total = sum(parts)
    values = []
    for mask in range(1 << total):
        offset = 0
        value = 1
        for width in parts:
            block = (mask >> offset) & ((1 << width) - 1)
            value *= 1 if block == (1 << width) - 1 else -1
            offset += width
        values.append(value)
    return values


def partitions(n, minimum=1):
    if n == 0:
        yield ()
    else:
        for first in range(minimum, n + 1):
            for tail in partitions(n - first, first):
                yield (first,) + tail


tol = D("1e-80")
point_checks = 0
best_ratio = (D("-Infinity"), None)
previous_u = D(0)
for n in range(1, 13):
    values = point_defect(n)
    u_direct = u_value(values)
    u_formula = point_u_formula(n)
    assert abs(u_direct - u_formula) < tol
    g_direct = g_value(values)
    g_formula = n * (u_formula - previous_u / 2)
    assert abs(g_direct - g_formula) < tol
    inf = D(influence(values).numerator) / influence(values).denominator
    ratio = D(0) if inf == 0 else g_direct / inf
    if ratio > best_ratio[0]:
        best_ratio = (ratio, n)
    previous_u = u_formula
    point_checks += 1

tensor_checks = 0
for total in range(1, 11):
    for parts in partitions(total):
        values = tensor_point_defects(parts)
        expected_u = sum(point_u_formula(n) for n in parts)
        expected_g = D(0)
        for n in parts:
            prev = D(0) if n == 1 else point_u_formula(n - 1)
            expected_g += n * (point_u_formula(n) - prev / 2)
        assert abs(u_value(values) - expected_u) < tol
        assert abs(g_value(values) - expected_g) < tol
        expected_i = sum(Fraction(2 * n, 1 << n) for n in parts)
        assert influence(values) == expected_i
        tensor_checks += 1

# Exact sign certificates used in the proof for the unique maximizer n=3.
assert 3 ** 12 > 2 ** 19   # log_2(3) > 19/12, hence kappa < 17/8.
assert 3 ** 18 < 2 ** 29   # log_2(3) < 29/18, hence kappa > 2.

kappa = D(37) / 4 - D(9) / 2 * D(3).ln() / LN2
assert best_ratio[1] == 3
assert abs(best_ratio[0] - kappa) < tol

print("PASS")
print(f"point_defect_formula_checks={point_checks}")
print(f"tensor_partition_checks={tensor_checks}")
print("maximizer_dimension=3")
print("kappa_exact=37/4-(9/2)log2(3)")
print("kappa_100d=" + format(kappa, ".101f"))
print("certificate_3^12_minus_2^19=" + str(3 ** 12 - 2 ** 19))
print("certificate_2^29_minus_3^18=" + str(2 ** 29 - 3 ** 18))
print("random_seed=None")
