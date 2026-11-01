from pathlib import Path
from fractions import Fraction as F
import json,time,hashlib
from review import kl, combine, bounds
ROOT=Path(__file__).resolve().parents[1]
spec={'helper_version':'fixtures-v1','helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'family':'point defects n2..6; tensor products of2bit defects t1..3; bent XOR origin surgery n2,4,6','domain':'11 roots; every physical coordinate; 3 fixed partitions; 2 complete reference pairs','case_count':264,'symmetry':'none; duplicates retained','arithmetic':'direct integer character sums; Fraction; review.py prime-log intervals','memory_estimate_mb':70,'maximum_runtime_seconds':55,'automatic_dimension_escalation':False}
(ROOT/'out/FROZEN_FIXTURES.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8')
start=time.monotonic();cases=checks=positive=0
roots=[]
for n in range(2,7):roots.append(('point'+str(n),n,[1-2*(x==0) for x in range(2**n)]))
for t in [1,2,3]:
 n=2*t;roots.append(('tensor'+str(t),n,[(-1)**sum(((x>>(2*k))&3)==0 for k in range(t)) for x in range(2**n)]))
for n in [2,4,6]:roots.append(('surgery'+str(n),n,[(-1)**(sum(((x>>(2*k))&3)==3 for k in range(n//2))+(x==0)) for x in range(2**n)]))
for name,n,table in roots:
 for coord in range(n):
  N=2**(n-1); laws=[]
  for bit in [0,1]:
   vals=[table[(y&((1<<coord)-1))|((y>>coord)<<(coord+1))|(bit<<coord)] for y in range(N)]
   coeff=[F(sum(vals[x]*(-1)**((x&s).bit_count()) for x in range(N)),N) for s in range(N)]
   assert sum(x*x for x in coeff)==1;checks+=1
   laws.append([x*x for x in coeff])
  p,q=laws
  pairs=[([(3*x+y)/4 for x,y in zip(p,q)],[(x+3*y)/4 for x,y in zip(p,q)]),([F(1+2*(j%2),2*N) for j in range(N)],[F(3-2*(j%2),2*N) for j in range(N)])]
  partitions=[[list(range(N))],[[j for j in range(N) if j%2==k] for k in [0,1]],[[j for j in range(N) if j.bit_count()%2==k] for k in [0,1]]]
  for rp,rm in pairs:
   m=[(x+y)/2 for x,y in zip(rp,rm)]
   fine=combine((F(1,2),kl(p,rp)),(F(1,2),kl(q,rm)))
   for blocks in partitions:
    coarse={};phi=F(0)
    for block in blocks:
     ap=sum(p[j] for j in block);am=sum(q[j] for j in block);u=sum(rp[j] for j in block);v=sum(rm[j] for j in block)
     coarse=combine((1,coarse),(F(1,2),kl([ap,am],[u,v])))
     if ap and am:
      e=sum(abs(u*p[j]/ap+v*q[j]/am-2*m[j]) for j in block)
      phi+=e*e/(4*(u*u/ap+v*v/am))
     elif ap or am:
      law,w,r=(p,ap,u) if ap else (q,am,v)
      o=sum(max(F(0),r*law[j]/w-2*m[j]) for j in block)
      phi+=w*o*o/(r*r)
    gap=combine((1,fine),(-1,coarse));lo,hi=bounds(gap)
    assert lo>=phi or (not gap and phi==0),(name,coord,str(lo),str(phi))
    positive+=phi>0;cases+=1;checks+=1
 assert time.monotonic()-start<55
assert cases==spec['case_count'],cases
# Independent sharpness enclosure, using the positive power series for -ln(1-z).
sharp=[]
for s in [F(1,8),F(1,32),F(1,128),F(1,512)]:
 z=4*s*s; phi=2*s*s
 lo=sum((z**k/k for k in range(1,13)),F(0))/2
 hi=lo+z**13/(26*(1-z))
 assert phi<=lo<=hi<=phi/(1-z);checks+=1
 sharp.append({'s':str(s),'ratio_lower':str(lo/phi),'ratio_upper':str(hi/phi),'rational_upper':str(1/(1-z))})
out={'status':'PASS','roots':len(roots),'cases':cases,'checks':checks,'positive_phi_cases':positive,'seconds':round(time.monotonic()-start,6),'sharpness':sharp}
(ROOT/'out/FIXTURES.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='sharpness'}))
