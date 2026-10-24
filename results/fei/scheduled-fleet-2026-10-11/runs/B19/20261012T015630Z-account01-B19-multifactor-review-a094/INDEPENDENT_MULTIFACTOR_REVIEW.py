#!/usr/bin/env python3
"""Independent checks for B05-A023-MULTIFACTOR-MOBIUS-OWNERSHIP-v1.

The proof-critical ownership and physical-chain cancellations are checked over
formal rational basis vectors, independently of the submitted interval code.
Small genuine-Boolean products are also reconstructed from truth tables.
"""
from fractions import Fraction
from itertools import permutations
from math import comb
from decimal import Decimal, getcontext

getcontext().prec = 100


def add(a, b):
    out = dict(a)
    for key, value in b.items():
        out[key] = out.get(key, Fraction()) + value
        if out[key] == 0:
            del out[key]
    return out


def scale(c, a):
    return {key: c * value for key, value in a.items() if c * value}


def basis(key):
    return {key: Fraction(1)}


def omega_basis(mask, r):
    """Expansion of Omega(mask) in the formal R(C) basis."""
    out = {}
    sub = mask
    while True:
        if sub:
            sign = -1 if ((mask.bit_count() - sub.bit_count()) & 1) else 1
            out = add(out, scale(sign, basis((r, sub))))
        if sub == 0:
            break
        sub = (sub - 1) & mask
    return out


def test_formal_mobius():
    checks = 0
    for r in range(1, 7):
        full = (1 << r) - 1
        orders = list(permutations(range(r)))
        reconstruction = {}
        for mask in range(1, 1 << r):
            reconstruction = add(reconstruction, omega_basis(mask, r))
        assert reconstruction == basis((r, full))
        checks += 1

        for order in orders:
            remaining = full
            total = {}
            position = {v: j for j, v in enumerate(order)}
            for owner in order:
                owned = {}
                for mask in range(1, 1 << r):
                    members = [j for j in range(r) if mask & (1 << j)]
                    if min(members, key=position.__getitem__) == owner:
                        owned = add(owned, omega_basis(mask, r))
                after = remaining & ~(1 << owner)
                expected = add(basis((r, remaining)), scale(-1, basis((r, after))))
                if after == 0:
                    expected.pop((r, 0), None)  # R(empty)=0.
                assert owned == expected
                total = add(total, owned)
                remaining = after
                checks += 1
            assert total == basis((r, full))
            checks += 1
    return checks


def test_formal_physical_telescope():
    checks = 0
    # P_m denotes R({q_m} union rest), and B denotes R(rest).
    for n in range(1, 201):
        signed = {}
        for m in range(1, n + 1):
            w = Fraction(1 << m, 1 << n)
            child = basis(("P", m - 1)) if m > 1 else basis("B")
            gamma = add(basis(("P", m)), scale(Fraction(-1, 2), child))
            gamma = add(gamma, scale(Fraction(-1, 2), basis("B")))
            signed = add(signed, scale(w, gamma))
        assert signed == add(basis(("P", n)), scale(-1, basis("B")))
        checks += 1
    return checks


def phi(x):
    if x == 0:
        return Decimal(0)
    return -x * x.ln() / Decimal(2).ln()


def pair_packet(a, v):
    q = a * a + v * v
    L = phi(a * a) + phi(v * v) - phi(q)
    if q == 0:
        Q = Decimal(0)
    else:
        s = Decimal("0.5") + abs(a * v) / q
        Q = q * (1 - phi(s) - phi(1 - s))
    return L + Q


def scalar_F(p):
    return 4 * p * (1 - p) + pair_packet(1 - p, p)


def fwht(values):
    values = list(values)
    step = 1
    while step < len(values):
        for start in range(0, len(values), 2 * step):
            for j in range(step):
                x, y = values[start + j], values[start + j + step]
                values[start + j], values[start + j + step] = x + y, x - y
        step *= 2
    return values


def product_truth(dims):
    values = [1]
    for n in dims:
        q = [1] + [-1] * ((1 << n) - 1)
        values = [a * b for a in values for b in q]
    return values


def packet_from_truth(values):
    raw = fwht(values)
    N = len(values)
    total = Decimal(0)
    for index, value in enumerate(raw):
        h = Decimal(value) / N
        if index == 0:
            a, v = (h + 1) / 2, (h - 1) / 2
        else:
            a = v = h / 2
        total += pair_packet(a, v)
    return total


def parity_probability(dims):
    prod = Decimal(1)
    for n in dims:
        prod *= 1 - Decimal(2) ** (1 - n)
    return (1 - prod) / 2


def test_boolean_and_symmetry():
    checks = 0
    for dims in ((1,), (2,), (2, 2), (2, 3), (2, 2, 2), (2, 2, 3), (2, 2, 2, 2)):
        p = parity_probability(dims)
        direct = packet_from_truth(product_truth(dims))
        assert abs(direct - scalar_F(p)) < Decimal("1e-80")
        assert abs(scalar_F(p) - scalar_F(1 - p)) < Decimal("1e-80")
        checks += 2
    return checks


def coefficient(r):
    return -2 * sum(
        Decimal((-1) ** (r - j) * comb(r, j) * j * j)
        * Decimal(j).ln() / Decimal(2).ln()
        for j in range(1, r + 1)
    )


def test_coefficients():
    checks = 0
    for r in range(3, 21):
        c = coefficient(r)
        assert ((-1) ** r) * c > 0
        checks += 1
    # The r=3 sign can be certified without floating point:
    # log_2(3)>4/3 because 3^3>2^4, hence 24-18log_2(3)<0.
    assert 3**3 > 2**4
    assert coefficient(3) < 0
    checks += 2
    return checks


def main():
    counts = {
        "formal_mobius_and_earliest_owner": test_formal_mobius(),
        "formal_physical_telescopes": test_formal_physical_telescope(),
        "truth_table_and_sign_symmetry": test_boolean_and_symmetry(),
        "alternating_coefficients": test_coefficients(),
    }
    print("PASS")
    for key, value in counts.items():
        print(f"{key}={value}")
    print(f"assertions={sum(counts.values())}")
    print("randomness=NONE")
    print("formal_arithmetic=fractions.Fraction")
    print("numeric_arithmetic=decimal.Decimal 100-digit context")
    for r in range(3, 9):
        print(f"c_{r}={coefficient(r):.40f}")


if __name__ == "__main__":
    main()
