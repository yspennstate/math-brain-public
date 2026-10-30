"""Exact-decimal arithmetic check for the B15 balanced-gate margin deduction.

Inputs are the source-certified entropy interval and exact influence of the
published n=18 balanced seed, plus the documented read-once Gamma cap and
current two-input AND margin floor.  This script does not reconstruct the seed;
that reconstruction and truth-table hash check are supplied by the named
fleet01/B15 source artifact referenced in REPORT.md.
"""
from decimal import Decimal, getcontext

getcontext().prec = 80

H_LO = Decimal("6.776605309005978082519790221891882314787235038")
H_HI = Decimal("6.776605309005978082519790221891882314787235039")
I = Decimal(261) / Decimal(128)
C0 = Decimal("6.4548")
C_AND = Decimal("0.0043974201")

den = I - 1
ratio_lo, ratio_hi = H_LO / den, H_HI / den
c_lo = 4 * (ratio_lo - C0)
c_hi = 4 * (ratio_hi - C0)
D_hi = C0 * den - H_LO  # least favorable for showing negativity
D_after_and = (C0 + C_AND / 4) * den - H_LO
factor_lo = c_lo / C_AND

assert den == Decimal(133) / Decimal(128)
assert c_lo > C_AND
assert D_hi < 0
assert D_after_and < 0
assert C0 + c_lo / 4 == ratio_lo

print("I =", I)
print("I-1 =", den)
print("H/(I-1) in [", ratio_lo, ",", ratio_hi, "]")
print("c_G in [", c_lo, ",", c_hi, "]")
print("c_G / c_AND >", factor_lo)
print("D_G <=", D_hi)
print("D_after_AND_margin <=", D_after_and)
print("required_cap_lower =", C0 + c_lo / 4)
print("PASS")
