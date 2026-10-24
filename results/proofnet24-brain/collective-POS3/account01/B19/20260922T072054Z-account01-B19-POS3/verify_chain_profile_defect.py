#!/usr/bin/env python3
from itertools import product

def count_interval(lo, hi, s, t):
    if lo > hi:
        return 0
    return max(0, min(hi, t) - max(lo, s) + 1)

def direct_counts(A, B, s, t):
    a,b=A; c,d=B
    uv=sum(1 for x in range(a,b+1) for y in range(c,d+1) if s <= x <= y <= t)
    vu=sum(1 for x in range(c,d+1) for y in range(a,b+1) if s <= x <= y <= t)
    return uv,vu

def closed_defect(A, B, s, t):
    a,b=A; c,d=B
    if max(a,c) > min(b,d):
        raise ValueError("profiles must overlap")
    def n(lo,hi):
        return count_interval(lo,hi,s,t)
    # A shifted left of B
    if a <= c and b <= d:
        L,O,R=n(a,c-1),n(c,b),n(b+1,d)
        return L*O + L*R + O*R
    # B shifted left of A
    if c <= a and d <= b:
        L,O,R=n(c,a-1),n(a,d),n(d+1,b)
        return -(L*O + L*R + O*R)
    # Remaining overlap types are strict nesting; the endpoint-equality
    # cases have already been harmlessly handled above.
    if c <= a and b <= d:  # A inside B
        L,O,R=n(c,a-1),n(a,b),n(b+1,d)
        return O*(R-L)
    if a <= c and d <= b:  # B inside A
        L,O,R=n(a,c-1),n(c,d),n(d+1,b)
        return O*(L-R)
    raise AssertionError((A,B,s,t))

def sign_variations(v):
    s=[1 if x>0 else -1 for x in v if x]
    return sum(x != y for x,y in zip(s,s[1:]))

def prefix_mask(v, interval):
    a,b=interval
    out=[]
    total=0
    for i,x in enumerate(v):
        total += x
        out.append(total if a <= i <= b else 0)
    return out

local_cases=0
nested_slices=0
for m in range(10):
    intervals=[(a,b) for a in range(m+1) for b in range(a,m+1)]
    for A in intervals:
        for B in intervals:
            if max(A[0],B[0]) > min(A[1],B[1]):
                continue
            for s in range(m+1):
                for t in range(s,m+1):
                    local_cases += 1
                    uv,vu=direct_counts(A,B,s,t)
                    assert uv-vu == closed_defect(A,B,s,t)
            nested=(B[0] <= A[0] and A[1] <= B[1]) or (A[0] <= B[0] and B[1] <= A[1])
            if nested:
                for t in range(m+1):
                    v=[]
                    for s in range(m+1):
                        if s <= t:
                            uv,vu=direct_counts(A,B,s,t)
                            v.append(uv-vu)
                        else:
                            v.append(0)
                    assert sign_variations(v) <= 1
                    nested_slices += 1
                for s in range(m+1):
                    v=[]
                    for t in range(m+1):
                        if s <= t:
                            uv,vu=direct_counts(A,B,s,t)
                            v.append(uv-vu)
                        else:
                            v.append(0)
                    assert sign_variations(v) <= 1
                    nested_slices += 1

transfer_cases=0
for m in range(6):
    n=m+1
    intervals=[(a,b) for a in range(n) for b in range(a,n)]
    for v in product(range(-2,3), repeat=n):
        if sign_variations(v) <= 1:
            for I in intervals:
                transfer_cases += 1
                assert sign_variations(prefix_mask(v,I)) <= 1

print("local_defect_cases", local_cases)
print("nested_one_crossing_slices", nested_slices)
print("one_step_variation_cases", transfer_cases)
print("POS3_CHAIN_PROFILE_DEFECT_CHECK_PASS")
