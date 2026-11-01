#!/usr/bin/env python3
"""Exact finite self-check for the terminal Han scalar-packet handoff.

For W=1, z=0, unit (unscaled) fresh Rademacher entries and outer
2x2 deformation Q=[[0,s],[t,0]] with s,t in {+-1}, enumerate all 2^7
fresh sign configurations and verify that det=0 in exactly 80 cases.
Scaling all fresh variables by the common band normalization does not
change the existence of this finite adversarial evaluation phenomenon;
the report uses the unscaled polynomial only as an exact obstruction to
a naive coefficient-norm => pointwise anti-concentration principle.
"""
from fractions import Fraction
from itertools import product


def det3(M):
    a,b,c = M[0]
    d,e,f = M[1]
    g,h,i = M[2]
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)


def distribution(s,t):
    counts = {}
    for a,b,c,d,e,f,g in product((-1,1), repeat=7):
        M = [
            [Fraction(a), Fraction(b), Fraction(s)],
            [Fraction(c), Fraction(d), Fraction(e)],
            [Fraction(t), Fraction(f), Fraction(g)],
        ]
        D = det3(M)
        counts[D] = counts.get(D,0) + 1
    return counts


ok = True
for s,t in product((-1,1), repeat=2):
    counts = distribution(s,t)
    expected = {Fraction(-4): 24, Fraction(0): 80, Fraction(4): 24}
    good = counts == expected
    ok &= good
    print(f"s={s:+d}, t={t:+d}: {sorted(counts.items())}")
    print(f"zero_count={counts.get(Fraction(0),0)}, zero_probability={Fraction(counts.get(Fraction(0),0),128)}")
    print(f"matches_expected={good}")

print(f"ALL_EXACT_CHECKS_PASS = {ok}")
assert ok
