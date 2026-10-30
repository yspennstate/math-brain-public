#!/usr/bin/env python3
from fractions import Fraction
from itertools import product


def eps(q, k):
    return Fraction(2, 1) * Fraction(1, (2 ** q) * q) * (
        Fraction(1, (2 ** k) * k) - Fraction(1, (2 ** q) * q)
    )


def full_per_block(q, k):
    r = (q - k) // 2
    return Fraction(2, q * r) * (Fraction(1, k) - Fraction(1, q))


def central_per_block(q, k):
    r = (q - k) // 2
    return Fraction(2, r) * Fraction(1, (2 ** q) * q) * (
        Fraction(1, (2 ** k) * k) - Fraction(1, (2 ** q) * q)
    )


def ward(q):
    return Fraction(q - 1, q)


pairs = 0
max_ratio = Fraction(0, 1)
arg = None
for q in range(3, 200, 2):
    for k in range(1, q, 2):
        assert (q - k) % 2 == 0
        r = (q - k) // 2
        assert r >= 1
        fpb = full_per_block(q, k)
        assert fpb == Fraction(4, q * q * k)
        cpb = central_per_block(q, k)
        assert r * cpb == eps(q, k)
        full_total = r * fpb
        assert full_total == 2 * (Fraction(1, q * k) - Fraction(1, q * q))
        ratio = eps(q, k) / ward(q)
        if ratio > max_ratio:
            max_ratio = ratio
            arg = (q, k)
        pairs += 1
assert max_ratio == Fraction(11, 192)
assert arg == (3, 1)


def phase(bits, c):
    return -1 if all(b == 0 for b in bits[:c]) else 1


def beta(n, c, i):
    N = 2 ** n
    disagree = 0
    for bits in product((0, 1), repeat=n):
        y = list(bits)
        y[i] ^= 1
        disagree += phase(bits, c) != phase(tuple(y), c)
    I = Fraction(disagree, N)
    return min(I, 1 - I)


subcube_checks = 0
for c in range(1, 9):
    n = c + 2
    vals = [beta(n, c, i) for i in range(n)]
    if c == 1:
        expect = [Fraction(0)] * n
    else:
        expect = [Fraction(1, 2 ** (c - 1)) if i < c else Fraction(0) for i in range(n)]
    assert vals == expect
    J = sum(vals, Fraction(0))
    expectJ = Fraction(0) if c == 1 else Fraction(c, 2 ** (c - 1))
    assert J == expectJ
    assert J <= 1
    subcube_checks += n

print("PASS")
print(f"odd_(q,k)_pairs={pairs}")
print(f"sharp_central_ratio={max_ratio} at q,k={arg}")
print(f"subcube_coordinate_checks={subcube_checks}")
print("full_per_block=4/(q^2 k)")
print("central_per_block=epsilon(q,k)/r")
print("projective_beta(c>=2)=2^(1-c) on defining coordinates; J=c*2^(1-c)<=1")
