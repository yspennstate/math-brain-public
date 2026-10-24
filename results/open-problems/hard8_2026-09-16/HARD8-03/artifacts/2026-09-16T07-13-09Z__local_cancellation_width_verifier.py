"""Exact/reproducible verifier for HARD8-03 checkpoint 2026-09-16T07:13:09Z.

Checks three claims from the accompanying report:

1. The constructive local-cancellation-width positivization theorem on thousands
   of deterministic pseudorandom Boolean signed rectangle decompositions.
2. The infinite pair-sum family M_p for p=1,...,6: exact rational rank,
   exact classification/count of maximal dissociated column sets, and the
   predicted one-full-pair structure.
3. The rank-4 six-vector example {3,5,6,7,11,12} has optimal local negative
   width 2 over all maximal dissociated subsets.

All matrix arithmetic used for ranks is exact (fractions.Fraction); all
subset-sum and {-1,0,1}-representation checks are integer arithmetic.
"""

from collections import defaultdict
from fractions import Fraction
from itertools import combinations, product
import math
import random


def bits(v, r):
    return tuple((v >> i) & 1 for i in range(r))


def rank_fraction(cols, r):
    """Exact real rank of columns with rational/integer entries."""
    A = [[Fraction(cols[j][i]) for j in range(len(cols))] for i in range(r)]
    rr = 0
    for c in range(len(cols)):
        piv = next((i for i in range(rr, r) if A[i][c] != 0), None)
        if piv is None:
            continue
        A[rr], A[piv] = A[piv], A[rr]
        pv = A[rr][c]
        A[rr] = [x / pv for x in A[rr]]
        for i in range(r):
            if i != rr and A[i][c] != 0:
                f = A[i][c]
                A[i] = [x - f * y for x, y in zip(A[i], A[rr])]
        rr += 1
        if rr == r:
            break
    return rr


def dissociated(cols):
    """HLS independence: all subset sums are distinct."""
    if not cols:
        return True
    r = len(cols[0])
    sums = {(0,) * r}
    for v in cols:
        new = {tuple(a + b for a, b in zip(s, v)) for s in sums}
        if sums & new:
            return False
        sums |= new
    return True


def maximal_dissociated_subsets(ids, r):
    vec = [bits(v, r) for v in ids]
    out = []
    n = len(ids)
    for mask in range(1 << n):
        idx = [i for i in range(n) if (mask >> i) & 1]
        S = [vec[i] for i in idx]
        if not dissociated(S):
            continue
        maximal = True
        for i in range(n):
            if not ((mask >> i) & 1) and dissociated(S + [vec[i]]):
                maximal = False
                break
        if maximal:
            out.append(tuple(idx))
    return out


def pair_sum_family(p):
    """Return r, column masks, and equal-sum pairs for M_p."""
    r = p + 2
    e = [1 << i for i in range(p)]
    g = 1 << p
    f = 1 << (p + 1)
    h = g + sum(e)
    s = [h - e[i] for i in range(p)]
    t = [f + e[i] for i in range(p)]
    ids = [h, f]
    pairs = [(h, f)]
    for i in range(p):
        ids += [s[i], t[i]]
        pairs.append((s[i], t[i]))
    return r, ids, pairs


def verify_pair_sum_family(max_p=6):
    for p in range(1, max_p + 1):
        r, ids, pairs = pair_sum_family(p)
        cols = [bits(v, r) for v in ids]
        assert rank_fraction(cols, r) == r

        # All pair sums are equal, exactly as in the proof.
        pair_sums = {
            tuple(a + b for a, b in zip(bits(u, r), bits(v, r)))
            for u, v in pairs
        }
        assert len(pair_sums) == 1

        maximal = maximal_dissociated_subsets(ids, r)
        expected_count = (p + 1) * (2 ** p)
        assert len(maximal) == expected_count

        for Sidx in maximal:
            Sids = {ids[i] for i in Sidx}
            full = sum(1 for a, b in pairs if a in Sids and b in Sids)
            singleton = sum(1 for a, b in pairs if (a in Sids) ^ (b in Sids))
            empty = sum(1 for a, b in pairs if a not in Sids and b not in Sids)
            assert full == 1
            assert singleton == p
            assert empty == 0
            assert len(Sidx) == r

        print(
            f"PAIR_FAMILY p={p} r={r}: rank={r}, "
            f"maximal_dissociated={len(maximal)}={expected_count} VERIFIED"
        )


def rectangle_cells(rect, nr, nc):
    rmask, cmask = rect
    return {
        (x, y)
        for x in range(nr)
        if (rmask >> x) & 1
        for y in range(nc)
        if (cmask >> y) & 1
    }


