from fractions import Fraction
from math import e, sqrt

rho = Fraction(1, 25)
delta = Fraction(7, 32)
sigma = delta - rho
gamma = Fraction(7, 10) * sigma
a = rho / gamma

y = Fraction(5, 14) - a*a
ridge_certificate = y*y - Fraction(4, 7)*a*a
assert sigma == Fraction(143, 800)
assert gamma == Fraction(1001, 8000)
assert a == Fraction(320, 1001)
assert y == Fraction(510915, 2004002)
assert ridge_certificate == Fraction(26508646025, 4016024016004)
assert ridge_certificate > 0
assert (1/sqrt(7) + float(a))**2 < 0.5

theta_floor = Fraction(300, 149)
assert theta_floor > 2
assert theta_floor / (theta_floor - 2) == 150

ridge_bound = sqrt(e)/(sqrt(2)*float(gamma))*150
assert ridge_bound < 1398

partner_packet = float(rho) * sqrt((1/32)/2)
assert abs(partner_packet - 1/200) < 1e-15

Cstar = 1 + 44*10**(15/2)
pivot_bound = Cstar*sqrt(200)
assert pivot_bound < 1.968e10

print({
    "rho": float(rho),
    "delta": float(delta),
    "sigma": float(sigma),
    "gamma": float(gamma),
    "rho_over_gamma": float(a),
    "ridge_diag_upper": (1/sqrt(7)+float(a))**2,
    "ridge_certificate": str(ridge_certificate),
    "theta_floor": float(theta_floor),
    "ridge_bound": ridge_bound,
    "partner_packet": partner_packet,
    "pivot_bound": pivot_bound,
})
