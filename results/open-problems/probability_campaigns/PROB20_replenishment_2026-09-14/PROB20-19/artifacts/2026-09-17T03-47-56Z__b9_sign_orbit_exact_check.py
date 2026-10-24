#!/usr/bin/env python3
from fractions import Fraction
from itertools import product

# Exact rational orthogonal matrix already used elsewhere in PROB20-19,
# here repurposed only to test the conditional Rademacher-sign proof route.
Q = [
    [Fraction(3, 5), Fraction(4, 5), Fraction(0, 1)],
    [Fraction(-4, 13), Fraction(3, 13), Fraction(12, 13)],
    [Fraction(48, 65), Fraction(-36, 65), Fraction(5, 13)],
]

def dot(a, b):
    return sum(x * y for x, y in zip(a, b))

cols = [[Q[r][c] for r in range(3)] for c in range(3)]
gram = [[dot(cols[i], cols[j]) for j in range(3)] for i in range(3)]
identity = [[Fraction(int(i == j), 1) for j in range(3)] for i in range(3)]
assert gram == identity

# Fix the magnitude vector a=(1,1,1). Before rotation every sign choice has
# min_i a_i^2 = 1, hence Top_2(a_i^2)=2. After rotation, average over all
# eight independent Rademacher signs exactly.
mins = []
for eps in product([1, -1], repeat=3):
    x = [Fraction(e, 1) for e in eps]
    y = [sum(Q[r][i] * x[i] for i in range(3)) for r in range(3)]
    sq = [v * v for v in y]
    mins.append(min(sq))

avg_min = sum(mins, Fraction(0, 1)) / 8
assert avg_min == Fraction(469, 4225)
assert avg_min < 1
assert Fraction(1, 1) - avg_min == Fraction(3756, 4225)

# Since Q is orthogonal, ||Qx||_2^2=3 for every sign vector x.
# Therefore Top_2 = 3 - min in dimension three.
avg_top2 = Fraction(3, 1) - avg_min
assert avg_top2 == Fraction(12206, 4225)
assert avg_top2 > 2
assert avg_top2 - 2 == Fraction(3756, 4225)

print("PROB20-19 B9 exact conditional-sign randomization obstruction")
print("Q_orthogonal = PASS")
print("sign_minima =", ",".join(str(x) for x in mins))
print("average_min_after_Q =", avg_min)
print("min_before_Q = 1")
print("average_top2_after_Q =", avg_top2)
print("top2_before_Q = 2")
print("conditional_top2_gain =", avg_top2 - 2)
print("pointwise_conditional_sign_domination = REFUTED")
print("ALL_EXACT_CHECKS_PASS")
