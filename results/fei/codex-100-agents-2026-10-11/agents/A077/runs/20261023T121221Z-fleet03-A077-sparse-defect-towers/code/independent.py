from pathlib import Path
from fractions import Fraction as F
from math import comb
import itertools,json,time
R=Path(__file__).resolve().parents[1]
start=time.perf_counter();checks=0;rows=[]
def check(x):
 global checks
 checks+=1
 assert x
def walsh(v):
 a=list(map(F,v));N=len(a);step=1
 while step<N:
  for j in range(0,N,2*step):
   for k in range(j,j+step):a[k],a[k+step]=a[k]+a[k+step],a[k]-a[k+step]
  step*=2
 return [x/N for x in a]
def maj(s,d):return 1 if 2*s.bit_count()<d else -1
for d in range(5,34,2):
 for b in range(1,(d-3)//2+1):
  c=d-b;p=F(1,2**c);I0=F(d*comb(d-1,(d-1)//2),2**(d-1));cap=4*(c-1)*p
  check(c>=4);check(cap<=F(3,4));check(I0>=F(15,8));check(5*(I0-cap)>=3*I0);check(96*I0<=160*(I0-cap))
  check(26<=F(208,15)*I0);check(F(343,15)*I0<=F(343,9)*(I0-cap))
  rows.append({'d':d,'b':b,'c':c,'I0':str(I0),'loss_bound':str(cap)})
physical=[]
for d,b in [(5,1),(7,1),(7,2),(9,3)]:
 c=d-b;N=1<<d;p=F(1,1<<c);h=[maj(s,d) for s in range(N)];lab=[1 if s%(1<<c)==0 else 2 if s%(1<<c)==1 else 0 for s in range(N)]
 check(lab.count(1)==lab.count(2)==2**b)
 for a in (1,2):
  check(all(h[s]==1 for s in range(N) if lab[s]==a));check(sum(abs(x) for x in walsh([int(t==a) for t in lab]))==1)
 I0=sum(F(sum(h[s]!=h[s^(1<<j)] for s in range(N)),N) for j in range(d))
 for v in itertools.product((-1,1),repeat=2):
  for w in itertools.product((-1,1),repeat=2):
   prof={1:v,2:w};mu={a:F(sum(t),2) for a,t in prof.items()};delta=F(sum(v[t]!=w[t] for t in range(2)),2)
   def val(s,t):return prof[lab[s]][t] if lab[s] else h[s]
   actual=sum(F(sum(val(s,t)!=val(s^(1<<j),t) for s in range(N) for t in range(2)),2*N) for j in range(d))
   formula=F(0)
   for j in range(d):
    for s in range(N):
     t=s^(1<<j);a,z=lab[s],lab[t]
     if not a and not z:cost=F(h[s]!=h[t])
     elif a and z:cost=F(0) if a==z else delta
     elif a:cost=(1-mu[a]*h[t])/2
     else:cost=(1-mu[z]*h[s])/2
     formula+=cost/N
   check(actual==formula);check(actual>=I0-4*(c-1)*p);check(5*actual>=3*I0);check(160*actual>=96*I0)
   private_actual=F(sum(val(s,0)!=val(s,1) for s in range(N)),N)
   check(private_actual==p*(int(v[0]!=v[1])+int(w[0]!=w[1])))
   physical.append({'d':d,'b':b,'v':list(v),'w':list(w),'actual_shared_influence':str(actual),'carrier_influence':str(I0)})
   assert time.perf_counter()-start<55
out={'status':'PASS','exact_assertions':checks,'analytic_parameter_cases':len(rows),'actual_profile_roots':len(physical),'rows':rows,'physical_roots':physical,'seconds':time.perf_counter()-start,'scope':'Independent implementation; rational physical edges and Walsh l1, not peer review.'}
(R/'out/INDEPENDENT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k not in ('rows','physical_roots')}))
