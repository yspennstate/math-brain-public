import math

h = 767/1024
Z0 = 1/256

C_D = 6*math.sqrt(math.e)*(2*h)**(-0.5)*(3-4*h)**(-1)*Z0**(-1/6)
delta = (2*h-1)*Z0
packet = delta/4
energy = packet/36
zero_edge = math.sqrt(delta)
small_b_E2 = delta/(1/8)**2
nested = delta/3
nested_endpoint = math.sqrt(nested)

C_L3 = (9*math.e/math.sqrt(2))**(2/3)
L3_O0 = C_L3*Z0**(-1/9)
C_H = 6*2**0.25*math.sqrt(math.e)
H_O0 = C_H*Z0**(-1/12)
square_O0 = H_O0*(1/4)**(-0.5)

print(f"h={h:.15f}")
print(f"Dprime_O0={C_D:.15f}")
print(f"Dprime_below_5262={C_D < 5262}")
print(f"anchor_delta={delta:.17f}")
print(f"four_bank_packet={packet:.17f}")
print(f"matching_energy={energy:.17e}")
print(f"matching_energy_reciprocal={1/energy:.15f}")
print(f"zero_edge_product={zero_edge:.17f}")
print(f"small_b_E2={small_b_E2:.17f}")
print(f"nested_mass={nested:.17f}")
print(f"nested_endpoint={nested_endpoint:.17f}")
print(f"L3_constant={C_L3:.17f}")
print(f"L3_O0={L3_O0:.17f}")
print(f"Hhalf_constant={C_H:.17f}")
print(f"Hhalf_O0={H_O0:.17f}")
print(f"outer_square_O0={square_O0:.17f}")

assert C_D < 5262
assert abs(delta - 255/131072) < 1e-18
assert abs(packet - 255/524288) < 1e-18
assert abs(energy - 85/6291456) < 1e-18
assert abs(small_b_E2 - 255/2048) < 1e-18
assert abs(nested - 85/131072) < 1e-18
assert abs(zero_edge - math.sqrt(510)/512) < 1e-15
assert abs(nested_endpoint - math.sqrt(170)/512) < 1e-15
assert square_O0 < 37.349
print("ALL_ARITHMETIC_ASSERTIONS_PASS")
