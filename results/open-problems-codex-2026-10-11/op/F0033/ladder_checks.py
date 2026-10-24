"""Exact finite checks of the second-attempt construction, not nu samples."""
import collections, fractions, json, pathlib
from finite_checks import graph,recurrent
P,Q=6,16
def height(x,y):
 if y%Q==0 and (x%2==1 or x%P==0):return 3
 if y%Q==Q-1 and x%2==0:return 3
 return 2
def bootstrap(vs,adj,o,h):
 if h[o]<3:return set(),[]
 active={o};layers=[[o]]
 while True:
  new=[i for i in range(len(vs)) if i not in active and h[i]+sum(j in active for j in adj[i])>=4]
  if not new:return active,layers
  active.update(new);layers.append(new)
def check():
 C={(0,0):4,(-1,0):1,(1,0):1,(0,-1):1}
 neigh=lambda x:[(x[0]-1,x[1]),(x[0]+1,x[1]),(x[0],x[1]-1),(x[0],x[1]+1)]
 region=set(C)
 for x in C:region.update(neigh(x))
 fractional=[];ceil_fail=[]
 for x in sorted(region):
  dw=4*C.get(x,0)-sum(C.get(y,0) for y in neigh(x))
  rhs=13*(int(x==(0,0))-(3-height(*x)))
  assert dw>=rhs
  fractional.append({'x':x,'Delta_w':dw,'required':rhs})
  dc=4*int(x in C)-sum(y in C for y in neigh(x))
  if height(*x)+int(x==(0,0))-dc>3:ceil_fail.append(x)
 results=[]
 for r in [2,3,5,8,12,20,32]:
  vs,adj,o=graph(r);h=[height(*x) for x in vs];assert recurrent(h,adj)
  active,layers=bootstrap(vs,adj,o,h)
  expected={i for i,x in enumerate(vs) if x[1] in [-1,0]}
  assert active==expected
  assert any(abs(vs[i][0])==r for i in active)
  results.append({'r':r,'first_wave_size':len(active),'layer_count':len(layers),'recurrent':True})
 # Full residue classification, inspect a box around each translated origin.
 counts=collections.Counter()
 vs,adj,o=graph(8)
 for a in range(P):
  for b in range(Q):
   h=[height(x+a,y+b) for x,y in vs]
   active,layers=bootstrap(vs,adj,o,h)
   if not active:kind='no_toppling'
   elif len(active)==1:kind='one_toppling'
   else:
    assert any(abs(vs[i][0])==8 for i in active)
    kind='unbounded_ladder_class'
   counts[kind]+=1
 assert counts=={'no_toppling':89,'one_toppling':3,'unbounded_ladder_class':4}
 safe_sites={(0,0),(2,0),(4,0),(0,2),(2,2),(4,2),(0,4)}
 safe_counts=collections.Counter()
 for a in range(P):
  for b in range(Q):
   h=[3 if ((x+a)%P,(y+b)%Q) in safe_sites else 2 for x,y in vs]
   active,layers=bootstrap(vs,adj,o,h)
   assert len(active)<=1
   safe_counts['one_toppling' if active else 'no_toppling']+=1
 assert safe_counts=={'no_toppling':89,'one_toppling':7}
 # Components of the saturated periodic pattern: seed stars (4) or singletons.
 saturated={(x,y) for x in range(-24,25) for y in range(-16,17) if height(x,y)==3}
 components=[]
 while saturated:
  seed=next(iter(saturated));comp={seed};todo=[seed];saturated.remove(seed)
  while todo:
   for y in neigh(todo.pop()):
    if y in saturated:saturated.remove(y);comp.add(y);todo.append(y)
  if all(-24<x<24 and -16<y<16 for x,y in comp):components.append(len(comp))
 assert set(components)<={1,4}
 out={'p':P,'q':Q,'mean_height':str(fractions.Fraction(199,96)),
      'infinite_total_probability_for_periodic_shift_law':str(fractions.Fraction(1,24)),
      'phase_counts':dict(counts),'finite_box_tests':results,'scaled_fractional_barrier':fractional,
      'safe_pattern_phase_counts':dict(safe_counts),
      'ceiling_barrier_failure_sites':ceil_fail,'interior_saturated_component_sizes':sorted(set(components))}
 pathlib.Path('ladder_results.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
if __name__=='__main__':check()
