from itertools import product

# Independent component audit of P15's restricted H58-invariant
# Williamson(523) emptiness self-check.
q = 523
d = 58
orbit_count = (q-1)//d
assert orbit_count == 9

# Global sign lets each candidate row be normalized to x(0)=+1.
row_sums = sorted({1 + d*sum(signs) for signs in product((-1,1), repeat=orbit_count)})
expected = [-521,-405,-289,-173,-57,59,175,291,407,523]
assert row_sums == expected
min_abs = min(abs(r) for r in row_sums)
assert min_abs == 57
lower_bound = 4*min_abs*min_abs
assert lower_bound == 12996 and lower_bound > 4*q

# Directly verify that no ordered four-tuple of feasible row sums can meet
# the necessary Williamson/GS row-sum identity sum r_i^2 = 4q = 2092.
solutions = []
for r1 in row_sums:
    for r2 in row_sums:
        for r3 in row_sums:
            for r4 in row_sums:
                if r1*r1+r2*r2+r3*r3+r4*r4 == 4*q:
                    solutions.append((r1,r2,r3,r4))
assert solutions == []

print('q=',q,'d=',d,'orbit_count=',orbit_count)
print('row_sums=',row_sums)
print('min_abs_row_sum=',min_abs)
print('four_square_lower_bound=',lower_bound)
print('target_4q=',4*q)
print('ordered_row_sum_solutions=',len(solutions))
print('VERDICT: PASS for the restricted H58-invariant Williamson(523) emptiness claim via the necessary row-sum identity alone.')
print('AUDIT_P15_H58_ROWSUM_PASS')
