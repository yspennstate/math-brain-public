import numpy as np, scipy.linalg as la, json, pathlib
out={'discrete':[],'morse':[]}
for d in [1,2,4,8,16,32,64,128,256,512,1024]:
 i=np.arange(1,d+1,dtype=float)
 ev=la.eigh_tridiagonal(i,-0.5*np.sqrt(i[:-1]*i[1:]),select='i',select_range=(0,0))[0][0]
 assert ev>=1/(2*d)-1e-10
 out['discrete'].append({'d':d,'weighted_cov_min_eigenvalue':float(ev),'d_times_eigenvalue':float(d*ev),'proved_lower_bound':1/(2*d)})
for a in [0.4,1.0,1.5,2.0,6.0,20.0]:
 left,right,N=-6.,100.,10000
 grid=np.linspace(left,right,N+2)[1:-1]; dx=(right-left)/(N+1)
 y=2*np.exp(-grid)
 potential=(a-y)**2/4-y/2
 vals=la.eigh_tridiagonal(2/dx**2+potential,np.full(N-1,-1/dx**2),select='i',select_range=(0,1))[0]
 k=a*a/4 if a<=1 else (a/8 if a<=2 else a-1)
 out['morse'].append({'a':a,'finite_difference_eigenvalues':vals.tolist(),'gap_estimate':float(vals[1]-vals[0]),'proved_gap_bound':k,'dx':dx})
# Random pointwise stationary-current cancellation and discrete inequality tests.
rng=np.random.default_rng(110)
maxres=0.; maxratio=0.
for d in [1,2,5,16,64]:
 R=np.eye(d)-np.eye(d,k=-1); G=(R+R.T)/2; K=(R-R.T)/2
 for _ in range(100):
  mu=-rng.uniform(.2,2,d); M=-np.cumsum(mu); x=rng.uniform(-3,3,d)
  h=np.exp(-x)-M; b=mu+R@np.exp(-x)
  maxres=max(maxres,float(np.max(abs(b-R@h))),abs(float(h@K@h)))
  v=rng.normal(size=d);ratio=sum(v*v/np.arange(1,d+1))/(2*d*float(v@G@v))
  maxratio=max(maxratio,float(ratio));assert ratio<=1+1e-10
out['stationarity_max_residual']=maxres;out['max_random_discrete_ratio']=maxratio
pathlib.Path('checks.json').write_text(json.dumps(out,indent=2),encoding='utf8')
print(json.dumps(out,indent=2))
