#!/usr/bin/env python3
from fractions import Fraction

z = Fraction(489, 50)
q = 15
assert z*z > q
s = z + Fraction(q, 1) / z
margin = s*s - Fraction(128, 1)  # compares (z+15/z)^2 with (8 sqrt 2)^2
assert margin > 0

gap = Fraction(50, 489) - Fraction(1, 11)
assert gap == Fraction(61, 5379)
assert gap > Fraction(113, 10000)

# Finite falsification scan for the general analytic inequality
# t + q/t > 4 sqrt(rG), G>=2r. This scan is NOT the proof;
# the report contains the derivative/minimum argument for all r,G.
min_margin = None
min_pair = None
checked = 0
for r in range(1, 201):
    for G in range(2*r, 20*r + 1):
        t = 4*G - 2*r - 1
        qg = 4*G - 1
        assert t*t > qg
        lhs = Fraction(t, 1) + Fraction(qg, t)
        sq_margin = lhs*lhs - Fraction(16*r*G, 1)
        assert sq_margin > 0
        checked += 1
        if min_margin is None or sq_margin < min_margin:
            min_margin = sq_margin
            min_pair = (r, G)

print('PROB10-09 HIGHER-RANK CENTRAL KERNEL EXACT CHECK')
print(f'z={z}')
print(f'z_squared_minus_15={z*z-Fraction(15,1)}')
print(f'z_plus_15_over_z={s}')
print(f'squared_margin_over_(8sqrt2)^2={margin}')
print(f'p_u_floor=50/489={float(Fraction(50,489)):.15f}')
print(f'p_c_ceiling=1/11={float(Fraction(1,11)):.15f}')
print(f'gap_exact={gap}')
print(f'gap_decimal={float(gap):.15f}')
print(f'gap_minus_113_over_10000={gap-Fraction(113,10000)}')
print(f'finite_negation_scan_cases={checked}')
print(f'finite_negation_scan_min_squared_margin={min_margin} at r,G={min_pair}')
print('ALL_EXACT_CHECKS_PASS')
