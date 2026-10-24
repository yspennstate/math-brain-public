from probe import Q
import numpy as np
V=np.array([[1,1],[1,-1]])/np.sqrt(2)
best=[(1e9,None) for _ in range(4)]
for r in np.r_[np.linspace(0,.99,150),1-10.**np.linspace(-3,-8,30)]:
 for s in np.r_[np.linspace(0,.99,150),1-10.**np.linspace(-3,-8,30)]:
  q=Q(r,s);T=-q[:2,2:]/2;H=V.T@(q[:2,:2]-T@T.T)@V
  if r*r+s*s<1e-10:continue
  z=r*r+s*s
  tests=[H[0,0],H[1,1]/z,np.linalg.det(H)/z,H[0,1]**2/H[1,1]]
  for i,t in enumerate(tests):
   if t<best[i][0]:best[i]=(t,(r,s))
print(best)
