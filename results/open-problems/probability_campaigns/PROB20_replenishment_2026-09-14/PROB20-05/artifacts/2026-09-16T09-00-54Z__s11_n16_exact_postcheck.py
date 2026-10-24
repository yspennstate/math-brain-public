#!/usr/bin/env python3
import csv, sys
from math import isqrt
import numpy as np
from scipy.optimize import linear_sum_assignment

DEN=10**15
ROOTS={d:(isqrt(d*DEN*DEN),isqrt(d*DEN*DEN)+1) for d in [11,10,13,2,15,6]}
for d,(lo,hi) in ROOTS.items():
    assert lo*lo <= d*DEN*DEN < hi*hi

def tuple_lb_num(row,k):
    A,B,C,D,E,F=map(int,row)
    if k==0:
        R=-726*A+66*B-330*C+128*E+64*F+45160
        cs={11:121*A-121*B+11*D-11*E,
            10:110*B+55*C-10*E-5*F-13000}
    elif k==1:
        R=-726*A+330*B-198*C+128*E+64*F+27160
        cs={13:143*A-143*B+13*D-13*E,
            2:-22*A+176*B+77*C-2*D-16*E-9*F-20240}
    else:
        R=-814*A+594*B-110*C-8*D+128*E+60*F+10920
        cs={15:165*A-165*B+15*D-15*E,
            6:66*B+33*C-6*E-3*F-7320}
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
    print(path,'count=',count,'min_lower_num=',mn,'den=',726*DEN,'tuple=',mt)

N=16
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
    check_tuples(argv[1],0,468848,31272940599700,(26,65,9,84,32,0))
    check_tuples(argv[2],0,7004,91923809202400,(22,66,12,10,63,0))
    check_tuples(argv[4],1,610209,370786206072638,(29,61,10,77,36,0))
    check_tuples(argv[5],1,1845,21811280673024,(27,62,11,7,2,90))
    check_tuples(argv[7],2,686413,659667425678029,(25,64,11,45,36,0))
    check_tuples(argv[8],2,1288,1128085956891390,(20,68,12,0,34,20))
    ident=tuple(range(16))
    adj_right=tuple(list(range(14))+[15,14])
    check_cell(argv[3],2115,2113,1380,[(ident,-2040,30328),(adj_right,-720,30416)])
    check_cell(argv[6],506,505,1380,[(ident,-2040,30328)])
    check_cell(argv[9],247,246,2820,[(ident,-2040,30328)])
    print('EXACT S11 N16 RADICAL + CELL POSTCHECK PASSED')
    return 0
if __name__=='__main__': raise SystemExit(main(sys.argv))
