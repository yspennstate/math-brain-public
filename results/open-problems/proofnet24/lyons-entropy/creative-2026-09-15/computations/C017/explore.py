import numpy as np
from itertools import combinations

def info(K):
 n=3; L=np.linalg.solve(np.eye(n)-K,K)
 pair={ (i,j):-np.log1p(-L[i,j]**2/(L[i,i]*L[j,j])) for i,j in combinations(range(n),2)}
 tau=sum(np.log1p(-L[i,j]**2/(L[i,i]*L[j,j])) for i,j in combinations(range(n),2))-np.linalg.slogdet(L)[1]+sum(np.log(np.diag(L)))
 M=np.diag([pair[(1,2)],pair[(0,2)],pair[(0,1)]])+tau*K
 de=np.linalg.det(M)
 Sigma=-K*K; np.fill_diagonal(Sigma,np.diag(K)*(1-np.diag(K)))
 d=np.diag(M)
 val=d@np.linalg.solve(M*M+de*Sigma,d)
 return val,tau,M
rng=np.random.default_rng(42)
minval=3; worst=None
for it in range(100000):
 D=1/(1+np.exp(rng.uniform(-14,14,3)))
 w=rng.dirichlet(np.ones(3)*.3)
 frac=1/(1+np.exp(rng.uniform(-18,18)))
 r=w*(1-D)*frac
 K=np.diag(D)+np.sqrt(np.outer(r,r))
 try: v,t,M=info(K)
 except Exception: continue
 if v<minval:
  minval=v; worst=(D,r,K,t,M)
 if v < 1.99:
  print('fail',v,repr(D),repr(r));break
print('min',minval)
print(worst)
