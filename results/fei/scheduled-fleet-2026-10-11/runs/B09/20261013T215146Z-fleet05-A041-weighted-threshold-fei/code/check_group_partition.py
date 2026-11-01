from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json,time
R=Path(__file__).resolve().parents[1]; start=time.monotonic(); checks=0; rows=[]
def ck(x):
 global checks
 assert x
 checks+=1
for r in range(1,7):
 for sizes in product((1,2,3),repeat=r):
  ck(sum(a-1 for a in sizes)+(r-1)==sum(sizes)-1)
  if r>=2:ck(3*sum(a>=2 for a in sizes)<=6*(r-1))
for sizes in ((2,2,1),(2,2,2)):
 n=sum(sizes); weights=[w for w,a in zip((1,2,3),sizes) for _ in range(a)]
 masks=[]; offset=0
 for a in sizes:masks.append(((1<<a)-1)<<offset);offset+=a
 profiles=[(Q(1,2),)*n,tuple([Q(1,8),Q(1,2),Q(7,8)][i%3] for i in range(n))]
 for p,t in product(profiles,range(1,sum(weights)+1)):
  vals=[Q(2*int(sum(w for i,w in enumerate(weights) if x>>i&1)>=t)-1) for x in range(1<<n)]
  u=vals[:]
  for i,q in enumerate(p):
   step=1<<i
   for base in range(0,len(u),2*step):
    for j in range(step):
     a,b=u[base+j],u[base+j+step]
     u[base+j]=(1-q)*a+q*b;u[base+j+step]=b-a
  d=Rcost=corr=Q(0); D=[Q(0)]*3;total=Q(0)
  for s,z in enumerate(u):
   factor=Q(1)
   for i,q in enumerate(p):
    if s>>i&1:factor*=q*(1-q)
   mass=z*z*factor;total+=mass
   if not s:continue
   aa=[(s&m).bit_count() for m in masks];r=sum(a>0 for a in aa)
   d+=(s.bit_count()-1)*mass;Rcost+=(r-1)*mass
   if r>=2:corr+=3*sum(a>=2 for a in aa)*mass
   for j,a in enumerate(aa):
    if a:D[j]+=(a-1)*mass
  ck(total==1);ck(d==sum(D)+Rcost);ck(corr<=6*Rcost)
  rows.append({'sizes':sizes,'threshold':t,'biases':[str(q) for q in p],'Delta':str(d),'group_deficits':[str(v) for v in D],'cross_group_reserve':str(Rcost),'jensen_correction':str(corr)})
out={'helper':'A041-group-partition-v1','occupation_patterns':sum(3**r for r in range(1,7)),'actual_three_weight_cases':len(rows),'assertions':checks,'runtime_seconds':time.monotonic()-start,'certificates':rows}
(R/'out/GROUP_PARTITION_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='certificates'},indent=2))