def signed_matrix(pos, neg, nr, nc):
    M = [[0] * nc for _ in range(nr)]
    for rect in pos:
        for x, y in rectangle_cells(rect, nr, nc):
            M[x][y] += 1
    for rect in neg:
        for x, y in rectangle_cells(rect, nr, nc):
            M[x][y] -= 1
    return M


def local_width_partition(pos, neg, nr, nc):
    """Construct the disjoint 1-rectangle partition from Theorem 3.1."""
    a = len(pos)

    # Group columns by the complete set of negative right supports containing y.
    patterns = defaultdict(list)
    for y in range(nc):
        B = tuple(j for j, (_rm, cm) in enumerate(neg) if (cm >> y) & 1)
        patterns[B].append(y)

    pieces = []
    for B, ys in patterns.items():
        row_levels = defaultdict(list)
        for x in range(nr):
            ell = sum((neg[j][0] >> x) & 1 for j in B)
            row_levels[ell].append(x)

        for ell, xs in row_levels.items():
            for I in combinations(range(a), ell + 1):
                rows = [x for x in xs if all((pos[i][0] >> x) & 1 for i in I)]
                cols = [y for y in ys if all((pos[i][1] >> y) & 1 for i in I)]
                if rows and cols:
                    pieces.append((tuple(rows), tuple(cols)))
    return pieces


def verify_local_width_theorem(trials=30000, seed=20260916):
    rng = random.Random(seed)
    accepted = 0
    nr, nc = 4, 5

    def randrect():
        return rng.randint(1, (1 << nr) - 1), rng.randint(1, (1 << nc) - 1)

    for _ in range(trials):
        a = rng.randint(1, 4)
        b = rng.randint(0, 3)
        pos = [randrect() for _ in range(a)]
        neg = [randrect() for _ in range(b)]
        M = signed_matrix(pos, neg, nr, nc)
        if any(v not in (0, 1) for row in M for v in row):
            continue

        accepted += 1
        pieces = local_width_partition(pos, neg, nr, nc)
        cover = [[0] * nc for _ in range(nr)]
        for rows, cols in pieces:
            for x in rows:
                for y in cols:
                    cover[x][y] += 1
        assert cover == M

        kappa_y = max(
            (sum((cm >> y) & 1 for _rm, cm in neg) for y in range(nc)),
            default=0,
        )
        bound = sum(
            math.comb(b, q)
            * sum(
                math.comb(a, ell + 1) if ell + 1 <= a else 0
                for ell in range(q + 1)
            )
            for q in range(kappa_y + 1)
        )
        assert len(pieces) <= bound

    assert accepted >= 2500  # deterministic seed currently gives 3024
    print(
        f"LOCAL_WIDTH theorem: {accepted} Boolean signed decompositions "
        f"verified from {trials} deterministic trials"
    )


def representation_min_negative(Aids, r, Sidx):
    Avec = [bits(v, r) for v in Aids]
    S = [Avec[i] for i in Sidx]
    best = defaultdict(lambda: 10 ** 9)
    witness = {}
    for coeff in product((-1, 0, 1), repeat=len(S)):
        out = tuple(sum(coeff[j] * S[j][d] for j in range(len(S))) for d in range(r))
        if not all(x in (0, 1) for x in out):
            continue
        oid = sum(out[d] << d for d in range(r))
        neg = sum(c == -1 for c in coeff)
        if neg < best[oid]:
            best[oid] = neg
            witness[oid] = coeff
    return best, witness


def verify_rank4_width2_example():
    r = 4
    Aids = [3, 5, 6, 7, 11, 12]
    maximal = maximal_dissociated_subsets(Aids, r)
    optimum = 10 ** 9
    optimum_data = None

    for Sidx in maximal:
        best, witness = representation_min_negative(Aids, r, Sidx)
        width = max(best[v] for v in Aids)
        if width < optimum:
            optimum = width
            optimum_data = (Sidx, best, witness)

    assert optimum == 2
    Sidx, best, witness = optimum_data
    Sids = [Aids[i] for i in Sidx]
    assert Sids == [3, 5, 6, 7, 11]
    assert best[12] == 2
    # One optimal representation is 12 = -3 + 5 + 6 - 7 + 11.
    assert witness[12] in [(-1, 1, 1, -1, 1)]

    print(
        "RANK4 local-width obstruction: A={3,5,6,7,11,12}, "
        "optimal width=2 VERIFIED"
    )


def main():
    verify_pair_sum_family(max_p=6)
    verify_rank4_width2_example()
    verify_local_width_theorem()
    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    main()
