import math

q = 4.0/3.0
z2_floor = 1.0/48.0
half_riesz_front = 8.0*math.sqrt(math.e/2.0)/(2.0-q)*q**(-0.25)
half_riesz_bound = half_riesz_front*z2_floor**(-0.125)
density_bound = 16.0*half_riesz_bound

o1_denom = 256**2 * 144
o23_denom = 256**2 * 3

print(f"q={q:.15g}")
print(f"half_riesz_front={half_riesz_front:.15f}")
print(f"half_riesz_bound={half_riesz_bound:.15f}")
print(f"density_bound={density_bound:.15f}")
print(f"o1_anchor_denominator={o1_denom}")
print(f"o23_denominator={o23_denom}")

assert density_bound < 337.952
assert o1_denom == 9437184
assert o23_denom == 196608
assert abs((1.0/48.0)/3.0 - 1.0/144.0) < 1e-18
print("STATUS=PASS")
