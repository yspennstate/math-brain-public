#!/usr/bin/env python3
"""Exact necessary row-sum enumeration for Williamson matrices of order 515.

If A,B,C,D are symmetric circulant {+1,-1} matrices of order n=515 and
A^2+B^2+C^2+D^2 = 4n I, their (odd) row sums a,b,c,d satisfy
a^2+b^2+c^2+d^2 = 4n = 2060.
This script enumerates the sorted absolute-value quadruples exactly.
It is a parameter reduction only, NOT an existence/nonexistence checker.
"""
from math import isqrt
n = 515
target = 4*n
vals = list(range(1, isqrt(target)+1, 2))
sol = []
for ia,a in enumerate(vals):
    for ib in range(ia, len(vals)):
        b = vals[ib]
        for ic in range(ib, len(vals)):
            c = vals[ic]
            rem = target-a*a-b*b-c*c
            if rem < c*c:
                continue
            if rem <= 0:
                continue
            d = isqrt(rem)
            if d >= c and (d & 1) and d*d == rem:
                sol.append((a,b,c,d))

assert len(sol) == len(set(sol))
for q in sol:
    assert tuple(sorted(q)) == q
    assert all(x > 0 and x % 2 == 1 for x in q)
    assert sum(x*x for x in q) == target

print(f"williamson_order_n={n}")
print(f"hadamard_order_4n={4*n}")
print(f"row_sum_square_target={target}")
print(f"sorted_absolute_rowsum_quadruple_count={len(sol)}")
for i,q in enumerate(sol, 1):
    print(f"{i:02d}: {q}")
print("EXACT_ENUMERATION_PASSED")
print("SCOPE: necessary Williamson row-sum parameters only; no existence/nonexistence conclusion.")
