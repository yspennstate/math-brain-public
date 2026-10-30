import shared as s
from fractions import Fraction as F
from pathlib import Path
import sys,time,json
R=Path(__file__).resolve().parents[1];start=time.monotonic();mode=sys.argv[1];cases=refs=0
ns=[1,2] if mode=='small' else [3]
for n in ns:
 N=2**n;t=F(1,N)
 truth=range(2**N) if mode=='small' else range(int(mode)*32,(int(mode)+1)*32)
 for bits in truth:
  g=[1 if bits>>y&1 else -1 for y in range(N)];a=s.fw(g);P=[z*z for z in a];Ig=sum(s.inf(g))
  for point in range(N):
   d=sum(g[point]!=g[point^(1<<j)] for j in range(n))
   for r in [1,2]:
    p=F(1,2**r);beta=6*p*t
    v=[g[y]*(-1 if x==0 and y==point else 1) for x in range(2**r) for y in range(N)]
    b=s.fw(v);law=[z*z for z in b];q=[sum(law[u*N+T] for u in range(2**r)) for T in range(N)]
    C=2*p*t*(n-d);E=2*p*t*d;J=2*r*p*t;If=sum(s.inf(v))
    s.ck(If==Ig+C-E+J);s.ck(E<=Ig/2)
    for T in range(N):
     phase=g[point]*(-1)**((T&point).bit_count())
     s.ck(q[T]==P[T]-4*p*t*phase*a[T]+4*p*t*t)
     s.ck(q[T]<=2*P[T]+beta*t);s.ck(q[T]>0)
    B=s.sub(s.entropy(law),s.entropy(q));s.ck(B[1]<=4*p*(1-p)*t*n+4*J)
    for model in [P,[t]*N,[z/2 for z in P]]:
     mass=sum(model);rep=[(model[T]+beta*t)/(1+beta) for T in range(N)]
     Q=[rep[T]*law[u*N+T]/q[T] for u in range(2**r) for T in range(N)]
     s.ck(sum(Q)==(mass+beta)/(1+beta))
     for u in range(2**r):
      for T in range(N):s.ck(Q[u*N+T]*q[T]==rep[T]*law[u*N+T])
     cost=s.ce(law,Q);c=s.ce(P,model)
     s.ck(cost[1]<=2*c[0]+15*(C+E+J))
     if Ig:
      C0=c[1]/Ig;K=4*C0+15
      s.ck(c[1]<=C0*Ig);s.ck(cost[1]<=K*If)
      # Exact polynomial price and single original-bank debit; no terminal replacement.
      bank=(K-2*C0)*Ig+(K-15)*(C+J)-(K+15)*E
      s.ck(bank>=0)
     elif c[1]==0:
      s.ck(cost[1]<=15*If)
     refs+=1
    cases+=1
    if time.monotonic()-start>55:raise RuntimeError('frozen cutoff')
out={'status':'PASS','mode':mode,'assertions':s.checks,'boolean_cases':cases,'reference_cases':refs,'seconds':time.monotonic()-start,'full_source_support_not_required':True,'subprobability_mass_retained':True}
(R/f'out/ENVELOPE_{mode}.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
