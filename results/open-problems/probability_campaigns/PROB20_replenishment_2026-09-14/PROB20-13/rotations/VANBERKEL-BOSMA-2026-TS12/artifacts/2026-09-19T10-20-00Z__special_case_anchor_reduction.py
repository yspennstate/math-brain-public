#!/usr/bin/env python3
"""Exact finite checker for VANBERKEL-BOSMA-2026-TS12, S_(4,6,17).

All arithmetic is exact Python-integer bitset arithmetic. No floating point,
randomness, external solver, or heuristic period detection is used.

Checks through LIMIT:
  1. direct greedy strict-3-sumfree generation;
  2. every excluded integer is represented by a strict triple containing at
     least one member of the fixed 14-element prefix anchor set A;
  3. triples containing at least two anchors do NOT suffice, quantifying the
     obstruction to a finite-shift collapse;
  4. the conspicuous candidate shift P=219526 is not an exact period on the
     first full aligned pair of P-blocks starting at 102.

These are finite facts only; they do not prove ultimate periodicity.
"""

LIMIT = 1_000_000
F, G, H = 4, 6, 17
ANCHORS = (4, 6, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 37, 38)
CANDIDATE_SHIFT = 219_526
ALIGN_START = 102


def greedy_strict3(limit: int):
    mask = (1 << (limit + 1)) - 1
    s_bits = (1 << F) | (1 << G) | (1 << H)
    vals = [F, G, H]
    pair_bits = (1 << (F + G)) | (1 << (F + H)) | (1 << (G + H))
    triple_bits = 1 << (F + G + H)

    for n in range(H + 1, limit + 1):
        if ((triple_bits >> n) & 1) == 0:
            old_s = s_bits
            triple_bits = (triple_bits | (pair_bits << n)) & mask
            pair_bits = (pair_bits | (old_s << n)) & mask
            s_bits |= 1 << n
            vals.append(n)

    return s_bits, vals, mask


def anchored_triples(vals, anchors, mask):
    """All strict triple sums <= LIMIT containing >=1 fixed anchor, exactly."""
    anchor_set = set(anchors)
    present_bits = 0
    present_set = set()
    anchor_pair_bits = 0
    triple_bits = 0

    for x in vals:
        # x is the largest member of every newly formed strict triple.
        triple_bits = (triple_bits | (anchor_pair_bits << x)) & mask

        if x in anchor_set:
            anchor_pair_bits |= present_bits << x
        else:
            for a in anchors:
                if a in present_set:
                    anchor_pair_bits |= 1 << (x + a)

        present_bits |= 1 << x
        present_set.add(x)

    return triple_bits & mask


def two_anchor_triples(s_bits, anchors, mask):
    """All strict triple sums <= LIMIT containing >=2 fixed anchors, exactly."""
    out = 0
    for i, a in enumerate(anchors):
        for b in anchors[i + 1:]:
            source = s_bits & ~(1 << a) & ~(1 << b)
            out |= (source << (a + b)) & mask
    return out


def first_positions(bits: int, count: int):
    ans = []
    while bits and len(ans) < count:
        low = bits & -bits
        ans.append(low.bit_length() - 1)
        bits ^= low
    return ans


def main():
    s_bits, vals, mask = greedy_strict3(LIMIT)
    domain = mask ^ ((1 << (H + 1)) - 1)
    excluded = (~s_bits) & mask & domain

    anchored = anchored_triples(vals, ANCHORS, mask) & domain
    missing_anchor = excluded & ~anchored
    false_anchor = anchored & s_bits

    two_anchor = two_anchor_triples(s_bits, ANCHORS, mask) & domain
    two_anchor_missing = excluded & ~two_anchor
    false_two_anchor = two_anchor & s_bits

    p = CANDIDATE_SHIFT
    start = ALIGN_START
    block_mask = (1 << p) - 1
    b0 = (s_bits >> start) & block_mask
    b1 = (s_bits >> (start + p)) & block_mask
    period_mismatch = b0 ^ b1

    print(f"LIMIT={LIMIT}")
    print(f"ACCEPTED_COUNT={len(vals)}")
    print(f"EXCLUDED_COUNT={excluded.bit_count()}")
    print(f"ANCHORS={ANCHORS}")
    print(f"ANCHOR_MISSING_COUNT={missing_anchor.bit_count()}")
    print(f"ANCHOR_FALSE_POSITIVE_COUNT={false_anchor.bit_count()}")
    print(f"TWO_ANCHOR_MISSING_COUNT={two_anchor_missing.bit_count()}")
    print(f"TWO_ANCHOR_FALSE_POSITIVE_COUNT={false_two_anchor.bit_count()}")
    print(f"TWO_ANCHOR_COVERED_COUNT={excluded.bit_count() - two_anchor_missing.bit_count()}")
    print(f"TWO_ANCHOR_COVERAGE_NUM={excluded.bit_count() - two_anchor_missing.bit_count()}")
    print(f"TWO_ANCHOR_COVERAGE_DEN={excluded.bit_count()}")
    print(f"TWO_ANCHOR_FIRST_MISSES={first_positions(two_anchor_missing, 20)}")
    print(f"CANDIDATE_SHIFT={p}")
    print(f"ALIGN_START={start}")
    print(f"SHIFT_BLOCK_MISMATCH_COUNT={period_mismatch.bit_count()}")
    print(f"SHIFT_BLOCK_FIRST_MISMATCH_OFFSETS={first_positions(period_mismatch, 20)}")

    assert missing_anchor == 0
    assert false_anchor == 0
    assert false_two_anchor == 0
    assert two_anchor_missing.bit_count() == 21401
    assert period_mismatch.bit_count() == 34
    print("ALL_EXACT_CHECKS_PASS")


if __name__ == "__main__":
    main()
