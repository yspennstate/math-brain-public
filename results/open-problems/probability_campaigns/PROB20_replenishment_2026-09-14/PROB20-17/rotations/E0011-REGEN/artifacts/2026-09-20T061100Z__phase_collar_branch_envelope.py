#!/usr/bin/env python3
"""Exact arithmetic self-check for the P02-A/E0011 phase-collar branch envelope.

This is evidence for the accompanying immutable report, not the mathematical
argument itself.  All rates are at p=1/2, q=1.

State j records how many of the four central O shields have been consumed by
a first harmless CO hit.  Stage 0 is before the first safe internal O2 branch
mark; stage 1 is after one row/column of the side CO collar has been cleared.
The proof deliberately overcharges suspicious clocks as FATAL.
"""
from fractions import Fraction

N = 4

# Conservative shield-defect fatal envelope:
# repeated central CO (j/2) + CO at shield vacancies (j/2)
# + every O2 edge incident to a shield vacancy (<= j) = 2j.
def defect_fatal(j):
    return Fraction(2*j, 1)

def fresh(j):
    return Fraction(N-j, 2)

# Stage 1: one opposite parallel internal O2 edge completes SUCCESS at rate 1/4.
# FATAL is overcharged by:
#   3 unsafe internal O2 edges: 3/4
#   CO refill of two cleared side sites: 1
#   every O2 edge incident to either cleared side site: <= 7/4
# total fixed non-defect rate = 1/4 + 3/4 + 1 + 7/4 = 15/4.
P1 = [Fraction(0) for _ in range(N+1)]
for j in range(N, -1, -1):
    r = fresh(j)
    d = defect_fatal(j)
    denom = Fraction(15,4) + r + d
    continuation = r*P1[j+1] if j < N else 0
    P1[j] = (Fraction(1,4) + continuation)/denom

# Stage 0: all four internal O2 edges are safe first-branch clocks, total rate 1.
P0 = [Fraction(0) for _ in range(N+1)]
for j in range(N, -1, -1):
    r = fresh(j)
    d = defect_fatal(j)
    denom = Fraction(1,1) + r + d
    continuation = r*P0[j+1] if j < N else 0
    P0[j] = (P1[j] + continuation)/denom

p_inf = P0[0]
assert p_inf == Fraction(872877833, 32794659135)

# A finite-horizon conversion.  There are at most 4 fresh-defect transitions,
# one stage-0 -> stage-1 transition, and one terminal transition.  Every waiting
# rate is >=1, hence absorption time is dominated by Gamma(6,1).  At T=20,
# exp(-20) < 2^-28 (because 28 log 2 < 20), so
# P(Gamma(6,1)>20) < 2^-28 * sum_{k=0}^5 20^k/k!.
from math import factorial
T = 20
gamma_tail_rational = sum(Fraction(T**k, factorial(k)) for k in range(6))/2**28
assert gamma_tail_rational == Fraction(104663, 805306368)
p_T = p_inf - gamma_tail_rational
assert p_T == Fraction(233167229997298013, 8803249279268290560)
assert p_T > Fraction(1, 40)  # > 0.025, a convenient clean lower bound

print("p_inf =", p_inf, "=", float(p_inf))
print("gamma6_tail_T20_upper =", gamma_tail_rational, "=", float(gamma_tail_rational))
print("p_success_by_T20_lower =", p_T, "=", float(p_T))
print("clean_lower_bound > 1/40 =", p_T > Fraction(1,40))
print("CHECKS_PASS")
