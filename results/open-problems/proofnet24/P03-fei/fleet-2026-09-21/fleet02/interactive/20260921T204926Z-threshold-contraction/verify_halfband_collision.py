#!/usr/bin/env python3
"""Exact finite checks for the half-band collision extension; not full FEI."""
from __future__ import annotations
from collections import Counter
from fractions import Fraction as F
from math import comb
from pathlib import Path
import argparse, json
import numpy as np
from verify_threshold_contraction import rm_values, walsh, moment_rademacher


def multiply(a: dict[int,int], b: dict[int,int]) -> dict[int,int]:
    c=Counter()
    for i,x in a.items():
        for j,y in b.items():c[i+j]+=x*y
    return {i:x for i,x in c.items() if x}


def exact_checks() -> dict:
    examples=[];laurent_checks=0;moment_checks=0
    # All four matrices are actually enumerated; no large-D enumeration is claimed.
    for D,d in ((3,2),(4,2),(4,3),(5,2)):
        N=1<<D;M=N-4
        base=(1<<(D-1))-1;direction=6 if D>=5 else 2
        pts=[(base^(direction if a else 0))|(b<<(D-1)) for a in (0,1) for b in (0,1)]
        codes=rm_values(D,d).astype(np.int64);L=len(codes)
        outside=[i for i in range(N) if i not in pts]
        Wout=codes[:,outside].sum(axis=1)
        counts=Counter(map(int,Wout))
        collision=F(sum(c*c for c in counts.values()),L*L)
        m=min(3,2**(d-1)-1,M)
        K=sum(F(comb(M,j)**2,comb(2*M,2*j)) for j in range(m+1))
        assert collision<=1/K
        for k in range(0,4*m+1):
            value=sum(a*b*(w-v)**k for w,a in counts.items() for v,b in counts.items())
            assert value==L*L*moment_rademacher(2*M,k)
            moment_checks+=1
        ids=np.arange(16,dtype=np.int64)
        h=np.ones((16,N),np.int64)
        for j,x in enumerate(pts):h[:,x]=1-2*((ids>>j)&1)
        W=h@codes.T
        freq=np.arange(0,N+1,2,dtype=np.int64)
        hist=np.array([[np.count_nonzero(np.abs(row)==w) for w in freq] for row in W],dtype=np.int64)
        active_coeff=walsh(hist.T).T
        signed_energies=[]
        factor={1:1,-1:-1}
        base_poly=multiply(multiply(multiply(factor,factor),factor),{1:1,-1:1})
        for R in range(16):
            if R.bit_count()!=3:continue
            sign=np.prod(codes[:,[pts[j] for j in range(4) if (R>>j)&1]],axis=1)
            signed=Counter()
            for w,z in zip(Wout,sign):signed[int(w)]+=int(z)
            norm=F(sum(a*a for a in signed.values()),L*L)
            assert norm<=collision
            signed_energies.append(str(norm))
            # Compare normalized cos coefficients with sin^3(t)cos(t)E[Z sin(tWout)].
            # Multiply both Laurent polynomials by 32*L: all arithmetic is integer.
            direct=Counter()
            for w,a in zip(freq,active_coeff[R]):
                if w==0:direct[0]+=2*int(a)
                else:direct[int(w)]+=int(a);direct[-int(w)]+=int(a)
            source=Counter()
            for w,a in signed.items():
                if not w or not a:continue
                p=multiply(base_poly,{w:1,-w:-1})
                for j,z in p.items():source[j]+=a*z
            assert {j:a for j,a in source.items() if a}=={j:a for j,a in direct.items() if a}
            laurent_checks+=1
        examples.append({'D':D,'d':d,'enumerated_codewords':L,
            'outside_positions':M,'moment_parameter_m':m,
            'collision_probability_exact':str(collision),'Christoffel_upper_bound_exact':str(1/K),
            'signed_coefficient_squared_norms_exact':signed_energies,
            'large_D_halfband_claim_tested_by_enumeration':False})
    threshold_cases=0
    for D in range(128,513):
        n=D-1;d=(D+1)//2;m=(1<<(d-1))-1
        # pi<22/7. This is the squared condition ensuring E1<=E0/4.
        bound=8*n**3*F((2097152*22)**2,147**2)
        assert m>=bound
        assert F((n+2)**3,n**3)<2
        threshold_cases+=1
    asymptotic_scales=[]
    import math
    for D in (128,256,512,1024):
        n=D-1;d=(D+1)//2
        # Written proofs, not these numerical scale summaries, establish the asymptotics.
        log2ratio=D+math.log2(1/54)-4*math.log2(n)
        # (4/(27*n^3))/(8*n/2^D) = 2^D/(54*n^4).
        asymptotic_scales.append({'D':D,'halfband_d':d,
            'log2_leading_current_over_J_float':log2ratio,
            'scope':'evaluation of analytic leading-order formula, not direct huge-dimensional simulation'})
    return {'status':'PASS','exact_Laurent_polynomial_checks':laurent_checks,
        'exact_two_copy_moment_checks':moment_checks,'exact_dimension_threshold_checks':threshold_cases,
        'examples':examples,'asymptotic_scales':asymptotic_scales}


def main() -> None:
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path);a=p.parse_args()
    result={'schema_version':1,'full_FEI':'OPEN_NOT_PROVED','checks':exact_checks()}
    text=json.dumps(result,indent=2,sort_keys=True)+'\n'
    if a.output:a.output.write_text(text,encoding='utf-8')
    print(text)

if __name__=='__main__':main()
