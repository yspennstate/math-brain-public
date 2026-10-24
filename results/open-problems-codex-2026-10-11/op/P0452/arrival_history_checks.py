from itertools import permutations,product,combinations
from pathlib import Path
import json
n=4;edges=list(combinations(range(n),2));states=0;pair_checks=0
for d in product(range(1,n),repeat=n):
 for order in permutations(edges):
  seen=set();count=[0]*n;parent=list(range(n))
  def find(v):
   while parent[v]!=v:parent[v]=parent[parent[v]];v=parent[v]
   return v
  for step in range(len(edges)+1):
   active=[count[i]<d[i] for i in range(n)]
   for i,j in edges:
    if active[i] and active[j] and find(i)!=find(j):assert (i,j) not in seen
    pair_checks+=1
   states+=1
   if step==len(edges):break
   i,j=order[step]
   if active[i] and active[j]:parent[find(i)]=find(j)
   count[i]+=1;count[j]+=1;seen.add((i,j))
Path('arrival_history_checks.json').write_text(json.dumps({'n':n,'all_positive_budget_vectors':81,'all_edge_orders':720,'prefix_states':states,'pair_checks':pair_checks,'passed':True},indent=2))
print(states,pair_checks,'arrival-history checks passed')
