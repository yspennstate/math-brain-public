from probe import Q
import numpy as np
m1=(1e9,None);m2=(1e9,None)
for r in np.r_[np.linspace(0,.95,55),1-10.**np.linspace(-2,-8,20)]:
 for s in np.r_[np.linspace(0,.95,55),1-10.**np.linspace(-2,-8,20)]:
  q=Q(r,s);c=q[2:,2:];b=q[:2,2:];a=q[:2,:2]
  ev=np.linalg.eigvalsh(c-4*np.eye(2))[0]
  if ev<m1[0]:m1=(ev,(r,s))
  ev=np.linalg.eigvalsh(a-b@b.T/4)[0]
  if ev<m2[0]:m2=(ev,(r,s))
print('lower block minus4',m1,'crude Schur',m2)
