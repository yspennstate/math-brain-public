#!/usr/bin/env python3
"""Exact finite certificate for I0075 period-8 center-star frontier.

Mathematical lemma in the accompanying run report:
  in any source-valid center-star replacement pattern that already obeys the
  necessary toroidal L1-separation >=3 condition, a selected-square pair at
  displacement (±2,±1) or (±1,±2) forces a source-level stretch violation.

This script exhaustively enumerates every 8x8 torus pattern of selected unit
squares with toroidal L1 separation >=3 and density >1/8, and verifies that
all such patterns contain one of those forbidden knight-offset pairs.
No floating point is used.
"""

from collections import Counter

N = 8
MIN_COUNT = 9  # density > 1/8 on 8x8 torus


def shift(mask, n, amount):
    amount %= n
    if amount == 0:
        return mask
    return ((mask << amount) | (mask >> (n - amount))) & ((1 << n) - 1)


def row_masks_sep3(n):
    out = []
    for mask in range(1 << n):
        # Same-row toroidal distances 1 and 2 are forbidden by L1>=3.
        if mask & shift(mask, n, 1):
            continue
        if mask & shift(mask, n, 2):
            continue
        out.append(mask)
    return out


def comp_adj(r, s, n):
    # Rows one apart: horizontal cyclic differences 0, +/-1 are forbidden.
    return (r & (s | shift(s, n, 1) | shift(s, n, -1))) == 0


def openpack_patterns(n, min_count):
    """All n x n torus patterns with toroidal L1 separation >=3."""
    rows = row_masks_sep3(n)
    seq = [0] * n

    def rec(y, total):
        if y == n:
            if not comp_adj(seq[-1], seq[0], n):
                return
            # Rows at cyclic distance two: same column is forbidden.
            if (seq[-2] & seq[0]) or (seq[-1] & seq[1]):
                return
            if total >= min_count:
                mask = 0
                for yy, r in enumerate(seq):
                    mask |= r << (yy * n)
                yield mask
            return

        for r in rows:
            if y >= 1 and not comp_adj(seq[y - 1], r, n):
                continue
            if y >= 2 and (seq[y - 2] & r):
                continue
            seq[y] = r
            yield from rec(y + 1, total + r.bit_count())

    yield from rec(0, 0)


def has_knight_pair(mask, n):
    for y in range(n):
        for x in range(n):
            i = y * n + x
            if not ((mask >> i) & 1):
                continue
            for dx, dy in ((1, 2), (1, -2), (2, 1), (2, -1)):
                j = ((y + dy) % n) * n + ((x + dx) % n)
                if (mask >> j) & 1:
                    return True
    return False


def main():
    total = 0
    with_knight = 0
    weights = Counter()
    for mask in openpack_patterns(N, MIN_COUNT):
        total += 1
        weights[mask.bit_count()] += 1
        if has_knight_pair(mask, N):
            with_knight += 1
        else:
            raise AssertionError(("PERIOD8_DENSER_SURVIVOR", mask, mask.bit_count()))

    assert total == 280832, total
    assert with_knight == total
    assert weights == Counter({9: 262272, 10: 18560}), weights

    print("I0075_PERIOD8_KNIGHT_EXACT")
    print("torus_period=8x8")
    print("necessary_input_filter=toroidal_L1_separation_at_least_3")
    print("density_target=selected_count>=9 (>1/8)")
    print("enumerated_patterns=280832")
    print("weight_9_patterns=262272")
    print("weight_10_patterns=18560")
    print("patterns_containing_forbidden_knight_pair=280832")
    print("survivors_without_knight_pair=0")
    print("arithmetic=exact_integer_bitmasks_only")
    print("ALL_ASSERTIONS_PASSED")


if __name__ == "__main__":
    main()
