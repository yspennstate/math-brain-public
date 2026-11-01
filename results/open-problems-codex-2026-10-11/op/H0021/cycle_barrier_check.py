import pathlib,itertools,math,json,time,collections
st=time.time();out={}
for n in [7,8,9]:
 path=[0,*range(2,n-4),1];edges=list(zip(path,path[1:]));edges += [(0,n-4),(0,n-3),(1,n-2),(1,n-1)]
 assert len(edges)==n-1
 cnt=collections.Counter()
 for perm in itertools.permutations(range(n)):
  F=[(u,v) for u,v in edges if abs(perm[u]-perm[v]) not in [1,n-1]]
  h=len(F);assert h>=2
  assert any(0 in e for e in F) and any(1 in e for e in F)
  cnt[h]+=1
 for h,z in cnt.items():
  upper=9*n*math.comb(n-1,h-2)*math.factorial(h+1)*2**(h+1)
  assert z<=upper
 out[str(n)]={'mapping_counts_by_noncycle_edges':dict(sorted(cnt.items())),'total_mappings':sum(cnt.values()),'all_bounds_passed':True}
out['asymptotic_log_bounds']=[]
for L in [20.,100.,1000.,10000.,1e6]:
 eta=.25;d=.5;ell=math.log(L);K=math.floor((1-eta)*L/ell)
 logbound=math.log(18)+4*math.log(K)+K*math.log(2*d*L)-L
 out['asymptotic_log_bounds'].append({'log_n':L,'K':K,'d':d,'eta':eta,'log_upper_bound':logbound})
out['elapsed_seconds']=time.time()-st
pathlib.Path('cycle_barrier_results.json').write_text(json.dumps(out,indent=2),encoding='utf8');print(json.dumps(out,indent=2))
