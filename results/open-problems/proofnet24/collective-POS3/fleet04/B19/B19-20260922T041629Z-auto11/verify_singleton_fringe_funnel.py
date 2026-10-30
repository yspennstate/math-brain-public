#!/usr/bin/env python3
"""Regression for the POS3 crossed-singleton fringe funnel.

Exhausts all transitively closed naturally labelled posets through n=6.
This is supporting finite evidence only; the report contains the general proof.
"""
from fractions import Fraction
from itertools import permutations

def closure(n, mask):
    pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
    reach=[0]*n
    for k,(i,j) in enumerate(pairs):
        if (mask>>k)&1:
            reach[i] |= 1<<j
    for k in range(n-1,-1,-1):
        bit=1<<k
        for i in range(k):
            if reach[i]&bit:
                reach[i] |= reach[k]
    return tuple(reach)

def all_posets(n):
    m=n*(n-1)//2
    seen=set()
    for mask in range(1<<m):
        r=closure(n,mask)
        if r not in seen:
            seen.add(r)
            yield r

def pred(n,r,v):
    return {i for i in range(n) if (r[i]>>v)&1}

def succ(n,r,v):
    return {j for j in range(n) if (r[v]>>j)&1}

def inc(r,a,b):
    return not ((r[a]>>b)&1 or (r[b]>>a)&1)

def cover(n,r,a,b):
    if not ((r[a]>>b)&1):
        return False
    return not any(k not in (a,b) and ((r[a]>>k)&1) and ((r[k]>>b)&1)
                   for k in range(n))

def autonomous(n,r,M):
    M=set(M)
    for t in range(n):
        if t in M:
            continue
        signs=[]
        for m in M:
            if (r[t]>>m)&1:
                signs.append(-1)
            elif (r[m]>>t)&1:
                signs.append(1)
            else:
                signs.append(0)
        if len(set(signs)) != 1:
            return False
    return True

def linear_extensions(n,r):
    pre=[0]*n
    for i in range(n):
        for j in range(n):
            if (r[i]>>j)&1:
                pre[j] |= 1<<i
    out=[]
    def rec(mask,seq):
        if mask==(1<<n)-1:
            out.append(tuple(seq))
            return
        for v in range(n):
            if not ((mask>>v)&1) and not (pre[v]&~mask):
                rec(mask|(1<<v),seq+(v,))
    rec(0,())
    return out

for n in range(4,7):
    singleton=0
    comparable=0
    incomparable=0
    reciprocal=0
    strong_outer=0
    amp_fail=0
    min_outer=None
    for r in all_posets(n):
        candidates=[]
        for x,y,d,u in permutations(range(n),4):
            if not inc(r,x,y):
                continue
            px,py=pred(n,r,x),pred(n,r,y)
            sx,sy=succ(n,r,x),succ(n,r,y)
            if not px.issubset(py) or py-px != {d}:
                continue
            if not sy.issubset(sx) or sx-sy != {u}:
                continue
            singleton += 1

            assert cover(n,r,d,y)
            assert cover(n,r,x,u)
            assert not ((r[u]>>d)&1)

            if (r[d]>>u)&1:
                comparable += 1
                continue

            assert inc(r,d,u)
            incomparable += 1
            assert pred(n,r,d).issubset(pred(n,r,u))
            assert succ(n,r,u).issubset(succ(n,r,d))
            Dout=pred(n,r,u)-pred(n,r,d)
            Uout=succ(n,r,d)-succ(n,r,u)
            assert x in Dout and y in Uout

            if Dout == {x} and Uout == {y}:
                reciprocal += 1
                assert autonomous(n,r,{d,x,y,u})

            candidates.append((x,y,d,u))

        if candidates:
            les=linear_extensions(n,r)
            E=len(les)
            pos=[{v:i for i,v in enumerate(L)} for L in les]
            for x,y,d,u in candidates:
                cdx=sum(p[d]<p[x] for p in pos)
                cxy=sum(p[x]<p[y] for p in pos)
                cyu=sum(p[y]<p[u] for p in pos)
                if 3*cdx>2*E and 3*cxy>2*E and 3*cyu>2*E:
                    strong_outer += 1
                    cdu=sum(p[d]<p[u] for p in pos)
                    if not 6*cdu>5*E:
                        amp_fail += 1
                    q=Fraction(cdu,E)
                    min_outer=q if min_outer is None or q<min_outer else min_outer

    print("n",n,
          "singleton",singleton,
          "d_lt_u",comparable,
          "d_parallel_u",incomparable,
          "reciprocal_singleton",reciprocal,
          "strong_outer_cases",strong_outer,
          "amplification_failures",amp_fail,
          "min_Pr_d_before_u",str(min_outer) if min_outer is not None else "NA")
    assert amp_fail == 0

print("POS3_SINGLETON_FRINGE_FUNNEL_CHECK_PASS")
