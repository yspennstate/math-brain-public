import numpy as np
from explore import atoms,X,sg,rng

def radial(a,b,c,u,v):
 p=atoms(a,b,c,u,v);m=np.where(X,[a,b,c],1-np.array([a,b,c]))
 p0=np.prod(m,axis=1);p1=p-p0
 d=np.empty((8,3));e=np.zeros((8,3));D2=np.zeros((8,3,3))
 for i in range(3):
  d[:,i]=sg[:,i]*(p+p[np.arange(8)^(1<<i)])
 e[:,0]=-v*np.prod(sg,axis=1);e[:,2]=-u*np.prod(sg,axis=1)
 for i in range(3):
  for j in range(3):
   if i!=j:D2[:,i,j]=sg[:,i]*sg[:,j]*m[:,3-i-j]
 P=(e[:,:,None]*d[:,None,:]+d[:,:,None]*e[:,None,:])/p[:,None,None]-(d[:,:,None]*d[:,None,:])*p1[:,None,None]/p[:,None,None]**2+D2*p1[:,None,None]/p[:,None,None]
 return P
if __name__=='__main__':
 worst=[1e9,1e9];arg=[None,None]
 for it in range(5000):
  a,b,c=rng.uniform(.01,.99,3);u,v=rng.uniform(0,1,2)
  cap=min(b/(u/a+v/c),(1-b)/(u/(1-a)+v/(1-c)))
  u*=cap*rng.uniform(.001,.9999);v*=cap*rng.uniform(.001,.9999)
  P=radial(a,b,c,u,v)
  for side in [0,1]:
   val=np.linalg.eigvalsh(P[X[:,1]==side].sum(axis=0))[0]
   if val<worst[side]:worst[side]=val;arg[side]=[a,b,c,u,v]
 print(worst,arg)
