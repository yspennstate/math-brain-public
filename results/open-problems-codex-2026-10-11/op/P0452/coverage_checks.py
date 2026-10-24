import json,numpy as np
from collections import deque
from pathlib import Path
from scipy.special import zeta,gammainc
rng=np.random.default_rng(4522027);out={'seed':4522027,'coverage':[]}
n=1536
for rep in range(3):
 A=rng.exponential(n,size=(n,n));W=np.triu(A,1);W+=W.T;np.fill_diagonal(W,np.inf);del A
 D=np.full(n,3);pref=np.zeros((n,n),dtype=bool)
 for i in range(n):pref[i,np.argpartition(W[i],2)[:3]]=True
 base=pref&pref.T
 for t in [2.,4.,6.,8.]:
  H=W<=t;degree=np.sum(H,axis=1);active=D>degree;G=base&H
  adj=[np.flatnonzero(G[i]).tolist() for i in range(n)]
  labels=np.full(n,-1);sz=[]
  for root in range(n):
   if labels[root]>=0:continue
   todo=[root];labels[root]=len(sz)
   for v in todo:
    for u in adj[v]:
     if labels[u]<0:labels[u]=len(sz);todo.append(u)
   sz.append(len(todo))
  sizes=np.array(sz);large=sizes[labels]>=32;largest=int(np.argmax(sizes));giant=labels==largest
  low=degree<=12;dist=np.full(n,100000)
  starts=np.flatnonzero(active&low);dist[starts]=0;q=deque(starts)
  while q:
   v=q.popleft()
   for u in adj[v]:
    if low[u] and dist[u]>dist[v]+1:dist[u]=dist[v]+1;q.append(u)
  row={'rep':rep,'t':t,'largest_fraction':float(np.mean(giant)),'large_mass':float(np.mean(large)),'active_fraction':float(np.mean(active)),'active_in_largest':int(np.sum(active&giant)),
       'uncovered_large_mass':{str(R):float(np.mean(large&(dist>R))) for R in [0,1,2,4,8,16]}}
  assert all(row['uncovered_large_mass'][str(R)]>=row['uncovered_large_mass'][str(R2)] for R,R2 in zip([0,1,2,4,8],[1,2,4,8,16]))
  out['coverage'].append(row)
 Path('coverage_checks.json').write_text(json.dumps(out,indent=2));print('coverage graph',rep,'done',flush=True)
# Explicit finite-mean/infinite-variance law D=2+Y, P(Y=j)=j^-2.5/zeta(2.5).
const=zeta(2.5,1);total=1+zeta(1.5,1)/const;heavy=[]
for B in [4,8,16,32,64]:
 a=.1;b=2*B;ys=np.arange(1,B);ds=ys+2;weights=ys.astype(float)**(-2.5)/const
 tail=(zeta(1.5,B)+zeta(2.5,B))/const
 bad_threshold=np.sum((ds-1)*weights*(gammainc(ds,a)+1-gammainc(ds,b)))
 eps=float(tail+bad_threshold)
 heavy.append({'max_potential':B,'a':a,'b':b,'outside_weighted_mass':eps})
 assert eps<total
out['heavy_tail']={'law':'D=2+Y, P(Y=j)=j^-2.5/zeta(2.5)','mean_potential':float(total),'variance':'infinite','compact_complement':heavy}
assert any(r['outside_weighted_mass']<1 for r in heavy)
Path('coverage_checks.json').write_text(json.dumps(out,indent=2));print('heavy-tail compact contraction checked',flush=True)
