#!/usr/bin/env python3
"""
R07 exact-arithmetic self-check for the explicit constants in
R07-GH-C08/C09 (ordinary Exp(1) FPP).

This script does not prove the probabilistic theorems; their full analytic
proof is in the immutable run report. It certifies every finite/rational
constant comparison used there.

No floating point arithmetic is used for the assertions.
"""
from fractions import Fraction

# Elementary rational bounds invoked analytically in the proof:
#   8/3 < e < 11/4.
E_LO = Fraction(8,3)
E_HI = Fraction(11,4)

# a = 1/(12e).  The SAW union bound uses 3 e a = 1/4 exactly.
# With ell >= 66 n, a ell /2 >= n follows from e < 11/4:
assert Fraction(66, 24) / E_HI == 1

# Tail sum for the straight-path Gamma upper tail:
# 1/(1-exp(-1/(24e))) <= 1+24e < 67.
assert 1 + 24*E_HI == 67

# SAW lower-tail count:
# 4*3^(m-1) * (e a)^m = (4/3)*(1/4)^m,
# and summing m>=n gives (16/9)*4^-n <= 4/9 for n>=1.
assert Fraction(16,9)*Fraction(1,4) == Fraction(4,9)

# Hence E T_n >= (5/9) * a n = 5/(108e) n.

# Expected geodesic length bound:
# 66 n + at most 67 + <1 <= 134 n for n>=1.
assert 66 + 67 + 1 == 134

# M=16 high-weight geodesic contribution:
# alpha_16 = 17 e^-16/(1-e^-16)
# < 34*(3/8)^16 using e>8/3 and e^-16<1/2.
alpha_upper = 34 * Fraction(3,8)**16

# Need 134*alpha_upper <= 5/(216 e).
# Since e < 11/4, 5/(216e) > 5/594.
high_tail_upper = 134 * alpha_upper
half_mean_lower = Fraction(5,594)
assert high_tail_upper < half_mean_lower

# Consequently the geodesic mass carried by edges X_e<=16 is at least
# 5/(216 e) n, and A=sum_{e in gamma}(X_e wedge 1) has
# E A >= 5/(3456 e) n.

# Cauchy plus E|gamma|<=134n:
# E sum (X_e wedge 1)^2 >=
# 25/[134*3456^2*e^2] n.
# Using e<11/4 gives the rational lower constant:
c_depth = Fraction(25*16, 134 * 3456**2 * 121)
assert c_depth == Fraction(25, 12103686144)

# Fixed depth delta=10^-7:
# N_delta >= sum (R_e wedge1)^2 - delta^2 |gamma|
# in expectation, so coefficient >= c_depth -134*10^-14.
delta_loss = Fraction(134, 10**14)
fixed_depth_coeff = c_depth - delta_loss
assert fixed_depth_coeff > Fraction(2,10**9)

# Initial refresh-covariance derivative:
# -C_n'(0+) >= (1/(16e))*c_depth*n.
# e<11/4 => 1/(16e)>1/44.
initial_derivative_coeff = c_depth / 44
assert initial_derivative_coeff > Fraction(4,10**11)

print("R07 deep-edge exact constant checker")
print("c_depth =", c_depth, "~", float(c_depth))
print("delta_loss =", delta_loss)
print("fixed_depth_coeff =", fixed_depth_coeff, "~", float(fixed_depth_coeff))
print("initial_derivative_coeff lower =", initial_derivative_coeff, "~", float(initial_derivative_coeff))
print("high_tail_upper =", high_tail_upper, "~", float(high_tail_upper))
print("half_mean_lower rational proxy =", half_mean_lower, "~", float(half_mean_lower))
print("PASS")
