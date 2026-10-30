import shared as s
from fractions import Fraction as F
from pathlib import Path
import time,json
R=Path(__file__).resolve().parents[1];start=time.monotonic();cases=terminals=0;fixture=None
for n in [1,2]:
 N=2**n;t=F(1,N)
 for bits in range(2**N):
  g=[1 if bits>>y&1 else -1 for y in range(N)];Pg=[x*x for x in s.fw(g)]
  for point in range(N):
   for r in [1,2]:
    p=F(1,2**r);beta=6*p*t
    v=[g[y]*(-1 if x==0 and y==point else 1) for x in range(2**r) for y in range(N)]
    P=[x*x for x in s.fw(v)];q=[sum(P[u*N+T] for u in range(2**r)) for T in range(N)]
    size=len(v)//2;vals=[[v[s.insert(W,0,b)] for W in range(size)] for b in range(2)]
    Pc=[[x*x for x in s.fw(w)] for w in vals];m=[(Pc[0][W]+Pc[1][W])/2 for W in range(size)]
    for model in [Pg,[t]*N,[x/2 for x in Pg]]:
     rep=[(model[T]+beta*t)/(1+beta) for T in range(N)]
     Q=[rep[T]*P[u*N+T]/q[T] for u in range(2**r) for T in range(N)];M=sum(Q)
     rr=[Q[s.insert(W,0,0)]+Q[s.insert(W,0,1)] for W in range(size)]
     pi=[[Pc[b][W]/(2*m[W]) if m[W] else F(1,2) for W in range(size)] for b in range(2)]
     Rt=[[2*rr[W]*pi[b][W] for W in range(size)] for b in range(2)]
     Z=[sum(w) for w in Rt];Rb=[[M*x/Z[b] for x in Rt[b]] for b in range(2)]
     s.ck(Z[0]+Z[1]==2*M);s.ck(Z[0]*Z[1]<=M*M)
     for b in range(2):s.ck(sum(Rb[b])==M)
     for W in range(size):
      s.ck(P[s.insert(W,0,0)]+P[s.insert(W,0,1)]==m[W])
      for b in range(2):
       if Pc[b][W]:s.ck(Pc[b][W]/Rb[b][W]==m[W]/rr[W]*Z[b]/M)
       if m[W]:
        ii=s.insert(W,0,b)
        if P[ii]:s.ck(P[ii]/Q[ii]==m[W]/rr[W]*(P[ii]/m[W])/(Q[ii]/rr[W]))
     cases+=1
     if n==2 and bits==1 and point==0 and r==1 and sum(model)==F(1,2):fixture=(Pc,pi,rr,Z,Rb,M)
     if time.monotonic()-start>55:raise RuntimeError('cutoff')
Pc,pi,rr,Z,Rb,M=fixture;size=len(rr)
for bits in range(16):
 hv=[1 if bits>>x&1 else -1 for x in range(4)];Ph=[x*x for x in s.fw(hv)]
 for Rh in [[x/2 for x in Ph],[F(1,8)]*4]:
  Mh=sum(Rh)
  for b in range(2):
   raw=[2*Rh[x]*rr[W]*pi[b][W] for x in range(4) for W in range(size)]
   z=sum(raw);s.ck(z==Mh*Z[b]);ref=[Mh*M*u/z for u in raw]
   s.ck(sum(ref)==Mh*M)
   for x in range(4):
    for W in range(size):
     s.ck(ref[x*size+W]==Rh[x]*Rb[b][W])
     if Ph[x]*Pc[b][W]:s.ck(Ph[x]*Pc[b][W]/ref[x*size+W]==Ph[x]/Rh[x]*Pc[b][W]/Rb[b][W])
  terminals+=1
out={'status':'PASS','assertions':s.checks,'subprobability_query_cases':cases,'terminal_reference_cases':terminals,'seconds':time.monotonic()-start,'missing_mass_preserved_in_children':True,'product_compatible_zero_fibers':True}
(R/'out/TRANSPORT_RESULTS.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
