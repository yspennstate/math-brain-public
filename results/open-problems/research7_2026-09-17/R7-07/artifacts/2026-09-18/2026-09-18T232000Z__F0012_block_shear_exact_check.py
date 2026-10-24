#!/usr/bin/env python3
"""Exact local certificate for the F0012 block-shear family."""
from itertools import product
from math import log2

SIGNS = (-1, 1)

def transformed(a,b,c,d):
    # P = [[1,0],[1,1]], P^{-1} = [[1,0],[-1,1]]
    # P^{-1} [[a,b],[c,d]] P =
    # [[a+b, b], [c+d-a-b, d-b]]
    return (a+b, b, c+d-a-b, d-b)

quads = list(product(SIGNS, repeat=4))
diag = [q for q in quads if transformed(*q)[2] == 0]
below = [q for q in quads
         if transformed(*q)[2] == 0 and transformed(*q)[0] == 0]
above = [q for q in quads
         if transformed(*q)[2] == 0 and transformed(*q)[3] == 0]

assert len(quads) == 16
assert len(diag) == 6
assert len(below) == 4
assert len(above) == 4

print("local_total=16")
print("diag_count=6")
print("below_count=4")
print("above_count=4")
print("diag_allowed=", diag)
print("below_allowed=", below)
print("above_allowed=", above)

for m in range(1, 7):
    N = 4 ** (m * (m - 1)) * 6 ** m
    free_log2 = 2 * m * (m - 1) + m * log2(6)
    n = 2 * m
    probability_exponent = n*n - free_log2
    expected = (n*n)/2 - (n/2) * (log2(6)-2)
    assert abs(probability_exponent - expected) < 1e-12
    print(f"m={m} n={n} family_count={N} "
          f"-log2(lower_probability)={probability_exponent:.12f} "
          f"normalized={probability_exponent/(n*n):.12f}")

print("EXACT_LOCAL_COUNT_AND_EXPONENT_PASS")
