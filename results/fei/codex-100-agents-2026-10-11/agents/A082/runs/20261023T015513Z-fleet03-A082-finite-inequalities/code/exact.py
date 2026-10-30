from fractions import Fraction as F
from functools import lru_cache
ASSERTIONS=0
def ck(v):
 global ASSERTIONS
 ASSERTIONS+=1
 assert v,ASSERTIONS
def add(a,b):
 d=dict(a)
 for k,v in b.items():
  d[k]=d.get(k,F(0))+v
  if not d[k]:del d[k]
 return d
def scale(a,w):return {k:v*w for k,v in a.items() if v*w}
def sub(a,b):return add(a,scale(b,-1))
@lru_cache(maxsize=50000)
def factors(n):
 d={};p=2
 while p*p<=n:
  while n%p==0:d[p]=d.get(p,0)+1;n//=p
  p=3 if p==2 else p+2
 if n>1:d[n]=d.get(n,0)+1
 return d
@lru_cache(maxsize=50000)
def logform(x):
 ck(x>0)
 return sub(factors(x.numerator),factors(x.denominator))
def ce(p,q):
 d={}
 for x,y in zip(p,q):
  if x:ck(y>0);d=add(d,scale(logform(y),-x))
 return d
def ent(p):return ce(p,p)
def lnunit(x):
 z=(x-1)/(x+1);v=sum((2*z**(2*k+1)/F(2*k+1) for k in range(24)),F(0))
 return v,v+2*z**49/(49*(1-z*z))
LN2=lnunit(F(2))
@lru_cache(maxsize=10000)
def lgprime(p):
 x=F(p);k=0
 while x>=2:x/=2;k+=1
 lo,hi=lnunit(x)
 lo=k+lo/LN2[1];hi=k+hi/LN2[0];den=1<<100
 # Outward rounding preserves the rigorous enclosure and bounds integer size.
 return F((lo.numerator*den)//lo.denominator,den),F(-((-hi.numerator*den)//hi.denominator),den)
def interval(a):
 lo=hi=F(0)
 for p,c in a.items():
  l,u=lgprime(p)
  if c>=0:lo+=c*l;hi+=c*u
  else:lo+=c*u;hi+=c*l
 return lo,hi
def nonpositive(a):
 if not a:return True
 return interval(a)[1]<=0
def ins(x,j):return (x&((1<<j)-1))|((x>>j)<<(j+1))
def marginal(q,j):return tuple(q[ins(x,j)]+q[ins(x,j)|(1<<j)] for x in range(len(q)//2))
def child(f,j,v):return tuple(f[ins(x,j)|(v<<j)] for x in range(len(f)//2))
@lru_cache(maxsize=10000)
def spectrum(f):
 n=len(f)
 out=tuple(F(sum(v*(-1 if (x&t).bit_count()%2 else 1) for x,v in enumerate(f))**2,n*n) for t in range(n))
 ck(sum(out)==1);return out
def erasure(f,j):
 p=spectrum(f);return sub(ent(p),ent(marginal(p,j)))
def calibrate(q,m):
 if m==1:return (F(1),)+(F(0),)*(len(q)-1)
 ck(q[0]<1)
 return (m,)+tuple(v*(1-m)/(1-q[0]) for v in q[1:])
def references(p):
 m=p[0];n=len(p)
 if m==1:return [p,p,p]
 u=(m,)+((1-m)/F(n-1),)*(n-1)
 v=[z/16 for z in u];v[0]=m;v[1]+=(1-m)*F(15,16)
 return [p,u,tuple(v)]
def influence(f):
 return sum(F(sum(v!=f[x^(1<<j)] for x,v in enumerate(f)),len(f)) for j in range((len(f)-1).bit_length()))
def serial_form(d):return {str(k):str(v) for k,v in d.items()}
