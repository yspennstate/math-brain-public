from itertools import combinations
import sympy as sp

# Exact checker for the R7-02 one-chord continuation of P0072.
# Graph: the m=k=2 double-series losange, with one added chord x-y.
# Vertices: s-x-a-y-t, plus b, with geodesic s-b-t.

p = sp.symbols("p0:7", nonnegative=True)
P0, P1, P2, P3, R, P5, P6 = p
names = ["sx", "xa", "ay", "yt", "xy", "sb", "bt", "ab"]
edges = [
    ("s", "x", "sx"), ("x", "a", "xa"), ("a", "y", "ay"),
    ("y", "t", "yt"), ("x", "y", "xy"), ("s", "b", "sb"),
    ("b", "t", "bt"), ("a", "b", "ab"),
]
path_sets = [
    frozenset(["sx", "xa", "ay", "yt"]),
    frozenset(["sx", "xa", "ab", "bt"]),
    frozenset(["sx", "xy", "ay", "ab", "bt"]),
    frozenset(["sx", "xy", "yt"]),
    frozenset(["sb", "bt"]),
    frozenset(["sb", "ab", "xa", "xy", "yt"]),
    frozenset(["sb", "ab", "ay", "yt"]),
]
inc = [[int(name in path_sets[j]) for name in names] for j in range(7)]
w = [sp.Integer(1) + sum(p[j] * inc[j][i] for j in range(7)) for i in range(8)]

# B11: exact dual path-cost certificate.
sentinel = {"sx": sp.Rational(1, 2), "yt": sp.Rational(1, 2), "ab": sp.Rational(1, 2)}
costs = [sum(sentinel.get(name, 0) for name in path_sets[j]) for j in range(7)]
assert costs == [1, 1, 1, 1, 0, 1, 1]

verts = ["s", "x", "a", "y", "t", "b"]

def is_tree(idxs):
    parent = {v: v for v in verts}
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        parent[rb] = ra
        return True
    for i in idxs:
        if not union(edges[i][0], edges[i][1]):
            return False
    return len({find(v) for v in verts}) == 1


def st_path_set(idxs):
    adj = {v: [] for v in verts}
    for i in idxs:
        u, v, nm = edges[i]
        adj[u].append((v, nm))
        adj[v].append((u, nm))
    stack = [("s", None, ())]
    seen = set()
    while stack:
        v, parent, used = stack.pop()
        if v == "t":
            return frozenset(used)
        seen.add(v)
        for z, nm in adj[v]:
            if z != parent and z not in seen:
                stack.append((z, v, used + (nm,)))
    raise RuntimeError("tree has no s-t path")

Z = sp.Integer(0)
N = [sp.Integer(0) for _ in range(7)]
tree_count = 0
for idxs in combinations(range(8), 5):
    if not is_tree(idxs):
        continue
    tree_count += 1
    term = sp.prod(w[i] for i in idxs)
    Z += term
    ps = st_path_set(idxs)
    j = path_sets.index(ps)
    N[j] += term
assert tree_count == 35
assert sp.expand(sum(N) - Z) == 0
Z = sp.expand(Z)
NR = sp.expand(N[4])
n = sum(p)
t = n + sp.Rational(3, 2)

# B16: exact drift certificate q_R > (R+1/2)/(n+3/2).
Dhalf = sp.Poly(sp.expand(t * NR - (R + sp.Rational(1, 2)) * Z), *p)
assert all(c > 0 for c in Dhalf.coeffs())
assert len(Dhalf.terms()) == 1397
assert min(Dhalf.coeffs()) == 2

# Every macroscopic support containing R and at least one bad path has a
# positive top-degree drift.  This is the finite face certificate used to
# exclude an interior limiting geodesic frequency.
PZ = sp.Poly(Z, *p)

def face_lead(poly, active):
    active = set(active)
    best = -1
    out = []
    for mon, c in poly.terms():
        supp = {i for i, e in enumerate(mon) if e}
        if not supp <= active:
            continue
        deg = sum(mon)
        if deg > best:
            best = deg
            out = [(mon, c)]
        elif deg == best:
            out.append((mon, c))
    return best, out

faces = 0
min_face_coeff = None
for k in range(2, 8):
    for active in combinations(range(7), k):
        if 4 not in active:
            continue
        dd, dterms = face_lead(Dhalf, active)
        dz, zterms = face_lead(PZ, active)
        assert dd == dz + 1
        assert all(c > 0 for _, c in dterms)
        faces += 1
        m = min(c for _, c in dterms)
        min_face_coeff = m if min_face_coeff is None else min(min_face_coeff, m)
