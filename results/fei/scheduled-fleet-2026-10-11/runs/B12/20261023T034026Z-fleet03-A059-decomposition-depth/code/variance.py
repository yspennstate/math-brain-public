from pathlib import Path
from fractions import Fraction as Q
import json,time,itertools,sys
import exact as E
R=Path(__file__).resolve().parents[1];start=time.perf_counter();pilot='--pilot' in sys.argv
sources=queries=trees=fronts=0
for code in range(8 if pilot else 256):
 g=tuple(1 if (code>>j)&1 else -1 for j in range(8));ga=E.walsh(g);mu=ga[0];var=1-mu*mu
 for perm in itertools.permutations(range(3)):
  trees+=1;states=[(g,Q(1),Q(0),list(range(3)))]
  for depth in range(4):
   fronts+=1
   E.ok(sum(w*(1-E.walsh(tab)[0]**2+spent) for tab,w,spent,ids in states)==var,'all-front SAME variance')
   if depth==3:break
   ns=[]
   for tab,w,spent,ids in states:
    idx=ids.index(perm[depth]);aa=E.walsh(tab);beta=aa[1<<idx]
    children=[E.slice_table(tab,idx,b) for b in [0,1]]
    E.ok(1-aa[0]**2-sum(1-E.walsh(h)[0]**2 for h in children)/2==beta*beta,'exact local variance')
    for h in children:ns.append((h,w/2,spent+beta*beta,ids[:idx]+ids[idx+1:]))
   states=ns
 for m in ([4] if pilot else [4,6]):
  c=Q(1,1<<m);sqrtc=Q(1,1<<(m//2));a=(1+c)/2
  bent=tuple((-1)**sum(((x>>(2*j))&1)*((x>>(2*j+1))&1) for j in range(m//2)) for x in range(1<<m))
  rare=tuple(bent[x]-int(x==0)+int(x==0)*g[y] for y in range(8) for x in range(1<<m))
  frequent=tuple(g[y] for y in range(8) for x in range(1<<m))
  full=tuple(v for l,r in zip(frequent,rare) for v in [l,r]);wa=E.walsh(full);ra=E.walsh(rare)
  d=E.influence(wa,0);D=E.add(E.entropy(wa),E.add(E.entropy(E.walsh(frequent)),E.entropy(ra)),-Q(1,2))
  E.ok(d==(1-c-mu*(sqrtc-c))/2,'nonflat actual source influence');E.ok(d>=Q(3,8))
  E.le(D,{2:2},'full source drop <=2');E.le({},D,'source drop nonnegative')
  E.le(E.add(D,{2:Q(m)*c*var/2}),{2:Q(17,3)*d},'source6 SAME bank incl entire variance allocation')
  E.ok(Q(m)*c/2<=Q(1,8));sources+=1
  if m==4:
   for i in range(3):
    bg={}
    for s,aa in enumerate(ga):
     if not ((s>>i)&1):bg=E.add(bg,E.phi(aa*aa,ga[s|(1<<i)]**2))
    DH=E.add(E.entropy(ra),E.add(E.entropy(E.walsh(E.slice_table(rare,m+i,0))),E.entropy(E.walsh(E.slice_table(rare,m+i,1)))),-Q(1,2))
    beta=ga[1<<i];inf=E.influence(ga,i)
    E.ok(abs(beta)<=inf,'BOOLEAN singleton L1 <= influence')
    target=E.add(E.add({},bg,c),{2:c*(m*beta*beta+7*inf)})
    E.le(DH,target,'arbitrary Boolean general transfer constant7')
    queries+=1
 E.walsh.cache_clear();E.cost_cached.cache_clear();E.bounds_cached.cache_clear()
 if time.perf_counter()-start>(55 if pilot else 175):raise RuntimeError('frozen cap')
for m in range(4,25,2):
 E.ok(Q(m,2**m)<=Q(1,4));E.ok(Q(m+1,2*m)<=1,'all-integer monotone ratio')
out=dict(status='PASS',source_cases=sources,general_queries=queries,variance_trees=trees,frontiers=fronts,assertions=E.checks,seconds=time.perf_counter()-start,pilot=pilot)
(R/'out'/('variance_pilot.json' if pilot else 'variance_validation.json')).write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
