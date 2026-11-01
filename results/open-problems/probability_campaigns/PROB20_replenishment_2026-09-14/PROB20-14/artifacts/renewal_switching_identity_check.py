"""Exact finite-state consistency check for PROB20-14 renewal switching.

This script is a certificate for algebraic identities only, not evidence for the
infinite-variance theorem.  It uses the critical finite-support law
P(xi=0)=2/5, P(xi=1)=1/5, P(xi=2)=2/5 (mean 1), enumerates all sequences of
length n with sum n-1, and checks equations (3.2)--(3.7) of the
2026-09-15T15:47:54Z report using exact rational arithmetic.
"""

from fractions import Fraction
from itertools import product, permutations
from math import prod

PI = {0: Fraction(2, 5), 1: Fraction(1, 5), 2: Fraction(2, 5)}
SUPPORT = tuple(PI)
N = 6
TARGET = N - 1
D = 2


def falling(x, s):
    out = 1
    for j in range(s):
        out *= x - j
    return out


def seq_weight(xs):
    out = Fraction(1, 1)
    for x in xs:
        out *= PI[x]
    return out


def sum_prob(length, target):
    total = Fraction(0, 1)
    for xs in product(SUPPORT, repeat=length):
        if sum(xs) == target:
            total += seq_weight(xs)
    return total


all_conditioned = []
a_n = Fraction(0, 1)
for xs in product(SUPPORT, repeat=N):
    if sum(xs) == TARGET:
        w = seq_weight(xs)
        a_n += w
        all_conditioned.append((xs, w))

assert a_n > 0


def q_expect(func):
    return sum((w / a_n) * func(xs) for xs, w in all_conditioned)


# Degree-count helpers for an allocation sequence.
def count(xs, value):
    return sum(x == value for x in xs)


def ordered_tuple_count_sum(xs, s, d):
    # Enumerate ordered distinct index tuples.  Small N only.
    total = 0
    for inds in permutations(range(N), s):
        if sum(xs[i] for i in inds) == d:
            total += 1
    return total


print(f"critical law={PI}, n={N}, target={TARGET}, a_n={a_n}")

summed_lhs = Fraction(0, 1)
summed_rhs = Fraction(0, 1)

for s in range(1, N + 1):
    u = sum_prob(s, D)
    residual = sum_prob(N - s, TARGET - D) if N - s >= 0 else Fraction(0, 1)
    ns = falling(N, s)

    ET = q_expect(lambda xs, s=s: ordered_tuple_count_sum(xs, s, D))
    ENfall = q_expect(
        lambda xs, s=s: count(xs, D) * falling(count(xs, 0), s - 1)
    )

    rhs_T = Fraction(ns, 1) * u * residual / a_n
    rhs_N = Fraction(ns, 1) * PI[D] * (PI[0] ** (s - 1)) * residual / a_n

    assert ET == rhs_T, (s, ET, rhs_T)
    assert ENfall == rhs_N, (s, ENfall, rhs_N)

    left_piece = ET / ns
    if u and PI[D]:
        right_piece = (
            u
            / (PI[D] * (PI[0] ** (s - 1)))
            * ENfall
            / ns
        )
        assert left_piece == right_piece, (s, left_piece, right_piece)
    else:
        right_piece = Fraction(0, 1)
        assert left_piece == 0

    summed_lhs += left_piece
    summed_rhs += right_piece
    print(
        f"s={s}: u_s(d)={u}, E[T_s,d]={ET}, "
        f"E[N_d(N_0)_(s-1)]={ENfall}, piece={left_piece}"
    )

assert summed_lhs == summed_rhs
print(f"summed identity exact: {summed_lhs} == {summed_rhs}")

# Direct check that sum_s T_s/(n)_s is the expected occupation count of level D
# by prefix sums of a uniformly random permutation of the degree multiset.
def occupation_by_permutations(xs, d):
    vals = []
    for perm in permutations(range(N)):
        total = 0
        visits = 0
        for idx in perm:
            total += xs[idx]
            if total == d:
                visits += 1
        vals.append(visits)
    return Fraction(sum(vals), len(vals))

EO = q_expect(lambda xs: occupation_by_permutations(xs, D))
assert EO == summed_lhs
print(f"occupation interpretation exact: E[O_{{n,d}}]={EO}")

print("ALL EXACT CHECKS PASSED")
