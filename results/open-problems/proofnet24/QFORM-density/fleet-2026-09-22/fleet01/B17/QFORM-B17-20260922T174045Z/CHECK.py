#!/usr/bin/env python3
import math
from fractions import Fraction

A = Fraction(19,32)
B = Fraction(5,4)
C = Fraction(1,4)
assert Fraction(3,20)*A == Fraction(57,640)
assert Fraction(3,20)*B == Fraction(3,16)
assert Fraction(3,20)*C == Fraction(3,80)
assert A-Fraction(1,4) == Fraction(11,32)
assert B-Fraction(1,2) == Fraction(3,4)
assert C-Fraction(1,4) == 0

def F(u):
    if u == 0.0:
        return 1.0
    return math.sqrt(2*math.pi/u)*math.erf(math.sqrt(u)/(2*math.sqrt(2)))

def H1(a):
    if a == 0.0:
        return 1.0
    return F(12*a/(1-a))/math.sqrt(1-a)

worst = -1e100
worst_a = None
min_ratio = 1e100
for i in range(1,200000):
    a = i/200000.0
    rhs = 1.0 - 3.0*a*a/20.0
    err = H1(a)-rhs
    if err > worst:
        worst, worst_a = err, a
    ratio=(1-H1(a))/(a*a)
    min_ratio=min(min_ratio,ratio)
assert worst < 2e-12
assert min_ratio > 0.14999

for y in [0.0,1e-6,1e-3,0.1,1.0,10.0,1e3]:
    Aval=3*math.sqrt(3)*(y*y+12*y+9)/(2*y+3)**3.5
    dlog=2*y*y*(y+12)/((2*y+3)*(y*y+12*y+9))
    assert dlog >= -1e-15
    assert Aval + 1e-14 >= math.exp(-y)

c=3*math.sqrt(2)
weak=c*Fraction(77,80)
partner=4.0630706168060372601254844225935
print("PASS")
print("coefficients", Fraction(57,640), Fraction(3,16), Fraction(3,80))
print("worst_grid_error", worst, "at", worst_a)
print("min_grid_ratio", min_ratio)
print("3sqrt2", c)
print("orientation_free_unit_limit", float(weak))
print("partner_finite_witness", partner)
print("gap_unit_envelope_minus_partner", float(weak)-partner)
