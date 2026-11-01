#!/usr/bin/env python3
"""Exact checksum for the persistent degree-5 Hamming-layer relaxation witness.

The universal n>=12 persistence is proved in the accompanying written artifact
by degree elevation / averaging over 12-coordinate restrictions.  This script
checks the seed n=12 profile exactly and, as a redundant finite checksum only,
checks its integer Newton constraints for 12<=n<=80.
"""

from fractions import Fraction
from math import comb

u = [1, -3, 24, -76, 90, -36]


def b(n, k):
    return sum(u[j] * comb(n - j, k - j) for j in range(6) if j <= k)


def objective():
    return -(
        Fraction(u[1])
        + Fraction(u[2])
        + Fraction(3, 4) * u[3]
        + Fraction(1, 2) * u[4]
        + Fraction(5, 16) * u[5]
    )

seed = [b(12, k) for k in range(13)]
expected = [1, 9, 57, 219, 486, 630, 462, 162, 9, 1, 9, 3, 0]
assert seed == expected
assert objective() == Fraction(9, 4)
assert sum(seed) == 2048
assert all(0 <= seed[k] <= comb(12, k) for k in range(13))
assert all(seed[12-k] == comb(12, k) - seed[k] for k in range(13))

for n in range(12, 81):
    assert all(0 <= b(n, k) <= comb(n, k) for k in range(n + 1))

print("P0169 d=5 persistent layer-relaxation witness")
print("arithmetic=integer/Fraction; floating_point=False")
print("u", u)
print("objective", objective())
print("n12_b", seed)
print("n12_caps", [comb(12, k) for k in range(13)])
print("n12_total_positive_count", sum(seed))
print("antipodal_layer_complementarity", True)
print("finite_checksum_n_range", "12..80")
print("UNIVERSAL_PERSISTENCE_REQUIRES_WRITTEN_DEGREE_ELEVATION_PROOF")
print("ASSERTIONS_PASS")
