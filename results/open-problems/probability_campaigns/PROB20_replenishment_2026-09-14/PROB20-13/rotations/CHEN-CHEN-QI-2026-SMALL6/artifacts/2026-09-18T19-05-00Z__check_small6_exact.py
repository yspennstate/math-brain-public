#!/usr/bin/env python3
"""Exact finite checker for Chen--Chen--Qi (2026), Open Problem 3.

Purpose: exclude irreducible limited doubly-simple presentations above the
known recursive-line values on 6x6 and 7x6.

The checker uses only exact combinatorics and integer polynomial identities.
It assumes the source-proved uniqueness (up to row/column permutation) of the
ordinary extremal C4-free skeletons for m=6,7, and the published exact SOS-rank
bounds BSR(2,q)=q+1, BSR(3,3)=6, BSR(4,3)=BSR(3,4)=7.

For an irreducible displayed decomposition, hereditary irreducibility implies
that every complete displayed subfamily supported in such a subgrid obeys the
corresponding BSR cap. At the minimal putative counterexample totals, there are
exactly two holes, so the remaining free cells are perfectly paired into
2-edges.

For 7x6, five automorphism orbits of individually forbidden 2-edge positions
are certified by explicit three-product polynomial relations (Lofberg--Qi,
Lemma B.2 mechanism). Every locally feasible near-perfect matching contains
one of these forbidden pairs.
"""
from itertools import combinations, permutations
from collections import defaultdict

Cell = tuple[int, int]
Pair = tuple[Cell, Cell]

ONE6 = {
    (0,0),(0,1),(1,2),(1,3),(2,0),(2,2),(2,4),(3,1),
    (3,3),(3,4),(4,1),(4,2),(4,5),(5,0),(5,3),(5,5),
}
ONE7 = ONE6 | {(6,4),(6,5)}

# Five representative forbidden-pair orbits on the canonical 7x6 skeleton.
# Each relation is a list (coefficient, formA, formB); a form is a tuple of
# one or two cells, representing u_rc or u_rc+u_st. The relation means
# sum coeff * formA*formB == 0 as a biquadratic polynomial.
FORBIDDEN_REPS = [
    (
        ((0,5),(3,2)),
        [
            ( 1, ((0,1),), ((4,5),)),
            ( 1, ((3,1),), ((4,2),)),
            (-1, ((4,1),), ((0,5),(3,2))),
        ],
    ),
    (
        ((1,1),(5,1)),
        [
            ( 1, ((1,3),), ((3,1),)),
            ( 1, ((3,1),), ((5,3),)),
            (-1, ((3,3),), ((1,1),(5,1))),
        ],
    ),
    (
        ((3,2),(3,5)),
        [
            ( 1, ((3,1),), ((4,2),)),
            ( 1, ((3,1),), ((4,5),)),
            (-1, ((4,1),), ((3,2),(3,5))),
        ],
    ),
    (
        ((3,2),(5,2)),
        [
            ( 1, ((1,2),), ((3,3),)),
            ( 1, ((1,2),), ((5,3),)),
            (-1, ((1,3),), ((3,2),(5,2))),
        ],
    ),
    (
        ((6,0),(6,2)),
        [
            ( 1, ((2,0),), ((6,4),)),
            ( 1, ((2,2),), ((6,4),)),
            (-1, ((2,4),), ((6,0),(6,2))),
        ],
    ),
]

def canon_pair(a: Cell, b: Cell) -> Pair:
    return (a,b) if a < b else (b,a)

def monomial_key(a: Cell, b: Cell):
    return (tuple(sorted((a[0], b[0]))), tuple(sorted((a[1], b[1]))))

def multiply_forms(f, g):
    out = defaultdict(int)
    for a in f:
        for b in g:
            out[monomial_key(a,b)] += 1
    return dict(out)

def check_relation(relation):
    total = defaultdict(int)
    for coeff, f, g in relation:
        for mon, val in multiply_forms(f,g).items():
            total[mon] += coeff * val
    return all(v == 0 for v in total.values()) and any(coeff for coeff,_,_ in relation)

