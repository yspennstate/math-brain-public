from pathlib import Path
import numpy as np,json
from scipy.spatial.distance import cdist
rng=np.random.default_rng(257625)
out=[];max_indegree=0;max_delta=0
def score(p,R):
 d=cdist(p,p);np.fill_diagonal(d,np.inf)
 ind=np.argsort(d,axis=1)[:,:2]
 s=np.take_along_axis(d,ind,axis=1)
 return d,s,np.minimum(s,R).mean(axis=1),ind
for n,reps in [(50,100),(150,50),(400,20)]:
 vals=[];lens=[]
 for _ in range(reps):
  p=rng.random((n,2))*np.sqrt(n)
  d,s,y,ind=score(p,2)
  deg=np.bincount(ind.ravel(),minlength=n);max_indegree=max(max_indegree,int(deg.max()));assert deg.max()<=12
  q=p.copy();q[0]=rng.random(2)*np.sqrt(n)
  _,_,new,ii=score(q,2)
  delta=abs(new.sum()-y.sum());max_delta=max(max_delta,delta);assert delta<=25*2+1e-9
  vals.append(s.mean())
  seen=np.zeros(n,bool);cur=0;seen[0]=True;L=0
  for k in range(n-1):
   row=d[cur].copy();row[seen]=np.inf;j=int(row.argmin());L+=row[j];seen[j]=True;cur=j
  assert L+1e-9>=y.sum()-2
  lens.append(L/n)
 out.append({'n':n,'replicates':reps,'score_mean':float(np.mean(vals)),'score_standard_error_across_instances':float(np.std(vals,ddof=1)/np.sqrt(reps)),'limit_score':.625,'nuv_mean':float(np.mean(lens))})
out.append({'checked_max_two_neighbor_indegree':max_indegree,'largest_replacement_score_delta_R2':max_delta,'passed':True})
Path('checks_euclidean.json').write_text(json.dumps(out,indent=2))
for x in out:print(x)
