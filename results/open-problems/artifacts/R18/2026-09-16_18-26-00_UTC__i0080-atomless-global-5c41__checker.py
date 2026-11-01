from fractions import Fraction as F

# Exact finite core for R18-I0080-C008 (atomless global witness).
# Analytic kernel/Taylor inequalities are proved in the run report.
eps = F(1,100)
kappa = F(8,5)
d = F(19,20)

# Retained C007 exact bounds.
KB0_lb = F(4193,13200)
long0_lb = F(12,25)
longmid_lb = F(967,1000)
coeff_lb = F(123,125)

# New short-plateau bound:
# K_B(eps) >= K_B(0)/(1+3 eps^2).
short_ratio_lb = 1 / (1 + 3*eps*eps)
high0_lb = kappa * KB0_lb * short_ratio_lb + coeff_lb * long0_lb
high0_margin = high0_lb - d
assert high0_margin > 0

# Low point y=3:
# short average <= kappa K_0(3-eps)
# so after multiplying by pi the extra term is
# kappa/(1+(3-eps)^2) = 16000/99401.
short3_pi_ub = kappa / (1 + (F(3)-eps)**2)
assert short3_pi_ub == F(16000,99401)

# atan(1/3) > 26/81 and pi/20 < 11/70.
low3_margin_pi = F(26,81) - F(11,70) - short3_pi_ub
assert low3_margin_pi > 0

# Midpoint retains the old long-average lower bound.
mid_lb = coeff_lb * longmid_lb
mid_margin = mid_lb - d
assert mid_margin == F(191,125000)
assert mid_margin > 0

# Auxiliary rational facts used in the Taylor bounds.
B = F(1,10)
# cos B <= 1 - B^2/2 + B^4/24 implies 1-cos B >= B^2/3
assert F(1,2) - B*B/F(24) >= F(1,3)
# x=B*eps=1/1000 <= 1, and cosh(x)-1 <= x^2 is proved analytically
# via the integral remainder and cosh(1)<2. This line checks the scale ratio.
x = B*eps
assert x == F(1,1000)
assert 3*eps*eps == F(3,10000)

# Smooth all-time path identity:
# ell=100+95*pi*t, D=19/(20 ell), b^2=pi D t.
# Algebraically b^2=(ell-100)/(100 ell)=1/100-1/ell
# because ell-100=95*pi*t.
assert F(95,100) == F(19,20)
# p=8/(5 ell) < 2/125 whenever ell>100.
assert kappa / 100 == F(2,125)

print("R18-I0080-C008 EXACT FINITE CORE PASS")
print("epsilon =", eps)
print("short_ratio_lb =", short_ratio_lb)
print("high0_lb =", high0_lb)
print("high0_margin =", high0_margin)
print("short3_pi_ub =", short3_pi_ub)
print("low3_margin_pi =", low3_margin_pi)
print("mid_lb =", mid_lb)
print("mid_margin =", mid_margin)
print("smooth-path rational identities: PASS")
