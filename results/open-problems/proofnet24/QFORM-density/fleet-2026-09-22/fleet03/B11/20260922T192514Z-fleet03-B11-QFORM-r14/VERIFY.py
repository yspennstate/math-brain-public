import math

C_diag = 128 * 2**0.25
C_pair = 3 * 400**(1/3) * (256/(math.sqrt(6)-2))**(1/6)
assert C_diag < 153
assert C_pair < 64
assert abs(math.sqrt(3/8) - math.sqrt(6)/4) < 1e-15
assert abs((3/8)-(1/4)-(1/8)) < 1e-15
assert (math.sqrt(6)-2)/4 > 0
print(f"C_diag={C_diag:.15f}")
print(f"C_pair={C_pair:.15f}")
print("QFORM_LOCALIZED_3BLOCK_REPAIR_CHECK_PASS")
