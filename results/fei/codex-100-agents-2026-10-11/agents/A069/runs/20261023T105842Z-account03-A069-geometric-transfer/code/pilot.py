from pathlib import Path
from fractions import Fraction as R
from itertools import product
from math import log2
from rational import fw
import json,time
RUN=Path(__file__).resolve().parents[1];start=time.monotonic();worst=(-100,None);cases=0
for ca,cb in product(range(16),repeat=2):
 aa=[1 if ca>>y&1 else -1 for y in range(4)];bb=[1 if cb>>y&1 else -1 for y in range(4)]
 for m,theta,eps in product((1,2),(0,1),(-1,1)):
  N=1<<m;rho=R(1,N);t=rho*rho;A=(1+3*t*theta)/4;B=5*(1-t*theta)/16;r=7*(1-t*theta)/R(32*(N-1));tab=[]
  for y,z,c in product(range(4),range(N),range(2)):
   p=R(aa[y]+bb[y],2);q=R(aa[y]-bb[y],2)
   tab.append((eps*p+(-1 if c else 1)*q)*(-1 if c==0 and z==0 else 1))
  P=[R(x*x,len(tab)**2) for x in fw(tab)];delta=0.
  for s,v in enumerate(P):
   ctrl=s%(2*N);c=ctrl&1;z=ctrl>>1;mass=A if ctrl==0 else B if ctrl==1 else r
   other=(A if c==0 else B) if (z^1)==0 else r
   delta+=float(v)*log2(float(1+other/mass))
  inf=R(sum(tab[x]!=tab[x^2] for x in range(len(tab))),len(tab));ex=delta-float(4*inf)
  cases+=1
  if ex>worst[0]:worst=(ex,[ca,cb,m,theta,eps])
  assert time.monotonic()-start<55
out={'status':'DISCOVERY_ONLY','cases':cases,'largest_private_excess':worst,'elapsed_seconds':time.monotonic()-start}
(RUN/'out/PILOT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
