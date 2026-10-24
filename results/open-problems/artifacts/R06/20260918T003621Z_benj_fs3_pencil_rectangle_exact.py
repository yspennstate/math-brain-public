#!/usr/bin/env python3
"""Exact finite self-check for R06 BENJ-2026-FS3.

For p1=(0,0), p2=(1,0), p3=(0,1), use the two line-pencil
parameters A,B in {1,2}.  The intersection with barycentric coordinates
(lambda1,lambda2,lambda3) proportional to (1,A,B) has
    r1(A,B) = sqrt(A^2+B^2)/(1+A+B).
Any separable predictor f(A)+g(B)+c has zero 2x2 mixed difference.
The Euclidean r1 mixed difference is
    Delta = r1(1,1)+r1(2,2)-r1(1,2)-r1(2,1)
          = 11*sqrt(2)/15 - sqrt(5)/2.
We certify Delta<0 by squaring the positive quantities
22*sqrt(2) and 15*sqrt(5): 968 < 1125.
"""

left_sq = 22**2 * 2
right_sq = 15**2 * 5

assert left_sq == 968
assert right_sq == 1125
assert left_sq < right_sq

print(f"(22*sqrt(2))^2 = {left_sq}")
print(f"(15*sqrt(5))^2 = {right_sq}")
print("Delta = 11*sqrt(2)/15 - sqrt(5)/2 < 0")
print("SEPARABLE_PENCIL_RECTANGLE_OBSTRUCTION_PASS")
