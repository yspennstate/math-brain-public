import math

mu = 1/3
alpha = 0.5 - math.sqrt(1.5)*mu
rho = math.sqrt(alpha/(1-alpha))
tau = rho*rho/(1+rho)
assert alpha > 0
assert abs(rho - (math.sqrt(3)-math.sqrt(2))) < 1e-14
assert abs(rho*(rho-tau) - tau) < 1e-14   # L=1 self-dual identity
assert tau > 3/40

h = 163/250
q = 2*h
CF = 3*math.e/((3-2*q)*math.sqrt(q))
assert 1 < q < 1.5

c3 = 37/225
theta = 1/8
c4 = ((1-1/225)*(1-2/225)*(1-3/225))/24
K2 = 5*math.sqrt(2*math.e)*(c3*theta**6)**(-1/10)
K1 = 5*math.sqrt(2*math.e)*(c4*theta**8)**(-1/10)
K2_second = 5*math.sqrt(2*math.e)*(c3)**(-1/10)

b=tau
b2=b/120
zeta1=b/(14400**(1/6))
zeta2=b2/(225**(1/6))

vals = {
    'alpha': alpha,
    'rho': rho,
    'tau=d/L': tau,
    'd/(L*8)': b/8,
    'k0_router_constant': CF/b,
    'k1_D5_constant': K2/b,
    'zeta1/L': zeta1,
    'k1_router_constant': CF/zeta1,
    'k2_D5_constant': K1/b,
    'b2/L': b2,
    'k2_second_D5_constant': K2_second/b2,
    'zeta2/L': zeta2,
    'k2_router_constant': CF/zeta2,
    'k0_Z3/L6': b**6,
    'k0_anchor/L6': (38/125)*b**6,
    'k0_nested/L6': (19/125)*b**6,
    'k1_Z3/L6': b**6/14400,
    'k1_anchor/L6': (38/125)*b**6/14400,
    'k1_nested/L6': (19/125)*b**6/14400,
    'k2_Z3/L6': b2**6/225,
    'k2_anchor/L6': (38/125)*b2**6/225,
    'k2_nested/L6': (19/125)*b2**6/225,
}

assert vals['k0_router_constant'] < 238
assert vals['k1_D5_constant'] < 635
assert vals['k1_router_constant'] < 1173
assert vals['k2_D5_constant'] < 1106
assert vals['k2_second_D5_constant'] < 21861
assert vals['k2_router_constant'] < 70333

for k,v in vals.items():
    print(f'{k} = {v:.15g}')
print('QFORM_B08_SELFDUAL_ROUTER_CHECK_PASS')
