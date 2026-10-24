from fractions import Fraction as F
from collections import Counter
from decimal import Decimal, getcontext

# R13 exact checker: a recursively balanced 86-leaf unsatisfiable tree with
# rational row magnitudes proving K_86^* >= 2.259253.
# All acceptance tests use exact integer/Fraction arithmetic.
# Decimal output is display-only.

N = 86
Q = F(2259253, 1000000)
ORBIT_WEIGHTS = [((0, 1), 4857310), ((2, 44), 3434640), ((3, 45), 2440010), ((4, 46), 1735453), ((5, 9, 47, 51), 1227150), ((6, 10, 48, 52), 876679), ((7, 11, 49, 53), 858684), ((8, 12, 50, 54), 598370), ((13, 55), 1715181), ((14, 56), 1222224), ((15, 57), 873158), ((16, 58), 855236), ((17, 59), 595968), ((18, 60), 1203336), ((19, 21, 61, 63), 850888), ((20, 22, 62, 64), 592938), ((23, 65), 2417246), ((24, 34, 66, 76), 1709252), ((25, 35, 67, 77), 1217998), ((26, 36, 68, 78), 870139), ((27, 37, 69, 79), 852278), ((28, 38, 70, 80), 593906), ((29, 39, 71, 81), 1199176), ((30, 32, 40, 42, 72, 74, 82, 84), 847945), ((31, 33, 41, 43, 73, 75, 83, 85), 590887)]

W = [None]*N
for orbit, value in ORBIT_WEIGHTS:
    assert value > 0
    for j in orbit:
        assert 0 <= j < N and W[j] is None
        W[j] = value
assert all(x is not None for x in W)

# Columns are indexed in preorder.  Column 0 is the dummy column from the
# CNF-to-NAE transformation.  Columns 1,...,85 are internal vertices of the
# balanced full binary tree: a node with s leaves splits floor(s/2), ceil(s/2).
# Its sign is + on the left subtree and - on the right subtree.
rows = []
subtree_size = {0:N}
next_col = 1

def build(size, path):
    global next_col
    if size == 1:
        rows.append([(0,+1)] + path)
        return
    a = size // 2
    b = size - a
    c = next_col
    next_col += 1
    subtree_size[c] = size
    build(a, path + [(c,+1)])
    build(b, path + [(c,-1)])

build(N, [])
assert len(rows) == N
assert next_col == N
assert set(subtree_size) == set(range(N))
depth_distribution = Counter(len(r)-1 for r in rows)
assert depth_distribution == Counter({6:42, 7:44})

# Exact projective partition / unsatisfiability certificate.
# Distinct leaves diverge at some internal vertex, so their templates contain
# a common non-dummy coordinate with opposite signs; their projective cylinders
# are disjoint.  A depth-d cylinder has projective mass 2^{-d}.  Kraft equality
# therefore proves that the 86 row cylinders partition all projective signings.
for i in range(N):
    si = dict(rows[i])
    assert si[0] == 1
    for j in range(i+1,N):
        sj = dict(rows[j])
        common = set(si).intersection(sj)
        assert any(c != 0 and si[c] == -sj[c] for c in common)

kraft = sum((F(1, 2**(len(r)-1)) for r in rows), F(0))
assert kraft == 1

# Rational magnitudes.  For a row with support S_i, set
#   |a_ij| = Q * (1/W_j) / sum_{k in S_i} (1/W_k).
# Thus every row has l1 mass Q exactly.  Its sign is the tree sign above.
column_sq = [F(0) for _ in range(N)]
row_l1 = []
for row in rows:
    inv = [F(1, W[j]) for j,_ in row]
    den = sum(inv, F(0))
    total = F(0)
    for (j,sgn), z in zip(row, inv):
        mag = Q * z / den
        assert mag > 0
        total += mag
        column_sq[j] += mag*mag
    row_l1.append(total)

assert all(x == Q for x in row_l1)
max_col = max(range(N), key=lambda j: column_sq[j])
max_load = column_sq[max_col]
assert max_load < 1
assert all(x <= 1 for x in column_sq)

# Compare exactly with Kunisky's published complete-tree obstruction at n=64:
# K(64) >= 1 + 7 sqrt(2)/8.  Since Q>1, square the positive difference term.
assert (Q-1)**2 > F(49,32)
# And with the preceding R13 six-column rational obstruction floor.
assert Q > F(23066933137,12500000000)

getcontext().prec = 50
def dec(x):
    return Decimal(x.numerator) / Decimal(x.denominator)

print("R13_BALANCED86_RATIONAL_LOAD_EXACT_PASS")
print("n_rows =", N)
print("n_columns =", N)
print("leaf_depth_distribution =", dict(sorted(depth_distribution.items())))
print("kraft_sum =", kraft)
print("row_l1_exact =", f"{Q.numerator}/{Q.denominator}")
print("row_l1_decimal =", dec(Q))
print("max_column_index =", max_col)
print("max_column_subtree_size =", subtree_size[max_col])
print("max_column_squared_norm =", dec(max_load))
print("min_squared_norm_slack =", dec(1-max_load))
known64 = Decimal(1) + Decimal(2).sqrt()*Decimal(7)/Decimal(8)
print("known_K64_zero_pad_lower =", known64)
print("new_minus_known_K64_zero_pad =", dec(Q)-known64)
print("orbit_count =", len(ORBIT_WEIGHTS))
print("orbit_weights =", ORBIT_WEIGHTS)
