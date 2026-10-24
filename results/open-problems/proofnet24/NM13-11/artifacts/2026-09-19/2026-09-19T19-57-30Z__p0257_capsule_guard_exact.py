from fractions import Fraction
from decimal import Decimal, getcontext

# predecessor endpoint from run 2026-09-19T19-00-00Z
B_PREV = Fraction(
    67912972013875969263511036761749020093804681381152096968758979249620085662158905166455464312429913990367412237074967475168634442739,
    107925477439598903973574775478848995038155897130780425053567086312912915161198061867187500000000000000000000000000000000000000000000,
)

# predecessor non-C4 chain correction
DELTA_CHAIN_OLD = Fraction(3673530000, 87180364995004919)
Q_OLD = Fraction(147939, 2800)

# central shape subfamily |y3|,|y4| <= a
a = Fraction(36, 125)
V_TOTAL = Fraction(81, 400)
CENTRAL_FRACTION = (2 * a) ** 2
V_CAP = V_TOTAL * CENTRAL_FRACTION
assert V_CAP == Fraction(26244, 390625)
assert CENTRAL_FRACTION == Fraction(5184, 15625)

# sharper per-vertex upper bounds for the internal second-neighbor distances
U1 = U4 = Fraction(229, 100)
U2 = Fraction(133, 100)
U3 = Fraction(177, 100)
assert U1 * U1 - Fraction(8321, 1600) == Fraction(1739, 40000)
assert U2 * U2 - Fraction(2801, 1600) == Fraction(731, 40000)
assert U3 * U3 - Fraction(1241, 400) == Fraction(19, 625)

# common path-boundary surplus delta, with vertex-wise guard radii
delta = Fraction(1, 2)
R1 = R4 = U1 + delta
R2 = U2 + delta
R3 = U3 + delta
assert R1 == Fraction(279, 100)
assert R2 == Fraction(183, 100)
assert R3 == Fraction(227, 100)

# Capsule containment.  The comparison points on [p1,p4] have the same x-coordinate
# as p2 and p3, so these are direct Euclidean-distance upper bounds.
p2_dist_up = a * Fraction(40, 111)
p3_dist_up = a * Fraction(200, 111)
assert p2_dist_up == Fraction(96, 925)
assert p3_dist_up == Fraction(96, 185)
assert R1 - R2 - p2_dist_up == Fraction(792, 925)
assert R1 - R3 - p3_dist_up == Fraction(1, 925)

# Endpoint-segment length bound on the central shape family.
D_UP = Fraction(81, 25)
D2_MAX = Fraction(129, 40) ** 2 + a * a
assert D_UP * D_UP - D2_MAX == Fraction(14031, 1000000)

# Capsule area coefficient, using pi < 22/7.
PI_UP = Fraction(22, 7)
Q_CAP = 2 * R1 * D_UP + PI_UP * R1 * R1
assert Q_CAP == Fraction(1489023, 35000)
assert Q_CAP < Q_OLD

SQRTQ_CAP_UP = Fraction(261, 40)
assert SQRTQ_CAP_UP * SQRTQ_CAP_UP - Q_CAP == Fraction(8991, 280000)

# pi^(3/2) > 3*(17/10) = 51/10.
PI32_LOW = Fraction(51, 10)

# Campbell-Mecke / exact-binomial limiting correction on the central subfamily:
# (5*pi^(3/2)/64) * V * delta * Q^(-7/2).
DELTA_CAP_NEW = (
    Fraction(5, 64)
    * PI32_LOW
    * V_CAP
    * delta
    / (Q_CAP ** 3 * SQRTQ_CAP_UP)
)
assert DELTA_CAP_NEW == Fraction(1166200000, 43777749624439689)

# The predecessor chain certificate is linear in shape volume; remove exactly the
# portion assigned to this central subfamily before inserting the stronger capsule term.
DELTA_CAP_OLD = DELTA_CHAIN_OLD * CENTRAL_FRACTION
assert DELTA_CAP_OLD == Fraction(30469727232, 2179509124875122975)
assert DELTA_CAP_NEW > DELTA_CAP_OLD

NET = DELTA_CAP_NEW - DELTA_CAP_OLD
assert NET == Fraction(
    1207847451541900648780089152,
    95414004772964790053367229345754775,
)
assert NET > Fraction(1, 100_000_000)

B_NEW = B_PREV + NET
assert B_NEW == Fraction(
    12234885369899315774910192590367613149468633559630832101342942986342507415367247043258638762394714330725215296855853141419683832042798882673372297,
    19443351973040638050987304673433346221975007518723198189172396736647229533566751930247359385542476562500000000000000000000000000000000000000000000,
)
assert B_NEW > Fraction(62925803, 100000000)

getcontext().prec = 80

def dec(x):
    return Decimal(x.numerator) / Decimal(x.denominator)

print("P0257 capsule-guard exact checker")
print("CENTRAL_FRACTION =", CENTRAL_FRACTION)
print("V_CAP =", V_CAP)
print("U1_SQ_SLACK =", U1 * U1 - Fraction(8321, 1600))
print("U2_SQ_SLACK =", U2 * U2 - Fraction(2801, 1600))
print("U3_SQ_SLACK =", U3 * U3 - Fraction(1241, 400))
print("P2_CAPSULE_SLACK =", R1 - R2 - p2_dist_up)
print("P3_CAPSULE_SLACK =", R1 - R3 - p3_dist_up)
print("D2_CAPSULE_SLACK =", D_UP * D_UP - D2_MAX)
print("Q_OLD =", Q_OLD, dec(Q_OLD))
print("Q_CAP =", Q_CAP, dec(Q_CAP))
print("SQRTQ_CAP_SQUARE_SLACK =", SQRTQ_CAP_UP * SQRTQ_CAP_UP - Q_CAP)
print("DELTA_CAP_OLD =", DELTA_CAP_OLD, dec(DELTA_CAP_OLD))
print("DELTA_CAP_NEW =", DELTA_CAP_NEW, dec(DELTA_CAP_NEW))
print("NET_MOVEMENT =", NET, dec(NET))
print("B_PREV =", dec(B_PREV))
print("B_NEW =", B_NEW)
print("B_NEW_DECIMAL =", dec(B_NEW))
print("B_NEW_GT_0.62925803 =", B_NEW > Fraction(62925803, 100000000))
print("ALL_EXACT_FINITE_CHECKS_PASS")
