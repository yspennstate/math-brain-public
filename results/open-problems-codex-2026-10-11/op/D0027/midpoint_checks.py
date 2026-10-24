from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
import json
cases=0;max_var=F(0)
for q in [F(1,5),F(1,2),F(4,5)]:
 p=1-q
 for mask in range(1,128):
  infected={i-3 for i in range(7) if mask>>i&1};left=min(infected);right=max(infected);M=F(left+right,2);D=right-left
  amin=F(D>0 and left+1 in infected);aplus=F(D>0 and right-1 in infected)
  drift=F(0);var=F(0);width_drift=F(0);active_rate=F(0)
  for x in range(left-1,right+2):
   if x-1 not in infected and x+1 not in infected:continue
   rate=p if x in infected else q
   new=infected^{x};assert new
   dm=F(min(new)+max(new),2)-M;dd=max(new)-min(new)-D
   assert abs(dm)<=F(1,2)
   drift+=rate*dm;var+=rate*dm*dm;width_drift+=rate*dd
   if dm:active_rate+=rate
  assert drift==p*(amin-aplus)/2
  assert width_drift==2*q-p*(amin+aplus)
  assert var<=F(1,2) and active_rate<=2
  max_var=max(max_var,var);cases+=1
r={'status':'PASS','exact_nonempty_infection_sets':cases,'q':['1/5','1/2','4/5'],'initial_window':[-3,3],'includes_births_outside_window':True,'max_predictable_variance_rate':str(max_var),'checked':'midpoint drift, width drift, jump size and variance/intensity bounds'}
Path('midpoint_checks.json').write_text(json.dumps(r,indent=2),encoding='utf8');print(r,flush=True)
