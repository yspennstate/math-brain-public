"""Independent FWHT, actual Bayes-kernel replay, rational derivative certificates."""
from fractions import Fraction as F
from pathlib import Path
import json,time
R=Path(__file__).resolve().parents[1];start=time.perf_counter();C=0
def ck(x):
 global C
 C+=1;assert x,C;assert time.perf_counter()-start<55
def spectrum(t):
 a=list(t);step=1
 while step<len(a):
  for base in range(0,len(a),2*step):
   for k in range(base,base+step):a[k],a[k+step]=a[k]+a[k+step],a[k]-a[k+step]
  step*=2
 return [F(x*x,len(a)**2) for x in a]
data=json.loads((R/'out/CHECK.json').read_text(encoding='utf-8'));strict=0
for row in data['rows']:
 n,j,S,T=row['n'],row['j'],row['S'],row['T'];alpha=F(row['alpha']);beta=1-alpha
 t=[1-2*((row['table']>>z)&1) for z in range(1<<n)];P=spectrum(t)
 kids=[spectrum([v for z,v in enumerate(t) if (z>>j)&1==y]) for y in [0,1]]
 ck(kids[0]==kids[1]);p=kids[0];u=p[0];v=P[0]
 Q=[beta*x for x in P];Q[0]+=alpha*v;Q[S]+=alpha*(1-v)
 bp=[P[z]+P[z|(1<<j)] for z in range(1<<n) if not (z>>j)&1]
 bq=[Q[z]+Q[z|(1<<j)] for z in range(1<<n) if not (z>>j)&1]
 ck(bp==p)
 for y in [0,1]:
  joint=[q*k/(2*x) if x else F(0) for q,k,x in zip(bq,kids[y],bp)]
  ck(sum(joint)==F(1,2));ck([2*x for x in joint]==bq)
 if T:
  fresh=[beta*x for x in p];fresh[0]+=alpha*u;fresh[T]+=alpha*(1-u)
  shift=alpha*(u-v);ck(shift>=0);ck(fresh[0]==bq[0]+shift);ck(fresh[T]==bq[T]-shift)
  ck(bq[0]<=u and fresh[0]==u);ck(fresh[T]>=p[T] and bq[T]>=fresh[T])
  ck(row['sign']==(-1 if shift>0 else 0));strict+=shift>0
  # Along the entire segment q0<=u and qT>=pT, so dD/dshift<=0.
  for h in [F(0),shift/2,shift]:
   if u:ck(p[T]/(bq[T]-h)<=u/(bq[0]+h))
 else:
  ck(bq==[beta*x+(alpha if z==0 else 0) for z,x in enumerate(p)])
  ck(row['sign']==(-1 if u<1 else 0));strict+=u<1
ck(strict==data['strictly_negative'])
out={'status':'PASS','transactions':len(data['rows']),'assertions':C,'seconds':time.perf_counter()-start,'method':'Independent FWHT; exact common-kernel normalization and rational monotonicity segment certificates'}
(R/'out/AUDIT.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
