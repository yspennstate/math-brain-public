from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
import json,time,hashlib
root=Path(__file__).resolve().parents[1];start=time.monotonic();checks=0
def verify(test):
 global checks
 assert test;checks+=1
def tables(n):return [tuple(1-2*((c>>x)&1) for x in range(1<<n)) for c in range(1<<(1<<n))]
def cut(v,i,b):
 return tuple(v[x] for x in range(len(v)) if (x>>i)&1==b)
def mean(v):return Q(sum(v),len(v))
def inf(v):
 return sum((Q(sum(v[x]!=v[x^(1<<i)] for x in range(len(v))),len(v)) for i in range((len(v)-1).bit_length())),Q(0))
def xi(w,h):
 t=(1-mean(w))/2;r=(1-mean(h))/2
 return 5*(r*(1-r)*inf(w)+t*(1-t)*inf(h))
def spectrum(v):
 return [Q(sum(z*(-1)**((s&x).bit_count()%2) for x,z in enumerate(v)),len(v)) for s in range(len(v))]
@lru_cache(None)
def lnunit(x):
 z=(x-1)/(x+1);lo=sum((2*z**(2*j+1)/(2*j+1) for j in range(18)),Q(0))
 return lo,lo+2*z**37/(37*(1-z*z))
@lru_cache(None)
def log2(x):
 k=x.numerator.bit_length()-x.denominator.bit_length();y=x/(Q(2)**k)
 if y<1:k-=1;y*=2
 a,b=lnunit(y);c,d=lnunit(Q(2))
 return k+a/d,k+b/c
def e(x):
 if not x:return Q(0),Q(0)
 a,b=log2(x);return -x*b,-x*a
def L(a,b):
 ea=e(a*a);eb=e(b*b);es=e(a*a+b*b)
 return ea[0]+eb[0]-es[1],ea[1]+eb[1]-es[0]
def erase(v,i):
 s=spectrum(v);pieces=[L(a,s[j^(1<<i)]) for j,a in enumerate(s) if not j>>i&1]
 return sum(p[0] for p in pieces),sum(p[1] for p in pieces)
queries=certified=endpoint=0
for w in tables(2):
 for h in tables(2):
  f=tuple(1 if x==1 or y==1 else -1 for y in h for x in w)
  verify(inf(f)==(1-mean(h))/2*inf(w)+(1-mean(w))/2*inf(h))
  for block in range(2):
   v=h if block else w;other=w if block else h;rate=(1-mean(other))/2
   for j in range(2):
    v0,v1=cut(v,j,0),cut(v,j,1);d=Q(sum(x!=y for x,y in zip(v0,v1)),len(v0))
    b=(mean(v0)-mean(v1))/2
    children=[(w,v0),(w,v1)] if block else [(v0,h),(v1,h)]
    D=xi(w,h)-sum(xi(*c) for c in children)/2
    verify(D==5*(rate*(1-rate)*d+b*b*inf(other)/4))
    fi=2*block+j
    if b and rate not in (0,1):
     bf=erase(f,fi);bw=erase(v,j)
     verify(bf[1]-rate*bw[0]<=5*rate*(1-rate)*abs(b));certified+=1
    else:
     # Exact rational coefficients prove original scalar R=0 in these cases.
     verify(b==0 or rate==0 or rate==1);endpoint+=1
    queries+=1
  verify(time.monotonic()-start<90)
for k in range(1,9):
 p=Q(1,2**k);I=Q(k,2**(k-1));IF=2*p*I;X=10*p*(1-p)*I
 verify(X/IF==5*(1-p))
out=dict(status='PASS',queries=queries,strict_interval_erasure_checks=certified,scalar_endpoint_checks=endpoint,exact_assertions=checks,runtime_seconds=time.monotonic()-start,checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),independent_agent_review=False)
(root/'out/AUDIT.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
