import math

C_riesz_cross = 4*math.sqrt(2)*math.exp(0.25)
C_mixed_base = 2**(21/8)*math.exp(0.25)
scale = 16**0.25 * (2**24/81)**0.125
C_eta_1_16 = C_mixed_base * scale * 16**0.125
C_n4_1_16 = 2**(19/4)*math.exp(0.25)*scale

print('C_riesz_cross', repr(C_riesz_cross))
print('C_mixed_base', repr(C_mixed_base))
print('target_scale_multiplier', repr(scale))
print('C_eta_1_16', repr(C_eta_1_16))
print('C_n4_1_16', repr(C_n4_1_16))

assert C_riesz_cross < 7.264
assert C_mixed_base < 7.921
assert C_eta_1_16 < 103.479
assert C_n4_1_16 < 319.173

# Deterministic mixed-packet implications, normalized D0=1.
# If Bmix>=1/2 and N4<1/16, then M4>Bmix^2/N4>4.
D0 = 1.0
Bmix = 0.5
N4 = 1/16
assert Bmix**2/N4 == 4.0

# If additionally L<1/2, the bad-coordinate fourth-power mass is <4L<2,
# leaving >2 units in the sign-coherent good bank once M4>4.
L = 0.5
assert 4*L == 2.0

print('QFORM_B06_R40_CHECK_PASS')
