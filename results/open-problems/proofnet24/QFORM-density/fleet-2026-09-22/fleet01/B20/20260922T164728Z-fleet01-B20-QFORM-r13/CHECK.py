import math

C3 = 94.356
tau = 1.0 / 4.0
Cstar = 32768.0 * math.sqrt(2.0)

# Case A: physical third pivot.
C_phys = C3 * (81.0 * 128.0) ** (1.0 / 8.0) / tau

# Case B: product-preserving cross cut plus quarter moment.
C_cross = (
    2.0 * math.sqrt(2.0)
    * (2.0 + math.sqrt(math.pi))
    * (4.0 * math.e) ** 0.25
    * 256.0 ** 0.25
    / tau
)

margin = 1.0 / 32.0 - 1.0 / 64.0

print(f"C_phys={C_phys:.15f}")
print(f"C_cross={C_cross:.15f}")
print(f"Cstar={Cstar:.15f}")
print(f"exterior_margin={margin:.15f}")
print(f"phys_below_candidate={C_phys < Cstar}")
print(f"cross_below_candidate={C_cross < Cstar}")

assert abs(margin - 1.0 / 64.0) < 1e-15
assert C_phys < 1198.924
assert C_cross < 310.012
assert C_phys < Cstar
assert C_cross < Cstar
print("STATUS=PASS")
