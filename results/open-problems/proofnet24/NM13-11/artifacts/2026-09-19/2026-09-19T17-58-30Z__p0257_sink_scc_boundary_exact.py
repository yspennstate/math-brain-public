from fractions import Fraction

# NM13-11 / P0257 exact checker:
# four-point sink-SCC atlas and Hamiltonian boundary-charge replacement.
# All certification arithmetic is exact rational arithmetic.

F = Fraction

def absmax(lo, hi):
    return max(abs(lo), abs(hi))

step = F(1, 10)
a_grid = [F(-1, 2) + i * step for i in range(11)]
b_grid = [F(2, 5) + i * step for i in range(13)]
c_grid = [F(2, 5) + i * step for i in range(13)]
d_grid = [F(2, 5) + i * step for i in range(13)]

accepted = 0
min_diag_margin = None
max_U2 = F(0)
max_R2 = F(0)

for ia in range(10):
    A0, A1 = a_grid[ia], a_grid[ia + 1]
    for ib in range(12):
        B0, B1 = b_grid[ib], b_grid[ib + 1]
        for ic in range(12):
            C0, C1 = c_grid[ic], c_grid[ic + 1]
            for idd in range(12):
                D0, D1 = d_grid[idd], d_grid[idd + 1]

                # p1=(0,0), p2=(1,0), p3=(a,b), p4=(c,d).
                # The selected long matching is p1-p4 and p2-p3.
                # The four complementary edges must be uniformly shorter;
                # then each vertex's two nearest INTERNAL neighbors are its
                # two cycle neighbors, so the internal directed 2NN graph is C4.
                diag14_min2 = C0*C0 + D0*D0
                diag23_min2 = (1-A1)*(1-A1) + B0*B0
                L2 = min(diag14_min2, diag23_min2)

                side12_max2 = F(1)
                side13_max2 = absmax(A0, A1)**2 + B1*B1
                side24_max2 = absmax(C0-1, C1-1)**2 + D1*D1
                side34_max2 = (
                    absmax(C0-A1, C1-A0)**2
                    + absmax(D0-B1, D1-B0)**2
                )
                U2 = max(side12_max2, side13_max2, side24_max2, side34_max2)

                if L2 <= U2:
                    continue

                diag14_max2 = absmax(C0, C1)**2 + D1*D1
                diag23_max2 = absmax(1-A0, 1-A1)**2 + B1*B1
                R2 = max(U2, diag14_max2, diag23_max2)

                accepted += 1
                margin = L2 - U2
                min_diag_margin = margin if min_diag_margin is None else min(min_diag_margin, margin)
                max_U2 = max(max_U2, U2)
                max_R2 = max(max_R2, R2)

assert 10 * 12 * 12 * 12 == 17280
assert accepted == 1796
assert min_diag_margin == F(1, 100)
assert max_U2 == F(401, 100)
assert max_R2 == F(128, 25)

# Exact rational upper bounds on the largest internal 2NN side U
# and on the shape diameter D.
Ubar = F(801, 400)      # 2.0025
Dbar = F(2263, 1000)   # 2.263
assert Ubar*Ubar > max_U2
assert Dbar*Dbar > max_R2

# External guard radius H.  If no external point lies within H*s
# of any gadget vertex, every gadget vertex's two nearest neighbors
# are its two C4 neighbors.  Thus the four vertices form a sink SCC
# in the directed two-nearest-neighbor graph.
H = F(5, 2)
delta = H - Ubar
assert delta == F(199, 400)
assert delta > 0

# Convex-parallel-body guard:
# area(K + B_{Hs}) <= [D^2/2 + (61/20) H D + (22/7) H^2] s^2.
# We use D^2 <= max_R2 exactly and D <= Dbar.
Q = max_R2/F(2) + F(61, 20)*H*Dbar + F(22, 7)*H*H
assert Q == F(2209661, 56000)

# Rational upper bound on sqrt(Q), to bound Q^(7/2) from above.
qroot = F(3926, 625)
assert qroot*qroot > Q

# Accepted normalized shape volume.
V = accepted * step**4
assert V == F(449, 2500)

# For every non-endpoint-containing sink SCC, a Hamiltonian path has
# at least two boundary crossings. Relative to the degree-two baseline,
# each crossing pays at least delta*s on the 2L side. Hence the L-side
# bonus is at least delta*s per typical component.
#
# Campbell-Mecke ordered-quadruple coefficient:
# (1/4!)*(2*pi)*(15*sqrt(pi)/16) = 5*pi^(3/2)/64.
# With pi>3 and sqrt(pi)>17/10, this exceeds 51/128.
prefactor_lower = F(51, 128)
sink4_lower = prefactor_lower * V * delta / (Q**3 * qroot)
assert sink4_lower == F(1953771303750000, 21178600162983614506103)

# Current certified four-point term being replaced (diameter guard,
# closed-3NN exit charge), not added to.
old_quad = F(
    13411559295654296875,
    628840228764059875161752016,
)
assert sink4_lower > old_quad
movement = sink4_lower - old_quad
assert movement == F(
    944571941717997011472301284909577998671875,
    13317955771393171902911839310485773138454004553648,
)
assert movement > F(7, 100_000_000)  # > 7e-8

# Frozen metric endpoint from the controlling 17:05 predecessor.
B_before = F(
    641377705174267468101274433764131457347844713295231130249870907152717283443310373029072200251405407093773621126563697479,
    1019260465779289339534879501998404060107472660571426304187235311834417648437500000000000000000000000000000000000000000000,
)
B_after = B_before + movement
expected_B_after = F(
    1036840803576585538238788458409057357623753998433226173823634661443281840749793585890028594106544121959770829209188511,
    1647719764425586367726663550234487807993856583136701789232573772690085937500000000000000000000000000000000000000000000,
)
assert B_after == expected_B_after
assert B_after > F(62925797, 100000000)

print("P0257 four-point sink-SCC Hamiltonian-boundary exact certificate")
print("candidate_cells =", 17280)
print("accepted_cells =", accepted)
print("accepted_shape_volume =", V)
print("min_diagonal_minus_side_squared =", min_diag_margin)
print("max_internal_2NN_side_squared =", max_U2)
print("Ubar =", Ubar)
print("Ubar_squared_gt_max_U2 =", Ubar*Ubar > max_U2)
print("max_shape_diameter_squared =", max_R2)
print("Dbar =", Dbar)
print("Dbar_squared_gt_max_R2 =", Dbar*Dbar > max_R2)
print("H =", H)
print("delta =", delta)
print("guard_Q =", Q)
print("qroot_upper =", qroot)
print("qroot_upper_squared_gt_Q =", qroot*qroot > Q)
print("prefactor_lower =", prefactor_lower)
print("sink4_lower_exact =", sink4_lower)
print("old_quad_exact =", old_quad)
print("sink4_gt_old_quad =", sink4_lower > old_quad)
print("metric_movement_exact =", movement)
print("metric_movement_gt_7e-8 =", movement > F(7, 100_000_000))
print("B_before_exact =", B_before)
print("B_after_exact =", B_after)
print("B_after_gt_0.62925797 =", B_after > F(62925797, 100000000))
print("ALL_EXACT_FINITE_CHECKS_PASS")
