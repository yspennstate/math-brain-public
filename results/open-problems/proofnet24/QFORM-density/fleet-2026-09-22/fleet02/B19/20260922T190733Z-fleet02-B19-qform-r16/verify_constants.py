import math

K3 = 9.840655864922019 * 1536 ** (1/12)
K2 = 7.673759290384858 * 1536 ** (1/8)
Kpartner = 12 * math.sqrt(math.e)

print(f"GOOD3={K3:.15f}")
print(f"R1_BASE={K2:.15f}")
print(f"PARTNER_THREE_HEAVY={Kpartner:.15f}")

assert K3 < 18.137
assert K2 < 19.201
assert Kpartner < 19.785
assert 3 * 256 == 768
assert 3 * 2 * 256 == 1536
print("QFORM_B19_R16_CONSTANT_CHECK_PASS")
