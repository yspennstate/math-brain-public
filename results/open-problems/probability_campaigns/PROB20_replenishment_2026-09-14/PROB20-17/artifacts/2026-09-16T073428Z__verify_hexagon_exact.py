#!/usr/bin/env python3
"""Exact finite enumeration for the six-direction rank-one certificate.

Vertices are Z/6Z.  Nonzero absolute overlaps have cyclic distance 1
(weight sqrt(3)/2) or 2 (weight 1/2); cyclic distance 3 has weight zero.
The script counts Hamiltonian permutations by the number of distance-1 and
 distance-2 edges.  The report turns these integer counts into an exact
closed form.
"""

import itertools
from collections import Counter
from math import sqrt

n = 6
counts = Counter()
zero = 0

for sigma in itertools.permutations(range(n)):
    k1 = 0
    k2 = 0
    good = True
    for r in range(n - 1):
        d = abs(sigma[r] - sigma[r + 1])
        d = min(d, n - d)
        if d == 3:
            good = False
            break
        if d == 1:
            k1 += 1
        elif d == 2:
            k2 += 1
        else:
            raise AssertionError("unexpected cyclic distance")
    if good:
        counts[(k1, k2)] += 1
    else:
        zero += 1

expected = {
    (5, 0): 12,
    (4, 1): 24,
    (3, 2): 84,
    (2, 3): 72,
    (1, 4): 48,
}
assert counts == expected
assert sum(counts.values()) == 240
assert zero == 480
assert sum(counts.values()) + zero == 720

alpha = sqrt(3.0) / 2.0
beta = 0.5
h6 = sum(c * alpha**k1 * beta**k2 for (k1, k2), c in counts.items()) / 720.0
h6_closed = 3.0 / 160.0 + 17.0 * sqrt(3.0) / 960.0
mu = (2.0 + sqrt(3.0)) / 6.0

assert abs(h6 - h6_closed) < 1e-15
assert h6 > 1.0 / 32.0
assert h6 < mu**5

# The prior SDP optimum is Delta=1/2.  A feasible circulant minorant has
# first row (1, 3/4, 1/4, 0, 1/4, 3/4), whose Fourier eigenvalues are
# 3, 3/2, 0, 0, 0, 3/2.  The report gives the short analytic upper bound
# Delta<=1/2 from the k=2 Fourier mode.

print("counts=" + repr(dict(sorted(counts.items(), reverse=True))))
print(f"zero_paths={zero}")
print(f"H6={h6:.16g}")
print(f"Delta5={1/32:.16g}")
print(f"mu={mu:.16g}")
print(f"mu5={mu**5:.16g}")
print(f"H6_minus_Delta5={h6-1/32:.16g}")
print(f"mu5_minus_H6={mu**5-h6:.16g}")
