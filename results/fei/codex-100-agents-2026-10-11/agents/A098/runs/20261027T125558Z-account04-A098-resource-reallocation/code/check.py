from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
from math import lcm
import json,time,sys

RUN=Path(__file__).resolve().parents[1]; START=time.perf_counter()
PILOT='--pilot' in sys.argv; CAP=55 if PILOT else 180
N=0; EDGES=0; UPDATES=0
def check(x):
 global N
 N+=1
 assert x
 if N%256==0:assert time.perf_counter()-START<CAP,'runtime cap'
def plus(*vv):
 d={}
 for v in vv:
  for p,a in v.items():d[p]=d.get(p,F(0))+a
 return {p:a for p,a in d.items() if a}
def times(v,c):return {p:a*c for p,a in v.items() if a*c}
@lru_cache(None)
def logs(q):
 q=F(q);assert q>0;d={}
 for n,sign in [(q.numerator,1),(q.denominator,-1)]:
  p=2
  while p*p<=n:
   while n%p==0:d[p]=d.get(p,0)+sign;n//=p
   p+=1
  if n>1:d[n]=d.get(n,0)+sign
 return {p:F(a) for p,a in d.items() if a}
def ce(p,q):return plus(*(times(logs(y),-x) for x,y in zip(p,q) if x))
def entropy(p):return ce(p,p)
def kl(p,q):return plus(ce(p,q),times(entropy(p),-1))
def sign(v):
 den=lcm(*(a.denominator for a in v.values())) if v else 1
 a=b=1
 for p,x in v.items():
  e=int(x*den)
  if e>=0:a*=p**e
  else:b*=p**(-e)
 return (a>b)-(a<b)
@lru_cache(None)
def lnrat(q):
 q=F(q);e=0
 while q>=2:q/=2;e+=1
 while q<1:q*=2;e-=1
 def series(x):
  z=(x-1)/(x+1);v=F(0);power=z
  for j in range(24):v+=2*power/(2*j+1);power*=z*z
  tail=2*power/(49*(1-z*z))
  return v,v+tail
 lo,hi=series(q);a,b=series(F(2))
 return (lo+e*a,hi+e*b) if e>=0 else (lo+e*b,hi+e*a)
def natural_bounds(v):
 lo=hi=F(0)
 for p,a in v.items():
  l,h=lnrat(p)
  lo+=a*(l if a>=0 else h);hi+=a*(h if a>=0 else l)
 return lo,hi

@lru_cache(None)
def spectrum(tab):
 d=len(tab)
 return tuple(F(sum(y*(-1 if (x&s).bit_count()%2 else 1) for x,y in enumerate(tab)),d)**2 for s in range(d))
