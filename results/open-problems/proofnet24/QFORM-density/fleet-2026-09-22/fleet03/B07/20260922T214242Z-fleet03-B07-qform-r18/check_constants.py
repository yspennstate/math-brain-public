import math

c0 = 0.5 - math.exp(-1.0)
eps0 = c0 / 4.0
ell0 = 1.0 - eps0
C2 = 7.270461147134126
half_riesz = C2 * 10.0**0.25

assert c0 > 0.13
assert abs(eps0 / c0 - 0.25) < 1e-15
assert ell0 > 0.96
assert half_riesz < 12.93

print(f"c0={c0:.17f}")
print(f"eps0={eps0:.17f}")
print(f"ell0={ell0:.17f}")
print(f"C2*10^(1/4)={half_riesz:.17f}")
print("PASS")
