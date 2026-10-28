from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
import sys,json,time
import prior as p
R=Path(__file__).resolve().parents[1];start=time.perf_counter();pilot='--pilot' in sys.argv;counts={}
def ck(v,k):
 assert v,k
 counts[k]=counts.get(k,0)+1
def ge(v):return not v or p.interval(v)[0]>=0
def cv(x):return {2:F(x)} if x else {}
def tables(n):return [tuple(1 if m>>x&1 else -1 for x in range(1<<n)) for m in range(1<<(1<<n))]
@lru_cache(None)
def cf(t):
 N=len(t);w=tuple(F(sum(t[x]*(-1 if (x&s).bit_count()%2 else 1) for x in range(N)),N) for s in range(N))
 ck(w==tuple(p.fwht(list(t))),'characters_FWHT')
 return w
@lru_cache(None)
def ent(ps):return p.ent(ps)
def audit(E,hs):
 active=sorted(set(E));r=len(active);M=len(E);N=len(hs[0]);n=N.bit_length()-1;k=M.bit_length()-1
 ps={s:F(E.count(s),M) for s in active};ws={s:cf(hs[s]) for s in active}
 indicators={s:tuple(F(v==s) for v in E) for s in active};vs={s:cf(indicators[s]) for s in active}
 out=tuple(hs[E[z]][x] for z in range(M) for x in range(N));fw=cf(out)
 P=tuple(c*c for c in fw);ck(sum(P)==1,'full_Parseval')
 mix=[];rank_checks=0
 for a in range(N):
  ma=sum(ps[s]*ws[s][a]**2 for s in active)
  ck(ma==sum(P[a+N*b] for b in range(M)),'old_spectral_marginal')
  for b in range(M):
   Q=sum(ws[s][a]**2*vs[s][b]**2 for s in active)
   rr=sum(ws[s][a]!=0 for s in active)
   ck(P[a+N*b]<=rr*Q,'pointwise_rank_majorant')
   ck(fw[a+N*b]==sum(ws[s][a]*vs[s][b] for s in active),'exact_spectral_superposition')
   mix.append(Q)
 ck(sum(mix)==1,'mixture_reference_normalized')
 H=ent(P);Hp=ent(tuple(ps.values()))
 retained=p.add(*(p.mul(ent(tuple(c*c for c in ws[s])),ps[s]) for s in active))
 indicator_entropy=p.add(*(p.mul(ent(tuple(c*c/ps[s] for c in vs[s])),ps[s]) for s in active))
 rhs=p.add(retained,p.mul(Hp,r),p.mul(indicator_entropy,r))
 ck(ge(p.add(rhs,p.mul(H,-1))),'retained_row_entropy_bound')
 # Normalized indicator has constant spectral atom p_s.
 for s in active:
  Hes=ent(tuple(c*c/ps[s] for c in vs[s]));h2=ent((ps[s],1-ps[s]))
  ck(ge(p.add(h2,cv(k*(1-ps[s])),p.mul(Hes,-1))),'indicator_entropy_bound')
 rowI=sum(ps[s]*p.data(hs[s])[2] for s in active)
 edges=F(0)
 for z in range(M):
  for j in range(k):
   zz=z^(1<<j)
   if z<zz:edges+=F(sum(a!=b for a,b in zip(hs[E[z]],hs[E[zz]])),N)*F(2,M)
 fullI=p.data(out)[2]
 ck(rowI+edges==fullI,'exact_original_influence')
 ck(time.perf_counter()-start<55,'runtime_guard')

Es=list(product(range(3),repeat=4));small=list(product(tables(1),repeat=3))
if pilot:Es=Es[:8];small=small[:8]
for E in Es:
 for hs in small:audit(E,hs)
large=list(product(tables(2),repeat=3))
if pilot:large=large[:8]
for hs in large:audit((0,1,1,2),hs)

# Independent reproduction of A092's all-seed physical edge formula.
seeds=[(n,g) for n in [1,2] for g in tables(n)]+[(3,tables(3)[mask]) for mask in [0,1,3,7,15,23,105,255]]
source_cases=0
for n,g in seeds[:4] if pilot else seeds:
 for k in [2,3]:
  N=n+k;out=tuple(g[x&((1<<n)-1)]*(-1 if x.bit_count()<=1 else 1) for x in range(1<<N))
  D0=sum(g[0]!=g[1<<i] for i in range(n));D1=sum(g[1<<j]!=g[(1<<i)|(1<<j)] for i in range(n) for j in range(n) if i!=j)
  predicted=p.data(g)[2]+F(N*(N-1)-2*k*D0-2*D1,1<<(N-1))
  ck(p.data(out)[2]==predicted,'A092_actual_influence_formula')
  fresh=sum(p.data(out)[3][n:]);ck(fresh==F(k*(N-1),1<<(N-1)),'actual_fresh_boundary')
  source_cases+=1
ck((4*34)**4<2**34,'A092_entropy_tail_base_integer')
ck(35**4<2*34**4,'A092_entropy_tail_ratio_integer')
out={'status':'PASS','pilot':pilot,'summary_circuits':len(Es)*len(small)+len(large),'source_cases':source_cases,'counts':counts,'total_predicates':sum(counts.values()),'runtime_seconds':time.perf_counter()-start,'scope':'finite exact validation; universal statements proved analytically; FEI OPEN'}
(R/'out'/('PILOT.json' if pilot else 'VALIDATION.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
