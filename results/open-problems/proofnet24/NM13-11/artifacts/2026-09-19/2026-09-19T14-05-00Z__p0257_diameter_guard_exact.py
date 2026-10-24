from fractions import Fraction
from math import isqrt

# NM13-11 / P0257 exact diameter-compressed guard checker.
# Exact rational enumeration and endpoint arithmetic only; no floating point
# is load-bearing. The external geometric input is the known sharp small
# quadrilateral perimeter theorem P <= (2+sqrt(6)-sqrt(2))*diameter.

def sqrt_upper(x: Fraction, D: int = 1000) -> Fraction:
    assert x >= 0
    if x == 0:
        return Fraction(0)
    p, q = x.numerator, x.denominator
    N = p * D * D
    m = isqrt(N // q)
    if m * m * q < N:
        m += 1
    assert m * m * q >= N
    return Fraction(m, D)

def absmax(lo: Fraction, hi: Fraction) -> Fraction:
    return max(abs(lo), abs(hi))

step = Fraction(1, 10)
a_grid = [Fraction(-1, 2) + i * step for i in range(11)]
b_grid = [Fraction(2, 5) + i * step for i in range(13)]
c_grid = [Fraction(2, 5) + i * step for i in range(13)]
d_grid = [Fraction(2, 5) + i * step for i in range(13)]

accepted = 0
min_diag_margin = None
min_delta = None
max_g = None
max_Q_rectangle = None

for ia in range(10):
    A0, A1 = a_grid[ia], a_grid[ia + 1]
    for ib in range(12):
        B0, B1 = b_grid[ib], b_grid[ib + 1]
        for ic in range(12):
            C0, C1 = c_grid[ic], c_grid[ic + 1]
            for idd in range(12):
                D0, D1 = d_grid[idd], d_grid[idd + 1]

                # p1=(0,0), p2=(1,0), p3=(a,b), p4=(c,d).
                # Selected long matching edges are p1p4 and p2p3.
                diag14_min2 = C0 * C0 + D0 * D0
                diag23_min2 = (1 - A1) * (1 - A1) + B0 * B0
                L2 = min(diag14_min2, diag23_min2)

                side12_max2 = Fraction(1)
                side13_max2 = absmax(A0, A1) ** 2 + B1 * B1
                side24_max2 = absmax(C0 - 1, C1 - 1) ** 2 + D1 * D1
                side34_max2 = (
                    absmax(C0 - A1, C1 - A0) ** 2
                    + absmax(D0 - B1, D1 - B0) ** 2
                )
                U2 = max(side12_max2, side13_max2, side24_max2, side34_max2)

                if L2 <= U2:
                    continue

                diag14_max2 = absmax(C0, C1) ** 2 + D1 * D1
                diag23_max2 = absmax(1 - A0, 1 - A1) ** 2 + B1 * B1
                R2 = max(U2, diag14_max2, diag23_max2)

                # Strict guard radius g exceeds every pair distance.
                g = sqrt_upper(R2, 1000) + Fraction(1, 1000)
                u = sqrt_upper(U2, 1000)
                delta = g - u
                if delta <= 0:
                    continue

                # Predecessor rectangle-based Steiner guard, retained only
                # to certify that the new diameter compression is stronger.
                xmin = min(Fraction(0), Fraction(1), A0, C0)
                xmax = max(Fraction(0), Fraction(1), A1, C1)
                ymin = Fraction(0)
                ymax = max(B1, D1)
                W, H = xmax - xmin, ymax - ymin
                Q_rectangle = (
                    W * H + 2 * g * (W + H) + Fraction(22, 7) * g * g
                )

                accepted += 1
                margin = L2 - U2
                min_diag_margin = (
                    margin if min_diag_margin is None
                    else min(min_diag_margin, margin)
                )
                min_delta = delta if min_delta is None else min(min_delta, delta)
                max_g = g if max_g is None else max(max_g, g)
                max_Q_rectangle = (
                    Q_rectangle if max_Q_rectangle is None
                    else max(max_Q_rectangle, Q_rectangle)
                )

assert 10 * 12 * 12 * 12 == 17280
assert accepted == 1796
assert min_diag_margin == Fraction(1, 100)
assert min_delta == Fraction(141, 1000)
assert max_g == Fraction(283, 125)
assert max_Q_rectangle == Fraction(3827833, 109375)

# Known exact small-quadrilateral theorem:
# P(K)/diam(K) <= 2 + sqrt(6) - sqrt(2).
# Exact rational relaxation:
# sqrt(6) < 49/20 and sqrt(2) > 7/5, hence the sharp ratio < 61/20.
assert Fraction(49, 20) ** 2 > 6
assert Fraction(7, 5) ** 2 < 2
perimeter_ratio_upper = Fraction(61, 20)

# Self-contained area bound for a convex hull of at most four vertices:
# A(K) <= diam(K)^2/2 (quadrilateral diagonal formula; triangle is smaller).
# Since diam(K) < g and pi < 22/7, Steiner gives
# |K+B_g| <= (1/2 + 61/20 + 22/7) g^2 = (937/140) g^2.
steiner_coeff = Fraction(1, 2) + perimeter_ratio_upper + Fraction(22, 7)
assert steiner_coeff == Fraction(937, 140)

Q_diameter = steiner_coeff * max_g * max_g
assert Q_diameter == Fraction(75043393, 2187500)
assert Q_diameter < max_Q_rectangle

qroot = sqrt_upper(Q_diameter, 1000) + Fraction(1, 1000)
assert qroot == Fraction(5859, 1000)
assert qroot * qroot > Q_diameter

# Campbell-Mecke prefactor lower from predecessor:
# (5*pi^(3/2))/128 > 51/256 using pi>3 and sqrt(pi)>17/10.
prefactor_lower = Fraction(51, 256)
cell_volume = step ** 4
atlas_diameter_lower = (
    prefactor_lower
    * accepted
    * cell_volume
    * min_delta
    / (Q_diameter ** 3 * qroot)
)
assert atlas_diameter_lower == Fraction(
    13411559295654296875,
    628840228764059875161752016,
)

old_atlas_lower = Fraction(
    6759425885009765625,
    339829027379933753224631296,
)
assert atlas_diameter_lower > old_atlas_lower

# Replace, do not add to, the predecessor atlas correction.
B_current = Fraction(
    1631470499263030121036034768604328605573396461083400872097661500093812049,
    2592689723052473092839289062500000000000000000000000000000000000000000000,
)
B_new = B_current - old_atlas_lower + atlas_diameter_lower
movement = B_new - B_current
assert movement > 0

expected_B_new = Fraction(
    193214201572982934989857783744396430558567581073465840160154030146749346281,
    307050892951201110918824226562500000000000000000000000000000000000000000000,
)
assert B_new == expected_B_new
assert B_new > Fraction(6292579048, 10_000_000_000)

print("P0257 diameter-compressed quadruple guard exact certificate")
print("candidate_cells =", 17280)
print("accepted_cells =", accepted)
print("accepted_shape_volume =", accepted * cell_volume)
print("min_diagonal_minus_side_squared =", min_diag_margin)
print("min_guard_bonus_delta =", min_delta)
print("max_strict_guard_radius =", max_g)
print("old_rectangle_Q =", max_Q_rectangle)
print("perimeter_ratio_rational_upper =", perimeter_ratio_upper)
print("steiner_coeff =", steiner_coeff)
print("new_diameter_Q =", Q_diameter)
print("new_Q_lt_old_Q =", Q_diameter < max_Q_rectangle)
print("qroot_upper =", qroot)
print("qroot_upper_squared_gt_new_Q =", qroot * qroot > Q_diameter)
print("new_atlas_lower_exact =", atlas_diameter_lower)
print("old_atlas_lower_exact =", old_atlas_lower)
print("new_atlas_gt_old_atlas =", atlas_diameter_lower > old_atlas_lower)
print("metric_movement_exact =", movement)
print("B_new_exact =", B_new)
print("B_new_gt_0.6292579048 =", B_new > Fraction(6292579048, 10_000_000_000))
print("ALL_EXACT_FINITE_CHECKS_PASS")
