#!/usr/bin/env python3
"""Exact arithmetic checker for B16 common-potential terminal-atom subtraction.

This does not reconstruct the G10 truth table. It consumes source-certified
intervals/invariants from:
- fleet02/B16 arity10 composition-prime report;
- fleet04/B12 AND/OR-atom stopping report;
- fleet03/B13 shared-graft tail report.

All sign decisions below are exact Fraction comparisons.
"""
from fractions import Fraction as F

C0 = F(16137, 2500)  # 6.4548 exactly in the active read-once candidate
I = F(257, 128)
H_LO = F("6.509836127588151479")
H_HI = F("6.509836127588151480")

# G10 is balanced at uniform inputs.
P_ROOT = I / 4 - F(1, 4)
assert P_ROOT == F(129, 512)

# fleet04/B12 exact stopping law.
TERMINAL_AND_PROB = F(29, 64)
P_AND = F(1, 16)
P_TERMINAL_EXPECTED = TERMINAL_AND_PROB * P_AND
assert P_TERMINAL_EXPECTED == F(29, 1024)
P_BLOCK = P_ROOT - P_TERMINAL_EXPECTED
assert P_BLOCK == F(229, 1024)

# Read-once fixed point is exact on the uniform AND atom:
# Gamma_RO(1/4) = Gamma_RO(1/2)-2, so each terminal AND has D_0=0.
D0_LO = (I - 1) * C0 - H_HI
D0_HI = (I - 1) * C0 - H_LO
assert D0_LO < D0_HI < 0

# Correction threshold for the root and for the preterminal block.
C_ROOT_LO = -D0_HI / P_ROOT
C_ROOT_HI = -D0_LO / P_ROOT
C_BLOCK_LO = -D0_HI / P_BLOCK
C_BLOCK_HI = -D0_LO / P_BLOCK
assert C_ROOT_HI < F("0.018289126551422929")
assert C_BLOCK_HI < F("0.020605216813393518")
assert C_BLOCK_LO > C_ROOT_HI

# Independent other-account source-valid balanced gate F6 forces every
# globally valid Gamma_RO+c*phi candidate to have at least this correction.
R6_LO = F("6.5218509495504481848190319299878158287105279434983773429918090394322216")
C_FORCED = 4 * (R6_LO - C0)
assert C_FORCED > F("0.2682037982017927")
assert C_FORCED > C_BLOCK_HI

# Rigorous worst-case slacks using H <= H_HI.
BLOCK_SLACK_LO = D0_LO + C_FORCED * P_BLOCK
ROOT_SLACK_LO = D0_LO + C_FORCED * P_ROOT
TERMINAL_EXPECTED_SLACK = C_FORCED * P_TERMINAL_EXPECTED
TERMINAL_EACH_SLACK = C_FORCED * P_AND

assert BLOCK_SLACK_LO > F("0.0553711671268978")
assert ROOT_SLACK_LO > F("0.0629667825056595")
assert TERMINAL_EXPECTED_SLACK > F("0.0075956153787617")
assert ROOT_SLACK_LO == BLOCK_SLACK_LO + TERMINAL_EXPECTED_SLACK
assert TERMINAL_EACH_SLACK > 0

def dec(x, digits=70):
    from decimal import Decimal, getcontext
    getcontext().prec = digits + 10
    return format(Decimal(x.numerator) / Decimal(x.denominator), f".{digits}f")

print("PASS")
print("P_root", P_ROOT)
print("P_terminal_expected", P_TERMINAL_EXPECTED)
print("P_block", P_BLOCK)
print("base_root_defect_interval", dec(D0_LO), dec(D0_HI))
print("root_c_threshold_interval", dec(C_ROOT_LO), dec(C_ROOT_HI))
print("block_c_threshold_interval", dec(C_BLOCK_LO), dec(C_BLOCK_HI))
print("forced_c_lower", dec(C_FORCED))
print("block_slack_lower_at_forced_c", dec(BLOCK_SLACK_LO))
print("terminal_expected_slack_at_forced_c", dec(TERMINAL_EXPECTED_SLACK))
print("root_slack_lower_at_forced_c", dec(ROOT_SLACK_LO))
print("terminal_each_AND_slack_at_forced_c", dec(TERMINAL_EACH_SLACK))
print("full_FEI OPEN_NOT_PROVED")
