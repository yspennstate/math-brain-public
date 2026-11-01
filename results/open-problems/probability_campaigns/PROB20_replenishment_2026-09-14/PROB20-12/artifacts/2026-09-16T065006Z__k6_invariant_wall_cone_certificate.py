import itertools
import collections
from functools import reduce
from math import gcd
import sympy as sp

# Exact certificate for the symmetry-fixed wall-cone theorem in
# PROB20-12, 2026-09-16T065006Z.
# No floating point or LP/polyhedral black box is used.

V = tuple(range(6))
C = tuple(range(3))
EDGES = list(itertools.combinations(V, 2))
EID = {e: i for i, e in enumerate(EDGES)}


def edge(e):
    return tuple(sorted(e))


def ix(c, e):
    return 15 * c + EID[edge(e)]


# ------------------------------------------------------------------
# 90 balanced colorings and 45-coordinate colored-edge incidences.
# ------------------------------------------------------------------
ST = []
COL = []
for col in itertools.product(C, repeat=6):
    if all(col.count(c) == 2 for c in C):
        r = [0] * 45
        for c in C:
            pts = tuple(v for v in V if col[v] == c)
            r[ix(c, pts)] = 1
        ST.append(tuple(r))
        COL.append(col)

assert len(ST) == 90
SINDEX = {c: i for i, c in enumerate(COL)}
i0 = SINDEX[(0, 0, 1, 1, 2, 2)]
assert i0 == 0


def val(a, r):
    return sum(x * y for x, y in zip(a, r))


def active(a, b):
    return frozenset(i for i, r in enumerate(ST) if val(a, r) == b)


def slackvec(a, b):
    return tuple(b - val(a, r) for r in ST)


def inside(S):
    return [e for e in EDGES if set(e) <= set(S)]


# ------------------------------------------------------------------
# Reconstruct the archived 4,450-facet catalogue.
# Store one representative per active set.
# ------------------------------------------------------------------
FAC = {}


def put(fam, a, b):
    assert all(val(a, r) <= b for r in ST)
    ac = active(a, b)
    if ac not in FAC:
        FAC[ac] = (fam, tuple(a), b, slackvec(a, b))


# Nonnegativity.
for c in C:
    for e in EDGES:
        a = [0] * 45
        a[ix(c, e)] = -1
        put("nonneg", a, 0)

# Single-fibre family.
bad = {0, 63, 11, 21, 38, 56}
for tc in C:
    others = [c for c in C if c != tc]
    c0, c1 = others
    for te in EDGES:
        comp = tuple(v for v in V if v not in te)
        bases = list(itertools.combinations(comp, 2))
        for mask in range(64):
            if mask in bad:
                continue
            a = [0] * 45
            a[ix(tc, te)] = 1
            for j, B in enumerate(bases):
                co = edge(set(comp) - set(B))
                if (mask >> j) & 1:
                    a[ix(c0, B)] -= 1
                else:
                    a[ix(c1, co)] -= 1
            put("fibre", a, 0)

# Aggregate blossoms.
for SS in itertools.combinations(V, 3):
    a = [0] * 45
    for c in C:
        for e in EDGES:
            if set(e) <= set(SS):
                a[ix(c, e)] += 1
    put("blossom", a, 1)

# s1.
for tc in C:
    others = [c for c in C if c != tc]
    for AA in itertools.combinations(V, 3):
        A = set(AA)
        B = set(V) - A
        a = [0] * 45
        for e in EDGES:
            if set(e) <= A:
                a[ix(tc, e)] += 1
            if set(e) <= B:
                for c in others:
                    a[ix(c, e)] -= 1
        put("s1", a, 0)

# s2.
for tc in C:
    for be in EDGES:
        A = set(V) - set(be)
        a = [0] * 45
        for c in C:
            if c != tc:
                for e in EDGES:
                    if set(e) <= A:
                        a[ix(c, e)] += 1
        a[ix(tc, be)] -= 1
        put("s2", a, 1)

# Full S6 x S3 action on colored-edge coefficients.
FULLGRP = []
for vp_t in itertools.permutations(V):
    for cp_t in itertools.permutations(C):
        FULLGRP.append((vp_t, cp_t))


def transf(a, g):
    vp, cp = g
    out = [0] * 45
    for c in C:
        for e in EDGES:
            out[ix(cp[c], (vp[e[0]], vp[e[1]]))] = a[ix(c, e)]
    return out


