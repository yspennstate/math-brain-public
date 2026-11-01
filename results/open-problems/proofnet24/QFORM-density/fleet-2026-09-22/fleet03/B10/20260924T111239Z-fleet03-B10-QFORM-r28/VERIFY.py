#!/usr/bin/env python3
import math

# Deterministic constant checks for fleet03/B10 r28.
harmonic = 3 * 2**(4/3) * (64/63)**(1/3)
completed_cap = math.sqrt(512/255) / 16
square_l32 = 2 * (32/255)**(1/3)

print(f"harmonic_zero_pivot_bound={harmonic:.15f}")
print(f"completed_coordinate_cap_upper={completed_cap:.15f}")
print(f"completed_square_L32_upper={square_l32:.15f}")
assert harmonic < 7.6
assert completed_cap < 0.089
assert square_l32 < 1.002

# Exact completed-square algebra regression on a fixed grid.
# Original: a(sqrt(c)H+S)^2 + 2b(sqrt(c)H+S)U + uU^2+2vUV+wV^2
# Completed: ac Z^2 + (u-b^2/a)U^2+2vUV+wV^2,
# Z=H+(S+(b/a)U)/sqrt(c).
maxerr = 0.0
for a in (1/64, -1/64, 1/100):
    c = 0.99
    b = 0.998
    u, v, w = 0.7, -0.3, 1.2
    for H in (-1.3, 0.0, 2.1):
        for S in (-0.2, 0.11):
            for U in (-0.8, 0.6):
                for V in (-1.1, 0.4):
                    y = math.sqrt(c)*H + S
                    q0 = a*y*y + 2*b*y*U + u*U*U + 2*v*U*V + w*V*V
                    Z = H + (S + (b/a)*U)/math.sqrt(c)
                    q1 = a*c*Z*Z + (u-b*b/a)*U*U + 2*v*U*V + w*V*V
                    maxerr = max(maxerr, abs(q0-q1))
print(f"completed_square_grid_max_abs_error={maxerr:.3e}")
assert maxerr < 1e-10
print("STATUS=PASS")
