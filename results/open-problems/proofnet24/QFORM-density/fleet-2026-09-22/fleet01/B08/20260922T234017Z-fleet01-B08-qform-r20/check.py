import math

# Worst-case constants in QFORM-SPECTRAL-GATED-96-HYBRID-SPLIT-v1
mu = 1/16
beta = 1/2
tau = 1/96
alpha = (1-math.sqrt(3*mu))/2
rho = alpha*beta-tau
gate = (math.sqrt(mu/alpha)+math.sqrt(6)*tau/rho)**2
C_exact = 9*math.sqrt(3*math.e)/(2*rho)
C_rational = (864/25)*math.sqrt(3*math.e)

print('alpha_worst =', repr(alpha))
print('rho_worst =', repr(rho))
print('gate_worst =', repr(gate))
print('partner_constant_exact_boundary =', repr(C_exact))
print('rational_report_constant =', repr(C_rational))
assert mu < 1/3
assert rho > 25/192
assert gate < 1/2
assert C_rational < 99

# Strictness family from Section 5
mu_ex = 1/24
beta_ex = 3/4
tau_ex = 1/192
alpha_ex = (1-math.sqrt(3*mu_ex))/2
rho_ex = alpha_ex*beta_ex-tau_ex
gate_ex = (math.sqrt(mu_ex/alpha_ex)+math.sqrt(6)*tau_ex/rho_ex)**2
C_ex = 9*math.sqrt(3*math.e)/(2*rho_ex)

print('example_alpha =', repr(alpha_ex))
print('example_rho =', repr(rho_ex))
print('example_gate =', repr(gate_ex))
print('example_constant =', repr(C_ex))
assert gate_ex < 1/2
assert C_ex < 54.174

# Parseval/frame bookkeeping for the explicit 89-row frame.
e1_mass = (1/2)**2 + 24*(1/math.sqrt(32))**2
e2_mass = 32*(1/math.sqrt(32))**2
e3_mass = 32*(1/math.sqrt(32))**2
print('frame_column_masses =', repr((e1_mass,e2_mass,e3_mass)))
assert abs(e1_mass-1) < 1e-14
assert abs(e2_mass-1) < 1e-14
assert abs(e3_mass-1) < 1e-14
assert 1/4 > 1/7

print('QFORM_B08_R20_CHECK_PASS')
