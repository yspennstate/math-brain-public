#!/usr/bin/env python3
import math
import random

eta0 = 1.0 - math.sqrt(15.0) / 4.0
sigma_factor = 1.0 - 2.0 * eta0
partner_constant = 6.0 * math.sqrt(math.pi) / sigma_factor
pair_constant = 4.0 * math.pi

assert 0.0 < eta0 < 0.5
assert abs(sigma_factor - (math.sqrt(15.0) / 2.0 - 1.0)) < 1e-15
assert partner_constant < pair_constant

max_identity_error = 0.0
for _ in range(100000):
    e1, e2, e3 = [random.random() * 0.499999 for _ in range(3)]
    x, y, z = 1.0 - e1, 1.0 - e2, 1.0 - e3
    det_direct = 1.0 + 2.0*x*y*z - x*x - y*y - z*z
    det_expanded = (-(e1*e1 + e2*e2 + e3*e3)
                    + 2.0*(e1*e2 + e1*e3 + e2*e3)
                    - 2.0*e1*e2*e3)
    max_identity_error = max(max_identity_error, abs(det_direct-det_expanded))
    if det_direct < 0.0:
        tau = -det_direct
        delta = max(e1, e2, e3)
        assert tau <= 4.0*delta*delta + 1e-12
        e = delta
        assert e*(2.0-e) + 1e-15 >= e

print(f"eta0={eta0:.15f}")
print(f"sigma_factor={sigma_factor:.15f}")
print(f"partner_constant={partner_constant:.15f}")
print(f"pair_constant={pair_constant:.15f}")
print(f"partner_below_pair={partner_constant < pair_constant}")
print(f"max_identity_error={max_identity_error:.3e}")
print("QFORM_B11_R23_CHECK_PASS")
