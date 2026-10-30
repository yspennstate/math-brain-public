#!/usr/bin/env python3
"""Independent exact audit of B07-A034-K3-FIBER-v1.

This script does not import the author checker.  It reconstructs the
three-bit Walsh classification, Boolean convolution identities, exact
address energies, the general-k point-defect formula, and the numerator
parity lemma behind the odd product-row reserve.
"""

from collections import Counter
from fractions import Fraction
from itertools import product


def cube(k):
    return list(range(1 << k))


def parity(x):
    return x.bit_count() & 1


def wt(x):
    return x.bit_count()


def walsh_numerators(values, k):
    return [
        sum(values[x] * (-1 if parity(s & x) else 1) for x in cube(k))
        for s in cube(k)
    ]


def affine_two_flat(support):
    if len(support) != 4:
        return False
    translate = {x ^ support[0] for x in support}
    return 0 in translate and all(x ^ y in translate for x in translate for y in translate)


assertions = 0
counts = Counter()
semibent_energies = Counter()

# Complete three-bit reconstruction.
for values in product((-1, 1), repeat=8):
    n = walsh_numerators(values, 3)
    assertions += 1
    assert sum(x * x for x in n) == 64  # unscaled Parseval
    assertions += 1
    assert len({x & 1 for x in n}) == 1

    magnitudes = tuple(sorted(map(abs, n), reverse=True))
    if magnitudes == (8, 0, 0, 0, 0, 0, 0, 0):
        kind = "character"
        D = next(i for i, x in enumerate(n) if x)
        expected_16J = 16 * wt(D)
    elif magnitudes == (6, 2, 2, 2, 2, 2, 2, 2):
        kind = "point_defect"
        D = next(i for i, x in enumerate(n) if abs(x) == 6)
        expected_16J = 12 + 8 * wt(D)
    elif magnitudes == (4, 4, 4, 4, 0, 0, 0, 0):
        kind = "semibent"
        support = [i for i, x in enumerate(n) if x]
        assertions += 1
        assert affine_two_flat(support)
        expected_16J = 4 * sum(map(wt, support))
        semibent_energies[Fraction(expected_16J, 16)] += 1
    else:
        raise AssertionError((values, n, magnitudes))

    # Booleanity in Fourier form: sum_T fhat(T)fhat(T xor U)=0.
    for u in range(1, 8):
        assertions += 1
        assert sum(n[t] * n[t ^ u] for t in range(8)) == 0

    actual_16J = sum(wt(t) * n[t] * n[t] for t in range(8)) // 4
    assertions += 1
    assert actual_16J == expected_16J
    if kind != "character":
        assertions += 1
        assert Fraction(actual_16J, 16) >= Fraction(3, 4)
    counts[kind] += 1

assert counts == Counter(character=16, point_defect=128, semibent=112)
assertions += 1
assert set(semibent_energies) == {Fraction(1), Fraction(3, 2), Fraction(2)}
assertions += 1

# Exact general-k point-defect energy, all major characters through k=9.
point_defect_checks = 0
for k in range(2, 10):
    for D in cube(k):
        values = [(-1 if parity(D & x) else 1) for x in cube(k)]
        values[0] *= -1
        n = walsh_numerators(values, k)
        denom = 1 << k
        J = sum(Fraction(wt(t) * n[t] * n[t], denom * denom) for t in cube(k))
        target = Fraction(k, 1 << (k - 1)) + (1 - Fraction(1, 1 << (k - 2))) * wt(D)
        assertions += 1
        assert J == target
        point_defect_checks += 1


def product_rank_one_full_support(nums, r):
    """Whether |nums| is a positive product tensor on r<=2 bits."""
    if any(x == 0 for x in nums):
        return False
    if r == 1:
        return True
    return abs(nums[0] * nums[3]) == abs(nums[1] * nums[2])


def normalized_nu_prime(nums, r):
    """Compute nu' after orienting each product ratio >=1."""
    flip = 0
    for i in range(r):
        if abs(nums[1 << i]) < abs(nums[0]):
            flip ^= 1 << i
    m = [nums[s ^ flip] for s in cube(r)]
    nu = abs(m[0])
    denominator_product = 1
    for i in range(r):
        ratio = Fraction(abs(m[1 << i]), abs(m[0]))
        assertions_local = ratio >= 1
        assert assertions_local
        denominator_product *= ratio.denominator
    assert nu % denominator_product == 0
    return nu // denominator_product


# Fresh finite audit of the arithmetic lemma.  Here a(x)=4g_T(x) is any
# allowed integer row value.  Full-support product magnitude is checked
# independently; the analytic proof in REPORT.md covers all r.
parity_checks = 0
odd_cases = 0
for r in (1, 2):
    for a in product(range(-4, 5), repeat=1 << r):
        nums = walsh_numerators(a, r)
        if not product_rank_one_full_support(nums, r):
            continue
        nu_prime = normalized_nu_prime(nums, r)
        trace_parity = sum(x & 1 for x in a) & 1
        assertions += 1
        assert (nu_prime & 1) == trace_parity
        parity_checks += 1
        odd_cases += nu_prime & 1

print("INDEPENDENT_K3_AUDIT_PASS")
print("classification_counts", dict(counts))
print("semibent_address_energies", {str(k): v for k, v in sorted(semibent_energies.items())})
print("general_k_point_defect_checks", point_defect_checks)
print("independent_product_row_parity_checks", parity_checks)
print("odd_product_row_cases", odd_cases)
print("assertions", assertions)

