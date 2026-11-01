#!/usr/bin/env python3
# R02 KLS exact self-check, 2026-09-16T1504Z_5d7c3e91.
# Finite/symbolic core only. The asymptotic probability theorem is proved in the report.

from fractions import Fraction
from itertools import product
from math import comb
import sympy as sp

print("R02 KLS product-localization horizon checker")

# C004 / X004 exact constants.
y=sp.symbols("y", real=True)
a=sp.Rational(1,3)
b=sp.Rational(2,5)
rate=1-y

# At t=0 the posterior law on [-1,infty) is a shifted Exp(rate),
# hence variance = rate^{-2}.
v0=sp.simplify(rate**-2)
assert sp.simplify(v0.subs(y,a)-sp.Rational(9,4))==0
assert sp.simplify(v0.subs(y,b)-sp.Rational(25,9))==0
assert sp.Rational(9,4)>2

# The witness interval width and Gaussian exponent at
# t_n=1/(10 log n): exp(-b^2/(2t_n))=n^{-4/5}.
assert sp.simplify(b-a-sp.Rational(1,15))==0
gaussian_power=sp.simplify(b*b*sp.Rational(10,2))
assert gaussian_power==sp.Rational(4,5)
assert gaussian_power<1

print("C004 constants PASS")
print("posterior limit variance interval:", v0.subs(y,a), "to", v0.subs(y,b))
print("witness interval width:", b-a)
print("Gaussian n-power:", gaussian_power)

# R02 directed audit of R03-C233, conditional on R03-C232's
# independently archived exhaustive type classification.
types=[
    ((1,1,1,1,1,1),20,32),
    ((2,2,1,1,1,1),14,comb(6,2)*32),
    ((3,1,1,1,1,1),10,6*32),
    ((3,2,2,1,1,1),10,6*comb(5,2)*32),
]
eps=list(product((-1,1),repeat=6))
for coeffs,atom_expected,directions in types:
    atom=sum(sum(c*e for c,e in zip(coeffs,s))==0 for s in eps)
    assert atom==atom_expected
    print("R03 type",coeffs,"zero sign columns",atom,"directions",directions)

assert types[0][2]==32
assert types[1][2]==480
assert types[2][2]==192
assert types[3][2]==1920
assert types[2][2]+types[3][2]==2112

# Fixed labelled six-row-set union bound:
# 32(20/64)^n + 480(14/64)^n + 2112(10/64)^n.
assert Fraction(20,64)==Fraction(5,16)
assert Fraction(14,64)==Fraction(7,32)
assert Fraction(10,64)==Fraction(5,32)

# Relative to 2^{-n}, bases double and all are <1.
bases=[Fraction(5,8),Fraction(7,16),Fraction(5,16)]
assert all(q<1 for q in bases)

print("R02-AUDIT-R03-C233-02 PASS")
print("fixed-row union coefficients: 32, 480, 2112")
print("target-scale bases:", *bases)
print("ALL CHECKS PASS")
