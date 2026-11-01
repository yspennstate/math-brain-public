"""Direct-Walsh witness reconstruction; no imports from previous A078 code."""
from fractions import Fraction as Q
from pathlib import Path
import json,hashlib,time
R=Path(__file__).resolve().parents[1];O=R/'out'
spec=dict(helper_version='independent-direct-walsh-v1',family='two explicit three-bit Boolean witnesses and their actual four-bit lifts',domain='fixed tables in PROOF.md',case_count=2,symmetry='none',arithmetic='direct integer character sums, Fraction masses, rational prime-log vectors, integer strict sign',memory_estimate_MB=20,max_runtime_seconds=30)
(O/'FROZEN_AUDIT_SPEC.json').write_text(json.dumps(spec,indent=2),encoding='utf-8')
start=time.monotonic();count=0
def ck(b):
 global count
 count+=1;assert b,count
 assert time.monotonic()-start<30
def plus(*terms):
 d={}
 for c,v in terms:
  for p,a in v.items():d[p]=d.get(p,Q(0))+c*a
 return {p:a for p,a in d.items() if a}
def log(q):
 d={}
 for s,num in ((1,q.numerator),(-1,q.denominator)):
  p=2
  while p<=num:
   while num%p==0:d[p]=d.get(p,0)+s;num//=p
   p+=1
 return {p:Q(a) for p,a in d.items() if a}
def spectrum(v):
 return [Q(sum(y*(-1 if (s&x).bit_count()%2 else 1) for x,y in enumerate(v)),len(v)) for s in range(len(v))]
def U(v):
 p=[a*a for a in spectrum(v)]
 return plus(*[(a,log(sum((b for t,b in enumerate(p) if t&s==s),Q(0))/a)) for s,a in enumerate(p) if a])
def H(v):return plus(*[(-a*a,log(a*a)) for a in spectrum(v) if a])
def child(v,i,b):return tuple(y for x,y in enumerate(v) if (x>>i)&1==b)
def padding(v,P):return tuple(v[x^P] if z else v[x] for z in (0,1) for x in range(len(v)))
def influence(v,i):return Q(sum(y!=v[x^(1<<i)] for x,y in enumerate(v)),len(v))
def du(v,i):return plus((1,U(v)),(-Q(1,2),U(child(v,i,0))),(-Q(1,2),U(child(v,i,1))))
def discount(v,P):return plus((1,U(v)),(-1,U(padding(v,P))))
records=[]
for mask,P,i,erasure in ((25,5,1,True),(24,3,2,False)):
 v=tuple(1-2*((mask>>x)&1) for x in range(8));F=padding(v,P)
 pc=(P&((1<<i)-1))|((P>>(i+1))<<i)
 d=discount(v,P);ds=[discount(child(v,i,b),pc) for b in (0,1)]
 corr=plus((-1,d),(Q(1,2),ds[0]),(Q(1,2),ds[1]))
 ck(corr==({2:-Q(1,2),3:Q(17,16),5:-Q(1,2)} if erasure else {2:Q(1,2)}))
 ck(du(F,i)==plus((1,du(v,i)),(1,corr)))
 ck(H(F)==H(v));ck(influence(F,i)==influence(v,i))
 ck(influence(F,3)==Q(sum(v[x]!=v[x^P] for x in range(8)),8))
 for table in (v,F):
  a=spectrum(table)
  ck(any(a[s] and a[s|(1<<i)] for s in range(len(a)) if not (s>>i)&1)==erasure)
 ck(ds==([{}, {2:Q(1,2)}] if erasure else [{2:Q(1,2)},{2:Q(1,2)}]))
 # Complete one-query stopping identity, both children, no dropped potential.
 ck(plus((1,U(F)))==plus((1,du(v,i)),(-1,d),(Q(1,2),U(child(v,i,0))),(Q(1,2),U(child(v,i,1)))))
 records.append(dict(mask=mask,P=P,i=i,seed_Walsh=[str(a) for a in spectrum(v)],seed_influences=[str(influence(v,j)) for j in range(3)],padding_influence=str(influence(F,3)),seed_H={str(p):str(a) for p,a in H(v).items()},seed_U={str(p):str(a) for p,a in U(v).items()},lift_U={str(p):str(a) for p,a in U(F).items()},nonzero_erasure=erasure))
ck(3**17==129140163);ck(2**8*5**8==100000000);ck(3**17>2**8*5**8)
result=dict(status='PASS',exact_assertions=count,records=records,strict_sign_integer_certificate=[3**17,2**8*5**8],runtime_seconds=time.monotonic()-start,checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),scope='independent implementation, same author; not independent mathematical review')
(O/'INDEPENDENT_AUDIT.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='records'}))
