import numpy as np
from explore import T,weights,bits
from itertools import product

def js(a,b,r,s):
 u=np.array([(1-a)**2-r,2*(a*(1-a)+r),a*a-r]);v=np.array([(1-b)**2-s,2*(b*(1-b)+s),b*b-s]);w=np.array([-1,2,-1])
 def cv(u,v):
  A=u[1]*v[1];B=u[2]*v[0]+u[0]*v[2]
  return np.array([u[0]*v[0],u[1]*v[0]+u[0]*v[1],A/2+B,A/2,u[1]*v[2]+u[2]*v[1],u[2]*v[2]])
 p=cv(u,v);g=np.array([cv(w,v),cv(u,w)]).T;acc=cv(w,w)
 J=g.T@(g/p[:,None]); c=acc@np.log(p/weights)
 M=J+np.array([[0,c],[c,0]])
 return -(g.T@np.log(p/weights)),M,c
rng=np.random.default_rng(9);worst=(1,None);minc=(1,None)
for k in range(10000):
 a,b=rng.uniform(.001,.999,2);r,s=rng.random(2)*np.minimum([a,b],1-np.array([a,b]))**2
 g,M,c=js(a,b,r,s);m=np.linalg.eigvalsh(M)[0]
 if m<worst[0]:worst=(m,[a,b,r,s,g.tolist(),M.tolist(),c])
 if c<minc[0]:minc=(c,[a,b,r,s])
print(worst);print(minc)
