from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,time
R=Path(__file__).resolve().parents[1]; start=time.perf_counter(); checks=0
def ck(b):
 global checks
 checks+=1
 assert b,checks
def plus(*xs):
 a={}
 for x in xs:
  for p,c in x.items():a[p]=a.get(p,F(0))+c
 return {p:c for p,c in a.items() if c}
def times(x,c):return {p:v*c for p,v in x.items() if v*c}
@lru_cache(None)
def log(q):
 q=F(q);a={}
 for n,s in [(q.numerator,1),(q.denominator,-1)]:
  p=2
  while p*p<=n:
   while n%p==0:a[p]=a.get(p,0)+s;n//=p
   p+=1
  if n>1:a[n]=a.get(n,0)+s
 return {p:F(v) for p,v in a.items() if v}
def ln(q):
 z=(q-1)/(q+1)
 s=sum((2*z**(2*j+1)/F(2*j+1) for j in range(24)),F(0))
 e=2*abs(z)**49/(49*(1-z*z))
 return s-e,s+e
@lru_cache(None)
def lp(p):
 if p==2:return F(1),F(1)
 k=p.bit_length()-1;a,b=ln(F(p,2**k));c,d=ln(F(2));scale=2**80
 x=k+a/d;y=k+b/c
 return F((x*scale).__floor__(),scale),F((y*scale).__ceil__(),scale)
def interval(x):
 a=b=F(0)
 for p,c in x.items():
  l,h=lp(p);a+=c*(l if c>=0 else h);b+=c*(h if c>=0 else l)
 return a,b
def ce(p,q):return plus(*(times(log(v),-w) for w,v in zip(p,q) if w))
def spectrum(v):
 a=list(v);h=1
 while h<len(a):
  for j in range(0,len(a),2*h):
   for k in range(j,j+h):x,y=a[k],a[k+h];a[k]=x+y;a[k+h]=x-y
  h*=2
 return [F(x,len(a))**2 for x in a]
def inf(v,i):return F(sum(x!=v[j^(1<<i)] for j,x in enumerate(v)),len(v))
def marginal(q,i):
 out=[F(0)]*(len(q)//2)
 for s,w in enumerate(q):out[(s&((1<<i)-1))|((s>>(i+1))<<i)]+=w
 return out
def children(v,i):return [[x for j,x in enumerate(v) if (j>>i)&1==b] for b in [0,1]]
def decrement(v,q,i):
 vs=children(v,i);qs=marginal(q,i)
 return plus(ce(spectrum(v),q),times(plus(*(ce(spectrum(w),qs) for w in vs)),-F(1,2)))

# Appended to A070's own exact arithmetic primitives; no A069 code is imported.
from itertools import product
def joint(a,b,m,k,theta,eps):
 n=(len(a)-1).bit_length();N=2**m;M=N//2**k;t=F(1,N*N)
 A=(1+3*t*theta)/4;B=5*(1-t*theta)/16;r=7*(1-t*theta)/(32*(N-1))
 a0=A+(2**k-1)*r;b0=B+(2**k-1)*r;w=2**k*r
 qc=[a0,b0]+[w]*(2*M-2)
 core=[F(j+1,len(a)*(len(a)+1)//2) for j in range(len(a))]
 v=[]
 for x in range(len(a)*2*M):
  y=x%len(a);z=x//len(a);c=z&1
  p=F(a[y]+b[y],2);q=F(a[y]-b[y],2)
  v.append((-1 if z==0 else 1)*(eps*p+(-1)**c*q))
 ref=[core[s%len(a)]*qc[s//len(a)] for s in range(len(v))]
 return v,ref,core,qc

for eps in [-1,1]:
 a=[F(7,5),F(-1,5)];b=[F(1),F(1)]
 v,ref,cr,qc=joint(a,b,1,0,F(1,3),eps)
 ck(sum(spectrum(v))==1)
 av=children(a,0);bv=children(b,0);rr=marginal(cr,0)
 costs=[ce([(x+y)/2 for x,y in zip(spectrum(aa),spectrum(bb))],rr) for aa,bb in zip(av,bv)]
 pc=[(x+y)/2 for x,y in zip(spectrum(a),spectrum(b))]
 db=plus(ce(pc,cr),times(plus(*costs),-F(1,2)))
 ck(decrement(v,ref,0)==db)
 ch=children(v,0)
 ck([sum(spectrum(w)) for w in ch]==[F(37,25),F(13,25)])
 energy=sum(p for s,p in enumerate(spectrum(v)) if s&1)
 ck(energy==F(8,25));ck(inf(v,0)==F(1,2));ck(energy!=inf(v,0))
result=dict(status='PASS',assertions=checks,cases=2,core_CE_identity='HOLDS for unnormalized real children',root_norm=1,child_squared_norms=['37/25','13/25'],core_spectral_energy='8/25',core_physical_pivotal_probability='1/2',elapsed_seconds=time.perf_counter()-start)
(R/'out/REAL_GUARD.json').write_bytes((json.dumps(result,indent=2)+'\n').encode('utf-8'))
print(json.dumps(result))
