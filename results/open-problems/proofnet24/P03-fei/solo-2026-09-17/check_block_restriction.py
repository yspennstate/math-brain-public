#!/usr/bin/env python3
"""Rigorous finite self-checks for BLOCK_RESTRICTION_IDENTITY_2026-09-18.md."""
from fractions import Fraction as F
from pathlib import Path
import itertools
import json
import random

from certify_nand80 import wht, h, IV, LN2_HI, rational_interval


def entropy(p):
    return sum((h(x) for x in p),IV(0))


def spectrum(values):
    N=len(values)
    return [F(x,N)**2 for x in wht(values)]


def overlap(a,b):
    assert max(a.lo,b.lo)<=min(a.hi,b.hi)


def restriction(values,n,A,xmask):
    C=[i for i in range(n) if i not in A]
    out=[]
    for ymask in range(1<<len(C)):
        index=0
        for j,i in enumerate(A): index|=((xmask>>j)&1)<<i
        for j,i in enumerate(C): index|=((ymask>>j)&1)<<i
        out.append(values[index])
    return out


def check(values,n,A):
    C=[i for i in range(n) if i not in A]
    p=spectrum(values); H=entropy(p)
    q=[]
    for d in range(1<<len(C)):
        total=F(0)
        for e in range(1<<len(A)):
            S=0
            for j,i in enumerate(A): S|=((e>>j)&1)<<i
            for j,i in enumerate(C): S|=((d>>j)&1)<<i
            total+=p[S]
        q.append(total)
    Hq=entropy(q)
    restricted=[spectrum(restriction(values,n,A,x)) for x in range(1<<len(A))]
    EH=sum((entropy(px) for px in restricted),IV(0))*F(1,1<<len(A))
    MI=Hq-EH; conditional=H-Hq; delta=H-EH
    overlap(delta,conditional+MI)
    influence=F(0)
    N=1<<n
    for i in A:
        influence+=F(sum(values[x]!=values[x^(1<<i)] for x in range(N)),N)
    # Outward subtraction can put the lower endpoint microscopically below
    # zero when the exact mutual information vanishes.
    assert MI.hi>=0
    rounding_allowance=F(1,1<<140)
    assert MI.hi <= F(2,LN2_HI)*influence+rounding_allowance, (n,A,MI.hi,F(2,LN2_HI)*influence)
    # Exact influence decomposition, evaluated from restriction truth tables.
    outside=F(0)
    for rv in [restriction(values,n,A,x) for x in range(1<<len(A))]:
        M=len(rv); k=len(C)
        outside+=sum((F(sum(rv[y]!=rv[y^(1<<j)] for y in range(M)),M)
                      for j in range(k)),F(0))*F(1,1<<len(A))
    full=sum((F(sum(values[x]!=values[x^(1<<i)] for x in range(N)),N)
              for i in range(n)),F(0))
    assert full==influence+outside
    return MI,influence


def main():
    records=[]; min_slack=None
    for n in range(1,4):
        N=1<<n
        for label in range(1<<N):
            values=[1-2*((label>>x)&1) for x in range(N)]
            for mask in range(1,1<<n):
                A=[i for i in range(n) if mask&(1<<i)]
                MI,I=check(values,n,A)
                slack=F(2,LN2_HI)*I-MI.hi
                min_slack=slack if min_slack is None else min(min_slack,slack)
                records.append([n,label,mask])
    rng=random.Random(202609180057)
    sampled=[]
    n=4;N=1<<n
    for _ in range(128):
        label=rng.randrange(1<<N)
        values=[1-2*((label>>x)&1) for x in range(N)]
        for mask in range(1,1<<n):
            A=[i for i in range(n) if mask&(1<<i)]
            check(values,n,A);sampled.append([label,mask])
    out={'status':'PASS','arithmetic':'exact truth tables and Fourier probabilities; 160-bit outward rational logarithm intervals',
         'exhaustive_range':'every Boolean truth table through n=3 and every nonempty coordinate block',
         'exhaustive_count':len(records),
         'sample_seed':202609180057,'sampled_n4_rule':'128 pseudorandom truth tables and every nonempty coordinate block',
         'sampled_n4_count':len(sampled),'minimum_exhaustive_certified_slack':str(min_slack),
         'scope':'Finite self-checks only; the universal block identity and inequality are proved in the note. No independent audit.'}
    Path('block_restriction_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'status':'PASS','exhaustive_count':len(records),
                      'sampled_n4_count':len(sampled),
                      'minimum_exhaustive_certified_slack':str(min_slack)},indent=2))


if __name__=='__main__':main()
