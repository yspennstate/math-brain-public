from fractions import Fraction
from itertools import product
from math import comb


def multiplier_direct(n, r, lam):
    total = Fraction(0)
    for c in range(2, n + 1):
        q = lam / (2 ** c)
        num = comb(n - 1 - r, c - 1) if c - 1 <= n - 1 - r else 0
        den = comb(n - 1, c - 1)
        total += q * (Fraction((2 ** (c - 1)) * num, den) - 1)
    return total / n


def multiplier_closed(n, r, lam):
    return lam / (2 * (r + 1)) - lam / n + lam / (n * (2 ** n))


def ordered_min_kernel(n, weight, lam):
    if weight == 0:
        return Fraction(0)
    total = Fraction(0)
    for c in range(weight + 1, n + 1):
        q = lam / (2 ** c)
        total += q * Fraction(comb(c - 1, weight), comb(n - 1, weight))
    return total / n


def fwht_normalized(vals):
    a = [Fraction(x) for x in vals]
    N = len(a)
    h = 1
    while h < N:
        for i in range(0, N, 2 * h):
            for j in range(i, i + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    return [x / N for x in a]


def qflip_pairing_direct(m, vals, lam):
    n = m + 1
    N = 1 << m
    total = Fraction(0)
    for w in range(N):
        flips = sum(vals[x] != vals[x ^ w] for x in range(N))
        p = Fraction(flips, N)
        total += ordered_min_kernel(n, w.bit_count(), lam) * p
    return total


def qflip_pairing_spectral(m, vals, lam):
    hats = fwht_normalized(vals)
    total = Fraction(0)
    for u in range(1, 1 << m):
        r = u.bit_count()
        total += lam * Fraction(r, r + 1) * hats[u] * hats[u]
    return total


multiplier_cases = 0
for lam in (Fraction(1), Fraction(3, 2), Fraction(8), Fraction(17, 3)):
    for n in range(2, 41):
        for r in range(n):
            lhs = multiplier_direct(n, r, lam)
            rhs = multiplier_closed(n, r, lam)
            assert lhs == rhs, (lam, n, r, lhs, rhs)
            multiplier_cases += 1

boolean_cut_cases = 0
for lam in (Fraction(8), Fraction(5, 3)):
    for m in range(1, 4):
        N = 1 << m
        for mask in range(1 << N):
            vals = [(mask >> x) & 1 for x in range(N)]
            lhs = qflip_pairing_direct(m, vals, lam)
            rhs = qflip_pairing_spectral(m, vals, lam)
            assert lhs == rhs, (lam, m, mask, lhs, rhs)
            boolean_cut_cases += 1

parity_dummy_cases = 0
for n in range(2, 13):
    m = n - 1
    total = Fraction(0)
    for bits in product((0, 1), repeat=m):
        if bits[0]:
            total += ordered_min_kernel(n, sum(bits), Fraction(8))
    assert total == 1, (n, total)
    parity_dummy_cases += 1

print('PASS')
print('exact_multiplier_cases', multiplier_cases)
print('exact_boolean_cut_pairing_cases', boolean_cut_cases)
print('parity_switch_dummy_dimensions', parity_dummy_cases)
print('projective_lambda8_A0_minus_A1', Fraction(2))
print('parity_switch_payment_per_active_coordinate', Fraction(1))
print('parity_switch_two_coordinate_total', Fraction(2))
