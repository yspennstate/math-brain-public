from fractions import Fraction as F
from pathlib import Path
import json,sys,time,math
R=Path(__file__).resolve().parents[1]
class E:
 def __init__(self,d=None): self.d={k:F(v) for k,v in (d or {}).items() if v}
 def __add__(self,b):
  if not isinstance(b,E): b=E({2:b})
  d=self.d.copy()
  for k,v in b.d.items(): d[k]=d.get(k,F(0))+v
  return E(d)
 __radd__=__add__
 def __neg__(self): return self*-1
 def __sub__(self,b): return self+-b
 def __mul__(self,b): return E({k:v*b for k,v in self.d.items()})
 __rmul__=__mul__
 def __truediv__(self,b): return self*F(1,b)
 def __eq__(self,b): return (self-b).d=={}
 def out(self): return {str(k):str(v) for k,v in self.d.items()}
def log(q):
 q=F(q); assert q>0; d={}
 for v,sg in [(q.numerator,1),(q.denominator,-1)]:
  p=2
  while p*p<=v:
   while v%p==0: d[p]=d.get(p,0)+sg; v//=p
   p+=1
  if v>1:d[v]=d.get(v,0)+sg
 return E(d)
U=E({'e':1})
def ent(a): return sum((-q*q*log(q*q) for q in a if q),E())
def kval(q): return (-q*q*log(q*q) if q else E())+3*q*q*U
def kp(q): return (-2*q*log(q*q) if q else E())+4*q*U
def fw(v):
 v=list(v); w=1
 while w<len(v):
  for j in range(0,len(v),2*w):
   for i in range(j,j+w): x,y=v[i],v[i+w];v[i]=x+y;v[i+w]=x-y
  w*=2
 return v
cache={}
def ln(q):
 q=F(q)
 if q in cache:return cache[q]
 orig=q;e=0
 while q>=2:q/=2;e+=1
 while q<1:q*=2;e-=1
 z=(q-1)/(q+1);s=sum((2*z**(2*j+1)/F(2*j+1) for j in range(40)),F(0));tail=2*z**81/(81*(1-z*z)); lo,hi=s,s+tail
 if e:
  a,b=ln(F(2)) if orig!=2 else (None,None)
  if orig==2:
   z=F(1,3);s=sum((2*z**(2*j+1)/F(2*j+1) for j in range(40)),F(0));lo=s;hi=s+2*z**81/(81*(1-z*z))
  elif e>0:lo+=e*a;hi+=e*b
  else:lo+=e*b;hi+=e*a
 cache[orig]=(lo,hi);return lo,hi
def bounds(x):
 l2,h2=ln(F(2));lo=hi=F(0)
 for k,v in x.d.items():
  if k=='e':a,b=1/h2,1/l2
  else:
   a,b=ln(F(k));a,b=a/h2,b/l2
  if v>=0:lo+=v*a;hi+=v*b
  else:lo+=v*b;hi+=v*a
 return lo,hi
checks=0
def ck(p):
 global checks
 assert p;checks+=1
def nonneg(x):
 if not x.d:ck(True)
 else:ck(bounds(x)[0]>=0)
def audit(v,deep=True):
 N=len(v);n=N.bit_length()-1;a=[F(w,N) for w in fw(v)];h=ent(a);inf=sum((s.bit_count()*q*q for s,q in enumerate(a)),F(0));mu=a[0];u=abs(mu)
 ck(sum(q*q for q in a)==1)
 ck(inf==F(sum(v[x]!=v[x^(1<<i)] for x in range(N) for i in range(n)),N))
 if deep:ck(a==[F(sum(v[x]*(-1 if (s&x).bit_count()%2 else 1) for x in range(N)),N) for s in range(N)])
 rr={}
 for c in [-1,1]:
  target=[F(c)]+[F(0)]*(N-1)
  rem=sum((kval(b)-kval(q)-kp(q)*(b-q) for q,b in zip(a,target)),E());rr[c]=rem
  expected=h+4*U+c*((2*mu*log(mu*mu) if mu else E())-4*mu*U)
  ck(rem==expected)
  if deep:
   edit=[x for x in range(N) if v[x]!=c]
   pot=E()
   for x in edit:
    gx=sum((log(q*q)*q*(-1 if (s&x).bit_count()%2 else 1) for s,q in enumerate(a) if q),E())
    pot+=v[x]*gx
   edges=sum(v[x]*v[x^(1<<i)] for x in edit for i in range(n) if (x^(1<<i)) not in edit)
   for K in [0,3,6]:
    W=pot-2*len(edit)*U-E({2:F(K,2)*edges})
    ck(-h+E({2:K*inf})==W*F(4,N)+rem)
 ck(rr[-1]+rr[1]==2*h+8*U)
 small=rr[1 if mu>=0 else -1]
 correction=4*(1-u)*U+(2*u*log(u*u) if u else E())
 ck(small==h+correction);nonneg(correction);nonneg(4*(1-u)**2*U-correction)
 ck(1-u<=1-u*u<=inf);nonneg(4*inf*inf*U-correction)
 if inf==0:ck(small==E())
 return h,inf,mu,small
start=time.perf_counter();pilot='--pilot' in sys.argv;roots=0
for n in range(3 if pilot else 4):
 for mask in range(1<<(1<<n)):
  audit([1 if (mask>>x)&1 else -1 for x in range(1<<n)]);roots+=1
fixtures=[]
if not pilot:
 seeds=[[1 if (m>>x)&1 else -1 for x in range(4)] for m in range(1,15)]
 seeds += [[-1 if x==0 else 1 for x in range(8)], [1 if x.bit_count()>=2 else -1 for x in range(8)], [(-1)**x.bit_count() for x in range(8)]]
 for sid,seed in enumerate(seeds):
  sh,si,_,_=audit(seed,False);n=len(seed).bit_length()-1
  for t in [1,2]:
   for k in [1,2]:
    d=t*n+1;p=F(1,1<<k);g=[]
    for x in range(1<<d):
     val=-1 if (x>>(t*n))&1 else 1
     for b in range(t):val*=seed[(x>>(b*n))&((1<<n)-1)]
     g.append(val)
    vals=[g[x&((1<<d)-1)] if (x>>d)==0 else 1 for x in range(1<<(d+k))]
    hh,ii,mm,sm=audit(vals,False)
    ck(mm==1-p);ck(ii==p*(1+t*si+k))
    ck(hh==p*t*sh+E({2:(4*p-2*p*p)*k})-(1-p)**2*log((1-p)**2))
    fixtures.append({'seed':sid,'t':t,'k':k,'I':str(ii),'mu':str(mm),'H':hh.out(),'smaller_refund':sm.out()})
result={'status':'PASS','pilot':pilot,'root_tables':roots,'activation_fixtures':len(fixtures),'exact_assertions':checks,'elapsed_seconds':time.perf_counter()-start,'arithmetic':'Fraction; prime-log identities plus symbolic reciprocal ln2; outward40-term atanh bounds','fixtures':fixtures}
(R/'out'/('PILOT.json' if pilot else 'CHECK.json')).write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='fixtures'}))
