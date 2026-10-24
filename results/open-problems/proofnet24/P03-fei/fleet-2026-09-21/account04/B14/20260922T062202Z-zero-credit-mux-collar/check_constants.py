#!/usr/bin/env python3
from decimal import Decimal, getcontext

getcontext().prec = 60
C = Decimal("6.521851214")
z0 = Decimal("0.0167628035")
a = Decimal("0.268204856")

# Source-envelope derivative estimate on symmetric representatives >= 0.2498.
derivative_bound = Decimal("4.9096") * Decimal("2.002") + Decimal("8.629") + Decimal("46.5") + a
assert derivative_bound < 66

# Global crude candidate bound from z log_2(1/z) < 0.54.
gamma_upper = Decimal("4.9096") * Decimal("0.54") + Decimal("8.629") / 2 + a / 4
assert gamma_upper < Decimal("7.033")
assert gamma_upper + 1 < 9

eps = Decimal(1) / Decimal(4400)
balanced_margin = z0 - (Decimal(66) + C) * eps
assert balanced_margin > Decimal("0.0002805")

# |sigma| <= 1e-6:
# candidate/leaf + data mixture + output <= 141e-6,
# six-mass Fannes cost < 88e-6,
# h_2(4 sigma^2) < 2e-10.
selector_loss = Decimal(141) * Decimal("1e-6") + Decimal("88e-6") + Decimal("2e-10")
final_margin = balanced_margin - selector_loss
assert final_margin > Decimal("0.0000515")

print("PASS")
print("derivative_bound =", derivative_bound)
print("gamma_upper =", gamma_upper)
print("balanced_collar_margin =", balanced_margin)
print("selector_release_loss =", selector_loss)
print("final_3d_collar_margin =", final_margin)
