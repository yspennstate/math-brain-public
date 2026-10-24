from pathlib import Path
import numpy as np,json,time
rng=np.random.default_rng(191);out=[];start=time.time()
def gin(n):return (rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)))/np.sqrt(2*n)
worst=0;cases=0
for n in [1,2,4,8,16]:
 vals={k:[] for k in ['affine_nonlinear','one_variable','commutator','cubic_sum']}
 for rep in range(160):
  x,y,z=gin(n),gin(n),gin(n)
  mats={'affine_nonlinear':x+y@z-z@y,'one_variable':x@x@x-x,'commutator':x@y-y@x,'cubic_sum':x@y@x+y@x@y}
  for k,m in mats.items():vals[k].append(float(np.linalg.svd(m,compute_uv=False)[-1]))
  a=np.linalg.svd(x,compute_uv=False)[-1];b=np.linalg.svd(y,compute_uv=False)[-1]
  prod=np.linalg.svd(x@y,compute_uv=False)[-1];worst=max(worst,float(a*b-prod));cases+=1
  m=mats['affine_nonlinear'];sm=np.linalg.svd(m,compute_uv=False)[-1]
  ds=[]
  for j in range(n):
   others=np.delete(m,j,axis=1)
   residual=m[:,j] if n==1 else m[:,j]-others@np.linalg.lstsq(others,m[:,j],rcond=None)[0]
   ds.append(np.linalg.norm(residual))
  assert min(ds)<=np.sqrt(n)*sm+1e-9
 for k,vs in vals.items():out.append({'n':n,'model':k,'samples':len(vs),'quantiles':np.quantile(vs,[0,.1,.5,.9]).tolist(),'lower_tails':{str(t):float(np.mean(np.array(vs)<=t)) for t in [.001,.01,.1]}})
report={'seed':191,'seconds':time.time()-start,'product_inequality_max_violation':worst,'product_checks':cases,'column_distance_checks':cases,'results':out,'warning':'Finite-size diagnostics only; no proof of a general tail estimate.'}
Path('numerics.json').write_text(json.dumps(report,indent=2));print(json.dumps(report,indent=2))
