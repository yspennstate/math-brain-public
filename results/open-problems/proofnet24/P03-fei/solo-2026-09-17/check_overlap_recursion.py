#!/usr/bin/env python3
"""Exact checks of the aggregate-overlap obstruction; standard library only."""
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import json
from certify_nand80 import wht


def overlap(coeff):
    N=len(coeff); n=N.bit_length()-1
    return sum((2*abs(coeff[s]*coeff[s^(1<<i)])
                for i in range(n) for s in range(N) if not(s&(1<<i))),F(0))


def initial(a):
    N=len(a); n=N.bit_length()-1
    c=[F(x,N) for x in wht(a)]
    alpha=c[0]; t=[c[1<<i] for i in range(n)]
    I=4*sum(s.bit_count()*v*v for s,v in enumerate(c))
    assert I==2*sum(abs(x) for x in t)
    return alpha,t,overlap(c),I


def main():
    records=[]
    for n in range(1,5):
        for m in range(1,1<<n):
            a=[int(x<m) for x in range(1<<n)]
            alpha,t,R,I=initial(a)
            for k in [2,3]:
                if n*k>12:continue
                prod=a
                for _ in range(k-1):prod=[x*y for x in prod for y in a]
                ap=[1-x for x in prod]
                alphap,tp,Rp,Ip=initial(ap)
                assert alphap==1-alpha**k
                assert Ip==k*alpha**(k-1)*I
                assert Rp/Ip==R/I+1-2*alpha**k
                f=[1-2*x for x in ap]
                N=len(f); fp=[F(x,N) for x in wht(f)]
                Rf=overlap(fp)
                assert Rf/Ip==4*Rp/Ip+2*(abs(1-2*alphap)-2*alphap)
                records.append([n,m,k])
    corridors=[]
    for depth in range(1,11):
        bits=depth+7
        m=(isqrt(5*(1 << (2*bits)))-(1<<bits))//2
        alpha=F(m,1<<bits)
        gain=F(0)
        for j in range(depth):
            alpha=1-alpha*alpha
            assert F(3,5)<alpha<F(2,3)
            gain+=4*(2*alpha-1)
        assert gain>F(4*depth,5)
        # A small rational lower bound, not an approximate decimal.
        lower=F((gain.numerator*1000000)//gain.denominator,1000000)
        corridors.append({'depth':depth,'base_bits':bits,'base_size':m,
                          'formal_dimension':bits*(1<<depth),
                          'certified_gain_lower_bound':str(lower)})
    out={'status':'PASS','exact_full_truth_table_composition_checks':len(records),
         'checked_parameters':records,'fixed_point_corridor_checks':corridors,
         'proof_scope':'The all-depth theorem is proved in COMPOSITION_AND_BARRIERS.md; these finite exact checks validate its recurrences, not its quantifier by enumeration.'}
    Path('overlap_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
