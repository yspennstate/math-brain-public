import math

mhalf = 2**0.25 * math.gamma(0.75) / math.sqrt(math.pi)
K_D = (2*math.pi)**1.5 * math.exp(0.75)
Holder_D = (4*math.sqrt(2)/math.pi) * K_D
Heat_D = Holder_D * mhalf
Density_D = 6*math.sqrt(math.e)
K_F = (4*math.pi)**1.5
Holder_F = (4*math.sqrt(2)/math.pi) * K_F
Heat_F = Holder_F * mhalf

print(f"mhalf={mhalf:.15f}")
print(f"K_D_prefactor={K_D:.15f}")
print(f"Holder_D_prefactor={Holder_D:.15f}")
print(f"Heat_D_prefactor={Heat_D:.15f}")
print(f"Density_D_prefactor={Density_D:.15f}")
print(f"K_F_prefactor={K_F:.15f}")
print(f"Holder_F_prefactor={Holder_F:.15f}")
print(f"Heat_F_prefactor={Heat_F:.15f}")

assert abs(Holder_D - 16*math.sqrt(math.pi)*math.exp(0.75)) < 1e-12
assert abs(Heat_D - 16*2**0.25*math.exp(0.75)*math.gamma(0.75)) < 1e-12
assert abs(Holder_F - 32*math.sqrt(2*math.pi)) < 1e-12
assert abs(Heat_F - 32*2**0.75*math.gamma(0.75)) < 1e-12
print("PASS")
