#!/usr/bin/env python3
"""R13 run 4 exact self-check for the pointwise certified metric envelope.

Uses the elementary RMS signing bound B(n)<=sqrt(n) and the Guo-Fang-Lu
constant B(n)<3*sqrt(2*pi).  The rational Archimedean bounds
333/106 < pi < 355/113 certify the exact integer crossover.
"""
from fractions import Fraction

lo_pi=Fraction(333,106)
hi_pi=Fraction(355,113)

# Compare squared bounds: n versus 18*pi.
assert Fraction(56,1) < 18*lo_pi
assert 18*hi_pi < Fraction(57,1)

print("R13 Komlos run-4 metric-envelope checker")
print("56 < 18*pi < 57 certified from 333/106 < pi < 355/113: PASS")
print("Thus min(sqrt(n),3*sqrt(2*pi)) uses sqrt(n) for n<=56 and the constant for n>=57: PASS")
print("ALL_EXACT_CHECKS_PASS")
