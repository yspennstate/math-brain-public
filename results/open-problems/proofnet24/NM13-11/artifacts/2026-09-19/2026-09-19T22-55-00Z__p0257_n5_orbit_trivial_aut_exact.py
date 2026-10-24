from fractions import Fraction as F
from itertools import combinations, permutations, product
from decimal import Decimal, getcontext
from collections import Counter

getcontext().prec = 100

def dec(q):
    return Decimal(q.numerator) / Decimal(q.denominator)

def diff_abs_bounds(A, B):
    alo, ahi = A
    blo, bhi = B
    hi = max(abs(alo-blo), abs(alo-bhi), abs(ahi-blo), abs(ahi-bhi))
    if ahi < blo:
        lo = blo-ahi
    elif bhi < alo:
        lo = alo-bhi
    else:
        lo = F(0)
    return lo, hi

def sq_dist_interval(P, Q):
    lx, hx = diff_abs_bounds(P[0], Q[0])
    ly, hy = diff_abs_bounds(P[1], Q[1])
    return lx*lx + ly*ly, hx*hx + hy*hy

def strongly_connected(adj):
    n = len(adj)
    def reachable(start, reverse=False):
        seen = {start}
        stack = [start]
        while stack:
            v = stack.pop()
            if reverse:
                nbrs = [u for u in range(n) if v in adj[u]]
            else:
                nbrs = adj[v]
            for u in nbrs:
                if u not in seen:
                    seen.add(u)
                    stack.append(u)
        return len(seen) == n
    return reachable(0) and reachable(0, reverse=True)

def permuted_adj(adj, p):
    n = len(adj)
    out = [None] * n
    for old in range(n):
        new = p[old]
        out[new] = tuple(sorted(p[u] for u in adj[old]))
    return tuple(out)

PERMS5 = list(permutations(range(5)))

def canonical(adj):
    return min(permuted_adj(adj, p) for p in PERMS5)

def automorphisms(adj):
    return [p for p in PERMS5 if permuted_adj(adj, p) == adj]

# Exact finite orbit census: every loopless labelled 2-out digraph on five vertices.
allowed = {
    v: [tuple(c) for c in combinations(range(5), 2) if v not in c]
    for v in range(5)
}
strong_labelled = []
classes = {}
for rows in product(*(allowed[v] for v in range(5))):
    if strongly_connected(rows):
        strong_labelled.append(rows)
        c = canonical(rows)
        classes.setdefault(c, rows)

assert len(strong_labelled) == 5346
assert len(classes) == 53

