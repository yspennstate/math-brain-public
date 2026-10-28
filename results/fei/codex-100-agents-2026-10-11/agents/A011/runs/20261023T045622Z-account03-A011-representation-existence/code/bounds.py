import sys
sys.dont_write_bytecode=True
import check as core
from fractions import Fraction as F
from pathlib import Path
import time,json
RUN=Path(__file__).resolve().parents[1];start=time.monotonic();cases=0
for m in range(1,4):
 for label in range(2**(2**m)):
  v=tuple(1 if label>>x&1 else -1 for x in range(2**m));P=core.spectrum(v)
  for r in range(1,4):
   for mode in range(3):
    Q=P if mode==0 else tuple(z/2 for z in P) if mode==1 else tuple(F(x+1,3*sum(range(1,len(P)+1))) for x in range(len(P)))
    c=core.ce(P,Q);vv,qq=core.point(v,Q,r,0,F(8));PP=core.spectrum(vv);rho=F(1,2**(m+r));beta=8*rho
    for T,p in enumerate(P):
     q=sum(PP[u*len(P)+T] for u in range(2**r));core.ck(q<=F(3,2)*p+beta/F(len(P)))
    core.ck(core.ce(PP,qq)[1]<=F(3,2)*c[1]+40*rho*(m+r));cases+=1
    if time.monotonic()-start>55:raise RuntimeError('frozen55second cutoff')
for r in range(1,65):
 p=F(1,2**r);zero=(1-2*p)**2;atom=4*p*p;H=(F(0),F(0))
 if zero:
  l,h=core.shared.log(1/zero);H=(zero*l,zero*h)
 l,h=core.shared.log(1/atom);H=(H[0]+(2**r-1)*atom*l,H[1]+(2**r-1)*atom*h)
 core.ck(H[1]<=16*p*r)
out={'status':'PASS','local_floor_reference_cases':cases,'scalar_collapse_widths':64,'exact_assertions':core.checks,'seconds':time.monotonic()-start,'independence':'local bound audit shares primary transform; separate direct-character replay is independent'}
(RUN/'out/BOUND_RESULTS.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
