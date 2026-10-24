from fractions import Fraction as F
from itertools import combinations, permutations, product
from decimal import Decimal, getcontext

getcontext().prec = 80


def dec(q):
    return Decimal(q.numerator) / Decimal(q.denominator)


def diff_abs_bounds(A, B):
    alo, ahi = A
    blo, bhi = B
    vals = [alo-blo, alo-bhi, ahi-blo, ahi-bhi]
    hi = max(abs(v) for v in vals)
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


def canonical(adj):
    return min(permuted_adj(adj, p) for p in permutations(range(len(adj))))


def count_strong_out2(n):
    all_pairs = [tuple(c) for c in combinations(range(n), 2)]
    allowed = {v: [c for c in all_pairs if v not in c] for v in range(n)}
    total = 0
    for rows in product(*(allowed[v] for v in range(n))):
        if strongly_connected(rows):
            total += 1
    return total


# Normalized positive-measure chart.  Each coordinate is a closed rational interval.
P = {
    0: ((F(0), F(0)), (F(0), F(0))),
    1: ((F(1), F(1)), (F(0), F(0))),
    2: ((F(3, 10), F(21, 50)), (F(-1, 10), F(1, 50))),
    3: ((F(-13, 50), F(-7, 50)), (F(-3, 20), F(-3, 100))),
    4: ((F(59, 100), F(71, 100)), (F(-13, 100), F(-1, 100))),
}

# Desired directed two-nearest-neighbor topology.
TARGET = ((2, 3), (2, 4), (0, 4), (0, 2), (1, 2))
C5 = ((1, 4), (0, 2), (1, 3), (2, 4), (0, 3))

D = {}
for i, j in combinations(range(5), 2):
    lo, hi = sq_dist_interval(P[i], P[j])
    D[i, j] = D[j, i] = (lo, hi)

rank_gaps = []
max_second_neighbor_sq = F(0)
for v in range(5):
    desired = set(TARGET[v])
    excluded = set(range(5)) - {v} - desired
    max_desired = max(D[v, u][1] for u in desired)
    min_excluded = min(D[v, u][0] for u in excluded)
    gap = min_excluded - max_desired
    assert gap > 0
    rank_gaps.append(gap)
    max_second_neighbor_sq = max(max_second_neighbor_sq, max_desired)

assert rank_gaps == [F(809, 5000), F(1, 2), F(3, 1000), F(26, 625), F(197, 1250)]
assert max_second_neighbor_sq == F(1, 2)
assert strongly_connected(TARGET)

AUTOMORPHISMS = [p for p in permutations(range(5)) if permuted_adj(TARGET, p) == TARGET]
assert AUTOMORPHISMS == [(0, 1, 2, 3, 4), (4, 3, 2, 1, 0)]
assert canonical(TARGET) == ((1, 2), (0, 2), (0, 3), (2, 4), (2, 3))
assert canonical(TARGET) != canonical(C5)

# Exact finite digraph enumeration: every row chooses two distinct other vertices.
strong_counts = tuple(count_strong_out2(n) for n in (3, 4, 5))
assert strong_counts == (1, 69, 5346)

# Geometric and guard constants.
V = F(3, 25) ** 6
U = F(71, 100)
H = F(21, 25)
assert U*U - max_second_neighbor_sq == F(41, 10000) > 0
assert H - U == F(13, 100) > 0

xmin, xmax = F(-13, 50), F(1)
ymin, ymax = F(-3, 20), F(1, 50)
w = xmax - xmin
h = ymax - ymin
assert (w, h) == (F(63, 50), F(17, 100))

# Rectangle parallel body: wh + 2H(w+h) + pi H^2.
# Use the classical rational upper bound pi < 22/7.
QBAR = w*h + 2*H*(w+h) + F(22, 7)*H*H
assert QBAR == F(24171, 5000)
SQRT_Q_UP = F(11, 5)
assert SQRT_Q_UP*SQRT_Q_UP - QBAR == F(29, 5000) > 0

# Ordered-tuple chart multiplicity is at most |Aut(TARGET)|=2.
# Campbell--Mecke / exact-binomial limit gives
#   Delta >= (2*pi/aut)*V*(H-U)*int_0^infty r^8 exp(-Q r^2) dr
# where the integral is 105*sqrt(pi)/(32 Q^(9/2)).
# Hence Delta = 105*pi^(3/2)/(16*aut)*V*(H-U)*Q^(-9/2).
# Lower-bound pi^(3/2) by 51/10: pi>3 and sqrt(pi)>17/10 because 3>(17/10)^2.
AUT = F(len(AUTOMORPHISMS))
PI32_LO = F(51, 10)
DELTA = F(105, 16) / AUT * PI32_LO * V * (H-U) / (QBAR**4 * SQRT_Q_UP)
assert DELTA == F(35802000, 6621983582864573)
assert DELTA > F(54, 10**10)

B_BEFORE = F(
    428290077362103688393910556289374260624427851669128955928061085239297514491295131572164454010069801964500982465126129692695841537835318496791550852459470618357,
    680627096921253366568966735604927531896699764460645393329189347179240150914086801287321056287307690561375724195312500000000000000000000000000000000000000000000,
)
B_AFTER = B_BEFORE + DELTA
assert B_AFTER == F(
    257829989578496350414183523146605335856248997408453788237962025484814476957683136019074638921462335179814079007196663994330380573638384791944133112730116386394080336881706051,
    409736496533210395577129470979508748365626015570562389564441613457911228367916571422161933413348402679750261900585439123098992187500000000000000000000000000000000000000000000,
)
assert B_AFTER > F(6292580518, 10**10)

print("TARGET =", TARGET)
print("CANONICAL =", canonical(TARGET))
print("AUTOMORPHISMS =", AUTOMORPHISMS)
print("RANK_GAPS =", rank_gaps)
print("MIN_RANK_GAP =", min(rank_gaps), dec(min(rank_gaps)))
print("MAX_SECOND_NEIGHBOR_SQ =", max_second_neighbor_sq, dec(max_second_neighbor_sq))
print("U2_SLACK =", U*U-max_second_neighbor_sq, dec(U*U-max_second_neighbor_sq))
print("CHART_VOLUME =", V, dec(V))
print("RECTANGLE =", (xmin, xmax, ymin, ymax))
print("QBAR =", QBAR, dec(QBAR))
print("SQRT_Q_UPPER_SLACK =", SQRT_Q_UP*SQRT_Q_UP-QBAR, dec(SQRT_Q_UP*SQRT_Q_UP-QBAR))
print("STRONG_OUT2_COUNTS_n3_n4_n5 =", strong_counts)
print("DELTA =", DELTA, dec(DELTA))
print("DELTA_GT_5_4E_9 =", DELTA > F(54, 10**10))
print("B_BEFORE =", B_BEFORE)
print("B_BEFORE_DEC =", dec(B_BEFORE))
print("B_AFTER =", B_AFTER)
print("B_AFTER_DEC =", dec(B_AFTER))
print("B_AFTER_GT_0_6292580518 =", B_AFTER > F(6292580518, 10**10))
print("ALL_EXACT_FINITE_CHECKS_PASS")
