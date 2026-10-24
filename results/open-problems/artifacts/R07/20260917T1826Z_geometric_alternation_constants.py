from fractions import Fraction

# Exact-rational self-check for the canonical geometric alternating-fence example.
# Analytic inputs used on the proof page: Mills' inequality
#   P(Z >= z) <= exp(-z^2/2)/(z*sqrt(2*pi))
# and the elementary strict bounds exp(x) > 1+x+x^2/2 for x>0, pi>3.

a = Fraction(3, 4)
r = Fraction(1, 2)  # e^{-P/2} when P = log 4
s2 = 1 - r*r
z2 = a*a*(1+r)*(1+r)/s2
half_z2 = z2/2

# exp(27/32) > 1 + 27/32 + (27/32)^2/2 > 2,
# hence exp(-27/32) < 1/2.
exp_lower = 1 + half_z2 + half_z2*half_z2/2

# (z*sqrt(2*pi))^2 = z^2*2*pi > z^2*6, using pi>3.
denom_sq_lower = z2 * 2 * 3

assert s2 == Fraction(3, 4)
assert z2 == Fraction(27, 16)
assert half_z2 == Fraction(27, 32)
assert exp_lower == Fraction(4505, 2048)
assert exp_lower > 2
assert denom_sq_lower == Fraction(81, 8)
assert denom_sq_lower > 4

print("a =", a)
print("r =", r)
print("1-r^2 =", s2)
print("z^2 =", z2)
print("z^2/2 =", half_z2)
print("1+x+x^2/2 at x=27/32 =", exp_lower, "> 2")
print("lower bound on (z*sqrt(2*pi))^2 using pi>3 =", denom_sq_lower, "> 4")
print("Mills: q_alt < (1/2)/2 = 1/4 = exp(-log 4)")
print("Therefore kappa_alt > 1")
print("PASS")
