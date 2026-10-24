"""Exact extension certificate for PROB20-12, 2026-09-16T081000Z.

Run from a checkout of the repository.  This deliberately imports the previous
verified exact certificate rather than duplicating its 4,450-facet catalogue
construction.  It then performs the new C6 subgroup recursion, checks the exact
separators, extracts the two new full facet orbits, and verifies the augmented
6,880-facet count.
"""

from pathlib import Path
import itertools
import runpy
import collections
from functools import reduce
from math import gcd
import sympy as sp

HERE = Path(__file__).resolve().parent
PREV = HERE / "2026-09-16T065006Z__k6_invariant_wall_cone_certificate.py"
ns = runpy.run_path(str(PREV))

V = ns["V"]
C = ns["C"]
EDGES = ns["EDGES"]
EID = ns["EID"]
ST = ns["ST"]
COL = ns["COL"]
SINDEX = ns["SINDEX"]
i0 = ns["i0"]
FAC = ns["FAC"]
F = ns["F"]
FULLGRP = ns["FULLGRP"]
STAB = ns["STAB"]
WORBS = ns["WORBS"]
transf = ns["transf"]
normalize_rat_vec = ns["normalize_rat_vec"]
extreme_rays = ns["extreme_rays"]


def edge(e):
    return tuple(sorted(e))


def ix(c, e):
    return 15 * c + EID[edge(e)]


def dot(a, r):
    return sum(x * y for x, y in zip(a, r))


def compose(p, q):
    return tuple(p[q[i]] for i in range(90))


def group_orbits(group):
    unseen = set(range(90))
    out = []
    while unseen:
        x = min(unseen)
        o = {p[x] for p in group}
        out.append(tuple(sorted(o)))
        unseen -= o
    return out


def state_perm(vp, cp):
    perm = [None] * 90
    for ii, s in enumerate(COL):
        t = [None] * 6
        for v in V:
            t[vp[v]] = cp[s[v]]
        perm[ii] = SINDEX[tuple(t)]
    return tuple(perm)


def invariant_data_group(j, G):
    orbs = group_orbits(G)
    orbidx = {}
    for oi, o in enumerate(orbs):
        for s in o:
            orbidx[s] = oi
    B = sp.Matrix([
        [sp.Rational(sum(int(F[s, k]) for s in o), len(o)) for k in range(46)]
        for o in orbs
    ])
    D = sp.Matrix.hstack(*B.columnspace())
    R = D[[orbidx[i0], orbidx[j]], :]
    ns0 = R.nullspace()
    S = sp.Matrix.hstack(*[D * v for v in ns0])
    return orbs, orbidx, D, S


def actset(ac, p):
    return frozenset(p[i] for i in ac)


def averaged_generators(catalog, j, G, orbs):
    act = {ac: t for ac, t in catalog.items() if i0 in ac and j in ac}
    activekeys = set(act)
    seen = set()
    gens = []
    for ac, t in act.items():
        if ac in seen:
            continue
        orbitacs = {actset(ac, p) for p in G} & activekeys
        seen |= orbitacs
        ss = [0] * 90
        for x in orbitacs:
            s = act[x][3]
            for k in range(90):
                ss[k] += s[k]
        vals = []
        for o in orbs:
            vv = {ss[s] for s in o}
            assert len(vv) == 1
            vals.append(vv.pop())
        gens.append((normalize_rat_vec(sp.Matrix(vals)), t[0], len(orbitacs)))
    return gens


# ---------------------------------------------------------------------------
# The orbit-size-2 wall and its cyclic order-6 subgroup.
# ---------------------------------------------------------------------------
j = min(WORBS[0])
assert COL[j] == (1, 1, 2, 2, 0, 0)

# Generator: site cycle (0 3 5 1 2 4), color cycle (0 1 2).
vp = (3, 2, 4, 5, 0, 1)
cp = (1, 2, 0)
gen = state_perm(vp, cp)
identity = tuple(range(90))
H = [identity]
for _ in range(5):
    H.append(compose(gen, H[-1]))
assert len(set(H)) == 6
assert compose(gen, H[-1]) == identity
assert all(p[i0] == i0 and p[j] == j for p in H)

orbs, orbidx, D, S = invariant_data_group(j, H)
assert len(orbs) == 20
assert D.shape[1] == 9
assert S.shape[1] == 7
expected_orbit_data = [
    (1, "001122"), (6, "001212"), (6, "001221"), (3, "002211"),
    (6, "010212"), (6, "010221"), (2, "011202"), (6, "011220"),
    (6, "012012"), (6, "012021"), (6, "012201"), (6, "012210"),
    (6, "020112"), (6, "020211"), (2, "021012"), (6, "022011"),
    (1, "112200"), (6, "120201"), (2, "122010"), (1, "220011"),
]
assert [(len(o), "".join(map(str, COL[min(o)]))) for o in orbs] == expected_orbit_data

