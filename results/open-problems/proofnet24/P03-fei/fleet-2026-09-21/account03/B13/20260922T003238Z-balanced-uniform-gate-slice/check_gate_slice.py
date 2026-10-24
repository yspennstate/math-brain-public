"""Exact-decimal arithmetic check for the B13 balanced-uniform gate-slice application.

This consumes the certified entropy interval and exact influence of the already
proved 162-input shared-graft construction. It checks only the arithmetic
consequences used in REPORT.md; it does not reconstruct that source witness.
"""
from decimal import Decimal, getcontext

getcontext().prec = 80

H_LO = Decimal("7.014850042680291613033104756310658624299893163")
H_HI = Decimal("7.014850042680291613033104756310658624299893164")
I = Decimal(68013) / Decimal(32768)
C0 = Decimal("6.4548")
C_RO_PROVED = Decimal("6.4573")
C_AND = Decimal("0.0043974201")

den = I - 1
ratio_lo = H_LO / den
ratio_hi = H_HI / den
c_lo = 4 * (ratio_lo - C0)
defect_c0 = C0 * den - H_LO
defect_ro = C_RO_PROVED * den - H_LO
factor = c_lo / C_AND

assert den == Decimal(35245) / Decimal(32768)
assert ratio_lo > Decimal("6.521850083658612443633672199029299526203969333")
assert c_lo > Decimal("0.268200334634449774534688796117198104815877334")
assert factor > Decimal("60.9903")
assert defect_c0 < 0
assert defect_ro < 0

print("I-1 =", den)
print("H/(I-1) in [", ratio_lo, ",", ratio_hi, "]")
print("c_F(C0=6.4548) >=", c_lo)
print("c_F / c_AND >=", factor)
print("D_F(C0=6.4548) <=", defect_c0)
print("D_F(C=6.4573) <=", defect_ro)
print("PASS")
