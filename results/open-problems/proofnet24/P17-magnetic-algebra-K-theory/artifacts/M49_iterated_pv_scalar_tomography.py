#!/usr/bin/env python3
"""Exact checker for ProofNet24 P17 M49.

Purpose
-------
Verify the iterated Pimsner-Voiculescu (PV) scalar tomography formulas for the
historical Example 4.3.3 magnetic noncommutative 4-torus.

Conventions
-----------
Generator order:
    (1,2,3,4) = (hull_1,hull_2,physical_1,physical_2).

Ordered K0 exterior basis:
    (), (1,2), (1,3), (1,4), (2,3), (2,4), (3,4), (1,2,3,4).

PV boundaries use the retained M48 right-exterior-contraction convention.
For i<j we define the two-step descendant by cutting j first and then i.

Source deformation entries:
    Theta_13 = 97/153, Theta_24 = 87/148, Theta_34 = 1/153,
    Theta_12 = Theta_14 = Theta_23 = 0.

This script performs exact rational/integer algebra only.  It performs no
spectral computation and certifies no magnetic gap.
"""

from fractions import Fraction
from itertools import combinations

BASIS = (
    (), (1, 2), (1, 3), (1, 4),
    (2, 3), (2, 4), (3, 4), (1, 2, 3, 4),
)

THETA = {
    (1, 2): Fraction(0),
    (1, 3): Fraction(97, 153),
    (1, 4): Fraction(0),
    (2, 3): Fraction(0),
    (2, 4): Fraction(87, 148),
    (3, 4): Fraction(1, 153),
}


def right_contract_term(term, j):
    """Return (sign, contracted_term), or None if j is absent."""
    if j not in term:
        return None
    pos = term.index(j)
    sign = -1 if ((len(term) - pos - 1) % 2) else 1
    return sign, term[:pos] + term[pos + 1 :]


def right_contract(x, j):
    """Right exterior contraction on a sparse exterior-class dictionary."""
    out = {}
    for term, coeff in x.items():
        hit = right_contract_term(term, j)
        if hit is None:
            continue
        sign, new_term = hit
        out[new_term] = out.get(new_term, 0) + sign * coeff
    return {k: v for k, v in out.items() if v}


def class_dict(v):
    return {term: coeff for term, coeff in zip(BASIS, v) if coeff}


def complement_pair(i, j):
    comp = tuple(k for k in (1, 2, 3, 4) if k not in (i, j))
    assert len(comp) == 2
    return comp


def delta_ij(x, i, j):
    """Two-step PV boundary for i<j: first cut j, then cut i."""
    assert i < j
    return right_contract(right_contract(x, j), i)


def residual_trace(y, kl):
    """Canonical trace on the residual two-generator torus."""
    return Fraction(y.get((), 0)) + THETA[kl] * Fraction(y.get(kl, 0))


def T_ij(x, i, j):
    kl = complement_pair(i, j)
    return residual_trace(delta_ij(x, i, j), kl)


# 1. M48 one-step signs are exactly right contraction.
expected_one_step = {
    1: {(2,): -1, (3,): -1, (4,): -1, (2, 3, 4): -1},
    2: {(1,): +1, (3,): -1, (4,): -1, (1, 3, 4): +1},
    3: {(1,): +1, (2,): +1, (4,): -1, (1, 2, 4): -1},
    4: {(1,): +1, (2,): +1, (3,): +1, (1, 2, 3): +1},
}
for j in (1, 2, 3, 4):
    got = {}
    for term in BASIS[1:]:
        hit = right_contract_term(term, j)
        if hit is not None and len(term) in (2, 4):
            sign, out = hit
            # Record only the basis monomial with coefficient 1.
            if len(term) == 2 or term == (1, 2, 3, 4):
                got[out] = sign
    assert got == expected_one_step[j], (j, got)


# 2. Two-step signs and graded anticommutativity.
expected_top_sign = {
    (1, 2): +1,
    (1, 3): -1,
    (1, 4): +1,
    (2, 3): +1,
    (2, 4): -1,
    (3, 4): +1,
}

top = {(1, 2, 3, 4): 1}
for i, j in combinations((1, 2, 3, 4), 2):
    kl = complement_pair(i, j)
    got = delta_ij(top, i, j)
    assert got == {kl: expected_top_sign[(i, j)]}, ((i, j), got)

    # Opposite cut order is the negative map under the natural identifications.
    opposite = right_contract(right_contract(top, i), j)
    assert opposite == {kl: -expected_top_sign[(i, j)]}

    # Formula s_ij = (-1)^(i+j+1).
    formula_sign = -1 if ((i + j + 1) % 2) else 1
    assert formula_sign == expected_top_sign[(i, j)]


# 3. Exact source scalar-descendant formulas.
# Ordered vector = (c0,c12,c13,c14,c23,c24,c34,q).
def descendants(v):
    x = class_dict(v)
    return {(i, j): T_ij(x, i, j) for i, j in combinations((1, 2, 3, 4), 2)}


def expected_descendants(v):
    c0, c12, c13, c14, c23, c24, c34, q = v
    return {
        (1, 2): Fraction(c12) + Fraction(1, 153) * q,
        (1, 3): Fraction(c13) - Fraction(87, 148) * q,
        (1, 4): Fraction(c14),
        (2, 3): Fraction(c23),
        (2, 4): Fraction(c24) - Fraction(97, 153) * q,
        (3, 4): Fraction(c34),
    }


