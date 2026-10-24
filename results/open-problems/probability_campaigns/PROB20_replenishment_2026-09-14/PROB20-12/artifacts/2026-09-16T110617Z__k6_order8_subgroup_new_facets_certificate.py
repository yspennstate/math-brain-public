"""Exact reproducibility certificate for the 2026-09-16T110617Z PROB20-12 run.

Run from a checkout of yspennstate/math-open-problems.  This extends the
previous exact 6,880-facet certificate by descending from the orbit-size-3
K6 wall to two order-8 subgroups, extracting two further full facet orbits,
and checking closure of those two invariant slices after augmentation.

All facet/rank/orbit assertions use exact integer/rational SymPy arithmetic.
The only group actions are finite permutations.
"""

from pathlib import Path
import itertools
import runpy
import collections
import sympy as sp

HERE = Path(__file__).resolve().parent
PREV = HERE / "2026-09-16T081000Z__c6_new_facet_orbits_certificate.py"
ns = runpy.run_path(str(PREV))

V = ns["V"]
C = ns["C"]
EDGES = ns["EDGES"]
EID = ns["EID"]
ST = ns["ST"]
COL = ns["COL"]
SINDEX = ns["SINDEX"]
i0 = ns["i0"]
F = ns["F"]
FULLGRP = ns["FULLGRP"]
FULLPERMS = ns["FULLPERMS"]
STAB = ns["STAB"]
WORBS = ns["WORBS"]
FAC_AUG = ns["FAC_AUG"]
transf = ns["transf"]
state_perm = ns["state_perm"]
normalize_rat_vec = ns["normalize_rat_vec"]
extreme_rays = ns["extreme_rays"]
averaged_generators = ns["averaged_generators"]

assert len(ST) == 90
assert len(FAC_AUG) == 6880
assert [len(o) for o in WORBS] == [2, 3, 8, 12, 16, 24, 24]


def edge(e):
    return tuple(sorted(e))


def ix(c, e):
    return 15 * c + EID[edge(e)]


def dot(a, r):
    return sum(x * y for x, y in zip(a, r))


def compose(p, q):
    return tuple(p[q[i]] for i in range(90))


def generated_group(gens):
    identity = tuple(range(90))
    G = {identity, *gens}
    changed = True
    while changed:
        changed = False
        cur = list(G)
        for p in cur:
            for q in cur:
                r = compose(p, q)
                if r not in G:
                    G.add(r)
                    changed = True
    return sorted(G)


def group_orbits(group):
    unseen = set(range(90))
    out = []
    while unseen:
        x = min(unseen)
        o = {p[x] for p in group}
        out.append(tuple(sorted(o)))
        unseen -= o
    return out


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


def face_from_fixed_ray(r, orbs, orbidx):
    y = [r[orbidx[s]] for s in range(90)]
    Z = [s for s, v in enumerate(y) if v == 0]
    Dfull = sp.Matrix.hstack(*F.columnspace())
    rank = Dfull[Z, :].rank()
    ns0 = Dfull[Z, :].nullspace()
    S = sp.Matrix.hstack(*[Dfull * v for v in ns0])
    rays = extreme_rays(S)
    return y, Z, rank, S, rays


def active_set_from_slack(r):
    return frozenset(i for i, x in enumerate(r) if x == 0)


def add_orbit(catalog, fam, a, b):
    out = dict(catalog)
    for g in FULLGRP:
        aa = transf(a, g)
        assert all(dot(aa, s) <= b for s in ST)
        ac = frozenset(i for i, s in enumerate(ST) if dot(aa, s) == b)
        if ac not in out:
            out[ac] = (fam, tuple(aa), b, tuple(b - dot(aa, s) for s in ST))
    return out


def active_minor_det(ac):
    AF = F[sorted(ac), :]
    assert AF.rank() == 37
    piv_rows = AF.T.rref()[1]
    chosen_rows = [sorted(ac)[i] for i in piv_rows]
    M = F[chosen_rows, :]
    piv_cols = M.rref()[1]
    minor = M[:, list(piv_cols)]
    assert minor.shape == (37, 37)
    return int(minor.det())


