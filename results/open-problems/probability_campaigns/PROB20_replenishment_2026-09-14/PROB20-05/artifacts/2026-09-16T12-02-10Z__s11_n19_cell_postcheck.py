#!/usr/bin/env python3
import csv, sys
import numpy as np
from scipy.optimize import linear_sum_assignment
N=19
AA=np.array([2*i+1-N for i in range(N)],dtype=np.int64)
SRC=np.array([(AA[r],AA[s]) for r in range(N) for s in range(N)],dtype=np.int64)
RHS=7*N*N*(N*N-1)
IDENT=tuple(range(N))
ADJ_RIGHT=tuple(list(range(17))+[18,17])
EXPECT={
0:(1277,1275,1980,[(IDENT,-2400,60488),(ADJ_RIGHT,-720,60600)]),
1:(261,260,1980,[(IDENT,-2400,60488)]),
2:(2914,2913,3840,[(IDENT,-2400,60488)]),
3:(1734,1733,5460,[(IDENT,-2400,60488)]),
4:(772,771,6900,[(IDENT,-2400,60488)]),
}
def check(path,k):
 reps=sorted(tuple(map(int,row)) for row in csv.reader(open(path)) if row)
 succ=0; fails=[]; mn=None; mp=None
 for p in reps:
  targ=np.repeat(np.array([(AA[l],AA[p[l]]) for l in range(N)],dtype=np.int64),N,axis=0)
  weights=SRC@targ.T
  rr,cc=linear_sum_assignment(weights,maximize=True)
  assert len(rr)==N*N and len(cc)==N*N
  W=int(weights[rr,cc].sum()); margin=15*W-RHS
  if margin>=0:
   succ+=1
   if mn is None or margin<mn: mn,mp=margin,p
  else:
   fails.append((p,margin,W))
 exp_total,exp_succ,exp_min,exp_fails=EXPECT[k]
 assert len(reps)==exp_total,(k,len(reps),exp_total)
 assert succ==exp_succ,(k,succ,exp_succ)
 assert mn==exp_min,(k,mn,exp_min,mp)
 assert fails==exp_fails,(k,fails,exp_fails)
 print(f'k={k} total={len(reps)} success={succ} min_success={mn} min_perm={mp} failures={fails}')
def main(argv):
 if len(argv)!=3:
  print('usage: postcheck.py k reps.csv'); return 2
 k=int(argv[1]); assert k in EXPECT
 check(argv[2],k)
 print(f'EXACT S11 N19 CELL POSTCHECK PASSED k={k}')
 return 0
if __name__=='__main__': raise SystemExit(main(sys.argv))
