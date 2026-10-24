"""PROB20-12 exact finite certificate for the s=2 threshold-cover facet.

Checks over exact integers/Fractions:
  * the true K6 colored-matching marginal polytope has affine dimension 37;
  * representative s=2 threshold inequality has 66 saturating deterministic
    vertices with equality-face affine dimension 36, hence is a facet;
  * an explicit rational point satisfies all single-fibre cuts, all aggregate
    K6 blossoms, and all s=1 triangle-cover facets, but violates the s=2
    facet by exactly 1/4.

The rational point is a polyhedral independence witness only; it is not claimed
to arise from an orthogonal decomposition.
"""

from fractions import Fraction
import itertools
import sympy as sp

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

VERTICES = []
for matching in MATCHINGS:
    for perm in itertools.permutations(range(3)):
        row = [0] * 45
        for c, j in enumerate(perm):
            row[ix(c, matching[j])] = 1
        VERTICES.append(row)
assert len(VERTICES) == 90

# Exact affine dimension of the true marginal polytope.
base = VERTICES[0]
full_rank = sp.Matrix(
    [[row[j] - base[j] for j in range(45)] for row in VERTICES[1:]]
).rank()
assert full_rank == 37

# Representative s=2, q=0 threshold facet:
# A={0,1,2,3}, B={4,5}, target color 2, other threshold color 1.
# sum_{e subset A} mu_2(e) + sum_{e subset A} mu_1(e) - mu_0(45) <= 1.
A4 = {0, 1, 2, 3}
B_EDGE = (4, 5)


def s2_variable_expression(row):
    value = -row[ix(0, B_EDGE)]
    for e in EDGES:
        if set(e) <= A4:
            value += row[ix(2, e)] + row[ix(1, e)]
    return value


s2_values = [s2_variable_expression(row) for row in VERTICES]
assert max(s2_values) == 1
s2_equal = [k for k, value in enumerate(s2_values) if value == 1]
assert len(s2_equal) == 66
s2_base = VERTICES[s2_equal[0]]
s2_face_rank = sp.Matrix(
    [
        [VERTICES[k][j] - s2_base[j] for j in range(45)]
        for k in s2_equal[1:]
    ]
).rank()
assert s2_face_rank == 36

# Rational independence witness, in units of 1/8.
VALUES = {}


def put(color, data):
    for edge, numerator in data.items():
        VALUES[(color, tuple(sorted(edge)))] = Fraction(numerator, 8)


put(
    0,
    {
        (0, 1): 2,
        (0, 4): 1,
        (0, 5): 1,
        (1, 4): 1,
        (1, 5): 1,
        (2, 5): 1,
        (3, 4): 1,
    },
)
put(
    1,
    {
        (0, 1): 1,
        (0, 2): 1,
        (1, 2): 1,
        (2, 3): 2,
        (2, 5): 1,
        (4, 5): 2,
    },
)
put(
    2,
    {
        (0, 1): 1,
        (0, 3): 1,
        (1, 3): 1,
        (2, 3): 2,
        (3, 4): 1,
        (4, 5): 2,
    },
)


def x(color, edge):
    return VALUES.get((color, tuple(sorted(edge))), Fraction(0))


# Affine constraints.
assert [sum(x(c, e) for e in EDGES) for c in range(3)] == [Fraction(1)] * 3
assert [
    sum(x(c, e) for c in range(3) for e in EDGES if v in e) for v in V
] == [Fraction(1)] * 6

# All 2880 single-fibre cover inequalities.
min_fibre_slack = None
fibre_count = 0
for target_color in range(3):
    other = [c for c in range(3) if c != target_color]
    c0, c1 = other
    for target_edge in EDGES:
        C = tuple(v for v in V if v not in target_edge)
        Bs = list(itertools.combinations(C, 2))
        for mask in range(1 << 6):
            rhs = Fraction(0)
            for j, edge0 in enumerate(Bs):
                edge1 = tuple(sorted(set(C) - set(edge0)))
                rhs += x(c0, edge0) if ((mask >> j) & 1) else x(c1, edge1)
            slack = rhs - x(target_color, target_edge)
            assert slack >= 0
            fibre_count += 1
            min_fibre_slack = slack if min_fibre_slack is None else min(min_fibre_slack, slack)
assert fibre_count == 2880
assert min_fibre_slack == 0

# Aggregate perfect-matching blossoms.
def y(edge):
    return sum(x(c, edge) for c in range(3))


aggregate_triangle_masses = []
for S_tuple in itertools.combinations(V, 3):
    S = set(S_tuple)
    mass = sum(y(e) for e in EDGES if set(e) <= S)
    assert mass <= 1
    aggregate_triangle_masses.append(mass)
assert max(aggregate_triangle_masses) == Fraction(3, 4)

# All 60 s=1 triangle-cover facets.
min_triangle_slack = None
triangle_count = 0
for target_color in range(3):
    other = [c for c in range(3) if c != target_color]
    for A_tuple in itertools.combinations(V, 3):
        A = set(A_tuple)
        B = set(V) - A
        lhs = sum(x(target_color, e) for e in EDGES if set(e) <= A)
        rhs = sum(x(c, e) for c in other for e in EDGES if set(e) <= B)
        slack = rhs - lhs
        assert slack >= 0
        triangle_count += 1
        min_triangle_slack = slack if min_triangle_slack is None else min(min_triangle_slack, slack)
assert triangle_count == 60
assert min_triangle_slack == 0

# Violate the representative s=2 facet by 1/4.
s2_expr_witness = -x(0, B_EDGE)
for e in EDGES:
    if set(e) <= A4:
        s2_expr_witness += x(2, e) + x(1, e)
assert s2_expr_witness == Fraction(5, 4)
assert s2_expr_witness - 1 == Fraction(1, 4)

print("full affine dimension:", full_rank)
print("s=2 facet saturating vertices:", len(s2_equal))
print("s=2 equality-face dimension:", s2_face_rank)
print("single-fibre inequalities checked:", fibre_count)
print("minimum single-fibre slack:", min_fibre_slack)
print("max aggregate blossom mass:", max(aggregate_triangle_masses))
print("s=1 triangle facets checked:", triangle_count)
print("minimum s=1 triangle slack:", min_triangle_slack)
print("s=2 witness expression:", s2_expr_witness)
print("s=2 exact violation:", s2_expr_witness - 1)