# ---------------------------------------------------------------------------
# Orbit-size-3 wall: v0=001122, v=002211.
# ---------------------------------------------------------------------------
j = min(WORBS[1])
assert COL[i0] == (0, 0, 1, 1, 2, 2)
assert COL[j] == (0, 0, 2, 2, 1, 1)
Gedge = [p for p in STAB if p[j] == j]
assert len(Gedge) == 16

# H7 generators:
#   site (0 1), color identity;
#   site (2 4 3 5), color (1 2).
g7a = state_perm((1, 0, 2, 3, 4, 5), (0, 1, 2))
g7b = state_perm((0, 1, 4, 5, 3, 2), (0, 2, 1))
H7 = generated_group([g7a, g7b])
assert len(H7) == 8
assert all(p[i0] == i0 and p[j] == j for p in H7)

orbs7, orbidx7, D7, S7 = invariant_data_group(j, H7)
assert len(orbs7) == 16
assert S7.shape[1] == 7
rays7 = extreme_rays(S7)
assert len(rays7) == 20

gens7 = averaged_generators(FAC_AUG, j, H7, orbs7)
dirs7 = {g[0] for g in gens7}
missing7 = sorted(set(rays7) - dirs7)
assert missing7 == [
    (0,0,0,1,1,3,0,2,2,0,0,2,0,0,0,2),
    (0,0,0,1,3,1,2,0,2,0,2,0,0,0,0,2),
    (0,0,0,2,0,2,1,3,1,0,0,2,0,0,2,0),
    (0,0,0,2,2,0,3,1,1,0,2,0,0,0,2,0),
]

lifted7 = []
for r in missing7:
    y, Z, rank, Sf, fr = face_from_fixed_ray(r, orbs7, orbidx7)
    assert rank == 36
    assert Sf.shape[1] == 2
    assert len(fr) == 2
    for rr in fr:
        ac = active_set_from_slack(rr)
        assert F[sorted(ac), :].rank() == 37
        lifted7.append(ac)
assert len(lifted7) == 8

# Sparse representative of the resulting full orbit, one-based display:
# x0(12)+x0(56) <= x1(34)+x1(35)+x1(46)
#   + x2(13)+x2(14)+x2(23)+x2(24)+x2(34)+x2(36)+x2(45).
a3 = [0] * 45
for e in [(0,1), (4,5)]:
    a3[ix(0, e)] += 1
for e in [(2,3), (2,4), (3,5)]:
    a3[ix(1, e)] -= 1
for e in [(0,2), (0,3), (1,2), (1,3), (2,3), (2,5), (3,4)]:
    a3[ix(2, e)] -= 1
b3 = 0
vals3 = [dot(a3, s) for s in ST]
assert collections.Counter(vals3) == {0: 46, -1: 40, -2: 4}
ac3 = frozenset(i for i, x in enumerate(vals3) if x == 0)
assert ac3 not in FAC_AUG
assert active_minor_det(ac3) == 2
orb3 = {frozenset(p[i] for i in ac3) for p in FULLPERMS}
assert len(orb3) == 1080
assert 4320 // len(orb3) == 4
assert all(ac in orb3 for ac in lifted7)

FAC_7960 = add_orbit(FAC_AUG, "new3", a3, b3)
assert len(FAC_7960) == 7960
assert collections.Counter(t[0] for t in FAC_7960.values())["new3"] == 1080
assert not (set(rays7) - {g[0] for g in averaged_generators(FAC_7960, j, H7, orbs7)})

# ---------------------------------------------------------------------------
# H8 slice.
# ---------------------------------------------------------------------------
# generators:
#   site (4 5), color identity;
#   site (2 4)(3 5), color (1 2).
g8a = state_perm((0, 1, 2, 3, 5, 4), (0, 1, 2))
g8b = state_perm((0, 1, 4, 5, 2, 3), (0, 2, 1))
H8 = generated_group([g8a, g8b])
assert len(H8) == 8
assert all(p[i0] == i0 and p[j] == j for p in H8)

