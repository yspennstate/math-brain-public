"""Hankel analogue of the grammar maximum.  w_r is parity mixing exactly
for odd r; concatenation shifts by an even amount and nesting flips all
parities, so both preserve parity mixing.  The parity-mixing grammar is
therefore the same grammar restricted to ODD cycles, and by Theorem 4.1
its p_H equals its p_T."""
from fractions import Fraction as Fr
from math import comb
from functools import lru_cache

def pmul(a, b):
    out = [Fr(0)]*(len(a)+len(b)-1)
    for i,u in enumerate(a):
        if u:
            for j,v in enumerate(b):
                if v: out[i+j] += u*v
    return out

def pint01(p):
    return sum(c/(i+1) for i,c in enumerate(p))

@lru_cache(maxsize=None)
def cycle_poly(r):
    p = [Fr(0)]*(r+1)
    p[0] += Fr(2,r); p[r] -= Fr(1,r)
    for k in range(r+1):
        p[k] -= Fr(comb(r,k)*(-1)**k, r)
    return tuple(p)

def profiles(r, memo):
    if r in memo: return memo[r]
    out = set()
    if r >= 3 and r % 2 == 1:
        out.add(cycle_poly(r))
    for a in range(3, r-2):
        b = r-a
        if b < 3: continue
        for pa in profiles(a, memo):
            for pb in profiles(b, memo):
                out.add(tuple(pmul(list(pa), list(pb))))
    if r >= 4:
        for pin in profiles(r-1, memo):
            out.add((pint01(list(pin)),))
    memo[r] = out
    return out

def reduced(r, memo):
    out = set()
    if r >= 3 and r % 2 == 1:
        out.add(cycle_poly(r))
    for a in range(3, r-2):
        b = r-a
        if b < 3: continue
        for pa in profiles(a, memo):
            for pb in profiles(b, memo):
                out.add(tuple(pmul(list(pa), list(pb))))
    return out

memo = {}
QUARTER = Fr(1,4)
print(" r   profiles   max p_H over reduced parity-mixing words   vs 1/4")
for r in range(3, 19):
    ps = reduced(r, memo)
    if not ps:
        print(f" {r:2d}   (none)"); continue
    best = max(pint01(list(p)) for p in ps)
    flag = "= 1/4" if best == QUARTER else ("EXCEEDS 1/4 ***" if best > QUARTER else "< 1/4")
    print(f" {r:2d}   {len(ps):6d}      {str(best):<22} {flag}")
