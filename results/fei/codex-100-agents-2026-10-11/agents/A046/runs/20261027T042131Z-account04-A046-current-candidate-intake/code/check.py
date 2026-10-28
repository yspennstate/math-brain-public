from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
from math import lcm
import json,time,sys
START=time.perf_counter(); COUNT=0
RUN=Path(__file__).resolve().parents[1]
def ok(x):
 global COUNT
 COUNT+=1
 if not x: raise AssertionError(COUNT)
 if time.perf_counter()-START>55: raise TimeoutError('55 second frozen cap')
@lru_cache(None)
def factors(n):
 d=2; out={}
 while d*d<=n:
  while n%d==0: out[d]=out.get(d,0)+1; n//=d
  d+=1
 if n>1: out[n]=out.get(n,0)+1
 return out
class Log:
 def __init__(self): self.c={}
 def add(self,w,r):
  if not w:return self
  assert r>0
  for n,sg in [(r.numerator,1),(r.denominator,-1)]:
   for k,e in factors(n).items():
    self.c[k]=self.c.get(k,F(0))+sg*w*e
    if not self.c[k]: del self.c[k]
  return self
 def plus(self,b,scale=F(1)):
  z=Log(); z.c=self.c.copy()
  for k,e in b.c.items():
   z.c[k]=z.c.get(k,F(0))+scale*e
   if not z.c[k]:del z.c[k]
  return z
 def sign(self):
  den=lcm(*(x.denominator for x in self.c.values())) if self.c else 1
  a=b=1
  for p,e in self.c.items():
   n=int(e*den)
   if n>0:a*=p**n
   else:b*=p**(-n)
  return (a>b)-(a<b)
 def dump(self):return {str(p):str(e) for p,e in sorted(self.c.items())}
def kl(p,q):
 z=Log()
 for a,b in zip(p,q):
  if a:z.add(a,a/b)
 return z
def ce(p,q):
 z=Log()
 for a,b in zip(p,q):
  if a:z.add(a,1/b)
 return z
def spike(p,j,u):return [(1-u)*x+(u if i==j else 0) for i,x in enumerate(p)]
def d(t,u):
 if t==0:return Log().add(F(1),1/(1-u))
 if t==1:return Log()
 return Log().add(1-t,1/(1-u)).add(t,t/(t+u*(1-t)))
def scaled(z,x):return Log().plus(z,x)
pilot='--pilot' in sys.argv
casecount=0; free=0; paid=0
for pi in ([F(3,4)] if pilot else [F(1,4),F(3,4),F(1)]):
 for rho in [F(1,4),F(3,4)]:
  for a in range(5):
   for b in range(5-a):
    s=[F(a,4),F(b,4),F(4-a-b,4)]
    p=[(1-pi)/2,(1-pi)/2]+[pi*x for x in s]
    for M in range(3):
     for E in range(3):
      for beta in ([F(1,2)] if pilot else [F(0),F(1,7),F(1,2),F(3,4)]):
       q=[(1-rho)/3,2*(1-rho)/3]+[rho*x for x in spike(s,M,beta)]
       L=Log().add(pi,pi/rho)
       for x,y in zip(p[:2],q[:2]):
        if x:L.add(x,x/y)
       ok(L.sign()>=0)
       old=kl(p,q); ok(old.c==L.plus(d(s[M],beta),pi).c)
       prev=None
       for gamma in [F(0),F(1,9),F(1,2),F(3,4)]:
        r=p[:2]+[pi*x for x in spike(s,E,gamma)]
        direct=ce(p,r).plus(ce(p,q),-1)
        formula=scaled(d(s[E],gamma).plus(d(s[M],beta),-1),pi).plus(L,-1)
        ok(direct.c==formula.c)
        ok(kl(p,r).c==scaled(d(s[E],gamma),pi).c)
        if prev is not None:ok(direct.plus(prev,-1).sign()>=0)
        if M==E and gamma<=beta:ok(direct.sign()<=0);free+=1
        if M==E and pi==rho and pi==1 and gamma>beta and s[E]<1:ok(direct.sign()>0);paid+=1
        prev=direct;casecount+=1
# Adversarial prepaid-vacuum contrast: identical beta=0 and positive floor.
p=[F(1,4),F(3,4),F(0)]; q=[F(1,2),F(1,2),F(0)]; r=[F(1,4),F(2,3),F(1,12)]
negative=ce(p,r).plus(ce(p,q),-1); positive=ce(p,r).plus(ce(p,p),-1)
ok(negative.sign()<0);ok(positive.sign()>0)
ok(negative.c==Log().add(F(1,4),F(27,32)).c)
def spectrum(table,n):
 N=1<<n
 return [F(sum(v*(-1 if (s&x).bit_count()%2 else 1) for x,v in enumerate(table)),N)**2 for s in range(N)]
