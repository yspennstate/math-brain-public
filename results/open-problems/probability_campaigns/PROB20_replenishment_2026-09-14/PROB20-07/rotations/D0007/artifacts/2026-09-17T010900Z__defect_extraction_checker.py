#!/usr/bin/env python3
"""Exact rational certificate for D0007's positive defect-extraction construction.

This checks only the finite arithmetic core of the theorem proved in the paired
run report.  All decisive inequalities use fractions.Fraction and exact integer
powers; decimal output is display-only.
"""
from fractions import Fraction
from decimal import Decimal, getcontext

E = 20001
r = 20000
m = 2*r + 1
n = 147785

delta = Fraction(1, 40003)
a = Fraction(40000, 40003)
b = Fraction(40002, 40003)

assert m == 40001
assert n % 2 == 1 and n >= m
assert (n-m) % 2 == 0

# The m-point atomic complete mix: r+1 copies of +a and r copies of -b.
assert (r+1)*a == r*b

# The two positive smoothing intervals exactly touch and stay in [0,1].
assert b-a == 2*delta
assert b+delta == 1

left_a = a-delta
left_b = b-delta
assert left_a == Fraction(39999, 40003)
assert left_b == Fraction(40001, 40003)

# After extraction with weight w=m/n, the two positive-interval densities are
# (r+1)/(4 n delta) and r/(4 n delta), respectively.
scaled_a = Fraction(r+1, 4*n*delta)
scaled_b = Fraction(r, 4*n*delta)

# Frozen target density f_*(x)=(E/2)|x|^(E-1) is increasing on [0,1], so
# domination on each interval reduces to its left endpoint.
target_a = Fraction(E, 2) * left_a**(E-1)
target_b = Fraction(E, 2) * left_b**(E-1)
assert scaled_a < target_a
assert scaled_b < target_b

# This exact construction is just past its own odd threshold: at n-2 the first
# interval domination fails.  This does NOT assert that F_* is non-CM at n-2.
n_prev = n-2
scaled_a_prev = Fraction(r+1, 4*n_prev*delta)
assert scaled_a_prev > target_a

da = target_a-scaled_a
db = target_b-scaled_b
dprev = scaled_a_prev-target_a

getcontext().prec = 50
def dec(fr):
    return Decimal(fr.numerator) / Decimal(fr.denominator)

print("D0007 exact defect-extraction positive-CM certificate")
print(f"E={E}; frozen f_*(x)=(E/2)|x|^(E-1) on [-1,1]")
print(f"m={m}; r={r}; n0={n}; pair_count={(n-m)//2}")
print(f"delta={delta}; a={a}; b={b}")
print(f"zero-sum atomic identity (r+1)a-rb = {(r+1)*a-r*b}")
print(f"interval touching identity b-a-2delta = {b-a-2*delta}")
print(f"right endpoint b+delta = {b+delta}")
print(f"left_a={left_a}; left_b={left_b}")
print(f"target_a-scaled_a ~ {dec(da)}")
print(f"target_b-scaled_b ~ {dec(db)}")
print(f"scaled_a(n0-2)-target_a ~ {dec(dprev)}")
print(f"sign target_a-scaled_a = {1 if da>0 else -1}")
print(f"sign target_b-scaled_b = {1 if db>0 else -1}")
print(f"sign scaled_a(n0-2)-target_a = {1 if dprev>0 else -1}")
print(f"|A margin numerator| bit_length={abs(da.numerator).bit_length()}")
print(f"|B margin numerator| bit_length={abs(db.numerator).bit_length()}")
print(f"|previous-A deficit numerator| bit_length={abs(dprev.numerator).bit_length()}")
print("CONCLUSION: weighted m-CM smoothed defect law is pointwise dominated by F_* at n0=147785.")
print("With symmetric residual pairs, this certifies F_* is 147785-CM; hence F_* is odd-n CM for all n>=147785.")
print("ALL EXACT D0007 DEFECT-EXTRACTION CHECKS PASSED")
