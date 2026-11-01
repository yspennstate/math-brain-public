#!/usr/bin/env python3
import math

C = 9*math.sqrt(3)*math.e/2

# Example 3.1: rank-6 projection, leverage 1/6.
k = 6
ell = 1/6
s0 = k*(1-ell)/4
assert abs(s0-1.25) < 1e-15
assert s0-0.5 >= 4.5*ell - 1e-15
z0 = s0*(s0-0.25)*(s0-0.5)/6
assert abs(z0-5/32) < 1e-15
bound0 = C*z0**(-1/6)

# Dense-cross-tail example: k=8, leverage 1/8, ||E||op<=|beta|/32.
k = 8
ell = 1/8
r = 1/32
s0 = k*(1-ell)/4
sr = s0 - 2*r*math.sqrt(k*s0)
cr = (0.5+r)**2
rhor = (math.sqrt(ell)+r)**2
margin = sr - 2*cr - 4.5*rhor
assert sr > 2*cr
assert margin > 0
zlb = sr*(sr-cr)*(sr-2*cr)/6
assert zlb > 0
bound1 = C*zlb**(-1/6)
assert bound1 < 25.943

# Hostile-count sample: one baseline defect, two large hostile modes,
# theta=1/2, protected post-dense-tail gap g=1.
rdef = 1
K = 2
theta = 0.5
g = 1.0
count_bound = 2*math.sqrt(6*math.pi*(rdef+K+3))/((1-theta)*g)

print('QFORM_B12_R26_CHECK_PASS')
print('rank6_s0', repr(s0 if False else 1.25))
print('rank6_Z_lower', repr(z0))
print('rank6_density_coefficient', repr(bound0))
print('dense_tail_sr', repr(sr))
print('dense_tail_cr', repr(cr))
print('dense_tail_rhor', repr(rhor))
print('dense_tail_gate_margin', repr(margin))
print('dense_tail_Z_lower', repr(zlb))
print('dense_tail_density_coefficient', repr(bound1))
print('hostile_count_sample_coefficient', repr(count_bound))
