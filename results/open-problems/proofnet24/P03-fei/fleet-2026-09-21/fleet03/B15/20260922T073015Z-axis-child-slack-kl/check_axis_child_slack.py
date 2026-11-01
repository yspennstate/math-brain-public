from fractions import Fraction

# Exact decimal/rational checker for the conservative scalar envelope in REPORT.md.
# No truth-table search occurs here; the mathematical inputs are the cited central
# prime reserve and the source-valid |Gamma^dagger'|<85 bound.

C = Fraction(6521851214, 10**9)       # C^dagger = 6.521851214
DELTA0 = Fraction(49065, 10**7)       # weakened central prime reserve 0.0049065
EPS = Fraction(1, 50000)              # 2e-5 axial radius
R = 2 * EPS                            # r = 2t-1
Z = R * R                              # 4 eps^2

# h_2(z) <= z log_2(e/z).  Since e<3 and 3 < 2^31 z,
# log_2(e/z)<31, hence h_2(z)<31 z.
assert Z < Fraction(1, 2)
assert Fraction(3, 1) < (2**31) * Z
H_UPPER = 31 * Z

LINEAR = (8 * C + 182) * EPS
QUADRATIC = 64 * EPS * EPS
LOSS = LINEAR + QUADRATIC + H_UPPER
RESERVE = DELTA0 - LOSS

print(f"C={float(C):.12f}")
print(f"epsilon={float(EPS):.12g}")
print(f"r={float(R):.12g}")
print(f"z={float(Z):.12g}")
print(f"2^31*z={float((2**31)*Z):.12f}")
print(f"linear_loss={float(LINEAR):.15f}")
print(f"quadratic_loss={float(QUADRATIC):.15f}")
print(f"entropy_loss_upper={float(H_UPPER):.15f}")
print(f"total_loss_upper={float(LOSS):.15f}")
print(f"reserve_lower={float(RESERVE):.15f}")
assert RESERVE > 0

# Dead-envelope check: the same conservative proof cannot certify 2.1e-5.
# This is NOT a counterexample to the gate inequality; it only marks the limit
# of the displayed worst-case envelope.
EPS_BAD = Fraction(21, 10**6)
Z_BAD = 4 * EPS_BAD * EPS_BAD
assert Fraction(3, 1) < (2**31) * Z_BAD
LOSS_BAD = ((8 * C + 182) * EPS_BAD
            + 64 * EPS_BAD * EPS_BAD
            + 31 * Z_BAD)
RESERVE_BAD = DELTA0 - LOSS_BAD
print(f"envelope_reserve_at_2.1e-5={float(RESERVE_BAD):.15f}")
assert RESERVE_BAD < 0
print("PASS")