def automorphisms(m: int, one: set[Cell]):
    row_support = [frozenset(c for r,c in one if r == rr) for rr in range(m)]
    support_to_rows = defaultdict(list)
    for r,s in enumerate(row_support):
        support_to_rows[s].append(r)
    autos = []
    for cp in permutations(range(6)):
        transformed = [frozenset(cp[c] for c in s) for s in row_support]
        choices = [support_to_rows.get(s, []) for s in transformed]
        if any(not x for x in choices):
            continue
        def rec(i, used, rp):
            if i == m:
                autos.append((tuple(rp), tuple(cp)))
                return
            for rr in choices[i]:
                if rr not in used:
                    used.add(rr); rp.append(rr)
                    rec(i+1, used, rp)
                    rp.pop(); used.remove(rr)
        rec(0, set(), [])
    return autos

def transform_cell(cell: Cell, auto):
    rp, cp = auto
    r,c = cell
    return (rp[r], cp[c])

def transform_form(form, auto):
    return tuple(transform_cell(x, auto) for x in form)

def build_forbidden7():
    autos = automorphisms(7, ONE7)
    assert len(autos) == 24, len(autos)
    forbidden = set()
    orbit_sizes = []
    free = {(r,c) for r in range(7) for c in range(6)} - ONE7
    for rep, relation in FORBIDDEN_REPS:
        assert rep[0] in free and rep[1] in free and rep[0] != rep[1]
        assert check_relation(relation)
        orb = set()
        for auto in autos:
            p = canon_pair(transform_cell(rep[0],auto), transform_cell(rep[1],auto))
            assert p[0] in free and p[1] in free
            rel_t = [(coef, transform_form(f,auto), transform_form(g,auto)) for coef,f,g in relation]
            assert check_relation(rel_t)
            for _,f,g in rel_t:
                for form in (f,g):
                    if len(form) == 1:
                        assert form[0] in ONE7
            orb.add(p)
        orbit_sizes.append(len(orb))
        forbidden |= orb
    assert sorted(orbit_sizes) == [6,12,12,24,24], orbit_sizes
    assert len(forbidden) == 78, len(forbidden)
    return autos, forbidden, orbit_sizes

def region_constraints(m: int, one: set[Cell]):
    """Return exact necessary subgrid caps for an irreducible presentation."""
    regs = []
    # 2 x q and q x 2: BSR(2,q)=q+1 (including trivial q=1).
    for rows in combinations(range(m),2):
        for q in range(1,7):
            for cols in combinations(range(6),q):
                cells = frozenset((r,c) for r in rows for c in cols)
                ones = sum(x in one for x in cells)
                regs.append((cells, q+1-ones, ("2xq",rows,cols)))
    for cols in combinations(range(6),2):
        for q in range(1,m+1):
            for rows in combinations(range(m),q):
                cells = frozenset((r,c) for r in rows for c in cols)
                ones = sum(x in one for x in cells)
                regs.append((cells, q+1-ones, ("qx2",rows,cols)))
    # Exact BSR(3,3)=6.
    if m >= 3:
        for rows in combinations(range(m),3):
            for cols in combinations(range(6),3):
                cells = frozenset((r,c) for r in rows for c in cols)
                ones = sum(x in one for x in cells)
                regs.append((cells, 6-ones, ("3x3",rows,cols)))
    # Exact BSR(4,3)=BSR(3,4)=7.
    if m >= 4:
        for rows in combinations(range(m),4):
            for cols in combinations(range(6),3):
                cells = frozenset((r,c) for r in rows for c in cols)
                ones = sum(x in one for x in cells)
                regs.append((cells, 7-ones, ("4x3",rows,cols)))
    if m >= 3:
        for rows in combinations(range(m),3):
            for cols in combinations(range(6),4):
                cells = frozenset((r,c) for r in rows for c in cols)
                ones = sum(x in one for x in cells)
                regs.append((cells, 7-ones, ("3x4",rows,cols)))
    assert all(cap >= 0 for _,cap,_ in regs)
    return regs

