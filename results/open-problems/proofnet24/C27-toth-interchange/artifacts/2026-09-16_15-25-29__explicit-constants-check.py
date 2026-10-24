#!/usr/bin/env python3
from fractions import Fraction

Cinf = Fraction(1527*3,8)
Ctorus = Fraction(3*(729+40500),8)
assert Fraction(573,1) > Cinf
assert Fraction(15461,1) > Ctorus
print("EXPLICIT CONSTANT ARITHMETIC")
print(f"infinite-volume coefficient upper bound = {Cinf} < 573")
print(f"torus coefficient upper bound = {Ctorus} < 15461")
print("PASS")
