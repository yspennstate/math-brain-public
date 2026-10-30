#!/usr/bin/env python3
from fractions import Fraction as F

Cminus = F(521851214, 10**9)      # C^dagger - 6
a = F(268204856, 10**9)          # quadratic lift
G1 = F(129096, 10000)             # G(1)

# ln 2 = 2 sum_{j>=0} 1/((2j+1) 3^(2j+1)); seven terms suffice.
ln2_partial = 2 * sum(F(1, (2*j+1) * 3**(2*j+1)) for j in range(7))
ln2_floor = F(6931471, 10_000_000)
assert ln2_partial > ln2_floor
linv = F(10_000_000, 6931471)

# Same-side collar rho <= 1/86.
rho = F(1, 86)
same_gap = Cminus - 31 * linv * rho - a * F(1,2) * rho * rho
assert same_gap > 0
same_margin_per_m = same_gap / 2

# The same envelope does not certify rho=1/85.
rho85 = F(1, 85)
same_gap85 = Cminus - 31 * linv * rho85 - a * F(1,2) * rho85 * rho85
assert same_gap85 < 0

# Center-crossing collar v <= (1-u)/112, u<v.
k = 112
d = F(1, k+1) + F(1, k)
ln_upper = d + d*d / (2*(1-d))
xdiff = ln_upper * linv
L = G1 + 31*xdiff + 31*linv + a*d
J_upper = L / (2*k)
reserve_lower = Cminus * F(1,2) * (1 - F(1, (k+1)**2))
cross_gap = reserve_lower - J_upper
assert cross_gap > 0

# The same envelope does not certify k=111.
k2 = 111
d2 = F(1, k2+1) + F(1, k2)
ln_upper2 = d2 + d2*d2 / (2*(1-d2))
xdiff2 = ln_upper2 * linv
L2 = G1 + 31*xdiff2 + 31*linv + a*d2
J_upper2 = L2 / (2*k2)
reserve_lower2 = Cminus * F(1,2) * (1 - F(1, (k2+1)**2))
cross_gap111 = reserve_lower2 - J_upper2
assert cross_gap111 < 0

print('ln2_partial', ln2_partial, float(ln2_partial))
print('ln2_floor_gap', ln2_partial-ln2_floor, float(ln2_partial-ln2_floor))
print('same_gap_1_over_86', same_gap, float(same_gap))
print('same_margin_per_m', same_margin_per_m, float(same_margin_per_m))
print('same_envelope_1_over_85', same_gap85, float(same_gap85))
print('d_star_112', d, float(d))
print('x_minus_1_upper_112', xdiff, float(xdiff))
print('L_star_112', L, float(L))
print('J_upper_112', J_upper, float(J_upper))
print('reserve_lower_112', reserve_lower, float(reserve_lower))
print('cross_gap_112', cross_gap, float(cross_gap))
print('cross_envelope_111', cross_gap111, float(cross_gap111))
print('PASS')
