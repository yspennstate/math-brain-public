from fractions import Fraction
import math

# Deterministic arithmetic checks for QFORM-DEPENDENT-PROJECTION-ALL-HOLDER-BARRIER-v1.
eps = Fraction(1, 64)
D = (1 - eps + eps*eps) / 2
Dmin = Fraction(4033, 8192)
assert D == Dmin

# For B=[[eps,1/sqrt(2)],[1/sqrt(2),(1-eps)/2]],
# ||B||_F^2 = 5/4-eps/2+5 eps^2/4 <=5/4 on [0,1/64].
# sigma_min = |det B|/sigma_max >= 2D/sqrt(5) > 7/16,
# using sqrt(5)<9/4 and (8/9)Dmin=4033/9216>7/16=4032/9216.
kappa_lower = Fraction(7, 16)
assert Fraction(8,9)*Dmin > kappa_lower

coarse_pairlog = 8*math.sqrt(5)*float(Dmin*kappa_lower)**(-0.25)
ruled = math.pi*math.sqrt(2)
F_threshold = 256/(math.pi*float(eps))
G_threshold = 512/(9*math.pi)
carrier_radius = math.sqrt(1+float(eps)**2)

print(f"eps={float(eps):.12f}")
print(f"carrier_spectrum=[{-carrier_radius:.12f},1,{carrier_radius:.12f}]")
print(f"Dmin={float(Dmin):.12f}")
print(f"kappa_lower={float(kappa_lower):.12f}")
print(f"pairlog_bound_coarse={coarse_pairlog:.12f}")
print(f"ruled_positive_side={ruled:.12f}")
print(f"F_stationary_threshold={F_threshold:.12f}")
print(f"G_stationary_threshold={G_threshold:.12f}")
print("STATUS=PASS")
