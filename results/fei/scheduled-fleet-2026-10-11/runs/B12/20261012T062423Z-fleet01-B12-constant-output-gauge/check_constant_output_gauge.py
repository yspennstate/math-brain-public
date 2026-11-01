#!/usr/bin/env python3
"""Exact/finite audit for the B12 constant-output gauge obstruction.

Exact Walsh coefficients and entropy log-prime vectors use Fraction.
The exhaustive three-bit census uses high-precision Decimal only to locate
and count witnesses.  The archived witness sign is certified analytically.
No randomness is used.
"""

from collections import defaultdict
from decimal import Decimal, getcontext
from fractions import Fraction

getcontext().prec = 80

GP = (1, 1, -1, 1, -1, 1, -1, -1)
GM = (-1, 1, 1, 1, 1, 1, 1, 1)
H = (1, -1, -1, -1, -1, -1, -1, -1)
QUERY = 0


def walsh(values):
    a = [Fraction(x) for x in values]
    n = len(a)
    step = 1
    while step < n:
        for base in range(0, n, 2 * step):
            for j in range(base, base + step):
                u, v = a[j], a[j + step]
                a[j], a[j + step] = u + v, u - v
        step *= 2
    return tuple(x / n for x in a)


def restrict(values, dimension, coordinate, bit):
    return tuple(values[j] for j in range(1 << dimension)
                 if ((j >> coordinate) & 1) == bit)


def factor_integer(n):
    n = abs(n)
    out = defaultdict(int)
    p = 2
    while p * p <= n:
        while n % p == 0:
            out[p] += 1
            n //= p
        p += 1
    if n > 1:
        out[n] += 1
    return out


def entropy_vector(coefficients):
    out = defaultdict(Fraction)
    for coefficient in coefficients:
        if coefficient == 0:
            continue
        mass = coefficient * coefficient
        for p, exponent in factor_integer(mass.denominator).items():
            out[p] += mass * exponent
        for p, exponent in factor_integer(mass.numerator).items():
            out[p] -= mass * exponent
    return {p: c for p, c in out.items() if c}


def add_vectors(*terms):
    out = defaultdict(Fraction)
    for scalar, vector in terms:
        for p, coefficient in vector.items():
            out[p] += scalar * coefficient
    return {p: c for p, c in out.items() if c}


def vector_decimal(vector):
    return sum(Decimal(c.numerator) / Decimal(c.denominator)
               * Decimal(p).ln() for p, c in vector.items())


def source_data(gp, gm):
    b = tuple(Fraction(x - y, 2) for x, y in zip(gp, gm))
    bh = walsh(b)
    return sum(x * x for x in bh), entropy_vector(bh)


def child_data(h):
    hh = walsh(h)
    variance = 1 - hh[0] * hh[0]
    influence = sum(j.bit_count() * x * x for j, x in enumerate(hh))
    return variance, influence


def components(gp, gm, h, dimension, coordinate):
    q, z = source_data(gp, gm)
    variance, influence = child_data(h)
    children = []
    for bit in (0, 1):
        gpb = restrict(gp, dimension, coordinate, bit)
        gmb = restrict(gm, dimension, coordinate, bit)
        hb = restrict(h, dimension, coordinate, bit)
        qb, zb = source_data(gpb, gmb)
        vb, ib = child_data(hb)
        children.append((qb, zb, vb, ib))
    delta_qi = q * influence - sum(qb * ib for qb, _, _, ib in children) / 2
    delta_vz = add_vectors(
        (variance, z),
        (-children[0][2] / 2, children[0][1]),
        (-children[1][2] / 2, children[1][1]),
    )
    return (q, z, variance, influence), children, delta_qi, delta_vz


def representation_from_output(F, h, unselected):
    gp, gm = [], []
    for f, selector, other in zip(F, h, unselected):
        if selector == 1:
            gp.append(f)
            gm.append(other)
        else:
            gp.append(other)
            gm.append(f)
    return tuple(gp), tuple(gm)


def main():
    root, children, delta_qi, delta_vz = components(GP, GM, H, 3, QUERY)
    assert root == (
        Fraction(5, 8),
        {2: Fraction(15, 4), 3: Fraction(-9, 8)},
        Fraction(7, 16),
        Fraction(3, 4),
    )
    assert children == [
        (Fraction(1), {2: Fraction(2)}, Fraction(3, 4), Fraction(1)),
        (Fraction(1, 4), {2: Fraction(1)}, Fraction(0), Fraction(0)),
    ]
    assert delta_qi == Fraction(-1, 32)
    assert delta_vz == {2: Fraction(57, 64), 3: Fraction(-63, 128)}

    F = tuple(GP[j] if H[j] == 1 else GM[j] for j in range(8))
    assert F == (1,) * 8
    support = [j for j, (x, y) in enumerate(zip(GP, GM)) if x != y]
    assert support == [0, 2, 4, 6, 7]
    assert {H[j] for j in support} == {-1, 1}

    # Exact elementary sign chain used in the proof:
    # 2^98 < 3^63 follows from (2^14)^7 < (3^9)^7.
    assert 2 ** 14 < 3 ** 9
    assert 2 ** 98 < 3 ** 63
    delta_vz_decimal = vector_decimal(delta_vz)
    assert delta_vz_decimal < Decimal(2).ln() / 8 < Fraction(1, 8)

    # Old coefficient C*=4+2ln2+2/e is strictly larger than 4.
    c_star = Decimal(4) + 2 * Decimal(2).ln() + 2 / Decimal(1).exp()
    old_drop = -c_star / 32 + delta_vz_decimal
    assert old_drop < 0

    # Exhaustive census of all 2^8 selectors and 2^8 unselected branches
    # representing F=1, at the frozen query coordinate.  Count only
    # activation-irreducible cases (both selector signs on disagreement).
    irreducible = 0
    negative_old = 0
    best = None
    for hm in range(1 << 8):
        h = tuple(1 if (hm >> j) & 1 else -1 for j in range(8))
        for um in range(1 << 8):
            other = tuple(1 if (um >> j) & 1 else -1 for j in range(8))
            gp, gm = representation_from_output(F, h, other)
            disagreement = [j for j in range(8) if gp[j] != gm[j]]
            if not disagreement or {h[j] for j in disagreement} != {-1, 1}:
                continue
            irreducible += 1
            _, _, dqi, dvz = components(gp, gm, h, 3, QUERY)
            drop = c_star * (Decimal(dqi.numerator) / Decimal(dqi.denominator)) \
                + vector_decimal(dvz)
            if drop < 0:
                negative_old += 1
            if best is None or drop < best[0]:
                best = (drop, gp, gm, h, dqi, dvz)

    assert negative_old > 0
    assert best is not None

    print("PASS")
    print("output=constant_1")
    print("disagreement_support=", support)
    print("selector_signs_on_support=", sorted({H[j] for j in support}))
    print("delta_qI=-1/32")
    print("delta_VZ=(57/64)ln2-(63/128)ln3")
    print("delta_VZ_decimal=", delta_vz_decimal)
    print("C_star=", c_star)
    print("old_potential_drop=", old_drop)
    print("exact_sign_chain=2^14<3^9 => 2^98<3^63")
    print("coefficient_cone=A>=4lambda implies negative total drop")
    print("output_influence_query=0")
    print("output_split_raw_entropy=0")
    print("exhaustive_representations=65536")
    print("activation_irreducible_representations=", irreducible)
    print("negative_old_potential_cases=", negative_old)
    print("minimum_old_drop_decimal=", best[0])
    print("random_seed=NONE")


if __name__ == "__main__":
    main()
