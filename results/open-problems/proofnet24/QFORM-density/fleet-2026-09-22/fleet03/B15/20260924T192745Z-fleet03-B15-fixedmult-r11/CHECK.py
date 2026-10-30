from fractions import Fraction as F
from math import factorial

# Exact arithmetic for fleet03/B15 candidate s8 < 291 retune.

# Inner five-direction half-potential retune.
d=F(11,40)
p=F(9,1000)
h=F(107,1000)
assert p+d*d == F(677,8000)
assert F(677,8000) < F(291,1000)**2
assert 1-d-F(291,1000)-4*h == F(3,500)
assert d+h < 1
assert 25**8 < 2*23**8

e_partial_6=sum(F(1,factorial(k)) for k in range(7))
assert e_partial_6 + F(1,4410) < F(68,25)
c2_majorant_sq=F(64*23**2*68*2000,25**2*25*107)
assert c2_majorant_sq < F(105,2)**2
assert p > F(32,105)**4

x=F(347,500)
assert sum(x**k/F(factorial(k),1) for k in range(5)) > 2
x=F(161,100)
assert sum(x**k/F(factorial(k),1) for k in range(8)) > 5
C_upper=F(22,7)+4*F(347,500)+8+8*F(161,100)
assert C_upper < 27
assert F(27**2,1)/d < F(103,2)**2

# Outer retune.
eta=F(13,399)
kappa=F(1,178)
u=eta+eta*eta
assert u == F(5356,159201)
assert kappa < F(1,13)**2
assert u < F(23,125)**2

# Order-one completion restricted-rank contradiction.
rank_margin=1-eta-F(23,125)-4*F(1,13)
assert rank_margin == F(308449,648375)
assert rank_margin > 0

# Collar: eps=sqrt(18*kappa)=sqrt(9/89)<319/1000.
assert F(9,89) < F(319,1000)**2
delta_lower=1-3*eta-2*F(319,1000)*(1-eta+F(23,125))
assert delta_lower == F(4180787,24937500)
assert delta_lower > F(1,6)

# Two-high leverage exclusion.
two_high_margin=F(1,216)-4*u*u
assert two_high_margin == F(20726611,202759667208)
assert two_high_margin > 0

# One-high diagonal-dominance closure.
one_high_margin=((F(2,5)-eta)/2)**2-u
assert one_high_margin == F(563,5306700)
assert one_high_margin > 0

# Terminal receiver: delta>1/6 => g>1/72 => W_dis>1/5400.
assert 5400 < 5**6

# Scalar pivot <291.
scalar_sq_margin=F(291)**2-F(105,2)**2*F(399,13)
assert scalar_sq_margin == F(4437,52)
assert scalar_sq_margin > 0

# LPP-sharpened large-V3 branch:
# 2*6^(4/3)*sqrt(178) < 291 iff sixth powers compare.
large_margin=291**6-(2**6)*(6**8)*(178**3)
assert large_margin == 989059098393
assert large_margin > 0

# Old ephemeral <348 rational certificate was false as written.
old_majorant=6*F(14143,10000)*F(27183,10000)*F(257,200)*F(2937,250)
assert old_majorant == F(870557078411163,2500000000000)
assert old_majorant > 348

print("QFORM_B15_S8_291_EXACT_CHECK_PASS")
print("rank_margin =", rank_margin)
print("delta_lower =", delta_lower)
print("two_high_margin =", two_high_margin)
print("one_high_margin =", one_high_margin)
print("scalar_sq_margin =", scalar_sq_margin)
print("large_sixth_power_margin =", large_margin)
print("old_348_majorant =", old_majorant)