assert faces == 63
assert min_face_coeff == 2

# B24: one-sided blown-up bad face.  p0..p3 are macroscopic; R,p5,p6
# are lower scale.  The leading ratio is 2(R+p5+p6+1)N/D.
T = sp.symbols("T", positive=True)
a0, a1, a2, a3 = sp.symbols("a0 a1 a2 a3", nonnegative=True)
rr, v5, v6 = sp.symbols("rr v5 v6", nonnegative=True)
subs_one = {P0: a0*T, P1: a1*T, P2: a2*T, P3: a3*T, R: rr, P5: v5, P6: v6}
ZO = sp.Poly(sp.expand(Z.subs(subs_one)), T)
NO = sp.Poly(sp.expand(NR.subs(subs_one)), T)
assert ZO.degree() == 5 and NO.degree() == 4
z5 = sp.factor(ZO.coeff_monomial(T**5))
n4 = sp.factor(NO.coeff_monomial(T**4))
Nq = (2*a0**2 + 3*a0*a1 + 5*a0*a2 + 3*a0*a3 + 3*a1*a2 +
      3*a1*a3 + 2*a2**2 + 3*a2*a3)
Dq = (2*a0**3 + 4*a0**2*a1 + 8*a0**2*a2 + 6*a0**2*a3 +
      2*a0*a1**2 + 10*a0*a1*a2 + 8*a0*a1*a3 + 6*a0*a2**2 +
      12*a0*a2*a3 + 4*a0*a3**2 + 2*a1**2*a2 + 2*a1**2*a3 +
      3*a1*a2**2 + 8*a1*a2*a3 + 3*a1*a3**2 + a2**3 +
      4*a2**2*a3 + 3*a2*a3**2)
assert sp.factor(n4/z5 - 2*(rr + v5 + v6 + 1)*Nq/Dq) == 0
S = a0 + a1 + a2 + a3
pos = sp.Poly(sp.expand(4*Nq*S - 3*Dq), a0, a1, a2, a3)
assert len(pos.terms()) == 17
assert all(c > 0 for c in pos.coeffs())
assert min(pos.coeffs()) == 2

# Intersection blown-up face: only p0,p3 are macroscopic.  All other
# bad side routes and R are lower scale.  The factorized leading ratio
# is the formula used in the proof to obtain the same 3/2 invasion floor.
u1, u2 = sp.symbols("u1 u2", nonnegative=True)
subs_int = {P0: a0*T, P3: a3*T, P1: u1, P2: u2, R: rr, P5: v5, P6: v6}
ZI = sp.Poly(sp.expand(Z.subs(subs_int)), T)
NI = sp.Poly(sp.expand(NR.subs(subs_int)), T)
assert ZI.degree() == 4 and NI.degree() == 3
z4 = sp.factor(ZI.coeff_monomial(T**4))
n3 = sp.factor(NI.coeff_monomial(T**3))
target = 2*(2*a0 + 3*a3)*(rr + u1 + u2 + 1)*(rr + v5 + v6 + 1) / (
    (a0 + a3)*(a0 + 2*a3)*(2*rr + 2*u1 + 2*u2 + 2*v5 + 2*v6 + 3)
)
assert sp.factor(n3/z4 - target) == 0

print("TREE_COUNT", tree_count)
print("PATH_COSTS", costs)
print("DRIFT_CERT_TERMS", len(Dhalf.terms()), "MIN_COEFF", min(Dhalf.coeffs()), "MAX_COEFF", max(Dhalf.coeffs()))
print("POSITIVE_R_BAD_SUPPORTS", faces, "MIN_LEADING_COEFF", min_face_coeff)
print("ONE_SIDE_POS_TERMS", len(pos.terms()), "MIN_COEFF", min(pos.coeffs()), "MAX_COEFF", max(pos.coeffs()))
print("ONE_SIDE_LIMIT = 2*(1+U)*N/D with 4*N*S-3*D coefficientwise positive")
print("INTERSECTION_LIMIT verified; after R->infinity and normalization gives")
print("((2a0+3a3)/((a0+a3)(a0+2a3)))*((A+1)(B+1)/(A+B+1)) >= 3/2")
print("ALL_EXACT_CHECKS_PASS")
