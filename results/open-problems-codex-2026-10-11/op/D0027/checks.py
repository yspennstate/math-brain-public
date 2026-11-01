from pathlib import Path
from fractions import Fraction as F
from itertools import product
import json,math,time
start=time.monotonic(); count=0
for q in [F(1,5),F(1,2),F(4,5)]:
 p=1-q
 for n in range(1,6):
  for pin in product([-1,0,1],repeat=n):
   # -1 is free; 0 infected pin; 1 healthy pin.
   exact=F(0);gap=F(0)
   for state in product([0,1],repeat=n):
    pi=math.prod(q if x==0 else p for x in state)
    nu=math.prod((q if x==0 else p) if a==-1 else F(x==a) for a,x in zip(pin,state))
    exact+=nu*nu/pi
    if all(state):gap+=nu
   formula=math.prod(F(1) if a==-1 else 1/(q if a==0 else p) for a in pin)
   assert exact==formula
   gap_formula=F(0) if 0 in pin else p**pin.count(-1)
   assert gap==gap_formula
   count+=1
checks={'date':'2026-10-11','pinning_norm_and_gap_exact_cases':count,'q':['1/5','1/2','4/5'],'n_max':5,'elapsed_seconds':time.monotonic()-start,'status':'PASS'}
Path('checks.json').write_text(json.dumps(checks,indent=2),encoding='utf8');print(checks,flush=True)
