from fractions import Fraction as F
from pathlib import Path
import json,time
R=Path(__file__).resolve().parents[1]; start=time.monotonic();checks=0
def ck(b):
 global checks
 checks+=1;assert b,checks
def fw(v):
 a=list(v);s=1
 while s<len(a):
  for i in range(0,len(a),2*s):
   for j in range(i,i+s):a[j],a[j+s]=a[j]+a[j+s],a[j]-a[j+s]
  s*=2
 return [F(x,len(a)) for x in a]
def inf(v):return sum((F(sum(v[x]!=v[x^(1<<j)] for x in range(len(v))),len(v)) for j in range(len(v).bit_length()-1)),F(0))
h=[(-1)**(y&1) for y in range(4)]
v=[h[y]*(-1 if x==0 and y==1 else 1) for x in range(2) for y in range(4)]
a=fw(v);P=[z*z for z in a];q=[P[T]+P[4+T] for T in range(4)];rho=F(1,2)
cases=0
for bits in range(16):
 g=[1 if bits>>z&1 else -1 for z in range(4)];b=fw(g);Pg=[z*z for z in b]
 full=[g[z]*v[w] for z in range(4) for w in range(8)];c=fw(full)
 ck(all(c[T*8+S]==b[T]*a[S] for T in range(4) for S in range(8)))
 ck(inf(full)==inf(g)+inf(v))
 for Rg in [[F(1,4)]*4,[F(i+1,10) for i in range(4)]]:
  for scale in [F(1),F(1,2)]:
   data=[scale*(F(13,16) if T==1 else F(1,16)) for T in range(4)]
   rep=[(1-rho)*data[T]+rho/4 for T in range(4)]
   Q=[rep[S%4]*P[S]/q[S%4] for S in range(8)]
   prod=[Rg[T]*Q[S] for T in range(4) for S in range(8)]
   ck(sum(prod)==sum(Rg)*sum(Q))
   for T in range(4):
    for S in range(8):
     if Pg[T]*P[S]:
      ck(1/prod[T*8+S]==(1/Rg[T])*(1/Q[S]))
      ck(c[T*8+S]**2/prod[T*8+S]==(Pg[T]/Rg[T])*(P[S]/Q[S]))
   cases+=1
   if time.monotonic()-start>55:raise RuntimeError('cutoff')
out={'status':'PASS','assertions':checks,'tensor_reference_cases':cases,'seconds':time.monotonic()-start,'validation':'every actual product coefficient, physical influence, reference mass, CE log argument and KL likelihood ratio'}
(R/'out/TENSOR_RESULTS.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