# Bridge seed and orbit.
L = {0, 3}
D = {1, 2}
R = {4, 5}
SA = [e for e in inside(L | D) if set(e) != D]
SB = [e for e in inside(D | R) if set(e) != D]
a = [0] * 45
for e in SA:
    a[ix(0, e)] += 1
for c in (1, 2):
    for e in SB:
        a[ix(c, e)] -= 1
for g in FULLGRP:
    put("bridge", transf(a, g), 0)

# Residue seed and orbit.
T = {0, 1, 3}
d = 2
RR = {4, 5}
AA = set(inside(T)) | {edge((d, r)) for r in RR}
BB = {edge((d, t)) for t in T} | set(inside(RR))
CC = {edge((t, r)) for t in T for r in RR}
a = [0] * 45
for e in AA:
    a[ix(0, e)] += 1
    a[ix(1, e)] -= 1
for e in BB:
    a[ix(1, e)] += 1
    a[ix(2, e)] -= 1
for e in CC:
    a[ix(2, e)] += 1
    a[ix(0, e)] -= 1
for g in FULLGRP:
    put("residue", transf(a, g), 1)

# Sparse-cover seed and orbit.
a = [0] * 45
for e in [(0, 1), (0, 2)]:
    a[ix(0, e)] += 1
for e in [(1, 5), (2, 5), (3, 4), (3, 5), (4, 5)]:
    a[ix(1, e)] -= 1
for e in [(3, 5), (4, 5)]:
    a[ix(2, e)] -= 1
for g in FULLGRP:
    put("sparse", transf(a, g), 0)

assert len(FAC) == 4450
famcnt = collections.Counter(t[0] for t in FAC.values())
assert famcnt == {
    "nonneg": 45,
    "fibre": 2610,
    "blossom": 10,
    "s1": 30,
    "s2": 45,
    "bridge": 270,
    "residue": 360,
    "sparse": 1080,
}
print("facet_families", dict(famcnt))

# Affine evaluation matrix: constant plus 45 incidence coordinates.
F = sp.Matrix([[1] + list(r) for r in ST])
assert F.rank() == 38
print("affine_rank", F.rank())

# ------------------------------------------------------------------
# Base stabilizer G0 of 001122, order 48.
# ------------------------------------------------------------------
pairs = {0: (0, 1), 1: (2, 3), 2: (4, 5)}
STAB = []
for cp_t in itertools.permutations(C):
    cp = {c: cp_t[c] for c in C}
    for flips in itertools.product([0, 1], repeat=3):
        vp = {}
        for c in C:
            src = pairs[c]
            dst = pairs[cp[c]]
            if flips[c]:
                dst = dst[::-1]
            vp[src[0]] = dst[0]
            vp[src[1]] = dst[1]
        perm = [None] * 90
        for ii, s in enumerate(COL):
            t = [None] * 6
            for v in V:
                t[vp[v]] = cp[s[v]]
            perm[ii] = SINDEX[tuple(t)]
        STAB.append(tuple(perm))

assert len(STAB) == 48


def group_orbits(group):
    unseen = set(range(90))
    out = []
    while unseen:
        x = min(unseen)
        o = {p[x] for p in group}
        out.append(tuple(sorted(o)))
        unseen -= o
    return out


# Seven G0 wall orbits.
unseen = set(range(90)) - {i0}
WORBS = []
while unseen:
    j = min(unseen)
    o = {p[j] for p in STAB}
    WORBS.append(o)
    unseen -= o
WORBS = sorted(WORBS, key=lambda z: (len(z), min(z)))
assert [len(o) for o in WORBS] == [2, 3, 8, 12, 16, 24, 24]
print("wall_orbits", [len(o) for o in WORBS])


# ------------------------------------------------------------------
# Exact invariant fixed-wall subspace.
# ------------------------------------------------------------------
def invariant_data(j):
    G = [p for p in STAB if p[j] == j]
    orbs = group_orbits(G)
    orbidx = {}
    for oi, o in enumerate(orbs):
        for s in o:
            orbidx[s] = oi

    # Reynolds averages of each affine feature, evaluated on state orbits.
    B = sp.Matrix([
        [sp.Rational(sum(int(F[s, k]) for s in o), len(o)) for k in range(46)]
        for o in orbs
    ])
    cols = B.columnspace()
    D = sp.Matrix.hstack(*cols)

    # Impose s(v0)=s(j)=0.
    R = D[[orbidx[i0], orbidx[j]], :]
    ns = R.nullspace()
    S = sp.Matrix.hstack(*[D * v for v in ns])
    return G, orbs, orbidx, D, S


