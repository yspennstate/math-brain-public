import math

K3 = 2*math.sqrt(2)
K2 = 2.0
D = math.pi*math.sqrt(2) * (6.0**(3.0/4.0)) * ((2*math.pi)**0.25) * ((K3*K2)**0.25)
C = (5/math.pi) * (D/8.0)**(4.0/5.0)
C_exact = 5*(2**(-7/10))*(3**(3/5))
C_out = C * (5/4)*(2**(3/10))
C_out_exact = 25*(3**(3/5))*2**(-12/5)
rho0 = math.sqrt(29/3072)
fixed_aff = C * 64**(1/5) * rho0**(-2/5)
fixed_out = C_out * 64**(1/5) * rho0**(-2/5)
print('D=', repr(D))
print('C=', repr(C))
print('C_exact=', repr(C_exact))
print('C_out=', repr(C_out))
print('C_out_exact=', repr(C_out_exact))
print('rho0=', repr(rho0))
print('fixed_aff=', repr(fixed_aff))
print('fixed_out=', repr(fixed_out))
assert abs(C-C_exact) < 1e-12
assert abs(C_out-C_out_exact) < 1e-12
assert C < 5.951
assert C_out < 9.157
assert fixed_aff < 34.735
assert fixed_out < 53.455
print('QFORM_RANK2_KERNEL_AFFINE_CHECK_PASS')
