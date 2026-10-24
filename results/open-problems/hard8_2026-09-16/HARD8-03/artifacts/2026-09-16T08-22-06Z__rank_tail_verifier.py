"""Exact verifier for HARD8-03 checkpoint 2026-09-16T08:22:06Z.

Pure Python / standard library only.

Checks:
1. Coordinate-partition family M_{g,h}: exact real rank, maximal
   dissociated-set classification, and forced local negative widths on small
   instances.
2. Exact exhaustive ambient-dimension-4 evidence for the conjectural rank-tail
   inequality described in the report. This finite search is evidence only,
   not a proof of the general statement.
"""

from fractions import Fraction
from itertools import product, combinations


def rank_q(vectors):
    """Exact real rank of row-vectors over Q."""
    if not vectors:
        return 0
    a = [list(map(Fraction, v)) for v in vectors]
    m, n = len(a), len(a[0])
    r = c = 0
    while r < m and c < n:
        piv = next((i for i in range(r, m) if a[i][c] != 0), None)
        if piv is None:
            c += 1
            continue
        a[r], a[piv] = a[piv], a[r]
        pv = a[r][c]
        a[r] = [x / pv for x in a[r]]
        for i in range(m):
            if i != r and a[i][c] != 0:
                f = a[i][c]
                a[i] = [a[i][j] - f * a[r][j] for j in range(n)]
        r += 1
        c += 1
    return r


def coordinate_partition_columns(g, h):
    rows = list(product(range(h), repeat=g))
    cols = []
    for j in range(g):
        for k in range(h):
            cols.append(tuple(int(x[j] == k) for x in rows))
    return rows, cols


def is_dissociated(cols, indices):
    """All subset sums are distinct."""
    if not indices:
        return True
    zero = (0,) * len(cols[0])
    sums = {zero}
    for idx in indices:
        v = cols[idx]
        new = []
        for s in sums:
            t = tuple(a + b for a, b in zip(s, v))
            if t in sums:
                return False
            new.append(t)
        sums.update(new)
    return True


def maximal_dissociated_masks(cols):
    n = len(cols)
    cache = {}

    def dis(mask):
        if mask not in cache:
            idx = [i for i in range(n) if (mask >> i) & 1]
            cache[mask] = is_dissociated(cols, idx)
        return cache[mask]

    out = []
    for mask in range(1 << n):
        if not dis(mask):
            continue
        maximal = True
        for j in range(n):
            if not ((mask >> j) & 1) and dis(mask | (1 << j)):
                maximal = False
                break
        if maximal:
            out.append(mask)
    return out


def min_negative_width(cols, s_indices, target_idx):
    """Exact min # negative coefficients in {-1,0,1} representation."""
    s = [cols[i] for i in s_indices]
    target = cols[target_idx]
    m = len(s)
    d = len(target)
    for q in range(m + 1):
        for neg_positions in combinations(range(m), q):
            neg = set(neg_positions)
            base = [0] * d
            for pos in neg_positions:
                v = s[pos]
                for i, x in enumerate(v):
                    base[i] -= x
            rest = [pos for pos in range(m) if pos not in neg]
            for positive_mask in range(1 << len(rest)):
                out = base.copy()
                for bit, pos in enumerate(rest):
                    if (positive_mask >> bit) & 1:
                        v = s[pos]
                        for i, x in enumerate(v):
                            out[i] += x
                if tuple(out) == target:
                    return q
    return None


def verify_coordinate_family():
    tested = [(2, 2), (2, 3), (2, 4), (3, 2), (3, 3)]
    rows_out = []
    for g, h in tested:
        rows, cols = coordinate_partition_columns(g, h)
        r = rank_q(cols)
        expected_r = 1 + g * (h - 1)
        assert r == expected_r

        maximal = maximal_dissociated_masks(cols)
        expected_count = g * (h ** (g - 1))
        assert len(maximal) == expected_count
        assert {mask.bit_count() for mask in maximal} == {expected_r}

        widths = set()
        bad_ranks = set()
        for mask in maximal:
            sidx = [i for i in range(len(cols)) if (mask >> i) & 1]
            omitted = [i for i in range(len(cols)) if not ((mask >> i) & 1)]
            assert len(omitted) == g - 1
            for j in omitted:
                w = min_negative_width(cols, sidx, j)
                widths.add(w)
            bad_ranks.add(rank_q([cols[j] for j in omitted]))
        assert widths == {h - 1}
        assert bad_ranks == {g - 1}

        rows_out.append(
            (g, h, len(rows), len(cols), r, len(maximal), h - 1, g - 1)
        )
    return rows_out


