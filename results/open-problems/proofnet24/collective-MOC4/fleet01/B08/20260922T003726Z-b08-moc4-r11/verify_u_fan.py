#!/usr/bin/env python3
"""Exact finite checks for the Drury-u comparison fan used in the B08 MOC4 report.

No floating point and no external packages.  The script checks:
  * the ten displayed formulas define the same functional on every subset-event
    generator P_{I,J}, hence on Saxl_4;
  * u(1)=1 and u(P_{I,J}) >= 0 for every generator;
  * each formula has four positive and one negative permutation term;
  * among the resulting 40 strict comparisons forced by u(s)>max(s), exactly
    30 distinct comparisons are transposition-neighbour comparisons.
"""
from fractions import Fraction
from itertools import combinations, permutations

PERMS = tuple(permutations(range(4)))

EXPRESSIONS = (
    (("3214", "4132", "3421", "2341"), "3241"),
    (("3214", "4132", "2431", "4321"), "4231"),
    (("3124", "4132", "3412", "2341"), "3142"),
    (("3124", "1432", "4312", "2341"), "1342"),
    (("2314", "4123", "3412", "2431"), "2413"),
    (("3214", "4123", "4312", "2431"), "4213"),
    (("2314", "4123", "1432", "3421"), "1423"),
    (("2134", "4123", "3412", "2341"), "2143"),
    (("3124", "2314", "1432", "4321"), "1324"),
    (("2134", "3214", "1432", "4321"), "1234"),
)

def p(text):
    return tuple(int(ch) - 1 for ch in text)

def event_value(sigma, I, J):
    return int({sigma[i] for i in I} == set(J))

def u_num_on_function(values, expression):
    positives, negative = expression
    return sum(values[p(x)] for x in positives) - values[p(negative)]

def is_transposition_neighbour(x, y):
    d = [i for i in range(4) if x[i] != y[i]]
    return len(d) == 2 and x[d[0]] == y[d[1]] and x[d[1]] == y[d[0]]

# Constants: every formula gives (4-1)/3 = 1.
assert all(Fraction(u_num_on_function({q: 1 for q in PERMS}, e), 3) == 1 for e in EXPRESSIONS)

# Equality of the ten formulas on the complete subset-event spanning family.
all_u_values = []
for k in range(5):
    for I in combinations(range(4), k):
        for J in combinations(range(4), k):
            values = {q: event_value(q, I, J) for q in PERMS}
            nums = [u_num_on_function(values, e) for e in EXPRESSIONS]
            assert len(set(nums)) == 1, (I, J, nums)
            assert nums[0] >= 0, (I, J, nums[0])
            all_u_values.append(Fraction(nums[0], 3))

# Forty forced comparisons; exactly thirty are distinct transposition comparisons.
all_edges = []
trans_edges = []
for positives, negative in EXPRESSIONS:
    n = p(negative)
    for positive in positives:
        q = p(positive)
        edge = (n, q)  # violation forces score(q) > score(n)
        all_edges.append(edge)
        if is_transposition_neighbour(n, q):
            trans_edges.append(edge)
assert len(all_edges) == 40
assert len(trans_edges) == 30
assert len(set(trans_edges)) == 30

print("PASS")
print("u_event_values=", sorted(set(all_u_values)))
print("forced_comparisons=40")
print("distinct_transposition_comparisons=30")
