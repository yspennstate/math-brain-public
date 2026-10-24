from fractions import Fraction
from functools import lru_cache
from math import ceil, sqrt

BUDGET = Fraction(1, 64)

def mmax(n):
    if n == 0:
        return 0
    return 2*n - ceil(2*sqrt(n))

# Safe combinatorial lower envelope.
L = {(0, 0): Fraction(1)}
ARG = {}
for n in range(1, 16):
    for e in range(mmax(n)+1):
        dp = {(0, 0): (Fraction(0), ())}
        for i in range(n):
            ndp = {}
            for (used, sdeg), (cost, ds) in dp.items():
                for d in range(5):
                    ep = e - d
                    if ep < 0 or ep > mmax(n-1):
                        continue
                    if (n-1, ep) not in L:
                        continue
                    key = (used+1, sdeg+d)
                    cand = (cost + L[(n-1, ep)], ds + (d,))
                    if key not in ndp or cand[0] < ndp[key][0]:
                        ndp[key] = cand
            dp = ndp
        key = (n, 2*e)
        if key in dp:
            c, ds = dp[key]
            L[(n,e)] = Fraction(2, 2*n+e) * c
            ARG[(n,e)] = ds

for n in range(1,16):
    vals = [L[(n,e)] for e in range(mmax(n)+1)]
    assert all(vals[i] >= vals[i+1] for i in range(len(vals)-1))

L14 = L[(14,mmax(14))]
L15 = L[(15,mmax(15))]
assert L14 > BUDGET
assert L15 < BUDGET

def qco_rect(h,w):
    cells=[(i,j) for i in range(h) for j in range(w)]
    idx={v:i for i,v in enumerate(cells)}
    edges=[]
    for (x,y),i in idx.items():
        for dx,dy in ((1,0),(0,1)):
            z=(x+dx,y+dy)
            if z in idx:
                edges.append((i,idx[z]))
    @lru_cache(None)
    def ecount(mask):
        return sum(1 for a,b in edges if ((mask>>a)&1) and ((mask>>b)&1))
    @lru_cache(None)
    def q(mask):
        if mask == 0:
            return Fraction(1)
        den = 2*mask.bit_count() + ecount(mask)
        s = Fraction(0)
        m = mask
        while m:
            bit = m & -m
            m ^= bit
            s += q(mask ^ bit)
        return Fraction(2, den)*s
    return q((1<<(h*w))-1)

q_3x5 = qco_rect(3,5)
q_2x7 = qco_rect(2,7)
q_2x8 = qco_rect(2,8)
q_4x4 = qco_rect(4,4)
assert q_3x5 < BUDGET
assert q_2x7 > BUDGET
assert q_2x8 < BUDGET
assert q_4x4 < BUDGET

def drift_rect(h,w):
    if h>w:
        h,w=w,h
    if h == 1:
        return Fraction(-1,2)
    if h == 2:
        return Fraction(w,2)-1
    return -Fraction(3*h*w,2) + Fraction(7*(h+w),2) - 8

assert drift_rect(3,5) == Fraction(-5,2)
assert drift_rect(4,4) == Fraction(-4,1)
assert drift_rect(2,8) == Fraction(3,1)
assert drift_rect(2,7) == Fraction(5,2)

viable=[]
for h in range(2,17):
    for w in range(h,17):
        if h*w > 16:
            continue
        q = qco_rect(h,w)
        d = drift_rect(h,w)
        if q < BUDGET and d > 0:
            viable.append((h,w,q,d))
assert [(h,w) for h,w,_,_ in viable] == [(2,8)]

print("M_MAX_14", mmax(14))
print("L14", L14)
print("L14_decimal", float(L14))
print("L14_minus_1_over_64", L14-BUDGET)
print("L15", L15)
print("L15_decimal", float(L15))
print("ARG14", ARG[(14,mmax(14))])
print("qCO_3x5", q_3x5, float(q_3x5))
print("qCO_2x7", q_2x7, float(q_2x7))
print("qCO_2x8", q_2x8, float(q_2x8))
print("qCO_4x4", q_4x4, float(q_4x4))
print("drift_3x5", drift_rect(3,5))
print("drift_2x8", drift_rect(2,8))
print("viable_rectangles_area_le_16", [(h,w) for h,w,_,_ in viable])
print("PASS cardinality obstruction and thin-strip classification")
