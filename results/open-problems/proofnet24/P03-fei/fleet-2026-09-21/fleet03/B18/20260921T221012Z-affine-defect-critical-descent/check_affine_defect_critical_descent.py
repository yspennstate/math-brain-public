#!/usr/bin/env python3
"""Exact finite checks for the affine-defect critical-descent theorem.

No third-party packages.  A codimension-c affine subspace is represented by a
full-rank c x n parity-check matrix over F_2; its columns are the quotient
images of the physical coordinate vectors.  We exhaust all such matrices for
3 <= n <= 5 and 2 <= c < n.
"""

from itertools import product
from math import log2


def rank_cols(cols, c):
    basis = [0] * c
    rank = 0
    for x in cols:
        y = x
        while y:
            b = y.bit_length() - 1
            if basis[b]:
                y ^= basis[b]
            else:
                basis[b] = y
                rank += 1
                break
    return rank


def spectral_entropy(c):
    delta = 2.0 ** (-c)
    p0 = (1.0 - 2.0 * delta) ** 2
    p = 4.0 * delta * delta
    h = 0.0
    if p0:
        h -= p0 * log2(p0)
    h -= (2**c - 1) * p * log2(p)
    return h


def ratio(c, m):
    return spectral_entropy(c) / (m * 2.0 ** (1 - c))


def main():
    full_total = 0
    redundant_total = 0
    rows = []

    for n in range(3, 6):
        for c in range(2, n):
            full = 0
            redundant = 0
            irredundant = 0
            for cols in product(range(1 << c), repeat=n):
                if rank_cols(cols, c) != c:
                    continue
                full += 1
                m = sum(x != 0 for x in cols)
                assert m >= c

                if m > c:
                    redundant += 1
                    witnesses = [
                        i
                        for i, x in enumerate(cols)
                        if x and rank_cols(cols[:i] + cols[i + 1 :], c) == c
                    ]
                    assert witnesses
                    i = witnesses[0]
                    child = cols[:i] + cols[i + 1 :]
                    assert rank_cols(child, c) == c
                    assert sum(x != 0 for x in child) == m - 1
                    # Same codimension => same spectral entropy; folded
                    # influence drops by exactly 2^(1-c).
                    parent_ratio = ratio(c, m)
                    child_ratio = ratio(c, m - 1)
                    assert abs(child_ratio / parent_ratio - m / (m - 1)) < 1e-12
                else:
                    irredundant += 1
                    nonzero = tuple(x for x in cols if x)
                    assert len(nonzero) == c
                    assert rank_cols(nonzero, c) == c

            rows.append((n, c, full, redundant, irredundant))
            full_total += full
            redundant_total += redundant

    # Floating diagnostic only; the report contains an all-c analytic proof of H < 4J.
    max_ratio = -1.0
    max_c = None
    for c in range(2, 51):
        r = ratio(c, c)
        assert r < 4.0
        if r > max_ratio:
            max_ratio, max_c = r, c

    print("PASS affine-defect critical-descent checker")
    print("exhaustive_full_rank_matrices", full_total)
    print("redundant_m_gt_c_cases", redundant_total)
    print("all_redundant_cases_have_deletable_nonzero_column", redundant_total)
    for n, c, full, redundant, irredundant in rows:
        print(
            "n=%d c=%d full=%d redundant=%d irredundant=%d"
            % (n, c, full, redundant, irredundant)
        )
    print("one_point_ratio_float_diagnostic_c=2..50")
    print("max_ratio %.15f at_c %d" % (max_ratio, max_c))


if __name__ == "__main__":
    main()
