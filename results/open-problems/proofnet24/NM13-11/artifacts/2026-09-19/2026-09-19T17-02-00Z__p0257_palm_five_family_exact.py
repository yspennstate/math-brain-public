from fractions import Fraction as F
from itertools import combinations

# NM13-11 / P0257 exact checker for the positive-measure closed-4NN
# five-point Palm family. All load-bearing finite geometry and endpoint
# arithmetic below use Fraction only.

centers = [
    (F(0), F(0)),
    (F(1), F(0)),
    (F(139,100), F(-96,100)),
    (F(53,100), F(-160,100)),
    (F(-28,100), F(-96,100)),
]

# z_2,z_3,z_4 independently range over axis-aligned squares of halfwidth eps.
# z_0,z_1 are fixed by the similarity normalization.
eps = F(311,2500)
u = F(14211,10000)
G = F(19349,10000)

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

def coord_interval(i):
    x,y = centers[i]
    if i < 2:
        return x,x,y,y
    return x-eps, x+eps, y-eps, y+eps

def d2_bounds(i,j):
    xil,xih,yil,yih = coord_interval(i)
    xjl,xjh,yjl,yjh = coord_interval(j)
    dxlo,dxhi = xil-xjh, xih-xjl
    dylo,dyhi = yil-yjh, yih-yjl
    lo = sq_min_interval(dxlo,dxhi) + sq_min_interval(dylo,dyhi)
    hi = sq_max_interval(dxlo,dxhi) + sq_max_interval(dylo,dyhi)
    return lo,hi

# No collisions anywhere in the normalized shape box.
min_pair2 = min(d2_bounds(i,j)[0] for i,j in combinations(range(5),2))
assert min_pair2 > 0

# Robust C5 two-nearest-neighbor graph over the whole shape box.
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

assert min_cycle_gap == F(2541,6250000)
assert max_adj2 == F(3155317,1562500)
assert max_pair2 == F(23398093,6250000)
assert u*u - max_adj2 == F(12233,100000000)
assert G*G - max_pair2 == F(14313,100000000)

# No internal 3-subset can be a closed 2NN triple: the first two
# gadget neighbors are exactly the two C5 neighbors.
for S_tuple in combinations(range(5),3):
    S = set(S_tuple)
    assert not all(adj[v] <= S for v in S)

# No internal 4-subset can be a closed 3NN quadruple. For each omitted q,
# some included v sees q uniformly closer than some included w.
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
    quad_witness_margin[q] = (best,witness)

assert min(m for m,_ in quad_witness_margin.values()) == F(1753549,6250000)

# Six-dimensional normalized shape volume for z2,z3,z4.
V = (2*eps)**6
assert V == F(904820297013361,3814697265625000000)

# Analytic Palm lower bound proved in the report:
# Q=(9*pi/4)G^2 and
# Delta = (7*pi^(3/2)/256) V (G-u) Q^(-9/2)
#       = 14 V (G-u)/(3^9*pi^3*G^9).
# Archimedes pi < 22/7 therefore gives the rational certificate below.
pi_upper = F(22,7)
Delta = F(14) * V * (G-u) * (F(7,22)**3) / (F(3)**9 * G**9)
expected_Delta = F(
    73152390845020319331241164800000000,
    9958549111999599858289773721668371466642884877,
)
assert Delta == expected_Delta
assert Delta > 0

# Previous fixed-five-point term. The new broad Palm term replaces this
# term; it is NOT added on top of it.
old_five = F(
    617957324772210680294839810774947619464673905410513091139772637,
    87668429669475046757725067436695098876953125000000000000000000000000000000000,
)
assert Delta > old_five
movement = Delta - old_five
expected_movement = F(
    6407001273582750203255574667874285334231775934124407017116256881573849090387571570749820298931597341636454289351,
    873050362435350100599920653515826024844000104546950115203715972384088672697544097900390625000000000000000000000000000000000,
)
assert movement == expected_movement

B_before = F(
    4440401023269606295089343772266001019765040495180329193870131957751848714940547584423907813736824655635701,
    7056567727198538556457527417360012074120943099260330200195312500000000000000000000000000000000000000000000,
)
B_after = B_before + movement
expected_B_after = F(
    641377705174267468101274433764131457347844713295231130249870907152717283443310373029072200251405407093773621126563697479,
    1019260465779289339534879501998404060107472660571426304187235311834417648437500000000000000000000000000000000000000000000,
)
assert B_after == expected_B_after
assert B_after > B_before
assert B_after > F(6292579048319052,10**16)

print('P0257 positive-measure closed-4NN five-point Palm family exact certificate')
print('eps =', eps)
print('u =', u)
print('G =', G)
print('min_pair_squared_lower =', min_pair2)
print('min_C5_squared_gap =', min_cycle_gap)
print('u_squared_slack =', u*u-max_adj2)
print('G_squared_slack =', G*G-max_pair2)
print('min_quad_nonclosure_witness_margin =', min(m for m,_ in quad_witness_margin.values()))
print('normalized_shape_volume_V =', V)
print('pi_upper =', pi_upper)
print('old_five_point_correction =', old_five)
print('new_Palm_correction_lower =', Delta)
print('net_movement =', movement)
print('B_before =', B_before)
print('B_after =', B_after)
print('B_after_gt_0.6292579048319052 =', B_after > F(6292579048319052,10**16))
print('ALL_EXACT_FINITE_CHECKS_PASS')
