#!/usr/bin/env python3
from itertools import combinations
from collections import Counter

CASES = [
    (4,6,17),(4,5,19),(1,9,24),(7,9,26),
    (1,11,29),(1,12,31),(5,7,26),(6,13,37),
    (6,7,27),(5,6,31),(7,13,38),(1,15,38),
]

def sum3_set(vals):
    return {a+b+c for a,b,c in combinations(vals,3)}

def intervals(points):
    xs=sorted(points)
    if not xs: return []
    out=[]
    a=b=xs[0]
    for x in xs[1:]:
        if x==b+1:
            b=x
        else:
            out.append((a,b))
            a=b=x
    out.append((a,b))
    return out

def greedy(init, max_n):
    vals=list(sorted(init))
    S=set(vals)
    T=sum3_set(vals)
    for n in range(vals[-1]+1,max_n+1):
        if n not in T:
            for a,b in combinations(vals,2):
                T.add(a+b+n)
            vals.append(n)
            S.add(n)
    return S

def complement_gap_after(first_end, ints):
    x=first_end+1
    while True:
        covering=None
        for a,b in ints:
            if a<=x<=b:
                covering=(a,b)
                break
        if covering is None:
            start=x
            y=x
            while True:
                if any(a<=y<=b for a,b in ints):
                    return (start,y-1)
                y+=1
        x=covering[1]+1

rows=[]
for f,g,h in CASES:
    q=f+g
    d=h-g
    delta=d+1-q
    A=2*q+h
    r0=min(delta,q)
    J=(A,A+r0-1)
    prefix=[f,g]+list(range(h,h+q))+list(range(J[0],J[1]+1))
    T=sum3_set(prefix)
    ints=intervals(T)
    gap=complement_gap_after(J[1],ints)
    r1=gap[1]-gap[0]+1
    assert r1<=q, (f,g,h,r1,q)

    S=greedy((f,g,h),gap[1]+q+5)
    assert all(x in S for x in range(gap[0],gap[1]+1))
    assert all(x not in S for x in range(J[1]+1,gap[0]))

    if delta==2:
        expected=2
        cls="delta=2"
    elif (f,g,h)==(4,5,19):
        expected=1
        cls="early-disconnect"
    elif (f,g,h)==(5,6,31):
        expected=1
        cls="delta>q partial-first-gap"
    else:
        expected=q-2*delta+6
        cls="IJJ-to-JJJ"
    assert r1==expected, ((f,g,h),r1,expected,cls)
    rows.append(((f,g,h),q,delta,J,gap,r1,cls))

print("SECOND_BLOCK_EXACT_TABLE")
for row in rows:
    print(row)
print("FORMULA_COUNTS")
print(Counter(r[-1] for r in rows))
print("ALL_EXACT_CHECKS_PASS")
