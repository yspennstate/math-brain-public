#!/usr/bin/env python3
"""Exact finite diagnostic for B13 two-block Boolean interaction inequality.

Enumerates Boolean functions modulo global output sign for n<=4, all nontrivial
coordinate bipartitions (one representative modulo A<->B), and computes the
exact ratio q/(ab), where a,b are pure-side Fourier-square masses and q is the
cross-side Fourier-square mass.

The analytic theorem is not proved by this script. The script is only a
falsification/diagnostic check.
"""

from decimal import Decimal, getcontext
from fractions import Fraction


def fwht_int(vals):
    a = list(vals)
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2 * h):
            for j in range(i, i + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    return a


def exact_min_ratio(n):
    N = 1 << n
    full = (1 << n) - 1
    parts = [A for A in range(1, full) if A & 1]
    min_ratio = None
    checked = 0

    # Fix f(0)=-1 to quotient by global output sign.
    for bits in range(1 << (N - 1)):
        vals = [-1] + [1 if (bits >> (i - 1)) & 1 else -1
                       for i in range(1, N)]
        W = fwht_int(vals)
        sq = [w * w for w in W]  # common N^{-2} normalization cancels below

        for A in parts:
            B = full ^ A
            aa = bb = qq = 0
            for S, wsq in enumerate(sq):
                if S == 0 or wsq == 0:
                    continue
                hit_a = bool(S & A)
                hit_b = bool(S & B)
                if hit_a and hit_b:
                    qq += wsq
                elif hit_a:
                    aa += wsq
                elif hit_b:
                    bb += wsq

            if aa and bb:
                checked += 1
                ratio = Fraction(qq * N * N, aa * bb)
                if min_ratio is None or ratio < min_ratio:
                    min_ratio = ratio

    return checked, min_ratio


def main():
    getcontext().prec = 60
    gamma = ((Decimal(17).sqrt() - Decimal(3)) / Decimal(4)) ** 2
    print("gamma =", gamma)
    total = 0
    for n in (2, 3, 4):
        checked, ratio = exact_min_ratio(n)
        total += checked
        ratio_dec = Decimal(ratio.numerator) / Decimal(ratio.denominator)
        ok = ratio_dec >= gamma
        print(
            f"n={n} checked={checked} min_ratio={ratio.numerator}/{ratio.denominator} "
            f"decimal={ratio_dec} theorem_ok={ok}"
        )
        assert ok
    print("total_nontrivial_block_cases =", total)
    print("violations = 0")


if __name__ == "__main__":
    main()
