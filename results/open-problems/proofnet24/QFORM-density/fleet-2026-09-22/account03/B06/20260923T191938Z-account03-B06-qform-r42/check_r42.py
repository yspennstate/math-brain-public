from fractions import Fraction
from math import sqrt

E0 = Fraction(11907, 16384)
M0sq = Fraction(19, 32) * E0 / 64
R2 = M0sq - Fraction(1, 1024)
assert M0sq == Fraction(226233, 33554432)
assert R2 == Fraction(193465, 33554432)
assert R2 / 2 == Fraction(193465, 67108864)

paid = 4 / sqrt(float(R2))
assert paid < 52.679

partner_currency = Fraction(61, 4 * 1728 * 64)
partner_bound = 12 * float(partner_currency) ** (-1/3)
assert partner_bound < 232.274

# Layer-cake identity used in Theorem 2.1.  Splitting at t=2*sqrt(H):
# int_0^inf min(1,4H/t^2) dt = 2sqrt(H)+2sqrt(H)=4sqrt(H).
for H in [Fraction(1,100), Fraction(1,1), Fraction(25,4), Fraction(100,1)]:
    t0 = 2 * sqrt(float(H))
    exact = t0 + 4 * float(H) / t0
    assert abs(exact - 4 * sqrt(float(H))) < 1e-12

print('QFORM_B06_R42_CHECK_PASS')
print('E0=', float(E0))
print('M0sq=', float(M0sq))
print('R2=', float(R2))
print('R2_half=', float(R2/2))
print('zero_core_paid_bound=', paid)
print('partner_paid_bound=', partner_bound)
