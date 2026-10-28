from joint import *
import joint as engine
start=time.perf_counter();dag=graph();raw=json.loads((ROOT/'out/JOINT_CASES.json').read_text(encoding='utf-8'))
source=ROOT.parents[3]/'agents/A072/runs/20261023T015130Z-account03-A072-exact-walsh-engine'
saved=json.loads((source/'out/HULL_CASES.json').read_text(encoding='utf-8'))
def unpack(p):return {int(k):F(v) for k,v in p.items()}
def source_profile(p):
 out={}
 for k,v in p.items():out=add(out,{2:F(v)} if k=='constant' else mul(lp(F(k)),F(v)))
 return out
source_orbits={o['core_orbit']:{tuple(z['truth']):z for z in o['states']} for o in saved['orbits']}
def axes_reduce(t,axes):
 axes=list(axes)
 while True:
  drop=next((i for i in range(len(axes)) if all(t[x]==t[x^(1<<i)] for x in range(len(t)))),None)
  if drop is None:return t,axes
  ck(child(t,drop,0)==child(t,drop,1));t=child(t,drop,0);axes.pop(drop)
all_results=[];cuts=[];source_checked=set()
for pairdata in raw:
 pair=pairdata['pair_original'];nodes={tuple(tuple(t) for t in row['truths']):dict(S=unpack(row['S']),R=unpack(row['R'])) for row in pairdata['states_certificate']}
 for side in [0,1]:
  def key(t):return (t,G) if side==0 else (G,t)
  @lru_cache(None)
  def single(t):
   node=nodes[key(t)];R=pos(neg(node['S']))
   for i,kids in dag[t]:
    r=mean([single(c) for c in kids])
    if cmp(r,R)>0:R=r
   return R
  single(G)
  typ=2 if pair[side] in [2,4] else 3
  for t in dag:
   src=source_orbits[typ][t]
   ck(single(t)==source_profile(src['exact_R']))
   ck(nodes[key(t)]['S']==source_profile(src['exact_S']))
   source_checked.add((typ,t))
  A0=neg(nodes[(G,G)]['S']);ck(single(G)==A0)
  incoming={G:A0};paths={G:[]};axes={G:list(range(6))}
  for t in sorted(dag,key=len,reverse=True):
   a=incoming[t];ck(cmp(a,single(t))>=0)
   for i,kids in dag[t]:
    avgR=mean([single(c) for c in kids]);ac=[add(single(c),minus(a,avgR)) for c in kids]
    ck(mean(ac)==a)
    for b,c in enumerate(kids):
     actual,ca=axes_reduce(child(t,i,b),[x for k,x in enumerate(axes[t]) if k!=i]);ck(actual==c)
     if c not in incoming or cmp(ac[b],incoming[c])<0:
      incoming[c]=ac[b];paths[c]=paths[t]+[(axes[t][i],b)];axes[c]=ca
  B={};witness=None
  for t in dag:
   required=nodes[key(t)]['R'];gap=minus(required,incoming[t]);positive=pos(gap)
   if cmp(positive,B)>0:B=positive;witness=t
   cuts.append(dict(pair=pair,first_core=pair[side],truth=list(t),source_incoming_credit=pack(incoming[t]),joint_required_credit=pack(required),shortfall=pack(gap),prefix_original_coordinates=paths[t],conditional_reach=str(F(1,1<<len(paths[t])))))
  result=dict(pair=pair,first_core=pair[side],extra_initial_old_debit_threshold=pack(B),threshold_interval=ev(B),verdict='ALL_ACTUAL_PREFIXES_SAME_CREDIT' if not B else 'SHARP_OLD_DEBIT_THRESHOLD_REQUIRED',cut_count=len(dag))
  if witness is not None:result['witness']=cuts[-len(dag)+list(dag).index(witness)]
  all_results.append(result)
  save('PREFIX_CUTS.json',cuts);save('PREFIX_RESULTS.json',all_results)
  ck(time.perf_counter()-start<55)
ck(len(cuts)==72 and len(source_checked)==24)
globalB={}
for z in all_results:
 B=unpack(z['extra_initial_old_debit_threshold'])
 if cmp(B,globalB)>0:globalB=B
result=dict(version='A084-inherited-prefix-v1',cuts=len(cuts),source_profiles_independently_matched=len(source_checked),exact_assertions=engine.CHECKS,results=all_results,global_old_debit_threshold=pack(globalB),global_threshold_interval=ev(globalB),runtime_seconds=time.perf_counter()-start,full_fei='OPEN',continuum='Initial old net debit D is any real>=the exact reported threshold; credit shifts by D through every original source allocation and no donor is renewed.')
save('PREFIX_VALIDATION.json',result);print(json.dumps(result))
