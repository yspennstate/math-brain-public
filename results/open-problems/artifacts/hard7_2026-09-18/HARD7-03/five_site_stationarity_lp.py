from fractions import Fraction
from itertools import product

# Five-site local-stationarity relaxation for homogeneous totally asymmetric K=2 exclusion.
# Variables p[w], w in {0,1,2}^5, are candidate 5-block probabilities.
# Constraints:
#   (i) normalization,
#   (ii) shift consistency of 4-block marginals,
#   (iii) stationarity E[L 1{middle 3-block=u}]=0 for all u in {0,1,2}^3.
# Objective q(w)=1{w_2>0,w_3<2}, the unit-rate eligibility/current at the central bond.

alphabet = range(3)
words = list(product(alphabet, repeat=5))
idx = {w: i for i, w in enumerate(words)}
rows = []
rhs = []
row_names = []

# Normalization.
rows.append([1] * len(words))
rhs.append(1)
row_names.append("normalization")

# Shift consistency.
for u in product(alphabet, repeat=4):
    row = [0] * len(words)
    for a in alphabet:
        row[idx[(a,) + u]] += 1
    for z in alphabet:
        row[idx[u + (z,)]] -= 1
    rows.append(row)
    rhs.append(0)
    row_names.append("shift:" + "".join(map(str, u)))

# Generator stationarity for middle three-site cylinder indicators.
for u in product(alphabet, repeat=3):
    row = [0] * len(words)
    for w in words:
        old = w[1:4]
        coeff = 0
        for x in range(4):
            if w[x] > 0 and w[x + 1] < 2:
                ww = list(w)
                ww[x] -= 1
                ww[x + 1] += 1
                new = tuple(ww[1:4])
                coeff += int(new == u) - int(old == u)
        row[idx[w]] = coeff
    rows.append(row)
    rhs.append(0)
    row_names.append("stationarity:" + "".join(map(str, u)))

assert len(rows) == 109
assert all(len(r) == 243 for r in rows)

q = [int(w[2] > 0 and w[3] < 2) for w in words]

# Exact dual certificate y for min b^T y subject A^T y >= q.
# The order is normalization; lexicographic 4-block shift rows; lexicographic
# 3-block generator-stationarity rows.
pairs = [
(24,47),(2688,3055),(3078,3055),(2688,3055),(-16,235),(-16,235),
(1518,3055),(1149,3055),(889,3055),(24,65),(3487,3055),(3747,3055),
(3487,3055),(1632,3055),(1502,3055),(1834,3055),(556,3055),(556,3055),
(-42,3055),(5752,3055),(5752,3055),(5752,3055),(0,1),(0,1),
(2447,3055),(0,1),(0,1),(-432,3055),(0,1),(0,1),(0,1),(0,1),(0,1),
(556,3055),(0,1),(0,1),(-151,3055),(0,1),(0,1),(0,1),(0,1),(0,1),
(722,3055),(0,1),(0,1),(-16,235),(5752,3055),(5752,3055),(5752,3055),
(0,1),(0,1),(2187,3055),(0,1),(0,1),(-432,3055),(0,1),(0,1),(0,1),
(0,1),(0,1),(556,3055),(0,1),(0,1),(1409,3055),(0,1),(0,1),(0,1),
(0,1),(0,1),(917,3055),(0,1),(0,1),(-16,235),(5752,3055),(5752,3055),
(5752,3055),(0,1),(0,1),(1992,3055),(0,1),(0,1),(-432,3055),
(393,611),(239,3055),(0,1),(99,3055),(-1208,3055),(-122,611),
(380,611),(-547,3055),(-23,611),(-2283,3055),(-2839,3055),
(-2688,3055),(-2033,3055),(-551,611),(-1572,3055),(751,3055),
(-1436,3055),(166,3055),(-1245,611),(-6586,3055),(-95,47),
(-733,611),(-4257,3055),(-2489,3055),(0,1),(-1992,3055),(0,1)
]
assert len(pairs) == len(rows)
y = [Fraction(a,b) for a,b in pairs]

dual_slacks = []
for j,w in enumerate(words):
    lhs = sum(Fraction(rows[i][j]) * y[i] for i in range(len(rows)))
    dual_slacks.append(lhs - q[j])
assert all(s >= 0 for s in dual_slacks)
dual_obj = sum(Fraction(rhs[i]) * y[i] for i in range(len(rows)))
assert dual_obj == Fraction(24,47)

# Sparse exact primal witness showing the relaxation optimum is exactly 24/47.
# All omitted words have probability zero.
primal_weights = {
    (0,0,2,2,0): 3,
    (0,1,1,2,0): 3,
    (0,1,2,1,1): 2,
    (0,2,0,1,1): 2,
    (0,2,1,0,1): 2,
    (0,2,2,0,0): 3,
    (1,0,1,2,1): 2,
    (1,0,2,1,0): 2,
    (1,1,0,2,1): 2,
    (1,1,1,1,1): 3,
    (1,1,2,0,1): 1,
    (1,1,2,0,2): 2,
    (1,2,0,1,1): 1,
    (1,2,0,2,0): 2,
    (1,2,1,1,0): 2,
    (2,0,0,2,2): 3,
    (2,0,1,1,2): 3,
    (2,0,2,0,1): 2,
    (2,1,0,1,2): 2,
    (2,1,1,0,2): 2,
    (2,2,0,0,2): 3,
}
p = [Fraction(primal_weights.get(w,0),47) for w in words]
assert sum(p) == 1
for i,row in enumerate(rows):
    assert sum(Fraction(row[j]) * p[j] for j in range(len(words))) == rhs[i]
primal_obj = sum(Fraction(q[j]) * p[j] for j in range(len(words)))
assert primal_obj == Fraction(24,47)

print("HARD7-03 exact five-site local-stationarity LP certificate")
print("variables=243")
print("equalities=109")
print("primal_support=21")
print(f"primal_objective={primal_obj}")
print(f"dual_objective={dual_obj}")
print(f"dual_min_slack={min(dual_slacks)}")
print(f"dual_tight_columns={sum(s == 0 for s in dual_slacks)}/243")
print("LP_OPTIMUM=24/47")
print("HOMOGENEOUS_UNIT_RATE_TI_STATIONARY_CURRENT<=24/47")
print("SLOW_RATE_c=1/2_LIMITING_BULK_CURRENT<=12/47")
print("ALL_EXACT_CHECKS_PASS")
