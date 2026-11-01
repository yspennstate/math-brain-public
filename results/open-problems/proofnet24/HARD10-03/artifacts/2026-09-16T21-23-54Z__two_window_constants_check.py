from fractions import Fraction

# Exact arithmetic self-check for constants used in NEW-L108.
# This does not verify the probabilistic proof; it only checks the finite inequalities.

# For x = beta^(1/4) >= 4:
# (2R+1)^3 <= (13x/4)^3 and (2R+3)^3 <= (15x/4)^3.
# The first term has one less power of x, so x^3 <= x^4/4.
coef = Fraction(13, 4) ** 3 / 4 + 6 * Fraction(15, 4) ** 3
assert coef < 325

# c_* = pi^(3/2)/64 < pi^2/64 < (22/7)^2/64 = 121/784.
# Also (beta/2)^(-3/2) < 3 beta^(-3/2), since 2^(3/2) < 3.
heat_constant = Fraction(121, 784) * 3 * coef
assert heat_constant < 151

# At beta_0=10^8, beta^(-1/2)=1/10^4 and G>=100.
# Since e>2, exp(-G/5) <= exp(-20) < 2^(-20).
bad_poly = Fraction(151, 10_000)
bad_exp_upper = Fraction(12, 2**20)
total_bad_upper = bad_poly + bad_exp_upper
assert total_bad_upper < Fraction(19, 1250)
assert 1 - total_bad_upper > Fraction(1231, 1250)

print("coef =", coef, float(coef))
print("heat_constant =", heat_constant, float(heat_constant))
print("heat_constant < 151 =", heat_constant < 151)
print("bad_poly =", bad_poly, float(bad_poly))
print("bad_exp_upper =", bad_exp_upper, float(bad_exp_upper))
print("total_bad_upper =", total_bad_upper, float(total_bad_upper))
print("total_bad_upper < 19/1250 =", total_bad_upper < Fraction(19, 1250))
print("success_lower =", 1-total_bad_upper, float(1-total_bad_upper))
print("success_lower > 1231/1250 =", 1-total_bad_upper > Fraction(1231,1250))
print("ALL_EXACT_CHECKS_PASS")
