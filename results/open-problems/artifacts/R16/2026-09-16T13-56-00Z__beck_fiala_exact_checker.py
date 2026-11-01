#!/usr/bin/env python3
"""
R16 Beck-Fiala exact finite checker, 2026-09-16.

Exact-arithmetic checks:
  1. R_t = 6 t!/t^t sum_{r=0}^{t-1} t^r/r! agrees with the equivalent
     integration-by-parts finite sum.
  2. Integerized bound b_var(t)=ceil(R_t)-1 and the Bednarchak-Helm
     all-t baseline b_lin(t)=2t-3 for t>=3 (plus t=1,2 cases).
  3. The first t where b_var strictly beats b_lin is t=16.
  4. Exact exhaustive counterexample search, modulo column permutations,
     for every 4 x n 0/1 matrix with n<=6 and column support <=t,
     t=1,2,3,4. Report worst possible discrepancy.
  5. Exact monotonicity of the finite values R_t for t<=200
     (the analytic all-t proof uses conditional Jensen, not this check).

No floating-point computation is used for the certified claims below.
"""

from fractions import Fraction
from itertools import product, combinations_with_replacement
from math import factorial

def ceil_frac(x: Fraction) -> int:
    return -((-x.numerator)//x.denominator)

def R(t: int) -> Fraction:
    assert t >= 1
    return Fraction(6*factorial(t), t**t) * sum(
        Fraction(t**r, factorial(r)) for r in range(t)
    )

def R_alt(t: int) -> Fraction:
    # 3*pi E|S_t| after integration by parts and polynomial expansion:
    # 6 * sum_{r=0}^{t-1} (t-1)! / ((t-1-r)! t^r).
    return 6 * sum(
        Fraction(factorial(t-1), factorial(t-1-r) * t**r)
        for r in range(t)
    )

for t in range(1,201):
    assert R(t) == R_alt(t)
print("exact_radius_formula_t_1_200=PASS")

for t in range(1,200):
    assert R(t+1) >= R(t)
print("exact_radius_monotonicity_t_1_200=PASS")

def b_var(t: int) -> int:
    return ceil_frac(R(t)) - 1

def b_linear(t: int) -> int:
    if t == 1:
        return 1
    if t == 2:
        return 2  # Beck-Fiala 2t-2
    return 2*t - 3  # Bednarchak-Helm, t>=3

cross = [t for t in range(1,201) if b_var(t) < b_linear(t)]
assert cross and cross[0] == 16
print("first_integerized_variation_improvement_over_linear=16")
print("t,R_t,b_var,b_linear,b_combined")
for t in range(1,31):
    print(t, f"{R(t).numerator}/{R(t).denominator}",
          b_var(t), b_linear(t), min(b_var(t), b_linear(t)))

def min_disc_for_columns(cols, m):
    n = len(cols)
    best = None
    for signs in product((-1,1), repeat=n):
        row_sums = [0]*m
        for j,c in enumerate(cols):
            sj=signs[j]
            for i in range(m):
                row_sums[i] += sj*c[i]
        d=max(abs(z) for z in row_sums) if m else 0
        if best is None or d < best:
            best=d
            if best == 0:
                break
    return best

def exhaustive_worst(m, nmax, t):
    types = [
        bits for bits in product((0,1), repeat=m)
        if 1 <= sum(bits) <= t
    ]
    worst=-1
    witness=None
    witness_n=None
    checked=0
    for n in range(1,nmax+1):
        for inds in combinations_with_replacement(range(len(types)), n):
            cols=[types[i] for i in inds]
            d=min_disc_for_columns(cols,m)
            checked += 1
            if d>worst:
                worst=d
                witness=cols
                witness_n=n
    return worst,witness_n,witness,checked

expected={1:1,2:2,3:2,4:2}
for t in range(1,5):
    w,wn,wit,count=exhaustive_worst(4,6,t)
    assert w == expected[t]
    print(f"exhaustive_m4_nle6_t{t}: worst={w}; checked_multisets={count}; witness_n={wn}; witness={wit}")

print("ALL_EXACT_CHECKS_PASS")
