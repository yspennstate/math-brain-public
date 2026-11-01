import numpy as np
from scipy.linalg import eigvalsh
from itertools import combinations
rng=np.random.default_rng(532026)
n=4; edges=list(combinations(range(n),2)); masks=np.array([[bool(s>>i&1) for i in range(n)] for s in range(1<<n)],float)
def calc(x,r):
 L=2*r[:,None]*r[None,:]/(x[:,None]+x[None,:]); K=np.linalg.solve(np.eye(n)+L,L)
 ell=r*r/x; cf=np.array([2*np.log((x[i]+x[j])/abs(x[i]-x[j])) for i,j in edges]); C=np.zeros((n,n))
 for c,(i,j) in zip(cf,edges):C[i,j]=C[j,i]=c
 lp=masks@np.log(ell)
 for c,(i,j) in zip(cf,edges):lp-=c*masks[:,i]*masks[:,j]
 p=np.exp(lp-max(lp));p/=p.sum();mu=p@masks;Y=masks-mu
 Q=np.array([Y[:,i]*Y[:,j] for i,j in edges]).T;Q-=p@Q
 S=Y.T@(p[:,None]*Y);T=Y.T@(p[:,None]*Q);V=Q.T@(p[:,None]*Q)
 noise=np.diag([2*K[i,j]**2/c for c,(i,j) in zip(cf,edges)])
 Se=S-T@np.linalg.solve(V+noise,T.T)
 e1=eigvalsh(np.linalg.inv(S)-C)[0];e2=eigvalsh(np.linalg.inv(Se)-C)[0]
 return e1,e2,K,p,C,(S,T,V,noise)
best=None
for it in range(50000):
 x=np.sort(np.exp(rng.uniform(0,3,4)))
 r=np.exp(rng.uniform(-1,6,4))
 e1,e2,*_=calc(x,r)
 if e1<-.2 and e2>.3:
  score=min(-e1,e2)
  if best is None or score>best[0]:
   best=(score,x,r,e1,e2);print(it,best,flush=True)
   if score>3:break
print('best',best)