rays = extreme_rays(S)
assert len(rays) == 13
old_gens = averaged_generators(FAC, j, H, orbs)
old_dirs = {g[0] for g in old_gens}
missing = sorted(set(rays) - old_dirs)
assert missing == [
    (0,1,1,1,0,3,3,3,0,3,3,0,0,0,0,3,0,0,6,3),
    (0,2,0,1,0,1,3,2,1,3,2,0,0,0,3,3,0,0,3,3),
    (0,3,0,1,0,0,3,3,3,3,1,1,0,0,6,3,0,0,0,3),
]
seps = [
    (0,-1,0,0,1,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0),
    (0,-1,1,0,1,0,0,0,0,0,0,3,1,0,0,0,0,0,0,0),
    (0,-1,1,0,1,2,0,0,0,0,0,0,1,0,0,0,0,1,0,0),
]
unique_old = sorted({g[0] for g in old_gens})
assert len(unique_old) == 117
for r, lam, expected in zip(missing, seps, (-1, -2, -3)):
    assert all(sum(a*b for a, b in zip(lam, g)) >= 0 for g in unique_old)
    assert sum(a*b for a, b in zip(lam, r)) == expected


# ---------------------------------------------------------------------------
# Two explicit new facet representatives.
# ---------------------------------------------------------------------------
NEW_SETS = [
    {
        0: [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3),(2,5),(3,4)],
        1: [(0,1),(0,2),(0,3),(0,5),(1,2),(1,3),(1,4),(2,3),(2,4),(2,5),(3,4),(3,5)],
        2: [(0,2),(1,3),(2,3)],
    },
    {
        0: [(0,1),(0,2),(1,2),(1,3),(1,4),(2,3),(2,4),(2,5),(3,4)],
        1: [(0,1),(0,2),(1,2),(1,3),(1,4),(2,3),(2,4),(2,5),(3,4)],
        2: [(0,2),(1,2),(1,3),(1,4),(2,3),(2,4)],
    },
]

# Full state action.
FULLPERMS = []
for vp0, cp0 in FULLGRP:
    FULLPERMS.append(state_perm(vp0, cp0))
assert len(FULLPERMS) == 4320

new_active_sets = []
expected = [
    (50, {0: 2, 1: 38, 2: 50}, -1, 2160, 2),
    (54, {1: 36, 2: 54}, +1, 270, 16),
]
for idx, (Ssets, exp) in enumerate(zip(NEW_SETS, expected), 1):
    a = [0] * 45
    for c, es in Ssets.items():
        for e in es:
            a[ix(c, e)] = 1
    vals = [dot(a, r) for r in ST]
    assert max(vals) == 2
    ac = frozenset(i for i, x in enumerate(vals) if x == 2)
    assert len(ac) == exp[0]
    assert dict(sorted(collections.Counter(vals).items())) == exp[1]
    assert ac not in FAC

    AF = F[sorted(ac), :]
    assert AF.rank() == 37
    piv_rows = AF.T.rref()[1]
    chosen_rows = [sorted(ac)[i] for i in piv_rows]
    M = F[chosen_rows, :]
    piv_cols = M.rref()[1]
    minor = M[:, list(piv_cols)]
    assert minor.shape == (37, 37)
    assert minor.det() == exp[2]

    orb = {frozenset(p[i] for i in ac) for p in FULLPERMS}
    assert len(orb) == exp[3]
    assert 4320 // len(orb) == exp[4]
    new_active_sets.append(ac)

# Full affine dimension exact certificate.
piv_rows = F.T.rref()[1]
M = F[list(piv_rows), :]
piv_cols = M.rref()[1]
assert len(piv_rows) == len(piv_cols) == 38
assert M[:, list(piv_cols)].det() == -1

# Distinct full symmetry orbits.
orb0 = {frozenset(p[i] for i in new_active_sets[0]) for p in FULLPERMS}
orb1 = {frozenset(p[i] for i in new_active_sets[1]) for p in FULLPERMS}
assert orb0.isdisjoint(orb1)
assert not (orb0 & set(FAC))
assert not (orb1 & set(FAC))


# ---------------------------------------------------------------------------
# Augment the exact catalogue and re-check the C6 fixed cone.
# ---------------------------------------------------------------------------
FAC_AUG = dict(FAC)

def put_aug(fam, a, b):
    assert all(dot(a, r) <= b for r in ST)
    ac = frozenset(i for i, r in enumerate(ST) if dot(a, r) == b)
    if ac not in FAC_AUG:
        FAC_AUG[ac] = (fam, tuple(a), b, tuple(b - dot(a, r) for r in ST))

for idx, Ssets in enumerate(NEW_SETS, 1):
    a = [0] * 45
    for c, es in Ssets.items():
        for e in es:
            a[ix(c, e)] = 1
    for g in FULLGRP:
        put_aug(f"new{idx}", transf(a, g), 2)

assert len(FAC_AUG) == 6880
counts = collections.Counter(t[0] for t in FAC_AUG.values())
assert counts["new1"] == 2160
assert counts["new2"] == 270

aug_gens = averaged_generators(FAC_AUG, j, H, orbs)
aug_dirs = {g[0] for g in aug_gens}
assert not (set(rays) - aug_dirs)

print("states", len(ST), "old_facets", len(FAC), "augmented_facets", len(FAC_AUG))
print("wall", "001122", "112200", "C6_state_orbits", len(orbs), "fixed_wall_dim", S.shape[1])
print("C6_extreme_rays", len(rays), "old_uncovered", len(missing), "old_unique_averaged_dirs", len(unique_old))
print("separations", [sum(a*b for a,b in zip(lam,r)) for lam,r in zip(seps,missing)])
print("new_facet_orbits", [(2160,2,50,-1),(270,16,54,1)])
print("augmented_C6_uncovered", len(set(rays)-aug_dirs))
print("ALL EXACT CHECKS PASSED")
