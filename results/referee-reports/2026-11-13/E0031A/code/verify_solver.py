#!/usr/bin/env python3
import os,time,json,functools,resource
from pathlib import Path
from matching import solve,SCALE,np
import networkx as nx
rng=np.random.default_rng(310013)
counts={'brute_force':0,'networkx_integer':0,'one_dimensional':0,'duplicates':0}
max_real_difference=0.0
for d in [1,2,3,4]:
 for n in [2,4,6,8,10,12]:
  for rep in range(5):
   x=rng.random((n,d));cost,q,partner=solve(x)
   dist=np.sqrt(((x[:,None,:].astype(np.longdouble)-x[None,:,:].astype(np.longdouble))**2).sum(axis=2))
   w=np.floor(dist*SCALE+np.longdouble(.5)).astype(np.int64)
   @functools.lru_cache(None)
   def brute(mask):
    if not mask:return (0,0.0)
    i=(mask&-mask).bit_length()-1;rem=mask^(1<<i);opts=[]
    for j in range(i+1,n):
     if rem&(1<<j):
      a,b=brute(rem^(1<<j));opts.append((a+int(w[i,j]),b+float(dist[i,j])))
    return min(opts)
   qb,_=brute((1<<n)-1)
   assert q==qb,(n,d,q,qb)
   counts['brute_force']+=1
 for n in [16,32,64]:
  for rep in range(3):
   x=rng.random((n,d));cost,q,partner=solve(x)
   dist=np.sqrt(((x[:,None,:].astype(np.longdouble)-x[None,:,:].astype(np.longdouble))**2).sum(axis=2))
   w=np.floor(dist*SCALE+np.longdouble(.5)).astype(np.int64)
   g=nx.Graph();g.add_nodes_from(range(n))
   g.add_weighted_edges_from((i,j,-int(w[i,j])) for i in range(n) for j in range(i+1,n))
   m=nx.max_weight_matching(g,maxcardinality=True)
   assert len(m)==n//2
   assert q==sum(int(w[i,j]) for i,j in m)
   max_real_difference=max(max_real_difference,abs(cost-sum(float(dist[i,j]) for i,j in m)))
   counts['networkx_integer']+=1
for n in [2,8,64,512,2048]:
 for rep in range(3):
  x=rng.random((n,1));cost,q,p=solve(x)
  u=np.sort(x[:,0]);expected=np.sum(u[1::2]-u[::2])
  assert abs(cost-expected)<=n/(2*SCALE)+1e-12
  counts['one_dimensional']+=1
for d in [1,2,3,4]:
 for n in [4,8,32]:
  x=rng.random((n,d));x[-1]=x[-2]
  c1,_,_=solve(x);c2,_,_=solve(x[:-2])
  assert abs(c1-c2)<=n/SCALE+1e-12
  counts['duplicates']+=1
benchmark=[]
for n in [256,1024,2048]:
 x=rng.random((n,3));t=time.monotonic();solve(x);elapsed=time.monotonic()-t
 benchmark.append({'n':n,'seconds':elapsed})
result={'counts':counts,'max_independent_solver_real_cost_difference':max_real_difference,'benchmark':benchmark,'nice':os.getpriority(os.PRIO_PROCESS,0),'max_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'networkx':nx.__version__,'numpy':np.__version__,'note':'Every call also checks integral dual feasibility and complementary slackness on every complete-graph edge.'}
Path('data/verification.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
