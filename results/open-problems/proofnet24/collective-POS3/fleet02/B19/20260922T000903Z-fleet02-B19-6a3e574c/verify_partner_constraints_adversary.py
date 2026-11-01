from fractions import Fraction
from itertools import combinations

N = 15
CHAINS = {
    "A": [0, 1, 2, 3, 4],
    "B": [5, 6, 7, 8, 9],
    "C": [10, 11, 12, 13, 14],
}
COVERS = [
    (0,5),(1,2),(1,7),(2,3),(2,12),(3,4),(3,9),
    (5,1),(5,6),(5,11),(6,2),(6,7),(7,4),(7,8),
    (8,9),(9,14),(10,1),(10,11),(11,12),(12,8),
    (12,13),(13,4),(13,14),
]
COMMON_ORDER = [0,10,5,6,1,11,2,7,12,3,13,8,9,4,14]

chain_of = {x: k for k, vs in CHAINS.items() for x in vs}
index_in_chain = {x: i + 1 for k, vs in CHAINS.items() for i, x in enumerate(vs)}
chain_names = list(CHAINS)
pos = {x: i for i, x in enumerate(COMMON_ORDER)}

lt = [[False] * N for _ in range(N)]
for x, y in COVERS:
    lt[x][y] = True
for k in range(N):
    for i in range(N):
        if lt[i][k]:
            for j in range(N):
                if lt[k][j]:
                    lt[i][j] = True
assert not any(lt[i][i] for i in range(N))

for vs in CHAINS.values():
    for x, y in combinations(vs, 2):
        assert lt[x][y]
for x in range(N):
    for y in range(N):
        if lt[x][y]:
            assert pos[x] < pos[y]

antichain3 = next(
    t for t in combinations(range(N), 3)
    if all(not lt[x][y] and not lt[y][x] for x, y in combinations(t, 2))
)
# Fixed 3-chain cover gives width <= 3, and antichain3 gives width >= 3.
assert antichain3 == (1, 6, 11)

adj = {x: set() for x in range(N)}
for x, y in combinations(range(N), 2):
    if not lt[x][y] and not lt[y][x]:
        adj[x].add(y)
        adj[y].add(x)
seen = {0}
stack = [0]
while stack:
    x = stack.pop()
    for y in adj[x] - seen:
        seen.add(y)
        stack.append(y)
assert len(seen) == N

def prefix_set(state):
    out = set()
    for ci, name in enumerate(chain_names):
        out.update(CHAINS[name][:state[ci]])
    return out

states = set()
for a in range(6):
    for b in range(6):
        for c in range(6):
            state = (a, b, c)
            S = prefix_set(state)
            if all(not lt[x][y] or x in S for y in S for x in range(N)):
                states.add(state)
assert len(states) == 43

start = (0, 0, 0)
finish = (5, 5, 5)
A = {s: 0 for s in states}
A[start] = 1
for total in range(N):
    for s in sorted(states):
        if sum(s) != total or A[s] == 0:
            continue
        for ci in range(3):
            t = list(s)
            t[ci] += 1
            t = tuple(t)
            if t in states:
                A[t] += A[s]
E = A[finish]
assert E == 4477

B = {s: 0 for s in states}
B[finish] = 1
for total in range(N - 1, -1, -1):
    for s in sorted(states):
        if sum(s) != total:
            continue
        B[s] = 0
        for ci in range(3):
            t = list(s)
            t[ci] += 1
            t = tuple(t)
            if t in states:
                B[s] += B[t]
assert B[start] == E

def flux(x, other_chain):
    own_ci = chain_names.index(chain_of[x])
    other_ci = chain_names.index(other_chain)
    r = index_in_chain[x]
    out = [0] * (len(CHAINS[other_chain]) + 1)
    for s in states:
        if s[own_ci] != r - 1:
            continue
        t = list(s)
        t[own_ci] += 1
        t = tuple(t)
        if t in states:
            out[s[other_ci]] += A[s] * B[t]
    assert sum(out) == E
    return out

def f(q):
    return f"{q.numerator}/{q.denominator}" if q.denominator != 1 else str(q.numerator)

