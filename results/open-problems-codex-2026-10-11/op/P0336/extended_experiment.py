import numpy as np, scipy.optimize, pathlib,json,time
rng=np.random.default_rng(1336);out=[];start=time.time()
for n,reps in [(1000,8),(3000,8),(5000,4)]:
 for rep in range(reps):
  a=rng.random((n,2));b=rng.random((n,2));b[:,0]+=2
  d=b[None,:,0]-a[:,None,0];h=b[None,:,1]-a[:,None,1]
  r=np.hypot(d,h);r+=d;np.square(h,out=h);h/=r;del d,r
  i,j=scipy.optimize.linear_sum_assignment(h);opt=float(np.mean(h[i,j]));del h
  ia=np.argsort(a[:,1]);ib=np.argsort(b[:,1]);rank=np.empty(n,dtype=int);rank[ia]=ib
  dd=b[rank,0]-a[:,0];hh=b[rank,1]-a[:,1];rankcost=np.mean(hh*hh/(np.hypot(dd,hh)+dd))
  marks=np.minimum((a[:,0]*4).astype(int),3);targets=np.minimum(((b[j,0]-2)*4).astype(int),3);z=np.minimum((a[:,1]*4).astype(int),3)
  grid=np.zeros((4,4,4),int);np.add.at(grid,(z,marks,targets),1)
  row={'n':n,'rep':rep,'corr':float(np.corrcoef(a[:,0],b[j,0]-2)[0,1]),'corr_rank':float(np.corrcoef(a[:,0],b[rank,0]-2)[0,1]),'horizontal_mse':float(np.mean((b[j,0]-2-a[:,0])**2)),'same_half':float(np.mean((a[:,0]<.5)==(b[j,0]-2<.5))),'rank_same_fraction':float(np.mean(rank==j)),'opt_n_excess':n*opt,'rank_n_excess':float(n*rankcost),'grid':grid.tolist(),'elapsed':time.time()-start}
  out.append(row);pathlib.Path('numerics_extended.json').write_text(json.dumps(out,indent=2)); print(json.dumps({k:v for k,v in row.items() if k!='grid'}),flush=True)
  if time.time()-start>350:break
 if time.time()-start>350:break
