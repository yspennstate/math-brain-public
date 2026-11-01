#!/usr/bin/env python3
import csv, sys
from math import isqrt
import numpy as np
from scipy.optimize import linear_sum_assignment

DEN=10**15
ROOTS={d:(isqrt(d*DEN*DEN),isqrt(d*DEN*DEN)+1) for d in [165,30,195,10,15]}
for d,(lo,hi) in ROOTS.items():
    assert lo*lo <= d*DEN*DEN < hi*hi

def tuple_lb_num(row,k):
    A,B,C,D,E,F=map(int,row)
    if k==0:
        R=-5445*A+1485*B-1980*C+900*E+450*F+231750
        cs={165:242*A-242*B+22*D-22*E,
            30:352*B+176*C-32*E-16*F-40320}
    elif k==1:
        R=-5445*A+3465*B-990*C+900*E+450*F+105750
        cs={195:286*A-286*B+26*D-26*E,
            30:-44*A-22*C-4*D-2*F-160,
            10:396*B+198*C-36*E-18*F-43920}
    else:
        R=-495*A+495*B+450*D+450*E+450*F-2250
        cs={15:-176*A+176*B-16*D-16*E-16*F-20160}
    out=R*DEN
    for rad,c in cs.items():
        lo,hi=ROOTS[rad]
        out += c*(lo if c>=0 else hi)
    return out

def check_tuples(path,k,expected_count,expected_min,expected_tuple):
    count=0; mn=None; mt=None
    with open(path,newline='') as f:
        for row in csv.reader(f):
            if not row: continue
            z=tuple_lb_num(row,k)
            assert z>0,(path,row,z)
            count += 1
            if mn is None or z<mn: mn=z; mt=tuple(map(int,row))
    assert count==expected_count,(path,count,expected_count)
    assert mn==expected_min,(path,mn,expected_min,mt)
    assert mt==expected_tuple,(path,mt,expected_tuple)
    print(path,'count=',count,'min_lower_num=',mn,'den=',5445*DEN,'tuple=',mt)

N=15
AA=np.array([2*i+1-N for i in range(N)],dtype=np.int64)
SRC=np.array([(AA[r],AA[s]) for r in range(N) for s in range(N)],dtype=np.int64)
CELL_RHS=7*N*N*(N*N-1)

def check_cell(path,expected_total,expected_succ,expected_min,expected_fails):
    reps=sorted(tuple(map(int,row)) for row in csv.reader(open(path)) if row)
    assert len(reps)==expected_total,(path,len(reps),expected_total)
    succ=0; fails=[]; mn=None; mp=None
    for p in reps:
        targ=np.repeat(np.array([(AA[l],AA[p[l]]) for l in range(N)],dtype=np.int64),N,axis=0)
        weights=SRC@targ.T
        rr,cc=linear_sum_assignment(weights,maximize=True)
        W=int(weights[rr,cc].sum())
        margin=15*W-CELL_RHS
        if margin>=0:
            succ+=1
            if mn is None or margin<mn: mn,mp=margin,p
        else:
            fails.append((p,margin,W))
    assert succ==expected_succ,(path,succ,expected_succ)
    assert mn==expected_min,(path,mn,expected_min,mp)
    assert fails==expected_fails,(path,fails,expected_fails)
    print(path,'total=',len(reps),'success=',succ,'min_success=',mn,'min_perm=',mp,'failures=',fails)

def main(argv):
    if len(argv)!=10:
        print('usage: postcheck.py k0_fixed k0_adapt k0_reps k1_fixed k1_adapt k1_reps k2_fixed k2_adapt k2_reps')
        return 2
    check_tuples(argv[1],0,351224,464700117651048,(27,62,11,51,68,0))
    check_tuples(argv[2],0,9856,262254931637784,(22,67,11,30,45,8))
    check_tuples(argv[4],1,477114,1748832501837588,(25,66,9,68,23,0))
    check_tuples(argv[5],1,2985,2422750720161648,(26,69,5,26,6,50))
    check_tuples(argv[7],2,526550,6847256973591904,(29,61,10,69,41,0))
    check_tuples(argv[8],2,2323,6847256973591904,(29,61,10,9,1,100))
    ident=tuple(range(15))
    adj_right=tuple(list(range(13))+[14,13])
    check_cell(argv[3],2954,2952,1620,[(ident,-1320,23432),(adj_right,-180,23508)])
    check_cell(argv[6],742,741,1620,[(ident,-1320,23432)])
    check_cell(argv[9],309,308,3000,[(ident,-1320,23432)])
    print('EXACT S11 N15 RADICAL + CELL POSTCHECK PASSED')
    return 0
if __name__=='__main__': raise SystemExit(main(sys.argv))
