import numpy as np
from explore_general import calc
rng=np.random.default_rng(322)
best=(-1,None)
for j in range(200000):
 if j<60000:
  lp=np.clip(rng.beta(.3,.3),1e-5,1-1e-5); lt=np.clip(rng.beta(.3,.3),1e-5,1-1e-5)
  a=(lp+2*lt)/3;b=(lp-lt)/3
  K=np.eye(3)*(a-b)+b*np.ones((3,3))
 else:
  Z=rng.normal(size=(3,3))+1j*rng.normal(size=(3,3))
  Q,_=np.linalg.qr(Z)
  lam=np.clip(rng.beta(.3,.3,3),1e-5,1-1e-5)
  K=(Q*lam)@Q.conj().T
 try:o=calc(K)
 except np.linalg.LinAlgError:continue
 if o is None: continue
 if o[-1]>best[0]: best=(o[-1],K)
 if o[-1]>1.001:
  print('FAIL',o[-1],repr(K),o[:4]);break
else:print('PASS')
print('best',best)
