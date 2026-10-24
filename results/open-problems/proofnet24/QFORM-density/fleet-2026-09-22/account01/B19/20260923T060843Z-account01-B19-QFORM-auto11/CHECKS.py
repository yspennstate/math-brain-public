import math

C_star = 2**(15/4) * 3**(-3/8)
rho0 = math.sqrt(29/3072)
fixed = C_star * 64**0.25 * rho0**(-3/8)
M = 2*math.sqrt(6)*math.pi**(1/3)
A = 2**(10/3)*math.sqrt(3)*math.pi**(4/3)
C_from_A = (4/math.pi)*(A/6)**(3/4)

assert abs(C_star-C_from_A) < 1e-12
assert C_star < 8.912
assert fixed < 60.42
print('C_star=', repr(C_star))
print('rho0=', repr(rho0))
print('fixed_threshold_bound=', repr(fixed))
print('M=', repr(M))
print('A=', repr(A))
print('QFORM_B19_AUTO11_NEARNULL_CHECK_PASS')
