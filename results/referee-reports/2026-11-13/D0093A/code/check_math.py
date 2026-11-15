#!/usr/bin/env python3
"""Exact-arithmetic checks of the gathering-cost calculation and constants."""
from fractions import Fraction as F
from pathlib import Path

def solve_means(L,lam):
    # Thomas elimination for 2h_j-h_(j-1)-h_(j+1)=2(1+lambda).
    diagonal=[F(2)]*(L-1)
    rhs=[2*(1+lam)]*(L-1)
    for j in range(1,L-1):
        diagonal[j]-=1/diagonal[j-1]
        rhs[j]+=rhs[j-1]/diagonal[j-1]
    h=[F(0)]*(L+1)
    h[L-1]=rhs[-1]/diagonal[-1]
    for j in range(L-3,-1,-1):
        h[j+1]=(rhs[j]+h[j+2])/diagonal[j]
    return h

cases=0
for L in range(2,65):
    for lam in [F(1,10),F(1),F(4),F(10)]:
        h=solve_means(L,lam)
        assert all(h[j]==(1+lam)*j*(L-j) for j in range(L+1))
        assert sum(h)==(1+lam)*F(L*(L*L-1),6)
        # The hitting-probability weights received by one regular source sum to L.
        assert sum(F(L-abs(j),L) for j in range(-L+1,L))==L
        cases+=1
for L in range(16,2001):
    middle=sum(4*min(j,L-j)>=L for j in range(L))
    assert 3*middle>=L
    t=L*L//64
    assert 128*t>=L*L
    assert F(16*t,L*L)<=F(1,4)
text=(f'Exact tridiagonal mean solutions and independent sum formula: {cases} cases PASS\n'
      'Poisson source-intensity identity: PASS\n'
      'Middle-site count and maximal-inequality constants: L=16,...,2000 PASS\n'
      'These checks supplement the proofs in REPORT.md; they do not prove the ARW bound.\n')
(Path(__file__).resolve().parents[1]/'data'/'math_checks.txt').write_text(text)
print(text,end='')
