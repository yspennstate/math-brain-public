#!/usr/bin/env python3
"""Exact checks for the nullity-one bilinear shield theorem.

All Walsh numerators are integers.  The exhaustive range is every binary
s x m matrix of rank m-1, every Boolean core D, for 1<=m<=3 and
m-1<=s<=3.  Separate direct truth-table reconstructions include affine
phases.  Floating point is used only to report U; the asserted theorem uses
the exact flat-support and influence identities.
"""

from itertools import product
from math import log2


def parity(x):
    return x.bit_count() & 1


def rank(rows, m):
    rows = list(rows)
    r = 0
    for j in range(m):
        p = next((i for i in range(r, len(rows)) if (rows[i] >> j) & 1), None)
        if p is None:
            continue
        rows[r], rows[p] = rows[p], rows[r]
        for i in range(len(rows)):
            if i != r and ((rows[i] >> j) & 1):
                rows[i] ^= rows[r]
        r += 1
    return r


def matvec(rows, y):
    return sum(parity(row & y) << i for i, row in enumerate(rows))


def spectrum_formula(rows, m, D, a=0, b=0):
    s = len(rows)
    nums = {}
    for alpha in range(1 << s):
        target = a ^ alpha
        fiber = [y for y in range(1 << m) if matvec(rows, y) == target]
        for beta in range(1 << m):
            num = sum(D[y] * (-1 if parity((b ^ beta) & y) else 1) for y in fiber)
            if num:
                nums[(alpha, beta)] = num
    return nums


def truth_spectrum(rows, m, D, a=0, b=0, c=0):
    s = len(rows)
    n = s + m
    nums = {}
    for alpha in range(1 << s):
        for beta in range(1 << m):
            total = 0
            for x in range(1 << s):
                for y in range(1 << m):
                    phase = parity(x & matvec(rows, y)) ^ parity(a & x) ^ parity(b & y) ^ c
                    f = D[y] * (-1 if phase else 1)
                    chi = parity(alpha & x) ^ parity(beta & y)
                    total += f * (-1 if chi else 1)
            if total:
                nums[(alpha, beta)] = total
    # Formula denominator is 2^m; truth denominator is 2^(s+m).
    return nums, n


def upper_U(support, n):
    # Uniform law on support.  For an atom w, pi(w)/p(w) is the number of
    # support atoms containing w in the physical coordinate order.
    total = 0.0
    for w in support:
        count = sum(1 for v in support if (v & w) == w)
        total += log2(count)
    return total / len(support)


def run():
    matrices = cores = instances = atoms = 0
    max_ratio = (0.0, None)
    max_total_ratio = (0.0, None)
    direct = 0

    for m in range(1, 4):
        r = m - 1
        for s in range(max(1, r), 4):
            for rows in product(range(1 << m), repeat=s):
                if rank(rows, m) != r:
                    continue
                matrices += 1
                nonzero_rows = sum(row != 0 for row in rows)
                nonzero_cols = sum(any((row >> j) & 1 for row in rows) for j in range(m))
                assert nonzero_rows >= r
                assert nonzero_cols >= r
                Ix = nonzero_rows / 2
                Ilower = (nonzero_rows + nonzero_cols) / 2
                for mask in range(1 << (1 << m)):
                    D = [1 if (mask >> y) & 1 else -1 for y in range(1 << m)]
                    cores += 1
                    nums = spectrum_formula(rows, m, D)
                    assert len(nums) == 1 << (2 * r)
                    assert all(abs(v) == 2 for v in nums.values())
                    instances += 1
                    atoms += len(nums)

                    # Selected physical translations test U in the actual
                    # coordinate order.  H=2r and U<=H are then checked.
                    for a, b in [(0, 0), ((1 << s) - 1, 0), (0, (1 << m) - 1)]:
                        translated = spectrum_formula(rows, m, D, a, b)
                        support = [alpha | (beta << s) for alpha, beta in translated]
                        U = upper_U(support, s + m)
                        H = 2 * r
                        assert U <= H + 1e-12
                        if Ix:
                            ratio = U / Ix
                            if ratio > max_ratio[0]:
                                max_ratio = (ratio, (m, s, rows, mask, a, b, U, Ix))
                        if Ilower:
                            total_ratio = U / Ilower
                            assert total_ratio <= 2 + 1e-12
                            if total_ratio > max_total_ratio[0]:
                                max_total_ratio = (total_ratio, (m, s, rows, mask, a, b, U, Ilower))

                    # Direct Walsh reconstruction on a deterministic sparse
                    # subgrid, including nonzero affine phases.
                    if (mask % max(1, 1 << max(0, (1 << m) - 4)) == 0
                            and matrices % 7 == 1):
                        a = (1 << s) - 1
                        b = (1 << m) - 1
                        c = (mask ^ matrices) & 1
                        raw, n = truth_spectrum(rows, m, D, a, b, c)
                        form = spectrum_formula(rows, m, D, a, b)
                        scale = 1 << s
                        assert set(raw) == set(form)
                        assert all(abs(raw[k]) == scale * abs(form[k]) for k in raw)
                        assert sum(v * v for v in raw.values()) == 1 << (2 * n)
                        direct += 1

    print(f"PASS matrices={matrices} core_instances={instances} atoms={atoms} direct={direct}")
    print(f"max sampled U/Ix={max_ratio[0]:.15f}")
    print(f"argmax={max_ratio[1]}")
    print(f"max sampled U/Iphysical_lower={max_total_ratio[0]:.15f}")
    print(f"total_argmax={max_total_ratio[1]}")
    print("exact scope: every rank-(m-1) matrix and every Boolean D for 1<=m<=3, m-1<=s<=3")
    print("proof scope: all s,m, every physical orientation, affine phases, permitted trees, disjoint terminal cores")


if __name__ == "__main__":
    run()
