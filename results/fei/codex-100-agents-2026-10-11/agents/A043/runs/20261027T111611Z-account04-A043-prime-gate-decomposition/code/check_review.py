"""Separate exact reproduction of the new A041 nonsymmetric boundary."""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
from math import comb
import json,time
R=Path(__file__).resolve().parents[1];out=R/'out'
spec={'helper_version':'A043-A041-independent-review-v1','family':'F_m=sign(3b1+3b2+2sum rare>=5)','domain':'m=3,4; epsilon=1/(8m),1/(64m); m=2 primeness negative control','case_count':5,'symmetry':'none: all proper blocks tested','arithmetic':'integer cofactor rows; direct Fraction physical mixed derivatives, moments and output law','memory_estimate_mb':35,'max_runtime_seconds':55}
(out/'review_frozen_spec.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8')
t0=time.perf_counter();checks=0
def ck(b):
 global checks
 checks+=1;assert b,checks;assert time.perf_counter()-t0<55
def table(m):return tuple(1 if 3*((x&1)+((x>>1)&1))+2*(x>>2).bit_count()>=5 else -1 for x in range(1<<(m+2)))
def rows(a,n,B):
 C=[i for i in range(n) if i not in B]
 return {tuple(a[sum(((u>>j)&1)<<i for j,i in enumerate(B))+sum(((v>>j)&1)<<i for j,i in enumerate(C))] for v in range(1<<len(C))) for u in range(1<<len(B))}
results=[]
for m in (3,4):
 n=m+2;a=table(m)
 ck(all(len(rows(a,n,B))>=3 for k in range(2,n) for B in combinations(range(n),k)))
 for den in (8,64):
  e=F(1,den*m);p=[F(1,2)]*2+[e]*m;v=[4*z*(1-z) for z in p]
  probs=[]
  for x in range(1<<n):
   pr=F(1)
   for i,pi in enumerate(p):pr*=pi if x>>i&1 else 1-pi
   probs.append(pr)
  mean=sum((probs[x]*a[x] for x in range(1<<n)),F(0))
  d=[]
  for i in range(n):
   di=F(0)
   for x in range(1<<n):
    if x>>i&1:continue
    diff=F(a[x|(1<<i)]-a[x],2)
    ck(diff in (0,1));di+=probs[x]/(1-p[i])*diff
   d.append(di)
  q=[F(comb(m,k))*e**k*(1-e)**(m-k) for k in range(m+1)]
  ck(d[0]==d[1]==sum(q[:3])/2)
  qm=[F(comb(m-1,k))*e**k*(1-e)**(m-1-k) for k in range(m)]
  ck(all(di==qm[0]/2+qm[2]/4 for di in d[2:]))
  pair=sum((probs[x]*a[x]*(2*((x&1)-p[0]))*(2*(((x>>1)&1)-p[1])) for x in range(1<<n)),F(0))
  ck(pair==(q[0]-q[1]-q[2])/2);ck(F(3,8)<=pair<=F(1,2))
  I=sum(vv*di for vv,di in zip(v,d));Delta=I-(1-mean*mean)
  ck(-F(1,2)<=mean<=-F(1,4));ck(I<=1+2*m*e);ck(Delta<=F(1,4)+2*m*e)
  a3=comb(m,3)*e**3
  ck(d[0]>F(1,4));ck(d[0]<=F(1,2));ck(2*d[0]**2>=F(1,2)-a3)
  ck(2*Delta-2*d[0]**2<=5*m*e)
  # Degree >=3, independently certified by a restriction to Maj3.
  vals=[a[x] for x in range(8)]
  ck(vals==[1 if x.bit_count()>=2 else -1 for x in range(8)])
  results.append({'m':m,'epsilon':str(e),'Delta':str(Delta),'pair_mass':str(pair*pair),'conservative_ratio_lower':str(F(9,320*m)/e)})
a=table(2);ck(len(rows(a,4,(2,3)))==2)
result={'status':'PASS','assertions':checks,'cases':5,'seconds':time.perf_counter()-t0,'results':results}
(out/'review_results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:result[k] for k in ('status','assertions','cases','seconds')}))
