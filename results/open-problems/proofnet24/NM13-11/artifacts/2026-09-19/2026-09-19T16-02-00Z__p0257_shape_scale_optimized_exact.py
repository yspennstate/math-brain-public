from fractions import Fraction as F
from itertools import combinations

# NM13-11 / P0257 exact checker for the reflection-symmetric
# five-point closed-4NN shape/scale optimization.
# All load-bearing finite geometry and endpoint arithmetic use Fraction only.

centers = [
    (F(0), F(1)),
    (F(1), F(15569,62500)),
    (F(336053,500000), F(-1)),
    (F(-336053,500000), F(-1)),
    (F(-1), F(15569,62500)),
]
h = F(18677,125000)
s = F(29,100)
u = F(167,100)
G = F(627,250)

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

# Robust C5 two-nearest-neighbor graph.
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

assert min_cycle_gap == F(42029,10000000000)
assert max_adj2 == F(34861176877,12500000000)
assert max_pair2 == F(314035122997,50000000000)
assert u*u - max_adj2 == F(73123,12500000000)
assert G*G - max_pair2 == F(468077003,50000000000)

# No internal 3-subset is a closed 2NN triple.
for S_tuple in combinations(range(5),3):
    S = set(S_tuple)
    assert not all(adj[v] <= S for v in S)

# No internal 4-subset is a closed 3NN quadruple:
# for each omitted q, some included v sees q uniformly closer than
# one included w, so q enters v's first three gadget neighbors.
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

assert min(m for m,_ in quad_witness_margin.values()) == F(51308167,488281250)

# Closure guard and block geometry.
# Every internal pair is < sG, while every point outside the block
# is at distance >= sG from every gadget point.
R = F(1) + h + G
H = s * R
block_side = 2*H
A = block_side * block_side
assert R == F(457177,125000)
assert H == F(13258133,12500000)
assert A == F(175778090645689,39062500000000)
assert A < F(9,2)
assert u*u > max_adj2
assert G*G > max_pair2

# Target-cell area and exit-rank bonus.
cell_side = 2*h*s
a = cell_side*cell_side
delta = s*(G-u)
assert cell_side == F(541633,6250000)
assert a == F(293366306689,39062500000000)
assert delta == F(12151,50000)

# Finite-n success probability identity in the area-n source square.
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

# Analytic rational void lower bound:
# e < 49/18 < 25/9, hence sqrt(e) < 5/3.
# Since A < 9/2,
# exp(-A) > exp(-9/2) > (18/49)^4 * (3/5).
void_lower = F(18,49)**4 * F(3,5)
assert void_lower == F(314928,28824005)

# New five-point term.
new_correction = F(1,2) * delta * a**5 * void_lower / A
expected_new_correction = F(
    617957324772210680294839810774947619464673905410513091139772637,
    87668429669475046757725067436695098876953125000000000000000000000000000000000,
)
assert new_correction == expected_new_correction

# Previous fixed-pentagon five-point term (to be replaced, not added).
old_correction = F(
    103378033182640540347138740422965357233277009068757704011629,
    37976910704917354451026767492294311523437500000000000000000000000000000000,
)
assert new_correction > old_correction
movement = new_correction - old_correction
assert movement == F(
    480806627016681356772296428587326521482399703460995420940745822473919759,
    111126187791499162154133312360499985516071319580078125000000000000000000000000000000000,
)

B_before = F(
    3847056774953229044237009118302761877406033721941558197688508436151771210158889400069556382518559477259,
    6113640759150720907870373094172649443624466657638549804687500000000000000000000000000000000000000000000,
)
B_after = B_before - old_correction + new_correction
expected_B_after = F(
    4440401023269606295089343772266001019765040495180329193870131957751848714940547584423907813736824655635701,
    7056567727198538556457527417360012074120943099260330200195312500000000000000000000000000000000000000000000,
)
assert B_after == expected_B_after
assert B_after > B_before
assert B_after > F(6292579048245666,10**16)

print("P0257 reflection-symmetric five-point shape/scale exact certificate")
print("q =", centers[2][0])
print("t =", centers[1][1])
print("h =", h)
print("scale_s =", s)
print("min_C5_squared_gap =", min_cycle_gap)
print("u_squared_slack =", u*u-max_adj2)
print("G_squared_slack =", G*G-max_pair2)
print("min_quad_nonclosure_witness_margin =", min(m for m,_ in quad_witness_margin.values()))
print("R =", R)
print("block_area_A =", A)
print("A_lt_9_over_2 =", A < F(9,2))
print("cell_area_a =", a)
print("twoL_bonus_delta =", delta)
print("void_lower =", void_lower)
print("old_five_point_correction =", old_correction)
print("new_five_point_correction =", new_correction)
print("movement_exact =", movement)
print("B_before =", B_before)
print("B_after =", B_after)
print("B_after_gt_0.6292579048245666 =", B_after > F(6292579048245666,10**16))
print("ALL_EXACT_FINITE_CHECKS_PASS")
