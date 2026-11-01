from pathlib import Path
from fractions import Fraction as F
import json,time
R=Path(__file__).resolve().parents[1];start=time.monotonic();count=0
def ck(b):
 global count
 count+=1
 assert b,count
 if time.monotonic()-start>55:raise RuntimeError('55 second cap')
def fac(n):
 a={};d=2
 while d*d<=n:
  while n%d==0:a[d]=a.get(d,0)+1;n//=d
  d+=1
 if n>1:a[n]=a.get(n,0)+1
 return a
def add(*xs):
 a={}
 for x in xs:
  for k,v in x.items():a[k]=a.get(k,F(0))+v
 return {k:v for k,v in a.items() if v}
def times(c,x):return {k:c*v for k,v in x.items() if c*v}
def log(x):
 x=F(x);return add({k:F(v) for k,v in fac(x.numerator).items()},{k:F(-v) for k,v in fac(x.denominator).items()})
def div(P,Q):return add(*(times(p,log(p/Q[z])) for z,p in P.items() if p))
def ent(P):return add(*(times(-p,log(p)) for p in P.values() if p))
def ln(x):
 z=(x-1)/(x+1);power=z;v=F(0)
 for j in range(36):v+=2*power/(2*j+1);power*=z*z
 return v,v+2*power/(73*(1-z*z))
l2=ln(F(2));cache={2:(F(1),F(1))}
def bounds(x):
 lo=hi=F(0)
 for p,c in x.items():
  if p not in cache:
   k=p.bit_length()-1;a,b=ln(F(p,1<<k));cache[p]=(k+a/l2[1],k+b/l2[0])
  a,b=cache[p]
  if c<0:a,b=b,a
  lo+=c*a;hi+=c*b
 return lo,hi
rows=[]
for n in range(2,11):
 N=1<<n;p=F(1,N);v=2*p;m=1-4*p+8*p*p
 truth=[-1]+[1]*(N-1)
 walsh=[sum(f*(-1 if (x&s).bit_count()%2 else 1) for x,f in enumerate(truth)) for s in range(N)]
 ck(walsh[0]==N-2);ck(all(a==-2 for a in walsh[1:]))
 P={(s&1,s>>1):F(a*a,N*N) for s,a in enumerate(walsh)}
 PB={z:sum(P[a,z] for a in [0,1]) for z in range(N//2)}
 ck(PB[0]==m);ck(all(q==8*p*p for z,q in PB.items() if z))
 PE={z:P[1,z]/v for z in PB};ck(all(q==2*p for q in PE.values()))
 W1=div(PE,PB)
 formula=add({2:F((1-4*p)*n-2+6*p)},times(-2*p,log(m)))
 ck(W1==formula)
 if n>=3:ck(bounds(add(W1,{2:-F(n,2)+2}))[0]>0)
 theta=F(1)/(1+F(2)**(n-3));Q={(a,z):(theta if a else 1-theta)*q for z,q in PB.items() for a in [0,1]}
 W=div(P,Q);cap=log(1+F(2)**(3-n));hcond=add(ent(P),times(-1,ent(PB)))
 ck(W==add(cap,{2:(n-3)*v},times(-1,hcond)))
 ck(bounds(W)[0]>=0);ck(bounds(add(cap,{2:(n-3)*v},times(-1,W)))[0]>=0)
 # The tempting reference P_B|E makes the singleton occupied divergence zero.
 ck(div(PE,PE)=={})
 if n>=3:ck(bounds(W1)[0]>0)
 else:ck(W1=={})
 if n==10:
  ck(bounds(W1)[0]>7);ck(bounds(W)[1]<F(1,32))
 rows.append({'n':n,'occupation':str(v),'occupied_KL_interval':[str(x) for x in bounds(W1)],'absolute_KL_interval':[str(x) for x in bounds(W)]})
for dummy in [False,True]:
 n=3;N=8
 truth=[-1 if (x&3==0 if dummy else x==0) else 1 for x in range(N)]
 a=[sum(f*(-1 if (x&s).bit_count()%2 else 1) for x,f in enumerate(truth)) for s in range(N)]
 law={s:F(z*z,64) for s,z in enumerate(a)}
 H=ent(law);I=sum((q*s.bit_count() for s,q in law.items()),F(0))
 # The only nonconstant complete child is a two-bit point defect, H=2,a=I=1.
 t=F(1) if dummy else F(1,2);Hbar={2:2*t};S={2:-t}
 D=add(H,{2:-I});sigma=F(0) if dummy else F(1,4)
 ck(bounds(D)[0]>0);ck(S[2]<0);ck(add(D,S)==add(H,times(-1,Hbar),{2:-sigma}))
 if dummy:ck(add(D,S)=={});ck(D=={2:F(1)})
out={'status':'PASS','assertions':count,'seconds':time.monotonic()-start,'domain':'actual point defects n2..10 and two negative-reserve controls; direct character sums; no primary helper imported','rows':rows}
(R/'out/INDEPENDENT_CHECK.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps({k:v for k,v in out.items() if k!='rows'}))
