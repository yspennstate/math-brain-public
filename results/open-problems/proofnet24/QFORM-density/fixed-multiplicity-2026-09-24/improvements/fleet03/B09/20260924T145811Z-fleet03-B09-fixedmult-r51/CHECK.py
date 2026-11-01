#!/usr/bin/env python3
import math

eta = 1/100
kappa = 1/6400
delta = (74 - 3*math.sqrt(101))/100
tau = delta**8/2
heavy = 2*math.e*tau**(-1/8)
high = 5*math.e*(kappa**5/2048)**(-1/10)
partner = 3*4**(-1/3)

assert delta > 0
assert abs(tau - delta**8/2) < 1e-18
assert abs(1/12800 - kappa/2) < 1e-18
assert heavy < 14
assert high < 2331
assert max(heavy, high) < 6010
assert partner < 1.89

print('PASS')
print(f'delta={delta:.15f}')
print(f'tau={tau:.15f}')
print(f'kappa/2={kappa/2:.15f}')
print(f'heavy_slice_bound={heavy:.12f}')
print(f'high_residual_bound={high:.12f}')
print('full_normalized_bound=6010')
print(f'partner_example_bound={partner:.12f}')
