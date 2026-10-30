#!/usr/bin/env python3
"""Exact sanity checks for the balanced support-deficit reduction.

These checks do not prove FEI.  They verify, on exhaustive small Boolean
families, the two algebraic mechanisms used in the accompanying proof:
(1) balanced suspension shifts the Fourier support by one coordinate and adds
exactly one to total influence while preserving spectral entropy;
(2) balanced disjoint self-composition has I_2=I^2 and
H_2=H(1+I).

All Fourier-energy identities are checked with integer Walsh transforms and
fractions.  Entropy recurrences are checked via exact equality of probability
multisets represented as rational squared-Walsh weights; no floating-point
comparison decides a pass/fail.
"""
from __future__ import annotations
from collections import Counter
from fractions import Fraction
import json
from pathlib import Path

def fwht(a):
    a=list(map(int,a))
    n=len(a); h=1
    while h<n:
        for i in range(0,n,2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h]
                a[j],a[j+h]=x+y,x-y
        h*=2
    return a

def spectral_counter(vals):
    W=fwht(vals); N=len(vals)
    den=N*N
    return Counter({i: Fraction(w*w,den) for i,w in enumerate(W) if w})

def influence(vals):
    W=fwht(vals); N=len(vals); den=N*N
    return sum((Fraction(w*w,den)*i.bit_count() for i,w in enumerate(W)), Fraction(0))

def suspension(vals):
    # bit 0 is the new y coordinate; y=+1 on 0 and y=-1 on 1.
    N=len(vals)
    out=[]
    for x in range(N):
        out.extend([vals[x],-vals[x]])
    return out

def compose_self(vals):
    """f(f(block_0),...,f(block_{n-1})) for n-bit balanced f."""
    N=len(vals); n=N.bit_length()-1
    assert N==1<<n
    out=[]
    total_bits=n*n
    for z in range(1<<total_bits):
        outer_index=0
        for b in range(n):
            inner_index=(z>>(b*n)) & (N-1)
            inner_val=vals[inner_index]
            if inner_val==-1:
                outer_index |= 1<<b
        out.append(vals[outer_index])
    return out

def normalized_weight_multiset(vals):
    W=fwht(vals); den=len(vals)**2
    return Counter(Fraction(w*w,den) for w in W if w)

def predicted_composition_multiset(vals):
    # Spectral sample: outer S, then an independent inner spectral sample
    # for each active block.  We only need the multiset of probabilities.
    W=fwht(vals); N=len(vals); den=N*N
    p=[Fraction(w*w,den) for w in W]
    n=N.bit_length()-1
    out=Counter()
    for S,ps in enumerate(p):
        if not ps: continue
        active=[j for j in range(n) if (S>>j)&1]
        states=[Fraction(1)]
        for _ in active:
            states=[a*b for a in states for b in p if b]
        for q in states:
            out[ps*q]+=1
    return out

suspensions=0
balanced_compositions=0
for n in range(1,4):
    N=1<<n
    for mask in range(1<<N):
        vals=[-1 if (mask>>x)&1 else 1 for x in range(N)]
        F=suspension(vals)
        # Exact spectrum shift: every nonzero weight preserved.
        assert normalized_weight_multiset(F)==normalized_weight_multiset(vals)
        assert influence(F)==influence(vals)+1
        assert sum(F)==0
        suspensions += 1
        if n>=2 and sum(vals)==0 and influence(vals)>1:
            C=compose_self(vals)
            assert influence(C)==influence(vals)*influence(vals)
            assert normalized_weight_multiset(C)==predicted_composition_multiset(vals)
            balanced_compositions += 1

out={
  "status":"PASS",
  "scope":"exhaustive Boolean functions n<=3 for suspension; balanced n=2,3 with I>1 for depth-2 self-composition",
  "suspensions_checked":suspensions,
  "balanced_self_compositions_checked":balanced_compositions,
  "arithmetic":"integer Walsh transforms + fractions; probability-multiset equality",
  "full_FEI_status":"OPEN; finite checks only"
}
root=Path(".")
print(json.dumps(out,indent=2))
