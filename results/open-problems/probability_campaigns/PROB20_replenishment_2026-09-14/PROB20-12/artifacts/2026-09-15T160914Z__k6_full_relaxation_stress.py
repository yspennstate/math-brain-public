"""PROB20-12 numerical stress test of the current proved K6 relaxation.

Evidence only, NOT a proof of polyhedral equality.

Builds the rank-(2,2,2) colored-perfect-matching marginal polytope on six
vertices and the current relaxation consisting of:
  * 2880 single-fibre cover inequalities;
  * 20 aggregate K6 three-vertex blossoms;
  * 60 s=1 triangle threshold inequalities;
  * 45 DISTINCT s=2 four-set threshold inequalities;
  * color-sum and aggregate vertex-degree affine equations;
  * coordinate nonnegativity via bounds.

It then compares 1249 deterministic objective directions against exact
maximization over the 90 true deterministic vertices. SciPy/HiGHS is floating
point, so matching objective values are corroborative evidence only.
"""
import itertools
from collections import Counter
import numpy as np
from scipy.optimize import linprog

V = tuple(range(6))
EDGES = list(itertools.combinations(V, 2))
EID = {e: i for i, e in enumerate(EDGES)}


def ix(color, edge):
    return 15 * color + EID[tuple(sorted(edge))]


def perfect_matchings(vertices):
    vertices = tuple(sorted(vertices))
    if not vertices:
        yield []
        return
    a = vertices[0]
    for j in range(1, len(vertices)):
        b = vertices[j]
        rem = vertices[1:j] + vertices[j + 1 :]
        for rest in perfect_matchings(rem):
            yield [(a, b)] + rest


MATCHINGS = list(perfect_matchings(V))
assert len(MATCHINGS) == 15

TRUE_VERTICES = []
for matching in MATCHINGS:
    for perm in itertools.permutations(range(3)):
        row = np.zeros(45)
        for c, j in enumerate(perm):
            row[ix(c, matching[j])] = 1.0
        TRUE_VERTICES.append(row)
TRUE_VERTICES = np.asarray(TRUE_VERTICES)
assert TRUE_VERTICES.shape == (90, 45)

# Affine equations.
A_EQ = []
B_EQ = []
for c in range(3):
    row = np.zeros(45)
    for e in EDGES:
        row[ix(c, e)] = 1.0
    A_EQ.append(row)
    B_EQ.append(1.0)
for v in V:
    row = np.zeros(45)
    for c in range(3):
        for e in EDGES:
            if v in e:
                row[ix(c, e)] += 1.0
    A_EQ.append(row)
    B_EQ.append(1.0)
A_EQ = np.asarray(A_EQ)
B_EQ = np.asarray(B_EQ)

A_UB = []
B_UB = []
LABELS = []

# 2880 single-fibre cover inequalities.
for target_color in range(3):
    c0, c1 = [c for c in range(3) if c != target_color]
    for target_edge in EDGES:
        complement = tuple(v for v in V if v not in target_edge)
        bases = list(itertools.combinations(complement, 2))
        assert len(bases) == 6
        for mask in range(1 << 6):
            row = np.zeros(45)
            row[ix(target_color, target_edge)] = 1.0
            for j, edge0 in enumerate(bases):
                edge1 = tuple(sorted(set(complement) - set(edge0)))
                if (mask >> j) & 1:
                    row[ix(c0, edge0)] -= 1.0
                else:
                    row[ix(c1, edge1)] -= 1.0
            A_UB.append(row)
            B_UB.append(0.0)
            LABELS.append("fibre")

# 20 aggregate three-vertex blossom inequalities.
for triple in itertools.combinations(V, 3):
    S = set(triple)
    row = np.zeros(45)
    for c in range(3):
        for e in EDGES:
            if set(e) <= S:
                row[ix(c, e)] += 1.0
    A_UB.append(row)
    B_UB.append(1.0)
    LABELS.append("blossom")

# 60 distinct s=1 triangle threshold inequalities.
for target_color in range(3):
    other_colors = [c for c in range(3) if c != target_color]
    for triple in itertools.combinations(V, 3):
        A = set(triple)
        B = set(V) - A
        row = np.zeros(45)
        for e in EDGES:
            if set(e) <= A:
                row[ix(target_color, e)] += 1.0
            if set(e) <= B:
                for c in other_colors:
                    row[ix(c, e)] -= 1.0
        A_UB.append(row)
        B_UB.append(0.0)
        LABELS.append("s1")

# 45 DISTINCT s=2 inequalities. For complement edge B and singled color i:
# sum_{e subset A, c != i} x_{c,e} - x_{i,B} <= 1.
# Ordering the other two colors does not create a new inequality.
for complement_edge in EDGES:
    B = set(complement_edge)
    A = set(V) - B
    for singled_color in range(3):
        row = np.zeros(45)
        for c in range(3):
            if c != singled_color:
                for e in EDGES:
                    if set(e) <= A:
                        row[ix(c, e)] += 1.0
        row[ix(singled_color, complement_edge)] -= 1.0
        A_UB.append(row)
        B_UB.append(1.0)
        LABELS.append("s2")

A_UB = np.asarray(A_UB)
B_UB = np.asarray(B_UB)
counts = Counter(LABELS)
assert counts == Counter({"fibre": 2880, "blossom": 20, "s1": 60, "s2": 45})
assert A_UB.shape == (3005, 45)

# Deterministic objective suite: exactly 1249 directions.
rng = np.random.default_rng(20260915)
OBJECTIVES = []
for j in range(45):
    e = np.zeros(45)
    e[j] = 1.0
    OBJECTIVES.extend([e, -e])
for _ in range(159):
    obj = np.zeros(45)
    ids = rng.choice(45, size=int(rng.integers(2, 9)), replace=False)
    obj[ids] = rng.integers(-3, 4, size=len(ids))
    if not np.any(obj):
        obj[ids[0]] = 1.0
    OBJECTIVES.append(obj)
for _ in range(500):
    OBJECTIVES.append(rng.integers(-5, 6, size=45).astype(float))
for _ in range(500):
    OBJECTIVES.append(rng.normal(size=45))
assert len(OBJECTIVES) == 1249

max_gap = 0.0
num_large_gaps = 0
num_failures = 0
num_nonvertex_returned = 0
worst = None

for objective_id, obj in enumerate(OBJECTIVES):
    exact = float(np.max(TRUE_VERTICES @ obj))
    result = linprog(
        -obj,
        A_ub=A_UB,
        b_ub=B_UB,
        A_eq=A_EQ,
        b_eq=B_EQ,
        bounds=[(0.0, None)] * 45,
        method="highs",
    )
    if not result.success:
        num_failures += 1
        continue
    relaxed = -float(result.fun)
    gap = relaxed - exact
    if gap > max_gap:
        max_gap = gap
        worst = (objective_id, exact, relaxed)
    if gap > 1e-8:
        num_large_gaps += 1
    nearest = float(np.min(np.linalg.norm(TRUE_VERTICES - result.x, axis=1)))
    if nearest > 1e-7:
        num_nonvertex_returned += 1

print("constraint counts:", counts)
print("relaxation inequality rows:", A_UB.shape[0])
print("true deterministic vertices:", len(TRUE_VERTICES))
print("objectives tested:", len(OBJECTIVES))
print("solver failures:", num_failures)
print("gaps > 1e-8:", num_large_gaps)
print("maximum relaxation gap:", max_gap)
print("worst objective record:", worst)
print("returned optima farther than 1e-7 from all true vertices:", num_nonvertex_returned)
print("IMPORTANT: matching floating-point optima are numerical evidence only, not a proof.")
