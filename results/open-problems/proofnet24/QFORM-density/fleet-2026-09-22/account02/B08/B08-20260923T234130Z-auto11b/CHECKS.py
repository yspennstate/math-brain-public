import math

sstar = 1/(64*math.sqrt(896))
p0 = sstar*sstar/64
d0 = 1/64
crude_gate = 83*p0**(-4/9)*d0**(-1/5)

m = 2048
c = 2/m
q = 4/(1-2*c)
U = (4*math.pi*math.sqrt(c))**c
Hq = (2*(q-1))**((q-1)/q)
Cbase = (q+1)/math.pi * ((2*math.pi/q)*Hq/U)**(q/(q+1))
stress_coeff = Cbase * 16**(-2/(5-2*c)) * 4**(-(1-2*c)/(5-2*c))

eigs = [4*(1-math.sqrt(c)), 4, 4*(1+math.sqrt(c))]
pair_non1 = 16/m
pair_with1 = 8*math.sqrt(2)/m

print('s_star', repr(sstar))
print('p0=s_star^2/64', repr(p0))
print('crude_gate_coefficient_before_Cstr^(8/9)', repr(crude_gate))
print('stress_m', m)
print('stress_leverage_c', repr(c))
print('stress_q', repr(q))
print('stress_Uc', repr(U))
print('stress_Hq', repr(Hq))
print('stress_constant_before_Sc_power', repr(Cbase))
print('stress_density_coefficient_before_Sc_power', repr(stress_coeff))
print('stress_nonzero_eigenvalues_over_L', *[repr(x) for x in eigs])
print('stress_pair_bound_without_coordinate1_over_L', repr(pair_non1))
print('stress_pair_bound_with_coordinate1_over_L', repr(pair_with1))
assert min(eigs) >= 1
assert pair_non1 < 1/64
assert pair_with1 < 1/64
assert c < 1/4
assert crude_gate < 1.01e6
assert stress_coeff < 1.68
print('QFORM_B08_R30_CHECK_PASS')
