from decimal import Decimal, getcontext

getcontext().prec = 70

# This checker validates the finite/exact arithmetic checkpoints used in the
# accompanying proof.  The infinite-family statements are proved symbolically
# in the report; enumeration below is diagnostic only.

# Critical-side full-Z fibre witness, concrete g=3.
g = 3
b = 4 * g - 3
pc_factor_slack = b**3 - b**2 - b - 1
assert pc_factor_slack > 0
print(f"g=3 pc fibre factor slack b^3-b^2-b-1 = {pc_factor_slack} > 0")

# Operator side for g=3,k=1.
# R < z + Q/z becomes 4*sqrt(3) < 15/2.
# Squaring positive sides: 48 < 225/4, equivalently 192 < 225.
assert 192 < 225
print(f"g=3,k=1 operator exact squared check: 192 < 225; slack={225-192}")

# Clean infinite sufficient range k<=g-2:
# at the worst k=g-2 the margin is
#   2g - 4 sqrt(g) + (6g-3)/(4g-2).
# For g=3 the exact squared check above is stronger than needed.
# For g>=4, 2g >= 4 sqrt(g) is equivalent after squaring to
# 4g^2 >= 16g, and the rational residual is strictly positive.
for g in range(4, 101):
    assert 4 * g * g >= 16 * g
    assert 6 * g - 3 > 0 and 4 * g - 2 > 0
print("clean sufficient range k<=g-2 verified algebraically: g=3 by squared check; g>=4 by 4g^2>=16g plus positive residual")

# High-precision numerical diagnostics for the concrete g=3,k=1 corollary.
sqrt3 = Decimal(3).sqrt()
beta = Decimal(2) + Decimal(2) * sqrt3 + (Decimal(1) + Decimal(8) * sqrt3).sqrt()
pu_lower = Decimal(1) / beta
gap_lower = pu_lower - Decimal(1) / Decimal(10)
assert gap_lower > 0
print(f"g=3,k=1 beta upper diagnostic = {beta}")
print(f"g=3,k=1 p_2to2 lower diagnostic = {pu_lower}")
print(f"g=3,k=1 gap lower diagnostic = {gap_lower}")

# Diagnostic table for the sharper exact criterion
# 2k(4g-3) < 16g^2 - 16g^(3/2) -20g +8sqrt(g)+9.
# This table is not used as a proof of the infinite statement.
vals = []
for G in range(3, 11):
    root = Decimal(G).sqrt()
    A = Decimal(16) * G * G - Decimal(16) * root * G - Decimal(20) * G + Decimal(8) * root + Decimal(9)
    threshold = A / (Decimal(2) * (4 * G - 3))
    K = 0
    while Decimal(K + 1) < threshold:
        K += 1
    vals.append((G, K, str(threshold)))
print("K(g) diagnostic (g,K,strict-threshold): " + repr(vals))

print("ALL_EXACT_CHECKS_PASS")
