#!/usr/bin/env python3
# R01 independent exact audit of the explicit 17x17 sign matrix in
# artifacts/R02/20260916T1801Z_8d4e2f1a_i0095_exact.cpp.
# Fix the last sign to +1, quotienting the global x -> -x symmetry,
# and enumerate all 2^16 remaining sign vectors exactly over integers.

from fractions import Fraction

A = [
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1],
[-1,-1,-1,1,1,1,1,-1,-1,-1,-1,1,1,1,1,1,1],
[1,1,1,-1,-1,-1,1,-1,-1,-1,1,-1,1,1,1,1,1],
[-1,1,1,-1,-1,1,-1,-1,-1,1,-1,1,-1,1,1,1,1],
[1,-1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,1,1,1,1],
[1,-1,1,1,1,-1,-1,1,-1,1,-1,-1,-1,1,1,1,1],
[-1,1,-1,1,-1,-1,1,1,1,-1,-1,-1,-1,1,1,1,1],
[1,-1,1,1,-1,-1,-1,-1,1,-1,-1,1,1,-1,1,1,1],
[-1,1,-1,1,1,-1,-1,-1,-1,1,1,-1,1,-1,1,1,1],
[1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,1,-1,1,1,1],
[-1,1,1,-1,1,1,-1,1,1,-1,-1,-1,1,-1,1,1,1],
[-1,-1,1,-1,1,-1,1,1,-1,-1,1,1,-1,-1,1,1,1],
[1,1,-1,1,-1,1,-1,1,-1,-1,1,1,-1,-1,1,1,1],
[1,1,-1,-1,1,-1,1,-1,1,1,-1,1,-1,-1,1,1,1],
[-1,-1,1,1,-1,1,1,-1,1,1,1,-1,-1,-1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]

best = 10**9
best_mask = None
for mask in range(1 << 16):
    mx = 0
    for row in A:
        s = row[16]
        for j in range(16):
            s += -row[j] if ((mask >> j) & 1) else row[j]
        mx = max(mx, abs(s))
    if mx < best:
        best = mx
        best_mask = mask

assert best == 7, (best, best_mask)
assert best_mask == 430, best_mask
ratio_sq = Fraction(best * best, 17)
assert ratio_sq == Fraction(49, 17)
print('R01 independent R02/I0095 A17 exact audit')
print('vectors_checked =', 1 << 16)
print('discrepancy =', best)
print('argmask =', best_mask)
print('ratio_squared = 49/17')
print('PASS')