def enumerate_near_perfect(m: int, one: set[Cell], forbidden=frozenset()):
    """Enumerate all H=2 matchings obeying the exact necessary subgrid caps."""
    allcells = [(r,c) for r in range(m) for c in range(6)]
    free = sorted(x for x in allcells if x not in one)
    regs = region_constraints(m, one)
    pair_regs = {}
    partners = {a: [] for a in free}
    for a,b in combinations(free,2):
        p = canon_pair(a,b)
        if p in forbidden:
            continue
        inds = [k for k,(cells,cap,_) in enumerate(regs) if a in cells and b in cells]
        if all(regs[k][1] >= 1 for k in inds):
            pair_regs[p] = inds
            partners[a].append(b)
            partners[b].append(a)
    for a in partners:
        partners[a].sort()

    solutions = []
    nodes = 0
    for holes in combinations(free,2):
        rem0 = set(free) - set(holes)
        used = [0]*len(regs)
        current = []
        def dfs(rem):
            nonlocal nodes
            nodes += 1
            if not rem:
                solutions.append((holes, tuple(sorted(current))))
                return
            best = None; opts_best = None
            for a in sorted(rem):
                opts = []
                for b in partners[a]:
                    if b not in rem:
                        continue
                    p = canon_pair(a,b)
                    inds = pair_regs.get(p)
                    if inds is not None and all(used[k] < regs[k][1] for k in inds):
                        opts.append(b)
                if opts_best is None or len(opts) < len(opts_best):
                    best, opts_best = a, opts
                    if not opts:
                        break
            if not opts_best:
                return
            for b in opts_best:
                p = canon_pair(best,b)
                inds = pair_regs[p]
                for k in inds: used[k] += 1
                current.append(p)
                dfs(rem - {best,b})
                current.pop()
                for k in inds: used[k] -= 1
        dfs(rem0)
    unique = {}
    for holes,pairs in solutions:
        key = (tuple(sorted(holes)), tuple(sorted(pairs)))
        unique[key] = key
    return nodes, list(unique.values())

def main():
    assert len(ONE6) == 16 and 36-len(ONE6) == 20
    assert len(ONE7) == 18 and 42-len(ONE7) == 24
    autos7, forbidden7, orbit_sizes = build_forbidden7()
    nodes6, sol6 = enumerate_near_perfect(6, ONE6)
    nodes7_local, sol7_local = enumerate_near_perfect(7, ONE7)
    nodes7_final, sol7_final = enumerate_near_perfect(7, ONE7, forbidden7)

    print("MODEL-INDEPENDENT EXACT CHECKER")
    print("m=6 canonical E1 size=16, free cells=20, target N=25 => E2=9,H=2")
    print(f"m=6 local-BSR search nodes={nodes6}, surviving H=2 matchings={len(sol6)}")
    print("m=7 canonical E1 size=18, free cells=24, target N=29 => E2=11,H=2")
    print(f"m=7 skeleton automorphisms={len(autos7)}")
    print(f"m=7 product-relation forbidden orbit sizes={sorted(orbit_sizes)}, total forbidden pairs={len(forbidden7)}")
    print(f"m=7 local-BSR search nodes={nodes7_local}, surviving H=2 matchings={len(sol7_local)}")
    print(f"m=7 after exact product-relation exclusions nodes={nodes7_final}, surviving H=2 matchings={len(sol7_final)}")
    assert len(sol6) == 0
    assert len(sol7_local) == 24
    assert len(sol7_final) == 0
    assert all(any(p in forbidden7 for p in pairs) for _,pairs in sol7_local)
    print("CONCLUSION_6x6: no irreducible total-25 candidate on the unique extremal skeleton")
    print("CONCLUSION_7x6: no irreducible total-29 candidate on the unique extremal skeleton")
    print("By hereditary irreducibility, larger totals reduce to these minimal exceedance layers.")
    print("CHEN_CHEN_QI_SMALL6_EXACT_PASS")

if __name__ == "__main__":
    main()
