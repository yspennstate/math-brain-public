from fractions import Fraction as F
from pathlib import Path
import json,time
from functools import lru_cache
import exact as E
from reduced import local
R=Path(__file__).resolve().parents[1];start=time.perf_counter();C=0
def ck(x):
 global C
 C+=1;assert x,C;assert time.perf_counter()-start<55
@lru_cache(None)
def target(w,b):
 d=F(1,2**w);p=[(1-2*d)**2]+[4*d*d]*((1<<w)-1);q=[p[0]]+[b*x for x in p[1:]];q[-1]+=(1-b)*(1-p[0]);return E.kl(p,[E.iv(x) for x in q])
rows=[]
for w in range(2,11):
 for j in range(-8,9):
  for b in [F(5,6),F(4,5),F(9,10)]:
   same,outs,*_=local(w,F(j,8),b);ck(same[1]<0)
   for bn in [b,(b+F(4,5))/2,F(4,5)]:
    diff=E.iv(0) if w==2 else E.scale(F(1,4),E.sub(target(w-1,bn),target(w-1,b)))
    var=F(0) if w==2 else 1-(1-F(1,2**(w-2)))**2
    cap=E.scale(var/4,E.logpoint(b/bn));changed=E.add(same,diff)
    ck(changed[1]<cap[0]);ck(diff[0]>=0 or diff[0]<=0<=diff[1])
    if b!=bn and w>=3:ck(diff[1]<cap[0])
    rows.append({'w':w,'mu':str(F(j,8)),'old_beta':str(b),'new_beta':str(bn),'sigma':E.enc(changed),'increment':E.enc(diff),'cap':E.enc(cap)})
 E.logpoint.cache_clear()
o={'status':'PASS','cases':len(rows),'assertions':C,'primitive_assertions':E.checks,'seconds':time.perf_counter()-start,'rows':rows};(R/'out/SCALARS.json').write_text(json.dumps(o,indent=2),encoding='utf-8');print(json.dumps({k:v for k,v in o.items() if k!='rows'}))
