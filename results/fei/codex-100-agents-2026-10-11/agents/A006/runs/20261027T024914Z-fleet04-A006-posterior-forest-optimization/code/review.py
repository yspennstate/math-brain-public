"""Independent physical reconstruction of A010's sidewise identities; no source import."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import time,json
R=Path(__file__).resolve().parents[1];start=time.monotonic();checks=0
def ck(x):
 global checks
 checks+=1
 assert x,checks
def fwht(v):
 v=v[:];h=1
 while h<len(v):
  for j in range(0,len(v),2*h):
   for k in range(j,j+h):v[k],v[k+h]=v[k]+v[k+h],v[k]-v[k+h]
  h*=2
 return v
rows=[]
for r,s in [(1,1),(1,2),(2,1),(2,2)]:
 n=3+2*(r+s);N=1<<n
 X=[3|(3<<(3+2*j)) for j in range(r)]
 Y=[6|(3<<(3+2*r+2*j)) for j in range(s)]
 truth=[1 if all(x&m for m in X+Y) else -1 for x in range(N)]
 W=fwht(truth);p=[F(w*w,N*N) for w in W]
 a=F(3,4)**r;b=F(3,4)**s;u=(1+a)/2;v=(1+b)/2
 I=F(sum(truth[x]!=truth[x^(1<<i)] for x in range(N) for i in range(n)),N)
 ck(I==F(5,4)-(a+b)/4-3*a*b/4+(r*a*(1+b)+s*b*(1+a))/6)
 xm=sum(3<<(3+2*j) for j in range(r));ym=sum(3<<(3+2*r+2*j) for j in range(s))
 ck(sum(p[A] for A in range(N) if A&xm)==v*a*(1-a))
 ck(sum(p[A] for A in range(N) if A&ym)==u*b*(1-b))
 ck(p[5]==(1-a)**2*(1-b)**2/16)
 # Full tuple occupation DP: tuple probability and K-weighted probability.
 mu={0:F(1)};occ={0:F(0)}
 for m,alpha in zip(X+Y,[F(1,2*r)]*r+[F(1,2*s)]*s):
  bits=[i for i in range(n) if m>>i&1]
  local={sum(1<<bits[i] for i in range(4) if z>>i&1): (1-alpha if z==0 else alpha/15) for z in range(16)}
  new={};tag={}
  for A,pv in mu.items():
   for B,q in local.items():
    C=A|B;new[C]=new.get(C,F(0))+pv*q
    tag[C]=tag.get(C,F(0))+(occ[A]+pv*bool(B))*q
  mu,occ=new,tag
 ck(sum(occ.values())==1);ck(occ[0]==0)
 # Every actual tuple witnesses side-product lower bounds (K>=1).
 side=[]
 for ms,den in [(X,2*r),(Y,2*s)]:
  law={0:F(1)}
  for m in ms:
   bits=[i for i in range(n) if m>>i&1];new={}
   for A,z in law.items():
    for mask in range(16):
     B=sum(1<<bits[i] for i in range(4) if mask>>i&1);q=1-F(1,den) if not B else F(1,15*den)
     new[A|B]=new.get(A|B,F(0))+z*q
   law=new
  side.append(law)
 for A in range(1,N):
  bx=A&(xm|3);by=A&(ym|4)
  ck(occ.get(A,F(0))>=side[0].get(bx,F(0))*side[1].get(by,F(0)))
 rows.append({'r':r,'s':s,'physical_inputs':N,'I':str(I),'full_source_mass':str(sum(occ.values()))})
for t in range(4,257):
 a=F(3,4)**t
 ck(a<F(1,3));ck(t*a<=F(81,64));ck(t*t*a<7)
 if t>=7:ck(3*(t+1)**2<=4*t*t)
for r in range(4,65):
 for s in range(4,65):
  a=F(3,4)**r;b=F(3,4)**s
  I=F(5,4)-(a+b)/4-3*a*b/4+(r*a*(1+b)+s*b*(1+a))/6
  ck(F(5,4)<I<2)
  ck((1-a)**2*(1-b)**2/16>F(1,81))
ck(F(1429,60)<24)
ck(time.monotonic()-start<55)
out={'status':'PASS','assertions':checks,'seconds':time.monotonic()-start,'physical_rows':rows,'scalar_pairs':61**2,'reviewed_claim':'A010-UNEQUAL-CORE-RETUNING-AND-UNIFORM-WEIGHT-OBSTRUCTION@1','scope':'whole analytic proof reconstructed; finite checks supplement all-r,s argument'}
(R/'out/REVIEW.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:out[k] for k in ['status','assertions','seconds']}))
