#!/usr/bin/env python3
"""Corrected exact-arithmetic self-check for the P02-A/E0011 phase-collar branch envelope.

Correction relative to the earlier 061100Z scratch artifact: after a horizontal
first internal O2 branch mark the two cleared side targets are not adjacent, so
the union of their incident edge sets can have 8 (not 7) edges.  This file uses
the uniform source-honest upper bound 8/4 = 2 for those O2 clocks.
"""
from fractions import Fraction
from math import factorial

N = 4

def fresh(j):
    return Fraction(N-j, 2)

# repeated central CO j/2 + CO at consumed-shield vacancies j/2
# + at most 4j O2 edges incident to those vacancies at rate 1/4
def defect_fatal(j):
    return Fraction(2*j, 1)

# Stage 1.  Rates deliberately overcharged as FATAL:
# success: opposite parallel central edge, 1/4
# other central O2: 3/4
# CO refills at two cleared side targets: 1
# O2 edges incident to the two cleared side targets: <= 8/4 = 2
# plus defect_fatal(j); fresh first central CO hits remain safe.
P1 = [Fraction(0) for _ in range(N+1)]
for j in range(N, -1, -1):
    r = fresh(j)
    d = defect_fatal(j)
    total_fixed = Fraction(1,4) + Fraction(3,4) + Fraction(1,1) + Fraction(2,1)
    continuation = r*P1[j+1] if j < N else 0
    P1[j] = (Fraction(1,4) + continuation)/(total_fixed + r + d)

# Stage 0.  Every one of the four internal central O2 edges is a safe first
# branch edge, total rate 1.  First central CO hits consume their O shield but
# leave the central site vacant; later suspicious events are in defect_fatal.
P0 = [Fraction(0) for _ in range(N+1)]
for j in range(N, -1, -1):
    r = fresh(j)
    d = defect_fatal(j)
    continuation = r*P0[j+1] if j < N else 0
    P0[j] = (P1[j] + continuation)/(Fraction(1,1) + r + d)

p_inf = P0[0]
assert p_inf == Fraction(6215, 244944)

# Finite horizon T=20.  Across both stages there are at most four fresh-defect
# transitions, one stage transition and one terminal transition.  Each waiting
# rate is at least 1, so the absorption time is dominated by Gamma(6,1).
# exp(-20)<2^-28, hence the rational tail bound below.
T = 20
gamma_tail_upper = sum(Fraction(T**k, factorial(k)) for k in range(6))/2**28
assert gamma_tail_upper == Fraction(104663, 805306368)
p_T = p_inf - gamma_tail_upper
assert p_T == Fraction(103736302151, 4109478395904)
assert p_T > Fraction(1,40)

print("p_inf_lower =", p_inf, "=", float(p_inf))
print("gamma6_tail_T20_upper =", gamma_tail_upper, "=", float(gamma_tail_upper))
print("p_success_by_T20_lower =", p_T, "=", float(p_T))
print("clean_lower_bound > 1/40 =", p_T > Fraction(1,40))
print("CHECKS_PASS")
