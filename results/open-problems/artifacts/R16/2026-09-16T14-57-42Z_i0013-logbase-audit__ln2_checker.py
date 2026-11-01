#!/usr/bin/env python3
from fractions import Fraction

K = 40
L = sum(Fraction(1, j*(2**j)) for j in range(1, K+1))
U = L + Fraction(1, (K+1)*(2**K))
lo = Fraction(6931, 10000)
hi = Fraction(6932, 10000)

# For ln 2 = sum_{j>=1} 1/(j 2^j), tail bound:
# sum_{j>K} 1/(j2^j) <= (1/(K+1))*sum_{j>K}2^{-j}
# = 1/((K+1)2^K).
assert L < U
assert L > lo
assert U < hi
assert U < 1

print("K =", K)
print("L =", L)
print("U =", U)
print("decimal enclosure = [%.16f, %.16f]" % (float(L), float(U)))
print("certified coarse enclosure: 6931/10000 < ln(2) < 6932/10000 < 1")
print("normalization consequence: literal d_B*ln(2) is strictly smaller than d_B for d_B>0")
print("ALL_EXACT_CHECKS_PASS")
