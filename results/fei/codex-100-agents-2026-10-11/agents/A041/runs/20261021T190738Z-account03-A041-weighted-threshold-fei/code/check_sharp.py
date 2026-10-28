from pathlib import Path
from fractions import Fraction as Q
from itertools import product
from math import comb
import json,time,hashlib
R=Path(__file__).resolve().parents[1];O=R/'out';O.mkdir(exist_ok=True)
spec={'helper':'A041-sharp-two-jump-v1','family':'F=2*1{number of zero inputs<=1}-1; split a+b; genuine real-weight representation 1<w<2,t=aw+b-w','domains':{'direct_tables':'a=b=2; all 81 labeled biases in {1/4,1/2,3/4}^4','compressed_counts':'a=b in {2,3,4,8,16,32,64}; plus (2,3),(3,2)','review':'AND_d d=3,4,5,8,16; analytic all-d variance argument'},'case_count':95,'symmetry':'only exact fair separate-count formulas for compressed checks; direct tables use no quotient','arithmetic':'Fraction and integer binomial coefficients','memory_estimate_MB':100,'maximum_runtime_seconds':60}
(O/'FROZEN_SHARP_SPEC.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8')
src=R.parent/'20261014T083216Z-account05-A041-weighted-threshold-fei/code/check_stage.py'
ns={'__file__':str(__file__)};exec(compile(src.read_text(encoding='utf-8').split('parser=')[0],str(src),'exec'),ns)
reference=ns['reference'];transform=ns['transform'];start=time.monotonic();checks=0
def ck(x):
 global checks
 assert x
 checks+=1
def direct_coefficient(vals,p,S):
 # Independent expectation of f times the unnormalized centered basis.
 total=Q(0)
 for x,f in enumerate(vals):
  term=Q(f)
  for i,q in enumerate(p):
   bit=(x>>i)&1
   term*=q if bit else 1-q
   if S>>i&1:term*=bit-q
  total+=term
 scale=Q(1)
 for i,q in enumerate(p):
  if S>>i&1:scale*=q*(1-q)
 return total*total/scale
rows=[]
for p in product((Q(1,4),Q(1,2),Q(3,4)),repeat=4):
 vals=[2*int(x.bit_count()>=3)-1 for x in range(16)]
 _,P,v=transform(vals,p);KA,_=reference(vals,p,2,'A');KB,_=reference(vals,p,2,'B')
 for s in range(16):ck(P[s]==direct_coefficient(vals,p,s))
 for s in range(16):
  if s&3 and s>>2:ck(P[s]<=2*KA[s]);ck(P[s]<=2*KB[s])
 ck(P[15]==9*v[15]/64);ck(KA[15]==5*v[15]/64);ck(KB[15]==5*v[15]/64)
 rows.append({'p':list(map(str,p)),'top_P':str(P[15]),'top_Kstar':str(max(KA[15],KB[15])),'ratio':'9/5'})
compressed=[]
for a,b in [(m,m) for m in (2,3,4,8,16,32,64)]+[(2,3),(3,2)]:
 n=a+b;M=D=Z=overlap=Q(0)
 for u in range(1,a+1):
  for t in range(1,b+1):
   den=4**(n-1);mult=comb(a,u)*comb(b,t)
   pp=Q((n+1-2*(u+t))**2,den)
   ka=Q((a+1-2*u)**2+(b-2*t)**2,den)
   kb=Q((a-2*u)**2+(b+1-2*t)**2,den)
   ck(pp<=2*ka);ck(pp<=2*kb)
   M+=mult*pp;D+=mult*(u+t-1)*pp;Z+=mult*max(ka,kb);overlap+=mult*min(ka,kb)
 top=Q((n-1)**2,max((a-1)**2+b*b,a*a+(b-1)**2))
 ck(1<top<2)
 if a==b:ck(top==2-Q(1,a*a+(a-1)**2))
 compressed.append({'a':a,'b':b,'top_ratio':str(top),'M':str(M),'D':str(D),'Zstar':str(Z),'overlap':str(overlap)})
 ck(time.monotonic()-start<60)
review=[]
for d in (3,4,5,8,16):
 ps=tuple(Q(i+1,d+2) for i in range(d))
 for i,p in enumerate(ps):
  v=[4*q*(1-q) for q in ps];VT=Q(1)
  for j,z in enumerate(v):
   if j!=i:VT*=z
  top=Q(4)
  for q in ps:top*=q*(1-q)
  ck(4**(d-2)*top/VT==p*(1-p))
 review.append({'d':d,'required_owner_mass':d,'degree_capacity':d-1,'ratio':str(Q(d,d-1))})
ck(all(Q((j-4)**2,16)!=Q(3,5) for j in range(9)))
out={'helper':spec['helper'],'cases':len(rows)+len(compressed)+len(review),'assertions':checks,'runtime_seconds':time.monotonic()-start,'direct_all_bias_formula':rows,'compressed_family':compressed,'A045_review':review,'AND3_phase_obstruction':'normalized empty mass 3/5 not in {(j-4)^2/16:j=0..8}'}
(O/'SHARP_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k not in ('direct_all_bias_formula','compressed_family','A045_review')}))
