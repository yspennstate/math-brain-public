from math import e, sqrt

Cct = 103680 ** (1/3)
near = Cct * e**(2/3) * 2**(1/6) * 12**(1/3)
far = 16*sqrt(30) * (24*12)**(1/4)
partner_mid = 34*sqrt(9)

print(f'C_cross_transverse={Cct:.15f}')
print(f'near_null_branch={near:.15f}')
print(f'non_small_pivot_branch={far:.15f}')
print(f'partner_e_minus8_to_1={partner_mid:.15f}')

assert near < 236
assert far < 362
assert partner_mid == 102
assert 1/24 < (1/12)/2 + 1e-15
assert 1/12 > 0
print('QFORM_B19_R21_GROUPED_PAYMENT_CHECK_PASS')
