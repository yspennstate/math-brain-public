from fractions import Fraction
from decimal import Decimal, getcontext

# Exact algebraic self-check for the PROB10-09 central-surface-extension candidate.
# This checks only finite/rational algebra. It does NOT replace the written
# direct-integral/diamagnetic proof or constitute an independent audit.

p = Fraction(31, 200)
phi = 1 - (1 - p) ** 3 / (1 - p + p * p) ** 2
witness = 5 * phi - 1

# Bartholdi records Nagnibeda's rigorous ||M_2|| <= 0.662816.
# Deliberately round upward to 0.663.
nagnibeda_printed = Fraction(662816, 10**6)
nagnibeda_round = Fraction(663, 1000)
surface_adj_bound = 8 * nagnibeda_round
R = surface_adj_bound + 2

disc = R * R - 36
expected_disc = Fraction(271069, 15625)

# For R=913/125 and Q=9,
# beta^{-1}=(913-sqrt(271069))/2250.
# p0 < beta^{-1} iff sqrt(271069) < 2257/4,
# proved by squaring positive quantities.
square_margin = 2257**2 - 16 * 271069

getcontext().prec = 60
sqrtD = Decimal(271069).sqrt()
p2_lower = (Decimal(913) - sqrtD) / Decimal(2250)
gap_lower = p2_lower - Decimal(31) / Decimal(200)

checks = {
    "fiber_witness_positive": witness > 0,
    "nagnibeda_rounding_up_valid": nagnibeda_printed < nagnibeda_round,
    "surface_adj_bound_identity": surface_adj_bound == Fraction(663, 125),
    "central_R_identity": R == Fraction(913, 125),
    "discriminant_identity": disc == expected_disc,
    "p0_lt_p2_lower": square_margin > 0,
    "gap_positive": gap_lower > 0,
}

print("P0 =", p)
print("PHI_Z(P0) =", phi)
print("FIBER_WITNESS_5PHI_MINUS_1 =", witness)
print("FIBER_WITNESS_POSITIVE =", witness > 0)
print("NAGNIBEDA_PRINTED_BOUND =", nagnibeda_printed)
print("ROUNDING_UP_VALID =", nagnibeda_printed < nagnibeda_round)
print("SURFACE_ADJ_RATIONAL_BOUND =", surface_adj_bound)
print("CENTRAL_EXTENSION_R =", R)
print("R_SQUARED_MINUS_36 =", disc)
print("DISC_IDENTITY_OK =", disc == expected_disc)
print("P0_LT_P2LB_SQUARE_MARGIN =", square_margin)
print("P0_LT_P2LB =", square_margin > 0)
print("P2_LOWER_NUMERIC =", p2_lower)
print("GAP_LOWER_NUMERIC =", gap_lower)
print("GAP_EXACT = (2257 - 4*sqrt(271069))/9000")
print("CHECKS =", checks)
print("VERDICT =", "PASS_SELF_CHECK_PARTIAL" if all(checks.values()) else "FAIL")
