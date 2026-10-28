from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
from itertools import combinations
import time,json
R=Path(__file__).resolve().parents[1];started=time.perf_counter();checks=0
def ck(x):
 global checks
 checks+=1
 assert x,checks
def walsh(f):
 a=list(f);d=1
 while d<len(a):
  for j in range(0,len(a),2*d):
   for k in range(j,j+d):
    u,v=a[k],a[k+d];a[k],a[k+d]=u+v,u-v
  d*=2
 return a
@lru_cache(None)
def influences(f):
 n=(len(f)-1).bit_length()
 return tuple(Q(sum(f[x]!=f[x^(1<<j)] for x in range(len(f))),len(f)) for j in range(n))
@lru_cache(None)
def certified(f,K=1):
 N=len(f);n=(N-1).bit_length();w=walsh(f)
 A=N*N*(2*n-K*sum(influences(f)));ck(A.denominator==1);A=int(A)
 right=1
 for v in w:
  if v:right*=pow(v*v,v*v)
 return pow(2,A)<=right if A>=0 else True
def child(f,j,b):return tuple(v for x,v in enumerate(f) if (x>>j)&1==b)
@lru_cache(None)
def hereditary(f,K=1):
 if not certified(f,K):return False
 n=(len(f)-1).bit_length()
 return all(hereditary(child(f,j,b),K) for j in range(n) for b in (0,1))
def trees(coords,depth):
 yield None
 if depth:
  for i in coords:
   sub=list(trees(tuple(j for j in coords if j!=i),depth-1))
   for a in sub:
    for b in sub:yield(i,a,b)
policies=list(trees(tuple(range(4)),2));ck(len(policies)==65)
seed=tuple((-1 if x&3==0 else 1)*(-1 if x>>2==0 else 1) for x in range(16))
stats=dict(roots=0,policies=65,tree_cases=0,eligible=0,noneligible=0,adaptive_eligible=0)
boundary_hit=False
for r in (0,1,2):
 for edits in combinations(range(16),r):
  E=set(edits);G=tuple(-v if x in E else v for x,v in enumerate(seed));delta=Q(r,16);stats['roots']+=1
  for tree in policies:
   p=[Q(0),Q(0)];e=[Q(0),Q(0)];q=[Q(0),Q(0)];spent=Q(0);eligible=True;touchleaves=[Q(0),Q(0)]
   def walk(node,points,touched,depth):
    global spent,eligible
    reach=Q(len(points),16)
    if node is None:
     row=tuple(G[x] for x in points);eligible=eligible and hereditary(row)
     for j in range(2):
      if j not in touched:touchleaves[j]+=reach
     return
    i,lo,hi=node;j=i//2
    inf=Q(sum(G[x]!=G[x^(1<<i)] for x in points),len(points));spent+=reach*inf
    if j not in touched:
     p[j]+=reach;e[j]+=Q(sum(x in E for x in points),16);q[j]+=reach*inf
    walk(lo,[x for x in points if not (x>>i)&1],touched|{j},depth+1)
    walk(hi,[x for x in points if (x>>i)&1],touched|{j},depth+1)
   walk(tree,list(range(16)),set(),0)
   stats['tree_cases']+=1;stats['eligible' if eligible else 'noneligible']+=1
   for j in range(2):
    ck(p[j]+touchleaves[j]==1);ck(0<=e[j]<=delta)
    ck(q[j]>=Q(1,2)*p[j]-2*e[j])
    if eligible:
     ck(delta-e[j]>=Q(1,4)*(1-p[j]));ck(q[j]>=Q(1,2)-2*delta)
   ck(spent>=sum(q))
   if eligible:
    ck(spent>=1-4*delta);ck(sum(p)>=2*(1-4*delta))
    if tree and tree[1]!=tree[2]:stats['adaptive_eligible']+=1
    if r==0 and spent==1:boundary_hit=True
ck(boundary_hit);ck(stats['eligible']>0);ck(stats['noneligible']>0);ck(stats['adaptive_eligible']>0)
# Exact hypothesis and repair-radius guards, including all repair points.
h=(-1,1,1,1);ck(not certified(h));ck(influences(h)==(Q(1,2),Q(1,2)))
for x in range(4):
 g=tuple(-v if a==x else v for a,v in enumerate(h));ck(hereditary(g))
guard=tuple(h[x&3]*(-1 if x>>2 else 1) for x in range(8))
ck(certified(guard));ck(not hereditary(guard));ck(child(guard,2,0)==h)
stats.update(status='PASS',checks=checks,wall_seconds=time.perf_counter()-started,
 missing_heredity_guard='z*h2 is FEI1 certified with debit0 but untouched violating descendant h2',
 boundary='unedited two-copy first-bit-per-factor tree attains spent1',
 proof_scope='author analytic proof; exact finite certificate only, no universal FEI claim')
(R/'out/CHECKS.json').write_text(json.dumps(stats,indent=2)+'\n',encoding='utf-8')
print(json.dumps(stats))
