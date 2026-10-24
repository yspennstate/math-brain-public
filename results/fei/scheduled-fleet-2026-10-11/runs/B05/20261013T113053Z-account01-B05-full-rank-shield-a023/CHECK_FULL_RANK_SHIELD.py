#!/usr/bin/env python3
"""Exact finite checks for the B05 full-rank shielding theorem.

The proof is analytic.  This checker independently constructs truth tables and
integer Walsh transforms.  It exhausts every Boolean core D and every
invertible matrix through m=3, then checks representative rectangular
full-column-rank instances and explicit multi-defect cores.
"""

from itertools import product
from random import Random


def parity(x):
    return x.bit_count() & 1


def rank_gf2(rows, m):
    rows = list(rows)
    rank = 0
    for col in range(m):
        pivot = next((i for i in range(rank, len(rows)) if (rows[i] >> col) & 1), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        for i in range(len(rows)):
            if i != rank and ((rows[i] >> col) & 1):
                rows[i] ^= rows[rank]
        rank += 1
    return rank


def fwht(a):
    a = list(a)
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2 * h):
            for j in range(i, i + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    return a


def truth_table(s, m, rows, dmask, avec=0, bvec=0, c=0):
    vals = []
    for z in range(1 << (s + m)):
        x = z & ((1 << s) - 1)
        y = z >> s
        bil = 0
        for i, row in enumerate(rows):
            if (x >> i) & 1:
                bil ^= parity(row & y)
        phase = bil ^ parity(avec & x) ^ parity(bvec & y) ^ c
        d = (dmask >> y) & 1
        vals.append(-1 if (phase ^ d) else 1)
    return vals


def check_instance(s, m, rows, dmask, avec=0, bvec=0, c=0):
    vals = truth_table(s, m, rows, dmask, avec, bvec, c)
    walsh = fwht(vals)
    expected_abs = 1 << s
    nonzero = [w for w in walsh if w]
    assert len(nonzero) == 1 << (2 * m)
    assert all(abs(w) == expected_abs for w in nonzero)

    # Every nonzero squared coefficient is exactly 2^{-2m}; hence H=2m.
    denom = 1 << (s + m)
    assert expected_abs * (1 << m) == denom

    # Physical x-row influences: a nonzero row gives 1/2.  A zero row gives
    # either 0 or 1 according to the affine x coefficient.
    infl2 = 0  # twice I_x
    for i, row in enumerate(rows):
        if row:
            infl2 += 1
        elif (avec >> i) & 1:
            infl2 += 2
    assert infl2 >= m
    return len(vals), len(nonzero)


def all_rows(s, m):
    for packed in range(1 << (s * m)):
        yield tuple((packed >> (i * m)) & ((1 << m) - 1) for i in range(s))


def main():
    instances = 0
    truth_points = 0
    spectral_atoms = 0

    # Exhaustive square theorem: all Boolean D and all invertible M, m<=3.
    square_by_m = {}
    for m in range(1, 4):
        matrices = [rows for rows in all_rows(m, m) if rank_gf2(rows, m) == m]
        cores = range(1 << (1 << m))
        count = 0
        for rows in matrices:
            for dmask in cores:
                ntruth, nspec = check_instance(m, m, rows, dmask)
                instances += 1
                count += 1
                truth_points += ntruth
                spectral_atoms += nspec
        square_by_m[m] = {"GL": len(matrices), "cores": 1 << (1 << m), "instances": count}

    # Exhaustive small rectangular cases, including affine phases.
    rectangular = 0
    for s, m in [(2, 1), (3, 1), (3, 2)]:
        matrices = [rows for rows in all_rows(s, m) if rank_gf2(rows, m) == m]
        for rows in matrices:
            for dmask in range(1 << (1 << m)):
                for avec in [0, (1 << s) - 1]:
                    ntruth, nspec = check_instance(s, m, rows, dmask, avec, (1 << m) - 1, 1)
                    instances += 1
                    rectangular += 1
                    truth_points += ntruth
                    spectral_atoms += nspec

    # Seeded larger full-column-rank cases and arbitrary cores.
    rng = Random(20261013)
    seeded = 0
    for s, m in [(4, 3), (5, 3), (5, 4)]:
        for _ in range(80):
            while True:
                rows = tuple(rng.randrange(1 << m) for _ in range(s))
                if rank_gf2(rows, m) == m:
                    break
            dmask = rng.randrange(1 << (1 << m))
            ntruth, nspec = check_instance(s, m, rows, dmask,
                                           rng.randrange(1 << s),
                                           rng.randrange(1 << m), rng.randrange(2))
            instances += 1
            seeded += 1
            truth_points += ntruth
            spectral_atoms += nspec

    # Explicit products of 1, 2, and 3 point-defect cylinders are included as
    # arbitrary D.  Check them separately to make the target family visible.
    defects = 0
    for m, blocks in [(4, [(0, 1), (2, 3)]), (6, [(0, 1), (2, 3), (4, 5)])]:
        dmask = 0
        for y in range(1 << m):
            bit = 0
            for block in blocks:
                if all(((y >> j) & 1) == 0 for j in block):
                    bit ^= 1
            dmask |= bit << y
        rows = tuple(1 << i for i in range(m))
        ntruth, nspec = check_instance(m, m, rows, dmask)
        instances += 1
        defects += 1
        truth_points += ntruth
        spectral_atoms += nspec

    print("FULL-RANK SHIELD EXACT WALSH CHECK: PASS")
    print("square exhaustive:", square_by_m)
    print("rectangular exhaustive instances:", rectangular)
    print("seeded rectangular instances:", seeded)
    print("explicit multi-defect cores:", defects)
    print("total instances:", instances)
    print("truth-table points:", truth_points)
    print("nonzero spectral atoms checked:", spectral_atoms)
    print("verified invariant: support size=2^(2m), |Walsh|=2^s, p=2^(-2m)")
    print("analytic consequences: H=2m; square U=m; I_x=m/2; retained loss<=U")


if __name__ == "__main__":
    main()
