from pathlib import Path
import numpy as np,json
from scipy.sparse.csgraph import shortest_path
rng=np.random.default_rng(257004)
count=0;affected_checked=0
for n in [5,12,25]:
 for trial in range(30):
  w=np.zeros((n,n));i,j=np.triu_indices(n,1);w[i,j]=rng.exponential(n,len(i));w+=w.T
  i,j=rng.choice(n,2,replace=False);W=w[i,j];Wp=rng.exponential(n)
  h=w.copy();h[i,j]=h[j,i]=0 # scipy interprets off-diagonal zero as absent.
  dh=shortest_path(h,directed=False)
  old=shortest_path(w,directed=False);np.fill_diagonal(old,np.inf)
  neww=w.copy();neww[i,j]=neww[j,i]=Wp
  new=shortest_path(neww,directed=False);np.fill_diagonal(new,np.inf)
  for R in [.25,1,3,8]:
   yo=np.minimum(np.sort(old,axis=1)[:,:2],R).mean(1)
   yn=np.minimum(np.sort(new,axis=1)[:,:2],R).mean(1)
   support=(dh[i]<=R)|(dh[j]<=R)
   assert np.max(np.abs(yo[~support]-yn[~support]),initial=0)<1e-9
   bound=R*((dh[i]<=R).sum()+(dh[j]<=R).sum())*(min(W,Wp)<=R)
   assert abs(yo.sum()-yn.sum())<=bound+1e-8
   count+=1;affected_checked+=int(np.count_nonzero(yo!=yn))
out={'edge_resampling_inequality_cases':count,'changed_root_scores':affected_checked,'passed':True}
Path('referee_checks.json').write_text(json.dumps(out,indent=2));print(out)
