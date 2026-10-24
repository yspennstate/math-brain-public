#!/usr/bin/env python3
from fractions import Fraction
from itertools import product
from collections import Counter

D = 1_000_000
M = [
[-275992, 478033,      0,-275992,      0,-275992,      0,      0, 707099,      0,      0,      0],
[-275992, 478033,      0,-275992,      0,-275992,      0,      0,-707099,      0,      0,      0],
[ 275992,      0, 275992,      0, 478033,-275992,      0,      0,      0, 707099,      0,      0],
[ 275992,      0, 275992,      0, 478033,-275992,      0,      0,      0,-707099,      0,      0],
[      0,      0,-275992, 275992,      0,-275992, 478033,      0,      0,      0, 707099,      0],
[      0,      0,-275992, 275992,      0,-275992, 478033,      0,      0,      0,      0,-707099,      0],
[      0,      0,-425420, 425420,      0,-425420,-736850,      0,      0,      0,      0,      0],
[ 425420, 736849,      0, 425420,      0, 425420,      0,      0,      0,      0,      0,      0],
[-425420,      0,-425420,      0, 736849, 425420,      0,      0,      0,      0,      0,      0],
[-275992,      0, 275992, 275992,      0,      0,      0, 478033,      0,      0,      0, 707099],
[-275992,      0, 275992, 275992,      0,      0,      0, 478033,      0,      0,      0,-707099],
[-425420,      0, 425420, 425420,      0,      0,      0,-736849,      0,      0,      0,      0],
]
m = len(M)
n = len(M[0])
assert m == n == 12
assert all(len(r) == n for r in M)

col_sq = [sum(M[i][j] * M[i][j] for i in range(m)) for j in range(n)]
col_slack = [D*D - s for s in col_sq]
assert min(col_slack) > 0

row_l1 = [sum(abs(x) for x in row) for row in M]
qnum = min(row_l1)
Q = Fraction(qnum, D)
assert Q == Fraction(503277, 250000)
assert Q > 2

sat_count_dist = Counter()
sat_incidence = [0] * m
maxima = Counter()
disc_num = None

for eps in product((-1, 1), repeat=n):
    sat = []
    vals = []
    for i, row in enumerate(M):
        dot = sum(row[j] * eps[j] for j in range(n))
        vals.append(abs(dot))
        prods = [(1 if row[j] > 0 else -1) * eps[j]
                 for j in range(n) if row[j] != 0]
        if all(z == prods[0] for z in prods):
            sat.append(i)

    # Finite unsatisfiability/sign-cover core.
    assert len(sat) == 1
    i = sat[0]
    assert vals[i] == row_l1[i]

    sat_count_dist[len(sat)] += 1
    sat_incidence[i] += 1
    mx = max(vals)
    maxima[mx] += 1
    disc_num = mx if disc_num is None else min(disc_num, mx)

assert disc_num == qnum
assert sum(maxima.values()) == 2**n

old = Fraction(36907093, 20000000)
assert Q > old
assert Q - old == Fraction(3355067, 20000000)

print("R13_N12_EXPLICIT_OBSTRUCTION_EXACT_CHECK")
print("dimension =", n)
print("denominator =", D)
print("column_sq_numerators =", col_sq)
print("column_slacks =", col_slack)
print("min_column_slack =", min(col_slack))
print("row_l1_numerators =", row_l1)
print("min_row_l1_numerator =", qnum)
print("exact_discrepancy =", Q)
print("decimal_discrepancy =", float(Q))
print("strictly_above_2 =", Q > 2)
print("previous_R13_obstruction =", old)
print("improvement =", Q - old)
print("saturation_count_distribution =", dict(sorted(sat_count_dist.items())))
print("saturation_incidence =", sat_incidence)
print("maxima_distribution =", dict(sorted(maxima.items())))
print("R13_N12_EXPLICIT_OBSTRUCTION_EXACT_PASS")
