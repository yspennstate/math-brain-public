from decimal import Decimal, getcontext

getcontext().prec = 70

C_DAGGER = Decimal("6.521851214")
C_STAR = Decimal("6.5218512")
C0 = Decimal("6.4548")
M_PLUS = Decimal("6.52185121301287772365150440023918196647146413881")
D0 = Decimal(133) / Decimal(128)
Q_G10 = Decimal(229) / Decimal(1024)
A_STAR = Decimal("0.2682048")

A_DAGGER = Decimal(4) * (C_DAGGER - C0)
GAP = C_DAGGER - M_PLUS
ONE_STEP_SLACK = D0 * GAP
EXTRA_A = A_DAGGER - A_STAR
G10_EXTRA = EXTRA_A * Q_G10

assert A_DAGGER == Decimal("0.268204856")
assert GAP > 0
assert ONE_STEP_SLACK > Decimal("1.0256e-9")
assert C_DAGGER - C_STAR == Decimal("1.4e-8")
assert EXTRA_A == Decimal("5.6e-8")
assert G10_EXTRA == Decimal("1.25234375e-8")

print("PASS")
print("C_dagger=" + str(C_DAGGER))
print("a_dagger=" + str(A_DAGGER))
print("M_plus=" + str(M_PLUS))
print("C_minus_M=" + str(GAP))
print("d0_times_gap=" + str(ONE_STEP_SLACK))
print("extra_vs_Cstar=" + str(C_DAGGER - C_STAR))
print("extra_a_vs_astar=" + str(EXTRA_A))
print("G10_extra_block_slack=" + str(G10_EXTRA))
