#!/usr/bin/env python3
"""Independent exact finite core for P01/P81 Halmos-wall audit.

No floating point. Laurent polynomials in one unitary u are represented
as dict exponent -> Fraction.
"""
from fractions import Fraction
from collections import defaultdict


def clean(p):
    return {k: v for k, v in p.items() if v}


def add(p, q):
    r = defaultdict(Fraction)
    for k, v in p.items():
        r[k] += v
    for k, v in q.items():
        r[k] += v
    return clean(r)


def scale(p, a):
    return clean({k: a * v for k, v in p.items()})


def mul(p, q):
    r = defaultdict(Fraction)
    for i, a in p.items():
        for j, b in q.items():
            r[i + j] += a * b
    return clean(r)


def star(p):
    return clean({-k: v for k, v in p.items()})


ONE = {0: Fraction(1)}
U = {1: Fraction(1)}

# Critical wall c=1: q=(1+u)/2.
q = scale(add(ONE, U), Fraction(1, 2))
qstarq = mul(star(q), q)
expected_qstarq = {
    -1: Fraction(1, 4),
    0: Fraction(1, 2),
    1: Fraction(1, 4),
}
assert qstarq == expected_qstarq

# D^2 = 1-q*q. This is (2-u-u^{-1})/4 = |1-u|^2/4.
D2 = add(ONE, scale(qstarq, Fraction(-1)))
expected_D2 = {
    -1: Fraction(-1, 4),
    0: Fraction(1, 2),
    1: Fraction(-1, 4),
}
assert D2 == expected_D2
assert add(qstarq, D2) == ONE

# In the commutative spectral fiber C*(u) ~= C(T),
# det [[q,D],[D,-q*]] = -(q q* + D^2) = -1.
detJ = scale(add(qstarq, D2), Fraction(-1))
assert detJ == {0: Fraction(-1)}

# Frozen explicit word coordinates and charge compensation:
# w=s1^5 s2^-2, g=w^-1 a, lamp a has zero free-coordinate.
w = (5, -2)
g = (-5, 2)
assert (w[0] + g[0], w[1] + g[1]) == (0, 0)

# Inside wall: scalar block carries w, companion 0.
inside_scalar = w
inside_companion = (0, 0)

# Outside wall: scalar w+g=0, companion -g=w.
outside_scalar = (w[0] + g[0], w[1] + g[1])
outside_companion = (-g[0], -g[1])
assert inside_scalar == (5, -2)
assert outside_scalar == (0, 0)
assert outside_companion == w
assert (
    inside_scalar[0] + inside_companion[0],
    inside_scalar[1] + inside_companion[1],
) == w
assert (
    outside_scalar[0] + outside_companion[0],
    outside_scalar[1] + outside_companion[1],
) == w

print("P26-P01-P81-INDEPENDENT-EXACT-AUDIT: PASS")
print("q*q =", sorted(qstarq.items()))
print("D^2 =", sorted(D2.items()))
print("q*q + D^2 =", sorted(add(qstarq, D2).items()))
print("fiber determinant J =", sorted(detJ.items()))
print("w coordinate =", w)
print("g coordinate =", g)
print("inside total =", w)
print("outside scalar =", outside_scalar)
print("outside companion =", outside_companion)
print(
    "outside total =",
    (
        outside_scalar[0] + outside_companion[0],
        outside_scalar[1] + outside_companion[1],
    ),
)
print("END P26-P01-P81-INDEPENDENT-EXACT-AUDIT")
