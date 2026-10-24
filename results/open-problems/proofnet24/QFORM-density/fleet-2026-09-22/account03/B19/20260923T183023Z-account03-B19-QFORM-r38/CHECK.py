from math import comb, sqrt

m=124
N=comb(m,2)
sigma=1/480
tau=1/64
S=sigma/sqrt(N)
C=3*(2**(5/6))*((S*tau)**(-1/3))
print('N=',N)
print('S_lower=',repr(S))
print('density_bound=',repr(C))
assert N==7626
assert C < 743

# Exact comparison used in the report: if a projected residual row carries > half
# of total transverse Frobenius energy, rank-three crossing improves the constant.
ratio=(3*(2**(2/3)))/(3*(2**(5/6)))
print('rank3_to_grouped_constant_ratio=',repr(ratio))
assert ratio < 1
print('QFORM_B19_R38_CHECK_PASS')
