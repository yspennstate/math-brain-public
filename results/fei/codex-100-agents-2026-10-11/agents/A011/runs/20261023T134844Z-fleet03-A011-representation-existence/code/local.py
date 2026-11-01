import sys
sys.dont_write_bytecode=True
from fractions import Fraction as F
from pathlib import Path
import json,time
import check as c
R=Path(__file__).resolve().parents[1];start=time.monotonic();cases=zero=0
for n in range(4):
 for label in range(2**(2**n)):
  v=tuple(1 if label>>x&1 else -1 for x in range(2**n));A=c.fw(v);P=tuple(x*x for x in A)
  for r in range(4):
   p=F(1,2**r);t=F(1,2**n);rho=p*t;truth=tuple(v[y]-2*v[0]*(u==0 and y==0) for u in range(2**r) for y in range(2**n));newP=tuple(x*x for x in c.fw(truth));data=[sum(newP[u*len(P)+T] for u in range(2**r)) for T in range(len(P))]
   for model in range(3):
    Q=P if model==0 else tuple(x/2 for x in P) if model==1 else tuple(F(i+1,3*sum(range(1,len(P)+1))) for i in range(len(P)));old=c.cost([(i,1,z,q) for i,(z,q) in enumerate(zip(P,Q))])
    for j in range(1,6):
     B=1+4*j*(j+1);beta=(6 if j==1 else 8 if j==2 else 4*B)*rho;alpha=F(9,8) if j==1 else F(5,4) if j==2 else 1+F(1,8*j*(j+1));gamma=(36 if j==1 else 20 if j==2 else 4*(1+8*j*(j+1)))*rho;d=n+r+j+13;rows=[]
     for T in range(len(P)):
      c.ck(data[T]<=alpha*P[T]+gamma*t);floor=(Q[T]+beta*t)/(1+beta)
      for u in range(2**r):
       prob=newP[u*len(P)+T]
       if data[T]:q=floor*prob/data[T]
       else:c.ck(r==0 and prob==0);q=floor;zero+=1
       rows.append((u*len(P)+T,1,prob,q))
     c.ck(sum(q for S,m,z,q in rows)==(sum(Q)+beta)/(1+beta));error=(160 if j==1 else 112 if j==2 else 64*B)*rho*d;c.ck(c.cost(rows)[1]<=alpha*old[1]+error);cases+=1
     if time.monotonic()-start>300:raise RuntimeError('frozen local deadline')
out={'status':'PASS','cases':cases,'zero_data_fibers_retained':zero,'exact_assertions':c.checks,'seconds':time.monotonic()-start,'scope':'All labelled Boolean local functions n0..3, r0..3, three complete models, five stage coefficients; explicit zero-fiber mass checks'}
(R/'out/LOCAL.json').write_text(json.dumps(out,indent=2),encoding='utf-8',newline='');print(json.dumps(out))
