import numpy as np,json,pathlib,time
rng=np.random.default_rng(7191);checks=[];start=time.time()
for n in [2,4]:
 for _ in range(5):
  mats=[(rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)))/np.sqrt(2*n) for i in range(3)]
  a,h,b=mats;lam=1/128
  T=np.eye(n*n)+lam*np.kron(b.T,a)
  vecerr=float(np.linalg.norm((h+lam*a@h@b).reshape(-1,order='F')-T@h.reshape(-1,order='F')))
  lower=1-lam*np.linalg.norm(a,2)*np.linalg.norm(b,2)
  sv=float(np.linalg.svd(T,compute_uv=False)[-1]);cov=float(np.linalg.eigvalsh(T@T.conj().T-np.eye(n*n)/4)[0])
  assert vecerr<1e-12 and sv>=lower-1e-12 and cov>=-1e-12
  checks.append({'n':n,'vectorization_error':vecerr,'singular_value':sv,'deterministic_lower_bound':float(lower),'covariance_remainder_min_eigenvalue':cov})
d={'seed':7191,'seconds':time.time()-start,'checks':checks}
pathlib.Path('covariance_checks.json').write_text(json.dumps(d,indent=2));print('covariance checks passed:',len(checks),'seconds:',d['seconds'])
