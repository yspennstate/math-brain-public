import math

# Scaling two bank variables by sqrt(2):
# D -> D/4, kappa -> kappa/2, s3 -> s/2.
scale = ((1/4)**2 * (1/2) * (1/2)) ** (-1/6)
assert abs(scale - 2.0) < 1e-12

C_base = 6 * 400 ** (1/3)
C_half = 12 * 400 ** (1/3)
C_def_half = 4 * math.pi

# beta0=s0=1, Delta=1/2 gives ((1/2)^5*(1/2))^(-1/6)=2.
assert abs((((0.5)**5 * 0.5) ** (-1/6)) - 2.0) < 1e-12
assert 44.20 < C_base < 44.21
assert 88.41 < C_half < 88.42
assert 12.56 < C_def_half < 12.57

print('QFORM_TWO_BANK_SPECTRAL_LEAKAGE_CHECK_PASS')
print('scale_factor=', scale)
print('base_indefinite=', C_base)
print('half_gap_indefinite=', C_half)
print('definite_beta_half=', C_def_half)