orbs8, orbidx8, D8, S8 = invariant_data_group(j, H8)
assert len(orbs8) == 18
assert S8.shape[1] == 8
rays8 = extreme_rays(S8)
assert len(rays8) == 18

gens8 = averaged_generators(FAC_7960, j, H8, orbs8)
dirs8 = {g[0] for g in gens8}
missing8 = sorted(set(rays8) - dirs8)
assert missing8 == [
    (0,2,0,0,2,1,1,1,1,2,0,0,0,0,0,0,0,2),
    (0,2,0,1,1,2,0,0,2,1,1,0,0,0,2,0,0,0),
]

lifted8 = []
for r in missing8:
    y, Z, rank, Sf, fr = face_from_fixed_ray(r, orbs8, orbidx8)
    assert rank == 36
    assert Sf.shape[1] == 2
    assert len(fr) == 2
    for rr in fr:
        ac = active_set_from_slack(rr)
        assert F[sorted(ac), :].rank() == 37
        lifted8.append(ac)
assert len(lifted8) == 4

# Sparse representative, one-based display:
# x0(15)+x0(16)+x0(35)+x0(36)+x0(45)+x0(46)+x0(56)
# +x1(15)+x1(16)+x1(56)+x2(56) <= 1+x2(23)+x2(24).
a4 = [0] * 45
for e in [(0,4), (0,5), (2,4), (2,5), (3,4), (3,5), (4,5)]:
    a4[ix(0, e)] += 1
for e in [(0,4), (0,5), (4,5)]:
    a4[ix(1, e)] += 1
a4[ix(2, (4,5))] += 1
for e in [(1,2), (1,3)]:
    a4[ix(2, e)] -= 1
b4 = 1
vals4 = [dot(a4, s) for s in ST]
assert collections.Counter(vals4) == {1: 54, 0: 36}
ac4 = frozenset(i for i, x in enumerate(vals4) if x == 1)
assert ac4 not in FAC_7960
assert active_minor_det(ac4) == 1
orb4 = {frozenset(p[i] for i in ac4) for p in FULLPERMS}
assert len(orb4) == 540
assert 4320 // len(orb4) == 8
assert all(ac in orb4 for ac in lifted8)
assert orb3.isdisjoint(orb4)

FAC_8500 = add_orbit(FAC_7960, "new4", a4, b4)
assert len(FAC_8500) == 8500
assert collections.Counter(t[0] for t in FAC_8500.values())["new4"] == 540
assert not (set(rays8) - {g[0] for g in averaged_generators(FAC_8500, j, H8, orbs8)})

print("states", len(ST), "catalog_start", len(FAC_AUG), "catalog_final", len(FAC_8500))
print("wall", "001122", "002211", "ordered_edge_stabilizer", len(Gedge))
print("H7", "order", len(H7), "state_orbits", len(orbs7), "fixed_dim", S7.shape[1],
      "rays", len(rays7), "missing_before", len(missing7), "missing_after", 0)
print("new3", "orbit", len(orb3), "stabilizer", 4320 // len(orb3),
      "active", len(ac3), "minor_det", active_minor_det(ac3),
      "slack_counts", dict(sorted(collections.Counter(-x for x in vals3).items())))
print("H8", "order", len(H8), "state_orbits", len(orbs8), "fixed_dim", S8.shape[1],
      "rays", len(rays8), "missing_before", len(missing8), "missing_after", 0)
print("new4", "orbit", len(orb4), "stabilizer", 4320 // len(orb4),
      "active", len(ac4), "minor_det", active_minor_det(ac4),
      "objective_counts", dict(sorted(collections.Counter(vals4).items())))
print("ALL EXACT CHECKS PASSED")
