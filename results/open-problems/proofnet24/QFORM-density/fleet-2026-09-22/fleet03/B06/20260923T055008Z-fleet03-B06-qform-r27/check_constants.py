import math

# Arithmetic and exponent checks for fleet03/B06 r27.
kbar = 5.0/2.0
h = 9.0/10.0
q = 2*h

# Mixed-order L3 threshold and exact ratio.
assert kbar > 4*q/3
ratio = 3*kbar/(3*kbar-4*q)
assert abs(ratio - 25.0) < 1e-12

# Coarse outer-square coefficient before packet scale.
C0 = (2**(11/4) * 3**(-5/8) * math.sqrt(math.e)
      * q**(-1/4) * math.sqrt(ratio))
packet_factor = 3456**(1/10)
C = C0 * packet_factor
assert C < 54.424

# Nested packet threshold: (9/10)*(L^6/6912)=L^6/7680.
assert abs(6912/h - 7680.0) < 1e-12

# Half-Riesz L3 optimization constant.
A = 2**(4/3)
half_riesz = A**(3/4) * (3**(1/4) + 3**(-3/4))
assert abs(half_riesz - 8/3**(3/4)) < 1e-12

# The theoretical residual occupancy threshold for kbar=5/2 is h<15/16.
h_threshold = 3*kbar/8
assert abs(h_threshold - 15/16) < 1e-12

print('QFORM_B06_R27_CHECK_PASS')
print(f'ratio={ratio:.12f}')
print(f'outer_coarse_before_packet={C0:.12f}')
print(f'packet_factor={packet_factor:.12f}')
print(f'final_9_10_constant={C:.12f}')
print(f'half_riesz_constant={half_riesz:.12f}')
print(f'occupancy_threshold={h_threshold:.12f}')
print('nested_packet_divisor=7680')
