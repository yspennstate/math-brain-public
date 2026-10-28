from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations
from collections import Counter
from functools import lru_cache
import json,time,sys
import arithmetic as a
RUN=Path(__file__).resolve().parents[1];start=time.perf_counter();checks=0
def ck(v):
 global checks
 checks+=1
 assert v,checks
 if time.perf_counter()-start>55:raise RuntimeError('55-second guard')
@lru_cache(None)
def entropy(key,N):
 lo=hi=Q(0)
 for v,k in key:
  if v:
   l,h=a.log2(Q(v,N*N));lo-=Q(k*v,N*N)*h;hi-=Q(k*v,N*N)*l
 return lo,hi
def H(w,N):return entropy(tuple(sorted(Counter(v*v for v in w).items())),N)
def child(f,i,b):
 return [f[(x&((1<<i)-1))|((x>>i)<<(i+1))|(b<<i)] for x in range(len(f)//2)]
branches=Counter();roots=cuts=0;guard=[]
def case(seed,E):
 global roots,cuts
 N=len(seed);n=(N-1).bit_length();p=Q(1,N);R=len(E);f=seed.copy()
 for x in E:f[x]*=-1
 old=a.fwht(seed);w=a.fwht(f);support=[s for s,v in enumerate(old) if v]
 ck(all((x^y).bit_count()>=3 for x,y in combinations(support,2)))
 ck(len(support)*(n+1)<=N)
 sourceI=a.infs(seed);newI=a.infs(f);root=H(w,N)
 for i in range(n):
  cuts+=1;I=newI[i];FI=sourceI[i]
  c0,c1=[child(f,i,b) for b in (0,1)]
  h0,h1=H(a.fwht(c0),N//2),H(a.fwht(c1),N//2)
  Lup=root[1]-(h0[0]+h1[0])/2
  ck(sum(newI)==I+(sum(a.infs(c0))+sum(a.infs(c1)))/2)
  if not R:
   ck(Counter(v*v for v in w if v)==Counter(4*v*v for v in a.fwht(c0) if v));continue
  ck(abs(I-FI)<=2*R*p)
  if not I:branches['irrelevant_G']+=1;continue
  ck(I>=2*p)
  beta=Q(0)
  for s in range(N):
   if s>>i&1:continue
   t=s|(1<<i);ck(not(old[s] and old[t]))
   if old[s] or old[t]:
    off=t if old[s] else s;beta+=Q(w[off]*w[off],N*N)
  if FI==0:
   branches['seed_independent']+=1
   U=sum((x in E)!=(x^(1<<i) in E) for x in range(N) if not(x>>i&1))
   ck(I==2*p*U);ck(I<=2*R*p)
   for s in support:ck(Q(abs(w[s|(1<<i)]),N)<=I)
   ck(beta<=len(support)*I*I)
   if n==3 and R==1 and not support[0]:guard.append({'R':R,'actual_I':str(I),'false_seed_dependent_bound':str((n+1)*p)})
  else:
   si=sum(bool(s>>i&1) for s in support)
   ck(FI>=Q(1,si));ck(FI>=(n+1)*p)
   if n+1>=4*R:
    branches['seed_dependent_high_dimension']+=1
    ck(I>=(n+1-2*R)*p);ck(I>=Q(n+1,2)*p)
   else:branches['seed_dependent_low_dimension']+=1
  ck(Lup<Q(37,4)*R*I)
  ck(10*R*I-Lup>Q(3,2)*R*p)
 roots+=1
pilot='--pilot' in sys.argv
for s in range(8):
 for sign in (-1,1):
  seed=[sign*(-1 if (x&s).bit_count()%2 else 1) for x in range(8)]
  for R in range(3 if pilot else 4):
   for E in combinations(range(8),R):case(seed,E)
if not pilot:
 spec=json.loads((RUN/'out/FROZEN_SPEC.json').read_text(encoding='utf-8'))
 for n in (6,9):
  h=[-1]+[1]*((1<<(n//3))-1);seed=a.coded_truth(h)
  for E in spec['domain']['n'+str(n)+'_edits']:case(seed,E)
out={'status':'PASS','assertions':checks,'roots':roots,'coordinate_cuts':cuts,'branches':dict(branches),'seed_independent_boundary_guard':guard[:1],'runtime_seconds':time.perf_counter()-start,'pilot':pilot,'arithmetic':'integer Walsh/physical edges, Fraction, rigorous rational logarithm intervals'}
(RUN/'out'/('PILOT.json' if pilot else 'EXACT_CHECK.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
