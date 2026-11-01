from math import sqrt, exp

# Exact constants from strict N3(1/128).
tau = 1.0/128.0
eta = sqrt(tau + tau*tau)
delta = tau + eta
q = 1.0 - delta
mu = q*q/(1.0 + tau + 2.0*q)
m = (eta + eta*eta)/mu
rho0 = 1.0 - 2.0*m
C1 = 3.0*exp(2.0/3.0)
noheavy = C1/q * (3.0**(1.0/3.0))

print('tau', tau)
print('eta', eta)
print('delta', delta)
print('q', q)
print('mu', mu)
print('max_leverage_bound', m)
print('rho_lower', rho0)
print('noheavy_density_bound_using_rho>1/3', noheavy)

assert m < 1.0/3.0
assert rho0 > 1.0/3.0
assert noheavy < 9.328

# Heavy-coordinate transversality check.
def arrow(E, beta):
    return 0.5*(E + sqrt(E*E + 4.0*beta*beta))

beta = 0.18
Ebeta = tau + (eta + beta)**2/eta
rank2_error = delta + arrow(Ebeta, beta)
P0 = eta*beta*beta
heavy_paid = C1*((1.0/256.0)*P0)**(-1.0/3.0)

print('E(0.18)', Ebeta)
print('rank2_approx_error_at_beta_0.18', rank2_error)
print('heavy_mixed_det_lower', P0)
print('heavy_density_bound_if_rho>=1/256', heavy_paid)

assert rank2_error < 1.0
assert P0 > 0.00287
assert heavy_paid < 261.0

# Algebraic determinant check for the no-heavy 3x3 core.
# M=[[a,alpha,beta],[alpha,s*t,0],[beta,0,0]] has det=-s*t*beta^2.
for s in (-1.0, 1.0):
    a, alpha, t, b = 0.003, 0.7, 1.2, 0.95
    det = -s*t*b*b
    direct = (
        a*((s*t)*0.0 - 0.0*0.0)
        - alpha*(alpha*0.0 - 0.0*b)
        + b*(alpha*0.0 - (s*t)*b)
    )
    assert abs(det-direct) < 1e-12

print('all checks passed')
