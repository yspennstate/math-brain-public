#!/usr/bin/env python3
"""Exact finite check for R07 run 45's Cantor-dimension gap.

Temporal set: middle-thirds Cantor, d_t = log(2)/log(3).
Spatial set: two-map ratio-1/16 Cantor, d_x = log(2)/log(16) = 1/4.
Required: d_t > (1+d_x)/2 = 5/8.
This is equivalent to 8 log 2 > 5 log 3, hence 2^8 > 3^5.
"""

lhs = 2**8
rhs = 3**5
assert lhs == 256
assert rhs == 243
assert lhs > rhs
print(f"PASS: 2^8={lhs} > 3^5={rhs}; exact gap integer={lhs-rhs}")
