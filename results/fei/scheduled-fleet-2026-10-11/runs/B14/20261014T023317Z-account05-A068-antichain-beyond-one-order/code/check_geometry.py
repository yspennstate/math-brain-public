import itertools,json
from pathlib import Path
from time import perf_counter
start=perf_counter()
def g(u):
 x=[(-1)**(u>>i&1) for i in range(3)]
 return 1 if x[0]+x[0]*x[1]+x[2]>0 else -1
values=[g(u) for u in range(8)]
rows=[]
for order in itertools.permutations(range(3)):
 for orientation in range(8):
  failure=None
  for rank,j in enumerate(order):
   prefix=order[:rank]; exterior=order[rank+1:]
   for e in range(1<<len(exterior)):
    u=sum(((e>>i)&1)<<c for i,c in enumerate(exterior))
    pivotal=[]
    for a in range(1<<len(prefix)):
     v=u|sum(((a>>i)&1)<<c for i,c in enumerate(prefix))
     if g(v)!=g(v^(1<<j)):
      oriented=a^sum(((orientation>>c)&1)<<i for i,c in enumerate(prefix))
      pivotal.append((a,oriented))
    for (a,s),(b,t) in itertools.combinations(pivotal,2):
     if s&t in (s,t):
      failure=dict(pivot=j,prefix=list(prefix),exterior=list(exterior),exterior_assignment=e,pivotal_pair=[a,b])
      break
    if failure:break
   if failure:break
  assert failure is not None
  rows.append(dict(order=list(order),orientation=orientation,failure=failure))
# Exact opposite derivative signs of coordinate1 (the second coordinate).
assert (g(4)-g(6))//2==1 # x1+, x3-
assert (g(1)-g(3))//2==-1 # x1-, x3+
out=dict(status='PASS',orders_and_orientations=48,nonunate_coordinate=1,truth_table=values,all_fixed_one_order_antichain_geometries_fail=True,certificates=rows,exact_assertions=50,runtime_seconds=perf_counter()-start)
p=Path(__file__).resolve().parents[1]/'out/geometry.json'
p.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='certificates'}))

