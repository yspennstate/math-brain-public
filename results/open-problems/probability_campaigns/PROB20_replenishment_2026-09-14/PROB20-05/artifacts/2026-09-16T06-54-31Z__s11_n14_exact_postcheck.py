#!/usr/bin/env python3
import csv, sys
from math import isqrt
import numpy as np
from scipy.optimize import linear_sum_assignment

DEN=10**15
ROOTS={d:(isqrt(d*DEN*DEN),isqrt(d*DEN*DEN)+1) for d in [154,21,182,7,14]}
for d,(lo,hi) in ROOTS.items():
    assert lo*lo <= d*DEN*DEN < hi*hi

def tuple_lb_num(row,k):
    A,B,C,D,E,F=map(int,row)
    if k==0:
        R=-2541*A+1155*B-693*C+392*E+196*F+61460
        cs={154:121*A-121*B+11*D-11*E,
            21:132*B+66*C-12*E-6*F-14640}
    else:
        R=-2541*A+2079*B-231*C+392*E+196*F+6860
        cs={182:143*A-143*B+13*D-13*E,
            7:-44*A-22*C-4*D-2*F-160,
            14:88*B+44*C-8*E-4*F-9440}
    out=R*DEN
    for d,c in cs.items():
        lo,hi=ROOTS[d]
        out += c*(lo if c>=0 else hi)
    return out

def check_tuples(path,k,expected_count,expected_min):
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
    print(path,'count=',count,'min_lower_num=',mn,'den=',2541*DEN,'tuple=',mt)

N=14
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
    if len(argv)!=7:
        print('usage: postcheck.py k0_fixed k0_adapt k0_reps k1_fixed k1_adapt k1_reps')
        return 2
    check_tuples(argv[1],0,233615,54001491708670)
    check_tuples(argv[2],0,15594,252900108282995)
    check_tuples(argv[4],1,319843,607489394543570)
    check_tuples(argv[5],1,6205,1547284545289580)
    ident=tuple(range(14))
    adj=tuple(list(range(12))+[13,12])
    check_cell(argv[3],4941,4939,1260,[(ident,-1440,17740),(adj,-420,17808)])
    check_cell(argv[6],1254,1253,1260,[(ident,-1440,17740)])
    print('EXACT S11 N14 RADICAL + CELL POSTCHECK PASSED')
    return 0
if __name__=='__main__': raise SystemExit(main(sys.argv))
