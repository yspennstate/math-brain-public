from fractions import Fraction
from decimal import Decimal, getcontext

getcontext().prec = 50

# Uniform p_c comparison for every (12,8)-group whose standard product
# generators are retained.  Root T_12, discard one parent direction, and
# expose only radius 2 in each T_8 fibre.
p = Fraction(3, 50)
s = 1 - p
h0 = s
h1 = s * (s + p * h0) ** 7
C2 = s * (s + p * h1) ** 8
activation = 1 - C2
GW_mean = 11 * activation
GW_margin = GW_mean - 1

# Exact rational upper bounds for the standard-product adjacency norm.
u11 = Fraction(331663, 100000)  # sqrt(11) < u11
u7 = Fraction(264576, 100000)    # sqrt(7) < u7
base_A_up = 2 * u11 + 2 * u7

# If k new inverse pairs are added, D=20+2k and ||A|| <= base + 2k.
# The chosen floors below are all strictly below the resulting
# nonbacktracking p_{2->2} lower bound.
floors = {
    1: Fraction(819, 10000),
    2: Fraction(698, 10000),
    3: Fraction(609, 10000),
}


def dec(x):
    return Decimal(x.numerator) / Decimal(x.denominator)


print("p0 =", dec(p))
print("truncated_fibre_activation =", dec(activation))
print("GW_mean =", dec(GW_mean))
print("GW_mean_minus_1 =", dec(GW_margin))
print("FIBRE_MEAN_GT_1 =", GW_mean > 1)
print("FIBRE_MARGIN_GT_1_15 =", GW_margin > Fraction(1, 15))
print("SQRT11_UPPER_CERT =", u11 * u11 > 11,
      "slack =", u11 * u11 - 11)
print("SQRT7_UPPER_CERT =", u7 * u7 > 7,
      "slack =", u7 * u7 - 7)

all_ok = (GW_mean > 1 and GW_margin > Fraction(1, 15)
          and u11 * u11 > 11 and u7 * u7 > 7)

for k, floor in floors.items():
    D = 20 + 2 * k
    Q = D - 1
    Aup = base_A_up + 2 * k
    z = 1 / floor
    margin = z + Fraction(Q, 1) / z - Aup
    gap = floor - p
    checks = {
        "Z_ABOVE_SQRT_Q": z * z > Q,
        "ROOT_TEST_POSITIVE": margin > 0,
        "GAP_POSITIVE": gap > 0,
    }
    all_ok = all_ok and all(checks.values())
    print(f"k={k}")
    print("  D =", D)
    print("  A_upper =", dec(Aup))
    print("  pu_floor =", dec(floor))
    print("  z_test =", dec(z))
    print("  z_plus_Q_over_z_minus_A_upper =", margin, "=", dec(margin))
    print("  certified_gap =", gap, "=", dec(gap))
    for name, val in checks.items():
        print(" ", name, "=", val)

assert all_ok
print("ALL_EXACT_CHECKS_PASS")
