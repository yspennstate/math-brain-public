import json, time, sys
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
R=Path(__file__).resolve().parents[1]
(R/'out').mkdir(exist_ok=True)
START=time.monotonic(); checks=0
def ck(b, name):
 global checks
 checks+=1
 assert b, name
 if time.monotonic()-START>55: raise RuntimeError('55 second frozen watchdog')
# Exact linear forms in logarithms of primes; zero forms are recognized exactly.
def add(a,b):
 c=dict(a)
 for p,x in b.items(): c[p]=c.get(p,F(0))+x
 return {p:x for p,x in c.items() if x}
def mul(a,x): return {p:v*x for p,v in a.items() if v*x}
def sub(a,b): return add(a,mul(b,-1))
def rat(x): return {2:F(x)} if x else {}
@lru_cache(None)
def factors(n):
 out={}; p=2
 while p*p<=n:
  while n%p==0: out[p]=out.get(p,0)+1; n//=p
  p+=1
 if n>1: out[n]=out.get(n,0)+1
 return out
def logq(q): return sub(factors(q.numerator), factors(q.denominator))
def entropy(ps):
 out={}
 for q in ps:
  if q: out=add(out,mul(logq(q),-q))
 return out
def ln_interval(q):
 t=(q-1)/(q+1)
 lo=2*sum((t**(2*j+1)/F(2*j+1) for j in range(24)),F(0))
 return lo,lo+2*t**49/(49*(1-t*t))
L2=ln_interval(F(2))
@lru_cache(None)
def log_interval(p):
 if p==2:return F(1),F(1)
 e=p.bit_length()-1; a,b=ln_interval(F(p,1<<e))
 return e+a/L2[1],e+b/L2[0]
def bounds(a):
 lo=hi=F(0)
 for p,c in a.items():
  x,y=log_interval(p)
  lo+=c*(x if c>0 else y); hi+=c*(y if c>0 else x)
 return lo,hi
def sign(a):
 if not a:return 0
 lo,hi=bounds(a)
 ck(lo>0 or hi<0,'exact logarithm comparison resolved')
 return 1 if lo>0 else -1
def maximum(a,b):return a if sign(sub(a,b))>=0 else b
def minimum(a,b):return a if sign(sub(a,b))<=0 else b
def child(t,i,s):return tuple(t[j] for j in range(len(t)) if (j>>i)&1==s)
@lru_cache(None)
def spec(t):
 w=list(t); k=1
 while k<len(w):
  for j in range(0,len(w),2*k):
   for a in range(j,j+k):x,y=w[a],w[a+k];w[a]=x+y;w[a+k]=x-y
  k*=2
 return tuple(F(x,len(t)) for x in w)
@lru_cache(None)
def data(t):
 a=spec(t); ps=[x*x for x in a]; n=len(t).bit_length()-1
 ds=[sum((p for j,p in enumerate(ps) if j>>i&1),F(0)) for i in range(n)]
 ck(sum(ps)==1,'Boolean Parseval')
 for i,d in enumerate(ds):ck(d==F(sum(t[j]!=t[j^(1<<i)] for j in range(len(t))),len(t)),'edge versus spectral influence')
 return entropy(ps),sum(ds),ds
@lru_cache(None)
def solve(t):
 H,I,ds=data(t)
 if len(t)==1:return {},{}
 best={}; capped=None
 for i,d in enumerate(ds):
  a,b=child(t,i,0),child(t,i,1)
  Ha,Ia,_=data(a);Hb,Ib,_=data(b)
  ck(I==d+(Ia+Ib)/2,'physical influence conservation')
  drop=sub(H,mul(add(Ha,Hb),F(1,2)))
  ck(sign(drop)>=0,'entropy drop nonnegative')
  # Independent identity from the average and difference slice amplitudes.
  aa,bb=spec(a),spec(b)
  u=[(x+y)/2 for x,y in zip(aa,bb)];v=[(x-y)/2 for x,y in zip(aa,bb)]
  q=[x*x+y*y for x,y in zip(u,v)]
  erasure={}
  for x,y,z in zip(u,v,q):
   if z:erasure=add(erasure,mul(entropy([x*x/z,y*y/z]),z))
  js=sub(entropy(q),mul(add(Ha,Hb),F(1,2)))
  ck(sub(drop,add(erasure,js))=={},'exact erasure plus JS identity')
  ck(sign(erasure)>=0 and sign(js)>=0,'both charges nonnegative')
  va,wa=solve(a);vb,wb=solve(b)
  delta=sub(drop,rat(4*d))
  opt=add(maximum(delta,{}),mul(add(va,vb),F(1,2)))
  cop=add(minimum(drop,rat(4*d)),mul(add(wa,wb),F(1,2)))
  best=maximum(best,opt)
  capped=cop if capped is None else minimum(capped,cop)
 ck(add(best,capped)==H,'V plus minimum capped entropy equals H')
 ck(sign(sub(H,best))>=0,'V at most H')
 ck(sign(sub(best,maximum(sub(H,rat(4*I)),{})))>=0,'V at least positive H minus 4I')
 return best,capped
pilot='--pilot' in sys.argv; top=2 if pilot else 3; tables=0; positive=0
for n in range(top+1):
 for mask in range(1<<(1<<n)):
  t=tuple(1 if mask>>j&1 else -1 for j in range(1<<n));tables+=1
  # Second transform implementation: character dot products.
  direct=tuple(F(sum(t[j]*(-1 if (j&s).bit_count()%2 else 1) for j in range(len(t))),len(t)) for s in range(len(t)))
  ck(direct==spec(t),'direct characters versus butterfly WHT')
  V,W=solve(t)
  if sign(V)>0:positive+=1
out={'status':'PASS','tables':tables,'positive_V_tables':positive,'assertions':checks,'runtime_seconds':time.monotonic()-START,'arithmetic':'integer WHT; Fraction prime-log expressions; rational outward log intervals; exact Bellman max/min','scope':'all Boolean truth tables n<=%d; no symmetry reduction'%top}
(R/'out'/('PILOT.json' if pilot else 'CHECK.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
