import itertools,json,time
from pathlib import Path
import numpy as np

def comps(n,edges):
 p=list(range(n));sz=[1]*n
 def find(x):
  while p[x]!=x:p[x]=p[p[x]];x=p[x]
  return x
 for a,b in edges:
  a,b=find(a),find(b)
  if a!=b:p[b]=a;sz[a]+=sz[b]
 return [sz[i] for i in range(n) if find(i)==i]
def mass(n,edges,k):return sum(s for s in comps(n,edges) if s>=k)
# Exhaust every simple graph on five vertices and every one-edge change.
n=5;es=list(itertools.combinations(range(n),2)); count=0
for mask in range(1<<len(es)):
 ed={e for j,e in enumerate(es) if mask>>j&1}
 for e in es:
  other=ed^{e}
  for k in range(1,n+2):
   assert abs(mass(n,ed,k)-mass(n,other,k))<=2*(k-1)
   count+=1
# Exhaust all weight orders and all budgets for n=4. Move one edge to every rank.
n=4;es=list(itertools.combinations(range(n),2));bc=0

def graph(order,d):
 chosen=[set() for _ in range(n)]
 for i in range(n):chosen[i]=set(e for e in order if i in e)
 # Set order must be respected, not the auxiliary sets above.
 chosen=[set([e for e in order if i in e][:d[i]]) for i in range(n)]
 return {e for e in es if e in chosen[e[0]] and e in chosen[e[1]]}
for order in itertools.permutations(es):
 for d in itertools.product(range(1,n),repeat=n):
  g=graph(order,d)
  for e in es:
   rem=[x for x in order if x!=e]
   for pos in range(len(es)):
    new=rem[:pos]+[e]+rem[pos:];h=graph(new,d)
    assert len(g^h)<=4
    for k in [2,3,4]:assert abs(mass(n,g,k)-mass(n,h,k))<=8*(k-1)
    bc+=1
print('finite checks',count,bc,flush=True)
Path('finite_checks.json').write_text(json.dumps({'single_edge_cases':count,'rank_move_cases':bc,'passed':True},indent=2))