fixed_summary = []
for o in WORBS:
    j = min(o)
    G, orbs, orbidx, D, S = invariant_data(j)
    fixed_summary.append((len(o), j, COL[j], len(G), len(orbs), D.shape[1], S.shape[1]))

expected_dims = [4, 6, 7, 13, 12, 19, 25]
assert [x[-1] for x in fixed_summary] == expected_dims
for row in fixed_summary:
    print("fixed_wall", row)


# ------------------------------------------------------------------
# Exact ray enumeration in the small fixed cones.
# ------------------------------------------------------------------
def normalize_rat_vec(v):
    vals = [sp.Rational(x) for x in list(v)]
    den = sp.ilcm(*[x.q for x in vals])
    ints = [int(x * den) for x in vals]
    gg = reduce(gcd, [abs(x) for x in ints if x] or [1])
    ints = [x // gg for x in ints]
    for x in ints:
        if x:
            if x < 0:
                ints = [-y for y in ints]
            break
    return tuple(ints)


def extreme_rays(S):
    q, d = S.shape
    nonzero_rows = [i for i in range(q) if any(S[i, k] != 0 for k in range(d))]
    rays = {}
    for comb in itertools.combinations(nonzero_rows, d - 1):
        M = S[list(comb), :]
        if M.rank() != d - 1:
            continue
        ns = M.nullspace()
        if len(ns) != 1:
            continue
        z = ns[0]
        y = S * z
        if all(v >= 0 for v in y):
            pass
        elif all(v <= 0 for v in y):
            y = -y
        else:
            continue
        if all(v == 0 for v in y):
            continue
        rays[normalize_rat_vec(y)] = comb
    return rays


# Known active facets through v0.
ACT = {ac: t for ac, t in FAC.items() if i0 in ac}
assert len(ACT) == 2985


def actset(ac, p):
    return frozenset(p[i] for i in ac)


def known_averaged_generators(j, G, orbs):
    items = [(ac, t) for ac, t in ACT.items() if j in ac]
    activekeys = {ac for ac, _ in items}
    facdict = {ac: t for ac, t in items}
    seen = set()
    gens = []
    for ac, t in items:
        if ac in seen:
            continue
        orbitacs = {actset(ac, p) for p in G} & activekeys
        seen |= orbitacs
        ss = [0] * 90
        for x in orbitacs:
            s = facdict[x][3]
            for k in range(90):
                ss[k] += s[k]
        vals = []
        for o in orbs:
            vv = {ss[s] for s in o}
            assert len(vv) == 1
            vals.append(vv.pop())
        gens.append((normalize_rat_vec(sp.Matrix(vals)), t[0], len(orbitacs)))
    return gens


small_expected = {2: 4, 3: 11, 8: 7}
for o in WORBS[:3]:
    osize = len(o)
    j = min(o)
    G, orbs, orbidx, D, S = invariant_data(j)
    rays = extreme_rays(S)
    assert len(rays) == small_expected[osize]
    gens = known_averaged_generators(j, G, orbs)
    genkeys = {g[0] for g in gens}
    missing = set(rays) - genkeys
    assert not missing

    print("wall_type", osize, "rep", "".join(map(str, COL[j])))
    print("  edge_stabilizer_order", len(G))
    print("  state_orbits", len(orbs))
    print("  fixed_wall_dim", S.shape[1])
    print("  extreme_rays", len(rays))

    for n, rk in enumerate(sorted(rays), 1):
        matches = sorted({(fam, orbsize) for key, fam, orbsize in gens if key == rk})
        print("  ray", n, rk, "matches", matches)

    if osize == 2:
        assert all(any(fam == "nonneg" for key, fam, sz in gens if key == rk) for rk in rays)
    if osize == 3:
        assert all(any(fam in {"nonneg", "s2"} for key, fam, sz in gens if key == rk) for rk in rays)
    if osize == 8:
        assert all(any(fam == "nonneg" for key, fam, sz in gens if key == rk) for rk in rays)

print("TOTAL_FIXED_EXTREME_RAYS", sum(small_expected.values()))
print("ALL EXACT CHECKS PASSED")
