#!/usr/bin/env python3
"""Exact finite checks for systematic spectral coding and erasure obstruction.
The asymptotic coding/existence theorem is proved in FEI.md, not by enumeration.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb
from pathlib import Path
import json

def walsh(values):
    v=list(values); width=1
    while width<len(v):
        for start in range(0,len(v),2*width):
            for j in range(start,start+width):
                a,b=v[j],v[j+width];v[j],v[j+width]=a+b,a-b
        width*=2
    return [F(x,len(v)) for x in v]

def parity_image(s,columns):
    t=0
    for i,c in enumerate(columns):
        if s>>i&1:t^=c
    return t

def encode(s,columns,n):return s | (parity_image(s,columns)<<n)

def lift_truth(values,columns,r):
    n=len(columns); out=[]
    for w in range(1<<(n+r)):
        x=w&((1<<n)-1);z=w>>n
        for i,c in enumerate(columns):
            x^=((z&c).bit_count()%2)<<i
        out.append(values[x])
    return out

def influence(coeff):return sum((F(s.bit_count())*a*a for s,a in enumerate(coeff)),F(0))

def main():
    cases=[];function_checks=0;coefficient_checks=0;erasure_checks=0
    for k,r,columns in [(1,1,[1,1,1]),(2,3,[3,5,6]),(3,4,[7,11,13])]:
        n=len(columns);length=n+r
        minweight=min(encode(s,columns,n).bit_count() for s in range(1,1<<n))
        assert minweight>k
        code=[encode(s,columns,n) for s in range(1<<n)]
        for d in range(1,k+1):
            for A in combinations(range(length),d):
                mask=sum(1<<i for i in A)
                completions=[s&~mask for s in code]
                assert len(set(completions))==len(code)
                erasure_checks+=1
        for truthword in range(1<<(1<<n)):
            values=[1 if truthword>>i&1 else -1 for i in range(1<<n)]
            a=walsh(values);b=walsh(lift_truth(values,columns,r))
            expected=[F(0)]*(1<<length)
            for s,c in enumerate(a):expected[encode(s,columns,n)]=c
            assert b==expected
            extra=sum((F(parity_image(s,columns).bit_count())*c*c for s,c in enumerate(a)),F(0))
            assert influence(b)==influence(a)+extra
            assert F(0)<=extra<=r
            assert sorted(c*c for c in a if c)==sorted(c*c for c in b if c)
            function_checks+=1;coefficient_checks+=len(b)
        cases.append({'k':k,'message_dimension':n,'parity_bits':r,
                      'columns':columns,'minimum_distance':minweight})
    union_checks=[]
    for N,k in [(1000,1),(1000,2),(1000,5),(10000,20)]:
        L=(2*N-1).bit_length() # ceil(log_2(2N)), exact
        r=3*k*L
        assert r<=N
        bad=sum(comb(N,j)*sum(comb(r,h) for h in range(k-j+1)) for j in range(1,k+1))
        assert bad<2**r
        union_checks.append({'N':N,'k':k,'r':r,'union_bound_strictly_below_one':True,
                             'numerator':str(bad),'denominator_power_two':r})
    # Exact addressing parity-lift witness for the false pointwise bound.
    m=8
    masses=sum(comb(m,j) for j in range(m+1)); assert masses==2**m
    H=2*m
    I=sum(F(comb(m,j),2**m)*(j+1+(j+1)%2) for j in range(m+1))
    ln2_lower=2*(F(1,3)+F(1,81))
    assert I==F(11,2) and ln2_lower==F(56,81)
    assert H*ln2_lower>2*I
    out={'status':'ALL_EXACT_CHECKS_PASS','codes':cases,
         'boolean_function_lifts_checked':function_checks,
         'Fourier_coefficient_equalities':coefficient_checks,
         'full_code_erasure_block_checks':erasure_checks,'exact_union_bound_tests':union_checks,
         'pointwise_counterexample':{'physical_variables':265,'nonzero_Fourier_coefficients':65536,
           'entropy_bits':H,'influence':str(I),'erasure_entropy':0,
           'ln2_lower_bound':str(ln2_lower),'H_times_lower_minus_2I':str(H*ln2_lower-2*I)},
         'scope':'Coding identities and rigorous counterexample; no proof or disproof of FEI.'}
    Path(__file__).with_name('fei_checks.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
