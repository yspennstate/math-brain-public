from fractions import Fraction as Q
from pathlib import Path
import json,time
RUN=Path(__file__).resolve().parents[1];START=time.perf_counter();checks=0
def ck(b):
 global checks
 assert b;checks+=1
 if time.perf_counter()-START>60:raise RuntimeError('Frozen 60-second cap')
def ln(x):
 if x<1:
  a,b=ln(1/x);return -b,-a
 z=(x-1)/(x+1);power=z;s=Q(0);T=40
 for k in range(T):s+=power/(2*k+1);power*=z*z
 return 2*s,2*s+2*power/((2*T+1)*(1-z*z))
def scale(c,a):return (c*a[0],c*a[1]) if c>=0 else (c*a[1],c*a[0])
def add(*args):return tuple(sum(a[i] for a in args) for i in [0,1])
def F(x):return scale(2*(1+x)**2,ln(1+x))
rows=[]
for m in range(4,41,2):
 e=Q(1,1<<(m//2));d=e*e
 D=scale(Q(1,2),add(scale(1-e,F(2*e)),scale(1+e,F(-2*e))))
 J=scale(Q(1,4),add(scale(1-2*e,F(e)),scale(1+2*e,F(-e))))
 combined=add(scale(Q(1,2),D),scale(-1,J))
 ck(D[1]<8*d);ck(J[0]>=-d/2-Q(3,4)*d*d/(1-d))
 ck(combined[1]<Q(9,2)*d)
 for l in range(2,21):
  u=(2*l)*(2*l-1)*(2*l-2);v=(2*l-1)*(2*l-2)*(2*l-3)
  ck(u>0 and v>0)
  Dcoef=-Q(4*4**l,u)-Q(4*2**(2*l-1),v)
  Jcoef=-Q(2,u)-Q(4,v)
  K=Q(2*(4**l-1),u)+Q(4**l-4,v)
  ck(Dcoef/2-Jcoef==-K);ck(K>0)
 rows.append({'m':m,'D_natural_interval':list(map(str,D)),'J_natural_interval':list(map(str,J)),'combined_interval':list(map(str,combined)),'strict_upper':str(Q(9,2)*d)})
lo,hi=ln(Q(2));ck(lo>Q(2,3));ck(Q(9,4)/lo+Q(1,4)<4)
result={'status':'PASS','cases':len(rows),'exact_assertions':checks,'elapsed_seconds':time.perf_counter()-START,'method':'Independent Fraction natural-log intervals and exact combined coefficient identity; no helper import'}
(RUN/'out/independent_rows.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8')
(RUN/'out/independent_validation.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result))
