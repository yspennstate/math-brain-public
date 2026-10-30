from pathlib import Path
from itertools import combinations
import time,json,sys
R=Path(__file__).resolve().parents[1];start=time.perf_counter();checks=0;roots=0;nonzero=0;canonical=0
def ck(x):
 global checks
 assert x;checks+=1
 if time.perf_counter()-start>55:raise RuntimeError('frozen limit')
def rank(vs):
 b={}
 for v in vs:
  while v:
   k=v.bit_length()
   if k in b:v^=b[k]
   else:b[k]=v;break
 return len(b)
pilot='--pilot' in sys.argv
for n in range(1,3 if pilot else 4):
 N=1<<n;vs=range(1,N);bases=[b for b in combinations(vs,n) if rank(b)==n]
 ck(len(bases)==[0,1,3,28][n])
 for mask in range(1<<N):
  U={x for x in range(N) if mask>>x&1}
  if not U:continue
  left=set(U);labels={};k=0
  while left:
   todo=[left.pop()]
   while todo:
    x=todo.pop();labels[x]=k
    for i in range(n):
     y=x^(1<<i)
     if y in left:left.remove(y);todo.append(y)
   k+=1
  w={v:sum((x in U)!=(x^v in U) for x in range(N)) for v in vs}
  gam={v:sum(x^v in U and labels[x]!=labels[x^v] for x in U) for v in vs}
  ell={v:w[v]+2*gam[v] for v in vs};ck(all(0<=z<=2*N for z in ell.values()))
  Iold=sum(w[1<<i] for i in range(n));ck(all(gam[1<<i]==0 for i in range(n)))
  best=min(bases,key=lambda b:sum(ell[v] for v in b));val=sum(ell[v] for v in best)
  greed=[]
  for v in sorted(vs,key=lambda v:(ell[v],v)):
   if rank(greed+[v])>len(greed):greed.append(v)
  ck(val==sum(ell[v] for v in greed));ck(val<=Iold)
  levels=sorted({0,2*N,*ell.values()})
  integral=sum((b-a)*(n-rank([v for v in vs if ell[v]<=a])) for a,b in zip(levels,levels[1:]))
  ck(val==integral)
  Inew=sum(w[v] for v in best);G=sum(gam[v] for v in best);rho=Iold-Inew;rhoL=Iold-val
  ck(rho==rhoL+2*G);ck(0<=2*G<=rho);ck(rhoL>=0)
  # All input-minimal roots force zero release/flux in every labelled optimum.
  ordinary=min(sum(w[v] for v in b) for b in bases)
  if ordinary==Iold:
   canonical+=1;ck(rho==rhoL==G==0)
  nonzero+=int(rho>0);roots+=1
out={'status':'PASS','pilot':pilot,'assertions':checks,'nonempty_roots':roots,'positive_release_roots':nonzero,'input_minimal_roots':canonical,'seconds':time.perf_counter()-start,'method':'exhaustive independent bases versus greedy and finite rank integral; integer arithmetic'}
(R/'out'/('RANK_PILOT.json' if pilot else 'RANK_CHECK.json')).write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