tests = (
    (2, -3, 5, 7, -11, 13, -17, 19),
    (-23, 29, -31, 37, -41, 43, 47, -53),
    (0, 1, 0, 0, 0, 0, 0, 0),
    (1, 0, 0, 0, 0, 0, 0, 1),
)
for v in tests:
    assert descendants(v) == expected_descendants(v)


# 4. Fourfold descending PV boundary extracts q=c1234 with positive sign.
def Q(v):
    y = class_dict(v)
    for j in (4, 3, 2, 1):
        y = right_contract(y, j)
    return y.get((), 0)

for v in tests:
    assert Q(v) == v[7]


# 5. Full scalar tomography reconstruction.
def tau(v):
    c0, c12, c13, c14, c23, c24, c34, q = v
    th1 = Fraction(97, 153)
    th2 = Fraction(87, 148)
    b = Fraction(1, 153)
    return (
        Fraction(c0)
        + th1 * c13
        + th2 * c24
        + b * c34
        + th1 * th2 * q
    )


def reconstruct(tau_value, T, q):
    th1 = Fraction(97, 153)
    th2 = Fraction(87, 148)
    b = Fraction(1, 153)
    c12 = T[(1, 2)] - b * q
    c13 = T[(1, 3)] + th2 * q
    c14 = T[(1, 4)]
    c23 = T[(2, 3)]
    c24 = T[(2, 4)] + th1 * q
    c34 = T[(3, 4)]
    c0 = tau_value - th1 * c13 - th2 * c24 - b * c34 - th1 * th2 * q
    out = (c0, c12, c13, c14, c23, c24, c34, Fraction(q))
    assert all(z.denominator == 1 for z in out)
    return tuple(int(z) for z in out)

for v in tests:
    T = descendants(v)
    assert reconstruct(tau(v), T, Q(v)) == v


# 6. Compatibility with inherited M46 Chern formulas.
def inherited_chern(v):
    c0, c12, c13, c14, c23, c24, c34, q = v
    th1 = Fraction(97, 153)
    th2 = Fraction(87, 148)
    b = Fraction(1, 153)
    return {
        (1, 2): Fraction(c12) - b * q,
        (1, 3): Fraction(c13) + th2 * q,
        (1, 4): Fraction(c14),
        (2, 3): Fraction(c23),
        (2, 4): Fraction(c24) + th1 * q,
        (3, 4): Fraction(c34),
    }

for v in tests:
    c0, c12, c13, c14, c23, c24, c34, q = v
    T = descendants(v)
    Ch = inherited_chern(v)
    assert T[(1, 2)] + Ch[(1, 2)] == 2 * c12
    assert T[(1, 3)] + Ch[(1, 3)] == 2 * c13
    assert T[(2, 4)] + Ch[(2, 4)] == 2 * c24
    assert T[(3, 4)] == Ch[(3, 4)] == c34
    assert T[(1, 2)] - Ch[(1, 2)] == 2 * Fraction(1, 153) * q
    assert Ch[(1, 3)] - T[(1, 3)] == 2 * Fraction(87, 148) * q
    assert Ch[(2, 4)] - T[(2, 4)] == 2 * Fraction(97, 153) * q


# 7. Rational integer descendants and congruence regression checks.
def rational_scaled_data(v):
    T = descendants(v)
    q = Q(v)
    R12 = 153 * T[(1, 2)]
    R13 = 148 * T[(1, 3)]
    R24 = 153 * T[(2, 4)]
    R34 = T[(3, 4)]
    for z in (R12, R13, R24, R34):
        assert z.denominator == 1
    R12, R13, R24, R34 = map(int, (R12, R13, R24, R34))
    assert (R12 - q) % 153 == 0
    assert (R13 + 87 * q) % 148 == 0
    assert (R24 + 97 * q) % 153 == 0
    return (R12, R13, R24, R34, q)


def fiber_rank(v):
    c0, c12, c13, c14, c23, c24, c34, q = v
    return 22644*c0 + 14356*c13 + 13311*c24 + 148*c34 + 8439*q

historical = {
    "x1": (1, 0, -1, 0, 0, -1, 0, 1),
    "x2": (-1, 0, 2, 0, 0, 2, 0, -3),
    "x3": (2, 0, -2, 0, 0, -2, 0, 3),
    "x4": (0, 0, 1, 0, 0, 1, 0, -1),
}
expected_scaled = {
    "x1": (1, -235, -250, 0, 1),
    "x2": (-3, 557, 597, 0, -3),
    "x3": (3, -557, -597, 0, 3),
    "x4": (-1, 235, 250, 0, -1),
}
expected_ranks = {"x1": 3416, "x2": 7373, "x3": 15271, "x4": 19228}

for name, v in historical.items():
    assert v[3] == 0 and v[4] == 0  # M46 symmetry sector
    assert rational_scaled_data(v) == expected_scaled[name]
    assert fiber_rank(v) == expected_ranks[name]

print("M49 iterated PV scalar tomography: PASS")
print("top signs:", expected_top_sign)
print("historical scaled descendants:")
for name in historical:
    print(name, expected_scaled[name], "rank", expected_ranks[name])
