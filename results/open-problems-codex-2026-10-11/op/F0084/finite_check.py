"""Finite discrete GS checks. Not an approximation theorem for the continuum."""
import numpy as np, json, pathlib, time
root=pathlib.Path(__file__).resolve().parent
rng=np.random.default_rng(84)
def gs(dist,capacity):
 n,k=dist.shape
 order=np.argsort(dist,axis=1,kind='stable')
 assigned=np.full(n,-1,dtype=int); next_choice=np.zeros(n,dtype=int)
 rounds=0
 while True:
  active=np.flatnonzero((assigned<0)&(next_choice<k))
  if not len(active): break
  proposals=order[active,next_choice[active]]
  next_choice[active]+=1
  for j in np.unique(proposals):
   applicants=np.concatenate((np.flatnonzero(assigned==j),active[proposals==j]))
   applicants=applicants[np.argsort(dist[applicants,j],kind='stable')]
   assigned[applicants[:capacity]]=j
   assigned[applicants[capacity:]]=-1
  rounds+=1
  if rounds>n*k: raise RuntimeError('termination bound violated')
 return assigned,rounds

start=time.time(); results=[]
# 256 sites, 16 centres, capacity 16: conditioned critical finite torus.
grid=np.array([(i/4,j/4) for i in range(16) for j in range(16)])
for trial in range(20):
 centres=rng.random((16,2))*4
 delta=np.abs(grid[:,None,:]-centres[None,:,:]);delta=np.minimum(delta,4-delta)
 dist=np.sqrt((delta*delta).sum(axis=2))
 a,rounds=gs(dist,16); b,_=gs(dist,15)
 def distances(assign):
  z=np.full(len(assign),np.inf); valid=assign>=0
  z[valid]=dist[np.flatnonzero(valid),assign[valid]];return z
 da,db=distances(a),distances(b)
 assert np.all(da<=db+1e-12)
 # Capacity-volume obstruction: fewer than 16 sites at least as near to
 # the nearest centre as this site means assignment must be nearest.
 nearest=np.argmin(dist,axis=1)
 count=np.array([np.count_nonzero(dist[:,j]<=dist[i,j]) for i,j in enumerate(nearest)])
 small=count<16
 assert np.all(a[small]==nearest[small])
 # Check stability directly for every site/centre pair in both runs.
 for assign,cap in [(a,16),(b,15)]:
  ds=distances(assign)
  for j in range(16):
   held=np.flatnonzero(assign==j)
   covets=np.ones(256,dtype=bool) if len(held)<cap else dist[:,j]<dist[held,j].max()-1e-12
   desires=dist[:,j]<ds-1e-12
   assert not np.any(covets&desires)
 assert np.count_nonzero(b<0)==16
 results.append({'trial':trial,'rounds':rounds,'short_nearest_sites':int(small.sum()),'max_critical_distance':float(da.max())})
out={'model':'finite periodic discrete sites; fixed number of random centres, not infinite Poisson–Lebesgue', 'seed':84,'trials':20,'sites':256,'centres':16,'critical_capacity':16,'subcritical_capacity':15,'max_matrix_bytes':int(dist.nbytes),'elapsed_seconds':time.time()-start,'checks':'all pair stability; monotonic appetite; missing mass; small-ball nearest assignment','results':results}
(root/'finite_results.json').write_text(json.dumps(out,indent=2))
print(json.dumps({k:v for k,v in out.items() if k!='results'},indent=2))
