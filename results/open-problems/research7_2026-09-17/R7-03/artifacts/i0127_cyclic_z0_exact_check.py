#!/usr/bin/env python3
"""Exact finite check for the vertex-transitive/cyclic z=0 SSNC boundary.

A vertex-transitive hypothetical z=0 counterexample on 19 vertices has a
regular C_19 subgroup.  After identifying V with Z/19Z, its two missing
neighbours are +/-h and its eight out-steps choose exactly one member from
each remaining opposite pair +/-d.  This script exhausts all 9*2^8 = 2304
such oriented circulants and computes the exact second out-neighbourhood of
0.  Only integer modular arithmetic is used.
"""

from collections import Counter
from itertools import product

P = 19
counts = Counter()
minimum = P
minimum_cases = []
case_count = 0

for h in range(1, 10):
    representatives = [d for d in range(1, 10) if d != h]
    assert len(representatives) == 8

    for bits in product((0, 1), repeat=8):
        S = {
            d if bit == 0 else P - d
            for d, bit in zip(representatives, bits)
        }

        # S is a skew choice from the eight nonmissing opposite pairs.
        assert len(S) == 8
        assert all(((-s) % P) not in S for s in S)
        assert h not in S and (P - h) not in S

        N2 = {
            (a + b) % P
            for a in S
            for b in S
        } - S - {0}

        second_size = len(N2)
        counts[second_size] += 1
        case_count += 1

        if second_size < minimum:
            minimum = second_size
            minimum_cases = [(h, tuple(sorted(S)))]
        elif second_size == minimum:
            minimum_cases.append((h, tuple(sorted(S))))

assert case_count == 9 * (2 ** 8) == 2304
assert minimum == 8
assert counts == Counter({8: 18, 9: 126, 10: 2160})
assert len(minimum_cases) == 18

print(f"cases={case_count}")
print(f"min_second_neighborhood={minimum}")
print("distribution={8:18,9:126,10:2160}")
print(f"minimum_case_count={len(minimum_cases)}")
print("PASS")