# ---------- optimized dimension-4 exhaustive rank-tail search ----------


def v4(mask):
    return tuple((mask >> i) & 1 for i in range(4))


def subset_sum_dissociated(vectors):
    if not vectors:
        return True
    sums = {(0, 0, 0, 0)}
    for v in vectors:
        new = []
        for s in sums:
            t = (s[0] + v[0], s[1] + v[1], s[2] + v[2], s[3] + v[3])
            if t in sums:
                return False
            new.append(t)
        sums.update(new)
    return True


def exhaustive_dimension4_rank_tail():
    vecs = [v4(mask) for mask in range(1, 16)]
    n = 15

    diss = [False] * (1 << n)
    diss[0] = True
    for mask in range(1, 1 << n):
        vectors = [vecs[i] for i in range(n) if (mask >> i) & 1]
        diss[mask] = subset_sum_dissociated(vectors)

    # Every dissociated set in dimension 4 here has size <=5, so exhaustive
    # ternary representation enumeration is tiny.
    max_diss_size = max(mask.bit_count() for mask in range(1 << n) if diss[mask])
    assert max_diss_size <= 5

    tuple_to_idx = {vecs[i]: i for i in range(n)}
    repwidth = {}
    for smask in range(1 << n):
        if not diss[smask]:
            continue
        sidx = [i for i in range(n) if (smask >> i) & 1]
        s = [vecs[i] for i in sidx]
        best = [None] * n
        for coeff in product((-1, 0, 1), repeat=len(s)):
            neg = sum(c < 0 for c in coeff)
            out = [0, 0, 0, 0]
            for c, v in zip(coeff, s):
                if c:
                    out[0] += c * v[0]
                    out[1] += c * v[1]
                    out[2] += c * v[2]
                    out[3] += c * v[3]
            j = tuple_to_idx.get(tuple(out))
            if j is not None and (best[j] is None or neg < best[j]):
                best[j] = neg
        repwidth[smask] = best

    rank_cache = [0] * (1 << n)
    for mask in range(1, 1 << n):
        rank_cache[mask] = rank_q([vecs[i] for i in range(n) if (mask >> i) & 1])

    configurations = 0
    violations = []
    worst_ratio_num = 0
    worst_ratio_den = 1
    worst_record = None

    for vmask in range(1, 1 << n):
        configurations += 1
        r = rank_cache[vmask]

        maximal = []
        smask = vmask
        while True:
            if diss[smask]:
                rem = vmask & ~smask
                ok = True
                rr = rem
                while rr:
                    bit = rr & -rr
                    if diss[smask | bit]:
                        ok = False
                        break
                    rr -= bit
                if ok:
                    maximal.append(smask)
            if smask == 0:
                break
            smask = (smask - 1) & vmask

        assert maximal

        for k in (1, 2, 3):
            best_heavy_rank = 10**9
            best_smask = None
            for smask in maximal:
                widths = repwidth[smask]
                heavy = 0
                rr = vmask & ~smask
                while rr:
                    bit = rr & -rr
                    j = bit.bit_length() - 1
                    w = widths[j]
                    assert w is not None
                    if w > k:
                        heavy |= bit
                    rr -= bit
                hr = rank_cache[heavy]
                if hr < best_heavy_rank:
                    best_heavy_rank = hr
                    best_smask = smask

            if best_heavy_rank * (k + 1) > r:
                violations.append((vmask, r, k, best_heavy_rank, best_smask))
                return {
                    "configurations": configurations,
                    "violations": violations,
                    "worst": worst_record,
                }

            num = best_heavy_rank * (k + 1)
            den = r
            if num * worst_ratio_den > worst_ratio_num * den:
                worst_ratio_num, worst_ratio_den = num, den
                worst_record = (vmask, r, k, best_heavy_rank, best_smask)

    return {
        "configurations": configurations,
        "violations": violations,
        "worst_ratio": (worst_ratio_num, worst_ratio_den),
        "worst": worst_record,
    }


def main():
    family = verify_coordinate_family()
    print("Coordinate-partition exact checks:")
    for row in family:
        print(
            "g=%d h=%d rows=%d cols=%d rank=%d maximal=%d width=%d bad_rank=%d"
            % row
        )

    result = exhaustive_dimension4_rank_tail()
    print("\nDimension-4 exhaustive rank-tail search:")
    print("configurations=", result["configurations"])
    print("violations=", len(result["violations"]))
    print("worst_ratio_num_den=", result.get("worst_ratio"))
    print("worst_record=", result.get("worst"))
    assert result["configurations"] == 32767
    assert not result["violations"]


if __name__ == "__main__":
    main()
