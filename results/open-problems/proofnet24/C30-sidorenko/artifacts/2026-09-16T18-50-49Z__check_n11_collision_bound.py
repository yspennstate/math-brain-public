#!/usr/bin/env python3
from math import comb

N = 11
EDGE_MAX = comb(N, 2)


def onto5(k: int) -> int:
    return sum((-1) ** j * comb(k, j) * (k - j) ** 5 for j in range(k + 1))


def balanced_fifth_sum(total: int, slots: int) -> int:
    q, r = divmod(total, slots)
    return (slots - r) * q ** 5 + r * (q + 1) ** 5


def min_degree_binomial_sum(n: int, m: int, k: int) -> int:
    q, r = divmod(2 * m, n)
    assert 0 <= q <= n - 1
    return (n - r) * comb(q, k) + r * comb(q + 1, k)


def collision_lower_bound(n: int, m: int):
    total = 0
    rows = []
    for k in range(1, 6):
        d_k = min_degree_binomial_sum(n, m, k)
        slots = comb(n, k)
        fifth = balanced_fifth_sum(d_k, slots)
        coeff = onto5(k)
        term = coeff * fifth
        total += term
        rows.append((k, coeff, d_k, fifth, term))
    return total, rows


coeffs = [onto5(k) for k in range(1, 6)]
assert coeffs == [1, 30, 150, 240, 120]
print("n =", N)
print("onto5 =", coeffs)
print("integer_form = hom(H,G)*n^20 >= (2m)^15")
print("m, lower_bound, lhs_minus_rhs, certified")
certified = []
for m in range(EDGE_MAX + 1):
    lb, _ = collision_lower_bound(N, m)
    lhs = lb * N ** 20
    rhs = (2 * m) ** 15
    ok = lhs >= rhs
    if ok:
        certified.append(m)
    print(m, lb, lhs - rhs, int(ok))

assert all(m in certified for m in range(27))
assert 27 not in certified
assert max(m for m in range(28) if m in certified) == 26

lb26, rows26 = collision_lower_bound(N, 26)
lb27, rows27 = collision_lower_bound(N, 27)
print("m26_rows =", rows26)
print("m27_rows =", rows27)
print("m26_lower_bound =", lb26)
print("m27_lower_bound =", lb27)
print("largest_initial_edge_count_certified =", 26)
print("m27_scalar_certificate_fails =", int(lb27 * N ** 20 < 54 ** 15))
print("ALL_EXACT_CHECKS_PASS")
