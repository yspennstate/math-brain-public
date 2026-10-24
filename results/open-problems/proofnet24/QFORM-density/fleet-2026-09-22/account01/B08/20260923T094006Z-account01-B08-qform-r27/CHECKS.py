from fractions import Fraction
from math import sqrt

# Wide two-eigenvalue spectral-window constants
delta = Fraction(17, 200)
kappa = Fraction(1, 1000)
g = 0.5 - float(delta) - sqrt(2*float(delta))
sigma = g - float(kappa)
H = 8/sqrt(sigma)
assert sigma > 0
assert H < 195

# Exact rational certificate for H<195. With delta=17/200,
# sigma=207/500-sqrt(17)/10. It is enough to prove
# sqrt(17)/10 < 207/500 - 64/38025.
q = Fraction(207,500) - Fraction(64,38025)
assert q > 0
assert (10*q)**2 > 17

# Limiting leverage threshold at fixed kappa=1/1000.
threshold = (sqrt(2*(1-float(kappa)))-1)**2/2
assert threshold > 0.08549 and threshold < 0.08550
assert float(delta) < threshold

# account02/B08 r24 k=1 gate: beta=(3/16)*sqrt(3/5) L.
beta_coeff = Fraction(3,16) * sqrt(Fraction(3,5))
H_k1 = 8/sqrt(float(beta_coeff))
assert H_k1 < 21

# k=2 child gate: c=(1/2)*sqrt(3/5)L.
c_coeff = 0.5*sqrt(3/5)
H_k2 = 195/sqrt(c_coeff)
assert H_k2 < 314

# Inside N3(tau*=1/4,000,000), high child-window leverage >17/200
# forces an off-diagonal child star > L/9000.
tau = Fraction(1, 4_000_000)
star_sq_coeff = Fraction(17,200)*Fraction(1,1000)**2*Fraction(3,20) - tau*tau
assert star_sq_coeff == Fraction(203999, 16_000_000_000_000)
assert star_sq_coeff > Fraction(1,9000)**2

# Partner stress family, k=2, m=2^24.
m = 2**24
delta_p = 3/m
g_p = 0.5-delta_p-sqrt(2*delta_p)
sigma_abs = (g_p-0.001)*0.9
H_stress_k2 = 8/sqrt(sigma_abs)
assert H_stress_k2 < 11.945
assert 4*sqrt(5) < 8.945

print("QFORM_B08_R27_WIDE_TWOEIG_CHECK_PASS")
print("g(17/200) =", g)
print("sigma =", sigma)
print("Hwide =", H)
print("delta_threshold(kappa=1/1000) =", threshold)
print("partner k1 H coeff =", H_k1)
print("partner k2 diffuse-child H coeff =", H_k2)
print("N3 high-leverage star squared coeff =", float(star_sq_coeff))
print("partner k2 stress H =", H_stress_k2)
