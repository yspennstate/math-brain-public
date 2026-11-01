import pathlib,json,itertools,heapq
n=5;edges=list(itertools.combinations(range(n),2));ei={e:i for i,e in enumerate(edges)};masks=set()
for seq in itertools.product(range(n),repeat=n-2):
 deg=[1]*n
 for v in seq:deg[v]+=1
 if max(deg)>3:continue
 work=deg.copy();leaves=[v for v in range(n) if work[v]==1];heapq.heapify(leaves);es=[]
 for v in seq:
  u=heapq.heappop(leaves);es.append(tuple(sorted((u,v))));work[u]-=1;work[v]-=1
  if work[v]==1:heapq.heappush(leaves,v)
 es.append(tuple(sorted(leaves)));masks.add(sum(1<<ei[e] for e in es))
assert len(masks)==120
# Independently test every host using all labeled bounded-degree trees.
counts=[0]*11
for g in range(1024):
 present={t for t in masks if (g&t)==t}
 # A path has degree list 1,1,2,2,2. The other type has 1,1,1,2,3.
 types=set()
 for t in present:
  d=[0]*n
  for i,(u,v) in enumerate(edges):
   if t>>i&1:d[u]+=1;d[v]+=1
  types.add(tuple(sorted(d)))
 if len(types)==2:counts[g.bit_count()]+=1
p=pathlib.Path('experiment_results.json');a=json.loads(p.read_text(encoding='utf8'));assert counts==a['exact_n5']['universal3_by_edges'];a['independent_prufer_check']={'labeled_subcubic_trees':len(masks),'universal3_counts':counts,'agrees':True};p.write_text(json.dumps(a,indent=2),encoding='utf8');print('Independent Prüfer-code check passed.')
