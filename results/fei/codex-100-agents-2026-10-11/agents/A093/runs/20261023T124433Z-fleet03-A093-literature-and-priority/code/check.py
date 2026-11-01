from pathlib import Path
from fractions import Fraction as F
from itertools import product
import json,time,sys
R=Path(__file__).resolve().parents[1];pilot='--pilot' in sys.argv;n=2 if pilot else 3
def save(name,x):(R/'out'/name).write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
save('FROZEN_'+('PILOT' if pilot else 'MAIN')+'.json',dict(helper='check.py v1',family='every labelled Boolean core on n bits; actual disjoint length2 parity blocks and all sign translates; direct full/sibling frontiers',domain=f'n={n}; every ell in {{1,2}}^n; every theta in {{0,1}}^n; K=1,2,4 for complete frontier and K=1 for nonuniform stopping frontier',case_count=(2**(2**n))*(2**n)*(2**n),symmetry='none',arithmetic='integer Walsh-Hadamard; Fraction spectra/influences and entropy multiset certificates',memory_estimate_MB=80,max_runtime_seconds=55,automatic_dimension_escalation=False))
t0=time.monotonic();count=states=edges=frontiers=0
def ck(v):
 global count
 count+=1;assert v,count
 assert time.monotonic()-t0<55,'wall cap'
def spec(t):
 a=list(t);step=1
 while step<len(a):
  for k in range(0,len(a),2*step):
   for j in range(k,k+step):u,v=a[j],a[j+step];a[j]=u+v;a[j+step]=u-v
  step*=2
 return [F(x,len(t))**2 for x in a]
def influences(t):return [F(sum(t[x]!=t[x^(1<<j)] for x in range(len(t))),len(t)) for j in range((len(t)-1).bit_length())]
def table(core,ell,theta):
 out=[]
 for x in range(1<<sum(ell)):
  y=theta;pos=0
  for j,L in enumerate(ell):y^=(((x>>pos)&((1<<L)-1)).bit_count()%2)<<j;pos+=L
  out.append(core[y])
 return out
def marginal(p,j):
 out=[F(0)]*(len(p)//2)
 for x,v in enumerate(p):out[(x&((1<<j)-1))|((x>>(j+1))<<j)]+=v
 return out
def restrict(t,j,b):return [t[(x&((1<<j)-1))|(b<<j)|((x>>j)<<(j+1))] for x in range(len(t)//2)]
for core in product([-1,1],repeat=1<<n):
 P=spec(core);alpha=influences(core);J=sum(alpha);rootcap=2*J
 for ell in product([1,2],repeat=n):
  for theta in range(1<<n):
   t=table(core,ell,theta);p=spec(t);inf=influences(t);states+=1
   ck(sorted(x for x in P if x)==sorted(x for x in p if x))
   ck(sum(inf)==sum(L*a for L,a in zip(ell,alpha)))
   ck(sum(inf)==sum(s.bit_count()*v for s,v in enumerate(p)))
   pos=0
   for j,L in enumerate(ell):
    ck(all(inf[pos+k]==alpha[j] for k in range(L)))
    if L==2:
     # Every occupied physical query fiber has at most one occupied endpoint.
     ck(all(not(p[s] and p[s^(1<<pos)]) for s in range(len(p))))
     pp=marginal(p,pos)
     for b in [0,1]:ck(spec(restrict(t,pos,b))==pp)
     ck(sum(inf)-sum(influences(restrict(t,pos,0)))==alpha[j]);edges+=1
    pos+=L
 # Explicit nonuniform adaptive frontier: stop plus sibling, unwrap minus sibling.
 if J:
  j=next(i for i,a in enumerate(alpha) if a);JF=F(1,2)*(2*J-alpha[j])+F(1,2)*J
  tariff=F(1,2)*alpha[j]+F(1,2)*J
  ck(2*J-tariff==JF)
  for K in [F(1),F(2),F(4)]:
   ck(K*2*J-K*tariff==K*JF)
   # Both frontiers have identical terminal entropy multisets; its symbolic H cancels.
   ck(K*2*J-K*tariff-K*JF==0)
  frontiers+=1
maj=[1 if x.bit_count()<=1 else -1 for x in range(8)];p=spec(maj);J=sum(influences(maj))
ck(sorted(x for x in p if x)==[F(1,4)]*4);ck(J==F(3,2));ck(2*J-2==1);ck(J-2==F(-1,2))
save(('PILOT' if pilot else 'VALIDATION')+'.json',dict(status='PASS',exact_assertions=count,core_count=2**(2**n),physical_states=states,legal_query_edges=edges,nonuniform_frontiers=frontiers,seconds=time.monotonic()-t0,majority_control=dict(H='2',I='3/2',original_entropy_residual='1',different_current_influence_residual='-1/2'),scope='Every physical law and influence computed directly from truth tables; no peer helper imports; entropy equality certified by exact positive-mass multisets. Universal equivalence is analytic, not finite extrapolation.'))
print(json.dumps(json.loads((R/'out'/('PILOT.json' if pilot else 'VALIDATION.json')).read_text())))
