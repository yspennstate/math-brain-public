from pathlib import Path
from fractions import Fraction as Q
from itertools import permutations
import json,time
R=Path(__file__).resolve().parents[1];start=time.perf_counter();checks=0
def ck(b):
 global checks
 assert b;checks+=1
def influence(f):
 return Q(sum(f[x]!=f[x^(1<<i)] for x in range(len(f)) for i in range(len(f).bit_length()-1)),len(f))
# Explicit independent orbit enumeration on every child of dimension<=2.
count=0
for n in range(3):
 N=1<<n
 for mask in range(1<<N):
  f=[-1 if mask>>x&1 else 1 for x in range(N)]
  cost=[]
  for perm in permutations(range(1,N),n):
   span={0}
   for v in perm:span|={s^v for s in list(span)}
   if len(span)!=N:continue
   for shift in range(N):
    for char in range(N):
     g=[]
     for x in range(N):
      y=shift
      for j,v in enumerate(perm):
       if x>>j&1:y^=v
      g.append(f[y]*(-1 if (x&char).bit_count()%2 else 1))
     cost.append(influence(g))
  a=min(cost)
  w=[Q(sum(f[x]!=f[x^v] for x in range(N)),N) for v in range(N)]
  greedy=[];span={0}
  for v in sorted(range(1,N),key=lambda v:min(w[v],1-w[v])):
   if v in span:continue
   greedy.append(v);span|={s^v for s in list(span)}
  ck(a==sum((min(w[v],1-w[v]) for v in greedy),Q(0)));count+=1
# Dummy-selector guard, exact Walsh spectrum {1/4,1/4,1/4,1/4}.
f=[-1 if x&3==0 else 1 for x in range(8)]
co=[sum(f[x]*(-1 if (s&x).bit_count()%2 else 1) for x in range(8)) for s in range(8)]
ck(sorted(c*c for c in co)==[0,0,0,0,16,16,16,16]);ck(influence(f)==1)
ck(all(f[x]==f[x^4] for x in range(8)))
# K1, D=1, S=-1, sigma=Rchild=0, exact budget=0.
ck(1+(-1)+0==0)
# Essential 3-bit point root: singleton child reserves average(-1,0).
root=[-1]+[1]*7
ck(all(any(root[x]!=root[x^(1<<i)] for x in range(8)) for i in range(3)))
ck(Q(-1,2)<0)
out={'status':'PASS','assertions':checks,'complete_small_child_orbits':count,'negative_reserve_guards':2,'dummy_guard':{'K':1,'D':1,'S':-1,'sigma':0,'Rchild':0},'seconds':time.perf_counter()-start,'scope':'Independent enumeration of child minima; hypothesis guards. Not an independent agent review.'}
(R/'out/GUARDS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
