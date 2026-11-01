from pathlib import Path
from fractions import Fraction as F
import json,time
R=Path(__file__).resolve().parents[1];start=time.monotonic();checks=0
def ck(x):
 global checks
 checks+=1;assert x,checks;assert time.monotonic()-start<55
def spectrum(v):
 return [F(sum(v[x]*(-1)**((x&s).bit_count()%2) for x in range(len(v)))**2,len(v)**2) for s in range(len(v))]
rows=[]
for m in [2,3]:
 A=F(1,2**m);d=A*A
 v=[(-1)**sum(((x>>(2*j))&3)==3 for j in range(m))-2*(x==0) for x in range(2**(2*m+1))]
 p=spectrum(v);q1=[p[2*x]+p[2*x+1] for x in range(len(p)//2)]
 q2=[sum(p[4*x+j] for j in range(4)) for x in range(len(p)//4)]
 v0=v[0::2];v1=v[1::2];p0=spectrum(v0)
 T=sum((p0[x]*(q2[x//2]/(2*q1[x])-1) for x in range(len(p0))),F(0));ck(T==2*d/(1+d))
 for vchild,q,bound in [(v1,q1,2),(v0[0::2],q2,4),(v0[1::2],q2,None)]:
  ck(all(x in [-1,1] for x in vchild));pv=spectrum(vchild);ck(sum(pv)==1);ck(sum(q)==1)
  for pp,qq in zip(pv,q):
   ck(qq>0)
   if pp:ck(pp<=bound*qq if bound else pp*pp<2*qq*qq)
 # Rational certificate for the only numerical constant used in terminal bound.
 ck(F(16,13)**2<2)
 rows.append({'m':m,'partner_log_linear_expectation':str(T),'terminal_ratio_bounds':['2','4','squared ratio < 2']})
result={'status':'PASS','checks':checks,'runtime_seconds':time.monotonic()-start,'rows':rows,'independence':'Direct O(N^2) character sums; no FFT, imported helper or logarithm routine'}
(R/'out/INDEPENDENT_AUDIT.json').write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result))
