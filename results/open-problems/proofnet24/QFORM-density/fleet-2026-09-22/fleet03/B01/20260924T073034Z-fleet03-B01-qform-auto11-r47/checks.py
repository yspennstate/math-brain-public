import math

C_center=math.sqrt(24)/(2*math.pi)
C_shell=(2*math.sqrt(48)/math.pi)/(1-2**(-1.5))
C_F=C_center+C_shell
C_tetrad=8*math.exp(0.25)/math.pi
partner=math.sqrt(2/(3*math.pi))

print(f"C_center={C_center:.15f}")
print(f"C_shell={C_shell:.15f}")
print(f"C_F={C_F:.15f}")
print(f"C_tetrad_fejer={C_tetrad:.15f}")
print(f"C_F_lt_7p603={C_F < 7.603}")
print(f"partner_l2_fejer_prefactor={partner:.15f}")
print(f"shell_ratio={2**(-1.5):.15f}")

assert C_F < 7.603
assert abs(C_tetrad-3.2697438739437548) < 1e-12
assert abs(partner-0.4606588659617807) < 1e-12
assert 2**(-1.5) < 1
print("STATUS=PASS")
