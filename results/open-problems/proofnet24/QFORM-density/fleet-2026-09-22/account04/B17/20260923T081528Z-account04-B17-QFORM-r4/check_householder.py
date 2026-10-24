#!/usr/bin/env python3
"""Deterministic checks for QFORM-HOUSEHOLDER-CUBE-CONE-EXACT-v1."""
from fractions import Fraction
import math

A = [
    [Fraction(1,3), Fraction(-2,3), Fraction(-2,3)],
    [Fraction(-2,3), Fraction(1,3), Fraction(-2,3)],
    [Fraction(-2,3), Fraction(-2,3), Fraction(1,3)],
]

def matmul(X,Y):
    return [[sum(X[i][k]*Y[k][j] for k in range(3))
             for j in range(3)] for i in range(3)]

I = [[Fraction(int(i==j),1) for j in range(3)] for i in range(3)]
assert matmul(A,A)==I
assert sum(A[i][i] for i in range(3))==1
assert all(A[i][j] != 0 for i in range(3) for j in range(3))

a=1/math.sqrt(3)
b=math.sqrt(2/3)
closed=6*math.sqrt(3)*math.atanh((math.sqrt(2)-1)/math.sqrt(3))

# Composite Simpson check of (3/2) int_{-pi/3}^{pi/3} 1/(a+b cos t) dt.
N=200000
lo=-math.pi/3
hi=math.pi/3
h=(hi-lo)/N
s=1/(a+b*math.cos(lo))+1/(a+b*math.cos(hi))
for k in range(1,N):
    val=1/(a+b*math.cos(lo+k*h))
    s+=(4 if k%2 else 2)*val
numeric=1.5*h*s/3
assert abs(numeric-closed)<2e-12
assert closed < math.pi < 3*math.sqrt(2)

print("QFORM_HOUSEHOLDER_CUBE_CHECK_PASS")
print(f"p0_closed={closed:.16f}")
print(f"p0_simpson={numeric:.16f}")
print(f"three_sqrt_two={3*math.sqrt(2):.16f}")
