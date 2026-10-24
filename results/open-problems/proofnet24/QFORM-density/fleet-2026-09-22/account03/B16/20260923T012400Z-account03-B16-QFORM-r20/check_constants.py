from fractions import Fraction
import math

alpha = beta = delta = Fraction(1, 8)
c = Fraction(7, 8)
H2 = c - alpha*alpha
assert H2 == Fraction(55, 64)

g2 = (alpha*beta + delta) / H2
assert g2 == Fraction(9, 55)

rho = Fraction(1, 6)
s2 = Fraction(1, 4)
lev = (g2 + s2) / (1-rho)
assert lev == Fraction(273, 550)
assert lev < Fraction(1, 2)

Dmin = H2*(1-rho*rho)
assert Dmin == Fraction(1925, 2304)

Cstar = 103680**(1/3)
C_projection_packet = Cstar * 2**(2/3) * float(Dmin)**(-1/3)
C_mixed_fresnel = 3 * 2**(4/3) * float(Dmin)**(-1/3)
assert C_projection_packet < 79.178
assert C_mixed_fresnel < 8.027

partner_threshold = 12 * (2**-12)**(-1/6)
assert abs(partner_threshold-48) < 1e-12

print('H2_lower=', H2)
print('g_inf_sq_upper=', g2)
print('augmented_leverage_upper=', lev)
print('curvature_product_lower=', Dmin)
print('projection_packet_constant=', C_projection_packet)
print('mixed_fresnel_constant=', C_mixed_fresnel)
print('partner_d_ge_2^-12_constant=', partner_threshold)
print('partner_one_sheet_constant=', math.pi*math.sqrt(2))
print('STATUS=PASS')
