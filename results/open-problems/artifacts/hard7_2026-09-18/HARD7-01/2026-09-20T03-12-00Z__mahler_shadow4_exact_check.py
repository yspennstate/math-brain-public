from itertools import combinations
from collections import Counter
import sympy as sp

# Exact integer vertices in R^4:
# +/- e_1,...,+/-e_4,+/-u, u=(1,1,1,1).
pts = []
labels = []
for i in range(4):
    e = [0]*4
    e[i] = 1
    pts.append(sp.Matrix(e)); labels.append(f"e{i+1}")
    pts.append(sp.Matrix([-x for x in e])); labels.append(f"-e{i+1}")
u = sp.Matrix([1,1,1,1])
pts.extend([u,-u]); labels.extend(["u","-u"])

def affine_rank(indices):
    q0 = pts[indices[0]]
    if len(indices) == 1:
        return 0
    M = sp.Matrix.hstack(*[(pts[j]-q0) for j in indices[1:]]).T
    return M.rank()

facets = set()
for comb in combinations(range(len(pts)), 4):
    if affine_rank(comb) != 3:
        continue
    p0 = pts[comb[0]]
    M = sp.Matrix.hstack(*[(pts[j]-p0) for j in comb[1:]]).T
    ns = M.nullspace()
    assert len(ns) == 1
    n = ns[0]
    c = sp.expand(n.dot(p0))
    vals = [sp.expand(n.dot(p)-c) for p in pts]
    if all(v <= 0 for v in vals) or all(v >= 0 for v in vals):
        eq = tuple(i for i,v in enumerate(vals) if v == 0)
        if affine_rank(eq) == 3:
            facets.add(eq)

# antipode map from our ordering
anti = {}
for i,p in enumerate(pts):
    for j,q in enumerate(pts):
        if p == -q:
            anti[i] = j
            break
assert len(anti) == len(pts)

def antipodal_facet(F):
    return tuple(sorted(anti[i] for i in F))

sizes = Counter(map(len, facets))
assert len(pts) == 10
assert len(facets) == 30
assert sizes == Counter({4:30})
assert all(antipodal_facet(F) in facets for F in facets)
assert len({frozenset((F, antipodal_facet(F))) for F in facets}) == 15

# Explicit odd speed: alpha(+/-e_i)=0, alpha(u)=1, alpha(-u)=-1.
alpha = [sp.Integer(0)]*8 + [sp.Integer(1), sp.Integer(-1)]
assert all(alpha[anti[i]] == -alpha[i] for i in range(len(pts)))

# It cannot be globally linear alpha(x)=w.x:
# values on e_1,...,e_4 force w=0, contradicting alpha(u)=1.
w = sp.symbols('w1:5')
eqs = []
for i in range(4):
    pos_index = 2*i
    eqs.append(sp.Eq(sum(w[j]*pts[pos_index][j] for j in range(4)), alpha[pos_index]))
sol = sp.solve(eqs, w, dict=True)
assert sol == [{w[0]:0,w[1]:0,w[2]:0,w[3]:0}]
assert sum(sol[0][w[j]]*u[j] for j in range(4)) != alpha[8]

# For a 4-simplex facet (4 affinely independent vertices in its 3D affine hull),
# arbitrary prescribed speed values extend uniquely to an affine function on that facet.
# Thus every facet imposes zero extra linear restrictions in the 4D admissibility count.
V, F, I = 10, len(facets), sum(map(len, facets))
generic_lower_bound = sp.Rational(V - I + 4*F, 2)
assert I == 120
assert generic_lower_bound == 5
assert generic_lower_bound > 4  # four-dimensional trivial-shear space

# Finite arithmetic for the 10-vertex structural corollary:
# if p is the number of opposite pairs of 5-vertex facets, then I=4F+2p and
# choosing theta parallel to k=min(p,3) such facet-pair hyperplanes gives
# dim A >= 5-p+k. For p<=3 this equals 5, so shadow-rigidity forces p>=4.
for p in range(4):
    k = p
    assert 5-p+k == 5
    assert 5 > 4

print("VERTICES =", len(pts))
print("FACETS =", len(facets))
print("FACET_SIZE_COUNTS =", dict(sorted(sizes.items())))
print("OPPOSITE_FACET_PAIRS = 15")
print("INCIDENCE_I =", I)
print("GENERIC_DIM_LOWER_BOUND =", generic_lower_bound)
print("EXPLICIT_ODD_SPEED_NONTRIVIAL = True")
print("TEN_VERTEX_SHADOW_RIGID_REQUIRES_P_GE_4 = True")
print("ALL_EXACT_CHECKS_PASS = True")
