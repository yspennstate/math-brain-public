import numpy as np,json,time,pathlib
start=time.time();results=[]

def greedy(dist):
 n=dist.shape[0];order=np.argsort(dist,axis=None);mr=np.full(n,-1);mb=np.full(n,-1);left=n
 for k in order:
  i,j=divmod(int(k),n)
  if mr[i]<0 and mb[j]<0:
   mr[i]=j;mb[j]=i;left-=1
   if left==0:break
 return mr,mb

# Deterministic chain: exact integer coordinates, all finite blocking pairs checked.
for n in [2,3,5,10,30]:
 R=8*np.arange(n);B=8*np.arange(n)+5;D=np.abs(R[:,None]-B[None,:]);mr,mb=greedy(D)
 lengths=D[np.arange(n),mr]
 blocking=(D<lengths[:,None]) & (D<D[mb,np.arange(n)][None,:])
 expected=np.r_[n-1,np.arange(n-1)]
 assert np.array_equal(mr,expected) and not blocking.any() and lengths[0]==8*n-3
 results.append(dict(kind='chain',n=n,long_edge=int(lengths[0]),alternative_max=5,blocking_pairs=int(blocking.sum())))

# Balanced binomial processes on a flat torus, NOT infinite Poisson processes.
for d in [2,3]:
 n=2048;L=n**(1/d)
 for seed in range(4):
  rng=np.random.default_rng(8100+100*d+seed);R=rng.uniform(0,L,(n,d));B=rng.uniform(0,L,(n,d))
  D=np.zeros((n,n))
  for axis in range(d):
   delta=np.abs(R[:,None,axis]-B[None,:,axis]);delta=np.minimum(delta,L-delta);D+=delta*delta
  np.sqrt(D,out=D);mr,mb=greedy(D);xr=D[np.arange(n),mr];xb=D[mb,np.arange(n)]
  # Check all potential blocking pairs, independent of the greedy selection test.
  assert not ((D<xr[:,None]-1e-12)&(D<xb[None,:]-1e-12)).any()
  for k in [4,8,16]:
   side=L/k;r=side*np.sqrt(d);v=side**d
   ir=np.floor(R/side).astype(int);ib=np.floor(B/side).astype(int)
   cr=np.bincount(np.ravel_multi_index(ir[xr>r].T,(k,)*d),minlength=k**d)
   cb=np.bincount(np.ravel_multi_index(ib[xb>r].T,(k,)*d),minlength=k**d)
   assert not ((cr>0)&(cb>0)).any()
   signed=cr-cb
   assert np.abs(signed).sum()==2*(xr>r).sum()
   results.append(dict(kind='torus',dimension=d,n=n,seed=seed,k=k,r=float(r),volume=float(v),tail=float(np.mean(xr>r)),mean_absolute_charge=float(np.mean(np.abs(signed))),second_moment_per_volume=float(np.mean(signed**2)/v),fourth_moment_per_volume_squared=float(np.mean(signed**4)/v**2)))
  del D
pathlib.Path('experiment_results.json').write_text(json.dumps(dict(elapsed=time.time()-start,results=results),indent=2))
for d in [2,3]:
 for k in [4,8,16]:
  rows=[x for x in results if x['kind']=='torus' and x['dimension']==d and x['k']==k]
  print('d,k,r,tail,M2/V,M4/V2',d,k,rows[0]['r'],*[float(np.mean([x[key] for x in rows])) for key in ['tail','second_moment_per_volume','fourth_moment_per_volume_squared']])
print('elapsed',time.time()-start)
