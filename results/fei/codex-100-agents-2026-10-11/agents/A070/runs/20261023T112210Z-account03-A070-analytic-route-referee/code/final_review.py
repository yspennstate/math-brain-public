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

for m,d in product(range(1,7),[F(0),F(1,256)]):
 theta=F(1,512);rho=F(1,2**m);t=rho*rho;alpha=1-t*theta;qr=[]
 for s in range(2**(m+2)):
  if s==0:q=t*theta
  elif s<4:q=alpha*{1:F(1,4),2:F(1,4),3:F(1,16)}[s]
  else:q=alpha*(F(7,80) if s&2 else F(7,20))/(2*(2**m-1))
  qr.append(q)
 f0=[];f1=[]
 for x in range(len(qr)):
  c=x&1;u=(x>>1)&1;z=x>>2;q=-1 if c==0 and z==0 else 1
  f0.append(q*(-1)**u);f1.append(q*(-1)**c)
 dc=plus(times(decrement(f0,qr,1),1-d),times(decrement(f1,qr,1),d))
 x=t*theta
 U0=plus(times(log((1+3*x)/(1-x)),(1-rho)**2),times(log(5),2*rho-t))
 U1=plus(times(log((1+3*x)/(4*x)),t),times(log(F(5,4)),1-t))
 ck(dc==plus(times(U0,1-d),times(U1,d)))
 ck(interval(U0)[1]<F(13,4));ck(interval(U1)[1]<F(13,4));ck(interval(dc)[1]<4*(1-d))
 if d:
  p=t*d;q=x
  kl=plus(times(log(p/q),p),times(log((1-p)/(1-q)),1-p))
  ck(interval(kl)[0]>0);ck(interval(kl)[1]<p<=F(1,1024))
h=plus(times(log(F(1,256)),-F(1,256)),times(log(F(255,256)),-F(255,256)))
ck(interval(h)[1]<F(19,512));ck(F(19,512)<F(1,16))
ck((F(1,2)+F(63,64)-F(1,1024))/2==F(1519,2048));ck(F(1519,2048)>F(5,8))
ck(F(5,8)-F(7,12)==F(1,24));ck(F(1,24)>F(59,2560))
p=R.parent/'20261022T234315Z-account03-A070-analytic-route-referee/out/CORE_CHECKPOINT.json'
cert=json.loads(p.read_text(encoding='utf-8'));ck(F(cert['P_core_interval'][1])<F(7,12))
result=dict(status='PASS',assertions=checks,early_u_cases=12,theta='1/512 frozen from root',actual_disagreement=['0','1/256'],owner_capacity_lower='1519/2048',P_core_upper='7/12',remaining_original_earmark_lower='1/24',elapsed_seconds=time.perf_counter()-start)
(R/'out/FINAL_REVIEW.json').write_bytes((json.dumps(result,indent=2)+'\n').encode('utf-8'));print(json.dumps(result))
