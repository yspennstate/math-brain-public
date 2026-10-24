#!/usr/bin/env python3
"""Exact certificate for the B7 two-dominant/Jensen-Shannon obstruction.

For Z=B1+B2 with iid Bernoulli(p), r=1, and an independent fair J,
let Delta(p)=H(Z+J)-H(Z) and E(p)=2 p(1-p) Delta(p).
Direct symbolic differentiation gives

    E''(2/5) = 19/14 + (62/25) log(7/12)
              = 19/14 - (62/25) log(12/7).

This script certifies E''(2/5)>0 without floating-point logarithms.
Set t=(x-1)/(x+1)=5/19 for x=12/7. Then
log x = 2*atanh(t) = 2*sum_{j>=0} t^(2j+1)/(2j+1).
Bounding every denominator in the tail j>=2 by 5 gives an exact rational
upper bound.
"""
from fractions import Fraction

# Exact threshold equivalent to E''(2/5)>0.
target = Fraction(19, 14) * Fraction(25, 62)  # 475/868

t = Fraction(5, 19)  # (12/7 - 1)/(12/7 + 1)
# log(12/7) = 2[t + t^3/3 + t^5/5 + t^7/7 + ...]
# For j>=2, 1/(2j+1) <= 1/5, hence tail <= t^5/(5(1-t^2)).
log_upper = 2 * (t + t**3 / 3 + (t**5 / 5) / (1 - t**2))

assert log_upper < target

# A purely rational positive lower bound for E''(2/5):
# E'' = (62/25) * (target - log(12/7))
#      > (62/25) * (target - log_upper).
fpp_lower = Fraction(62, 25) * (target - log_upper)
assert fpp_lower > 0

print(f"target_for_log_12_over_7={target.numerator}/{target.denominator}")
print(f"rigorous_log_upper={log_upper.numerator}/{log_upper.denominator}")
print(f"certified_Epp_lower={fpp_lower.numerator}/{fpp_lower.denominator}")
print("PASS: E''(2/5) > 0, so the isolated 2p(1-p)*Jensen-Shannon excess is not universally concave.")