print("POS3_PARTNER_CONSTRAINTS_ADVERSARY")
print("N", N)
print("covers", COVERS)
print("chains", CHAINS)
print("width", 3, "antichain", antichain3)
print("incomparability_graph_connected", True)
print("ideal_states", len(states))
print("E", E)
labels = [chain_of[x] for x in COMMON_ORDER]
blocks = 1 + sum(labels[i] != labels[i - 1] for i in range(1, N))
assert blocks == 13
print("common_order", COMMON_ORDER)
print("common_order_chain_labels", "".join(labels))
print("common_order_blocks", blocks)

relevant = []
for x in range(N):
    for other in chain_names:
        if other == chain_of[x]:
            continue
        incomps = [y for y in CHAINS[other] if not lt[x][y] and not lt[y][x]]
        if not incomps:
            continue
        w = flux(x, other)
        gap = sum(pos[y] < pos[x] for y in CHAINS[other])
        peak = max(w)
        modes = [i for i, z in enumerate(w) if z == peak]
        assert modes == [gap]
        assert 3 * peak > E
        relevant.append((Fraction(peak, E), x, other, gap, w, peak))

minimum_heavy = min(relevant)
assert minimum_heavy[0] == Fraction(43, 121)
print("relevant_gap_marginals", len(relevant))
print("minimum_heavy_ratio", f(minimum_heavy[0]), "at", minimum_heavy[1], minimum_heavy[2])
for ratio, x, other, gap, w, peak in sorted(relevant, key=lambda z: (z[1], z[2])):
    print("MARGINAL", x, other, "gap", gap, "vector", w, "heavy", f(Fraction(peak, E)))

cells = []
for x in range(N):
    own = chain_of[x]
    own_ci = chain_names.index(own)
    coords = []
    for name in chain_names:
        if name == own:
            coords.append(index_in_chain[x] - 1)
        else:
            coords.append(sum(pos[y] < pos[x] for y in CHAINS[name]))
    s = tuple(coords)
    t = list(s)
    t[own_ci] += 1
    t = tuple(t)
    assert s in states and t in states
    value = A[s] * B[t]
    assert value * 19683 >= E
    cells.append((Fraction(value, E), x, s, value))

minimum_cell = min(cells)
assert minimum_cell[0] == Fraction(855, 4477)
print("minimum_central_cell_ratio", f(minimum_cell[0]), "at", minimum_cell[1], minimum_cell[2])
for ratio, x, s, value in sorted(cells, key=lambda z: z[1]):
    print("CENTRAL", x, "state", s, "mass", value, "ratio", f(ratio))

pairs = []
for x, y in combinations(range(N), 2):
    if lt[x][y] or lt[y][x]:
        continue
    w = flux(x, chain_of[y])
    numerator = sum(w[:index_in_chain[y]])
    p = Fraction(numerator, E)
    balanced = Fraction(1, 3) <= p <= Fraction(2, 3)
    pairs.append((x, y, p, balanced))
assert len(pairs) == 21
balanced_pairs = [(x, y, p) for x, y, p, balanced in pairs if balanced]
assert len(balanced_pairs) == 7
assert balanced_pairs == [
    (1,6,Fraction(1977,4477)),
    (2,11,Fraction(1526,4477)),
    (3,12,Fraction(1549,4477)),
    (4,9,Fraction(1569,4477)),
    (5,10,Fraction(1841,4477)),
    (7,12,Fraction(249,407)),
    (8,13,Fraction(2155,4477)),
]
print("incomparable_pairs", len(pairs))
print("balanced_pairs", len(balanced_pairs))
for x, y, p, balanced in pairs:
    print("PAIR", x, y, "p", f(p), "balance", f(min(p, 1-p)), "BAL" if balanced else "OUT")

oriented = []
for x, y, p, balanced in pairs:
    if balanced:
        continue
    p_order = p if pos[x] < pos[y] else 1 - p
    assert p_order > Fraction(2, 3)
    oriented.append((p_order, x, y))
minimum_oriented = min(oriented)
assert minimum_oriented[0] == Fraction(3023, 4477)
print("unbalanced_pairs_common_order_strong_majority_compatible", len(oriented))
print("minimum_oriented_probability", f(minimum_oriented[0]), "pair", minimum_oriented[1], minimum_oriented[2])
print("interpretation", "all fleet03/B10 heavy-marginal and pinned-central-atom constraints hold, with a common majority-compatible completion and 13 blocks, yet seven balanced pairs remain")
print("POS3_PARTNER_CONSTRAINTS_ADVERSARY_PASS")
