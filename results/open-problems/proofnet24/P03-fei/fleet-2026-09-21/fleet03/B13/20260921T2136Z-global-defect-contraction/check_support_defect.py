#!/usr/bin/env python3
"""Exact finite search for local support-defect/subcube distance calibrations.

This is supporting evidence only. It enumerates every nonempty E subset of {0,1}^m
with density <= 1/2 for m <= 4, computes the constant-sign derivative depth defect

    Delta(E) = [I(1_E)-2 j log2(1/j)]/(4j),  j=|E|/2^m,

and the minimum relative symmetric-difference distance

    delta(E)=min_Q |E triangle Q|/|E|

over coordinate subcubes Q.  It tests the tempting stronger bound delta <= 2 Delta
and the weaker finite calibration delta <= 4 Delta.
"""
from itertools import product
from math import log2


def subcube_masks(m):
    n = 1 << m
    out = []
    for states in product((-1, 0, 1), repeat=m):  # -1 means free
        mask = 0
        for x in range(n):
            if all(s == -1 or ((x >> r) & 1) == s for r, s in enumerate(states)):
                mask |= 1 << x
        out.append(mask)
    return out


def influence_indicator(m, E):
    n = 1 << m
    oriented = 0
    for r in range(m):
        flip = 1 << r
        for x in range(n):
            oriented += ((E >> x) & 1) != ((E >> (x ^ flip)) & 1)
    return oriented / n


def scan(m):
    n = 1 << m
    cubes = subcube_masks(m)
    count = bad2 = bad4 = 0
    max_ratio = 0.0
    maximizer = None
    for E in range(1, 1 << n):
        size = E.bit_count()
        if size > n // 2:
            continue
        count += 1
        j = size / n
        I = influence_indicator(m, E)
        iso = I - 2 * j * log2(1 / j)
        Delta = iso / (4 * j)
        delta = min((E ^ Q).bit_count() / size for Q in cubes)
        if Delta > 1e-14:
            ratio = delta / Delta
            if ratio > max_ratio:
                max_ratio = ratio
                maximizer = (E, size, I, Delta, delta, ratio)
            if delta > 2 * Delta + 1e-12:
                bad2 += 1
            if delta > 4 * Delta + 1e-12:
                bad4 += 1
    return count, bad2, bad4, max_ratio, maximizer


def main():
    for m in range(1, 5):
        count, bad2, bad4, max_ratio, rec = scan(m)
        print(f"m={m} supports={count} bad_delta_le_2Delta={bad2} "
              f"bad_delta_le_4Delta={bad4} max_delta_over_Delta={max_ratio:.15f}")
        if rec is not None:
            E, size, I, Delta, delta, ratio = rec
            print(f"  maximizer_mask={E} size={size} I={I:.15f} "
                  f"Delta={Delta:.15f} delta={delta:.15f} ratio={ratio:.15f}")


if __name__ == "__main__":
    main()
