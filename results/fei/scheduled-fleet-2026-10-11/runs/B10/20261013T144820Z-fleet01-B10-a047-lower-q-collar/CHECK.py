#!/usr/bin/env python3
from fractions import Fraction as F
s=F(99,2500)
bracket=(F(1,2)-s)*F(2,51)-s*s/(1-s)
assert bracket==F(5027251,306127500)
margin=bracket/F(64)
assert margin==F(5027251,19592160000)
assert margin>F(1,4000)
print("B10/A047 exact rational collar check: PASS")
print("s0 =",s)
print("bracket =",bracket)
print("margin lower bound after dropping 1/ln(2) =",margin)
print("decimal >",float(margin))
print("scope: p in [1/64,49/100], q in [0,1/100]")
