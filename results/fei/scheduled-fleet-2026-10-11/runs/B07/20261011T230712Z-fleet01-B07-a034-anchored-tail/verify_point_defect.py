#!/usr/bin/env python3
from fractions import Fraction

checks = 0
for k in range(1, 65):
    delta = Fraction(1, 1 << k)
    p0 = (1 - 2 * delta) ** 2
    small = 4 * delta * delta
    count = (1 << k) - 1
    assert p0 + count * small == 1
    checks += 1
    influence = small * k * (1 << (k - 1))
    assert influence == 2 * k * delta
    checks += 1
    if k >= 2:
        epsilon = count * small
        assert epsilon == 4 * delta * (1 - delta)
        assert epsilon <= 4 * delta
        checks += 2
    if k >= 3:
        # The analytic proof uses log2(e)<3/2 and
        # -log2(1-delta)<=3delta.  The remaining rational margin is exact.
        assert Fraction(3, 2) + k - 2 + 3 * delta < k
        assert 2 * k * (4 * delta) == 4 * influence
        checks += 2

print(f"PASS: {checks} exact rational assertions for k=1,...,64")
print("The logarithmic inequalities and all-k entropy bound are proved analytically in CONDITIONAL_PHASE_THEOREM.tex")
