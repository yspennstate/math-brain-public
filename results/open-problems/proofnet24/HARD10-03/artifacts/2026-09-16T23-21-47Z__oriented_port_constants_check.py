from fractions import Fraction

S_MIN = 4096
assert Fraction(1, 8) + Fraction(1, S_MIN) < Fraction(9, 64)
central_strip = Fraction(4, 9) * Fraction(9, 64)
assert central_strip == Fraction(1, 16)

u0 = 8
assert u0**4 > 256*u0 + 32
# f(u)=u^4-256u-32 has f'(u)=4u^3-256>0 for u>=8.
assert 4*u0**3 - 256 > 0

longitudinal = Fraction(7, 16)
transverse = Fraction(7, 8)
endpoint = longitudinal * transverse * transverse
assert endpoint == Fraction(343, 1024)

# From the elementary inequality e>2, each 6 e^{-32} < 6/2^32.
two_confinement_failures = Fraction(12, 2**32)
success = endpoint - two_confinement_failures
assert success == Fraction(359661565, 1073741824)
margin = success - Fraction(1, 3)
assert margin == Fraction(5242871, 3221225472)
assert margin > 0

print("S_MIN =", S_MIN)
print("d/S upper =", Fraction(1, 8) + Fraction(1, S_MIN), "< 9/64")
print("central strip bound =", central_strip)
print("scale-separation base:", u0**4, ">", 256*u0 + 32)
print("endpoint lower =", endpoint)
print("two confinement failures upper (using e>2) =", two_confinement_failures)
print("success lower =", success)
print("success lower decimal =", float(success))
print("margin over 1/3 =", margin)
print("ALL_EXACT_CHECKS_PASS")
