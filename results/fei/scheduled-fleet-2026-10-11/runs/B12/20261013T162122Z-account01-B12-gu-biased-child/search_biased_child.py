#!/usr/bin/env python3
"""Exhaustive small-case search for the one-biased-child GU defect."""

from decimal import Decimal, getcontext
from fractions import Fraction
from functools import lru_cache
from itertools import permutations

getcontext().prec = 90
D = Decimal
LN2 = D(2).ln()
TOL = D("1e-65")


def walsh(values):
    out = [Fraction(v) for v in values]
    size = len(out)
    step = 1
    while step < size:
        for base in range(0, size, 2 * step):
            for k in range(base, base + step):
                x, y = out[k], out[k + step]
                out[k], out[k + step] = x + y, x - y
        step *= 2
    return tuple(x / size for x in out)


def upper_transform(masses):
    out = list(masses)
    n = len(out).bit_length() - 1
    for bit in range(n):
        for mask in range(1 << n):
            if not ((mask >> bit) & 1):
                out[mask] += out[mask | (1 << bit)]
    return tuple(out)


def dfrac(x):
    return D(x.numerator) / x.denominator


def entropy_terms(masses, caps=None):
    if caps is None:
        caps = upper_transform(masses)
    ans = D(0)
    for atom, cap in zip(masses, caps):
        if atom:
            a, c = dfrac(atom), dfrac(cap)
            ans += a * (c / a).ln() / LN2
    return ans


@lru_cache(maxsize=None)
def u_value(values):
    coeff = walsh(values)
    masses = tuple(x * x for x in coeff)
    return entropy_terms(masses)


@lru_cache(maxsize=None)
def influences(values):
    coeff = walsh(values)
    p = tuple(x * x for x in coeff)
    n = len(values).bit_length() - 1
    return tuple(sum((q for mask, q in enumerate(p) if (mask >> bit) & 1), Fraction())
                 for bit in range(n))


def restrict(values, bit, sign):
    wanted = 1 if sign == 1 else 0
    return tuple(v for mask, v in enumerate(values) if ((mask >> bit) & 1) == wanted)


def delta_u(values, bit):
    return u_value(values) - (u_value(restrict(values, bit, -1)) + u_value(restrict(values, bit, 1))) / 2


def compose_one_child(outer, outer_bit, child):
    m = len(outer).bit_length() - 1
    n = len(child).bit_length() - 1
    result = []
    for mask in range(1 << (n + m - 1)):
        child_mask = mask & ((1 << n) - 1)
        out_mask = (1 << outer_bit) if child[child_mask] == 1 else 0
        cursor = n
        for j in range(m):
            if j == outer_bit:
                continue
            if (mask >> cursor) & 1:
                out_mask |= 1 << j
            cursor += 1
        result.append(outer[out_mask])
    return tuple(result)


def mean(values):
    return Fraction(sum(values), len(values))


def psi(mu):
    q = mu * mu
    if not q:
        return D(0)
    x = dfrac(q)
    return x * (D(1) / x).ln() / LN2


@lru_cache(maxsize=None)
def outer_ab(outer, bit):
    minus = restrict(outer, bit, -1)
    plus = restrict(outer, bit, 1)
    a_values = tuple(Fraction(x + y, 2) for x, y in zip(plus, minus))
    b_values = tuple(Fraction(x - y, 2) for x, y in zip(plus, minus))
    return walsh(a_values), walsh(b_values)


@lru_cache(maxsize=None)
def psi_gate(outer, bit, mu):
    a, b = outer_ab(outer, bit)
    alpha2 = 1 - mu * mu
    c = tuple(x + mu * y for x, y in zip(a, b))
    c2 = tuple(x * x for x in c)
    b2 = tuple(x * x for x in b)
    mixed = tuple(x + alpha2 * y for x, y in zip(c2, b2))
    caps = upper_transform(mixed)
    empty_branch = entropy_terms(c2, caps)
    return empty_branch + dfrac(alpha2) * entropy_terms(b2)


def biased_formula(outer, bit, child):
    mu = mean(child)
    beta = influences(outer)[bit]
    u_star = u_value(child) - psi(mu)
    return psi_gate(outer, bit, mu) + dfrac(beta) * u_star