def erase(s,i):return (s&((1<<i)-1))|((s>>(i+1))<<i)
def marginal(p,i):
 q=[F(0)]*(len(p)//2)
 for s,a in enumerate(p):q[erase(s,i)]+=a
 return tuple(q)
def children(tab,i):return [tuple(y for x,y in enumerate(tab) if (x>>i)&1==t) for t in [0,1]]
def influence(p):return sum(s.bit_count()*a for s,a in enumerate(p))
def ref(p,k):
 u=F(1,len(p))
 if k==0:return p
 if k==1:return (u,)*len(p)
 return tuple((a+u)/2 for a in p)

def query(tab,q,i):
 global EDGES
 EDGES+=1;p=spectrum(tab);r=marginal(p,i);v=marginal(q,i)
 ts=children(tab,i);ps=[spectrum(t) for t in ts]
 check(all((ps[0][s]+ps[1][s])/2==r[s] for s in range(len(r))))
 L=plus(kl(p,q),times(kl(r,v),-1))
 # Independent conditional-fiber reconstruction, retaining zero-source ghosts.
 cond={}
 for u,a in enumerate(r):
  if not a:continue
  inds=[s for s in range(len(p)) if erase(s,i)==u]
  cond=plus(cond,times(kl(tuple(p[s]/a for s in inds),tuple(q[s]/v[u] for s in inds)),a))
 check(L==cond)
 J=times(plus(*(kl(x,r) for x in ps)),F(1,2))
 avgD=times(plus(*(kl(x,v) for x in ps)),F(1,2))
 check(plus(avgD,times(kl(p,q),-1))==plus(J,times(L,-1)))
 B=plus(entropy(p),times(entropy(r),-1))
 avgCE=times(plus(*(ce(x,v) for x in ps)),F(1,2))
 check(plus(avgCE,times(ce(p,q),-1))==times(plus(B,L),-1))
 d=sum(a for s,a in enumerate(p) if s>>i&1)
 check(influence(p)==d+sum(influence(x) for x in ps)/2)
 check(natural_bounds(J)[1]<=2*d)
 return ts,v,L,J,d

def update(p,q,t=F(1,2)):
 global UPDATES
 UPDATES+=1
 # Partition into vacuum and occupied frequencies. Zero true cells retained.
 groups=[(0,),tuple(range(1,len(p)))] if len(p)>1 else [(0,)]
 new=list(q);pm=[];qm=[];rm=[]
 for ids in groups:
  a=sum(p[s] for s in ids);b=sum(q[s] for s in ids);r=(1-t)*b+t*a
  pm.append(a);qm.append(b);rm.append(r)
  if b:
   for s in ids:new[s]=q[s]*r/b
  else:check(a==0 and r==0)
 check(sum(new)==1)
 fee=kl(new,q)
 slack=plus(kl(p,q),times(kl(p,new),-1),times(fee,-1))
 if t in (0,1):check(not slack)
 else:
  symmetric=times(plus(kl(rm,qm),kl(qm,rm)),(1-t)/t)
  check(slack==symmetric)
 return tuple(new),fee,slack

def tree(tab,q,mass,depth=0):
 p=spectrum(tab);n=(len(tab)-1).bit_length()
 # Stop a real branch early, retaining its nonconstant terminal divergence.
 if not n or (depth>0 and n==1 and tab[0]<0):
  check(ce(p,tuple(mass*a for a in q))==plus(entropy(p),kl(p,q),logs(1/mass)))
  return {},{}, {},kl(p,q),F(0),influence(p),{}
 q,fee,slack=update(p,q,F(1,2) if depth%2==0 else F(1))
 i=n-1 if tab[0]>0 else 0
 ts,v,L,J,d=query(tab,q,i)
 cc=[tree(t,v,mass,depth+1) for t in ts]
 avg=lambda k:times(plus(*(c[k] for c in cc)),F(1,2))
 losses=plus(L,avg(0));fees=plus(fee,avg(1));js=plus(J,avg(2));terminal=avg(3)
 spent=d+sum(c[4] for c in cc)/2
 terminalI=sum(c[5] for c in cc)/2
 slacks=plus(slack,avg(6))
 return losses,fees,js,terminal,spent,terminalI,slacks

def affine_tests():
 cases=0
 for n in [2,3]:
  for mask in [1,(1<<(1<<n))-2]:
   tab=tuple(-1 if mask>>x&1 else 1 for x in range(1<<n));p=spectrum(tab)
   for base in [2,3]:
    z=sum(a*F(base)**(-s.bit_count()) for s,a in enumerate(p))
    q=tuple(a*F(base)**(-s.bit_count())/z for s,a in enumerate(p))
    # Log(p/q)=log(z)+|s|log(base) is affine in a NONPARTITION moment.
    check(ce(p,q)==plus(entropy(p),logs(z),times(logs(base),influence(p))))
    # Thus u=p is exactly the information projection on E|S|=I(p).
    check(not plus(kl(p,q),times(kl(p,p),-1),times(kl(p,q),-1)))
    cases+=1
 # Boundary projection forced by zero expected nonnegative cardinality.
 for n in [1,2,3]:
  p=(F(1),)+(F(0),)*((1<<n)-1);q=(F(1,1<<n),)*(1<<n)
  check(kl(p,q)==times(logs(2),n));cases+=1
 return cases

def moments_and_scope():
 roots=0;moments=0;query_count=0
 for n in ([4] if PILOT else [4,6,8]):
  # Literal truth table, not a stipulated arbitrary spectrum.
  tab=tuple(-1 if sum(1 for j in range(0,n,2) if (x>>j)&3==3)%2 else 1 for x in range(1<<n))
  p=spectrum(tab);u=F(1,1<<n);check(p==(u,)*(1<<n));check(influence(p)==F(n,2))
  eps=F(1,1<<(4*n));q=tuple(u*(eps if (s&((1<<(n-1))-1)).bit_count()%2 else 2-eps) if s>>(n-1) else u for s in range(1<<n))
  check(sum(q)==1 and min(q)>0);check(q[0]==p[0])
  for mask in range(1<<n):
   if mask.bit_count()<=n-2:
    check(sum(q[s] for s in range(1<<n) if s&mask==mask)==sum(p[s] for s in range(1<<n) if s&mask==mask));moments+=1
  D=plus(times(logs(2),n),times(logs(2-eps),F(-1,4)))
  check(kl(p,q)==D)
  check(sign(plus(D,times(logs(2),F(1,4)-n)))>0)
  check(sign(plus(times(logs(2),n),times(D,-1)))>0)
  check(plus(ce(p,q),times(entropy(p),-1))==D)
  for i in range(n-1):
   check(marginal(p,i)==marginal(q,i))
   check(plus(kl(p,q),times(kl(marginal(p,i),marginal(q,i)),-1))==D);query_count+=1
  roots+=1
 # Actual AND2: distinguish the two reference interfaces at a constant child.
 tab=(-1,-1,-1,1);p=spectrum(tab);v=marginal(p,0)
 const=next(spectrum(t) for t in children(tab,0) if max(spectrum(t))==1 and spectrum(t)[0]==1)
 check(v==(F(1,2),F(1,2)));check(const==(F(1),F(0)))
 check(v[1]>0 and const[1]==0) # D(projected||true-kernel)=infinity.
 return {'roots':roots,'inclusion_moments':moments,'erased_reference_queries':query_count,'and2_reverse_KL':'INFINITE'}

roots=queries=trees=0
for n in range((2 if PILOT else 3)+1):
 for mask in range(1<<(1<<n)):
  tab=tuple(1 if mask>>x&1 else -1 for x in range(1<<n));p=spectrum(tab);roots+=1
  check(sum(p)==1)
  for i in range(n):
   for k in range(3):query(tab,ref(p,k),i);queries+=1
  for mass in [F(1),F(1,2)]:
   q=ref(p,2);result=tree(tab,q,mass);trees+=1
   L,fees,J,terminal,spent,terminalI,slacks=result
   check(plus(terminal,L,fees,slacks)==plus(kl(p,q),J))
   check(spent+terminalI==influence(p))
   check(natural_bounds(J)[1]<=2*spent)
   # The raw signed-entropy/full-terminal bill is root CE + JS - update slack.
   initialCE=ce(p,tuple(mass*a for a in q));old=F(1,4)
   bill=plus(entropy(p),terminal,L,fees,logs(1/mass),times(logs(2),old))
   exact=plus(initialCE,J,times(slacks,-1),times(logs(2),old))
   check(bill==exact)
affine=affine_tests();moments=moments_and_scope()
result={'status':'PASS','helper_version':'A098-stage22-v1','pilot':PILOT,'roots':roots,'direct_queries':queries,'adaptive_trees':trees,'visited_query_nodes':EDGES,'executed_profile_updates':UPDATES,'affine_fixtures':affine,'high_moment':moments,'exact_assertions':N,'seconds':time.perf_counter()-START,'arithmetic':'Fraction; prime-exponent identities; integer-power signs; certified natural-log intervals'}
(RUN/'out'/('PILOT.json' if PILOT else 'VALIDATION.json')).write_bytes((json.dumps(result,indent=2)+'\n').encode('utf-8'))
print(json.dumps(result))
