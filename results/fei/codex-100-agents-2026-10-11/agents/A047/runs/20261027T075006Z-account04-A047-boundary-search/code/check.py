from fractions import Fraction as F
from pathlib import Path
from math import lcm
import sys,json,time
R=Path(__file__).resolve().parents[1];O=R/'out';O.mkdir(exist_ok=True)
start=time.perf_counter();pilot='--pilot' in sys.argv;checks=0
def require(b):
 global checks
 checks+=1
 assert b
 if time.perf_counter()-start>55:raise TimeoutError('frozen 55-second cap')
def add(*xs):
 d={}
 for x in xs:
  for p,a in x.items():d[p]=d.get(p,F(0))+a
 return {p:a for p,a in d.items() if a}
def mul(c,x):return {p:c*a for p,a in x.items() if c*a}
def log(x):
 x=F(x);assert x>0;d={}
 for n,sgn in [(x.numerator,1),(x.denominator,-1)]:
  p=2
  while p*p<=n:
   while n%p==0:d[p]=d.get(p,0)+sgn;n//=p
   p+=1
  if n>1:d[n]=d.get(n,0)+sgn
 return {p:F(a) for p,a in d.items() if a}
def kl(p,q):
 return add(*(mul(a,log(a/b)) for a,b in zip(p,q) if a))
def sign(x):
 den=lcm(*(a.denominator for a in x.values()));left=right=1
 for p,a in x.items():
  k=int(a*den)
  if k>0:left*=p**k
  else:right*=p**(-k)
 return (left>right)-(left<right)
def d(t,u):
 if t==1:return {}
 return add(mul(1-t,log(1/(1-u))),mul(t,log(t/(t+u*(1-t)))) if t else {})
def mix(p,u,j):return [(1-u)*a+(u if i==j else 0) for i,a in enumerate(p)]
grid=[F(0),F(1,4),F(1,2),F(3,4)];cases=0;source_count=0
for a in range(5):
 for b in range(5-a):
  for c in range(5-a-b):
   p=list(map(lambda z:F(z,4),[a,b,c,4-a-b-c]));pi=p[2]+p[3]
   if not pi:continue
   source_count+=1
   if pilot and source_count>3:continue
   cond=[p[2]/pi,p[3]/pi]
   for rho in [F(1,4),F(1,2),F(3,4),F(1)]:
    if rho==1 and pi<1:continue
    for beta in grid:
     for old in range(2):
      q=[(1-rho)/2]*2+[rho*x for x in mix(cond,beta,old)]
      credit=kl(p[:2]+[pi],q[:2]+[rho])
      require(sign(credit)>=0)
      require(kl(p,q)==add(credit,mul(pi,d(cond[old],beta))))
      for target in range(2):
       prev=None
       for floor in grid:
        fresh=p[:2]+[pi*x for x in mix(cond,floor,target)]
        price=add(kl(p,fresh),mul(-1,kl(p,q)))
        formula=add(mul(pi,d(cond[target],floor)),mul(-pi,d(cond[old],beta)),mul(-1,credit))
        require(price==formula)
        if prev is not None:require(sign(add(price,mul(-1,prev)))>=0)
        prev=price;cases+=1
# Adversarial incoming mismatch, matched control, and unrelated-target failure.
p=[F(1,4),F(3,4),F(0)];q=[F(1,2),F(1,2),F(0)]
fresh=[F(1,4),F(2,3),F(1,12)]
price=add(kl(p,fresh),mul(-1,kl(p,q)))
require(mul(4,price)==log(F(27,32)));require(sign(price)<0)
require(sign(kl(p,fresh))>0)
require(sign(add(d(F(0),F(1,4)),mul(-1,d(F(1),F(1,2)))))>0)
def spectrum(table):
 n=len(table);return [F(sum(v*(-1 if (x&s).bit_count()%2 else 1) for x,v in enumerate(table)),n) for s in range(n)]
children=[]
for branch in range(2):
 tab=[]
 for x in range(8):
  xx=-1 if x&1 else 1; yy=-1 if x&2 else 1;zz=-1 if x&4 else 1
  tab.append((xx if zz==1 else yy) if branch==0 else xx*yy*zz)
 children.append([z*z for z in spectrum(tab)])
table=[]
for x in range(16):
 a=x&1;xx=-1 if x&2 else 1;yy=-1 if x&4 else 1;zz=-1 if x&8 else 1
 table.append((xx if zz==1 else yy) if a==0 else xx*yy*zz)
P=[z*z for z in spectrum(table)];bar=[P[2*t]+P[2*t+1] for t in range(8)]
require(P.count(F(1,16))==8 and P.count(F(1,4))==2)
require(sum(F(s.bit_count())*p for s,p in enumerate(P))==F(11,4))
require(mul(-1,add(*(mul(p,log(p)) for p in P if p)))==log(8))
alphas=[F(1,16),F(1,8),F(1,4),F(1,2),F(3,4),F(15,16)]
circuit_cases=0
for alpha in alphas[:2] if pilot else alphas:
 Q=mix(P,alpha,15);qb=[Q[2*t]+Q[2*t+1] for t in range(8)]
 joints=[[qb[t]*(children[y][t]/(2*bar[t]) if bar[t] else F(1,2)) for t in range(8)] for y in range(2)]
 outcomes=[sum(row) for row in joints]
 require(outcomes==[(1-alpha)/2,(1+alpha)/2])
 inherited=[[a/outcomes[y] for a in joints[y]] for y in range(2)]
 require(inherited==children)
 K=kl(P,Q);outcome=kl([F(1,2)]*2,outcomes)
 E=add(K,mul(-1,kl(bar,qb)))
 require(sign(E)>=0);require(kl(bar,qb)==outcome)
 formula=add(mul(F(-3,4),log(1-alpha)),mul(F(-1,4),log(1+3*alpha)))
 require(K==formula);require(outcome==mul(F(-1,2),log(1-alpha*alpha)))
 for gamma in alphas[:1] if pilot else alphas:
  bill=mul(F(1,2),add(*(kl(ch,mix(ch,gamma,7)) for ch in children)))
  require(bill==mul(F(-1,2),log(1-gamma)));require(sign(bill)>0)
  require(add(E,outcome,bill)==add(K,bill))
  circuit_cases+=1
# A separate exact derivative numerator reconstruction (no differentiation engine).
for t in [F(1,16),F(1,4),F(1,2),F(15,16)]:
 for u in alphas:
  require((1-t)/(1-u)-t*(1-t)/(t+u*(1-t))==u*(1-t)/((1-u)*(t+u*(1-t))))
result={'status':'PASS','pilot':pilot,'finite_profiles':cases,'boolean_circuit_pairs':circuit_cases,'assertions':checks,'seconds':time.perf_counter()-start,'arithmetic':'Fraction, canonical prime-log identities, integer power signs','scope':'independent finite reconstruction; analytic continuum proof separate'}
(O/('PILOT.json' if pilot else 'CHECK.json')).write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result))
