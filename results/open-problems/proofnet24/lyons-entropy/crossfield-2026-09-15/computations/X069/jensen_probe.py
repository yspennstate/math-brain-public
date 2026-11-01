from probe import Q
import numpy as np
nodes,weights=np.polynomial.legendre.leggauss(300);nodes=(nodes+1)/2;weights=weights/2
best=(1e99,None)
for r in np.linspace(0,.998,30):
 for s in np.linspace(0,.998,30):
  x=r*r;y=s*s;t=nodes
  R=r/(1-x*t*t);S=s/(1-y*t*t);D=r*s/(1-x*y*t*t)
  k=t*(x/(1-x*t*t)+y/(1-y*t*t)-x*y/(1-x*y*t*t))
  T=np.stack([R+s*D,S-s*k,R-r*k,S+r*D],axis=1).reshape(-1,2,2)
  I=np.einsum('n,nij,nkj->ik',weights,T,T)
  H=Q(r,s)[:2,:2]-I
  ev=np.linalg.eigvalsh(H)[0]
  if ev<best[0]:best=ev,(r,s)
print(best)
