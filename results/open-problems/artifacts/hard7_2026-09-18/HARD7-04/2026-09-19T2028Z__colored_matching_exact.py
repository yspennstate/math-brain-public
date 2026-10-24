#!/usr/bin/env python3
"""Exact self-check for HARD7-04 colored-matching decomposition and dual matrix.

This is a finite sanity check, not a proof of the asymptotic MST claim.
It verifies:
  1. for L=6,8 labeled half-edges and three edge colors, the map
     colored matching <-> (ordered half-edge partition, within-color matchings)
     is one-to-one in every fixed color-count class;
  2. exact binomial marked-moment identities in a rational cubic test where
     the extinction root is rational; and
  3. the resulting two-type collar reproduction matrix and spectral radius.
"""

from itertools import product
from math import factorial, comb
from fractions import Fraction


def matchings(items):
    items = tuple(items)
    if not items:
        yield ()
        return
    a = items[0]
    for i in range(1, len(items)):
        b = items[i]
        rest = items[1:i] + items[i + 1 :]
        for M in matchings(rest):
            yield tuple(sorted(((min(a, b), max(a, b)),) + M))


def perfect_matching_count(size):
    """(size-1)!! for even size, with the empty matching counted once."""
    if size == 0:
        return 1
    out = 1
    for x in range(1, size, 2):
        out *= x
    return out


def representation_key(M, colors):
    sets = [set(), set(), set()]
    subs = [[], [], []]
    for edge, color in zip(M, colors):
        sets[color].update(edge)
        subs[color].append(edge)
    return (
        tuple(frozenset(s) for s in sets),
        tuple(tuple(sorted(x)) for x in subs),
    )


for L in (6, 8):
    Ms = list(matchings(range(L)))
    m = L // 2
    class_sizes = {}
    multiplicity = {}

    for M in Ms:
        for colors in product(range(3), repeat=m):
            counts = tuple(colors.count(c) for c in range(3))
            key = (counts,) + representation_key(M, colors)
            multiplicity[key] = multiplicity.get(key, 0) + 1
            class_sizes[counts] = class_sizes.get(counts, 0) + 1

    assert max(multiplicity.values()) == 1

    for counts, total in sorted(class_sizes.items()):
        a, b, c = counts
        edge_multinomial = factorial(m) // (
            factorial(a) * factorial(b) * factorial(c)
        )
        expected_from_colored_matchings = len(Ms) * edge_multinomial
        assert total == expected_from_colored_matchings

        partition_count = factorial(L) // (
            factorial(2 * a) * factorial(2 * b) * factorial(2 * c)
        )
        internal_matching_count = (
            perfect_matching_count(2 * a)
            * perfect_matching_count(2 * b)
            * perfect_matching_count(2 * c)
        )
        assert expected_from_colored_matchings == (
            partition_count * internal_matching_count
        )

    print(
        "L", L,
        "matchings", len(Ms),
        "colored", len(Ms) * 3**m,
        "count_classes", len(class_sizes),
        "unique representations", len(multiplicity),
    )


# Exact marked-moment / two-type matrix check.
# Cubic degrees have h(s)=s^2.  For p=2/3 the nontrivial extinction root is
# psi=1/4, since q=1-p+p*psi=1/2 and h(q)=1/4.
p = Fraction(2, 3)
psi = Fraction(1, 4)
q = 1 - p + p * psi
assert q == Fraction(1, 2)
d = 3


def expectation(fn):
    out = Fraction(0)
    for x in range(d + 1):
        probability = Fraction(comb(d, x)) * p**x * (1 - p) ** (d - x)
        out += probability * fn(x) * psi**x
    return out


EX = expectation(lambda x: x)
EX2 = expectation(lambda x: x * (x - 1))
ER = expectation(lambda x: d - x)
EXR = expectation(lambda x: x * (d - x))
ER2 = expectation(lambda x: (d - x) * (d - x - 1))

h = lambda z: z**2
hp = lambda z: 2 * z
assert psi == h(q)
assert EX == psi * p * d * q ** (d - 1)
assert EX2 == psi**2 * p**2 * d * (d - 1) * q ** (d - 2)
assert ER == (1 - p) * d * q ** (d - 1)
assert EXR == psi * p * (1 - p) * d * (d - 1) * q ** (d - 2)
assert ER2 == (1 - p) ** 2 * d * (d - 1) * q ** (d - 2)

Delta = Fraction(1, 12)
theta = Delta / (1 - p)
A_to_A = EX2 / EX
raw_A_to_B = theta * EXR / EX
B_to_A = theta * EXR / (theta * ER)
raw_B_to_B = theta**2 * ER2 / (theta * ER)
outside_pairing_fraction = psi

M = (
    (A_to_A, outside_pairing_fraction * raw_A_to_B),
    (B_to_A, outside_pairing_fraction * raw_B_to_B),
)
expected_M = (
    (p * hp(q), Delta * hp(q)),
    (p * hp(q), Delta * hp(q)),
)
assert M == expected_M

rho = M[0][0] + M[0][1]
assert rho == (p + Delta) * hp(q) == Fraction(3, 4)

print("q", q, "psi", psi, "hprime", hp(q), "matrix", M, "rho", rho)
print("ALL_EXACT_CHECKS_PASS = True")
