import os
"""Cross-check the profile calculus against Corollary 5.2/5.3: for a
k-pair core the normalised volume (k+1)! p must be an integer, and by the
parity refinement it must be EVEN.  Test every volume the grammar class
produces up to twelve pairs - these are computed by polynomial integration,
never by the polytope engine, so agreement is a genuine cross-check of an
independently derived calculus against a proved theorem."""
import sys
from fractions import Fraction as Fr
from math import factorial
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "verify"))
from grammar_max import pmul, pint01, cycle_poly, profiles

memo = {}
def reduced(r):
    out = set()
    if r >= 2: out.add(cycle_poly(r))
    for a in range(2, r-1):
        b = r-a
        if b < 2: continue
        for pa in profiles(a, memo):
            for pb in profiles(b, memo):
                out.add(tuple(pmul(list(pa), list(pb))))
    return out

bad_int = bad_even = tot = 0
for r in range(2, 13):
    for p in reduced(r):
        v = pint01(list(p))
        nv = factorial(r+1) * v
        tot += 1
        if nv.denominator != 1:
            bad_int += 1
            if bad_int <= 3: print(f"  NON-INTEGER r={r}: {v} -> {nv}")
        elif int(nv) % 2 != 0:
            bad_even += 1
            if bad_even <= 3: print(f"  ODD r={r}: {v} -> {int(nv)}")
print(f"checked {tot} grammar volumes for r = 2..12")
print(f"non-integer normalised volumes: {bad_int}")
print(f"odd normalised volumes: {bad_even}")
print("examples:", [(r, str(pint01(list(p))), int(factorial(r+1)*pint01(list(p))))
                    for r in (5, 6, 8) for p in list(reduced(r))[:1]])
