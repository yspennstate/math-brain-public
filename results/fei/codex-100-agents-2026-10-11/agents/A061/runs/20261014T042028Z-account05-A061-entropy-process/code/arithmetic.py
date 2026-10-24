from fractions import Fraction as F
from collections import defaultdict, Counter
from functools import lru_cache
from pathlib import Path
import sys,json,time

ROOT=Path(__file__).resolve().parents[1]
MODE=sys.argv[1]; START=time.perf_counter(); ASSERTS=0
CAP=60 if MODE=='pilot' else 600
def check(v,context=''):
 global ASSERTS
 assert v,context
 ASSERTS+=1
 assert time.perf_counter()-START<CAP,'frozen deadline'
def equal(a,b,context=''):check(a==b,(context,a,b))
@lru_cache(None)
def factors(n):
 out={};p=2
 while p*p<=n:
  while n%p==0:out[p]=out.get(p,0)+1;n//=p
  p+=1
 if n>1:out[n]=out.get(n,0)+1
 return out
def combine(*terms):
 d=defaultdict(F)
 for c,e in terms:
  for p,v in e.items():d[p]+=c*v
 return {p:v for p,v in d.items() if v}
@lru_cache(None)
def logexpr(q):
 return combine((1,factors(q.numerator)),(-1,factors(q.denominator)))
@lru_cache(None)
def masslog(q):return combine((q,logexpr(q))) if q else {}
def entropy(ps):
 counts=Counter(ps)
 return combine(*[(-c,masslog(p)) for p,c in counts.items() if p])
@lru_cache(None)
def lnseries(q):
 z=(q-1)/(q+1);z2=z*z;power=z;s=F()
 for k in range(48):s+=2*power/(2*k+1);power*=z2
 return s,s+2*power/(97*(1-z2))
LN2=lnseries(F(2));SCALE=1<<160
@lru_cache(None)
def loginterval(p):
 q=F(p);k=0
 while q>=2:q/=2;k+=1
 a,b=lnseries(q);lo=k+a/LN2[1];hi=k+b/LN2[0]
 return F((lo*SCALE).numerator//(lo*SCALE).denominator,SCALE),F(-((-hi*SCALE).numerator//(-hi*SCALE).denominator),SCALE)
def interval(e):
 lo=hi=F()
 for p,c in e.items():
  a,b=loginterval(p)
  if c>=0:lo+=c*a;hi+=c*b
  else:lo+=c*b;hi+=c*a
 return lo,hi
def constant(x):return {2:F(x)} if x else {}
def shifted(e,x):return combine((1,e),(1,constant(x)))
def fwht(t):
 a=list(t);h=1
 while h<len(a):
  for block in range(0,len(a),2*h):
   for j in range(block,block+h):a[j],a[j+h]=a[j]+a[j+h],a[j]-a[j+h]
  h*=2
 return [F(x,len(t)) for x in a]
def insert(x,i,b):return (x&((1<<i)-1))|((x>>i)<<(i+1))|(b<<i)
def total(a):return sum((a[s]**2*s.bit_count() for s in range(len(a))),F())
def vertex_influence(t,i):
 return F(sum(t[insert(x,i,0)]!=t[insert(x,i,1)] for x in range(len(t)//2)),len(t)//2)
def metrics(t,i,a=None):
 if a is None:a=fwht(t)
 n=len(t).bit_length()-1
 childt=[[t[insert(x,i,b)] for x in range(len(t)//2)] for b in (0,1)]
 ca=[fwht(c) for c in childt]
 for b in (0,1):equal(ca[b],[a[insert(x,i,0)]+(-1)**b*a[insert(x,i,1)] for x in range(len(t)//2)],'actual child Walsh')
 ps=[x*x for x in a];hh=entropy(ps)
 d=sum((ps[s] for s in range(len(a)) if s&(1<<i)),F())
 equal(d,vertex_influence(t,i),'physical influence')
 ii=total(a);childI=[total(c) for c in ca];childH=[entropy([x*x for x in c]) for c in ca]
 equal(ii,d+sum(childI,F())/2,'influence removal')
 rem=[ps[insert(x,i,0)]+ps[insert(x,i,1)] for x in range(len(t)//2)]
 B=combine((1,hh),(-1,entropy(rem)))
 D=combine((1,hh),(-F(1,2),childH[0]),(-F(1,2),childH[1]))
 return {'d':d,'B':B,'D':D,'H':hh,'I':ii,'childH':childH,'childI':childI,'childt':childt,'n':n}
def sigma(m,C):return shifted(combine((-F(1,2),m['childH'][0]),(-F(1,2),m['childH'][1])),C*sum(m['childI'],F())/2)

