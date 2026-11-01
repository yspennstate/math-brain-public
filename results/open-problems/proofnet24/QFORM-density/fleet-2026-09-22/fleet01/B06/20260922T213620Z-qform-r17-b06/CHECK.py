import math

theta=0.5
h2_over_gamma=1/math.sqrt(2)
sigma_over_gamma=math.sqrt(1-theta**2)*h2_over_gamma
Mconst=math.e*math.sqrt(math.pi)/sigma_over_gamma
outer_constant=2*math.sqrt(Mconst)

assert abs(sigma_over_gamma-math.sqrt(3/8))<1e-15
assert abs(Mconst-math.e*math.sqrt(math.pi)*math.sqrt(8/3))<1e-14
assert outer_constant<5.610

print(f"sigma_over_gamma={sigma_over_gamma:.15f}")
print(f"Mconst={Mconst:.15f}")
print(f"outer_constant={outer_constant:.15f}")
print("QFORM_B06_VERTEX_COVER_CHECK_PASS")
