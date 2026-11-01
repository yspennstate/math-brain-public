from fractions import Fraction as F
from itertools import combinations

# NM13-11 / P0257 exact five-point closed-4NN pentagon trap checker.
# All load-bearing finite geometry and endpoint arithmetic use Fraction only.

centers = [
    (F(0), F(1)),
    (F(1), F(1,4)),
    (F(3,5), F(-1)),
    (F(-3,5), F(-1)),
    (F(-1), F(1,4)),
]
h = F(1333,10000)
s = F(351,1250)
adj = {
    0: {1,4},
    1: {0,2},
    2: {1,3},
    3: {2,4},
    4: {3,0},
}

def sq_min_interval(lo, hi):
    assert lo <= hi
    if lo <= 0 <= hi:
        return F(0)
    return min(lo*lo, hi*hi)

def sq_max_interval(lo, hi):
    assert lo <= hi
    return max(lo*lo, hi*hi)

def d2_bounds(i,j):
    xi, yi = centers[i]
    xj, yj = centers[j]
    dx0, dx1 = xi-h-(xj+h), xi+h-(xj-h)
    dy0, dy1 = yi-h-(yj+h), yi+h-(yj-h)
    lo = sq_min_interval(dx0,dx1) + sq_min_interval(dy0,dy1)
    hi = sq_max_interval(dx0,dx1) + sq_max_interval(dy0,dy1)
    return lo,hi

# Target squares are pairwise disjoint.
for i,j in combinations(range(5),2):
    xi,yi = centers[i]
    xj,yj = centers[j]
    assert max(abs(xi-xj), abs(yi-yj)) > 2*h

# Method #16: certify the two-nearest-neighbor graph is exactly C5.
min_cycle_gap = None
max_adj2 = F(0)
max_pair2 = F(0)
for i in range(5):
    adj_upper = max(d2_bounds(i,j)[1] for j in adj[i])
    nonadj_lower = min(
        d2_bounds(i,k)[0]
        for k in range(5)
        if k != i and k not in adj[i]
    )
    gap = nonadj_lower - adj_upper
    assert gap > 0
    min_cycle_gap = gap if min_cycle_gap is None else min(min_cycle_gap,gap)
    max_adj2 = max(max_adj2, adj_upper)

for i,j in combinations(range(5),2):
    max_pair2 = max(max_pair2, d2_bounds(i,j)[1])

assert min_cycle_gap == F(3,5000)
assert max_adj2 == F(34305389,12500000)
assert max_pair2 == F(73605889,12500000)

# No internal 3-subset is a closed 2-nearest triple.
for S_tuple in combinations(range(5),3):
    S = set(S_tuple)
    is_closed = all(adj[v] <= S for v in S)
    assert not is_closed

# No internal 4-subset is a closed 3-nearest quadruple.
# For each omitted q, find v,w in the 4-subset with q uniformly closer
# to v than w is. Then q must enter v's first three gadget neighbors.
quad_witness_margin = {}
for q in range(5):
    S = [x for x in range(5) if x != q]
    best = None
    witness = None
    for v in S:
        for w in S:
            if w == v:
                continue
            margin = d2_bounds(v,w)[0] - d2_bounds(v,q)[1]
            if best is None or margin > best:
                best = margin
                witness = (v,w)
    assert best is not None and best > 0
    quad_witness_margin[q] = (best, witness)

assert min(m for m,_ in quad_witness_margin.values()) == F(9173111,25000000)

# Exact closure guard.
# G exceeds every normalized internal distance, while u exceeds every
# normalized cyclic-neighbor (hence second-neighbor) distance.
G = F(2427,1000)
u = F(1657,1000)
assert G*G > max_pair2
assert u*u > max_adj2

# Put the scaled cells in a square block with half-side H.
# Every gadget coordinate has absolute value <= s(1+h); every point
# outside the block is therefore at Euclidean distance >= sG.
H = s * (F(1) + h + G)
block_side = 2*H
A = block_side * block_side
assert H == F(12496653,12500000)
assert A == F(156166336202409,39062500000000)
assert A < 4

# Internal distances are strictly below the external lower distance.
assert s*s*max_pair2 < (s*G)**2

# Second-neighbor distance < su, fifth-neighbor distance >= sG.
delta = s*(G-u)
assert delta == F(27027,125000)
assert s*s*max_adj2 < (s*u)**2

# Each labeled target square has exact area a.
cell_side = 2*h*s
a = cell_side*cell_side
assert cell_side == F(467883,6250000)
assert a == F(218914501689,39062500000000)

# Exact finite-n block event:
# exactly one sample point in each of the five cells and no other point
# in the block, when the source square has area n.
def falling(n,k):
    z = 1
    for j in range(k):
        z *= n-j
    return z

def p_success(n):
    nF = F(n)
    return F(falling(n,5)) * (a/nF)**5 * (F(1)-A/nF)**(n-5)

for n in (5,6,10,50,200):
    p = p_success(n)
    assert p > 0
    assert p < 1

# Analytic seed used in the proof:
# e = 5/2 + sum_{k>=3} 1/k! < 5/2 + 2/9 = 49/18.
# Since A<4, exp(-A) > exp(-4) > (18/49)^4.
void_lower = F(18,49)**4
density_lower = a**5 * void_lower / A

# Each nonterminal closed-4NN five-set contributes > delta on the 2L
# side, hence > delta/2 on the L side.
correction = F(1,2)*delta*density_lower
assert correction == F(
    103378033182640540347138740422965357233277009068757704011629,
    37976910704917354451026767492294311523437500000000000000000000000000000000,
)

B_before = F(
    193214201572982934989857783744396430558567581073465840160154030146749346281,
    307050892951201110918824226562500000000000000000000000000000000000000000000,
)
B_after = B_before + correction
assert B_after > B_before
expected_B_after = F(
    3847056774953229044237009118302761877406033721941558197688508436151771210158889400069556382518559477259,
    6113640759150720907870373094172649443624466657638549804687500000000000000000000000000000000000000000000,
)
assert B_after == expected_B_after
assert B_after > F(62925790482456228, 10**17)

print("P0257 exact five-point closed-4NN pentagon trap certificate")
print("cell_halfwidth_normalized =", h)
print("scale =", s)
print("min_C5_2NN_squared_gap =", min_cycle_gap)
print("max_2NN_squared_normalized =", max_adj2)
print("max_internal_squared_normalized =", max_pair2)
print("min_quad_nonclosure_witness_margin =", min(m for m,_ in quad_witness_margin.values()))
print("G =", G)
print("u =", u)
print("block_halfside =", H)
print("block_area_A =", A)
print("cell_side =", cell_side)
print("cell_area_a =", a)
print("twoL_bonus_delta =", delta)
print("void_lower =", void_lower)
print("density_lower_exact =", density_lower)
print("five_point_correction_exact =", correction)
print("B_before_exact =", B_before)
print("B_after_exact =", B_after)
print("B_after_gt_0.62925790482456228 =", B_after > F(62925790482456228, 10**17))
print("ALL_EXACT_FINITE_CHECKS_PASS")
