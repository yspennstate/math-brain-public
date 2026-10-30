from math import sqrt, exp, log

# Current STAR4 constants from source-pinned fleet02/B19 + fleet03/B19.
tau = 2**-20
rho_star = 63*(1-tau)**2/16384
Delta = 3*rho_star/8
kappa0 = sqrt(1288/3)
Z_mismatch = Delta**3/(64*kappa0)
C_E3 = 3*2**(4/3)*exp(1/3)
B_mismatch = C_E3 * Z_mismatch**(-1/6)

F_B = 0.4537176735697731005
F = F_B/8
Acore_sq = 9*F/16
Cprod = (63/64)*Delta
gamma_cycle = sqrt(Acore_sq)*sqrt(2*Delta)*sqrt(2*Cprod)/(16*sqrt(2))
triangle_endpoint_bound = 2*(3+log(8))*gamma_cycle**(-1/3)

# Earlier r37 transverse physical-E3 packet.
Z_r37 = 1.8425438602123219e-9
B_r37 = C_E3 * Z_r37**(-1/6)

assert Z_mismatch > 2.2608e-12
assert B_mismatch < 920.903
assert B_r37 < 301.317
assert gamma_cycle > 2.2585e-5
assert triangle_endpoint_bound < 359.392

print('rho_star=', repr(rho_star))
print('Delta=', repr(Delta))
print('kappa0=', repr(kappa0))
print('Z_mismatch=', repr(Z_mismatch))
print('C_E3=', repr(C_E3))
print('marginal_free_mismatch_bound=', repr(B_mismatch))
print('marginal_free_r37_transverse_bound=', repr(B_r37))
print('F=', repr(F))
print('Acore_sq=', repr(Acore_sq))
print('gamma_cycle=', repr(gamma_cycle))
print('tail_free_rankone_triangle_reference_bound=', repr(triangle_endpoint_bound))
print('STATUS=PASS')
