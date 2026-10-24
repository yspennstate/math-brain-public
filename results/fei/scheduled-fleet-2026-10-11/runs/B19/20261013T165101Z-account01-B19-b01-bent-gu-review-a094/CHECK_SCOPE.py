#!/usr/bin/env python3
"""Minimal scope counterexample for the overbroad bent-fiber pattern."""
from fractions import Fraction
from CHECK_INDEPENDENT import direct_walsh


def value(z):
    # x1,x2 are bits 0,1; y1,y2,y3 are bits 2,3,4.
    x1, x2 = z & 1, (z >> 1) & 1
    y = z >> 2
    y1, y2, y3 = y & 1, (y >> 1) & 1, (y >> 2) & 1
    exponent = ((x1 ^ x2) & (y1 ^ y2 ^ y3)) ^ (y1 & y2)
    return -1 if exponent else 1


def upper_u(vals):
    n = len(vals).bit_length() - 1
    w = direct_walsh(vals)
    den = len(vals) ** 2
    # The example has dyadic upper ratios; retain exact powers only.
    ans = Fraction(0)
    for s, a in enumerate(w):
        if not a:
            continue
        pnum = a * a
        pinum = sum(w[t] * w[t] for t in range(1 << n) if (t & s) == s)
        ratio = pinum // pnum
        assert pinum == ratio * pnum and ratio & (ratio - 1) == 0
        ans += Fraction(pnum, den) * (ratio.bit_length() - 1)
    return ans


def main():
    vals = [value(z) for z in range(32)]
    w = direct_walsh(vals)
    support = [a for a in w if a]
    assert len(support) == 16 and {abs(a) for a in support} == {8}
    influences = []
    for j in range(5):
        changes = sum(vals[z] != vals[z ^ (1 << j)]
                      for z in range(32) if not z & (1 << j))
        influences.append(Fraction(changes, 16))
    assert influences == [Fraction(1, 2)] * 5
    assert upper_u(vals) == Fraction(2)
    print('M rows=(111,111), rank=1=m-2; all rows and columns nonzero')
    print('each kernel-coset core is the two-bit bent phase (-1)^(y1*y2)')
    print('spectral support=16 of 32, magnitude=8: plateaued, not bent')
    print('H=4, U=2, I=5/2; thus the claimed U=I=m-1=2 is false when s>m-2')
    print('PASS')


if __name__ == '__main__':
    main()
