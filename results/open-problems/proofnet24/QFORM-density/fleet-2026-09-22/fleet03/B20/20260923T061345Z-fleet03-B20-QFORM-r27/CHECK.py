from math import pi, sqrt

# Exact constants used in QFORM-RANK2-CROSS-NULL-TRANSVERSE-L3-v1.
K3 = 2*sqrt(2)
K2 = 2
N0 = (4*pi)**(1/3)*sqrt(6)
A0 = pi*sqrt(2)*(4**(2/3))*N0
C0 = (4/pi)*(A0/6)**(3/4)
rho = sqrt(29/3072)
branch = C0*(1/64)**(-1/4)*rho**(-3/8)
partner = (103680**(1/3))*(2**(7/6))
near_kernel = sqrt(2)/64

print('N0=', N0)
print('A0=', A0)
print('C0=', C0)
print('rho=', rho)
print('compound_branch_bound=', branch)
print('fleet04_B20_partitioned_bound=', partner)
print('near_kernel_norm=', near_kernel)

assert N0 < 5.695
assert A0 < 63.756
assert C0 < 7.5
assert branch < 51
assert partner < 105.463
assert near_kernel < 0.022098
print('QFORM_B20_R27_NULL_TRANSVERSE_CHECK_PASS')
