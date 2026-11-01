#!/usr/bin/env python3
"""Exact audit of the B12 simultaneous shared-coordinate obstruction.

All Walsh coefficients and all coefficients of logarithms of primes are
computed with Fraction.  Decimal values are display only.  No randomness.
"""

from collections import defaultdict
from decimal import Decimal, getcontext
from fractions import Fraction
from math import log

getcontext().prec = 80


GP = (1, -1, -1, 1, -1, -1, -1, 1,
      -1, -1, 1, -1, -1, -1, -1, 1)
GM = (1, -1, -1, -1, 1, -1, -1, 1,
      -1, -1, 1, -1, -1, -1, 1, -1)
H = (1, 1, 1, 1, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 1, -1, 1)
SHARED_COORD = 1


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
    return tuple(
        values[index]
        for index in range(1 << dimension)
        if ((index >> coordinate) & 1) == bit
    )


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


def entropy_log_vector(coefficients):
    """Return exact c_p such that E_raw = sum_p c_p ln p."""
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
        for p, c in vector.items():
            out[p] += scalar * c
    return {p: c for p, c in out.items() if c}


def vector_float(vector):
    return sum(float(c) * log(p) for p, c in vector.items())


def source_data(gp, gm):
    b_hat = walsh(tuple(Fraction(x - y, 2) for x, y in zip(gp, gm)))
    q = sum(x * x for x in b_hat)
    z = entropy_log_vector(b_hat)
    return q, z


def child_data(h):
    h_hat = walsh(h)
    variance = 1 - h_hat[0] * h_hat[0]
    influence = sum(index.bit_count() * x * x for index, x in enumerate(h_hat))
    return variance, influence


def potential_components(gp, gm, h, dimension, coordinate):
    q, z = source_data(gp, gm)
    variance, influence = child_data(h)
    children = []
    for bit in (0, 1):
        gp_b = restrict(gp, dimension, coordinate, bit)
        gm_b = restrict(gm, dimension, coordinate, bit)
        h_b = restrict(h, dimension, coordinate, bit)
        q_b, z_b = source_data(gp_b, gm_b)
        v_b, i_b = child_data(h_b)
        children.append((q_b, z_b, v_b, i_b))
    delta_qi = q * influence - sum(x[0] * x[3] for x in children) / 2
    delta_vz = add_vectors(
        (variance, z),
        (-children[0][2] / 2, children[0][1]),
        (-children[1][2] / 2, children[1][1]),
    )
    return (q, z, variance, influence), children, delta_qi, delta_vz


def influence(values):
    return sum(index.bit_count() * x * x for index, x in enumerate(walsh(values)))


def tensor(f, s):
    # Original coordinates are the low-order bits; spectator coordinates follow.
    return tuple(f_i * s_j for s_j in s for f_i in f)


def bent_spectator(k):
    # 2k variables, s(x,y)=(-1)^(x dot y).
    out = []
    mask = (1 << k) - 1
    for index in range(1 << (2 * k)):
        x = index & mask
        y = (index >> k) & mask
        out.append(-1 if (x & y).bit_count() % 2 else 1)
    return tuple(out)


def main():
    root, children, delta_qi, delta_vz = potential_components(
        GP, GM, H, 4, SHARED_COORD
    )
    assert root[0] == Fraction(1, 4)
    assert root[1] == {2: Fraction(5, 4)}
    assert root[2] == Fraction(15, 64)
    assert root[3] == Fraction(1, 2)
    assert children[0] == (
        Fraction(1, 8), {2: Fraction(3, 4)}, Fraction(0), Fraction(0)
    )
    assert children[1] == (
        Fraction(3, 8),
        {2: Fraction(9, 4), 3: Fraction(-9, 16)},
        Fraction(7, 16),
        Fraction(3, 4),
    )
    assert delta_qi == Fraction(-1, 64)
    assert delta_vz == {2: Fraction(-102, 512), 3: Fraction(63, 512)}

    # Exact sign certificate: 3^63 < 2^102, hence 63 ln 3 - 102 ln 2 < 0.
    assert 3 ** 63 < 2 ** 102
    assert vector_float(delta_vz) < 0

    disagreement = [i for i, (x, y) in enumerate(zip(GP, GM)) if x != y]
    assert disagreement == [3, 4, 14, 15]
    assert all(H[i] == 1 for i in range(16) if i not in disagreement)
    assert {H[i] for i in disagreement} == {-1, 1}

    f = tuple(GP[i] if H[i] == 1 else GM[i] for i in range(16))
    assert entropy_log_vector(walsh(f)) == {2: Fraction(3)}
    assert influence(f) == 2

    family_rows = []
    for k in range(0, 5):
        if k == 0:
            s = (1,)
        else:
            s = bent_spectator(k)
            s_hat = walsh(s)
            assert len({abs(x) for x in s_hat}) == 1
            assert entropy_log_vector(s_hat) == {2: Fraction(2 * k)}
            assert influence(s) == k

        gp_k = tensor(GP, s)
        gm_k = tensor(GM, s)
        h_k = tensor(H, (1,) * len(s))
        dimension = 4 + 2 * k
        _, _, d_qi_k, d_vz_k = potential_components(
            gp_k, gm_k, h_k, dimension, SHARED_COORD
        )
        predicted_vz = {
            2: Fraction(-(102 + 24 * k), 512),
            3: Fraction(63, 512),
        }
        assert d_qi_k == Fraction(-1, 64)
        assert d_vz_k == predicted_vz
        assert 3 ** 63 < 2 ** (102 + 24 * k)

        f_k = tensor(f, s)
        f_entropy = entropy_log_vector(walsh(f_k))
        f_influence = influence(f_k)
        assert f_entropy == {2: Fraction(3 + 2 * k)}
        assert f_influence == 2 + k
        family_rows.append(
            (
                k,
                dimension,
                d_qi_k,
                d_vz_k,
                Fraction(3 + 2 * k, 2 + k),
            )
        )

    print("PASS")
    print("base_disagreement_support=", disagreement)
    print("delta_qI=", delta_qi)
    print("delta_VZ= (63 ln 3 - 102 ln 2)/512")
    print("delta_VZ_decimal=", format(Decimal(str(vector_float(delta_vz))), ".18f"))
    print("sign_certificate=3^63<2^102:", 3 ** 63 < 2 ** 102)
    print("base_F_entropy_bits=3")
    print("base_F_influence=2")
    print("base_F_H_over_I=3/2")
    print("tensor_family_rows=(k,dimension,delta_qI,delta_VZ,H_over_I_bits)")
    for row in family_rows:
        print(row)
    print("random_seed=NONE")


if __name__ == "__main__":
    main()
