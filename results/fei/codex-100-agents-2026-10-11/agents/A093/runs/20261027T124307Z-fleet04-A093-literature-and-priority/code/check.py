from pathlib import Path
from fractions import Fraction as F
import json,time
r=Path(__file__).resolve().parents[1];start=time.perf_counter();checks=0
# Log forms are exact linear combinations of log2(prime), never floats.
def ck(x):
 global checks
 checks+=1
 assert x
 if time.perf_counter()-start>55:raise TimeoutError('55s fixed cap')
def add(*forms):
 d={}
 for a in forms:
  for k,v in a.items():d[k]=d.get(k,F(0))+v
 return {k:v for k,v in d.items() if v}
def scale(t,d):return {k:t*v for k,v in d.items() if t*v}
def logq(x):
 ck(x>0);d={}
 for n,sign in [(x.numerator,1),(x.denominator,-1)]:
  k=2
  while k*k<=n:
   while n%k==0:d[k]=d.get(k,F(0))+sign;n//=k
   k+=1
  if n>1:d[n]=d.get(n,F(0))+sign
 return {k:F(v) for k,v in d.items() if v}
def D(p,q):
 return add(*[scale(v,logq(v/q[j])) for j,v in enumerate(p) if v])
def CE(p,q):return add(*[scale(-v,logq(q[j])) for j,v in enumerate(p) if v])
def H(p):return CE(p,p)
def spec(tab):
 return [F(sum(v*((-1)**((s&x).bit_count()%2)) for x,v in enumerate(tab)),len(tab))**2 for s in range(len(tab))]
def project(p,i):
 n=(len(p)).bit_length()-1;out=[F(0)]*(len(p)//2)
 for s,v in enumerate(p):
  t=(s&((1<<i)-1))|((s>>(i+1))<<i);out[t]+=v
 return out
def child(tab,i,b):
 return [tab[(x&((1<<i)-1))|((x>>i)<<(i+1))|(b<<i)] for x in range(len(tab)//2)]
root_cases=child_cases=0;fixture=None
for special in range(8):
 for sign in [-1,1]:
  tab=[sign*(-1 if x==special else 1) for x in range(8)];P=spec(tab);Q=[F(1,8)]*8
  I=sum((F(s.bit_count())*v for s,v in enumerate(P)),F(0));ck(I==F(3,4));ck(CE(P,Q)=={2:F(3)});ck(4*I==3)
  for i in range(3):
   root_cases+=1;m=project(P,i);q=project(Q,i);ps=[spec(child(tab,i,b)) for b in [0,1]]
   ck(m==[F(5,8)]+[F(1,8)]*3);ck(q==[F(1,4)]*4)
   ck([sum(row[j] for row in ps)/2 for j in range(4)]==m)
   L=add(D(P,Q),scale(-1,D(m,q)));J=scale(F(1,2),add(*(D(p,m) for p in ps)))
   avgD=scale(F(1,2),add(*(D(p,q) for p in ps)))
   ck(add(avgD,scale(-1,D(P,Q)))==add(J,scale(-1,L)))
   gaps=[];fees=[];terminal=[];rs=[];zs=[]
   for p in ps:
    child_cases+=1;raw=[q[j]*v/m[j] for j,v in enumerate(p)];z=sum(raw);R=[v/z for v in raw]
    ck(sum(R)==1);ck(z>0)
    fee=D(R,q);drop=add(D(p,q),scale(-1,D(p,R)));gap=add(fee,scale(-1,drop))
    ck(gap==add(D(p,R),D(R,q),scale(-1,D(p,q))))
    if p==q:
     ck(R==[F(1,16)]+[F(5,16)]*3);ck(z==F(8,5));ck(gap=={5:F(3,16)})
     ck(gap==add(D(p,R),D(R,p)))
    else:
     ck(p==[F(1),F(0),F(0),F(0)]);ck(R==p);ck(z==F(2,5));ck(gap=={})
    gaps.append(gap);fees.append(fee);terminal.append(CE(p,R));rs.append(R);zs.append(z)
   G=scale(F(1,2),add(*gaps));ck(G=={5:F(3,32)})
   delta=add(H(P),scale(F(-1,2),add(*(H(p) for p in ps))))
   bill=add(delta,L,scale(F(1,2),add(*fees,*terminal)))
   ck(bill==add(CE(P,Q),J,G))
   if fixture is None:fixture={'P':[str(x) for x in P],'Q':[str(x) for x in Q],'projected_P':[str(x) for x in m],'projected_Q':[str(x) for x in q],'children':[[str(x) for x in p] for p in ps],'kernel_R':[[str(x) for x in p] for p in rs],'Z':[str(x) for x in zs],'average_gap_log_form':{str(k):str(v) for k,v in G.items()}}
# Partial profile identity, including t=0,1 and a true-zero ghost atom.
p=[F(1,2),F(1,3),F(1,6),F(0)];q=[F(1,4)]*4;pc=[p[0],sum(p[1:])];qc=[q[0],sum(q[1:])]
for t in [F(0),F(1,4),F(1,2),F(3,4),F(1)]:
 mass=[(1-t)*x+t*y for x,y in zip(qc,pc)]
 R=[mass[0]]+[mass[1]*x/qc[1] for x in q[1:]];ck(sum(R)==1)
 slack=add(D(p,q),scale(-1,D(p,R)),scale(-1,D(R,q)))
 if t in [0,1]:ck(slack=={})
 else:ck(slack==scale((1-t)/t,add(D(mass,qc),D(qc,mass))))
# Positive direction of exact witness uses only log2(5)>0; 5>1 rational.
ck(F(5)>1);ck(F(3,32)>0);ck(5**2<2**5)
result={'status':'PASS','root_queries':root_cases,'full_children':child_cases,'exact_assertions':checks,'elapsed_seconds':time.perf_counter()-start,'arithmetic':'Fraction/direct Walsh/exact prime-log cancellation; strict sign5>1','average_gap':'(3/32)log2(5)>0','bound':'gap<15/64 since25<32','pilot_and_main':'same48-query frozen domain,no escalation'}
(r/'out/CHECKS.json').write_text(json.dumps(result,indent=2),encoding='utf-8');(r/'out/BOOLEAN_WITNESS.json').write_text(json.dumps(fixture,indent=2),encoding='utf-8');print(json.dumps(result))
