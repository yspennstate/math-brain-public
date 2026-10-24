from fractions import Fraction
from itertools import product
from collections import Counter

D = 100_000_000
M = [
    [-41498232, 73852706, 0, -41498232, 0, -42638879, 0, 0, 0, 0, 0],
    [41498232, 0, 41498232, 0, 73852706, -42638879, 0, 0, 0, 0, 0],
    [0, 0, -26788739, 26788739, 0, -27525072, 47674824, 70710678, 0, 0, 0],
    [0, 0, -26788739, 26788739, 0, -27525072, 47674824, -70710678, 0, 0, 0],
    [0, 0, -41498232, 41498232, 0, -42638879, -73852706, 0, 0, 0, 0],
    [26788739, 47674824, 0, 26788739, 0, 27525072, 0, 0, 70710678, 0, 0],
    [26788739, 47674824, 0, 26788739, 0, 27525072, 0, 0, -70710678, 0, 0],
    [-26788739, 0, -26788739, 0, 47674824, 27525072, 0, 0, 0, 70710678, 0],
    [-26788739, 0, -26788739, 0, 47674824, 27525072, 0, 0, 0, -70710678, 0],
    [-42925791, 0, 42925791, 42925791, 0, 0, 0, 0, 0, 0, 70710678],
    [-42925791, 0, 42925791, 42925791, 0, 0, 0, 0, 0, 0, -70710678],
]

assert len(M) == 11 and all(len(row) == 11 for row in M)

col_sq = [sum(M[i][j] ** 2 for i in range(11)) for j in range(11)]
col_slack = [D * D - s for s in col_sq]
assert min(col_slack) > 0

row_l1 = [sum(abs(x) for x in row) for row in M]
NEW_NUM = min(row_l1)
NEW = Fraction(NEW_NUM, D)
OLD = Fraction(36_907_093, 20_000_000)
assert NEW == Fraction(199_488_049, 100_000_000)
assert NEW > OLD
assert NEW < 2

maxima = Counter()
sat_hist = Counter()
sat_counts = [0] * 11
best_num = None
best_eps = None
best_dots = None

for eps in product((-1, 1), repeat=11):
    dots = [sum(row[j] * eps[j] for j in range(11)) for row in M]
    mx = max(abs(x) for x in dots)
    maxima[mx] += 1

    saturated = []
    for i, row in enumerate(M):
        nz = [j for j, x in enumerate(row) if x]
        vals = [(1 if row[j] > 0 else -1) * eps[j] for j in nz]
        if all(v == vals[0] for v in vals):
            saturated.append(i)
    sat_hist[len(saturated)] += 1
    for i in saturated:
        sat_counts[i] += 1

    if best_num is None or mx < best_num:
        best_num = mx
        best_eps = eps
        best_dots = dots

assert sat_hist == Counter({1: 2048})
assert sat_counts == [256, 256, 128, 128, 256, 128, 128, 128, 128, 256, 256]
assert maxima == Counter({199_488_049: 768, 199_488_051: 512, 199_488_052: 768})
assert best_num == NEW_NUM

improvement = NEW - OLD
gap_to_2 = Fraction(2, 1) - NEW
assert improvement == Fraction(1_869_073, 12_500_000)
assert gap_to_2 == Fraction(511_951, 100_000_000)

print('R13_N11_EXPLICIT_OBSTRUCTION_EXACT_PASS')
print('D =', D)
print('new_discrepancy =', NEW, '=', float(NEW))
print('old_n11_padding_lower =', OLD, '=', float(OLD))
print('improvement =', improvement, '=', float(improvement))
print('gap_to_2 =', gap_to_2, '=', float(gap_to_2))
print('column_square_numerators =', col_sq)
print('column_slacks =', col_slack)
print('min_column_slack =', min(col_slack))
print('row_l1_numerators =', row_l1)
print('saturation_histogram =', dict(sat_hist))
print('row_saturation_counts =', sat_counts)
print('maxima_distribution =', dict(sorted(maxima.items())))
print('best_eps =', best_eps)
print('best_dots =', best_dots)
