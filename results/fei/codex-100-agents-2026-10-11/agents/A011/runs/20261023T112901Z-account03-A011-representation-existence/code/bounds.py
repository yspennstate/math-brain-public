import sys
sys.dont_write_bytecode=True
from fractions import Fraction as F
from pathlib import Path
import json,time
import check as core
R=Path(__file__).resolve().parents[1];start=time.monotonic();mode=sys.argv[1];cases=0
for n in (range(1,4) if mode=='first' else range(2,4)):
 for label in range(2**(2**n)):
  v=tuple(1 if label>>x&1 else -1 for x in range(2**n));amps=core.fw(v);P=tuple(z*z for z in amps)
  for r in range(1,4):
   p=F(1,2**r);t=F(1,2**n);rho=p*t
   for model in range(3):
    Q=P if model==0 else tuple(x/2 for x in P) if model==1 else tuple(F(x+1,3*sum(range(1,len(P)+1))) for x in range(len(P)))
    c=core.cost_rows([(i,1,z,q) for i,(z,q) in enumerate(zip(P,Q))])
    for j in ([1] if mode=='first' else range(3,n+2)):
     beta=(6 if j==1 else 4*(1+4*j*(j+1)))*rho;alpha=F(5,4) if j==1 else 1+F(1,8*j*(j+1))
     edited=tuple(v[y]-2*v[0]*(u==0 and y==0) for u in range(2**r) for y in range(2**n));out=tuple(z*z for z in core.fw(edited));rows=[]
     for T,a in enumerate(amps):
      marginal=sum(out[u*len(P)+T] for u in range(2**r));floor=(Q[T]+beta*t)/(1+beta)
      analytical_beta=12*rho if j==1 else beta
      core.ck(marginal<=alpha*P[T]+analytical_beta*t)
      for u in range(2**r):
       prob=out[u*len(P)+T];q=floor*prob/marginal;rows.append((u*len(P)+T,1,prob,q))
     core.ck(sum(q for S,m,z,q in rows)==(sum(Q)+beta)/(1+beta))
     error=(48 if j==1 else 36*(1+4*j*(j+1)))*rho*(n+r)
     core.ck(core.cost_rows(rows)[1]<=alpha*c[1]+error);cases+=1
     if time.monotonic()-start>300:raise RuntimeError('amended300second cutoff')
out={'status':'PASS','mode':mode,'actual_floor_reference_cases':cases,'exact_assertions':core.checks,'seconds':time.monotonic()-start,'scope':'complete actual first floor re-priced without changing model; or actual later scheduled floor, constants included'}
(R/'out'/('BOUND_'+mode+'.json')).write_text(json.dumps(out,indent=2),encoding='utf-8',newline='');print(json.dumps(out))
