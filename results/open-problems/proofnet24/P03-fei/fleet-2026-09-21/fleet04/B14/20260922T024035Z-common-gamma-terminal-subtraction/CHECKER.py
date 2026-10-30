from fractions import Fraction as F
from decimal import Decimal, getcontext

# Certified inherited data for the exact G10 witness.
# fleet03/B12:
H_LO = F("6.509836127588151479")
H_HI = F("6.509836127588151480")
I_MINUS_1 = F(129,128)

# Old read-once base potential and stable tail lift from fleet01/B18.
C0 = F("6.4548")
C_STAR = F("6.5218512")
A_STAR = F("0.2682048")
assert C_STAR == C0 + A_STAR/4

# fleet04/B12 AND/OR-atom stopping tree.
P_ROOT = F(129,512)
AND_TERMINAL_PROB = F(29,64)
P_AND2 = F(1,16)
EXPECTED_P_TERMINAL = AND_TERMINAL_PROB * P_AND2
Q_BLOCK = P_ROOT - EXPECTED_P_TERMINAL
assert EXPECTED_P_TERMINAL == F(29,1024)
assert Q_BLOCK == F(229,1024)

# Read-once base is tight on the uniform AND2/OR2 terminal atoms,
# so the signed preterminal block residual under Gamma_a is
# D_RO(G10) + a Q_BLOCK.
DRO_LO = C0*I_MINUS_1 - H_HI
DRO_HI = C0*I_MINUS_1 - H_LO
assert DRO_HI < 0

A_REQ_LO = -DRO_HI / Q_BLOCK
A_REQ_HI = -DRO_LO / Q_BLOCK
C_REQ_LO = C0 + A_REQ_LO/4
C_REQ_HI = C0 + A_REQ_HI/4

BLOCK_LO = DRO_LO + A_STAR*Q_BLOCK
BLOCK_HI = DRO_HI + A_STAR*Q_BLOCK
assert BLOCK_LO > F("0.05537")

# Independent root-minus-terminal evaluation under the same Gamma_*.
DROOT_LO = C_STAR*I_MINUS_1 - H_HI
DROOT_HI = C_STAR*I_MINUS_1 - H_LO
DTERM_EXPECTED = A_STAR*EXPECTED_P_TERMINAL
assert DROOT_LO - DTERM_EXPECTED == BLOCK_LO
assert DROOT_HI - DTERM_EXPECTED == BLOCK_HI

# Stable lift comfortably clears the exact G10 block requirement.
assert A_STAR > 13*A_REQ_HI
assert C_STAR > C_REQ_HI + F("0.0618")

getcontext().prec = 80
def dec(x, digits=30):
    return format(Decimal(x.numerator)/Decimal(x.denominator), f'.{digits}f')

print("PASS")
print("Q_block", Q_BLOCK)
print("D_RO_block_lower", dec(DRO_LO, 30))
print("D_RO_block_upper", dec(DRO_HI, 30))
print("required_a_lower", dec(A_REQ_LO, 30))
print("required_a_upper", dec(A_REQ_HI, 30))
print("required_center_lower", dec(C_REQ_LO, 30))
print("required_center_upper", dec(C_REQ_HI, 30))
print("stable_a", dec(A_STAR, 30))
print("stable_center", dec(C_STAR, 30))
print("stable_block_residual_lower", dec(BLOCK_LO, 30))
print("stable_block_residual_upper", dec(BLOCK_HI, 30))
print("stable_root_slack_lower", dec(DROOT_LO, 30))
print("expected_terminal_slack", dec(DTERM_EXPECTED, 30))
print("lift_factor_over_block_requirement_lower", dec(A_STAR/A_REQ_HI, 20))
print("full_FEI", "OPEN_NOT_PROVED")
