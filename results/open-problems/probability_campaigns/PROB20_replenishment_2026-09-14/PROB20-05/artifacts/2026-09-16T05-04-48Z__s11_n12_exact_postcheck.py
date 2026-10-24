#!/usr/bin/env python3
import csv, sys
from fractions import Fraction
from math import isqrt
import numpy as np
from scipy.optimize import linear_sum_assignment

N=12
RAD_DEN=10**15

def sqrt_bounds(d,den=RAD_DEN):
    q=isqrt(d*den*den)
    assert q*q <= d*den*den < (q+1)*(q+1)
    return Fraction(q,den),Fraction(q+1,den)
LB33,UB33=sqrt_bounds(33); LB6,UB6=sqrt_bounds(6)

def coeffs(tup):
    CSL,CSH,sV,ZL,ZH,ZV=map(int,tup)
    q0=Fraction(-CSL,1)+Fraction(9*CSH,11)-Fraction(sV,11)+Fraction(16*ZH,121)+Fraction(8*ZV,121)-200*Fraction(53,1210)
    q33=Fraction(CSL-CSH,9)+Fraction(ZL-ZH,99)
    q6=Fraction(2*CSH,99)+Fraction(sV,99)-Fraction(2*ZH,1089)-Fraction(ZV,1089)-200*Fraction(19,1815)
    return q0,q33,q6

def lower_bound(tup):
    q0,q33,q6=coeffs(tup)
    return q0 + q33*(LB33 if q33>=0 else UB33) + q6*(LB6 if q6>=0 else UB6)

def check_tuples(path,expected_count,expected_min_num,expected_min_den):
    count=0; mn=None; mt=None
    with open(path,newline='') as f:
        for row in csv.reader(f):
            if not row: continue
            t=tuple(map(int,row)); assert len(t)==6
            b=lower_bound(t); assert b>0,(t,b)
            count+=1
            if mn is None or b<mn: mn,mt=b,t
    assert count==expected_count,(count,expected_count)
    assert mn==Fraction(expected_min_num,expected_min_den),(mn,mt)
    print(path,'count=',count,'min_lower=',mn,'tuple=',mt)

A=np.array([2*i+1-N for i in range(N)],dtype=np.int64)
SRC=np.array([(A[r],A[s]) for r in range(N) for s in range(N)],dtype=np.int64)
CELL_RHS=7*N*N*(N*N-1)

def check_cell(reps_path,start,end):
    reps=[]
    with open(reps_path,newline='') as f:
        for row in csv.reader(f):
            if row: reps.append(tuple(map(int,row)))
    assert len(reps)==144834,len(reps)
    reps=sorted(reps)
    assert 0<=start<=end<=len(reps)
    succ=0; fail=[]; minm=None; minp=None
    for p in reps[start:end]:
        targ=np.repeat(np.array([(A[l],A[p[l]]) for l in range(N)],dtype=np.int64),N,axis=0)
        weights=SRC@targ.T
        rr,cc=linear_sum_assignment(weights,maximize=True)
        W=int(weights[rr,cc].sum())
        m=15*W-CELL_RHS
        if m>=0:
            succ+=1
            if minm is None or m<minm:minm,minp=m,p
        else: fail.append((p,m,W))
    print('cell range',start,end,'successes=',succ,'failures=',fail,'min_success=',minm,'min_perm=',minp)
    return succ,fail,minm

def main():
    if len(sys.argv)<4:
        print('usage: exact_postcheck.py fixed_tuples.csv adaptive_tuples.csv reps.csv [start end]')
        return 2
    check_tuples(sys.argv[1],49641,58468275106451,1089000000000000000)
    check_tuples(sys.argv[2],453,884512957239853,1089000000000000000)
    if len(sys.argv)==6:
        check_cell(sys.argv[3],int(sys.argv[4]),int(sys.argv[5]))
    print('EXACT S11 N12 RADICAL POSTCHECK PASSED')
    return 0
if __name__=='__main__': raise SystemExit(main())
