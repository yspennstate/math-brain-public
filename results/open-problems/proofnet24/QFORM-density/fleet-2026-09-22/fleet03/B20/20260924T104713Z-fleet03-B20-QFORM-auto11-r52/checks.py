import math

eps6 = 9/262144
delta0 = 1 - (1/math.sqrt(2) + 1/4)**2
sigma0 = delta0/2 - 1/64
CE3 = 3*2**(4/3)*math.exp(1/3)
beta0 = 1/(512*math.sqrt(2))
Cstar = 1 + 44*10**(15/2)
pivot_bound = Cstar*math.sqrt(512)

assert eps6 < 1/64
assert delta0 > 0
assert abs(delta0 - (7/16 - 1/(2*math.sqrt(2)))) < 1e-15
assert sigma0 > 0
assert abs(sigma0 - (13/64 - 1/(4*math.sqrt(2)))) < 1e-15
assert CE3/sigma0 < 401
assert 1/512 > beta0
assert pivot_bound < 3.745e10
assert 191/32 < 6 and not (192/32 < 6)

print({
    'eps6': eps6,
    'delta0': delta0,
    'sigma0': sigma0,
    'CE3': CE3,
    'E3_density_bound': CE3/sigma0,
    'beta0': beta0,
    'heavy_star_scale': 1/512,
    'pivot_bound': pivot_bound,
    'max_heavy_count': 191,
})
