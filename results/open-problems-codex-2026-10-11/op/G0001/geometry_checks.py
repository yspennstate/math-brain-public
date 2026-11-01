from pathlib import Path
from collections import deque
from itertools import product
import json,time
start=time.time()
def check(K,d):
 steps=[tuple((1 if sign else -1) if i==j else 0 for i in range(d)) for j in range(d) for sign in [0,1]]
 stars=[v for v in product([-1,0,1],repeat=d) if any(v)]
 def add(x,v):return tuple(a+b for a,b in zip(x,v))
 lo=tuple(min(x[i] for x in K)-1 for i in range(d));hi=tuple(max(x[i] for x in K)+1 for i in range(d))
 box=set(product(*(range(lo[i],hi[i]+1) for i in range(d))))
 U={lo};todo=deque(U)
 while todo:
  x=todo.popleft()
  for v in steps:
   y=add(x,v)
   if y in box and y not in K and y not in U:U.add(y);todo.append(y)
 H=box-U;B={add(x,v) for x in H for v in steps if add(x,v) in U}
 assert B
 seen={next(iter(B))};todo=deque(seen)
 while todo:
  x=todo.popleft()
  for v in stars:
   y=add(x,v)
   if y in B and y not in seen:seen.add(y);todo.append(y)
 assert seen==B,('star disconnected',K)
 m=len(B);assert m**d>=len(H)**(d-1),('surface',K)
 t=1
 while (t,)+(0,)*(d-1) in H:t+=1
 assert t<=m and (t,)+(0,)*(d-1) in B
 E={tuple(sorted((x,add(x,v)))) for x in H for v in steps if add(x,v) in U}
 links={e:set() for e in E}
 # Every cut edge belongs to 2(d-1) elementary squares.
 for e in E:
  x,y=e;ax=next(i for i in range(d) if x[i]!=y[i])
  for v in steps:
   if v[ax]:continue
   xv,yv=add(x,v),add(y,v)
   es={tuple(sorted(pair)) for pair in [(x,y),(x,xv),(y,yv),(xv,yv)]}
   cut=es&E;assert len(cut)%2==0
   for f in cut:links[e].add(f)
 seen={next(iter(E))};todo=deque(seen)
 while todo:
  for f in links[todo.popleft()]:
   if f not in seen:seen.add(f);todo.append(f)
 assert seen==E,('square disconnected',K)
 return m
out={'date':'2026-10-11','scope':'Finite geometry falsification checks; not a proof of critical extinction','enumeration':[],'special_shapes':[]}
for d,maxn in [(2,7),(3,5)]:
 steps=[tuple(s if i==j else 0 for i in range(d)) for j in range(d) for s in [-1,1]]
 shapes={frozenset({(0,)*d})}
 for n in range(1,maxn+1):
  for K in shapes:check(K,d)
  out['enumeration'].append({'dimension':d,'size':n,'rooted_sets_checked':len(shapes)})
  if n<maxn:
   new=set()
   for K in shapes:
    for x in K:
     for v in steps:
      y=tuple(a+b for a,b in zip(x,v))
      if y not in K:new.add(K|{y})
   shapes=new
for d in [2,3,4]:
 for r in [1,2]:
  cube=set(product(range(-r,r+1),repeat=d))
  for name,K in [('cube',cube),('hollow_cube',{x for x in cube if max(map(abs,x))==r}),('punctured_cube',cube-{(1,)+(0,)*(d-1)})]:
   # All these contain origin except hollow: translate a shell vertex to origin.
   anchor=next(iter(K));K={tuple(x[i]-anchor[i] for i in range(d)) for x in K}
   m=check(K,d);out['special_shapes'].append({'dimension':d,'r':r,'shape':name,'size':len(K),'boundary_size':m})
 # thin set with many possible translations of its boundary
 K={(i,)+(0,)*(d-1) for i in range(30)}
 m=check(K,d);out['special_shapes'].append({'dimension':d,'shape':'line','size':len(K),'boundary_size':m})
out['elapsed_seconds']=time.time()-start;out['result']='PASS'
Path('geometry_checks.json').write_text(json.dumps(out,indent=2),encoding='utf8');print(json.dumps(out,indent=2))
