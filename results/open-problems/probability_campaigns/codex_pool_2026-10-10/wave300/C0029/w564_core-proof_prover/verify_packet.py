"""Bounded exact arithmetic diagnostics; no numerical theorem certificate."""
import argparse
import itertools
import json
import math
import time
from collections import Counter
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def determinant(a):
    if not a:
        return F(1)
    if len(a) == 1:
        return a[0][0]
    return sum(((-1)**j * a[0][j] * determinant(
        [row[:j] + row[j+1:] for row in a[1:]]) for j in range(len(a))), F(0))

def shifted_gram(rows, r2):
    return [[F(sum(x*y for x,y in zip(a,b))) - (r2 if i==j else 0)
             for j,b in enumerate(rows)] for i,a in enumerate(rows)]

def positive_definite(a):
    # Independent finite-dimensional event check: Sylvester's principal minors.
    return all(determinant([row[:k] for row in a[:k]]) > 0
               for k in range(1, len(a)+1))

def solve(a, b):
    aug = [list(row) + [v] for row,v in zip(a,b)]
    for j in range(len(a)):
        pivot = next(i for i in range(j,len(a)) if aug[i][j])
        aug[j],aug[pivot] = aug[pivot],aug[j]
        scale=aug[j][j]
        aug[j]=[v/scale for v in aug[j]]
        for i in range(len(a)):
            if i!=j:
                scale=aug[i][j]
                aug[i]=[x-scale*y for x,y in zip(aug[i],aug[j])]
    return [row[-1] for row in aug]

def hadamard(n):
    h=[[1]]
    while len(h)<n:
        h=[row+row for row in h] + [row+[-x for x in row] for row in h]
    return h

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--gate-receipt', required=True)
    args=parser.parse_args()
    gate=json.loads(Path(args.gate_receipt).read_text(encoding='utf-8'))
    if not gate.get('allow_small_check') or time.time()-gate['checked_epoch']>60:
        raise SystemExit('Fresh positive small-check gate required (max age 60 seconds).')
    cpu_start=time.process_time()
    counts=Counter()
    witness=None
    for n in (2,3):
        for flat in itertools.product((-1,1),repeat=n*n):
            rows=[flat[i*n:(i+1)*n] for i in range(n)]
            d,x=rows[:-1],rows[-1]
            dx=[F(sum(u*v for u,v in zip(row,x))) for row in d]
            for r2 in (F(0),F(1,4),F(1),F(2),F(4),F(9)):
                actual=not positive_definite(shifted_gram(rows,r2))
                top=shifted_gram(d,r2)
                if positive_definite(top):
                    delta=F(sum(v*v for v in x))-r2-sum(
                        u*v for u,v in zip(dx,solve(top,dx)))
                    predicted=delta<=0
                    zero=shifted_gram(d,F(0))
                    d0=F(sum(v*v for v in x))-sum(
                        u*v for u,v in zip(dx,solve(zero,dx)))
                    # Diagnostic baseline: erase r^2 from the singular denominators.
                    y=solve(zero,dx)
                    naive=d0<=r2*(1+sum(v*v for v in y))
                    counts['strict_gap_cases']+=1
                    counts['boundary_equalities']+=int(delta==0)
                else:
                    predicted=naive=True
                    counts['skeleton_below_or_equal_threshold']+=1
                counts['cases']+=1
                counts['exact_mismatches']+=int(predicted!=actual)
                counts['naive_mismatches']+=int(naive!=actual)
                if naive!=actual and witness is None:
                    witness={'matrix':rows,'r_squared':str(r2),
                             'true_small_singular_event':actual,
                             'erased_denominator_event':naive}
            if time.process_time()-cpu_start>2.0:
                raise SystemExit('Declared 2-second CPU budget exceeded; partial run is not a pass.')
    atoms=[]
    for n in (2,4,8):
        h=hadamard(n)
        assert all(sum(x*y for x,y in zip(h[i],h[j]))==(n if i==j else 0)
                   for i in range(n) for j in range(n))
        zero=sum(sum(row)==0 for row in itertools.product((-1,1),repeat=n))
        assert zero==math.comb(n,n//2)
        r=F(1,8*(n+1))
        qr=F(zero,2**n)
        gaussian_upper=2*r
        gap_lower=qr-gaussian_upper
        assert gap_lower>=F(3,4*(n+1))
        assert r*r<F(2,n)
        atoms.append({'n':n,'sign_rows_enumerated':2**n,'singular_rows':zero,
                      'sign_atom':str(qr),'r':str(r),
                      'gaussian_upper_bound':str(gaussian_upper),
                      'replacement_gap_lower_bound':str(gap_lower)})
    assert counts['exact_mismatches']==0
    assert counts['naive_mismatches']>0
    n1=math.erf(1/math.sqrt(2))
    asymptotic=1-math.exp(-1.5)
    report={'command':'python -X utf8 verify_packet.py --gate-receipt evidence/compute_gate.json',
            'gate_receipt':gate,'method':'Exact Fraction arithmetic for n=2,3; Sylvester positive definiteness; sign-row enumeration for Hadamard n=2,4,8.',
            'counts':dict(counts),'first_naive_failure':witness,'hadamard':atoms,
            'finite_gaussian_diagnostic':{'n':1,'epsilon':1,'actual_cdf':n1,
                'mislabelled_limiting_cdf':asymptotic,'absolute_difference':abs(n1-asymptotic),
                'analytic_proof':'At n=1 the CDF is erf(t/sqrt(2)) with derivative sqrt(2/pi) at zero, unlike the limiting expression whose derivative is 1.'},
            'cpu_seconds':time.process_time()-cpu_start,
            'formal_certificate':False,'independent_review':'pending',
            'parent_target':'UNPROVED: H is the remaining signed averaged inequality.'}
    output=ROOT/'evidence'/'verification.json'
    output.parent.mkdir(exist_ok=True)
    output.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))

if __name__=='__main__':
    main()
