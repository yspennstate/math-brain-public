from math import sqrt, e

q = 4/3
Delta = 1/2304
assert abs((q-1)*Delta - 1/6912) < 1e-18
sqrtZ = sqrt((q-1)*Delta)
assert abs(sqrtZ - 1/(48*sqrt(3))) < 1e-15

Cvol = 3*e/((3-2*q)*sqrt(q))*Delta**(-1/6)
assert Cvol < 77

pivotE2 = 0.5*sqrtZ
assert abs(pivotE2 - 1/(96*sqrt(3))) < 1e-15

kappa = sqrtZ/16
assert abs(kappa - 1/(768*sqrt(3))) < 1e-15

theta = 1/16
rank_bound = 225/theta
assert rank_bound == 3600
assert sqrt(theta) == 1/4

# B07 r22 scaled payment with Lambda=L^2 and L normalized to 1.
Cr22 = (9*sqrt(3)*e/2) * (6/theta**2)**(1/6) / kappa
assert Cr22 < 95732

core = sqrt(theta/450)*kappa
assert abs(core - 1/(46080*sqrt(6))) < 1e-15

print('QFORM_B08_R26_CHECK_PASS')
print('volume_paid_constant', Cvol)
print('sqrtZ_coefficient', sqrtZ)
print('pivot_E2_coefficient', pivotE2)
print('four_bank_kappa_coefficient', kappa)
print('low_tail_distance_ratio', sqrt(theta))
print('bounded_core_rank_strictly_below', rank_bound)
print('B07_scaled_paid_constant', Cr22)
print('core_row_coefficient', core)
