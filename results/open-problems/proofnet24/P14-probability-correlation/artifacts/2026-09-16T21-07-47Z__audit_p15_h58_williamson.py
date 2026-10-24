# Independent exact arithmetic audit of P15 2026-09-16 19:23:52 report, section 8.
# Scope: H58-invariant Williamson-type rows at length 523 only.
N=523
d=58
assert (N-1) % d == 0
orbits=(N-1)//d
assert orbits == 9
row_sums=sorted({1+d*s for s in range(-orbits,orbits+1,2)})
expected=[-521,-405,-289,-173,-57,59,175,291,407,523]
assert row_sums == expected
min_abs=min(abs(r) for r in row_sums)
lower=4*min_abs*min_abs
assert min_abs == 57
assert lower == 12996
assert lower > 4*N  # 2092
# Directly confirm no 4-tuple can satisfy the necessary row-sum equation.
solutions=0
for a in row_sums:
    for b in row_sums:
        for c in row_sums:
            rem=4*N-a*a-b*b-c*c
            if rem >= 0:
                for e in row_sums:
                    if e*e == rem:
                        solutions += 1
assert solutions == 0
print('N',N)
print('subgroup_order',d)
print('nonzero_orbits',orbits)
print('row_sums',row_sums)
print('min_abs_row_sum',min_abs)
print('four_square_lower_bound',lower)
print('required_sum_squares',4*N)
print('ordered_solution_count',solutions)
print('VERDICT PASS restricted H58-invariant Williamson row-sum exclusion')
print('P15_H58_AUDIT_PASS')
