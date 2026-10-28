"""stage21-v1: independent exact ghost-complete physical reference transport."""
from pathlib import Path
from fractions import Fraction as F
import json,time,sys,hashlib,itertools
from functools import lru_cache
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'out';OUT.mkdir(exist_ok=True)
mode=sys.argv[1] if len(sys.argv)>1 else 'pilot'
def save(n,x):(OUT/n).write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
if mode=='freeze':
 save('FROZEN_SPEC.json',{'helper_version':'stage21-v1','helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'actual_Boolean_family':'ALL256 labelled three-bit Boolean tables; constant-one one/two-bit ghost endpoints','domain':'All6 fixed coordinate orders plus1 adaptive child-order policy;3 original reference decompositions,2 ghost-kernel rules fair/directed. No dimension increase.','case_count':'Primary256*7*3*2=10752 complete physical trees; pilot4*7*3*2=168. All8 leaves of every depth3 tree kept.','symmetry':'None; labelled functions, all outcomes, all original witness labels retained.','arithmetic':'Integer full Walsh, Fraction exact references/coefficient/kernel/likelihood identities; rational envelope products at physical denominator8. No floating sign or numerical log.','memory_estimate_MB':120,'maximum_runtime_seconds':{'pilot':55,'main':180},'scope':'General theorem proved analytically; bounded checks verify formulas, not finite-to-infinite inference.'});print('Frozen stage21-v1: main10752 trees, pilot168; estimate120MB.');raise SystemExit
spec=json.loads((OUT/'FROZEN_SPEC.json').read_text(encoding='utf-8'));assert spec['helper_sha256']==hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
start=time.perf_counter();cap=55 if mode=='pilot' else 180
checks=nodes=trees=ghost_rows=biased=collisions=ghost_children=0
def ck(x):
 global checks
 checks+=1
 if not x:raise AssertionError(checks)
 if checks%1024==0 and time.perf_counter()-start>cap:raise TimeoutError(cap)
def walsh(v):
 a=list(v); k=1
 while k<len(a):
  for i in range(0,len(a),2*k):
   for j in range(i,i+k):a[j],a[j+k]=a[j]+a[j+k],a[j]-a[j+k]
  k*=2
 return [F(x,len(v)) for x in a]
@lru_cache(maxsize=None)
def law(v):return tuple(x*x for x in walsh(v))
def delete(s,j):return (s&((1<<j)-1))|((s>>(j+1))<<j)
def restrict(v,j,t):return tuple(v[(x&((1<<j)-1))|((x>>j)<<(j+1))|(t<<j)] for x in range(len(v)//2))
cache={}
def data(v,j):
 key=(v,j)
 if key not in cache:
  p=law(v);vv=[restrict(v,j,t) for t in (0,1)];pp=[law(z) for z in vv];r=[F(0)]*(len(p)//2)
  for s,x in enumerate(p):r[delete(s,j)]+=x
  cache[key]=(p,vv,pp,tuple(r))
 return cache[key]
def expand(p,b,atoms):
 q=[b*x for x in p]
 for c,s in atoms:q[s]+=c
 return tuple(q)
def visit(v,coords,b,atoms,policy,rule,path=()):
 global nodes,ghost_rows,biased,collisions,ghost_children
 nodes+=1;p=law(v);q=expand(p,b,atoms)
 ck(b>0);ck(b+sum(c for c,s in atoms)==1);ck(sum(p)==sum(q)==1)
 ck(all(q[s]>=b*p[s] for s in range(len(p))))
 if not coords:return [(F(1,2**len(path)),b)]
 order=policy if isinstance(policy,tuple) else (tuple(sorted(coords)) if not path or path[-1]==0 else tuple(sorted(coords,reverse=True)))
 c=next(c for c in order if c in coords);j=coords.index(c)
 p,vv,pp,r=data(v,j);qb=[F(0)]*len(r)
 for s,x in enumerate(q):qb[delete(s,j)]+=x
 ks=[[],[]]
 for u,x in enumerate(r):
  ck((pp[0][u]+pp[1][u])/2==x)
  if x:
   vals=[pp[t][u]/(2*x) for t in (0,1)]
  else:
   vals=[F(1,2),F(1,2)] if rule==0 else [F((u+len(path))%2),F(1-(u+len(path))%2)]
   if qb[u]:ghost_rows+=1
  ck(sum(vals)==1)
  for t in (0,1):ks[t].append(vals[t])
 rt=[sum(qb[u]*ks[t][u] for u in range(len(r))) for t in (0,1)]
 ck(sum(rt)==1);ck(all(x>=b/2 for x in rt))
 if rt[0]!=F(1,2):biased+=1
 out=[]
 for t in (0,1):
  bt=b/(2*rt[t]);at=tuple((w*ks[t][delete(s,j)]/rt[t],delete(s,j)) for w,s in atoms)
  actual=tuple(qb[u]*ks[t][u]/rt[t] for u in range(len(r)))
  ck(expand(pp[t],bt,at)==actual);ck(len(at)==len(atoms));ck(bt+sum(w for w,s in at)==1)
  for u,mass in enumerate(pp[t]):
   if mass:
    ck(actual[u]>0)
    # Exact occupied-atom KL chain ratio, including ACTUAL reference normalizer.
    ck(mass/actual[u]==2*rt[t]*r[u]/qb[u])
  for w,s in at:
   if w and not pp[t][s]:ghost_children+=1
  for w,s in atoms:
   if w and not p[s] and pp[t][delete(s,j)]:collisions+=1
  out+=visit(vv[t],tuple(x for x in coords if x!=c),bt,at,policy,rule,path+(t,))
 return out
truths=range(256) if mode=='main' else (0,1,126,150)
policies=list(itertools.permutations(range(3)))+['adaptive']
for truth in truths:
 v=tuple(1-2*((truth>>x)&1) for x in range(8));p=law(v);occ=[i for i,x in enumerate(p) if x];zeros=[i for i,x in enumerate(p) if not x]
 refs=[(F(3,4),((F(1,4),occ[0]),)),(F(3,4),((F(1,8),0),(F(1,8),7))),(F(1,2),((F(1,4),zeros[0] if zeros else 0),(F(1,4),zeros[-1] if zeros else 7)))]
 for b,atoms in refs:
  for rule in (0,1):
   for policy in policies:
    leaves=visit(v,(0,1,2),b,atoms,policy,rule);ck(len(leaves)==8);ck(sum(w for w,bv in leaves)==1)
    # Exact finite-tree envelope inequality; every original physical reach retained.
    product=F(1)
    for w,bv in leaves:product*=(1/bv)**int(8*w)
    ck(product<=(1/b)**8);trees+=1
# One-bit collision: the original ghost is retained and its full KL is released.
p=(F(1),F(0));q=(F(3,4),F(1,4));ck(sum(q)==1);ck(q[0]<1)
ck((p[0]/q[0])==F(4,3))
endpoint={'function':'constant +1 on one physical bit','root_P':['1','0'],'root_Q':['3/4','1/4'],'both_actual_and_reference_children':['1'],'D_erase_bits':'log2(4/3)','outcome_KL_bits':'0','both_child_KL_bits':'0','exact_certificate':'4>3; source-zero ghost merges with true empty frequency'}
save('GHOST_ENDPOINT.json',endpoint)
result={'helper_version':'stage21-v1','mode':mode,'status':'PASS','Boolean_tables':len(truths),'complete_physical_trees':trees,'visited_nodes':nodes,'assertions':checks,'source_zero_ghost_kernel_rows':ghost_rows,'biased_reference_outcome_nodes':biased,'ghost_to_occupied_transitions':collisions,'retained_child_ghost_occurrences':ghost_children,'runtime_seconds':time.perf_counter()-start,'arithmetic':'integer Walsh and exact Fraction; no floating sign','memory':'estimated120MB; peak unmeasured'}
save('VALIDATION.json' if mode=='main' else 'PILOT.json',result);print(json.dumps(result))
