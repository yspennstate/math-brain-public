import itertools, json
import numpy as np
rng=np.random.default_rng(17017)
def law(Q, inds):
 k=len(inds)
 return np.array([abs(np.linalg.det(Q[np.ix_(s,inds)]))**2 for s in itertools.combinations(range(len(Q)),k)]) if k else np.ones(1)
def H(x):
 x=x[x>1e-15];return -sum(x*np.log(x))
records=[]
for n,r in [(4,1),(5,1),(6,2),(8,3),(10,4)]:
 best=(1e9,None)
 beststar=1e9
 for j in range(80):
  Z=rng.normal(size=(n,n))
  if j%2: Z=Z+1j*rng.normal(size=(n,n))
  Q=np.linalg.qr(Z)[0]
  a=law(Q,list(range(r)));c=law(Q,list(range(r+1)))
  d=law(Q,list(range(r))+[r+1]);b=law(Q,list(range(r+2)))
  beta=H(c)+H(d)-H(a)-H(b)
  betastar=2*H((c+d)/2)-H(a)-H(b)
  if beta<best[0]:best=beta,Q
  beststar=min(beststar,betastar)
 records.append(dict(n=n,r=r,min_beta=best[0],min_beta_star=beststar))
 np.save(f'computations/X017/best_n{n}.npy',best[1])
print(json.dumps(records,indent=2))
