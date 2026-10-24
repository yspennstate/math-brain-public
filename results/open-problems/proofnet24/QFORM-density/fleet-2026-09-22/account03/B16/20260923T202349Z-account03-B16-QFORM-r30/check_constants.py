import math

C_pair = 9.200274035222916
partner = C_pair * (64 * 1728 / 61) ** (1/5)
projection_prefactor = 3 * 2 ** (5/6)
kappa_quarter_eps_64 = projection_prefactor * (1/4) ** (-5/6) * (1/64) ** (-1/3)

print(f"partner={partner:.12f}")
print(f"projection_prefactor={projection_prefactor:.12f}")
print(f"kappa_quarter_eps_64={kappa_quarter_eps_64:.12f}")

assert partner < 41.256
assert kappa_quarter_eps_64 < 67.883

# Algebraic Fourier constants in the proof:
# (2*pi)^3 * [1/(8*pi^(3/2))] = pi^(3/2)
assert math.isclose((2*math.pi)**3 / (8*math.pi**1.5), math.pi**1.5, rel_tol=1e-15)
# (1/(2*pi))*6*(pi^(3/2))^(2/3) = 3
assert math.isclose((1/(2*math.pi))*6*(math.pi**1.5)**(2/3), 3.0, rel_tol=1e-15)

print("STATUS=PASS")
