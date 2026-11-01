from fractions import Fraction
from math import sqrt, log

E0 = Fraction(11907, 16384)
T0 = Fraction(14211, 141070336)
t = T0 / E0
assert t == Fraction(6316, 45565443)
assert t < Fraction(1, 7000)

q = Fraction(2048, 31) * (Fraction(1, 7000) + Fraction(1, 2 * 7000**2))
assert q == Fraction(224016, 23734375)
assert q < Fraction(1, 64)

# Pair-law contradiction at d=1/256, m=3/5.
d = Fraction(1, 256)
m = Fraction(3, 5)
F = 2 * ((1 - d - m)**2 - m * (1 - d) / 4)
assert F - d == Fraction(9049, 819200)
assert F > d

# Top-plane leverage and star constants.
ell = Fraction(19, 32)
x2_floor = E0 / 64
row2 = x2_floor * ell
assert row2 == Fraction(226233, 33554432)
small_star2 = row2 - Fraction(1, 1024)
assert small_star2 == Fraction(193465, 33554432)

# E2 and cofactor-bank floors.
z2 = Fraction(31, 2048) * E0**2
assert z2 == Fraction(4395076119, 549755813888)
zia = z2 / 5
assert zia == Fraction(4395076119, 2748779069440)

# Physical pair paid branch at determinant 3/4096.
D = Fraction(3, 4096)
pair_bound = float(D)**(-0.5) * (9.2 + log(10000 * sqrt(float(D))))
assert pair_bound < 547

print('QFORM_B06_R40_CHECK_PASS')
print('T0/E0 =', float(t))
print('tail/top2 ratio majorant =', float(q), '< 1/64')
print('pair-law endpoint excess =', float(F-d))
print('top-plane leverage floor =', float(ell))
print('cross-star norm floor =', sqrt(float(row2)))
print('small-mutual-edge residual-star norm floor =', sqrt(float(small_star2)))
print('small-mutual-edge residual-star product floor =', float(small_star2))
print('Z2 absolute floor =', float(z2))
print('same-anchor cofactor bank floor =', float(zia))
print('same-anchor cofactor Frobenius norm floor =', sqrt(float(zia)))
print('large-mutual-edge density bound =', pair_bound)
