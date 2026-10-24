#!/usr/bin/env python3
"""Exact finite sanity check for P20's all-odd-m semicircle proof.

This script is supplementary only: the theorem is proved symbolically in the
canonical run report.  The script exhaustively checks every nonempty proper
subset x of Z_m for odd m <= 19 and verifies the stronger prescribed-length
witness produced by the proof:

* if |x| is odd, an interval W of length (m-1)/2;
* if |x| is even, W is the complement of an interval of length (m-1)/2,
  hence |W|=(m+1)/2.

All computations use exact integer bit masks.  No sampling is used.
"""


def interval_mask(m: int, start: int, length: int) -> int:
    mask = 0
    for j in range(length):
        mask |= 1 << ((start + j) % m)
    return mask


def construct_witness(m: int, x: int):
    assert m >= 3 and m % 2 == 1
    full = (1 << m) - 1
    assert 0 < x < full
    h = (m - 1) // 2

    if x.bit_count() % 2 == 1:
        y = x
        complement_case = False
    else:
        y = full ^ x
        complement_case = True

    s = y.bit_count()
    assert 0 < s < m and s % 2 == 1

    chosen = None
    for start in range(m):
        I = interval_mask(m, start, h)
        if 2 * (I & y).bit_count() > s:
            chosen = I
            break

    assert chosen is not None
    W = (full ^ chosen) if complement_case else chosen
    return W


def verify_one(m: int, x: int) -> None:
    W = construct_witness(m, x)
    ell = W.bit_count()
    sym = (W ^ x).bit_count()
    assert sym < min(ell, m - ell)

    h = (m - 1) // 2
    if x.bit_count() % 2 == 1:
        assert ell == h
    else:
        assert ell == h + 1


def main() -> None:
    total = 0
    for m in range(3, 20, 2):
        full = (1 << m) - 1
        checked = 0
        for x in range(1, full):
            verify_one(m, x)
            checked += 1
        total += checked
        print(f"m={m:2d} subsets={checked:7d} PRESCRIBED_LENGTH_WITNESS_PASS")

    print(f"TOTAL_SUBSETS={total}")
    print("P20-CI241-SEMICIRCLE-SANITY: ALL_EXACT_CHECKS_PASS")


if __name__ == "__main__":
    main()
