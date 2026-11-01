from fractions import Fraction
from math import isqrt

# NM13-11 / P0257 exact atlas checker.
# Exact rational enumeration only; no floating point is used in certification.


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
max_Q = None

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

                # A cell is accepted only if every selected diagonal is
                # strictly longer than every one of the four selected sides
                # throughout the entire cell.
                if L2 <= U2:
                    continue

                diag14_max2 = absmax(C0, C1) ** 2 + D1 * D1
                diag23_max2 = absmax(1 - A0, 1 - A1) ** 2 + B1 * B1
                R2 = max(U2, diag14_max2, diag23_max2)

                # Strict guard radius: g > sqrt(R2).
                g = sqrt_upper(R2, 1000) + Fraction(1, 1000)
                # Upper bound on every second-neighbor side radius.
                u = sqrt_upper(U2, 1000)
                delta = g - u
                if delta <= 0:
                    continue

                # Rectangle containing the normalized convex hull.
                xmin = min(Fraction(0), Fraction(1), A0, C0)
                xmax = max(Fraction(0), Fraction(1), A1, C1)
                ymin = Fraction(0)
                ymax = max(B1, D1)
                W, H = xmax - xmin, ymax - ymin

                # Steiner upper bound for union of four radius-g disks:
                # area(conv Q)+g*perimeter(conv Q)+pi*g^2
                # <= W*H + 2g(W+H) + (22/7)g^2.
                Q = W * H + 2 * g * (W + H) + Fraction(22, 7) * g * g

                accepted += 1
                margin = L2 - U2
                min_diag_margin = (
                    margin
                    if min_diag_margin is None
                    else min(min_diag_margin, margin)
                )
                min_delta = delta if min_delta is None else min(min_delta, delta)
                max_Q = Q if max_Q is None else max(max_Q, Q)

assert 10 * 12 * 12 * 12 == 17280
assert accepted == 1796
assert min_diag_margin == Fraction(1, 100)
assert min_delta == Fraction(141, 1000)
assert max_Q == Fraction(3827833, 109375)

qroot = sqrt_upper(max_Q, 1000) + Fraction(1, 1000)
assert qroot == Fraction(5917, 1000)
assert qroot * qroot > max_Q

# Campbell-Mecke + final factor 1/2 converting a 2L bonus to L:
# coefficient = (1/2)(1/4!)(2*pi)(15*sqrt(pi)/16)
#             = 5*pi^(3/2)/128.
# Use exact elementary lower bounds pi>3 and sqrt(pi)>17/10:
prefactor_lower = Fraction(51, 256)
cell_volume = step**4
atlas_lower = (
    prefactor_lower
    * accepted
    * cell_volume
    * min_delta
    / (max_Q**3 * qroot)
)
assert atlas_lower == Fraction(
    6759425885009765625,
    339829027379933753224631296,
)

# Previous four-point fixed-block correction must be REPLACED, not added:
old_quad_delta = Fraction(
    1579888671017488353,
    4294967296000000000000000000000,
)
B_current = Fraction(
    2517031533989904805963567012121706380405600461327497,
    4000000000000000000000000000000000000000000000000000,
)
B_prequad = B_current - old_quad_delta
assert B_prequad == Fraction(
    4916077214821159023396228863546259379089219326781,
    7812500000000000000000000000000000000000000000000,
)

B_new = B_prequad + atlas_lower
movement = B_new - B_current
assert movement > 0
assert B_new > Fraction(6292579, 10_000_000)

expected_B_new = Fraction(
    1631470499263030121036034768604328605573396461083400872097661500093812049,
    2592689723052473092839289062500000000000000000000000000000000000000000000,
)
assert B_new == expected_B_new

print("P0257 closed-3-nearest quadruple shape-atlas exact certificate")
print("candidate_cells =", 17280)
print("accepted_cells =", accepted)
print("accepted_shape_volume =", accepted * cell_volume)
print("min_diagonal_minus_side_squared =", min_diag_margin)
print("min_guard_bonus_delta =", min_delta)
print("max_Q =", max_Q)
print("qroot_upper =", qroot)
print("qroot_upper_squared_gt_max_Q =", qroot * qroot > max_Q)
print("prefactor_lower =", prefactor_lower)
print("atlas_lower_exact =", atlas_lower)
print("old_fixed_quad_delta_exact =", old_quad_delta)
print("atlas_replacement_gt_old_fixed_quad =", atlas_lower > old_quad_delta)
print("metric_movement_exact =", movement)
print("B_new_exact =", B_new)
print("B_new_gt_0.6292579 =", B_new > Fraction(6292579, 10_000_000))
print("ALL_EXACT_FINITE_CHECKS_PASS")
