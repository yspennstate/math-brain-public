from fractions import Fraction
from math import gamma, e, sqrt

# Corollary 5.1 constants at mu=1/48 and the 3/4--1/4 split.
mu = Fraction(1, 48)
E0_lower = Fraction(9, 16)
overlap_each_lower = Fraction(1, 1) / (144 * mu)
assert overlap_each_lower == Fraction(1, 3)

q0_packet = E0_lower / 1296
q1_packet = Fraction(4, 3125) * overlap_each_lower
q2_packet = overlap_each_lower / 128
q3_packet = Fraction(2, 9) * overlap_each_lower

assert q0_packet == Fraction(1, 2304)
assert q1_packet == Fraction(4, 9375)
assert q2_packet == Fraction(1, 384)
assert q3_packet == Fraction(2, 27)
assert min(q0_packet, q1_packet, q2_packet, q3_packet) == Fraction(4, 9375)

# The Pluecker overlap probability estimate uses sum ell_i = 3:
# sum ell_i^2 <= mu * sum ell_i = 3 mu = 1/16 here.
assert 3 * mu == Fraction(1, 16)

# The q=1 aggregate-e3 Fourier constant in (6.8).
def beta(a, b):
    return gamma(a) * gamma(b) / gamma(a + b)

C_q1 = e / (6 * sqrt(2)) * beta(1/6, 1/12)
scale_2304 = 2304 ** (1/6)
C_diffuse_q0 = C_q1 * scale_2304
assert abs(C_diffuse_q0 - 20.554409641631917) < 1e-10
assert C_diffuse_q0 < 21

# q=4/3 permits projection leverage <=2/3 and remains L1-integrable.
q = 4/3
beta_exp = 1/(4*q)
assert beta_exp > 1/6
C_q = e / (6 * sqrt(2*q)) * beta(1/6, beta_exp - 1/6)
C_q43 = C_q * scale_2304
assert abs(C_q43 - 54.17252823972646) < 1e-9
assert C_q43 < 54.173

print("QFORM_B08_R25_CHECK_PASS")
print("q0_packet", q0_packet, float(q0_packet))
print("q1_packet", q1_packet, float(q1_packet))
print("q2_packet", q2_packet, float(q2_packet))
print("q3_packet", q3_packet, float(q3_packet))
print("uniform_packet", min(q0_packet, q1_packet, q2_packet, q3_packet))
print("C_q1_diffuse_q0", C_diffuse_q0)
print("C_q43_diffuse_q0", C_q43)
