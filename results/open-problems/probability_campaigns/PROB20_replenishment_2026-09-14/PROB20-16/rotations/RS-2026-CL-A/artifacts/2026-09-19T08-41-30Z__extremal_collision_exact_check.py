#!/usr/bin/env python3
"""Exact finite self-checks for the B24 collision-kernel identities.

This is only a self-check of finite examples, not a proof or independent audit.
It verifies:
  1. E[(1+a)^{|S cap T|}] = sum_A a^{|A|} P(A subset S)^2.
  2. The empty/full law saturates the fixed-marginal upper bound.
  3. A singleton law saturates the first-order lower bound when np <= 1.
  4. iid Bernoulli support need not minimize pressure.
All arithmetic is exact fractions.Fraction.
"""
from fractions import Fraction
from itertools import product


def subsets(n):
    return [frozenset(i for i, b in enumerate(bits) if b)
            for bits in product([0, 1], repeat=n)]


def kernel(S, T, a):
    return (1 + a) ** len(S & T)


def expected_kernel(mu, n, a):
    ss = subsets(n)
    return sum(mu.get(S, Fraction(0)) * mu.get(T, Fraction(0)) * kernel(S, T, a)
               for S in ss for T in ss)


def inclusion_prob(mu, A):
    return sum(w for S, w in mu.items() if A.issubset(S))


def feature_expansion(mu, n, a):
    return sum((a ** len(A)) * inclusion_prob(mu, A) ** 2 for A in subsets(n))


# Arbitrary rational law: exact feature expansion.
n = 3
a = Fraction(2, 1)  # kernel base 1+a = 3
ss = subsets(n)
weights = [1, 2, 3, 4, 5, 6, 7, 8]
Z = sum(weights)
mu = {S: Fraction(w, Z) for S, w in zip(ss, weights)}
lhs = expected_kernel(mu, n, a)
rhs = feature_expansion(mu, n, a)
assert lhs == rhs == Fraction(599, 108)
print("feature_expansion_exact", lhs)

# Uniform-marginal p empty/full law: upper extremal formula.
p = Fraction(2, 5)
mu_two = {frozenset(): 1 - p, frozenset(range(n)): p}
upper = 1 + p * p * ((1 + a) ** n - 1)
assert expected_kernel(mu_two, n, a) == upper == Fraction(129, 25)
print("empty_full_saturates_upper", upper)

# n=2, p=1/2 singleton law: lower first-order formula and iid comparison.
n2 = 2
p2 = Fraction(1, 2)
mu_single = {frozenset({0}): p2, frozenset({1}): p2}
lower = 1 + a * n2 * p2 * p2
assert expected_kernel(mu_single, n2, a) == lower == 2
print("singleton_saturates_lower", lower)

mu_iid = {}
for S in subsets(n2):
    mu_iid[S] = (p2 ** len(S)) * ((1 - p2) ** (n2 - len(S)))
iid_formula = (1 + a * p2 * p2) ** n2
assert expected_kernel(mu_iid, n2, a) == iid_formula == Fraction(9, 4)
assert iid_formula > lower
print("iid_not_minimum", iid_formula, "gap", iid_formula - lower)

print("ALL_EXACT_CHECKS_PASS")
