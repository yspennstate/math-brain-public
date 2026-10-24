#!/usr/bin/env python3
"""
R13 exact checker: six-column rational Boolean Komlos obstruction.
Pure integer/rational arithmetic only.
"""
from itertools import product
from fractions import Fraction
from collections import Counter

D = 10**9
a = 385_788_865
e = 366_670_139
f = 604_609_799
g = 636_135_052
d = 707_106_781

M = [
    [-a,  d,  0, -e,  0, -a],
    [ a,  0,  e,  0,  d, -a],
    [ 0,  0, -f,  f,  0, -g],
    [ a,  d,  0,  e,  0,  a],
    [-a,  0, -e,  0,  d,  a],
    [-g,  0,  f,  f,  0,  0],
]

QNUM = 1_845_354_650
assert 2*a + d + e == QNUM
assert 2*f + g == QNUM
row_l1 = [sum(abs(x) for x in row) for row in M]
assert row_l1 == [QNUM]*6

# Unit-column condition, exactly.
col_sq = [sum(M[i][j]**2 for i in range(6)) for j in range(6)]
assert all(x <= D*D for x in col_sq)

# Exact Boolean discrepancy: all 64 signings have infinity numerator QNUM.
maxima = []
witness_counts = Counter()
for eps in product((-1,1), repeat=6):
    vals = [sum(M[i][j]*eps[j] for j in range(6)) for i in range(6)]
    ab = [abs(x) for x in vals]
    mx = max(ab)
    maxima.append(mx)
    for i,x in enumerate(ab):
        if x == mx:
            witness_counts[i+1] += 1

assert len(maxima) == 64
assert min(maxima) == QNUM
assert max(maxima) == QNUM
assert Counter(maxima) == Counter({QNUM:64})

# The new lower bound is strictly above 9/5.
assert QNUM * 5 > 9 * D

# Exact rational separation from the preceding five-column radical T:
# sqrt(2)<71/50, sqrt(3)<87/50, sqrt(6)<49/20.
assert 2*50*50 < 71**2
assert 3*50*50 < 87**2
assert 6*20*20 < 49**2
# Hence 51+3sqrt(6) < 1167/20, and sqrt(1167/20)<191/25.
assert (191**2)*20 > 1167*(25**2)
# Therefore T < [2(71/50)+3(87/50)+2(191/25)]/13 = 1167/650 < 9/5.
upper_T = Fraction(1167,650)
assert upper_T < Fraction(9,5)
assert Fraction(QNUM,D) > Fraction(9,5)

print("R13_N6_RATIONAL_OBSTRUCTION_EXACT_PASS")
print("D =", D)
print("row_l1_numerators =", row_l1)
print("column_squared_norm_numerators =", col_sq)
print("column_squared_norm_deficits =", [D*D-x for x in col_sq])
print("signings =", len(maxima))
print("maxima_distribution =", dict(sorted(Counter(maxima).items())))
print("witness_counts =", dict(sorted(witness_counts.items())))
print("exact_discrepancy =", Fraction(QNUM,D))
print("decimal_discrepancy =", QNUM/D)
print("preceding_T_upper_certificate =", upper_T, "=", float(upper_T))
print("strict_chain: preceding T < 9/5 < new exact discrepancy")
