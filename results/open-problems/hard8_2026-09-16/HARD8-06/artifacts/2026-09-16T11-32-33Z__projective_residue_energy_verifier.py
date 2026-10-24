#!/usr/bin/env python3
"""
Exact verifier for HARD8-06 projective p-adic residue-tree energy checkpoint.

Uses only Python standard library exact integer/Fraction arithmetic.
Checks:
  * balanced occupancy minimum C_m(s) by exhaustive compositions;
  * P^1(Z/p^ell Z) cardinality and determinant coincidence criterion;
  * exact projective energy direct sum vs closed form;
  * all-level energy >= one-level energy, with strict higher-level gains;
  * sample primitive split-polynomial discriminant/chordal identities.
No randomness, floating point, external solver, or timeout inference.
"""
from fractions import Fraction
from itertools import combinations
from math import gcd


def C(m, s):
    a, r = divmod(s, m)
    return m * a * (a - 1) + 2 * r * a


def compositions(total, parts, prefix=()):
    if parts == 1:
        yield prefix + (total,)
        return
    for x in range(total + 1):
        yield from compositions(total - x, parts - 1, prefix + (x,))


def projective_energy(q, s):
    total = 0
    ell = 1
    while True:
        m = (q + 1) * q ** (ell - 1)
        if m >= s:
            break
        total += C(m, s)
        ell += 1
    return total


def projective_closed(q, s):
    L = 0
    ell = 1
    while (q + 1) * q ** (ell - 1) < s:
        L = ell
        ell += 1
    if L == 0:
        return Fraction(0), 0
    total = Fraction(q * (1 - Fraction(1, q ** L)), q * q - 1) * s * s - L * s
    for ell in range(1, L + 1):
        m = (q + 1) * q ** (ell - 1)
        r = s % m
        total += Fraction(r * (m - r), m)
    return total, L


def inv_mod(a, m):
    return pow(a, -1, m)


def canonical_pair(x, y, p, ell):
    m = p ** ell
    x %= m
    y %= m
    if x % p == 0 and y % p == 0:
        return None
    if y % p != 0:
        return ("A", (x * inv_mod(y, m)) % m)
    # y is a nonunit, hence x is a unit.
    return ("I", (y * inv_mod(x, m)) % m)


def primitive_pairs(p, ell):
    m = p ** ell
    out = []
    classes = {}
    for x in range(m):
        for y in range(m):
            c = canonical_pair(x, y, p, ell)
            if c is not None:
                out.append((x, y, c))
                classes[c] = (x, y)
    return out, classes


def vp_int(n, p):
    if n == 0:
        raise ValueError("valuation of zero not used")
    n = abs(n)
    out = 0
    while n % p == 0:
        n //= p
        out += 1
    return out


def vp_frac(x, p):
    x = Fraction(x)
    if x == 0:
        raise ValueError("valuation of zero not used")
    return vp_int(x.numerator, p) - vp_int(x.denominator, p)


def poly_mul(A, B):
    out = [0] * (len(A) + len(B) - 1)
    for i, a in enumerate(A):
        for j, b in enumerate(B):
            out[i + j] += a * b
    return out


def primitive_split_poly(factors):
    # factor (a,b) means b*x-a, with gcd(a,b)=1 and b>0.
    coeff = [1]
    roots = []
    for a, b in factors:
        assert b > 0 and gcd(abs(a), abs(b)) == 1
        coeff = poly_mul(coeff, [-a, b])
        roots.append(Fraction(a, b))
    g = 0
    for c in coeff:
        g = gcd(g, abs(c))
    assert g == 1
    return coeff, roots


def discr_from_roots(coeff, roots):
    d = len(roots)
    lead = coeff[-1]
    val = Fraction(lead ** (2 * d - 2), 1)
    for i, j in combinations(range(d), 2):
        val *= (roots[i] - roots[j]) ** 2
    assert val.denominator == 1 and val.numerator != 0
    return val.numerator


box_minimum_checks = 0
for m in range(1, 6):
    for s in range(0, 9):
        brute = min(sum(n * (n - 1) for n in comp) for comp in compositions(s, m))
        assert brute == C(m, s)
        box_minimum_checks += 1

projective_cardinality_checks = 0
projective_determinant_checks = 0
for p, ell in [(2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3), (5, 1), (5, 2)]:
    prim, classes = primitive_pairs(p, ell)
    m = p ** ell
    expected = (p + 1) * p ** (ell - 1)
    assert len(classes) == expected
    projective_cardinality_checks += 1
    for x, y, c in prim:
        for x2, y2, c2 in prim:
            same = c == c2
            det_zero = ((x * y2 - x2 * y) % m == 0)
            assert same == det_zero
            projective_determinant_checks += 1

closed_form_checks = 0
one_level_comparison_checks = 0
strict_higher_level_improvements = 0
for q in [2, 3, 4, 5, 7, 8, 9]:
    for s in range(1, 501):
        direct = projective_energy(q, s)
        closed, L = projective_closed(q, s)
        assert closed.denominator == 1
        assert direct == closed.numerator
        closed_form_checks += 1
        first = C(q + 1, s)
        assert direct >= first
        one_level_comparison_checks += 1
        if direct > first:
            strict_higher_level_improvements += 1

# Exact leading-coefficient sanity check.
geometric_sum_checks = 0
for q in [2, 3, 4, 5, 7]:
    for L in range(1, 10):
        lhs = sum(Fraction(1, (q + 1) * q ** (ell - 1)) for ell in range(1, L + 1))
        rhs = Fraction(q, q * q - 1) * (1 - Fraction(1, q ** L))
        assert lhs == rhs
        geometric_sum_checks += 1

# Sample exact discriminant/chordal identities for primitive split polynomials.
examples = [
    [(1, 2), (3, 2)],
    [(1, 2), (5, 2), (3, 4)],
    [(1, 3), (4, 3)],
    [(1, 2), (1, 3), (5, 6)],
    [(2, 3), (5, 3), (8, 3)],
    [(-1, 2), (3, 4), (7, 8)],
]
discriminant_identity_checks = 0
sample_energy_checks = 0
for factors in examples:
    coeff, roots = primitive_split_poly(factors)
    assert len(set(roots)) == len(roots)
    disc = discr_from_roots(coeff, roots)
    d = len(roots)
    for p in [2, 3, 5, 7]:
        lhs = vp_int(disc, p)
        hs = [max(0, -vp_frac(r, p)) for r in roots]
        assert vp_int(coeff[-1], p) == sum(hs)
        rhs = 0
        for i, j in combinations(range(d), 2):
            delta = vp_frac(roots[i] - roots[j], p) + hs[i] + hs[j]
            assert delta >= 0
            rhs += 2 * delta
        assert lhs == rhs
        discriminant_identity_checks += 1
        assert lhs >= projective_energy(p, d)
        sample_energy_checks += 1

print("ALL_CHECKS_PASSED")
print("box_minimum_checks =", box_minimum_checks)
print("projective_cardinality_checks =", projective_cardinality_checks)
print("projective_determinant_checks =", projective_determinant_checks)
print("closed_form_checks =", closed_form_checks)
print("one_level_comparison_checks =", one_level_comparison_checks)
print("strict_higher_level_improvements =", strict_higher_level_improvements)
print("geometric_sum_checks =", geometric_sum_checks)
print("discriminant_identity_checks =", discriminant_identity_checks)
print("sample_energy_checks =", sample_energy_checks)
