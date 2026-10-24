import itertools,json,pathlib,networkx as nx
def derangements(neighbors):
 return [dict(zip(neighbors,p)) for p in itertools.permutations(neighbors)
         if all(a!=b for a,b in zip(neighbors,p))]
def walk(plan,e,steps):
 p=[e[0],e[1]]
 for _ in range(steps-1): p.append(plan[p[-1]][p[-2]])
 return p

root=pathlib.Path(__file__).resolve().parent
g=nx.cubical_graph(); e=(0,1); k=3; L=2
count=0; overlap=None; pairs=0
for tup in itertools.product(*(derangements(sorted(g[v])) for v in g)):
 plan=dict(enumerate(tup)); base=walk(plan,e,k)
 if len(set(base))!=k+1: continue
 external=[]
 for i in range(1,k):
  for c in g[base[i]]:
   if c in [base[i-1],base[i+1]]: continue
   mod=dict(plan); mod[base[i]]=next(p for p in derangements(sorted(g[base[i]])) if p[base[i-1]]==c)
   path=walk(mod,e,i+L); segment=path[i:]
   if len(set(path))==len(path) and not set(segment[1:])&set(base):
    external.append((i,c,segment))
   excursion=[base[i]]; current=c; prev=base[i]
   for _ in range(L):
    excursion.append(current)
    if current in base: break
    prev,current=current,plan[current][prev]
   else: continue
   end=excursion[-1]
   if end in [base[0],base[-1]] or len(set(excursion[1:-1]))!=len(excursion)-2: continue
   ell=base.index(end)
   if not 1<=ell<=k-1: continue
   rev=dict(plan)
   for v in excursion[1:-1]: rev[v]={b:a for a,b in plan[v].items()}
   assert walk(rev,e,k)==base
   chosen=excursion[-2]
   assert chosen not in [base[ell-1],base[ell+1]]
   rm=dict(rev); rm[end]=next(p for p in derangements(sorted(g[end])) if p[base[ell-1]]==chosen)
   back=walk(rm,e,ell+len(excursion)-1)[ell:]
   assert back==excursion[::-1]
   assert ell<=i or i<=ell  # Collision belongs to at least one prefix.
   orig_bad=len(set(walk(mod,e,i+L)))!=i+L+1
   reversed_bad=len(set(walk(rm,e,ell+L)))!=ell+L+1
   assert orig_bad or reversed_bad
   restored=dict(rev)
   for v in back[1:-1]: restored[v]={b:a for a,b in rev[v].items()}
   assert restored==plan
   pairs+=1
 for p,q in itertools.combinations(external,2):
  ep=set(zip(p[2],p[2][1:])); eq=set(zip(q[2],q[2][1:]))
  assert not ep&eq
  intersection=set(p[2][1:])&set(q[2][1:])
  if intersection and overlap is None:
   overlap={'graph_edges':list(g.edges()),'plan':plan,'base':base,'L':L,
            'deviations':[p,q],'shared_external_vertices':sorted(intersection)}
 count+=1
# Longer excursions supply non-vacuous checks of the involution itself.
for k,L in [(4,4),(5,3)]:
 for tup in itertools.product(*(derangements(sorted(g[v])) for v in g)):
  plan=dict(enumerate(tup)); base=walk(plan,e,k)
  if len(set(base))!=k+1: continue
  for i in range(1,k):
   for c in g[base[i]]:
    if c in [base[i-1],base[i+1]]: continue
    excursion=[base[i]]; previous,current=base[i],c
    for _ in range(L):
     excursion.append(current)
     if current in base: break
     previous,current=current,plan[current][previous]
    else: continue
    end=excursion[-1]
    if end in [base[0],base[-1]] or len(set(excursion[1:-1]))!=len(excursion)-2: continue
    ell=base.index(end); rev=dict(plan)
    for v in excursion[1:-1]: rev[v]={b:a for a,b in plan[v].items()}
    assert walk(rev,e,k)==base
    chosen=excursion[-2]; assert chosen not in [base[ell-1],base[ell+1]]
    rm=dict(rev); rm[end]=next(p for p in derangements(sorted(g[end])) if p[base[ell-1]]==chosen)
    back=walk(rm,e,ell+len(excursion)-1)[ell:]; assert back==excursion[::-1]
    mod=dict(plan); mod[base[i]]=next(p for p in derangements(sorted(g[base[i]])) if p[base[i-1]]==c)
    orig=walk(mod,e,i+L); other=walk(rm,e,ell+L)
    assert len(set(orig))<len(orig) or len(set(other))<len(other)
    restored=dict(rev)
    for v in back[1:-1]: restored[v]={b:a for a,b in rev[v].items()}
    assert restored==plan
    pairs+=1
out={'simple_cube_plans_k3':count,'reversal_cases':pairs,'vertex_packing_counterexample':overlap}
(root/'reversal_results.json').write_text(json.dumps(out,indent=2),encoding='utf8')
print(json.dumps(out))
