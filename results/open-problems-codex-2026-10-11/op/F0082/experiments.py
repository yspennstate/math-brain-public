import numpy as np,json,time,math
from scipy.optimize import linear_sum_assignment
from scipy.spatial.distance import cdist
rng=np.random.default_rng(82011)
results=[]
def cross(a,b,c,d):
 def o(p,q,r):return (q[0]-p[0])*(r[1]-p[1])-(q[1]-p[1])*(r[0]-p[0])
 return o(a,b,c)*o(a,b,d)<0 and o(c,d,a)*o(c,d,b)<0
for L in [4,8,16,32]:
 start=time.time(); lens=[]; unmatched=0; nr=0; nb=0; crossings=0; checks=0
 for rep in range(16):
  r=rng.random((rng.poisson(L*L),2))*L;b=rng.random((rng.poisson(L*L),2))*L
  i,j=linear_sum_assignment(cdist(r,b));length=np.linalg.norm(r[i]-b[j],axis=1);lens.extend(length.tolist());nr+=len(r);nb+=len(b);unmatched+=len(r)+len(b)-2*len(i)
  # All pairs in first two samples; at most about 1 million at L=32.
  if rep<2:
   for k in range(len(i)):
    for m in range(k):checks+=1;crossings+=cross(r[i[k]],b[j[k]],r[i[m]],b[j[m]])
 row={'L':L,'replicates':16,'red_points':nr,'blue_points':nb,'unmatched_total_intensity':unmatched/(16*L*L),'bound_sqrt2_over_L':math.sqrt(2)/L,'length_mean':float(np.mean(lens)),'length_quantiles':dict(zip(['50%','90%','99%'],np.quantile(lens,[.5,.9,.99]).tolist())),'tail_2':float(np.mean(np.array(lens)>2)),'tail_4':float(np.mean(np.array(lens)>4)),'crossing_pairs_checked':checks,'proper_crossings':int(crossings),'seconds':time.time()-start};results.append(row);print(row,flush=True)
r=np.array([[-.1,0],[0,-10.]]);b=np.array([[.1,0],[0,10.]])
D=cdist(r,b);i,j=linear_sum_assignment(np.minimum(D,1));counter={'distance_matrix':D.tolist(),'capped_optimal_pairs':list(zip(i.tolist(),j.tolist())),'capped_original':float(min(D[0,0],1)+min(D[1,1],1)),'capped_swap':float(min(D[0,1],1)+min(D[1,0],1)),'crossing':bool(cross(r[0],b[0],r[1],b[1]))};print(counter)
json.dump({'seed':82011,'finite_box':results,'capped_counterexample':counter},open('experiments.json','w'),indent=2)

