"""Exact bounded graph checks; no Monte Carlo and no large plan enumeration."""
import itertools, collections, fractions, json, math, time, pathlib
import networkx as nx
F=fractions.Fraction
root=pathlib.Path(__file__).resolve().parent
deadline=time.monotonic()+150
def derangements(neighbors):
 return [dict(zip(neighbors,p)) for p in itertools.permutations(neighbors)
         if all(a!=b for a,b in zip(neighbors,p))]
def walk(plan,e,steps):
 p=[e[0],e[1]]
 for _ in range(steps-1): p.append(plan[p[-1]][p[-2]])
 return p
def nbw_prob(g,e,k):
 states={(e[0],e[1],(1<<e[0])|(1<<e[1])):F(1)}
 for _ in range(k-1):
  nxt=collections.defaultdict(F)
  for (u,v,mask),mass in states.items():
   for w in g[v]:
    if w!=u and not (mask>>w)&1:
     nxt[v,w,mask|(1<<w)]+=mass/F(g.degree(v)-1)
  states=nxt
 return sum(states.values(),F(0))
local=[]
for d in range(3,8):
 ds=derangements(list(range(d)))
 fibers=[sum(p[0]==c for p in ds) for c in range(1,d)]
 assert len(set(fibers))==1 and len(ds)==(d-1)*fibers[0]
 local.append({'degree':d,'derangements':len(ds),'fiber_counts':fibers})
print('local',local,flush=True)
results=[]; vertex_overlap_example=None
graphs=[g for g in nx.graph_atlas_g() if 4<=len(g)<=6 and min(dict(g.degree()).values())>=3 and nx.is_connected(g)]
for g in graphs:
 choices=[derangements(sorted(g[v])) for v in g]
 size=math.prod(map(len,choices))
 if size>60000 or time.monotonic()>deadline: continue
 # Fix one edge; all k=2,...,n-1 are checked for this prescribed edge.
 e=tuple(sorted(g.edges())[0]); n=len(g)
 counts=collections.Counter(); deviations=collections.Counter(); weights=collections.defaultdict(F)
 for tup in itertools.product(*choices):
  plan=dict(enumerate(tup))
  for k in range(2,n):
   base=walk(plan,e,k)
   if len(set(base))!=k+1: continue
   counts[k]+=1
   for L in [1,2]:
    W=sum(g.degree(base[i])-2 for i in range(1,k))
    deviations[k,L,'W']+=W
    for i in range(1,k):
     u,v,b=base[i-1:i+2]
     for c in g[v]:
      if c in [u,b]: continue
      modified=dict(plan); modified[v]=next(p for p in choices[v] if p[u]==c)
      path=walk(modified,e,i+L)
      if len(set(path))==len(path): continue
      deviations[k,L,'bad']+=1
      if i>k-L: continue
      fiber=[p for p in choices[v] if p[u]==c]
      for p in fiber:
       target=dict(plan); target[v]=p
       key=tuple(tuple(target[x][y] for y in sorted(g[x])) for x in g)
       weights[k,L,key]+=F(1,len(fiber))
 for k in range(2,n):
  p=nbw_prob(g,e,k)
  assert F(counts[k],size)==p
  for L in [1,2]:
   # Global bad bound valid without imposing the theorem's large-k conditions.
   assert deviations[k,L,'bad'] >= F(deviations[k,L,'W'],2)-counts[k]*(F(2*g.number_of_edges(),L)+max(dict(g.degree()).values())-1)
   incoming=[w for (kk,ll,key),w in weights.items() if kk==k and ll==L]
   assert all(w<=(L+1)*(max(dict(g.degree()).values())-2) for w in incoming)
 results.append({'n':n,'edges':list(g.edges()),'plans':size,'start':e,
                 'simple_probabilities':{str(k):str(nbw_prob(g,e,k)) for k in range(2,n)},
                 'checked':'plan/NBW equality; global bad-count lower bound; conditional heat-bath incoming bound'})
 print('graph',len(results),'n',n,'plans',size,flush=True)
out={'local_derangement_checks':local,'graph_checks':results,'runtime_seconds':time.monotonic()-(deadline-150)}
(root/'finite_results.json').write_text(json.dumps(out,indent=2),encoding='utf8')
print('PASS',len(results),'graphs',flush=True)