def influence(P):return sum((i.bit_count()*x for i,x in enumerate(P)),F(0))
def child(t,n,i,b):
 return [t[(x&((1<<i)-1))|((x>>i)<<(i+1))|(b<<i)] for x in range(1<<(n-1))]
# Independent direct Walsh reconstruction of the A049 circuit.
f=[]
for w in range(16):
 a,x,y,z=[(w>>i)&1 for i in range(4)]
 m=(-1)**(x if z==0 else y); parity=(-1)**(x+y+z)
 f.append(m if a==0 else parity)
P=spectrum(f,4); P0=spectrum(child(f,4,0,0),3);P1=spectrum(child(f,4,0,1),3)
ok(sorted(x for x in P if x)==[F(1,16)]*8+[F(1,4)]*2)
ok(ce(P,P).c==Log().add(F(3),F(2)).c)
ok(influence(P)==F(11,4));ok(influence(P0)==F(3,2));ok(influence(P1)==3)
ok(P[-1]==F(1,4));ok(P0[-1]==0);ok(P1[-1]==1)
ok(P[0]==P0[0]==P1[0]==0)
A049=[]
for alpha in [F(1,7),F(1,2),F(3,4)]:
 Q=spike(P,15,alpha); erased=[Q[2*j]+Q[2*j+1] for j in range(8)]
 pe=[P[2*j]+P[2*j+1] for j in range(8)]
 un=[]
 for pc in [P0,P1]:un.append([q*(pp/(2*e) if e else F(1,2)) for q,pp,e in zip(erased,pc,pe)])
 masses=[sum(x) for x in un];qc=[[x/mass for x in arr] for arr,mass in zip(un,masses)]
 ok(masses==[(1-alpha)/2,(1+alpha)/2]);ok(qc==[P0,P1])
 K=kl(P,Q); O=kl([F(1,2)]*2,masses); Er=K.plus(kl(pe,erased),-1)
 ok(kl(pe,erased).c==O.c);ok(Er.plus(O).c==K.c);ok(Er.c==K.plus(O,-1).c);ok(Er.sign()>=0)
 Kformula=Log().add(-F(3,4),1-alpha).add(-F(1,4),1+3*alpha)
 ok(K.c==Kformula.c)
 for gamma in [F(1,7),F(1,2),F(3,4)]:
  fresh=[spike(P0,7,gamma),spike(P1,7,gamma)]
  invoice=scaled(kl(P0,fresh[0]).plus(kl(P1,fresh[1])),F(1,2))
  ok(invoice.c==Log().add(-F(1,2),1-gamma).c);ok(invoice.sign()>0)
  ok(K.plus(invoice).plus(K,-1).sign()>0)
  bare=invoice.plus(K,-1).sign()
  rational=(1-alpha)**3*(1+3*alpha)-(1-gamma)**2
  ok(bare==((rational>0)-(rational<0)))
  A049.append({'alpha':str(alpha),'gamma':str(gamma),'root_K':K.dump(),'outcome_K':O.dump(),'floor_invoice':invoice.dump(),'total_excess_sign':1})
# Complete finite census for the scoped dimension minimum; all labelled signs.
tables=nodes=0
for n in range(4):
 for mask in range(1<<(1<<n)):
  t=[-1 if mask>>j&1 else 1 for j in range(1<<n)];S=spectrum(t,n);tables+=1
  if n<=2:ok(sum(x>0 for x in S)==1 or all(x==F(1,4) for x in S))
  for i in range(n):
   for outcome in [0,1]:
    C=spectrum(child(t,n,i,outcome),n-1);nodes+=1
    if S[-1] and sum(x>0 for x in C)>1:ok(C[-1]>0)
result={'status':'PASS','helper':'check.py v1','pilot':pilot,'law_cases':casecount,'exact_assertions':COUNT,'tables':tables,'singleton_outcomes':nodes,'free_cap_checks':free,'positive_matched_checks':paid,'witness_spectrum':[str(x) for x in P],'witness_truth_table':f,'A049':A049,'vacuum_credit_guard':negative.dump(),'matched_guard':positive.dump(),'seconds':time.perf_counter()-START,'arithmetic':'Fraction, exact prime-log vectors, exact integer-power signs'}
(RUN/'out'/('PILOT.json' if pilot else 'CHECK.json')).write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k not in ['A049','witness_spectrum','witness_truth_table']}))
