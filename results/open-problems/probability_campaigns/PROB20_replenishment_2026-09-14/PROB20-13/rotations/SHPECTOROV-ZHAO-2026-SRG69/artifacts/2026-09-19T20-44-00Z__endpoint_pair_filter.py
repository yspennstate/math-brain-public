#!/usr/bin/env python3
"""Exact integer checker for the local endpoint-multiplicity Cauchy filter.

For a hypothetical rooted local graph L (7-regular on 20 vertices), let
  a = mult_L(5), b = mult_L(-3), r = 19-a-b.
The remaining r eigenvalues have
  sum  = -7 - 5a + 3b,
  sum2 = 91 - 25a - 9b.
Cauchy requires r*sum2 >= sum^2 and sum2 >= 0.
This script exhausts nonnegative integer (a,b) and records the survivors.
"""

survivors = []
for a in range(20):
    for b in range(20):
        r = 19 - a - b
        if r <= 0:
            continue
        s1 = -7 - 5*a + 3*b
        s2 = 91 - 25*a - 9*b
        if s2 < 0:
            continue
        slack = r*s2 - s1*s1
        if slack >= 0:
            survivors.append((a,b,r,s1,s2,slack))

expected = (
    [(0,b) for b in range(8)]
    + [(1,b) for b in range(7)]
    + [(2,b) for b in range(5)]
)
assert [(a,b) for a,b,*_ in survivors] == expected
assert len(survivors) == 20
assert max(a for a,b,*_ in survivors) == 2
assert max(b for a,b,*_ in survivors) == 7

print("SRG69 exact endpoint-multiplicity filter")
print("formula_slack = 4*(16*a*b - 159*a - 55*b + 420)")
print("survivor_count =", len(survivors))
for row in survivors:
    print("a=%d b=%d r=%d s1=%d s2=%d cauchy_slack=%d" % row)
print("max_mult_L_5 = 2")
print("max_mult_L_minus3 = 7")
print("implied_residual_Gram_rank_max = 10")
print("ALL_EXACT_CHECKS_PASS")
