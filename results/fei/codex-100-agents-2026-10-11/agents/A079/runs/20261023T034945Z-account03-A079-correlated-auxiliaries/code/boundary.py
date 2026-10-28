"""Targeted support boundary certificates; no new dimensions."""
import check as c
from fractions import Fraction as F
from pathlib import Path
import time,hashlib,json
start=time.monotonic()
hs=[(1,),(-1,),(-1,1),(1,-1),(-1,1,-1,1),(1,-1,-1,1),(-1,1,1,1),(1,-1,-1,-1)]
states=[(-1,)*4,(0,0,0,0),(1,0,0,0),(0,0,1,0)]
cases=actions=0
for h in hs:
 r=c.prob(h)
 target=tuple(F(t==len(h)-2) for t in range(len(h)-1))
 for st in states:
  if time.monotonic()-start>45:raise TimeoutError('boundary frozen45s')
  a,b=c.rows(st);refs,old=c.review(a,b,h,r,target)
  for s,(_,rc) in zip((1,-1),refs):
   for kind,n in [('seed',len(h).bit_length()-1),('controller',len(a).bit_length()-1)]:
    for i in range(n):c.step(a,b,h,rc,s,kind,i);actions+=1
   cases+=1
out=dict(status='PASS',signed_cases=cases,query_actions=actions,assertions=c.checks,seconds=time.monotonic()-start,source='true-support-only reference, including empty-zero and point endpoints',target='nonempty point law, including ghost atoms',helper_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),core_sha256=hashlib.sha256(Path(c.__file__).read_bytes()).hexdigest())
c.save('boundary.json',out);print(json.dumps(out))
