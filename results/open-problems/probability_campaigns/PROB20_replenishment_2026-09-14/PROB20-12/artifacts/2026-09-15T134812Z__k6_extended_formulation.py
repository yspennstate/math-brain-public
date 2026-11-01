"""PROB20-12 exact K6 bookkeeping / certificate script.

This script uses only the Python standard library. It does NOT prove Lyons
Question 2.8. It exactly checks combinatorial facts used in the 2026-09-15
checkpoint:

- K6 has 15 uncolored perfect matchings;
- there are 90 colored perfect-matching states;
- their marginal polytope has affine dimension 37 (exact rational rank);
- the recovered artificial marginal point has a valid aggregate 1/2-1/2
  perfect-matching decomposition;
- the same point violates the recorded exact single-fibre separator by
  lhs=1/2, rhs=0;
- the p,z extended formulation has 15 p variables and 135 z variables.
"""
from itertools import combinations, permutations
from fractions import Fraction

V = tuple(range(6))
EDGES = tuple(combinations(V, 2))
EIDX = {e: i for i, e in enumerate(EDGES)}


def canon_edge(e):
    return tuple(sorted(e))


def perfect_matchings(vertices):
    vertices = tuple(sorted(vertices))
    if not vertices:
        yield ()
        return
    a = vertices[0]
    for b in vertices[1:]:
        e = (a, b)
        rest = tuple(v for v in vertices if v not in e)
        for tail in perfect_matchings(rest):
            yield tuple(sorted((canon_edge(e),) + tail))


MATCHINGS = tuple(sorted(set(perfect_matchings(V))))
assert len(MATCHINGS) == 15

# A colored state chooses one edge for each of colors 0,1,2, and those three
# edges form a perfect matching.
STATES = []
for M in MATCHINGS:
    for p in permutations(M):
        STATES.append(tuple(p))
assert len(STATES) == 90

# Colored marginal incidence matrix A: 45 coordinates x 90 states.
A = [[0 for _ in STATES] for __ in range(45)]
for s, st in enumerate(STATES):
    for color, e in enumerate(st):
        A[15 * color + EIDX[e]][s] = 1


def rank_rational(mat):
    """Exact Gaussian-elimination rank over Q."""
    a = [[Fraction(x) for x in row] for row in mat]
    m = len(a)
    n = len(a[0]) if m else 0
    r = 0
    for c in range(n):
        piv = next((i for i in range(r, m) if a[i][c]), None)
        if piv is None:
            continue
        a[r], a[piv] = a[piv], a[r]
        pv = a[r][c]
        a[r] = [x / pv for x in a[r]]
        for i in range(m):
            if i != r and a[i][c]:
                f = a[i][c]
                a[i] = [a[i][j] - f * a[r][j] for j in range(n)]
        r += 1
        if r == m:
            break
    return r


# Exact affine dimension of the convex hull of the 90 colored-state marginals.
v0 = [A[row][0] for row in range(45)]
diffs = []
for s in range(1, 90):
    diffs.append([A[row][s] - v0[row] for row in range(45)])
affine_dim = rank_rational(diffs)
assert affine_dim == 37, affine_dim

# Artificial marginal point from the recovered checkpoint.
mu = [[Fraction(0) for _ in EDGES] for __ in range(3)]


def setmu(c, e, x):
    mu[c][EIDX[canon_edge(e)]] = Fraction(x)


setmu(0, (0, 2), 1)
setmu(1, (1, 3), Fraction(1, 2))
setmu(1, (4, 5), Fraction(1, 2))
setmu(2, (1, 4), Fraction(1, 2))
setmu(2, (3, 5), Fraction(1, 2))

# Its aggregate y is exactly a 1/2-1/2 mixture of two uncolored perfect matchings.
M1 = tuple(sorted(((0, 2), (1, 3), (4, 5))))
M2 = tuple(sorted(((0, 2), (1, 4), (3, 5))))
assert M1 in MATCHINGS and M2 in MATCHINGS
for e in EDGES:
    y = sum(mu[c][EIDX[e]] for c in range(3))
    rhs = Fraction(1, 2) * (e in M1) + Fraction(1, 2) * (e in M2)
    assert y == rhs, (e, y, rhs)

# Exact single-fibre separator, target color-2 edge 14 and distinguished
# color-0 edge 02 in the complement {0,2,3,5}.
lhs = mu[2][EIDX[(1, 4)]]
rhs = (
    sum(mu[0][EIDX[e]] for e in [(0, 3), (0, 5), (2, 3), (2, 5), (3, 5)])
    + mu[1][EIDX[(3, 5)]]
)
assert lhs == Fraction(1, 2) and rhs == 0

# Extended p,z formulation dimensions.
# z_(M,i,e) exists for 15 matchings, 3 colors, and 3 edges of M.
z_index = {}
k = 0
for m, M in enumerate(MATCHINGS):
    for c in range(3):
        for e in M:
            z_index[(m, c, e)] = k
            k += 1
assert k == 135

print("K6 perfect matchings:", len(MATCHINGS))
print("Colored states:", len(STATES))
print("Colored marginal affine dimension:", affine_dim)
print("Extended formulation variables: p=15, z=135")
print("Artificial aggregate decomposition: 1/2*M1 + 1/2*M2 VERIFIED")
print("Artificial fibre separator: lhs=1/2, rhs=0 VERIFIED")
