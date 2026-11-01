#!/usr/bin/env python3
"""Exact/rigorous finite reconstruction checks for the B12 GU composition theorem."""

from decimal import Decimal, getcontext
from fractions import Fraction
from itertools import product

getcontext().prec = 100
D = Decimal
LN2 = D(2).ln()
TOL = D("1e-75")


def walsh(values):
    out = [Fraction(v) for v in values]
    size = len(out)
    step = 1
    while step < size:
        for base in range(0, size, 2 * step):
            for j in range(base, base + step):
                x, y = out[j], out[j + step]
                out[j], out[j + step] = x + y, x - y
        step *= 2
    return [x / size for x in out]


def probabilities(values):
    return [x * x for x in walsh(values)]


def u_value(values):
    p = probabilities(values)
    n = len(values).bit_length() - 1
    upper = p[:]
    for bit in range(n):
        for mask in range(1 << n):
            if not ((mask >> bit) & 1):
                upper[mask] += upper[mask | (1 << bit)]
    ans = D(0)
    for atom, cap in zip(p, upper):
        if atom:
            a = D(atom.numerator) / atom.denominator
            c = D(cap.numerator) / cap.denominator
            ans += a * (c / a).ln() / LN2
    return ans


def restrict(values, bit, sign):
    wanted = 1 if sign == 1 else 0
    return [value for mask, value in enumerate(values) if ((mask >> bit) & 1) == wanted]


def coordinate_delta_u(values, bit):
    return u_value(values) - (
        u_value(restrict(values, bit, -1)) + u_value(restrict(values, bit, 1))
    ) / 2


def g_value(values):
    n = len(values).bit_length() - 1
    return sum((coordinate_delta_u(values, bit) for bit in range(n)), D(0))


def coordinate_influences(values):
    p = probabilities(values)
    n = len(values).bit_length() - 1
    return [sum((mass for mask, mass in enumerate(p) if (mask >> bit) & 1), Fraction())
            for bit in range(n)]


def influence(values):
    return sum(coordinate_influences(values), Fraction())


def parity_sign(mask, offset, width):
    ans = 1
    for bit in range(offset, offset + width):
        ans *= 1 if ((mask >> bit) & 1) else -1
    return ans


def parity_inflate(outer, widths):
    total = sum(widths)
    result = []
    for mask in range(1 << total):
        outer_mask = 0
        offset = 0
        for j, width in enumerate(widths):
            if parity_sign(mask, offset, width) == 1:
                outer_mask |= 1 << j
            offset += width
        result.append(outer[outer_mask])
    return result


def compose(outer, children):
    widths = [len(child).bit_length() - 1 for child in children]
    total = sum(widths)
    result = []
    for mask in range(1 << total):
        outer_mask = 0
        offset = 0
        for j, (child, width) in enumerate(zip(children, widths)):
            block_mask = (mask >> offset) & ((1 << width) - 1)
            if child[block_mask] == 1:
                outer_mask |= 1 << j
            offset += width
        result.append(outer[outer_mask])
    return result


def balanced_functions_upto_two_bits():
    answer = []
    for n in (1, 2):
        for signs in product((-1, 1), repeat=1 << n):
            if sum(signs) == 0:
                answer.append(list(signs))
    return answer


# Part I: balanced-disjoint upper-mass and influence chain rules.
balanced = balanced_functions_upto_two_bits()
balanced_chain_checks = 0
for outer_signs in product((-1, 1), repeat=4):
    outer = list(outer_signs)
    outer_coord_inf = coordinate_influences(outer)
    for h1 in balanced:
        for h2 in balanced:
            composed = compose(outer, [h1, h2])
            expected_u = u_value(outer)
            expected_u += (D(outer_coord_inf[0].numerator) / outer_coord_inf[0].denominator) * u_value(h1)
            expected_u += (D(outer_coord_inf[1].numerator) / outer_coord_inf[1].denominator) * u_value(h2)
            assert abs(u_value(composed) - expected_u) < TOL
            expected_i = outer_coord_inf[0] * influence(h1) + outer_coord_inf[1] * influence(h2)
            assert influence(composed) == expected_i
            balanced_chain_checks += 1


# Part II: arbitrary outer gates, with every parity-block pattern in {1,2}^m.
parity_inflation_checks = 0
zero_g_checks = 0
min_outer_delta = (D("Infinity"), None)
max_outer_delta = (D("-Infinity"), None)
for m in (1, 2, 3):
    for truth_index in range(1 << (1 << m)):
        outer = [1 if ((truth_index >> row) & 1) else -1 for row in range(1 << m)]
        outer_u = u_value(outer)
        outer_deltas = [coordinate_delta_u(outer, j) for j in range(m)]
        outer_inf = coordinate_influences(outer)
        for j, delta in enumerate(outer_deltas):
            if delta < min_outer_delta[0]:
                min_outer_delta = (delta, (m, truth_index, j))
            if delta > max_outer_delta[0]:
                max_outer_delta = (delta, (m, truth_index, j))
        for widths in product((1, 2), repeat=m):
            inflated = parity_inflate(outer, widths)
            assert abs(u_value(inflated) - outer_u) < TOL
            expected_g = sum((outer_deltas[j] for j, width in enumerate(widths) if width == 1), D(0))
            assert abs(g_value(inflated) - expected_g) < TOL
            expected_i = sum((Fraction(widths[j]) * outer_inf[j] for j in range(m)), Fraction())
            assert influence(inflated) == expected_i
            parity_inflation_checks += 1
            if all(width >= 2 for width in widths):
                assert abs(g_value(inflated)) < TOL
                zero_g_checks += 1


# Exact small obstruction: coordinate decrements need not be nonnegative, and
# parity inflation can delete precisely the negative coordinates from G.
obstruction_outer = [1, 1, -1, 1, 1, -1, -1, -1]
obstruction_deltas = [coordinate_delta_u(obstruction_outer, j) for j in range(3)]
assert all(abs(x - y) < TOL for x, y in zip(obstruction_deltas, (D("0.5"), D("-0.5"), D("-0.5"))))
assert abs(u_value(obstruction_outer) - D("0.5")) < TOL
assert influence(obstruction_outer) == Fraction(3, 2)
obstruction_inflated = parity_inflate(obstruction_outer, (1, 2, 2))
assert abs(g_value(obstruction_inflated) - D("0.5")) < TOL
assert influence(obstruction_inflated) == Fraction(5, 2)


print("PASS")
print(f"balanced_chain_checks={balanced_chain_checks}")
print(f"parity_inflation_checks={parity_inflation_checks}")
print(f"all_blocks_nonterminal_zero_G_checks={zero_g_checks}")
print(f"min_outer_coordinate_delta={min_outer_delta[0]}")
print(f"min_outer_coordinate_delta_witness={min_outer_delta[1]}")
print(f"max_outer_coordinate_delta={max_outer_delta[0]}")
print(f"max_outer_coordinate_delta_witness={max_outer_delta[1]}")
print("signed_delta_obstruction_truth_vector=++-++---")
print("signed_delta_obstruction_deltas=(1/2,-1/2,-1/2)")
print("signed_delta_obstruction_G=-1/2")
print("widths_(1,2,2)_inflated_G=1/2")
print("widths_(1,2,2)_inflated_I=5/2")
print("outer_scope=all Boolean truth tables through arity 3")
print("parity_width_scope=all width vectors in {1,2}^m")
print("arithmetic=Fraction Walsh coefficients; Decimal(100) logarithms")
print("random_seed=None")
