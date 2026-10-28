"""Standalone independent representation of the critical inherited conversion."""
from fractions import Fraction as F
from pathlib import Path
import json,time
R=Path(__file__).resolve().parents[1];start=time.perf_counter();checks=0
def ck(x):
 global checks
 checks+=1
 if not x:raise AssertionError(checks)
 if time.perf_counter()-start>60:raise TimeoutError('60s')
def walsh(t):
 return [F(sum(v*(-1)**((s&x).bit_count()) for x,v in enumerate(t)),len(t)) for s in range(len(t))]
def factors(n):
 out={};p=2
 while p*p<=n:
  while n%p==0:out[p]=out.get(p,0)+1;n//=p
  p+=1
 if n>1:out[n]=out.get(n,0)+1
 return out
def logs(x):
 a=factors(x.numerator)
 for p,e in factors(x.denominator).items():a[p]=a.get(p,0)-e
 return {p:F(e) for p,e in a.items() if e}
def add(a,b,k=F(1)):
 out=dict(a)
 for p,e in b.items():out[p]=out.get(p,F(0))+k*e
 return {p:e for p,e in out.items() if e}
def kl(p,q):
 out={}
 for a,b in zip(p,q):
  if a:ck(b>0);out=add(out,logs(a/b),a)
 return out
g=[1 if x.bit_count()!=1 else -1 for x in range(8)]
p=[a*a for a in walsh(g)];ck(p==[F(1,16)]*7+[F(9,16)])
ck(F(sum(g[x]!=g[x^(1<<j)] for j in range(3) for x in range(8)),8)==F(9,4))
q=[p[0]]+[F(5,6)*p[s]+(F(15,96) if s==7 else 0) for s in range(1,8)]
pc=[[a*a for a in walsh([g[2*x+b] for x in range(4)])] for b in (0,1)]
pe=[p[2*x]+p[2*x+1] for x in range(4)]
qe=[q[2*x]+q[2*x+1] for x in range(4)]
outcome=[];inherited=[]
for b in (0,1):
 joint=[qe[x]*pc[b][x]/(2*pe[x]) for x in range(4)]
 outcome.append(sum(joint));inherited.append([a/sum(joint) for a in joint])
ck(outcome==[F(13,24),F(11,24)])
ck(inherited==[[F(0),F(0),F(0),F(1)],[F(1,4),F(5,22),F(5,22),F(13,44)]])
fresh=[[F(0),F(0),F(0),F(1)],[F(1,4),F(5,24),F(5,24),F(1,3)]]
cost={}
for b in (0,1):cost=add(cost,add(kl(pc[b],fresh[b]),kl(pc[b],inherited[b]),-1),F(1,2))
expected={p:e/8 for p,e in logs(F(1404,1331)).items()};ck(cost==expected)
# Polynomial coefficients in ascending powers, separate from the probability calculation.
def poly(a,b):
 out=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]+=x*y
 return out
den=poly(poly(poly([2,-1],[2,-1]),[2,-1]),[1,2])
num=[8,4,0,0,0];ck([a-b for a,b in zip(num,den)]==[0,0,18,-11,2])
ck(18-11>0 and 1404>1331 and 1404<2*1331)
ck(6**3<2*5**3 and 5**3<2*4**3)
# Rational surrogate of the universal upper bound for every integer m>=1.
# coefficient = CE/2-2+sigma_g/2 < -9/32, C<1/6.
ck(F(53,32)-2+F(1,16)==-F(9,32))
ck(F(1,6)-1-F(9,32)<0)
result={'status':'PASS','checks':checks,'seconds':time.perf_counter()-start,'pure_core_sigma':{str(p):str(e) for p,e in cost.items()},'all_alpha_polynomial':[0,0,18,-11,2],'scope':'Independent core reconstruction and universal rational sign; full activation and minimal-dimension clauses of A047 not reviewed'}
(R/'out/AUDIT.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
