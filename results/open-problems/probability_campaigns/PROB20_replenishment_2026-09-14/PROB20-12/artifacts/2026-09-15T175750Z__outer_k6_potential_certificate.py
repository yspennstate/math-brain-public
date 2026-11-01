"""Exact certificate for the K6 duad-syntheme / pentad potential reduction.

This script uses only itertools and SymPy exact arithmetic.  It verifies:
  * the 15x15 edge/perfect-matching incidence matrix has rank 10;
  * K6 has exactly six 1-factorizations ('pentads') and every perfect matching
    belongs to exactly two;
  * the 15 perfect matchings therefore identify with the 15 edges of an
    outer K6 on the six pentads;
  * each original K6 edge corresponds to a perfect matching of the outer K6;
  * p*_M = (1/4) sum_{e in M} y_e - 1/12 solves A p*=y whenever all original
    vertex degrees of y equal one;
  * every zero-marginal skeleton move is an outer vertex potential
    delta_ab = alpha_a+alpha_b with sum alpha=0;
  * differences of pentad-incidence vectors form another exact kernel basis;
  * the ten outer two-triangle half-matchings correspond exactly to the ten
    complementary original 3-set blossom slacks.

No floating-point arithmetic is used.
"""

import itertools
import sympy as sp

V = tuple(range(6))
EDGES = list(itertools.combinations(V, 2))
EID = {e: i for i, e in enumerate(EDGES)}


def gen_matchings(vertices):
    vertices = tuple(vertices)
    if not vertices:
        yield ()
        return
    a = vertices[0]
    for j in range(1, len(vertices)):
        b = vertices[j]
        rem = vertices[1:j] + vertices[j + 1 :]
        for rest in gen_matchings(rem):
            yield tuple(sorted(((a, b),) + rest))


MATCHINGS = sorted(set(gen_matchings(V)))
assert len(MATCHINGS) == 15

# A[e,M]=1 iff original edge e belongs to original perfect matching M.
A = sp.zeros(15, 15)
for j, M in enumerate(MATCHINGS):
    for e in M:
        A[EID[e], j] = 1
assert A.rank() == 10
print("rank(A)=", A.rank())

# Enumerate all K6 1-factorizations: five perfect matchings covering each edge once.
PENTADS = []
ones = sp.ones(15, 1)
for comb in itertools.combinations(range(15), 5):
    h = sp.Matrix([1 if j in comb else 0 for j in range(15)])
    if A * h == ones:
        PENTADS.append(comb)
assert len(PENTADS) == 6
print("six pentads (matching indices):")
for a, P in enumerate(PENTADS):
    print(a, P)

# Each perfect matching lies in exactly two pentads, giving an outer K6 edge.
assert [sum(j in P for P in PENTADS) for j in range(15)] == [2] * 15
OUTER_PAIR = {}
for j in range(15):
    pair = tuple(a for a, P in enumerate(PENTADS) if j in P)
    assert len(pair) == 2
    OUTER_PAIR[j] = pair
assert len(set(OUTER_PAIR.values())) == 15
print("matching -> outer-edge pair:")
for j, pair in OUTER_PAIR.items():
    print(j, MATCHINGS[j], "->", pair)

# Each original edge belongs to three original perfect matchings; their outer
# pairs must partition the six pentad vertices, i.e. form an outer perfect matching.
OUTER_PM = {}
for e in EDGES:
    js = [j for j, M in enumerate(MATCHINGS) if e in M]
    assert len(js) == 3
    pairs = tuple(sorted(OUTER_PAIR[j] for j in js))
    assert sorted(v for pair in pairs for v in pair) == list(range(6))
    OUTER_PM[e] = pairs
print("original edge -> outer perfect matching:")
for e, F in OUTER_PM.items():
    print(e, "->", F)

# Symbolic aggregate edge variables, constrained only by degree_y(v)=1.
y = sp.symbols("y0:15")
deg_eq = [sum(y[EID[e]] for e in EDGES if v in e) - 1 for v in V]
# The first six variables happen to form a nonsingular choice for solving the six
# independent affine degree equations in the ordering used above.
sol_list = sp.solve(deg_eq, y[:6], dict=True)
assert len(sol_list) == 1
DEG_SUB = sol_list[0]

# Canonical real skeleton solution.
pstar = []
for M in MATCHINGS:
    pstar.append(
        sp.Rational(1, 4) * sum(y[EID[e]] for e in M)
        - sp.Rational(1, 12)
    )

residual = A * sp.Matrix(pstar) - sp.Matrix(y)
assert all(sp.simplify(expr.subs(DEG_SUB)) == 0 for expr in residual)
assert sp.simplify((sum(pstar) - 1).subs(DEG_SUB)) == 0
print("canonical p* identity A p*=y and sum p*=1 verified exactly")

# Outer incidence B[j,a]=1 iff outer edge corresponding to original matching j
# touches pentad vertex a.  Potentials alpha with sum alpha=0 are represented by
# columns e_a-e_5, a=0,...,4.
B = sp.zeros(15, 6)
for j, pair in OUTER_PAIR.items():
    for a in pair:
        B[j, a] = 1
K = sp.Matrix.hstack(*[B[:, a] - B[:, 5] for a in range(5)])
assert K.rank() == 5
assert A * K == sp.zeros(15, 5)
assert 15 - A.rank() == 5
print("outer-potential kernel basis has exact rank 5 and spans ker(A)")

# Pentad differences are another exact kernel basis.
H = sp.zeros(15, 6)
for a, P in enumerate(PENTADS):
    for j in P:
        H[j, a] = 1
for a in range(6):
    assert A * H[:, a] == sp.ones(15, 1)
D = sp.Matrix.hstack(*[H[:, a] - H[:, 0] for a in range(1, 6)])
assert D.rank() == 5
# An explicit nonzero 5x5 minor is useful as a small certificate.
minor_rows = (0, 1, 3, 4, 7)
minor_det = D[list(minor_rows), :].det()
assert minor_det == 2
print("pentad-difference kernel basis rank 5; minor rows", minor_rows, "det=", minor_det)

# Map all ten complementary outer triangle pairs to the ten original 3|3 blossom
# slacks.  We verify exact equality modulo only the six degree equations.
seen_outer = set()
triangle_map = []
for T0 in itertools.combinations(range(6), 3):
    T1 = tuple(sorted(set(range(6)) - set(T0)))
    T = min(tuple(T0), T1)
    if T in seen_outer:
        continue
    seen_outer.add(T)

    internal_outer_matchings = [
        j
        for j, pair in OUTER_PAIR.items()
        if set(pair) <= set(T) or set(pair) <= set(set(range(6)) - set(T))
    ]
    lhs = sp.Rational(1, 2) * sum(pstar[j] for j in internal_outer_matchings)

    found = []
    seen_original = set()
    for S0 in itertools.combinations(range(6), 3):
        S1 = tuple(sorted(set(range(6)) - set(S0)))
        S = min(tuple(S0), S1)
        if S in seen_original:
            continue
        seen_original.add(S)
        blossom_half_slack = sp.Rational(1, 2) * (
            1 - sum(y[EID[e]] for e in EDGES if set(e) <= set(S))
        )
        diff = sp.simplify((lhs - blossom_half_slack).subs(DEG_SUB))
        if diff == 0:
            found.append(S)

    assert len(found) == 1
    triangle_map.append((T, found[0]))

assert len(triangle_map) == 10
print("outer two-triangle pair -> original 3|3 blossom cut:")
for item in triangle_map:
    print(item)

print("ALL EXACT CHECKS PASSED")
