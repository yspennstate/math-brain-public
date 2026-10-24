import numpy as np
from itertools import product, permutations
from scipy.optimize import differential_evolution
states=np.array(list(product([0,1],repeat=3)),dtype=float)
perms=list(permutations(range(3)))
P=np.array([np.eye(3)[list(s)] for s in perms])

def output(p,B):
    factors=states*p+(1-states)*(1-p)
    law=np.prod(factors,axis=1)
    signs=2*states-1
    grad=np.array([signs[:,i]*np.prod(np.delete(factors,i,1),1) for i in range(3)]).T
    hess=np.zeros((8,3,3))
    for i in range(3):
      for j in range(3):
        if i!=j:
          k=3-i-j
          hess[:,i,j]=signs[:,i]*signs[:,j]*factors[:,k]
    def channel(a):
      z=a.copy()
      z[[4,2,1]]=B@a[[4,2,1]]
      z[[3,5,6]]=B@a[[3,5,6]]
      return z
    y=channel(law); dy=channel(grad); ddy=channel(hess.reshape(8,9)).reshape(8,3,3)
    H=-dy.T@(dy/y[:,None])-np.einsum('s,sij->ij',np.log(y),ddy)
    return H

def obj(z):
   p=z[:3]; nu=np.r_[z[3:],1.]
   nu/=nu.sum();B=np.einsum('s,sij->ij',nu,P)
   return -np.linalg.eigvalsh(output(p,B))[-1]

if __name__=='__main__':
 rng=np.random.default_rng(692026)
 mx=(-1e9,None)
 for i in range(100000):
   p=rng.beta(.35,.35,size=3)
   if np.min(p*(1-p))<1e-12:continue
   nu=rng.dirichlet(np.ones(6)*.15)
   B=np.einsum('s,sij->ij',nu,P)
   H=output(p,B); lam=np.linalg.eigvalsh(H)[-1]
   if lam>mx[0]:mx=(lam,(p,B,np.linalg.eigh(H)[1][:,-1]))
   if lam>1e-7:
     print('positive',lam,p,B,flush=True);break
 print('max',mx,flush=True)
 res=differential_evolution(obj,[(1e-6,1-1e-6)]*3+[(0,10)]*5,maxiter=300,popsize=10,tol=1e-9,polish=True)
 print('DE',res.fun,res.x,flush=True)
