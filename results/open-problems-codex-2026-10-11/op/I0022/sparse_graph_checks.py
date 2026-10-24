"""Independent small-tree enumeration and target graph sampling checks."""
from functools import lru_cache
from collections import deque
from itertools import product
from math import comb
import pathlib,json,time
ROOT=pathlib.Path(__file__).parent
start=time.monotonic()

@lru_cache(None)
def trees(n):
 if n==1: return ((),)
 out=[]
 def forests(left):
  if left==0:
   yield ()
  else:
   for m in range(1,left+1):
    for t in trees(m):
     for rest in forests(left-m): yield (t,)+rest
 out.extend(forests(n-1))
 return tuple(out)

def energy(t):
 d=len(t)
 if d in (0,1): e=0
 elif d in (3,9): e=d**3
 else: return None
 for child in t:
  c=energy(child)
  if c is None:return None
  e+=c
 return e

tree_rows=[]
for n,k,q in [(4,3,1),(7,3,2),(10,9,1)]:
 alltrees=trees(n)
 assert len(alltrees)==comb(2*(n-1),n-1)//n
 partition=0;target=0
 for t in alltrees:
  e=energy(t)
  if e is not None:
   partition+=1<<e
   if e==q*k**3: target+=1
 assert target==(1 if q==1 else k)
 # Compare with the separately implemented allocation polynomial algorithm.
 from sparse_exact_checks import partition as allocation_partition
 assert partition==allocation_partition(n)
 tree_rows.append({'n':n,'ordered_trees_enumerated':len(alltrees),
                   'target_trees':target,'partition_bits':partition.bit_length()})

graph_rows=[]
for k in [3,9,27]:
 n=2*k+1;A=k-1;B=k
 adj=[[] for _ in range(n)]
 def edge(x,y):adj[x].append(y);adj[y].append(x)
 edge(0,1)
 for x in range(2,k+1):edge(0,x)
 for x in range(k+1,n):edge(1,x)
 assert len(adj[0])==k and len(adj[1])==k+1
 # The second hub has outdegree k and undirected degree k+1.
 dist=[]
 for u in range(n):
  row=[-1]*n;row[u]=0;todo=deque([u])
  while todo:
   v=todo.popleft()
   for w in adj[v]:
    if row[w]<0:row[w]=row[v]+1;todo.append(w)
  dist.append(row)
 counts={d:sum(row.count(d) for row in dist) for d in range(4)}
 assert counts[0]==n
 assert counts[1]==2*(n-1)
 assert counts[2]==2*k*k
 assert counts[3]==2*k*(k-1)
 mixed=0
 for u,v,w in product(range(2,n),repeat=3):
  if len({u,v,w})<3:continue
  labels=[x>=k+1 for x in (u,v,w)]
  if not (all(labels) or not any(labels)):
   assert sorted([dist[u][v],dist[u][w],dist[v][w]])==[2,3,3]
   mixed+=1
 assert mixed==3*A*B*(A+B-2)
 graph_rows.append({'k':k,'pair_counts':counts,'mixed_ordered_distinct_leaf_triples':mixed,
                    'mixed_probability':mixed/n**3})

results={'tree_enumeration':tree_rows,'graph_checks':graph_rows,
         'elapsed_seconds':round(time.monotonic()-start,3)}
(ROOT/'sparse_graph_checks.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
print(json.dumps(results,indent=2))
