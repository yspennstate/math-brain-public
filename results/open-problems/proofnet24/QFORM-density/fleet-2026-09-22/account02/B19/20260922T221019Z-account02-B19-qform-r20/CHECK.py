import math

eps_star=(1-1/math.sqrt(2))**2
eps=1/16
delta=0.5-eps-math.sqrt(2*eps)
D=0.5
c=61/64
pi3=D*(1-c)*delta**3
bound=3*math.e*pi3**(-1/3)
assert eps < eps_star
assert delta > 0
assert abs(delta-(7/16-1/(2*math.sqrt(2)))) < 1e-15
assert pi3 > 0
assert bound < 339.450
print(f"epsilon_star={eps_star:.15f}")
print(f"delta_1over16={delta:.15f}")
print(f"Pi3_lower={pi3:.15e}")
print(f"density_bound={bound:.12f}")
print("QFORM_B19_R20_MSS_CROSSCUT_CHECK_PASS")
