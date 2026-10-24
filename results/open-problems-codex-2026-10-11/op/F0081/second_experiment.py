import numpy as np,json,time
from pathlib import Path
rng=np.random.default_rng(882)
def matching(R,B,L=None):
 if not len(R) or not len(B):return np.full(len(R),np.inf),np.full(len(B),np.inf)
 z=np.abs(R[:,None]-B[None,:]);z=np.minimum(z,L-z) if L else z;D=np.linalg.norm(z,axis=2)
 a=np.full(len(R),np.inf);b=np.full(len(B),np.inf)
 for k in np.argsort(D,axis=None):
  i,j=divmod(int(k),len(B))
  if np.isinf(a[i]) and np.isinf(b[j]):a[i]=b[j]=D[i,j]
 return a,b
start=time.time();records=[];total=0
# Check the entire signed survivor-measure change, not just total charge.
for d in [1,2,3]:
 for n in range(1,16):
  for trial in range(100):
   R=rng.uniform(0,5,(n,d));B=rng.uniform(0,5,(rng.integers(1,17),d));Z=rng.uniform(0,5,(1,d))
   a,b=matching(R,B);aa,bb=matching(np.vstack([R,Z]),B)
   assert (aa[:n]>=a-1e-12).all() and (bb<=b+1e-12).all()
   finite=np.unique(np.r_[a[np.isfinite(a)],b[np.isfinite(b)],aa[np.isfinite(aa)],bb[np.isfinite(bb)]])
   ts=np.r_[0,(finite[:-1]+finite[1:])/2,finite[-1]+1]
   for t in ts:
    newreds=(aa[:n]>t).astype(int)-(a>t).astype(int)
    removedblues=(b>t).astype(int)-(bb>t).astype(int)
    assert (newreds>=0).all() and (removedblues>=0).all()
    assert int(newreds.sum()+removedblues.sum()+(aa[-1]>t))==1
   total+=1
# Independent Poisson counts on a torus (including unmatched points at infinity).
for d in [2,3]:
 L=6.;v=L**d;replicates=350;side=2.;cubev=side**d;r=side*np.sqrt(d)
 charges=[];absolute=[]
 for trial in range(replicates):
  R=rng.uniform(0,L,(rng.poisson(v),d));B=rng.uniform(0,L,(rng.poisson(v),d));a,b=matching(R,B,L)
  nr=int(((R<side).all(axis=1)&(a>r)).sum());nb=int(((B<side).all(axis=1)&(b>r)).sum())
  assert nr==0 or nb==0
  charges.append(nr-nb);absolute.append(nr+nb)
 records.append(dict(d=d,L=L,replicates=replicates,side=side,r=float(r),volume=cubev,mean=float(np.mean(charges)),second_moment=float(np.mean(np.array(charges)**2)),variance_bound=2*cubev,mean_absolute=float(np.mean(absolute)),charges=charges))
Path('second_experiments.json').write_text(json.dumps(dict(insertion_cases=total,records=records,elapsed=time.time()-start),indent=2))
print('Insertion one-atom assertions passed:',total)
for x in records: print({k:v for k,v in x.items() if k!='charges'})
print('elapsed',time.time()-start)
