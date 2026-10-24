from fractions import Fraction
from decimal import Decimal, getcontext

# Exact-arithmetic self-check for NM13-11 / P0257.
# This certifies the finite geometry and rational endpoint arithmetic for the
# four-point closed 3-nearest-neighbor trap used in the accompanying report.
# No simulation or floating-point inequality is used in any assertion.

S = Fraction(15, 8)          # guard-block side length
c = Fraction(21, 100)        # target-cell center coordinate magnitude
h = Fraction(111, 3200)      # target-cell half-width
A = S * S
cell_area = (2 * h) ** 2
R_guard = S / 2 - (c + h)

# For a point in one target cell and points in the two adjacent target cells,
# each adjacent distance squared is at most adj2.  Any diagonal-cell distance
# is at least diag_min2 and every internal distance is at most diag_max2.
adj2 = (2 * (c + h)) ** 2 + (2 * h) ** 2
diag_min2 = 2 * (2 * (c - h)) ** 2
diag_max2 = 2 * (2 * (c + h)) ** 2

assert adj2 < Fraction(1, 4)             # hence r_2 < 1/2
assert adj2 < diag_min2                  # adjacent < diagonal: no internal closed triple
assert diag_max2 < R_guard * R_guard     # all 3 internal points precede every outside point

# In 2L the terminal vertex of each successful nonterminal gadget gains
# r_4-r_2 > R_guard-1/2 over the generic r_1+r_2 charge.
gap_2L = R_guard - Fraction(1, 2)
assert gap_2L == Fraction(617, 3200)
bonus_L = gap_2L / 2
assert bonus_L == Fraction(617, 6400)

# Analytic step used on the proof page:
# for 0<x<1, 1-x < exp(-x).  With x=A/64 this gives
# (1-A/64)^64 < exp(-A).  The only finite numerical comparison needed here is
# that this exact rational lower seed is itself > 1/40.
x = A / 64
exp_lower_seed = (1 - x) ** 64
assert 0 < x < 1
assert exp_lower_seed > Fraction(1, 40)

# In the area-n source square, a fixed successful block has limiting
# probability cell_area^4 exp(-A), while the block density tends to 1/A.
# Using exp(-A)>1/40 gives the following exact source-model density lower bound.
gadget_density_lo = cell_area ** 4 / (40 * A)
delta_b_lo = bonus_L * gadget_density_lo
assert delta_b_lo == Fraction(
    1579888671017488353,
    4294967296000000000000000000000,
)

previous_cert = Fraction(
    4916077214821159023396228863546259379089219326781,
    7812500000000000000000000000000000000000000000000,
)
new_cert = previous_cert + delta_b_lo
assert new_cert == Fraction(
    2517031533989904805963567012121706380405600461327497,
    4000000000000000000000000000000000000000000000000000,
)
assert new_cert > previous_cert
assert new_cert > Fraction(629257883497476, 10**15)

getcontext().prec = 80

def dec(q):
    return Decimal(q.numerator) / Decimal(q.denominator)

print("P0257 four-point closed 3-nearest trap exact certificate")
print("S =", S, "A =", A)
print("c =", c, "h =", h, "target_cell_area =", cell_area)
print("guard_radius_lower =", R_guard)
print("adjacent_distance_sq_upper =", adj2)
print("diagonal_distance_sq_lower =", diag_min2)
print("diagonal_distance_sq_upper =", diag_max2)
print("ADJ_LT_HALF =", adj2 < Fraction(1, 4))
print("ADJ_LT_DIAG =", adj2 < diag_min2)
print("DIAG_LT_GUARD =", diag_max2 < R_guard * R_guard)
print("2L_gap_per_successful_nonterminal_gadget_gt =", gap_2L)
print("L_bonus_per_successful_nonterminal_gadget_gt =", bonus_L)
print("finite_exp_lower_seed =", exp_lower_seed)
print("FINITE_EXP_LOWER_SEED_GT_1_OVER_40 =", exp_lower_seed > Fraction(1, 40))
print("gadget_density_lower_using_exp_gt_1_over_40 =", gadget_density_lo)
print("delta_b_lower_exact =", delta_b_lo)
print("delta_b_lower_decimal =", dec(delta_b_lo))
print("previous_cert_exact =", previous_cert)
print("new_cert_exact =", new_cert)
print("new_cert_decimal =", dec(new_cert))
print("NEW_CERT_GT_PREVIOUS =", new_cert > previous_cert)
print("NEW_CERT_GT_0.629257883497476 =", new_cert > Fraction(629257883497476, 10**15))
print("ALL_EXACT_FINITE_CHECKS_PASS")
