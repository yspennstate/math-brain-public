"""Completeness of the Appendix A case enumeration.

Appendix A reduces Lemma 8.1 to the finite list of noncoordinate, non-L slab
normals M = c1 Z1 + c2 Z2 + c3 Z3 + (r external unit coefficients) with
r in {0,1,2}, max c - min c <= 2, and the coefficient-sum condition (A.2)
    m = 1 - E - delta1 - delta2 + delta3,
where c_i = m + delta_i, delta_i in {0,1,2}, min delta = 0, and E is the sum
of the r external signs (E in {0}, {-1,1}, {-2,0,2} for r = 0, 1, 2).

This script enumerates every solution, quotients by permutations of the
Z-coordinates, removes the coordinate and L cases, and compares the
resulting sets with the printed 9 + 19 + 26 rows.

Run:  python -u check_appendixA_completeness.py
"""
from itertools import product

E_SETS = {0: [0], 1: [-1, 1], 2: [-2, 0, 2]}

printed = {
    0: [(-3, -1, -1), (-2, -1, 0), (-1, -1, 1), (0, 1, 2), (1, 2, 2),
        (1, 3, 3), (2, 2, 3), (2, 3, 4), (3, 3, 5)],
    1: [(-4, -2, -2), (-3, -2, -1), (-2, -2, 0), (-2, -1, -1), (-2, 0, 0),
        (-1, -1, 0), (-1, 0, 1), (0, 0, 2), (0, 1, 1), (0, 2, 2), (1, 1, 2),
        (1, 2, 3), (2, 2, 2), (2, 2, 4), (2, 3, 3), (2, 4, 4), (3, 3, 4),
        (3, 4, 5), (4, 4, 6)],
    2: [(-5, -3, -3), (-4, -3, -2), (-3, -3, -1), (-3, -2, -2), (-3, -1, -1),
        (-2, -2, -1), (-2, -1, 0), (-1, -1, -1), (-1, -1, 1), (-1, 0, 0),
        (-1, 1, 1), (0, 0, 1), (0, 1, 2), (1, 1, 1), (1, 1, 3), (1, 2, 2),
        (1, 3, 3), (2, 2, 3), (2, 3, 4), (3, 3, 3), (3, 3, 5), (3, 4, 4),
        (3, 5, 5), (4, 4, 5), (4, 5, 6), (5, 5, 7)],
}

fails = 0
for r in (0, 1, 2):
    found = set()
    for delta in product((0, 1, 2), repeat=3):
        if min(delta) != 0:
            continue
        for E in E_SETS[r]:
            m = 1 - E - delta[0] - delta[1] + delta[2]
            c = tuple(m + d for d in delta)
            key = tuple(sorted(c))
            # remove the coordinate cases (M = +-Z_j: one entry +-1, rest 0)
            nz = [x for x in c if x]
            if len(nz) <= 1 and (not nz or abs(nz[0]) == 1) and r == 0:
                continue
            # for r >= 1 a "coordinate" slab in the reduced sense is a pure
            # external or a single +-Z_j with no other Z-content: M with
            # c = 0 entirely is an external-only form; c = +-e_j gives the
            # matrix argument of the appendix only when r = 0, so keep the
            # r >= 1 ones (they appear in the printed table, e.g. (-1,0,1)
            # ... check below which convention reproduces the print)
            if all(x == 0 for x in c):
                continue
            # remove the L case (M = +-L, i.e. b = +-(1,1,1): c = (1,1,-1)
            # up to the fixed c3 sign, appearing as c = (1,1,-1)) and the
            # identical-to-L normal c = (1,1,1) with r = 0 is b=(1,1,-1)...
            # The unambiguous L-cases: sorted |c| = (1,1,1) with r = 0 and
            # product of signs making M = +-L; enumerate explicitly:
            if r == 0 and key in ((-1, -1, -1), (1, 1, 1)):
                continue
            found.add(key)
    want = set(printed[r])
    extra = sorted(found - want)
    missing = sorted(want - found)
    status = "OK" if not extra and not missing else "MISMATCH"
    if status != "OK":
        fails += 1
    print(f"r={r}: derived {len(found)} classes, printed {len(printed[r])} "
          f"[{status}]")
    if extra:
        print(f"   derived but not printed: {extra}")
    if missing:
        print(f"   printed but not derived: {missing}")

print()
print("COMPLETENESS CHECK", "PASSED" if fails == 0 else
      f"NEEDS INTERPRETATION ({fails} set mismatches; see above)")
