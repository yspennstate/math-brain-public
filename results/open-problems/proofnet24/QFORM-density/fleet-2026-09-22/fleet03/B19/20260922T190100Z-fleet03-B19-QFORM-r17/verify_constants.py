from fractions import Fraction
from math import e, pi, sqrt

E = Fraction(1, 256)
packet_det = E / 16
assert packet_det == Fraction(1, 4096)

# If C is the 3-row packet, Pi_3(C)=sqrt(det(CC^T)).
# The one-sided exact-rank theorem is 3*sqrt(e)*Pi^(-1/3).
# With det >= 1/4096, Pi >= 1/64, hence Pi^(-1/3)<=4.
bound = 12 * sqrt(e)
assert bound < 19.785

# Rank-exactly-three packet has det >= E/4.
rank3_bound = 3 * sqrt(e) * 2 ** (5/3)
assert rank3_bound < 15.704

# Near-coloop zero-self endpoint multiplier from the fresh pair currency.
delta = Fraction(4191, 281804800)
zero_self_multiplier = sqrt(pi) * float(Fraction(281804800, 4191)) ** 0.25
assert zero_self_multiplier < 28.542

print('QFORM_B19_R17_CONSTANT_CHECK_PASS')
print('E =', E)
print('packet_det =', packet_det)
print('12*sqrt(e) =', bound)
print('rank3_endpoint =', rank3_bound)
print('near_coloop_delta =', delta)
print('zero_self_multiplier / C_lin^2 / gamma^-1 =', zero_self_multiplier)
