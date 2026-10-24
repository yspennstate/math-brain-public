#!/usr/bin/env python3
"""
R17 exact checker for run 20260916_2214Z_confidence_regen_8c2f.

No Monte Carlo is used.

Checks:
  X014 finite-sample confidence is not a deterministic mean certificate:
       an exact Bernoulli counterexample has a positive-probability misleading
       sample for every finite sample size.
  C015 finite beam-search sanity:
       exhaustive binary pairs through n=7 and W=1,2,3 verify that every beam
       score is <= exact LCS; exact block concatenation inequality is also
       checked for n=2 blocks.
  Exact finite means are printed only as finite evidence, not asymptotic bounds.
"""
from itertools import product
from fractions import Fraction

def lcs(x,y):
    d=[0]*(len(y)+1)
    for a in x:
        prev=0
        for j,b in enumerate(y,1):
            old=d[j]
            if a==b:
                d[j]=prev+1
            else:
                d[j]=max(d[j],d[j-1])
            prev=old
    return d[-1]

def nextpos(s,start,c):
    i=start
    while i<len(s) and s[i]!=c:
        i+=1
    return i

def beam_score(x,y,W):
    """Finite deterministic beam heuristic.
    Tie-breaking is lexicographic after the Archivara key (i+j, |i-j|).
    Every transition appends one common symbol, so the returned value is a
    valid common-subsequence length.
    """
    active={(0,0)}
    L=0
    N=len(x)
    while active:
        nxt=set()
        for i,j in active:
            for c in (0,1):
                ii=nextpos(x,i,c)
                jj=nextpos(y,j,c)
                if ii<N and jj<N:
                    nxt.add((ii+1,jj+1))
        if not nxt:
            break
        L+=1
        if len(nxt)>W:
            nxt=set(sorted(nxt,key=lambda p:(p[0]+p[1],abs(p[0]-p[1]),p[0],p[1]))[:W])
        active=nxt
    return L

# X014: exact finite-sample non-certification.
p=Fraction(1,4)
print("X014 finite-sample confidence obstruction")
for M in (1,2,5,10,100):
    misleading_prob=p**M
    assert misleading_prob>0
    # all-ones sample has empirical mean 1 while true mean is p.
    assert Fraction(1,1)>p
    print(f"  M={M}: P(all ones)={misleading_prob} > 0 while true mean={p}")
print("X014 exact logical counterexample: PASS")

# C015 finite beam sanity.
total_pairs=0
means={}
for n in range(1,8):
    strings=list(product((0,1),repeat=n))
    for W in (1,2,3):
        sh=0
        sl=0
        for x in strings:
            for y in strings:
                h=beam_score(x,y,W)
                L=lcs(x,y)
                assert 0<=h<=L<=n
                sh+=h
                sl+=L
                total_pairs+=1
        den=4**n
        means[(n,W)]=(Fraction(sh,den),Fraction(sl,den))
        print(f"n={n}, W={W}: E[beam]={Fraction(sh,den)}, E[LCS]={Fraction(sl,den)}")
print("Beam <= LCS exhaustive checks:", total_pairs)

# Exact block transfer for n=2 blocks, W=1,2,3.
block_checks=0
n=2
strings=list(product((0,1),repeat=n))
for W in (1,2,3):
    for x1 in strings:
      for y1 in strings:
       h1=beam_score(x1,y1,W)
       for x2 in strings:
        for y2 in strings:
            h2=beam_score(x2,y2,W)
            # Concatenate two valid per-block subsequences; its total length
            # cannot exceed the exact LCS of the concatenated strings.
            assert h1+h2 <= lcs(x1+x2,y1+y2)
            block_checks+=1
print("Exact two-block concatenation checks:", block_checks)

# Exact doubling superadditivity for true expected LCS at n=1,2,3.
# This is not needed to prove Fekete; it is a regression check of the finite data.
def exact_mean_lcs(n):
    ss=list(product((0,1),repeat=n))
    return Fraction(sum(lcs(x,y) for x in ss for y in ss),4**n)
for n in (1,2,3):
    e1=exact_mean_lcs(n)
    e2=exact_mean_lcs(2*n)
    assert e2 >= 2*e1
    print(f"superadditivity regression n={n}: E[L_{2*n}]={e2} >= 2E[L_{n}]={2*e1}")

print("ALL_EXACT_CHECKS_PASS")
