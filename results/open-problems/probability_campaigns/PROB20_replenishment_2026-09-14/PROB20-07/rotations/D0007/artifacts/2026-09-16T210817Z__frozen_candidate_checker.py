#!/usr/bin/env python3
"""Exact arithmetic self-check for D0007's first frozen candidate.

Candidate:
    f_*(x) = (20001/2) x^20000 1_{[-1,1]}(x).
Let E=20001. Then |X| has density E*y^(E-1), so
    E[1-|X|] = 1/(E+1) = 1/20002.
The report proves analytically that any odd m-CM law supported on [-1,1]
and symmetric about 0 must satisfy E[1-|X|] >= 1/m.
Therefore every odd m < E+1 is ruled out.  The largest such odd m is E=20001.

The script also rechecks the weaker single-shell obstruction inherited from
Yin--Zhu Example 2.1, solely as a comparison with the literature route.
All decisive comparisons below use exact Python integers / fractions.
"""
from fractions import Fraction

R = 10_000
E = 2 * R + 1
M_LAST = E          # largest odd m with m < E+1
M_NEXT = E + 2      # next odd m

# Normalization of (E/2) x^(E-1) on [-1,1], E odd.
# Integral x^(E-1) = 2/E, hence coefficient E/2 normalizes exactly.
assert Fraction(E, 2) * Fraction(2, E) == 1

# Exact first absolute moment and deficiency moment.
mean_abs = Fraction(E, E + 1)
mean_def = 1 - mean_abs
assert mean_def == Fraction(1, E + 1)

# Odd-m deterministic deficiency obstruction from the report:
# m * E[1-|X|] >= 1 is necessary for m-CM.
assert M_LAST % 2 == 1
assert M_LAST * mean_def < 1
assert M_NEXT % 2 == 1
assert M_NEXT * mean_def > 1   # the *particular* deficiency obstruction stops here

# Symmetry gives 2-CM, so even dimensions are not bad for this candidate.
# The report proves the semigroup property: if m-CM and k-CM with the same
# center, then (m+k)-CM.  No extra finite arithmetic is needed for that proof.

# Secondary exact check: Yin--Zhu endpoint-tail criterion for m=2q+1.
# Criterion: (2q+1) q^E < (q+1)^E.
def shell_bad(q: int) -> bool:
    return (2*q + 1) * pow(q, E) < pow(q + 1, E)

Q_LAST = 2363
assert all(shell_bad(q) for q in range(1, Q_LAST + 1))
assert not shell_bad(Q_LAST + 1)

print("ALL EXACT D0007 FROZEN-CANDIDATE CHECKS PASSED")
print(f"candidate exponent: {E-1}")
print(f"normalizing coefficient: {E}/2")
print(f"E[|X|] = {mean_abs.numerator}/{mean_abs.denominator}")
print(f"E[1-|X|] = {mean_def.numerator}/{mean_def.denominator}")
print(f"deficiency obstruction certifies every odd m=3,5,...,{M_LAST} as non-CM")
print(f"N_bad(F_*) after this report = {M_LAST}")
print(f"at next odd m={M_NEXT}, m*E[1-|X|] = {(M_NEXT*mean_def).numerator}/{(M_NEXT*mean_def).denominator} > 1")
print(f"weaker endpoint-tail obstruction stops after odd m={2*Q_LAST+1}")
