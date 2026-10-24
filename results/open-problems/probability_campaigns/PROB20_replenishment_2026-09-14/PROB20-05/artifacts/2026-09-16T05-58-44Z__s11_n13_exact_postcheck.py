#!/usr/bin/env python3
import csv, sys
from fractions import Fraction
from math import isqrt
import numpy as np
from scipy.optimize import linear_sum_assignment

N=13
RAD_DEN=10**15

def sqrt_bounds(d,den=RAD_DEN):
    q=isqrt(d*den*den)
    assert q*q <= d*den*den < (q+1)*(q+1)
    return Fraction(q,den), Fraction(q+1,den)

LB143,UB143=sqrt_bounds(143)
LB13,UB13=sqrt_bounds(13)
LB26,UB26=sqrt_bounds(26)

def lb_k0(row):
    A,B,C,D,E,F=map(int,row)
    c143=Fraction(2*A,39)-Fraction(2*B,39)+Fraction(2*D,429)-Fraction(2*E,429)
    c13=Fraction(16*B,429)+Fraction(8*C,429)-Fraction(16*E,4719)-Fraction(8*F,4719)-Fraction(18880,4719)
    rat=-A+Fraction(7*B,11)-Fraction(2*C,11)+Fraction(52*E,363)+Fraction(26*F,363)+Fraction(2570,363)
    return rat + c143*(LB143 if c143>=0 else UB143) + c13*(LB13 if c13>=0 else UB13)

def lb_k1(row):
    A,B,C,D,E,F=map(int,row)
    c26=-Fraction(4*A,429)+Fraction(4*B,429)-Fraction(4*D,4719)-Fraction(4*E,4719)-Fraction(4*F,4719)-Fraction(4720,4719)
    rat=-Fraction(7*A,33)+Fraction(7*B,33)+Fraction(26*D,363)+Fraction(26*E,363)+Fraction(26*F,363)-Fraction(4630,363)
    return rat + c26*(LB26 if c26>=0 else UB26)

def check_tuples(path,k,expected_count,expected_min):
    fn=lb_k0 if k==0 else lb_k1
    count=0; mn=None; mt=None
    with open(path,newline='') as f:
        for row in csv.reader(f):
            if not row: continue
            assert len(row)==6
            b=fn(row); assert b>0,(k,row,b)
            count += 1
            if mn is None or b<mn: mn,mt=b,tuple(map(int,row))
    assert count==expected_count,(path,count,expected_count)
    assert mn==expected_min,(path,mn,mt,expected_min)
    print(path,'count=',count,'min_lower=',mn,'tuple=',mt)

A=np.array([2*i+1-N for i in range(N)],dtype=np.int64)
SRC=np.array([(A[r],A[s]) for r in range(N) for s in range(N)],dtype=np.int64)
CELL_RHS=7*N*N*(N*N-1)

def check_cell(reps_path,start,end,expected_total):
    with open(reps_path,newline='') as f:
        reps=sorted(tuple(map(int,row)) for row in csv.reader(f) if row)
    assert len(reps)==expected_total,(len(reps),expected_total)
    assert 0<=start<=end<=len(reps)
    succ=0; fail=[]; minm=None; minp=None
    for p in reps[start:end]:
        targ=np.repeat(np.array([(A[l],A[p[l]]) for l in range(N)],dtype=np.int64),N,axis=0)
        weights=SRC@targ.T
        rr,cc=linear_sum_assignment(weights,maximize=True)
        W=int(weights[rr,cc].sum())
        m=15*W-CELL_RHS
        if m>=0:
            succ += 1
            if minm is None or m<minm: minm,minp=m,p
        else:
            fail.append((p,m,W))
    print('cell',reps_path,'range',start,end,'successes=',succ,'failures=',fail,'min_success=',minm,'min_perm=',minp)
    return succ,fail,minm

def main():
    if len(sys.argv)<6:
        print('usage: postcheck.py k0_fixed k0_adapt k1_fixed k1_adapt mode [reps start end]')
        return 2
    check_tuples(sys.argv[1],0,127855,Fraction(7081914994511,196625000000000000))
    check_tuples(sys.argv[2],0,3342,Fraction(142364791528987,294937500000000000))
    check_tuples(sys.argv[3],1,165348,Fraction(109222340349379,78650000000000000))
    check_tuples(sys.argv[4],1,2936,Fraction(218061138318209,235950000000000000))
    print('EXACT S11 N13 RADICAL TUPLE POSTCHECK PASSED')
    if sys.argv[5]=='cell':
        reps=sys.argv[6]; start=int(sys.argv[7]); end=int(sys.argv[8]); total=int(sys.argv[9])
        check_cell(reps,start,end,total)
    return 0
if __name__=='__main__': raise SystemExit(main())
