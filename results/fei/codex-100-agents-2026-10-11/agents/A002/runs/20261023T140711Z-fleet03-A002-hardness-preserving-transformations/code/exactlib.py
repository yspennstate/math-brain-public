import sys,json,time,itertools,math
from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
R=Path(__file__).resolve().parents[1]
start=time.monotonic(); checks=0; counts={}
def ok(v):
 global checks
 assert v
 checks+=1
 if time.monotonic()-start>(55 if '--pilot' in sys.argv else 180): raise RuntimeError('frozen compute cap')
def fw(a):
 a=list(a); h=1
 while h<len(a):
  for j in range(0,len(a),2*h):
   for i in range(j,j+h): a[i],a[i+h]=a[i]+a[i+h],a[i]-a[i+h]
  h*=2
 return a
@lru_cache(None)
def factors(a):
 out={}; b=2
 while b*b<=a:
  while a%b==0: out[b]=out.get(b,0)+1; a//=b
  b+=1
 if a>1: out[a]=out.get(a,0)+1
 return out

def add(*terms):
 out={}
 for c,v in terms:
  for p,w in v.items(): out[p]=out.get(p,Q(0))+c*w
 return {p:w for p,w in out.items() if w}
def logq(x):
 if not x: return {}
 z=x*x
 return add(*[(Q(-a)*z,{p:Q(1)}) for p,a in factors(z.numerator).items()],*[(Q(a)*z,{p:Q(1)}) for p,a in factors(z.denominator).items()])
@lru_cache(None)
def lnint(n):
 b=n.bit_length()-1; x=Q(n,2**b); z=(x-1)/(x+1); v=Q(0)
 for j in range(32): v+=2*z**(2*j+1)/(2*j+1)
 err=2*z**65/(65*(1-z*z))
 # ln(2) obtained separately with same positive series
 z2=Q(1,3); l2=sum((2*z2**(2*j+1)/(2*j+1) for j in range(32)),Q(0)); e2=2*z2**65/(65*(1-z2*z2))
 return v+b*l2,v+err+b*(l2+e2),l2,l2+e2
@lru_cache(None)
def log2int(n):
 if n==2: return Q(1),Q(1)
 lo,hi,l2,h2=lnint(n); return lo/h2,hi/l2
def interval(v):
 low=high=Q(0)
 for p,c in v.items():
  a,b=log2int(p); low+=c*(a if c>=0 else b); high+=c*(b if c>=0 else a)
 return low,high
def bounded(v,b):
 lo,hi=interval(v); ok(lo>=-b and hi<=b)
def rankadd(b,v):
 while v:
  j=v.bit_length()-1
  if j in b: v^=b[j]
  else: b[j]=v; return True
 return False
@lru_cache(None)
def stats(f):
 N=len(f); n=N.bit_length()-1; W=fw(f); mass=[Q(v*v,N*N) for v in W]
 H=add(*[(Q(1),logq(Q(v,N))) for v in W if v]); I=sum((s.bit_count()*x for s,x in enumerate(mass)),Q(0))
 B=fw([v*v for v in W]); cost=[Q(N*N-v,2*N*N) for v in B]
 minima=[]
 for centered in (False,True):
  weights=[min(x,1-x) if centered else x for x in cost]; basis={}; total=Q(0)
  for v in sorted(range(1,N),key=lambda v:weights[v]):
   if rankadd(basis,v): total+=weights[v]
  minima.append(total)
 b={}; support=[s for s,v in enumerate(W) if v]
 for s in support: rankadd(b,s^support[0])
 return {'n':n,'W':W,'mass':mass,'H':H,'I':I,'ell':minima[0],'a':minima[1],'cost':cost,'span':len(b),'mu':Q(W[0],N)}
def table(n,v): return tuple(1 if (v>>x)&1 else -1 for x in range(1<<n))
def tensor(g,t):
 d=len(g).bit_length()-1; mask=(1<<d)-1
 return tuple(math.prod(g[(x>>(d*j))&mask] for j in range(t)) for x in range(1<<(d*t)))
def activate(h,k): return tuple(h[x>>k] if x% (1<<k)==0 else 1 for x in range(len(h)*(1<<k)))
def restrict(f,A,b):
 n=len(f).bit_length()-1; free=[j for j in range(n) if j not in A]
 return tuple(f[sum(((x>>a)&1)<<j for a,j in enumerate(free))+sum(((b>>a)&1)<<j for a,j in enumerate(A))] for x in range(1<<len(free)))
def profile(mu,k):
 p=Q(1,2**k); nu=mu; delta=1-nu
 return add((1,logq(1-p*delta)),(-p,logq(nu)),(p*(1-p),logq(delta)),(2*k*p*((1-nu*nu)+(1-p)*delta*delta),{2:Q(1)}))