formula_checks = 0
ratio_count = 0
max_ratio = (D("-Infinity"), None)
min_ratio = (D("Infinity"), None)
max_abs_ratio = (D(0), None)

for m in (2, 3):
    for outer_index in range(1 << (1 << m)):
        outer = tuple(1 if (outer_index >> row) & 1 else -1 for row in range(1 << m))
        out_inf = influences(outer)
        for outer_bit in range(m):
            beta = out_inf[outer_bit]
            if not beta:
                continue
            for n in (1, 2, 3):
                for child_index in range(1 << (1 << n)):
                    child = tuple(1 if (child_index >> row) & 1 else -1 for row in range(1 << n))
                    composed = compose_one_child(outer, outer_bit, child)
                    direct = u_value(composed)
                    formula = biased_formula(outer, outer_bit, child)
                    assert abs(direct - formula) < TOL
                    formula_checks += 1
                    child_inf = influences(child)
                    for child_bit in range(n):
                        if not child_inf[child_bit]:
                            continue
                        defect = delta_u(composed, child_bit) - dfrac(beta) * delta_u(child, child_bit)
                        denom = dfrac(beta * child_inf[child_bit])
                        ratio = defect / denom
                        witness = (m, outer_index, outer_bit, n, child_index, child_bit, defect, beta, child_inf[child_bit])
                        if ratio > max_ratio[0]:
                            max_ratio = (ratio, witness)
                        if ratio < min_ratio[0]:
                            min_ratio = (ratio, witness)
                        if abs(ratio) > max_abs_ratio[0]:
                            max_abs_ratio = (abs(ratio), witness)
                        ratio_count += 1


def theta_gate(outer, outer_bit, mu):
    beta = influences(outer)[outer_bit]
    return psi_gate(outer, outer_bit, mu) - dfrac(beta) * psi(mu)


def tree_cocycle(outer, outer_bit, child, order):
    if not order:
        return D(0)
    bit = order[0]
    minus = restrict(child, bit, -1)
    plus = restrict(child, bit, 1)
    # After deleting one coordinate, later indices shift down.
    tail = tuple(k - 1 if k > bit else k for k in order[1:])
    local = theta_gate(outer, outer_bit, mean(child))
    local -= (theta_gate(outer, outer_bit, mean(minus)) +
              theta_gate(outer, outer_bit, mean(plus))) / 2
    return local + (tree_cocycle(outer, outer_bit, minus, tail) +
                    tree_cocycle(outer, outer_bit, plus, tail)) / 2


cocycle_tree_checks = 0
for outer_index in range(16):
    outer = tuple(1 if (outer_index >> row) & 1 else -1 for row in range(4))
    for outer_bit in range(2):
        if not influences(outer)[outer_bit]:
            continue
        endpoint_minus = theta_gate(outer, outer_bit, Fraction(-1))
        endpoint_plus = theta_gate(outer, outer_bit, Fraction(1))
        for n in (1, 2, 3):
            for child_index in range(1 << (1 << n)):
                child = tuple(1 if (child_index >> row) & 1 else -1 for row in range(1 << n))
                mu = mean(child)
                centered = theta_gate(outer, outer_bit, mu)
                centered -= (dfrac(1 - mu) * endpoint_minus +
                             dfrac(1 + mu) * endpoint_plus) / 2
                for order in permutations(range(n)):
                    assert abs(tree_cocycle(outer, outer_bit, child, order) - centered) < TOL
                    cocycle_tree_checks += 1

print("PASS")
print(f"formula_checks={formula_checks}")
print(f"normalized_defect_checks={ratio_count}")
print(f"max_ratio={max_ratio[0]}")
print(f"max_ratio_witness={max_ratio[1]}")
print(f"min_ratio={min_ratio[0]}")
print(f"min_ratio_witness={min_ratio[1]}")
print(f"max_abs_ratio={max_abs_ratio[0]}")
print(f"max_abs_ratio_witness={max_abs_ratio[1]}")
print(f"complete_tree_cocycle_checks={cocycle_tree_checks}")
print("candidate_bound_tested=defect <= 3*outer_influence*child_coordinate_influence")
print(f"candidate_bound_margin={D(3)-max_ratio[0]}")
print("random_seed=None")