aut_hist = Counter(len(automorphisms(rep)) for rep in classes.values())
assert aut_hist == Counter({1: 38, 2: 12, 4: 1, 5: 1, 10: 1})
assert sum(120 // len(automorphisms(rep)) for rep in classes.values()) == 5346

# New exact positive-measure Euclidean chart.
# p0=(0,0), p1=(1,0) after translation/rotation/scale normalization.
P = {
    0: ((F(0), F(0)), (F(0), F(0))),
    1: ((F(1), F(1)), (F(0), F(0))),
    2: ((F(53,100), F(63,100)), (F(21,125), F(53,250))),
    3: ((F(91,250), F(52,125)), (F(-13,60), F(-7,60))),
    4: ((F(89,100), F(93,100)), (F(-59,125), F(-56,125))),
}

TARGET = ((2,3), (2,4), (1,3), (0,2), (1,3))

# Previously charged size-5 canonical classes.
PREV_AUT2 = ((2,3), (2,4), (0,4), (0,2), (1,2))
PREV_C5 = ((1,4), (0,2), (1,3), (2,4), (0,3))

assert strongly_connected(TARGET)
AUT = automorphisms(TARGET)
assert AUT == [(0,1,2,3,4)]
assert len(AUT) == 1

TARGET_CANON = canonical(TARGET)
assert TARGET_CANON == ((1,2), (0,2), (0,3), (2,4), (0,3))
assert TARGET_CANON != canonical(PREV_AUT2)
assert TARGET_CANON != canonical(PREV_C5)

D = {}
for i, j in combinations(range(5), 2):
    lo, hi = sq_dist_interval(P[i], P[j])
    D[i,j] = D[j,i] = (lo, hi)

rank_gaps = []
max_second_neighbor_sq = F(0)
for v in range(5):
    desired = set(TARGET[v])
    excluded = set(range(5)) - {v} - desired
    max_desired = max(D[v,u][1] for u in desired)
    min_excluded = min(D[v,u][0] for u in excluded)
    gap = min_excluded - max_desired
    assert gap > 0
    rank_gaps.append(gap)
    max_second_neighbor_sq = max(max_second_neighbor_sq, max_desired)

assert rank_gaps == [
    F(6887,12500),
    F(49963,562500),
    F(541,12500),
    F(74,3125),
    F(493,1125000),
]
assert min(rank_gaps) == F(493,1125000)
assert max_second_neighbor_sq == F(100489,225000)

# Chart normalized 6-volume.
V = (
    (F(63,100)-F(53,100))
    * (F(53,250)-F(21,125))
    * (F(52,125)-F(91,250))
    * (F(-7,60)-F(-13,60))
    * (F(93,100)-F(89,100))
    * (F(-56,125)-F(-59,125))
)
assert V == F(429,19531250000)

# Internal r_2 bound and external guard.
U = F(669,1000)
H = F(407,500)
assert U*U - max_second_neighbor_sq == F(8489,9000000) > 0
assert H-U == F(29,200) > 0

# Bounding rectangle for every point in the chart: width 1, height 171/250.
xmin, xmax = F(0), F(1)
ymin, ymax = F(-59,125), F(53,250)
w = xmax-xmin
h = ymax-ymin
assert (w,h) == (F(1), F(171,250))

# H-parallel body of the rectangle covers the union of five guard disks.
# Q = wh + 2H(w+h) + pi H^2.  Use pi < 22/7.
QBAR = w*h + 2*H*(w+h) + F(22,7)*H*H
assert QBAR == F(4819497,875000)

SQRT_Q_UP = F(2347,1000)
assert SQRT_Q_UP*SQRT_Q_UP - QBAR == F(2887,7000000) > 0

# Source-valid five-point sink-SCC correction:
# Delta = 105*pi^(3/2)/(16*|Aut|) * V*(H-U)*Q^(-9/2).
# Rational lower bounds: pi^(3/2) > 51/10 and
# Q^(9/2) < QBAR^4 * SQRT_Q_UP.
PI32_LO = F(51,10)
DELTA = F(105,16) * PI32_LO * V * (H-U) / (QBAR**4 * SQRT_Q_UP)
assert DELTA == F(2314212291015625000,46898200879888981540448041041)
assert DELTA > F(493,10**13)

B_BEFORE = F(
257829989578496350414183523146605335856248997408453788237962025484814476957683136019074638921462335179814079007196663994330380573638384791944133112730116386394080336881706051,
409736496533210395577129470979508748365626015570562389564441613457911228367916571422161933413348402679750261900585439123098992187500000000000000000000000000000000000000000000
)
B_AFTER = B_BEFORE + DELTA
assert B_AFTER == F(
4030587548353407239385594764200229614297797658205062329180415991935634988507131251165427843820794999771597107722461131707733943325633277304301536835785477343473397459589419707534599554139802937648679697,
6405301507412145469471049291078200132062046565450533944155920254596661605498664430441568460794726368748340630284796689323210137382338787704649039451912789062500000000000000000000000000000000000000000000
)
assert B_AFTER > F(629258051894,10**12)

print("STRONG_LABELLED_N5 =", len(strong_labelled))
print("STRONG_ISOMORPHISM_CLASSES_N5 =", len(classes))
print("AUTOMORPHISM_HISTOGRAM =", dict(sorted(aut_hist.items())))
print("ORBIT_SIZE_SUM =", sum(120 // len(automorphisms(rep)) for rep in classes.values()))
print("TARGET =", TARGET)
print("TARGET_CANONICAL =", TARGET_CANON)
print("TARGET_AUTOMORPHISMS =", AUT)
print("RANK_GAPS =", rank_gaps)
print("MIN_RANK_GAP =", min(rank_gaps), dec(min(rank_gaps)))
print("MAX_SECOND_NEIGHBOR_SQ =", max_second_neighbor_sq, dec(max_second_neighbor_sq))
print("CHART_VOLUME =", V, dec(V))
print("U =", U, dec(U))
print("U2_SLACK =", U*U-max_second_neighbor_sq, dec(U*U-max_second_neighbor_sq))
print("H =", H, dec(H))
print("H_MINUS_U =", H-U, dec(H-U))
print("BBOX_W_H =", w, h)
print("QBAR =", QBAR, dec(QBAR))
print("SQRT_Q_UP =", SQRT_Q_UP, dec(SQRT_Q_UP))
print("SQRT_Q_SLACK =", SQRT_Q_UP*SQRT_Q_UP-QBAR, dec(SQRT_Q_UP*SQRT_Q_UP-QBAR))
print("DELTA =", DELTA, dec(DELTA))
print("B_BEFORE =", B_BEFORE, dec(B_BEFORE))
print("B_AFTER =", B_AFTER, dec(B_AFTER))
print("B_AFTER_GT_0.629258051894 =", B_AFTER > F(629258051894,10**12))
print("ALL_EXACT_FINITE_CHECKS_PASS")
