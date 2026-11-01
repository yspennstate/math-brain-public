"""PROB20-12 exact certificate for the new K6 triangle-cover facet.

All arithmetic used for the witness is rational. SymPy integer row reduction checks
the affine dimensions of the true colored-perfect-matching marginal polytope and
of the equality face of the triangle-cover inequality.

This is a finite combinatorial certificate. It does not assert that the rational
witness comes from an orthogonal decomposition.
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


# ---------------------------------------------------------------------------
# Part I. Exact facet check on the 90 deterministic colored perfect matchings.
# ---------------------------------------------------------------------------

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

base = VERTICES[0]
full_difference_matrix = sp.Matrix(
    [[VERTICES[k][j] - base[j] for j in range(45)] for k in range(1, 90)]
)
full_affine_dimension = full_difference_matrix.rank()
assert full_affine_dimension == 37

A = {0, 1, 2}
B = {3, 4, 5}


def triangle_functional(row):
    """LHS-RHS for

    mu_2(E(A)) <= mu_0(E(B)) + mu_1(E(B)).
    """
    value = 0
    for e in EDGES:
        es = set(e)
        if es <= A:
            value += row[ix(2, e)]
        if es <= B:
            value -= row[ix(0, e)] + row[ix(1, e)]
    return value


values = [triangle_functional(v) for v in VERTICES]
assert max(values) == 0

equality_indices = [k for k, value in enumerate(values) if value == 0]
assert len(equality_indices) == 72

eq_base = VERTICES[equality_indices[0]]
eq_difference_matrix = sp.Matrix(
    [
        [VERTICES[k][j] - eq_base[j] for j in range(45)]
        for k in equality_indices[1:]
    ]
)
equality_face_dimension = eq_difference_matrix.rank()
assert equality_face_dimension == 36

# Therefore the triangle-cover inequality is a facet: full dimension 37,
# equality-face dimension 36.

# ---------------------------------------------------------------------------
# Part II. Exact rational witness showing this facet is not implied by
#          affine constraints + all single-fibre cuts + aggregate K6 blossoms.
# Values are integer units divided by 40; unlisted coordinates are zero.
# ---------------------------------------------------------------------------

VALUES = {}


def put(color, data):
    for edge, numerator in data.items():
        VALUES[(color, tuple(sorted(edge)))] = Fraction(numerator, 40)


put(
    0,
    {
        (0, 1): 3,
        (0, 3): 5,
        (0, 4): 3,
        (0, 5): 8,
        (1, 3): 4,
        (1, 4): 2,
        (1, 5): 5,
        (2, 3): 2,
        (2, 4): 2,
        (2, 5): 3,
        (3, 5): 3,
    },
)

put(
    1,
    {
        (0, 3): 2,
        (0, 4): 3,
        (0, 5): 2,
        (1, 2): 3,
        (1, 3): 4,
        (1, 4): 5,
        (1, 5): 2,
        (2, 3): 5,
        (2, 4): 8,
        (2, 5): 3,
        (3, 4): 3,
    },
)

put(
    2,
    {
        (0, 1): 6,
        (0, 2): 6,
        (0, 5): 2,
        (1, 2): 6,
        (2, 4): 2,
        (3, 4): 6,
        (3, 5): 6,
        (4, 5): 6,
    },
)


def x(color, edge):
    return VALUES.get((color, tuple(sorted(edge))), Fraction(0))


# Color sums.
color_sums = [sum(x(c, e) for e in EDGES) for c in range(3)]
assert color_sums == [Fraction(1), Fraction(1), Fraction(1)]

# Aggregate degree equations.
vertex_sums = [
    sum(x(c, e) for c in range(3) for e in EDGES if v in e) for v in V
]
assert vertex_sums == [Fraction(1)] * 6

# All 2880 single-fibre inequalities from the earlier checkpoint.
minimum_fibre_slack = None
number_fibre_inequalities = 0
for target_color in range(3):
    other_colors = [c for c in range(3) if c != target_color]
    c0, c1 = other_colors
    for target_edge in EDGES:
        complement_vertices = tuple(v for v in V if v not in target_edge)
        Bs = list(itertools.combinations(complement_vertices, 2))
        assert len(Bs) == 6
        for mask in range(1 << 6):
            rhs = Fraction(0)
            for j, edge0 in enumerate(Bs):
                edge1 = tuple(sorted(set(complement_vertices) - set(edge0)))
                if (mask >> j) & 1:
                    rhs += x(c0, edge0)
                else:
                    rhs += x(c1, edge1)
            slack = rhs - x(target_color, target_edge)
            assert slack >= 0
            number_fibre_inequalities += 1
            if minimum_fibre_slack is None or slack < minimum_fibre_slack:
                minimum_fibre_slack = slack

assert number_fibre_inequalities == 2880
assert minimum_fibre_slack == 0

# Aggregate perfect-matching blossom inequalities.
def y(edge):
    return sum(x(c, edge) for c in range(3))


triangle_masses = {}
for S_tuple in itertools.combinations(V, 3):
    S = set(S_tuple)
    mass = sum(y(e) for e in EDGES if set(e) <= S)
    triangle_masses[S_tuple] = mass
    assert mass <= 1

assert max(triangle_masses.values()) == Fraction(7, 10)

# New triangle facet violation.
triangle_lhs = sum(x(2, e) for e in EDGES if set(e) <= A)
triangle_rhs = sum(x(c, e) for c in (0, 1) for e in EDGES if set(e) <= B)
triangle_violation = triangle_lhs - triangle_rhs

assert triangle_lhs == Fraction(9, 20)
assert triangle_rhs == Fraction(3, 20)
assert triangle_violation == Fraction(3, 10)

print("full affine dimension:", full_affine_dimension)
print("triangle equality-face dimension:", equality_face_dimension)
print("saturating deterministic vertices:", len(equality_indices))
print("single-fibre inequalities checked:", number_fibre_inequalities)
print("minimum single-fibre slack:", minimum_fibre_slack)
print("maximum aggregate K6 triangle mass:", max(triangle_masses.values()))
print("triangle facet lhs:", triangle_lhs)
print("triangle facet rhs:", triangle_rhs)
print("exact violation:", triangle_violation)
